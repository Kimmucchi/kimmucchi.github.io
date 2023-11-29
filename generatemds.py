from datetime import date

def generate_markdown(image_url):
    today_date = date.today().strftime("%Y-%m-%d")
    markdown_content = f"---\ndate: {today_date}\nimage: >-\n  {image_url}\n---"
    return markdown_content

def main(input_file_path, output_folder_path):
    with open(input_file_path, 'r') as file:
        image_urls = file.read().splitlines()

    for i, image_url in enumerate(image_urls):
        markdown_content = generate_markdown(image_url)
        output_file_path = f"{output_folder_path}/image_{i + 1}.md"

        with open(output_file_path, 'w') as output_file:
            output_file.write(markdown_content)

if __name__ == "__main__":
    # Specify the path to the input text file containing image URLs
    input_file_path = r"C:\Users\Quenn\OneDrive\Desktop\Stardust\Devmu\Discord\syndichat2023\_imgs\urls.txt"

    # Specify the path to the folder where you want to save the generated Markdown files
    output_folder_path = r"C:\Users\Quenn\OneDrive\Desktop\Stardust\Devmu\Discord\syndichat2023\_imgs"

    main(input_file_path, output_folder_path)