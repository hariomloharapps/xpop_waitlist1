from django import views
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WaitlistUser

import json


class LandingPageView(views.View):
    """
    View to render the XPOP landing page
    """
    def get(self, request):
        return render(request, 'waitlist/landing.html')
    

    
# Alternative non-DRF view for simple JSON response
@csrf_exempt
# @require_http_methods(["POST"])
def simple_waitlist_api(request):
    """
    Simple API endpoint without DRF (alternative option)
    """
    try:
        data = json.loads(request.body)
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip().lower()
        agree_to_help = data.get('agree_to_help', False)
        
        if not name or not email:
            return JsonResponse({
                'success': False,
                'error': 'Name and email are required'
            }, status=400)
        
        # Check if email already exists
        if WaitlistUser.objects.filter(email=email).exists():
            return JsonResponse({
                'success': False,
                'error': 'Email already registered'
            }, status=400)
        
        # Create user
        user = WaitlistUser.objects.create(
            name=name,
            email=email,
            agree_to_help=agree_to_help
        )
        
        return JsonResponse({
            'success': True,
            'message': 'Added to waitlist successfully!',
            'user_id': user.id,
            'is_beta_tester': user.is_beta_tester
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)