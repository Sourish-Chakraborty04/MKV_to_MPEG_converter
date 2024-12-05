import tkinter as tk
from tkinter import filedialog
from moviepy import VideoFileClip
from tqdm import tqdm
from tqdm.gui import tqdm_gui

def convert_file():
    # Open file dialog to select the .mkv file
    file_path = filedialog.askopenfilename(filetypes=[("MKV Files", "*.mkv")])

    if file_path:
        # Convert the .mkv file to mpeg format
        output_path = file_path.replace(".mkv", ".mp4")
        clip = VideoFileClip(file_path)

        # Create a progress bar
        with tqdm(total=clip.duration, desc="Converting video") as pbar:
            clip.reader.read_frame = lambda: pbar.update(1)

            # Write the video to the output file
            clip.write_videofile(output_path)

        status_label.config(text="Conversion completed!")

# Create the GUI window
window = tk.Tk()

# Create file input field and buttons
file_label = tk.Label(window, text="Select .mkv file:")
file_label.pack()
file_button = tk.Button(window, text="Select File", command=convert_file)
file_button.pack()
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()