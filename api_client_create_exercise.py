#from api_client_create_course import create_course_request
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.files.files_schema import CreateFileRequestSchema
from tools.fakers import get_random_email
from clients.private_http_builder import AuthenticationUserSchema
from clients.exercises.exercises_client import get_exercise_client, CreateExerciseRequestDict, UpdateExerciseRequestDict
from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request['email'],
    password=create_user_request['password']
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercise_client(authentication_user)


create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)


create_course_request = CreateCourseRequestDict(
    title="Python_homework",
    maxScore= 10,
    minScore= 2,
    description= "Homework Python",
    estimatedTime= "4 weeks",
    previewFileId= create_file_response.file.id,
    createdByUserId= create_user_response.user.id
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

create_exercise_request = CreateExerciseRequestDict(
    title="Python Exercise",
    courseId= create_course_response['course']['id'],
    maxScore= 10,
    minScore= 1,
    orderIndex= 1,
    description= "Some description",
    estimatedTime= "8 hours",
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)


print("Created exercise IDDDD",create_exercise_response['exercise']['id'])
get_exercise_response = exercises_client.get_exercise(create_exercise_response['exercise']['id'])
print("Get exercise data",get_exercise_response)


update_exercise_request = UpdateExerciseRequestDict (
    title = "Java Exercise"
)
print(create_exercise_response['exercise']['id'],update_exercise_request)
update_exercise_response = exercises_client.update_exercise(exercise_id=create_exercise_response['exercise']['id'],request = update_exercise_request)
print('Update exercise data:', update_exercise_response)

delete_exercise_response = exercises_client.delete_exercise(exercise_id=create_exercise_response['exercise']['id'])
print("Delete exercise response:", delete_exercise_response)