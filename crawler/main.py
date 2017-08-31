import sys
import getopt

import course_crawler

DEFAULT_COURSES_URL = 'https://education.aut.ac.ir/aportal/regadm/global/' \
    'popup.sem.courses.jsp?action=view&course_id=st_sem_course&cs_semester=' \
    '{}{}&cur_sort_col=CourseId&cur_sort_ord=ASC&cur_page={}'


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(
            argv[1:], "uys", ["url", "year", "semester"])
    except getopt.GetoptError as err:
        print err
        sys.exit(2)

    url = DEFAULT_COURSES_URL
    year = '96'
    semester = '1'
    for opt, arg in opts:
        if opt == '-u':
            url = arg
        elif opt == '-y':
            year = arg
        elif opt == '-s':
            semester = arg

    course_crawler.crawl_courses(url, year, semester)


if __name__ == '__main__':
    sys.exit(main())
