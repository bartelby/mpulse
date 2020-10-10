from rest_framework import serializers
from .models import Member

class CreateUpdateListSerializer(serializers.ListSerializer):

    def create(self, data):
        return [self.child.create(attrs) for attrs in data]

    def update(self, instances, data):
        instance_hash = {index: instance for index, instance in enumerate(instances)}

        result = [
                self.child.update(instance_hash[index], attrs)
                for index, attrs in enumerate(data)
            ]

        return result


class MemberSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        instance = Member(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.phone_number = validated_data['phone_number']
        instance.client_member_id = validated_data['client_member_id']
        instance.account_id = validated_data['account_id']
        
        instance.save()
        return instance


    class Meta:
        model = Member
        fields = ("id", "first_name", "last_name", "phone_number", "client_member_id", "account_id")
        read_only_fields = ["id"]
        list_serializer_class = CreateUpdateListSerializer
