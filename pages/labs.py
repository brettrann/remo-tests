#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Labs(Base):

    _page_title = 'Mozilla Reps - Labs'

    _labs_header_locator = (By.CSS_SELECTOR, 'h1')
    _labs_content_locator = (By.CSS_SELECTOR, 'div.large-6.columns > p')

    def go_to_labs_page(self):
        self.selenium.get(self.base_url + '/labs/')
        self.is_the_current_page

    @property
    def is_labs_header_visible(self):
        return self.is_element_visible(*self._labs_header_locator)

    @property
    def is_labs_content_visible(self):
        return self.is_element_visible(*self._labs_content_locator)

    @property
    def labs_header(self):
        return self.selenium.find_element(*self._labs_header_locator).text

    @property
    def labs_content(self):
        return self.selenium.find_element(*self._labs_content_locator).text
