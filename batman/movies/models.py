from django.db import models


class Cast(models.Model):
    name = models.CharField(max_length=128)
    birthday = models.CharField(max_length=16)
    demise = models.CharField(
        max_length=16, null=True, blank=True, default=None
    )  # noqa E501
    height = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Cast"
        verbose_name_plural = "Casts"


class Villain(models.Model):
    name = models.CharField(max_length=128)
    birthday = models.CharField(max_length=16)
    demise = models.CharField(
        max_length=16, null=True, blank=True, default=None
    )  # noqa E501
    height = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Villain"
        verbose_name_plural = "Villains"


class Movies(models.Model):
    title = models.CharField(max_length=128)
    main_actor = models.CharField(max_length=64)
    director = models.CharField(max_length=64)
    casts = models.ForeignKey(Cast, on_delete=models.CASCADE)
    villains = models.ForeignKey(Villain, on_delete=models.CASCADE)
    summary = models.TextField()
    published = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} - {self.published}"

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
