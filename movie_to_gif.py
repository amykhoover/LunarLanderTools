# pip install imageio[ffmpeg]

import imageio

if __name__ == "__main__":
    movie = "QDUnity/0_0_-episode-0.mp4"
    reader = imageio.get_reader(movie)
    fps = reader.get_meta_data()["fps"]

    writer = imageio.get_writer(f"{movie}.gif", fps=min(fps, 15))

    for frame in reader:
        writer.append_data(frame)

    writer.close()