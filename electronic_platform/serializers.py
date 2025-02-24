from rest_framework.serializers import ModelSerializer

from electronic_platform.models import Supplier, Product, Contact


class ContactSerializer(ModelSerializer):
    """Сериализатор модели контактов"""

    class Meta:
        model = Contact
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    """Сериализатор модели продуктов"""

    class Meta:
        model = Product
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    """Сериализатор модели поставщиков"""

    contacts = ContactSerializer(source="contact_set", many=True, read_only=True)
    products = ProductSerializer(source="product_set", many=True, read_only=True)

    def update(self, instance, validated_data):
        """Запрет на изменение задолжности"""
        validated_data.pop("debt", None)
        return super().update(instance, validated_data)

    class Meta:
        model = Supplier
        fields = "__all__"
