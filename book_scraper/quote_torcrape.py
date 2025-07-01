import requests

from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com/"

try: 
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops. Something went wrong. Maybe check your internet connection? More details: {e}")
else:
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # print(soup.prettify())
        quote_blocks = soup.find_all("div", class_= "quote")
        all_quotes = []
        all_authors = []
        all_tags = []
        quotes_with_is = 0
        for quote in quote_blocks:
            text = quote.find("span", class_= "text").get_text()
            author = quote.find("small", class_= "author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_= "tag")]

            all_quotes.append(text)
            all_authors.append(author)
            all_tags.extend(tags)
            
            if "is" in text.lower():
                quotes_with_is += 1

            total_quotes = len(all_quotes)
            unique_author = set(author)
            author_with_most_quote = max(set(all_authors), key=all_authors.count)

            tag_counts = {}
            for tag in all_tags:
                if tag in tag_counts:
                    tag_counts[tag] += 1
                else:
                    tag_counts[tag] = 1

               
        print("First Page Analysis")
        print("----------------------------------")
        print(f"Total number of quotes: {total_quotes}")
        print(f"Number of unique authors: {len(unique_author)}")
        print(f"Author with the most quotes: {author_with_most_quote}")
        print(f"Number of quotes containing the word 'is': {quotes_with_is}")


        for tag, count in tag_counts.items():
            print(f"- {tag}: {count}")

    else:
        print(f"""That was not supposed to happen. 
        Response status code: {response.status_code}
        Response: {response.text}
        """)


url = "https://www.scrapethissite.com/pages/simple/."

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print(f"Oops. Something went wrong. Maybe check your internet connection? More details: {e}")
else:
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())

        with open("scrape_country.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
        country_info = soup.find_all("div", class_= "country")
        # print(country_info)
        all_country = []
        all_population = []
        all_area = []
        


        for country in country_info:
            countries = country.find("h3", class_="country-name").get_text(strip=True)
            population_text = country.find("span", class_="country-population").get_text(strip=True)
            area = country.find("span", class_="country-area").get_text(strip=True)
            capital = country.find("span", class_="country-capital").get_text(strip=True)
            average_population = sum(all_population)/ len(all_population)
            population = int(population_text.replace(",", ""))

            all_country.append(countries)
            all_population.append(population_text)
            all_area.extend(area)


        print(len(all_country))
        print(min(all_population))
        print(max(all_population))
        print(average_population)