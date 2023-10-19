import zlib, base64

def compress_file(input_file, output_file) -> None:
    try:
        # Read the data from the input file
        with open(input_file, "r") as input_file:
            data = input_file.read()

        # Compress the data and encode it in Base64
        data_bytes = bytes(data, 'utf-8')
        compressed_data = zlib.compress(data_bytes, 9)
        encoded_data = base64.b64encode(compressed_data).decode("utf-8")

        # Write the encoded data to the output file
        with open(output_file, "w") as file:
            file.write(encoded_data)

        return f"Successfully compressed and saved as {output_file}"

    except Exception as e:
        return e
def decompress_file(input_file, output_file) -> None:
    try:
        with open(input_file, "r") as input_file:
            data = input_file.read()
        
        encoded = data.encode("utf-8")
        encoded_data = base64.b64decode(encoded)
        decompressed_data = zlib.decompress(encoded_data)
        decoded= decompressed_data.decode("utf-8")

        # Write the decoded data to the output file
        with open(output_file, "w") as output_file:
            output_file.write(decoded)
        
        return "successfully de-compressed file"
    except Exception as e:
        return e

# if __name__ == "__main__":
#     compress_file("/Users/yadhapdahal/Desktop/python/pypro/demo.txt", "/Users/yadhapdahal/Desktop/python/pypro/demo_compressed.txt")
#     decompress_file("/Users/yadhapdahal/Desktop/python/pypro/demo_compressed.txt", "/Users/yadhapdahal/Desktop/python/pypro/demo_de_compressed.txt")