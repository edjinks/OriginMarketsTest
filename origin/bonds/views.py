from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bond

from .serializers import BondSerializer

class BondView(LoginRequiredMixin, APIView):
    login_url = '/accounts/login'

    def get(self, request):
        if 'legal_name' in request.GET:                 #handles LEGALNAME param on GET
            legalname = request.GET['legal_name']
            bonds = Bond.objects.filter(legal_name=legalname, user=request.user.id) #filters just to current user and legalname param
        else:
            bonds = Bond.objects.filter(user = request.user.id)
        serializer = BondSerializer(bonds, many=True)
        return Response({"bonds": serializer.data})

    def post(self, request):
        bonds = request.data.get('bonds')
        serializer = BondSerializer(data=bonds)
        if serializer.is_valid(raise_exception=True):
            bond_saved = serializer.save(user=request.user) #save as users entry
        return Response({"success": "Bond '{}' created successfully".format(bond_saved.legal_name)})