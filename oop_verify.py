import json, codecs
import os
import sys
from bs4 import BeautifulSoup
from settings import base_urls
# from rescraper import Rescraper

"""
Pages engineered to fail:

verify_page_exists: 3tmge/files/index.html
size_comparison: 5dewf/files/index.html should be 340 KB
"""

# TODO: put this in settings
NUM_RETRIES = 2
TASK_FILE = '201606231548.json'
MIRROR = '127.0.0.1/'


with codecs.open(TASK_FILE, mode='r', encoding='utf-8') as file:
    run_info = json.load(file)


# Takes a URL and produces its relative file name.
def get_path_from_url(self, url):
    # Remove http://domain
    tail = url.replace(base_urls[0], '') + 'index.html'
    path = MIRROR + tail
    return path


# Creates a dictionary with filename : URL for all the URLs found by the crawler in the API
def generate_page_dictionary(self):
    for url in self.json_list:
        if url.endswith(self.page + '/') and url not in run_info['error_list']:
            key = self.get_path_from_url(url)
            self.paths[key] = url
            self.json_list.remove(url)
    return


# Superclass for page-specific page instances
class Page:
    def __init__(self, url, error=False):
        self.url = url
        self.error = error
        if not error:
            self.path = MIRROR + url.replace(base_urls[0], '') + 'index.html'
            self.file_size = os.path.getsize(self.path)
        else:
            self.path = ''
            self.file_size = 0

    def __str__(self):
        return self.path

    def get_content(self):
        name = file.split('/')[-3] + '/' + file.split('/')[-2]
        soup = BeautifulSoup(open(file), 'html.parser')
        return soup

# Superclass for page-specific verifiers
class Verifier:
    def __init__(self):
        self.pages = []
        self.minimum_size = 0
        self.page_elements = []
        self.failed_pages = []

    # First actual check
    # Check that each file path in the dictionary actually exists
    def verify_files_exist(self):
        for page in self.pages:
            print(page.path)
            if not os.path.exists(page.path):
                print('Failed: verify_files_exist(): ', page)
                self.failed_pages.append(page)                                  # Add to naughty list
                self.pages.pop(page)                                            # Remove from nice list
        return

    # Second check
    # Compare page size to page-specific minimum that any fully-scraped page should have
    def size_comparison(self):
        for page in self.pages:
            if not page.file_size > self.minimum_size:
                print('Failed: size_comparison(): ', page, ' has size: ', page.file_size)
                self.failed_pages.append(page)
                self.pages.pop(page)
        return

    # Third check
    # Check that specified elements are present and non-empty in each page
    def spot_check(self):
        for page in self.pages:
            soup = page.get_content()
            for element in self.page_elements:
                result = soup.select(element)
                if len(result) == 0 or len(result[0].contents) == 0:    # No results or empty results
                    print('Failed: spot_check(): ', page)
                    self.failed_pages.append(page)
                    self.pages.pop(page)
        return

class ProjectDashboardVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class ProjectFilesVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class ProjectWikiVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class ProjectAnalyticsVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class ProjectRegistrationsVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class ProjectForksVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class RegistrationDashboardVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class RegistrationFilesVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class RegistrationWikiVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class RegistrationAnalyticsVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []

class RegistrationForksVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class UserDashboardVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []


class InstitutionDashboardVerifier(Verifier):
    def __init__(self):
        Verifier.__init__(self)
        self.pages = []
        self.minimum_size = 410
        self.page_elements = [
            '#nodeTitleEditable',                                # Title
            '#contributors span.date.node-last-modified-date',   # Last modified
            '#contributorsList > ol',                            # Contributor list
            '#nodeDescriptionEditable',                          # Description
            '#tb-tbody',                                         # File list
            '#logScope > div > div > div.panel-body > span > dl' # Activity
        ]
        self.failed_pages = []
