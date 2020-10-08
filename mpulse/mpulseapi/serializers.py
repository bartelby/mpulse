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

class BulkCreateUpdateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        return result

    def to_representation(self, instances):
        rep_list = []
        for instance in instances:
            rep_list.append(
                dict(
                    id = instance.pk,
                    first_name = instance.first_name,
                    last_name = instance.last_name,
                    phone_number = instance.phone_number,
                    client_member_id = instance.client_member_id,
                    account_id = instance.account_id,
                )
            )

        return rep_list

    def update(self, instances, validated_data):

        instance_hash = {index: instance for index, instance in enumerate(instances)}
        print("instance hash", time.time() - start)
        start = time.time()
        result = [self.child.update(instance_hash[index], attrs) for index, attrs in enumerate(validated_data)]
        writable_fields = [x for x in self.child.Meta.fields if x not in self.child.Meta.read_only_fields]
        try:
            self.child.Meta.model.objects.bulk_update(result, wirtable_fields)
        except IntegrityError as e:
            raise ValidationError(e)

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

class BulkMemberSerializer(serializers.Serializer):

    def create(self, validated_data):
        instance = Member(**validated_data)
        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    def update(self, instance, validated_data):

        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.phone_number = validated_data['phone_number']
        instance.client_member_id = validated_data['client_member_id']
        instance.account_id = validated_data['account_id']

        if isinstance(self._kwargs["data"], dict):
            instance.save()

        return instance

    class Meta:
        model = Member
        fields = ("id", "first_name", "last_name", "phone_number", "client_member_id", "account_id")
        read_only_fields = ["id"]
        list_serializer_class = BulkCreateUpdateListSerializer

