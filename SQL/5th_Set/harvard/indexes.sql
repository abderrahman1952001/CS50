

CREATE INDEX "enrollement_by_user"
ON "enrollments"("student_id");


CREATE INDEX "enrollement_by_course"
ON "enrollments"("course_id");


CREATE INDEX courses_by_semester
ON courses(semester);


CREATE INDEX satisfies_by_courses
ON satisfies(course_id);


