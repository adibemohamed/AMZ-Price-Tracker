from .amazon_config import(
    get_web_driver_options,
    get_chrome_web_driver,
    set_ignore_certficate_error,
    set_browser_as_incongnito,
    NAME,
    CURRENCY,
    FILTERS,
    BASE_URL,
    DIRECTORY
)


class GenerateReport:
    def __init__(self):
        pass

class AmazonAPI:
    def __init__(self, search_term, filters, base_url, currency):
        self.base_url = base_url
        self.search_term = search_term
        options = get_web_driver_options()
        set_ignore_certficate_error(options)
        set_browser_as_incongnito(options)
        self.dirver = get_chrome_web_driver(options)
        pass


# run the main method in python
if __name__ == '__main__':
    print('HEY')