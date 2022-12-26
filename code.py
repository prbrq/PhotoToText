import easyocr

def text_recognition(file_path, text_file_name="result.txt"):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(file_path, detail=0, paragraph=True)

    print(result)

    with open(text_file_name, "w") as file:
        for line in result:
            file.write(f"{line}\n\n")

    return "Complited!"

def main():
    file_name = input("Enter a file name: ")
    file_path = file_name + ".jpg"
    text_file_name = file_name + ".txt"
    print(text_recognition(file_path=file_path))

if __name__ == "__main__":
    main()