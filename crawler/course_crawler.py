# -*- coding: utf-8 -*-

import urllib2
import sys

from bs4 import BeautifulSoup, NavigableString


def crawl_courses(url=None, year='96', semester='1', out_file_path='courses.out'):
    if url is None:
        return

    with open(out_file_path, 'w') as file:
        for i in xrange(1, sys.maxint):
            response = urllib2.urlopen(url.format(year, semester, i))
            soup = BeautifulSoup(response.read(), "html.parser")

            tables = soup.find_all('table')
            if len(tables[2]) == 5:
                break

            rows = []
            for child in tables[2].children:
                if isinstance(child, NavigableString):
                    continue
                rows.append(child)

            rows = rows[1:-1]
            courses = []
            for row in rows:
                course = []
                for detail in row.children:
                    if isinstance(detail, NavigableString):
                        continue
                    course.append(detail.contents[0])
                    file.write(detail.contents[0].encode('utf8') + '\n')

                courses.append(course)

            print i
