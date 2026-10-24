from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Todo


def todo_list(request):
    """Show tasks and process the add-task form."""
    if request.method == "POST" and request.POST.get("action") == "add":
        title = request.POST.get("title", "").strip()
        if title:
            Todo.objects.create(title=title)
            messages.success(request, "Task added successfully.")
        else:
            messages.error(request, "Please enter a task before adding it.")
        return redirect("todo:list")

    tasks = Todo.objects.all()
    total_count = tasks.count()
    completed_count = tasks.filter(is_completed=True).count()
    pending_count = total_count - completed_count
    return render(request, "todo/list.html", {
        "tasks": tasks,
        "total_count": total_count,
        "completed_count": completed_count,
        "pending_count": pending_count,
    })


@require_POST
def edit_task(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)
    new_title = request.POST.get("title", "").strip()
    if new_title:
        task.title = new_title
        task.save(update_fields=["title"])
        messages.success(request, "Task updated.")
    else:
        messages.error(request, "A task cannot have an empty title.")
    return redirect("todo:list")


@require_POST
def toggle_task(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)
    task.is_completed = not task.is_completed
    task.save(update_fields=["is_completed"])
    return redirect("todo:list")


@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Todo, pk=task_id)
    task.delete()
    messages.success(request, "Task deleted.")
    return redirect("todo:list")


@require_POST
def clear_completed(request):
    deleted_count, _ = Todo.objects.filter(is_completed=True).delete()
    messages.success(request, f"Cleared {deleted_count} completed task(s).")
    return redirect("todo:list")
