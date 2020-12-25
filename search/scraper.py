import requests
from googlesearch import search
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class GoogleSearchPro:
    '''
    Parameters:
    query: query string that we want to search for,
    number : Number of results we want.
    '''
    def __init__(self, query, number):
        self.query = query
        self.number = number

    def search_url_title(self):
        urls = []
        results_search = {}
        try:
            if self.query == "":
                print("[Blank] you haven't entered anything in search")
                return


            for i in search(self.query, tld='com', num=self.number, stop=self.number, pause=0):
                urls.append(i)


            user_agent = UserAgent()

            count = 1
            for url in urls:
                r = requests.get(url, headers={"user-agent": user_agent.chrome})
                htmlcontent = r.content
                soup = BeautifulSoup(htmlcontent, 'lxml')

                rows = soup.find_all('html')

                for row in rows:
                    title = row.find('title').get_text()
                    
                    # context = {
                    #     'title': title,
                    #     'url': url
                    # }
                    
                    # print(context)


                    results_search[count] = {
                        'count': count,
                        'title': title,
                        'url': url
                    }

                count += 1

        except Exception as e:
            print("Error occured", type(e).__name__)

        return results_search


def main():
    q = input("Enter your query: ")
    num = int(input("Enter number of query: "))

    obj1 = GoogleSearchPro(q, num)
    print(obj1.search_url_title())


if __name__ == "__main__":
    main()