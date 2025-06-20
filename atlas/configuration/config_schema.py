from marshmallow import (
    Schema,
    fields,
    validates_schema,
    ValidationError,
    validates_schema,
    EXCLUDE,
)
from marshmallow.validate import Regexp


MAP_1 = {
    "name": "OpenStreetMap",
    "layer": "//{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
    "attribution": "&copy OpenStreetMap",
}
MAP_2 = {
    "name": "OpenTopoMap",
    "layer": "//a.tile.opentopomap.org/{z}/{x}/{y}.png",
    "attribution": "&copy OpenStreetMap-contributors, SRTM | Style: &copy OpenTopoMap (CC-BY-SA)",
}

LANGUAGES = {
    "en": {
        "name": "English",
        "flag_icon": "flag-icon-gb",
        "months": [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
        "decades": [
            "January 1",
            "January 2",
            "January 3",
            "February 1",
            "February 2",
            "February 3",
            "March 1",
            "March 2",
            "March 3",
            "April 1",
            "April 2",
            "April 3",
            "May 1",
            "May 2",
            "May 3",
            "June 1",
            "June 2",
            "June 3",
            "July 1",
            "July 2",
            "July 3",
            "August 1",
            "August 2",
            "August 3",
            "September 1",
            "September 2",
            "September 3",
            "October 1",
            "October 2",
            "October 3",
            "November 1",
            "November 2",
            "November 3",
            "December 1",
            "December 2",
            "December 3",
        ],
        'bdefaut': [
            'Plaine méditerranéenne : Languedoc',
            'Plaine méditerranéenne : Roussillon',
            'Plaine subméditerranéenne : Aquitaine',
            'Plaine subméditerranéenne : Languedoc',
            'Pyrénées : Pyrénées eurosibériennes',
            'Pyrénées : Pyrénées euryméditerranéennes',
            'Causses : Causses quercynois',
            'Causses : Causses languedociens',
            'Massif Central : Auvergne',
            'Massif Central : Ségala - Lévézou - Haut-Albigeois',
            'Massif central : Montagne noire - Monts de Lacaune - Sidobre',
            'Massif Central : Cévennes'
        ]
    },
    "fr": {
        "name": "Français",
        "flag_icon": "flag-icon-fr",
        "months": [
            "Janvier",
            "Février",
            "Mars",
            "Avril",
            "Mai",
            "Juin",
            "Juillet",
            "Août",
            "Septembre",
            "Octobre",
            "Novembre",
            "Decembre",
        ],
        "decades": [
            "Janvier 1",
            "Janvier 2",
            "Janvier 3",
            "Février 1",
            "Février 2",
            "Février 3",
            "Mars 1",
            "Mars 2",
            "Mars 3",
            "Avril 1",
            "Avril 2",
            "Avril 3",
            "Mai 1",
            "Mai 2",
            "Mai 3",
            "Juin 1",
            "Juin 2",
            "Juin 3",
            "Juillet 1",
            "Juillet 2",
            "Juillet 3",
            "Août 1",
            "Août 2",
            "Août 3",
            "Septembre 1",
            "Septembre 2",
            "Septembre 3",
            "Octobre 1",
            "Octobre 2",
            "Octobre 3",
            "Novembre 1",
            "Novembre 2",
            "Novembre 3",
            "Decembre 1",
            "Decembre 2",
            "Decembre 3",
        ],
        'bdefaut': [
            'Plaine méditerranéenne : Languedoc',
            'Plaine méditerranéenne : Roussillon',
            'Plaine subméditerranéenne : Aquitaine',
            'Plaine subméditerranéenne : Languedoc',
            'Pyrénées : Pyrénées eurosibériennes',
            'Pyrénées : Pyrénées euryméditerranéennes',
            'Causses : Causses quercynois',
            'Causses : Causses languedociens',
            'Massif Central : Auvergne',
            'Massif Central : Ségala - Lévézou - Haut-Albigeois',
            'Massif central : Montagne noire - Monts de Lacaune - Sidobre',
            'Massif Central : Cévennes'
        ]
    },
    "it": {
        "name": "Italiano",
        "flag_icon": "flag-icon-it",
        "months": [
            "Gennaio",
            "Febbraio",
            "Marzo",
            "Aprile",
            "Maggio",
            "Giugno",
            "Luglio",
            "Agosto",
            "Settembre",
            "Ottobre",
            "Novembre",
            "Dicembre",
        ],
        "decades": [
            "Gennaio 1",
            "Gennaio 2",
            "Gennaio 3",
            "Febbraio 1",
            "Febbraio 2",
            "Febbraio 3",
            "Marzo 1",
            "Marzo 2",
            "Marzo 3",
            "Aprile 1",
            "Aprile 2",
            "Aprile 3",
            "Maggio 1",
            "Maggio 2",
            "Maggio 3",
            "Giugno 1",
            "Giugno 2",
            "Giugno 3",
            "Luglio 1",
            "Luglio 2",
            "Luglio 3",
            "Agosto 1",
            "Agosto 2",
            "Agosto 3",
            "Settembre 1",
            "Settembre 2",
            "Settembre 3",
            "Ottobre 1",
            "Ottobre 2",
            "Ottobre 3",
            "Novembre 1",
            "Novembre 2",
            "Novembre 3",
            "Dicembre 1",
            "Dicembre 2",
            "Dicembre 3",
        ],
        'bdefaut': [
            'Plaine méditerranéenne : Languedoc',
            'Plaine méditerranéenne : Roussillon',
            'Plaine subméditerranéenne : Aquitaine',
            'Plaine subméditerranéenne : Languedoc',
            'Pyrénées : Pyrénées eurosibériennes',
            'Pyrénées : Pyrénées euryméditerranéennes',
            'Causses : Causses quercynois',
            'Causses : Causses languedociens',
            'Massif Central : Auvergne',
            'Massif Central : Ségala - Lévézou - Haut-Albigeois',
            'Massif central : Montagne noire - Monts de Lacaune - Sidobre',
            'Massif Central : Cévennes'
        ]
    },
}


class SecretSchemaConf(Schema):
    class Meta:
        unknown = EXCLUDE

    SQLALCHEMY_DATABASE_URI = fields.String(
        required=True,
        validate=Regexp(
            "^postgresql:\/\/.*:.*@[^:]+:\w+\/\w+$",
            error="Database uri is invalid ex: postgresql://monuser:monpass@server:port/db_name",
        ),
    )
    GUNICORN_PORT = fields.Integer(load_default=8080)
    modeDebug = fields.Boolean(load_default=False)
    SECRET_KEY = fields.String(required=True)
    CACHE_TIMEOUT = fields.Number(load_default=3600)


class MapConfig(Schema):
    LAT_LONG = fields.List(fields.Float(), load_default=[44.7952, 6.2287])
    MIN_ZOOM = fields.Integer(load_default=1)
    MAX_BOUNDS = fields.List(fields.List(fields.Float()), load_default=[[-180, -90], [180, 90]])
    FIRST_MAP = fields.Dict(load_default=MAP_1)
    SECOND_MAP = fields.Dict(load_default=MAP_2)
    ZOOM = fields.Integer(load_default=10)
    STEP = fields.Integer(load_default=1)
    BORDERS_COLOR = fields.String(load_default="#000000")
    BORDERS_WEIGHT = fields.Integer(load_default=3)
    ENABLE_SLIDER = fields.Boolean(load_default=True)
    ENABLE_SCALE = fields.Boolean(load_default=True)
    MASK_STYLE = fields.Dict(
        load_default={"fill": False, "fillColor": "#020202", "fillOpacity": 0.3}
    )


class AtlasConfig(Schema):
    class Meta:
        unknown = EXCLUDE

    STRUCTURE = fields.String(load_default="Nom de la structure")
    NOM_APPLICATION = fields.String(load_default="Nom de l'application")
    CUSTOM_LOGO_LINK = fields.String(load_default="")
    URL_APPLICATION = fields.String(load_default="")
    DEFAULT_LANGUAGE = fields.String(load_default="fr")
    MULTILINGUAL = fields.Boolean(load_default=False)
    ID_GOOGLE_ANALYTICS = fields.String(load_default="UA-xxxxxxx-xx")
    ORGANISM_MODULE = fields.Boolean(load_default=False)
    DISPLAY_OBSERVERS = fields.Boolean(load_default=True)
    GLOSSAIRE = fields.Boolean(load_default=False)
    IGNAPIKEY = fields.String(load_default="")
    AFFICHAGE_INTRODUCTION = fields.Boolean(load_default=True)
    AFFICHAGE_LOGOS_HOME = fields.Boolean(load_default=True)
    AFFICHAGE_FOOTER = fields.Boolean(load_default=True)
    AFFICHAGE_STAT_GLOBALES = fields.Boolean(load_default=True)
    AFFICHAGE_DERNIERES_OBS = fields.Boolean(load_default=True)
    AFFICHAGE_EN_CE_MOMENT = fields.Boolean(load_default=True)
    AFFICHAGE_RANG_STAT = fields.Boolean(load_default=True)
    AFFICHAGE_NOUVELLES_ESPECES = fields.Boolean(load_default=True)
    AFFICHAGE_RECHERCHE_AVANCEE = fields.Boolean(load_default=False)

    RANG_STAT = fields.List(
        fields.Dict,
        load_default=[
            {"phylum": ["Arthropoda", "Mollusca"]},
            {"phylum": ["Chordata"]},
            {"regne": ["Plantae"]},
        ],
    )
    RANG_STAT_FR = fields.List(
        fields.String, load_default=["Faune invertébrée", "Faune vertébrée", "Flore"]
    )
    LIMIT_RANG_TAXONOMIQUE_HIERARCHIE = fields.Integer(load_default=13)
    LIMIT_FICHE_LISTE_HIERARCHY = fields.Integer(load_default=28)
    REMOTE_MEDIAS_URL = fields.String(load_default="http://mondomaine.fr/taxhub/")
    REMOTE_MEDIAS_PATH = fields.String(load_default="static/medias/")
    REDIMENSIONNEMENT_IMAGE = fields.Boolean(load_default=False)
    TAXHUB_URL = fields.String(required=False, load_default=None)
    ATTR_DESC = fields.Integer(load_default=100)
    ATTR_COMMENTAIRE = fields.Integer(load_default=101)
    ATTR_MILIEU = fields.Integer(load_default=102)
    ATTR_CHOROLOGIE = fields.Integer(load_default=103)
    ATTR_MAIN_PHOTO = fields.Integer(load_default=1)
    ATTR_OTHER_PHOTO = fields.Integer(load_default=2)
    ATTR_LIEN = fields.Integer(load_default=3)
    ATTR_PDF = fields.Integer(load_default=4)
    ATTR_AUDIO = fields.Integer(load_default=5)
    ATTR_VIDEO_HEBERGEE = fields.Integer(load_default=6)
    ATTR_YOUTUBE = fields.Integer(load_default=7)
    ATTR_DAILYMOTION = fields.Integer(load_default=8)
    ATTR_VIMEO = fields.Integer(load_default=9)
    PROTECTION = fields.Boolean(load_default=False)
    DISPLAY_PATRIMONIALITE = fields.Boolean(load_default=False)
    PATRIMONIALITE = fields.Dict(
        load_default={
            "label": "Patrimonial",
            "config": {
                "oui": {
                    "icon": "custom/images/logo_patrimonial.png",
                    "text": "Ce taxon est patrimonial",
                }
            },
        }
    )
    STATIC_PAGES = fields.Dict(
        load_default={
            "presentation": {
                "title": "Présentation de l'atlas",
                "picto": "fa-question-circle",
                "order": 0,
                "template": "static/custom/templates/presentation.html",
            }
        }
    )

    AFFICHAGE_MAILLE = fields.Boolean(load_default=False)
    ZOOM_LEVEL_POINT = fields.Integer(load_default=11)
    LIMIT_CLUSTER_POINT = fields.Integer(load_default=1000)
    NB_DAY_LAST_OBS = fields.String(load_default="7")
    NB_LAST_OBS = fields.Integer(load_default=100)
    TEXT_LAST_OBS = fields.String(
        load_default="Les observations des agents ces 7 derniers jours |"
    )
    MAP = fields.Nested(MapConfig, load_default=dict())
    # coupe le nom_vernaculaire à la 1ere virgule sur les fiches espèces
    SPLIT_NOM_VERN = fields.Boolean(load_default=True)
    INTERACTIVE_MAP_LIST = fields.Boolean(load_default=True)
    AVAILABLE_LANGUAGES = fields.Dict(load_default=LANGUAGES)
    # Flask parameter enabling auto reload of templates
    # (no need to restart the atlas service when updating templates)
    # Defaults to False to have the best performance in production
    TEMPLATES_AUTO_RELOAD = fields.Boolean(load_default=False)

    @validates_schema
    def validate_url_taxhub(self, data, **kwargs):
        """
        TAXHHUB_URL doit être rempli si REDIMENSIONNEMENT_IMAGE = True
        """
        if data["REDIMENSIONNEMENT_IMAGE"] and data["TAXHUB_URL"] is None:
            raise ValidationError(
                {"Le champ TAXHUB_URL doit être rempli si REDIMENSIONNEMENT_IMAGE = True"}
            )
