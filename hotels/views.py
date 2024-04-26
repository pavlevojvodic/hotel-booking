"""Hotel booking API with property listings, reservations, and customer messaging."""
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import HotelProperty, Reservation, Newsletter, CustomerMessage


@api_view(['GET'])
def load_all_data(request):
    """Load all hotel properties."""
    props = HotelProperty.objects.select_related('type', 'location').all()
    return JsonResponse({"properties": [{
        "id": p.id, "title": p.title, "subtitle": p.subtitle, "images": p.images,
        "lowest_price": str(p.lowest_price) if p.lowest_price else None,
        "lat": str(p.lat), "long": str(p.long), "website": p.website, "phone": p.phone,
    } for p in props]})

@api_view(['GET'])
def property_detail(request, property_id):
    try:
        p = HotelProperty.objects.get(id=property_id)
        return JsonResponse({"id": p.id, "title": p.title, "images": p.images,
                            "description_eng": p.description_eng, "website": p.website})
    except HotelProperty.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)

@api_view(['POST'])
def create_reservation(request):
    data = request.data
    try:
        r = Reservation.objects.create(property_id=data["property_id"], user_name=data["user_name"],
            user_email=data["user_email"], date_start=data["date_start"], date_end=data["date_end"])
        return JsonResponse({"success": True, "id": r.id}, status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@api_view(['POST'])
def newsletter(request):
    Newsletter.objects.create(email=request.data.get("email", ""))
    return JsonResponse({"success": True})

@api_view(['POST'])
def customer_message(request):
    d = request.data
    CustomerMessage.objects.create(customer_name=d.get("name"), email=d.get("email"),
                                   subject=d.get("subject"), message=d.get("message"))
    return JsonResponse({"success": True})
