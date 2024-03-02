import os
import json
from bs4 import BeautifulSoup, Comment

# Define the folder containing HTML files
folder_path = "webpages2"

# Create a list to store all results
all_results = []

index=33

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".html"):
        index = index +1
        
        file_path = os.path.join(folder_path, filename)
        
        # Print status update
        print(f"Processing file: {file_path}")

        # Read the HTML file
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser", on_duplicate_attribute='ignore')

        # Find URL in initial comment
        url_comment = soup.find(string=lambda text: isinstance(text, Comment))
        url = None
        if url_comment:
            url_text = url_comment.split("https://www.amazon.com/")[1].split("AUTHOR")[0]
            url = f"https://www.amazon.com/{url_text}AUTHOR"

        # Find div with id="audibleProductTitle"
        audible_title_div = soup.find("div", {"id": "audibleProductTitle"})
        title = None

        # If audibleProductTitle is not found, find divs with class="a-section a-spacing-none"
        if audible_title_div is None:
            product_title_divs = soup.find_all("div", class_="a-section a-spacing-none")
            for div in product_title_divs:
                title_span = div.find("span", {"id": "productTitle", "class": "a-size-extra-large celwidget"})
                if title_span:
                    title = title_span.text.strip()
                    break
        else:
            # Find span with id="productTitle"
            title_span = audible_title_div.find("span", {"id": "productTitle"})
            if title_span:
                title = title_span.text.strip()

        # Find all ul with class="a-unordered-list a-nostyle a-horizontal list maintain-height"
        image_url = None
        ul_tags = soup.find("ul", class_="a-unordered-list a-nostyle a-horizontal list maintain-height")
        
        if ul_tags != None:
                    
            # Find the <img> tag
            img_tag = ul_tags.find('img')

            # Extract the data-a-dynamic-image attribute
            dynamic_image_data = img_tag.get('data-a-dynamic-image')

            # Parse the attribute as a dictionary
            image_dict = eval(dynamic_image_data)

            # Extract the first URL
            image_url = list(image_dict.keys())[0]
        else:
            image_url = None

        # Find all divs with id="detailBullets_feature_div"
        detail_bullets_div = soup.find("div", {"id": "detailBullets_feature_div"})
        asin = publisher = publication_date = language = print_length = paperback = isbn_10 = isbn_13 = listening_length = audible_release_date = program_type = version = None

        if detail_bullets_div:
            # Find all li elements under ul class="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"
            bullet_list_items = detail_bullets_div.find("ul", class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list").find_all("li")
            for item in bullet_list_items:
                label = item.find("span", class_="a-text-bold").text.strip()
                value_span = item.find("span", class_="a-text-bold").find_next_sibling("span")
                value = value_span.text.strip() if value_span else ""
                if "ASIN" in label:
                    asin = value if value != "null" else None
                elif "Publisher" in label:
                    publisher = value
                elif "Publication date" in label:
                    publication_date = value
                elif "Language" in label:
                    language = value
                elif "Print length" in label:
                    print_length = value
                elif "Paperback" in label:
                    paperback = value
                elif "ISBN-10" in label:
                    isbn_10 = value
                elif "ISBN-13" in label:
                    isbn_13 = value

        # Find div with id="detailBullets_averageCustomerReviews"
        customer_reviews_div = soup.find("div", {"id": "detailBullets_averageCustomerReviews"})
        customer_reviews = None

        if customer_reviews_div:
            acr_popover_span = customer_reviews_div.find("span", {"id": "acrPopover", "class": "reviewCountTextLinkedHistogram noUnderline"})
            if acr_popover_span:
                customer_reviews = acr_popover_span["title"]

        # Print the extracted information in JSON format
        result = {
            "Index": index,
            "Title": title,
            "ASIN": asin,
            "ISBN-10": isbn_10, 
            "ISBN-13": isbn_13,
            "Publisher": publisher,
            "Publication date": publication_date,
            "Language": language,
            "Print length": print_length,
            "Image Url": image_url,
            "Customer Reviews": customer_reviews,
            "URL": url
        }

        # Add the result to the list of all results
        all_results.append(result)

# Write all results to a single JSON file
with open("Book_details2.json", "w") as json_file:
    json.dump(all_results, json_file, indent=4)

# Print status update
print("All files processed successfully.")
