from moviepy.editor import VideoFileClip
import numpy as np
from scipy.io.wavfile import write

def extract_audio(input_video, output_wav, target_sample_rate=16000, target_channels=1, target_dtype=np.int16):
    # Load video clip
    video_clip = VideoFileClip(input_video)

    # Extract audio
    audio_array = video_clip.audio.to_soundarray()

    # Convert to target sample rate and channels
    audio_array = audio_array.mean(axis=1)  # Convert stereo to mono
    audio_array = audio_array.astype(target_dtype)

    # Resample audio if needed
    if audio_array.shape[0] != target_sample_rate:
        audio_array = resample_audio(audio_array, video_clip.fps, target_sample_rate)

    # Save as WAV file
    write(output_wav, target_sample_rate, audio_array)

def resample_audio(audio_array, current_sample_rate, target_sample_rate):
    ratio = target_sample_rate / float(current_sample_rate)
    new_length = int(len(audio_array) * ratio)
    return np.interp(np.arange(new_length), np.arange(0, len(audio_array), 1/ratio), audio_array)

if __name__ == "__main__":
    input_video = "input/1.mp4"  # 输入的MP4文件名
    output_wav = "output/1.wav"  # 输出的WAV文件名

    extract_audio(input_video, output_wav)
