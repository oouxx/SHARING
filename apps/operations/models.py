from datetime import datetime
from users.models import UserProfile
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Search(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']

    def create_search(sender, instance, created, **kwargs):
        """
        Post save handler to create/update car instances when
        Bmw or Tesla is created/updated
        """
        content_type = ContentType.objects.get_for_model(instance)
        try:
            search = Search.objects.get(content_type=content_type,
                                  object_id=instance.id)
        except Search.DoesNotExist:
            search = Search(content_type=content_type, object_id=instance.id)
        search.created = instance.created
        # car.series = instance.series
        search.save()
