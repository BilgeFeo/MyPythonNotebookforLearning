from rembg import remove

input_file = "./input/input.png"
output_file = "./output/output.png"

with open(input_file, "rb") as image_file:
    with open(output_file, "wb") as output_file:
        tmpInput = image_file.read()
        tmpOutput = remove(tmpInput)
        output_file.write(tmpOutput)
