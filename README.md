# Color_Identifier-PYTHON
This project contains a Python script to identify the most dominant color in an image and output its hexadecimal code. The script uses the `PIL` (Pillow) library for image processing and `webcolors` for color conversion and naming.

## Prerequisites

1. **Python**: Ensure you have Python installed on your system.
2. **Pillow Library**:
   - Install the Pillow library using the command:
     ```sh
     pip install pillow
     ```
3. **Webcolors Library**:
   - Install the Webcolors library using the command:
     ```sh
     pip install webcolors
     ```

## Setup

1. **Download the Python File**:
   - Save the provided [`Python code`](color_identifier.py) to a file named `color_identifier.py`.

## Usage

1. **Run the Python Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where `color_identifier.py` is saved.
   - Execute the script with the following command:
     ```sh
     python color_identifier.py
     ```

2. **Input the Image Path**:
   - When prompted, enter the full path to the image file you want to analyze.

3. **View the Result**:
   - The script will output the identified color in RGB format, its hexadecimal code, and the closest web color name.

## Example

If you run the script and provide the path to an image file, it will output something like:
  ```sh
  Enter the path to the image file: /path/to/image/file.jpg
  Identified Color in RGB: (255, 0, 0)
  Hexadecimal Code: #ff0000
  Closest Web Color Name: red
  ```

In this example, the dominant color in the image is red, represented by the RGB values (255, 0, 0) and the hexadecimal code `#ff0000`.


>[!NOTE]
>- The script identifies the most frequent color in the image and provides the corresponding hex code.
>- Ensure that the image path is correctly provided; otherwise, the script will not be able to process the image.

- Feel free to modify the code to better fit your specific needs or to improve color detection accuracy.

- This project is protected under [MIT License](LICENSE). :shipit:

