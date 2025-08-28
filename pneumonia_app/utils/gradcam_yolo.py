import torch
import cv2
import numpy as np
from utils.ml_models import yolo_model   # ✅ import YOLO11 model từ utils/ml_models

# ---------------------------
# HÀM TẠO GRAD-CAM TỪ YOLO
# ---------------------------
def generate_gradcam_yolo(model, image_path, input_size=640, target_layers=None):
    """
    Sinh Grad-CAM cho YOLO11
    Args:
        model: YOLO11 đã load sẵn (yolo_model)
        image_path: đường dẫn ảnh đầu vào
        input_size: kích thước ảnh (default: 640)
        target_layers: list các tên layer thử lần lượt (default: ["model.24", "model.22", "model.21"])
    """

    if target_layers is None:
        target_layers = ["model.24", "model.22", "model.21", "model.20"]

    # Load ảnh
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"❌ Không load được ảnh từ đường dẫn: {image_path}")

    img_resized = cv2.resize(img, (input_size, input_size))
    img_rgb = cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB)
    img_tensor = torch.from_numpy(img_rgb).float().permute(2, 0, 1).unsqueeze(0) / 255.0

    # ---------------------------
    # TÌM LAYER HỢP LỆ
    # ---------------------------
    model_dict = dict(model.named_modules())
    target_module = None
    used_layer = None
    for layer in target_layers:
        if layer in model_dict:
            target_module = model_dict[layer]
            used_layer = layer
            break

    if target_module is None:
        raise ValueError(f"❌ Không tìm thấy layer nào trong danh sách {target_layers}")

    print(f"✅ Dùng layer: {used_layer}")

    activations = []
    gradients = []

    def forward_hook(module, inp, out):
        activations.append(out)

    def backward_hook(module, grad_in, grad_out):
        gradients.append(grad_out[0])

    # Gắn hook
    forward_handle = target_module.register_forward_hook(forward_hook)
    backward_handle = target_module.register_full_backward_hook(backward_hook)

    # Forward
    preds = model(img_tensor)

    # Lấy loss từ objectness để backprop
    if isinstance(preds, list) or isinstance(preds, tuple):
        loss = preds[0].sum()
    else:
        loss = preds.sum()
    loss.backward()

    # Lấy grad và act
    grads = gradients[0].mean(dim=[2, 3], keepdim=True)
    act = activations[0]

    # Grad-CAM = ReLU(sum(grad * act))
    gradcam = torch.relu((grads * act).sum(dim=1, keepdim=True)).squeeze().detach().cpu().numpy()

    # Chuẩn hóa heatmap
    gradcam = cv2.resize(gradcam, (img.shape[1], img.shape[0]))
    if gradcam.max() > gradcam.min():
        gradcam = (gradcam - gradcam.min()) / (gradcam.max() - gradcam.min() + 1e-8)
    else:
        gradcam = np.zeros_like(gradcam)

    # Overlay lên ảnh gốc
    heatmap = cv2.applyColorMap(np.uint8(255 * gradcam), cv2.COLORMAP_JET)
    overlay = cv2.addWeighted(img, 0.6, heatmap, 0.4, 0)

    # Gỡ hook
    forward_handle.remove()
    backward_handle.remove()

    return overlay, heatmap


# ---------------------------
# DEBUG CẤU TRÚC MÔ HÌNH
# ---------------------------
def debug_model_structure(model):
    print("===== CẤU TRÚC YOLO MODEL =====")
    for name, module in model.named_modules():
        print(name, ":", module)


# ---------------------------
# TEST TRỰC TIẾP
# ---------------------------
if __name__ == "__main__":
    test_image = "uploads/test.jpg"   # đổi ảnh để test
    debug_model_structure(yolo_model)

    overlay, heatmap = generate_gradcam_yolo(yolo_model, test_image)

    cv2.imwrite("gradcam_overlay.jpg", overlay)
    cv2.imwrite("gradcam_heatmap.jpg", heatmap)
    print("✅ Grad-CAM đã lưu ra file.")
