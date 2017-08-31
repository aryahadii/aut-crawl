import sys
import getopt

DEFAULT_COURSES_URL = "https://education.aut.ac.ir/aportal/regadm/global/popup.sem.courses.jsp?action=view&course_id=st_sem_course&cs_semester={}{}&cur_sort_col=CourseId&cur_sort_ord=ASC&cur_page={}"


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(
            argv[1:], "uys", ["url", "year", "semester"])
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    for opt, arg in opts:
        pass


if __name__ == '__main__':
    sys.exit(main())
