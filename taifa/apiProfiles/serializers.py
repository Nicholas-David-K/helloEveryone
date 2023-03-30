from rest_framework import serializers
from taifa.models import Profile, ProfileStatus



class ProfileStatusSerializer(serializers.ModelSerializer):
    user_profile = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = ProfileStatus
        fields = "__all__"



class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    avatar = serializers.ImageField(read_only=True)
    status = serializers.HyperlinkedRelatedField(source='profilestatus_set', many=True, read_only=True, view_name='status-detail')

    class Meta:
        model = Profile
        fields = "__all__"




class ProfileAvatarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ("avatar",)




