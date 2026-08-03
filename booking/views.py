from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from .models import Booking


@csrf_exempt
@require_POST
def create_booking(request):

    try:
        data = json.loads(request.body)

        booking = Booking.objects.create(
            name=data.get("name"),
            phone=data.get("phone"),
            email=data.get("email"),
            event_type=data.get("event_type"),
            event_date=data.get("event_date"),
            message=data.get("message", "")
        )

        return JsonResponse(
            {
                "success": True,
                "message": "Booking submitted successfully!",
                "booking_id": booking.id
            },
            status=201
        )

    except Exception as error:

        return JsonResponse(
            {
                "success": False,
                "message": str(error)
            },
            status=400
        )

# Create your views here.
