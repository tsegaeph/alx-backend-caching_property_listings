from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .utils import get_all_properties

@cache_page(60 * 15)  # 15 minutes view-level cache
def property_list(request):
    properties = get_all_properties()  # low-level cache
    return JsonResponse({"properties": properties})
