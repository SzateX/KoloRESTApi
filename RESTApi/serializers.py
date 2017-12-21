from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import SiteUser, RepoLink, Article, Comment, Tag, ArticleAuthor, ArticleTag, File


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SiteUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteUser
        fields = ('url', 'technologies', 'interests')


class RepoLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepoLink
        fields = ('url', 'link', 'user')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url', 'title', 'text', 'creation_date', 'publication_date',
                  'article_type', 'repository_link', 'creator')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url', 'text', 'creation_date', 'parent_comment', 'article',
                  'user')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('url', 'name')


class ArticleAuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleAuthor
        fields = ('url', 'user', 'article')


class ArticleTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ('url', 'tag', 'article')


class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('url', 'creation_date', 'user', 'article')
