from rest_framework import serializers
from .models import PayHistory, User, UserMembership,Membership


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password']

class LoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'password']

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

 
class MembershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = Membership
		fields = '__all__'

class PayHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = PayHistory
		fields = '__all__'

class UserMembershipSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserMembership
		fields = '__all__'

 