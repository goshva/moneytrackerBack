import os
import cv2

def rotate_images_in_folder(folder_path):
    img_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    
    for file in os.listdir(folder_path):
        ext = os.path.splitext(file)[1].lower()
        if ext in img_extensions:
            img_path = os.path.join(folder_path, file)
            img = cv2.imread(img_path)
            
            # Determine if the image is vertical
            height, width = img.shape[:2]
            print(height, width, height > width)

            if height > width:
                print('rotate')
                # Rotate the image by 90 degrees counter-clockwise
                rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
                
                # Save the rotated image back to the original path
                cv2.imwrite(img_path, rotated_img)

# Specify the path to the folder containing the images
folder_path = './tests'

# Call the function to rotate all vertical images in the specified folder
rotate_images_in_folder(folder_path)