# from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
from rest_framework.fields import CurrentUserDefault

# ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.
# class DescriptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Description
#         fields = "__all__"


class AuctionCreateSerializer(serializers.ModelSerializer):
    # Description = DescriptionSerializer(read_only=True)
    # this makes sure whoever user is creating this post, only that user will be declared as owner
    # owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    owner = serializers.PrimaryKeyRelatedField(
        #     default=serializers.CurrentUserDefault(),
        #     queryset=User.objects.all(),
        read_only=True,  # this makes it read_only field, not-editable field
    )

    class Meta:
        model = AuctionModel
        fields = [
            'name',
            'auction_date',
            'description',
            'base_price',
            'description_brand',
            'description_model_number',
            'description_date_of_purchase',
            'description_location', 'owner',
        ]
        # exclude = [ 'owner', ]

    # def create(self, validated_data):
    #     validated_data['owner'] = serializers.CurrentUserDefault()  # <= magic!
    #     instance = self.Meta.model(**validated_data)
    #     instance.save()
    #     return instance


# HyperlinkedModelSerializer - similar to the ModelSerializer class except that it uses hyperlinks to represent relationships, rather than primary keys

class QuestionSerializer(serializers.ModelSerializer):
    question_owner = serializers.PrimaryKeyRelatedField(read_only=True,  # this makes it read_only field, not-editable field
                                                        )
    belongs_to_auction = serializers.PrimaryKeyRelatedField(read_only=True,  # this makes it read_only field, not-editable field
                                                            )
    # belongs_to_auction = serializers.ReadOnlyField() # also works fine

    class Meta:
        model = QuestionModel
        fields = [
            'question_owner',
            'belongs_to_auction',
            'title',
        ]
        # fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    answer_owner = serializers.PrimaryKeyRelatedField(read_only=True,  # this makes it read_only field, not-editable field
                                                      )
    belongs_to_question = serializers.PrimaryKeyRelatedField(read_only=True,  # this makes it read_only field, not-editable field
                                                             )
    # parent_answer = serializers.PrimaryKeyRelatedField(
    # read_only=True,  # this makes it read_only field, not-editable field
    # unique = True,  # Set unique=True to enforce the OneToOne relationship
    # queryset=User.objects.all(),
    # )
    # parent_answer = serializers.ReadOnlyField() # also works fine

    class Meta:
        model = AnswerModel
        fields = [
            'answer_owner',
            'belongs_to_question',
            'title',
        ]

class BidSerializer(serializers.ModelSerializer):
    belongs_to_auction = serializers.PrimaryKeyRelatedField(read_only=True,  # this makes it read_only field, not-editable field
    )
    curr_bidder = serializers.PrimaryKeyRelatedField(read_only=True,  # this makes it read_only field, not-editable field
    )

    class Meta:
        model = BidModel
        fields = [
            'curr_price',
            'curr_bidder',
            'belongs_to_auction',
            # 'curr_bidder',
        ]