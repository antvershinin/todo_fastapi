from fastapi import APIRouter
from controllers.controllers import get_todos, add_todo, delete_todo, edit_todo, delete_all, complete_all

api_router = APIRouter()

api_router.add_api_route(path="/todos", endpoint=get_todos)

api_router.add_api_route(path="/todos", endpoint=add_todo, methods=["POST"])

api_router.add_api_route(path="/todos/{id}", endpoint=delete_todo, methods=["DELETE"])

api_router.add_api_route(path="/todos/{id}", endpoint=edit_todo, methods=["PATCH"])

api_router.add_api_route(path="/todos", endpoint=delete_all, methods=["DELETE"])

api_router.add_api_route(path="/todos", endpoint=complete_all, methods=["PATCH"])