from django.core.management.base import BaseCommand
from todo.models import Todo


class Command(BaseCommand):
    help = "Add a few example tasks for the classroom demonstration."

    def handle(self, *args, **options):
        examples = [
            "Complete Django project README",
            "Revise Python and Django basics",
            "Prepare project demonstration",
            "Push the project to GitHub",
        ]
        created_count = 0
        for title in examples:
            _, created = Todo.objects.get_or_create(title=title)
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(
            f"Sample data ready. Added {created_count} new task(s)."
        ))
