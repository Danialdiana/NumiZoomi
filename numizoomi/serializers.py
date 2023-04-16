from rest_framework import serializers

from numizoomi.models import Money

# class MoneyModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.description = description


class MoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Money
        fields = "__all__"



# def encode():
#     model = MoneyModel('Монета СССР 10 рублей', Description: Монета СССР 10 рублей')
#     model_sr = MoneySerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Монета СССР 10 рублей","description":"Description: Монета СССР 10 рублей"}')
#     data = JSONParser().parse(stream)
#     serializer = MoneySerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)

