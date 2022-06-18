from django.db import models


class Casts(models.Model):
    name = models.CharField(
        verbose_name="Nome do Ator",
        max_length=256,
        null=False,
        blank=False,
    )
    birthday = models.CharField(
        verbose_name="Data de Nascimento",
        max_length=10,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Elenco"


class Villains(models.Model):
    character_name = models.CharField(
        verbose_name="Nome do Papel/Novela",
        max_length=256,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name="Nome do Ator",
        max_length=256,
        null=False,
        blank=False,
    )
    birthday = models.CharField(
        verbose_name="Data de Nascimento",
        max_length=10,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Vilão"
        verbose_name_plural = "Vilões"


class Directors(models.Model):
    name = models.CharField(
        verbose_name="Nome do Ator",
        max_length=256,
        null=False,
        blank=False,
    )
    birthday = models.CharField(
        verbose_name="Data de Nascimento",
        max_length=10,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Diretor"
        verbose_name_plural = "Diretores"


class Screenwriters(models.Model):
    name = models.CharField(
        verbose_name="Nome do Ator",
        max_length=256,
        null=False,
        blank=False,
    )
    birthday = models.CharField(
        verbose_name="Data de Nascimento",
        max_length=10,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Roterista"
        verbose_name_plural = "Roteristas"


class MainActor(models.Model):
    character_name = models.CharField(
        verbose_name="Nome do Papel/Novela",
        max_length=256,
        null=False,
        blank=False,
    )
    name = models.CharField(
        verbose_name="Nome do Ator",
        max_length=256,
        null=False,
        blank=False,
    )
    birthday = models.CharField(
        verbose_name="Data de Nascimento",
        max_length=10,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Ator Principal"


class Movies(models.Model):
    title = models.CharField(
        verbose_name="Título do Filme",
        max_length=256,
        null=False,
        blank=False,
    )
    published_year = models.CharField(
        verbose_name="Ano de Lançamento",
        max_length=4,
        null=False,
        blank=False,
    )
    synopsis = models.TextField(verbose_name="Sinopse do Filme")
    casts = models.ManyToManyField(
        Casts,
        related_name="movie_casts",
    )
    villains = models.ManyToManyField(
        Villains,
        related_name="movie_villains",
    )
    directors = models.ManyToManyField(
        Directors,
        related_name="movie_directors",
    )
    screenwriters = models.ManyToManyField(
        Screenwriters,
        related_name="movie_screenwriters",
    )
    imdb_evaluation = models.CharField(
        verbose_name="Avaliação do IMDB",
        max_length=6,
    )
    main_actor = models.ManyToManyField(
        MainActor,
        related_name="batman",
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
