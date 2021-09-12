def main():

    course_info = {
        "CS101": "3004",
        "CS102": "4501",
        "CS103": "6755",
        "NT110": "1244",
        "CM241": "1411",
    }

    course_teacher = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee",
    }

    course_meeting = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m.",
    }

    course = input("Enter a course number: ")

    if course not in course_info:
        print(course, "is not in the system")
    else:
        print("The details for course", course, "are:")
        print("room_number:", course_info[course])
        print("course_teacher:", course_teacher[course])
        print("course_meeting:", course_meeting[course])


main()
