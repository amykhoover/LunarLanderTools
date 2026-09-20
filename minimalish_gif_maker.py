


import glob
from PIL import Image
import os


def compile_pngs_to_gif(frames_dir, output_gif_path, fps=10):

    pattern = os.path.join(frames_dir, "frame_*.png")
    file_list = sorted(glob.glob(pattern))
    frames = [Image.open(f) for f in file_list]

    frame_duration_ms = int(1000 / fps)

    frames[0].save(
        output_gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=frame_duration_ms,
    )

    print(f"Done! Saved GIF to: {output_gif_path}")
    
    


if __name__ == "__main__":
    run_folder="Run17-MaxSteps400"
    #"Run14-MaxSteps400"
    #"Run13-MaxSteps400"
    #run_folder = "Run9-MaxSteps400"     #"Run7-MaxSteps400"
    FRAMES_DIRECTORY = f"lunar_lander_examples/{run_folder}"
    OUTPUT_FILE = f"lunar_lander_examples/{run_folder}.gif"

    compile_pngs_to_gif(FRAMES_DIRECTORY, OUTPUT_FILE, fps=30)

