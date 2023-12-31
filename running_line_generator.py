import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont


def create_scrolling_text_video(text):
    font = ImageFont.truetype("arial.ttf", 32)
    image_width=100 # Width must be 100 according to the technical requirements
    image_height=100 # Height must be 100 according to the technical requirements
    text_color=(255, 255, 255) # Scrolling text color is white as in the example video
    bg_color=(255, 0, 255) # Background color is magenta as in the example video
    # Get size of the input text string
    text_width, text_height = font.getsize(text)
    # Number of frames
    num_frames = text_width + image_width
    # Calculate FPS, knowing that duration must be 3 seconds
    fps = num_frames / 3

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter("my_video.mp4", fourcc, fps, (image_width, image_height))
    # Create frames for text scrolling
    for i in range(num_frames):
        img = Image.new("RGB", (image_width, image_height), bg_color)
        draw = ImageDraw.Draw(img)
        x = image_width - i
        y = (image_height - text_height) // 2

        draw.text((x, y), text, font=font, fill=text_color)
        # Convert the image to an OpenCV frame
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        video_writer.write(frame)

    video_writer.release()


text = "Hey, Igor!"
create_scrolling_text_video(text)
