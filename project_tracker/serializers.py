from rest_framework import serializers
from .models import User, Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ClientSerializer(serializers.ModelSerializer):
    # Read-only field to display the username of the 'created_by' user
    created_by = serializers.ReadOnlyField(source='created_by.username')

    # Write-only field to accept a 'created_by_username' during input
    created_by_username = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'created_by_username']

    def create(self, validated_data):
        # Pop 'created_by_username' from validated_data
        created_by = validated_data.pop('created_by_username', None)

        if created_by:
            # Get or create the User instance based on the provided username
            created_by_user, _ = User.objects.get_or_create(username=created_by)
            validated_data['created_by'] = created_by_user

        # Create the Client instance
        return super().create(validated_data)



class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'created_at', 'created_by']

    def create(self, validated_data):
        client_name = validated_data.pop('client_name', None)
        created_by_username = validated_data.pop('created_by', None)

        # Retrieve or create Client instance
        client, _ = Client.objects.get_or_create(client_name=client_name)

        # Retrieve or create User instance
        created_by_user, _ = User.objects.get_or_create(username=created_by_username)

        # Create Project instance
        project = Project.objects.create(client=client, created_by=created_by_user, **validated_data)
        return project

    def update(self, instance, validated_data):
        client_name = validated_data.pop('client_name', None)
        created_by_username = validated_data.pop('created_by', None)

        # Update Client instance if client_name is provided
        if client_name:
            instance.client.client_name = client_name
            instance.client.save()

        # Update created_by User instance if created_by_username is provided
        if created_by_username:
            instance.created_by.username = created_by_username
            instance.created_by.save()

        # Update Project instance
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.save()

        return instance
