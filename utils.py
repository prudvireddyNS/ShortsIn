import os
import glob
import re

def remove_all_files(directory):
    files = [f for f in glob.glob(os.path.join(directory, '*')) if os.path.isfile(f)]
    
    if not files:
        print(f"No files to remove in '{directory}'.")
        return
    
    for f in files:
        try:
            os.remove(f)
            # print(f"Removed file: {f}")
        except Exception as e:
            print(f"Failed to delete {f}. Reason: {e}")

def process_script(script):
    title = script['script'].split('\n\n')[0].split(':')[1].strip()
    description = script['script'].split('\n\n')[1].split(':')[1].strip()
    tags = [tag.strip() for tag in script['script'].split('\n\n')[2].split(':')[1].strip().split(',')]
    text_for_image_generation = re.findall(r'<image>(.*?)<image>', script['img_des'])
    text_for_speech_generation = re.findall(r'<sentence>(.*?)<sentence>', script['img_des'])

    script_dict = {
        'title': title,
        'description': description,
        'tags': tags,
        'text_for_image_generation': text_for_image_generation,
        'text_for_speech_generation': text_for_speech_generation
    }
    print('script processed')
    return script_dict

def create_directories_if_not_exist(base_dir):
    directories = [
        os.path.join(base_dir, 'outputs/images'),
        os.path.join(base_dir, 'outputs/speech'),
        os.path.join(base_dir, 'outputs/temp_videos/processed_temp_videos'),
        os.path.join(base_dir, 'outputs/final_video')
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)