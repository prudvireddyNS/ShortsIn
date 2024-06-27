import os
from models import pipe, gemini_pro, generate_speech
# from script_processing import process_script
from video_audio_processing import (
    video_create,
    extract_audio,
    add_text_to_video,
    combine_audio_video,
    concatenate_videos
)
from utils import remove_all_files, process_script, create_directories_if_not_exist
from langchain.chains import LLMChain, SequentialChain
from prompts import prompt1, prompt2

class Shorts:
    def __init__(self) -> None:
        self.llm = gemini_pro
        self.image_generator = pipe
        self.speech_generator = generate_speech
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
    def generate(self, topic):
        script = self.scriptWriter(topic)
        print(script)
        script = process_script(script)
        print('Number of images to be generated: ', len(script['text_for_image_generation']))

        create_directories_if_not_exist(self.base_dir)
        self.ImgGen(script['text_for_image_generation'], os.path.join(self.base_dir, 'outputs/images'))
        self.SpeechGen(script['text_for_speech_generation'], os.path.join(self.base_dir, 'outputs/speech'))
        self.createVideo(os.path.join(self.base_dir, 'outputs/images'), os.path.join(self.base_dir, 'outputs/speech'), script)
        self.combineVideos(os.path.join(self.base_dir, 'outputs/temp_videos/processed_temp_videos'))
        return script

    def scriptWriter(self, topic):
        chain1 = LLMChain(llm=self.llm, prompt=prompt1, output_key='script')
        chain2 = LLMChain(llm=self.llm, prompt=prompt2, output_key='img_des')
        overall_chain = SequentialChain(
            chains=[chain1, chain2],
            input_variables=["topic"],
            output_variables=["script", "img_des"]
        )
        script = overall_chain.invoke(topic)
        print('script generated')
        return script

    def ImgGen(self, script, images_dir):
        print(images_dir)
        remove_all_files(images_dir)
        for i, text in enumerate(script):
            image = self.image_generator(text, num_inference_steps=30, guidance_scale=2, width=720, height=1280, verbose=0).images[0]
            image.save(os.path.join(images_dir, f'image_{i}.jpg'))
        print('images generated')

    def SpeechGen(self, script, speech_dir):
        remove_all_files(speech_dir)
        for i, text in enumerate(script):
            self.speech_generator(text, speech_dir, num=i)
        print('speech generated')

    def createVideo(self, image_dir, speech_dir, script):
        temp_videos_dir = os.path.join(self.base_dir, 'outputs/temp_videos')
        processed_temp_videos_dir = os.path.join(temp_videos_dir, 'processed_temp_videos')
        remove_all_files(temp_videos_dir)
        remove_all_files(processed_temp_videos_dir)
        images = os.listdir(image_dir)
        speeches = os.listdir(speech_dir)
        if len(images) == len(speeches):
            for i in range(len(images)):
                video_create(os.path.join(image_dir, images[i]), os.path.join(speech_dir, speeches[i]), temp_videos_dir, num=i)
                extract_audio(os.path.join(temp_videos_dir, f'video_{i}.mp4'), os.path.join(temp_videos_dir, f'extracted_audio_{i}.mp3'))
                text = script['text_for_speech_generation'][i].upper()
                add_text_to_video(
                    os.path.join(temp_videos_dir, f'video_{i}.mp4'),
                    os.path.join(temp_videos_dir, f'captions_video_{i}.mp4'),
                    text,
                    outline_thickness=2,
                    outline_color=(0, 0, 0),
                    font_path=os.path.join(self.base_dir, 'static/fonts/Montserrat-Bold.ttf')
                )
                combine_audio_video(
                    os.path.join(temp_videos_dir, f'captions_video_{i}.mp4'),
                    os.path.join(temp_videos_dir, f'extracted_audio_{i}.mp3'),
                    os.path.join(processed_temp_videos_dir, f'final_output_video_{i}.mp4')
                )
            print('created temp videos')
        else:
            print('len of images and speeches are not same')

    def combineVideos(self, videos_dir):
        final_video_dir = os.path.join(self.base_dir, 'outputs/final_video')
        remove_all_files(final_video_dir)
        concatenate_videos(videos_dir, final_video_dir)
        print("Combined video from individual videos")
