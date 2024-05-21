import qrcode

# Function to read the text from a file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to generate a QR code from text
def generate_qr_code(text, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(output_file)

# Main function
def main():
    input_file = 'tmp2.py'  # Replace with the path to your text file
    output_file = 'output_qr_code.png'  # Replace with the desired output file name

    text = read_text_file(input_file)
    generate_qr_code(text, output_file)
    print(f"QR code generated and saved to {output_file}")

if __name__ == "__main__":
    main()