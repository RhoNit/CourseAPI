from typing import Union
from fastapi import FastAPI, HTTPException, status
from data import courses
from schema.schemas import Message, Course

# FastAPI application instance configuration
app = FastAPI(
    title="Course API",
    version="v 1.0",
    description="API implementation of Courses"
)

# get all courses (query param: level is also there)
@app.get("/courses")
async def get_all_courses(level: Union[str, None] = None):
    try:
        if level:
            courses_with_level = []
            for i in courses.keys():
                if courses[i]["level"] == level:
                    courses_with_level.append(courses[i])
            return courses_with_level
        return courses
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Courses not found")


# get a specific course (by ID)
@app.get("/courses/{course_id}")
async def get_course_by_id(course_id: int):
    try:
        return courses[course_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id: {course_id} not found!")


# create a course
@app.post("/courses", response_model=Course)
async def create_course(new_course: Course):
    new_course_id = max(courses.keys()) + 1
    courses[new_course_id] = new_course.dict()
    return courses[new_course_id]


# remove a particular course (by ID)
@app.delete("/courses/{course_id}", response_model=Message)
async def delete_course(course_id: int):
    try:
        del courses[course_id]
        return Message(msg=f"Course with ID: {course_id} is successfully deleted")
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id: {course_id} not found!")
    