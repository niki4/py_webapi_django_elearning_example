Entity - Course (start date, description, Tutor), 
       - Webinar (date, description, Tutor)

Users - Admin, Tutor (isTutor=True), Student (isTutor=False)		-> custom User model (of models.Model)

Views - CourseListView, WebinarListView
      - TutorView (list of courses Tutor assigned to, list of students and their progress), 
      - StudentView (list of courses paid by Student and with access to, list of upcoming webinars)


API access - read for all, write for admin only (could be logged in to /admin/ if API opened in browser)
