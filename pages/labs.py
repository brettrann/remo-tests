#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base


class Labs(Base):

    _page_title = 'Mozilla Reps - Labs'
    _labs_page_header_locator = (By.CSS_SELECTOR, 'div.twelve.columns > h3')
    _labs_page_text_locator = (By.CSS_SELECTOR, 'div.twelve.columns > p')

    def go_to_labs_page(self):
        self.selenium.get(self.base_url + '/labs/')
        self.is_the_current_page

    @property
    def is_labs_page_header_visible(self):
        return self.find_element(*self._labs_page_header_locator)

    @property
    def is_labs_page_text_visible(self):
        return self.find_element(*self._labs_page_text_locator)
