#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.link_crawler import LinkCrawler
from pages.labs import Labs


class TestLabsPage:

    @pytest.mark.nondestructive
    def test_labs_page_content(self, mozwebqa):
        labs_page = Labs(mozwebqa)
        labs_page.go_to_labs_page()
        Assert.true(labs_page.is_labs_page_header_visible.text == 'Labs')
        Assert.true(labs_page.is_labs_page_text_visible)

    @pytest.mark.skip_selenium
    @pytest.mark.nondestructive
    def test_that_links_in_the_labs_page_return_200_code(self, mozwebqa):
        crawler = LinkCrawler(mozwebqa)
        urls = crawler.collect_links('/labs/', id='wrapper')
        bad_urls = []

        Assert.greater(
            len(urls), 0,
            'The link crawler did not find any urls to crawl')

        for url in urls:
            check_result = crawler.verify_status_code_is_ok(url)
            if check_result is not True:
                bad_urls.append(check_result)

        Assert.equal(
            0, len(bad_urls),
            '%s bad links found. ' % len(bad_urls) + ', '.join(bad_urls))
