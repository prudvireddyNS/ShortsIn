from diffusers import DiffusionPipeline, StableDiffusionXLPipeline, DPMSolverSinglestepScheduler
from langchain_google_genai import ChatGoogleGenerativeAI
import bitsandbytes as bnb
import torch.nn as nn
import torch
import pyttsx3
import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs

# stable_diffusion_xl_base = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
# stable_diffusion_xl_base.enable_model_cpu_offload()

pipe = StableDiffusionXLPipeline.from_pretrained("sd-community/sdxl-flash", torch_dtype=torch.float16).to('cuda')
pipe.scheduler = DPMSolverSinglestepScheduler.from_config(pipe.scheduler.config, timestep_spacing="trailing")


def quantize_model_to_4bit(model):
    replacements = []

    # Collect layers to be replaced
    for name, module in model.named_modules():
        if isinstance(module, nn.Linear):
            replacements.append((name, module))

    # Replace layers
    for name, module in replacements:
        # Split the name to navigate to the parent module
        *path, last = name.split('.')
        parent = model
        for part in path:
            parent = getattr(parent, part)

        # Create and assign the quantized layer
        quantized_layer = bnb.nn.Linear4bit(module.in_features, module.out_features, bias=module.bias is not None)
        quantized_layer.weight.data = module.weight.data
        if module.bias is not None:
            quantized_layer.bias.data = module.bias.data
        setattr(parent, last, quantized_layer)

    return model

# Quantize the UNet part of the pipeline
# stable_diffusion_xl_base.unet = quantize_model_to_4bit(stable_diffusion_xl_base.unet)

# pipe.unet = quantize_model_to_4bit(pipe.unet)
pipe.enable_model_cpu_offload()


# gemini_1_5_pro = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
gemini_pro = ChatGoogleGenerativeAI(model='gemini-pro')


def generate_speech(text, lang='en', speed=170, voice='default', num=0):
    """
    Generates speech for given script.
    """
    engine = pyttsx3.init()
    
    # Set language and voice
    voices = engine.getProperty('voices')
    if voice == 'default':
        voice_id = voices[0].id
    else:
        # Try to find the voice with the given name
        voice_id = None
        for v in voices:
            if voice in v.name:
                voice_id = v.id
                break
        if not voice_id:
            raise ValueError(f"Voice '{voice}' not found.")
    
    engine.setProperty('voice', voice_id)
    engine.setProperty('rate', speed)
    print(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'outputs/speech/speech_{num}.mp3'))
    engine.save_to_file(text, os.path.join(os.path.dirname(os.path.abspath(__file__)), f'outputs/speech/speech_{num}.mp3'))
    engine.runAndWait()

def quantize_model_to_4bit_play(model):
    replacements = []

    # Collect layers to be replaced
    for name, module in model.named_modules():
        if isinstance(module, nn.Linear):
            replacements.append((name, module))

    # Replace layers
    for name, module in replacements:
        # Split the name to navigate to the parent module
        *path, last = name.split('.')
        parent = model
        for part in path:
            parent = getattr(parent, part)

        # Create and assign the quantized layer
        quantized_layer = bnb.nn.Linear4bit(module.in_features, module.out_features, bias=module.bias is not None)
        quantized_layer.weight.data = module.weight.data
        if module.bias is not None:
            quantized_layer.bias.data = module.bias.data
        
        # Move quantized layer to CUDA device
        quantized_layer = quantized_layer.to('cuda')

        setattr(parent, last, quantized_layer)

    return model


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def text_to_speech(text: str, num: int) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB", # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2", # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.40,
            similarity_boost=0.1,
            style=0.7,
            use_speaker_boost=False,
        ),
    )

    # uncomment the line below to play the audio back
    # play(response)

    # Generating a unique file name for the output MP3 file
    save_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"outputs/speech/speech_{num}.mp3")

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

