"""
Image processing utilities for pet photos
Handles automatic cropping, resizing, and optimization
"""
from PIL import Image, ImageOps
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


def process_pet_image(image_file, target_size=(800, 800), quality=85):
    """
    Process and optimize pet image with smart cropping
    
    Args:
        image_file: Uploaded image file
        target_size: Tuple of (width, height) for output
        quality: JPEG quality (1-100)
    
    Returns:
        Processed InMemoryUploadedFile
    """
    # Open the image
    img = Image.open(image_file)
    
    # Convert RGBA to RGB if necessary
    if img.mode in ('RGBA', 'LA', 'P'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        img = background
    
    # Auto-orient based on EXIF data
    img = ImageOps.exif_transpose(img)
    
    # Smart crop to square (center crop)
    img = smart_crop_to_square(img)
    
    # Resize to target size
    img = img.resize(target_size, Image.Resampling.LANCZOS)
    
    # Save to BytesIO
    output = BytesIO()
    img.save(output, format='JPEG', quality=quality, optimize=True)
    output.seek(0)
    
    # Create InMemoryUploadedFile
    return InMemoryUploadedFile(
        output,
        'ImageField',
        f"{image_file.name.split('.')[0]}_processed.jpg",
        'image/jpeg',
        sys.getsizeof(output),
        None
    )


def smart_crop_to_square(img):
    """
    Intelligently crop image to square, focusing on center
    
    Args:
        img: PIL Image object
    
    Returns:
        Cropped PIL Image object
    """
    width, height = img.size
    
    if width == height:
        return img
    
    # Determine crop box
    if width > height:
        # Landscape - crop sides
        left = (width - height) // 2
        top = 0
        right = left + height
        bottom = height
    else:
        # Portrait - crop top/bottom
        left = 0
        top = (height - width) // 2
        right = width
        bottom = top + width
    
    return img.crop((left, top, right, bottom))


def create_thumbnail(image_file, size=(200, 200)):
    """
    Create a thumbnail version of the image
    
    Args:
        image_file: Uploaded image file
        size: Tuple of (width, height) for thumbnail
    
    Returns:
        Processed InMemoryUploadedFile
    """
    return process_pet_image(image_file, target_size=size, quality=80)


def validate_image(image_file, max_size_mb=5):
    """
    Validate uploaded image
    
    Args:
        image_file: Uploaded image file
        max_size_mb: Maximum file size in MB
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check file size
    if image_file.size > max_size_mb * 1024 * 1024:
        return False, f"Image size must be less than {max_size_mb}MB"
    
    # Check if it's a valid image
    try:
        img = Image.open(image_file)
        img.verify()
        return True, None
    except Exception as e:
        return False, "Invalid image file"


def get_image_info(image_file):
    """
    Get information about an image
    
    Args:
        image_file: Uploaded image file
    
    Returns:
        Dictionary with image info
    """
    try:
        img = Image.open(image_file)
        return {
            'width': img.width,
            'height': img.height,
            'format': img.format,
            'mode': img.mode,
            'size_kb': image_file.size / 1024
        }
    except Exception as e:
        return None
