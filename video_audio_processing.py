import os
import subprocess
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from moviepy.editor import VideoFileClip

def video_create(image, audio, output_dir, num):
    try:
        ffmpeg_command = [
            'ffmpeg',
            '-loop', '1',
            '-i', image,
            '-i', audio,
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-shortest',
            os.path.join(output_dir, f'video_{num}.mp4')
        ]
        result = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg command failed with error code {e.returncode}:")

def concatenate_videos(video_dir, output_dir):
    video_list = [os.path.join(video_dir, video) for video in os.listdir(video_dir) if video.endswith('.mp4')]

    try:
        inputs = []
        filter_complex = ''
        
        for i, video in enumerate(video_list):
            inputs.extend(['-i', video])
            filter_complex += f'[{i}:v:0] [{i}:a:0] '
        
        filter_complex += f'concat=n={len(video_list)}:v=1:a=1 [v] [a]'
        
        ffmpeg_command = [
            'ffmpeg',
            *inputs,
            '-filter_complex', filter_complex,
            '-map', '[v]',
            '-map', '[a]',
            os.path.join(output_dir, 'video.mp4')
        ]
        
        subprocess.run(ffmpeg_command, check=True, text=True)
        # print(f"Videos {video_list} have been successfully concatenated to './outputs/final_video/video.mp4'.")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg command failed with error code {e.returncode}:")
        print(e.stderr)

def extract_audio(input_video, output_audio):
    try:
        ffmpeg_command = [
            'ffmpeg',
            '-i', input_video,
            '-q:a', '0',
            '-map', 'a',
            output_audio
        ]
        result = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg command failed with error code {e.returncode}:")

def split_text_into_chunks(text, chunk_size):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def add_text_to_video(input_video, output_video, text, duration=1, fontsize=40, fontcolor=(255, 255, 255),
                      outline_thickness=2, outline_color=(0, 0, 0),
                      font_path='C:\\Users\\prudh\\Downloads\\montserrat\\Montserrat\\Montserrat-Bold.ttf'):
    
    # Split text into chunks
    chunks = split_text_into_chunks(text, 3)  # Adjust chunk size as needed

    # Open the input video
    cap = cv2.VideoCapture(input_video)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    chunk_duration_frames = duration * fps

    # Load font
    font = ImageFont.truetype(font_path, fontsize)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to PIL image
        frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(frame_pil)

        # Calculate the current chunk index based on the frame number
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        chunk_index = current_frame // chunk_duration_frames

        # Ensure chunk_index is within the range of available chunks
        if chunk_index < len(chunks):
            # Get the current chunk of text
            chunk = chunks[chunk_index]

            # Calculate text size
            text_width, text_height = draw.textsize(chunk, font=font)

            # Calculate text position
            text_x = (width - text_width) // 2
            text_y = height - 300  # Position text at the bottom

            # Check if the text exceeds the frame width
            if text_width > width:
                # Split the text into two lines
                words = chunk.split()
                half = len(words) // 2
                line1 = ' '.join(words[:half])
                line2 = ' '.join(words[half:])

                # Calculate text size for each line
                text_size_line1 = draw.textsize(line1, font=font)
                text_size_line2 = draw.textsize(line2, font=font)

                # Calculate text position for each line
                text_x_line1 = (width - text_size_line1[0]) // 2
                text_x_line2 = (width - text_size_line2[0]) // 2
                text_y = height - 250 - text_size_line1[1]  # Adjust vertical position for two lines

                # Draw outline and text for both lines
                for dx in range(-outline_thickness, outline_thickness + 1):
                    for dy in range(-outline_thickness, outline_thickness + 1):
                        if dx != 0 or dy != 0:
                            draw.text((text_x_line1 + dx, text_y + dy), line1, font=font, fill=outline_color)
                            draw.text((text_x_line2 + dx, text_y + text_size_line1[1] + dy), line2, font=font, fill=outline_color)
                
                draw.text((text_x_line1, text_y), line1, font=font, fill=fontcolor)
                draw.text((text_x_line2, text_y + text_size_line1[1]), line2, font=font, fill=fontcolor)

            else:
                # Draw outline and text for single line
                for dx in range(-outline_thickness, outline_thickness + 1):
                    for dy in range(-outline_thickness, outline_thickness + 1):
                        if dx != 0 or dy != 0:
                            draw.text((text_x + dx, text_y + dy), chunk, font=font, fill=outline_color)
                
                draw.text((text_x, text_y), chunk, font=font, fill=fontcolor)

            # Convert back to OpenCV frame
            frame = cv2.cvtColor(np.array(frame_pil), cv2.COLOR_RGB2BGR)

        # Write the frame with text to the output video
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

def combine_audio_video(video_path, audio_path, output_path):
    try:
        ffmpeg_command = [
            'ffmpeg',
            '-i', video_path,
            '-i', audio_path,
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-b:a', '192k',
            output_path
        ]
        result = subprocess.run(ffmpeg_command, check=True, capture_output=True, text=True)
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg command failed with error code {e.returncode}:")
