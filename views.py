import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
from .redis_client import redis_client


def list_prompts(request):
    prompts = Prompt.objects.all().values("id","title","complexity")
    return JsonResponse(list(prompts), safe=False)


def get_prompt(request, id):
    try:
        prompt = Prompt.objects.get(id=id)

        key = f"prompt:{id}:views"
        view_count = redis_client.incr(key)

        data = {
            "id": str(prompt.id),
            "title": prompt.title,
            "content": prompt.content,
            "complexity": prompt.complexity,
            "view_count": view_count
        }

        return JsonResponse(data)

    except Prompt.DoesNotExist:
        return JsonResponse({"error":"Not found"}, status=404)


@csrf_exempt
def create_prompt(request):

    if request.method == "POST":
        body = json.loads(request.body)

        prompt = Prompt.objects.create(
            title = body["title"],
            content = body["content"],
            complexity = body["complexity"]
        )

        return JsonResponse({"id": str(prompt.id)})