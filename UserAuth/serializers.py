from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer ,UserSerializer as UserBaseSerialize

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','username','password','email','first_name','last_name']


class UserSerializer(UserBaseSerialize):
    class Meta(UserBaseSerialize.Meta):
        fields=['id','username','email','first_name','last_name']