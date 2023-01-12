from graphene_django import DjangoObjectType
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth import get_user_model
from.models import UserAnime, CustomUser, UserProfile


class UserAnimeNode(DjangoObjectType):
    class Meta:
        model = UserAnime
        fields = "__all__"
        filter_fields = "__all__"
        interfaces = (graphene.relay.Node,)


class UserNode(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = "__all__"
        filter_fields = "__all__"
        interfaces = (graphene.relay.Node,)

class UserProfileNode(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = "__all__"
        filter_fields = "__all__"
        interfaces = (graphene.relay.Node,)



class Query(object):
    user_anime = graphene.relay.Node.Field(UserAnimeNode)
    all_user_anime = DjangoFilterConnectionField(UserAnimeNode)

    user = graphene.relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    user_profile = graphene.relay.Node.Field(UserProfileNode)
    all_users = DjangoFilterConnectionField(UserProfileNode)



class CreateUser(graphene.Mutation):

    user = graphene.Field(UserNode)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = get_user_model()(
            username= username,
            email=email,
            password=password
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)

# class CreateUserProfile(graphene.Mutation):
#
#     user_profile = graphene.Field( UserProfileNode)
#
#     class Arguments:
#         username = graphene.String(required=True)
#         email = graphene.String(required=True)
#         password = graphene.String(required=True)
#
#     def mutate(self, info, username, password, email):
#         user = get_user_model()(
#             username= username,
#             email=email,
#             password=password
#         )
#         user.set_password(password)
#         user.save()
#
#         return CreateUser(user=user)



class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()