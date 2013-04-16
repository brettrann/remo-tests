#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import requests
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By

from pages.base import Base


class Home(Base):

    _browserid_login_locator = (By.CSS_SELECTOR, '#browserid')
    _signin_locator = (By.CSS_SELECTOR, '#browserid')

    def go_to_homepage(self):
        self.selenium.get(self.base_url)

    def get_favicon_url(self):
        r = requests.get(self.base_url, verify=False)
        html = BeautifulSoup(r.content)
        return html.find(attrs={'rel': 'shortcut icon'}).get('href')
