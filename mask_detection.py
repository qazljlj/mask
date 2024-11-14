from PIL import Image
import numpy as np

def is_mask_image(image_path):
    # 打开图像
    image = Image.open(image_path)
    
    # 如果图像有alpha通道，检查透明度
    if image.mode == 'RGBA':
        alpha = np.array(image.split()[-1])
        # 检查是否存在透明和不透明的区域
        if np.any(alpha == 0) and np.any(alpha == 255):
            return True
    
    # 转换为灰度模式
    gray_image = image.convert('L')
    image_array = np.array(gray_image)

    # 统计颜色分布
    unique_values, counts = np.unique(image_array, return_counts=True)

    # 检查颜色集中在某个范围内
    if len(unique_values) < 10 or (np.max(unique_values) - np.min(unique_values) < 50):
        return True

    return False

# 示例使用
image_path = 'mask.png'
if is_mask_image(image_path):
    print("这可能是一张蒙版图片。")
else:
    print("这不是一张蒙版图片。")
