import re

from django import template
from django.urls import NoReverseMatch, reverse
from Insta.models import Like

register = template.Library()


@register.simple_tag
def has_user_liked_post(user, post):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-heart"
    except:
        return "fa-heart-o"
