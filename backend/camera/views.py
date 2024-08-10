from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import redirect
import requests
from utils.token_manager import get_new_token

class CameraListView(View):
    def get(self, request, *args, **kwargs):
        token = '978dec3668b84246b006b4fb4c97f3746684b9fd'
        headers = {
            'Authorization': f'PersonalAccessToken {token}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get('https://api.angelcam.com/v1/shared-cameras/', headers=headers)
            response.raise_for_status()
            
            data = response.json()
            cameras = data.get('results', [])
            camera_info = [
                {
                    'id': camera.get('id'),
                    'name': camera.get('name', 'Unknown Camera'),
                    'url': f"https://my.angelcam.com/dashboard/shared-camera/{camera.get('id')}/",
                    'snapshot': camera.get('snapshot', {}).get('url', None)
                }
                for camera in cameras
            ]
            
            return JsonResponse({'cameras': camera_info}, safe=False)

        except requests.exceptions.RequestException as e:
            return JsonResponse({
                "error": str(e),
                "status_code": e.response.status_code if e.response else None,
                "response_body": e.response.text if e.response else None
            }, status=500)

class CameraDetailView(View):
    def get(self, request, *args, **kwargs):
        camera_id = kwargs.get('camera_id')
        
        # Obtém o token mais recente
        token = get_new_token()
        if not token:
            return JsonResponse({'error': 'Unable to obtain new token'}, status=500)

        # Define as URLs para streaming
        if camera_id == '112860':
            stream_url = f"https://m4-eu8.angelcam.com/cameras/{camera_id}/streams/mjpeg/stream.mjpeg?token={token}"
        elif camera_id == '112859':
            stream_url = f"https://m3-eu8.angelcam.com/cameras/{camera_id}/streams/mp4/stream.mp4?token={token}"
        else:
            return JsonResponse({'error': 'Camera ID not recognized'}, status=400)

        # Obtenha informações da câmera da API Angelcam
        try:
            response = requests.get(f'https://api.angelcam.com/v1/cameras/{camera_id}/', headers={'Authorization': f'Bearer {token}'})
            response.raise_for_status()
            data = response.json()
            camera = {
                'name': data.get('name', 'Unknown Camera'),
                'stream_url': stream_url
            }
            return JsonResponse({'camera': camera}, safe=False)

        except requests.exceptions.RequestException as e:
            return JsonResponse({
                "error": str(e),
                "status_code": e.response.status_code if e.response else None,
                "response_body": e.response.text if e.response else None
            }, status=500)

def login_redirect(request):
    return redirect('/cameras/')

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")
