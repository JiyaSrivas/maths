import os
import wave
import struct
import math
import numpy as np

def generate_ambient_bgm(output_wav_path, total_duration_seconds=320.0, sample_rate=44100):
    """
    Synthesizes a royalty-free, peaceful, ambient chord progression.
    Uses soft sinusoidal harmonics, subtle chorus/tremolo, low-pass filtering,
    and soft envelope so it sits gracefully behind voice narration at -24dB.
    """
    print(f"Synthesizing ambient background music for {total_duration_seconds:.1f} seconds...")
    n_samples = int(total_duration_seconds * sample_rate)
    t = np.linspace(0, total_duration_seconds, n_samples, endpoint=False)
    
    # Chord progression (frequencies in Hz):
    # Cmaj9 (C3, E3, G3, B3, D4)
    # Am9   (A2, C3, E3, G3, B3)
    # Fmaj7 (F2, A2, C3, E3, G3)
    # Gsus4 (G2, C3, D3, G3, D4)
    chords = [
        [130.81, 164.81, 196.00, 246.94, 293.66], # Cmaj9
        [110.00, 130.81, 164.81, 196.00, 246.94], # Am9
        [87.31, 110.00, 130.81, 164.81, 196.00],  # Fmaj7
        [98.00, 130.81, 146.83, 196.00, 293.66]   # Gsus4
    ]
    chord_duration = 10.0 # seconds per chord
    
    left_channel = np.zeros(n_samples, dtype=np.float32)
    right_channel = np.zeros(n_samples, dtype=np.float32)
    
    num_chord_blocks = int(math.ceil(total_duration_seconds / chord_duration))
    
    for i in range(num_chord_blocks):
        chord = chords[i % len(chords)]
        t_start = i * chord_duration
        t_end = min((i + 1) * chord_duration, total_duration_seconds)
        idx_start = int(t_start * sample_rate)
        idx_end = int(t_end * sample_rate)
        block_len = idx_end - idx_start
        if block_len <= 0:
            continue
            
        t_block = np.linspace(0, (t_end - t_start), block_len, endpoint=False)
        # Gentle attack and release envelope (2 second attack, 2 second release)
        attack = int(2.0 * sample_rate)
        release = int(2.5 * sample_rate)
        env = np.ones(block_len, dtype=np.float32)
        if block_len > attack:
            env[:attack] = np.sin(np.linspace(0, np.pi/2, attack))**2
        if block_len > release:
            env[-release:] = np.cos(np.linspace(0, np.pi/2, release))**2
            
        block_sig_l = np.zeros(block_len, dtype=np.float32)
        block_sig_r = np.zeros(block_len, dtype=np.float32)
        
        for freq_idx, freq in enumerate(chord):
            # Fundamental + soft octave harmonic + detuned stereo spread
            amp = 0.20 / (freq_idx + 1)**0.6
            detune = 0.4 # Hz detuning for lush stereo pad
            # Left channel
            block_sig_l += amp * np.sin(2 * np.pi * freq * t_block)
            block_sig_l += (amp * 0.25) * np.sin(2 * np.pi * (2 * freq) * t_block)
            # Right channel slightly detuned
            block_sig_r += amp * np.sin(2 * np.pi * (freq + detune) * t_block)
            block_sig_r += (amp * 0.25) * np.sin(2 * np.pi * (2 * freq - detune) * t_block)
            
        # Subtle slow tremolo (0.2 Hz)
        tremolo = 0.85 + 0.15 * np.sin(2 * np.pi * 0.2 * t_block)
        
        left_channel[idx_start:idx_end] += block_sig_l * env * tremolo
        right_channel[idx_start:idx_end] += block_sig_r * env * tremolo

    # Normalize and attenuate to subtle background level (-24 dB peak)
    max_val = max(np.max(np.abs(left_channel)), np.max(np.abs(right_channel)))
    if max_val > 0:
        # Scale to -24 dB relative to 1.0 (approx 0.063 max amplitude)
        target_peak = 0.055
        left_channel = (left_channel / max_val) * target_peak
        right_channel = (right_channel / max_val) * target_peak
        
    # Overall fade in at video start and fade out at video end
    fade_len = int(3.0 * sample_rate)
    if n_samples > 2 * fade_len:
        fade_in = np.linspace(0, 1, fade_len)
        fade_out = np.linspace(1, 0, fade_len)
        left_channel[:fade_len] *= fade_in
        right_channel[:fade_len] *= fade_in
        left_channel[-fade_len:] *= fade_out
        right_channel[-fade_len:] *= fade_out
        
    # Convert to 16-bit PCM stereo
    int_left = np.int16(np.clip(left_channel * 32767, -32768, 32767))
    int_right = np.int16(np.clip(right_channel * 32767, -32768, 32767))
    
    interleaved = np.empty((n_samples * 2,), dtype=np.int16)
    interleaved[0::2] = int_left
    interleaved[1::2] = int_right
    
    with wave.open(output_wav_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(interleaved.tobytes())
        
    print(f"Background music saved to: {output_wav_path}")
    return output_wav_path

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(__file__)), "audio_cache", "ambient_bgm.wav")
    generate_ambient_bgm(out)
