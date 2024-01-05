import subprocess

def convert_wmv_to_mp4(input_file, output_file):
    try:
        subprocess.run(['ffmpeg', '-i', input_file, output_file])
        print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"Conversion failed: {e}")

# Replace 'input.wmv' and 'output.mp4' with your file names
input = input('input.wmv')
convert_wmv_to_mp4(input, 'output.mp4')
