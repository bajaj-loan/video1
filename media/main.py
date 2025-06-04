import os

class VideoByteConverter:

    def video_to_bytes(self, video_path, output_path):
        """Convert a video file to a binary .bin file"""
        with open(video_path, "rb") as video_file:
            video_bytes = video_file.read()
        with open(output_path, "wb") as bin_file:
            bin_file.write(video_bytes)
        print(f" Converted '{video_path}' to '{output_path}'")

    def bytes_to_video(self, bin_path, output_video_path):
        """Convert a binary .bin file back to a video file"""
        with open(bin_path, "rb") as bin_file:
            video_bytes = bin_file.read()
        with open(output_video_path, "wb") as video_file:
            video_file.write(video_bytes)
        print(f" Reconstructed video as '{output_video_path}'")

# Example usage
if __name__ == "__main__":
    converter = VideoByteConverter()

    # SET THESE PATHS
    original_video = "example.mp4"
    binary_output = "video_bytes.bin"
    reconstructed_video = "recovered_example.mp4"

    # Uncomment what you need:

    # 1. Convert video to bytes
    #converter.video_to_bytes(original_video, binary_output)

    # 2. Convert bytes back to video
    converter.bytes_to_video(binary_output, reconstructed_video)
