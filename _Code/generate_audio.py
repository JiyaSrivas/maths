import os
import subprocess
import wave
import sys

AUDIO_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "audio_cache")
os.makedirs(AUDIO_DIR, exist_ok=True)

SCENES_NARRATION = [
    {
        "scene": 1,
        "name": "hook",
        "text": (
            "Welcome to Linear Algebra and Calculus. Imagine the 2D plane as a flexible sheet. "
            "When a linear transformation acts upon it, grid lines tilt, unit squares stretch into parallelograms, "
            "and almost every vector rotates and gets knocked off its original span. "
            "Look at the plane: as space warps, vectors spin across quadrants. "
            "But here is the central question: does every vector turn? "
            "Or are there special invariant directions that stubbornly refuse to rotate, changing only in scale? "
            "In this video, we will discover eigenvalues and eigenvectors: the invariant axes that define how matrices transform our world."
        ),
        "target_pad": 1.0
    },
    {
        "scene": 2,
        "name": "concept_introduction",
        "text": (
            "Let us state the formal definition. Given an n-by-n square matrix A, a non-zero vector v is called an eigenvector "
            "if multiplying A by v produces a vector that is simply a scalar multiple of v. "
            "That is, A times v equals lambda times v. The scalar lambda is the eigenvalue. "
            "Notice the elegance of this equation: on the left, A times v is a coupled multi-dimensional transformation. "
            "On the right, it collapses into simple scalar multiplication: stretching, shrinking, or reversing v along its line. "
            "We strictly require v to be non-zero, because the zero vector satisfies this trivially for every number. "
            "By the end of this video, you will be able to determine both the eigenvalues and their invariant eigenspaces with complete clarity."
        ),
        "target_pad": 1.0
    },
    {
        "scene": 3,
        "name": "visual_intuition",
        "text": (
            "To build geometric intuition, let us examine the symmetric matrix with rows [2, 1] and [1, 2]. "
            "First, observe a generic vector: the standard unit basis vector [1, 0]. "
            "Under the transformation, it maps to [2, 1], rotating by over twenty-six degrees. It is not an eigenvector. "
            "Now, look at the diagonal line y equals x, with vector [1, 1]. "
            "As our matrix transforms space, watch closely: this vector never turns! "
            "It stays pinned to the line y equals x, stretching to exactly three times its original length. Here, lambda equals three! "
            "Next, observe the perpendicular line, y equals minus x, with vector [-1, 1]. "
            "When transformed, it maps to [-1, 1]—completely unchanged in length and direction! Here, lambda equals one. "
            "These two invariant lines form the natural coordinate framework of the transformation."
        ),
        "target_pad": 1.0
    },
    {
        "scene": 4,
        "name": "worked_example",
        "text": (
            "Now, how do we find these values algebraically without guessing? "
            "We begin with A v equals lambda v, which rewrites as open parenthesis A minus lambda I close parenthesis times v equals zero. "
            "For a non-zero vector v to exist, the matrix A minus lambda I must have linearly dependent columns, meaning its determinant is zero. "
            "This gives the characteristic equation: the determinant of [2 minus lambda, 1; 1, 2 minus lambda] equals zero. "
            "Calculating the determinant yields open parenthesis 2 minus lambda close parenthesis squared minus one, which simplifies to lambda squared minus four lambda plus three equals zero. "
            "Factoring gives open parenthesis lambda minus three close parenthesis times open parenthesis lambda minus one close parenthesis equals zero. "
            "Thus, our eigenvalues are lambda one equals three, and lambda two equals one! "
            "Substituting lambda equals three back into our nullspace equation yields minus x plus y equals zero, so y equals x, giving eigenvector [1, 1]. "
            "Substituting lambda equals one yields x plus y equals zero, so y equals minus x, giving eigenvector [-1, 1]. "
            "The algebra matches our visual geometry perfectly!"
        ),
        "target_pad": 1.0
    },
    {
        "scene": 5,
        "name": "interpretation",
        "text": (
            "Why is this concept so profoundly important? "
            "Because our two eigenvectors are orthogonal, they form a complete basis for the plane. "
            "Any arbitrary vector x can be decomposed into c1 times v1 plus c2 times v2. "
            "When we apply A repeatedly, say k times, the action decouples completely! "
            "A to the k times x is simply c1 times three to the k times v1, plus c2 times one to the k times v2. "
            "This is matrix diagonalization: A equals P D P inverse, turning coupled systems into simple independent scalings. "
            "This principle powers Google's PageRank to rank the web, predicts structural vibration frequencies to prevent bridge resonance, "
            "and underpins Principal Component Analysis for data compression in machine learning."
        ),
        "target_pad": 1.0
    },
    {
        "scene": 6,
        "name": "summary_credits",
        "text": (
            "To conclude, let us review our three key takeaways: "
            "First, an eigenvector represents an invariant direction that never rotates under a linear transformation, only scaling by lambda. "
            "Second, eigenvalues are the roots of the characteristic equation, the determinant of A minus lambda I equals zero. "
            "And third, the eigenbasis decouples complex matrix transformations into simple parallel scalings. "
            "This project was produced for Linear Algebra and Calculus M3 by Jiya. "
            "Thank you for watching, and happy learning!"
        ),
        "target_pad": 1.5
    }
]

def generate_scene_audio(scene_info):
    scene_num = scene_info["scene"]
    name = scene_info["name"]
    text = scene_info["text"]
    pad = scene_info["target_pad"]
    
    aiff_path = os.path.join(AUDIO_DIR, f"scene_{scene_num}_{name}.aiff")
    wav_path = os.path.join(AUDIO_DIR, f"scene_{scene_num}_{name}.wav")
    
    print(f"Generating audio for Scene {scene_num}: {name}...")
    # Use say with voice Daniel (or Samantha if preferred)
    cmd = ["say", "-v", "Daniel", "-r", "180", "-o", aiff_path, text]
    subprocess.run(cmd, check=True)
    
    # Convert to 44.1kHz stereo WAV with subtle padding at the start and end
    # Using ffmpeg filter to add silence padding
    ffmpeg_cmd = [
        "ffmpeg", "-y", "-i", aiff_path,
        "-af", f"apad=pad_dur={pad}",
        "-ar", "44100", "-ac", "2",
        wav_path
    ]
    subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    
    with wave.open(wav_path, "rb") as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        duration = frames / float(rate)
    
    print(f"  -> Scene {scene_num} Duration: {duration:.2f} seconds ({duration/60:.2f} minutes)")
    return {
        "scene": scene_num,
        "name": name,
        "wav_path": wav_path,
        "duration": duration
    }

def main():
    results = []
    total_dur = 0.0
    for scene in SCENES_NARRATION:
        res = generate_scene_audio(scene)
        results.append(res)
        total_dur += res["duration"]
        
    print("\n" + "="*50)
    print(f"TOTAL NARRATION DURATION: {total_dur:.2f} seconds ({total_dur/60:.2f} minutes)")
    print("="*50)
    return results

if __name__ == "__main__":
    main()
