PORT = 5000
HOST = "127.0.0.1"
API_KEY = "A21WFJHNJREGG8784WDMKM"
DATABASE_PATH = "app/database/database.db"
ALLOW_ORIGIN = "http://localhost:8080"
EXECUTOR_TIMEOUT = 5

executors = {
    "python": "app.executors.python_executors",
    "cpp": "app.executors.cpp_executors",
    "c": "app.executors.c_executors",
}
