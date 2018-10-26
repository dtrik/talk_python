import requests
import bs4
import collections

WeatherReport = collections.namedtuple('Report', 'cond, temp, scale, loc')
def main():
    print_header()
    zipcode = input("Please provide the zipcode you want weather at (eg: 47904): ")
    response = get_html_from_location(zipcode)
    report = parse_html(response)
    print("Weather at {} is {} degrees {} and it is {}".format(
        report.loc, 
        report.temp, 
        report.scale, 
        report.cond))


def get_html_from_location(zipcode):
    url = "http://www.wunderground.com/weather-forecast/{}".format(zipcode)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print("Unable to get weather for this zip code, please retry with correct zipcode")


def parse_html(response):
    soup = bs4.BeautifulSoup(response, 'html.parser')
    location = soup.find(class_='region-content-header').find('h1').get_text().strip()
    condition = soup.find(class_='condition-icon').get_text().strip()
    temperature = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text().strip()
    unit = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text().strip()
    report = WeatherReport(cond=condition,temp=temperature, scale=unit, loc=location)
    return(report)


def print_header():
    print('---------------------------')
    print('       JOURNAL APP')
    print('---------------------------')
    print()


if __name__ == '__main__':
    main()