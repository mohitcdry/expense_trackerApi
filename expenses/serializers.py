from rest_framework import serializers
from .models import ExpenseIncome
from django.contrib.auth.models import User


class ExpenseIncomeSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ExpenseIncome
        fields = [
            "id",
            "title",
            "description",
            "amount",
            "transaction_type",
            "tax",
            "tax_type",
            "total",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "total", "created_at", "updated_at"]

    def get_total(self, obj):
        if obj.tax_type == "flat":
            return obj.amount + obj.tax
        elif obj.tax_type == "percentage":
            return obj.amount + (obj.amount * obj.tax / 100)
        return obj.amount


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "email"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
