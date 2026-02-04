from concurrent import futures
import grpc
import course_service_pb2_grpc
import course_service_pb2

title = "Автотесты API"
description = "Будем изучать написание API автотестов"

class CourseServiceServicer (course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        print(f'Получен запрос к методу GetCourse по  курсе: {request.course_id}')
        return course_service_pb2.GetCourseResponse( course_id=request.course_id,title=title,description=description)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('[::]:50051')

    # Запускаем сервер
    server.start()
    print("gRPC сервер запущен на порту 50051...")

    # Ожидаем завершения работы сервера
    server.wait_for_termination(

# Запуск сервера при выполнении скрипта
if __name__ == "__main__":
    serve()