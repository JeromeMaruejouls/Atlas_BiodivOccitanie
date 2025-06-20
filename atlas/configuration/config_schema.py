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
    DISPLAY_BADGE_LRM = fields.Boolean(load_default=False)
    DISPLAY_BADGE_LRE = fields.Boolean(load_default=False)
    DISPLAY_BADGE_LRN = fields.Boolean(load_default=False)
    DISPLAY_BADGE_LRR = fields.Boolean(load_default=False)
    DISPLAY_BADGE_ZDET = fields.Boolean(load_default=False)
    DISPLAY_BADGE_EEE = fields.Boolean(load_default=False)
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
    BADGE_LRM = fields.Dict(
        load_default={
            "label": "LRM",
            "config": {
                "LC": {
                    "icon": "custom/images/badges/LRM_lc.png",
                    "text": "Liste Rouge Mondiale : Préoccupation mineure",
                },
                "NT": {
                    "icon": "custom/images/badges/LRM_nt.png",
                    "text": "Liste Rouge Mondiale : Quasi menacé",
                },
                "VU": {
                    "icon": "custom/images/badges/LRM_vu.png",
                    "text": "Liste Rouge Mondiale : Vulnérable",
                },
                "NA": {
                    "icon": "custom/images/badges/LRM_na.png",
                    "text": "Liste Rouge Mondiale : Non Applicable",
                },
                "DD": {
                    "icon": "custom/images/badges/LRM_dd.png",
                    "text": "Liste Rouge Mondiale : Données insuffisantes",
                },
                "EN": {
                    "icon": "custom/images/badges/LRM_en.png",
                    "text": "Liste Rouge Mondiale : En Danger",
                },
                "NE": {
                    "icon": "custom/images/badges/LRM_ne.png",
                    "text": "Liste Rouge Mondiale : Non évalué",
                },
                "CR": {
                    "icon": "custom/images/badges/LRM_cr.png",
                    "text": "Liste Rouge Mondiale : En danger critique",
                },
            },
        }
    )
    BADGE_LRE = fields.Dict(
        load_default={
            "label": "LRE",
            "config": {
                "LC": {
                    "icon": "custom/images/badges/LRE_lc.png",
                    "text": "Liste Rouge Européenne : Préoccupation mineure",
                },
                "NT": {
                    "icon": "custom/images/badges/LRE_nt.png",
                    "text": "Liste Rouge Européenne : Quasi menacé",
                },
                "VU": {
                    "icon": "custom/images/badges/LRE_vu.png",
                    "text": "Liste Rouge Européenne : Vulnérable",
                },
                "NA": {
                    "icon": "custom/images/badges/LRE_na.png",
                    "text": "Liste Rouge Européenne : Non Applicable",
                },
                "DD": {
                    "icon": "custom/images/badges/LRE_dd.png",
                    "text": "Liste Rouge Européenne : Données insuffisantes",
                },
                "EN": {
                    "icon": "custom/images/badges/LRE_en.png",
                    "text": "Liste Rouge Européenne : En Danger",
                },
                "NE": {
                    "icon": "custom/images/badges/LRE_ne.png",
                    "text": "Liste Rouge Européenne : Non évalué",
                },
                "CR": {
                    "icon": "custom/images/badges/LRE_cr.png",
                    "text": "Liste Rouge Européenne : En danger critique",
                },
            },
        }
    )
    BADGE_LRN = fields.Dict(
        load_default={
            "label": "LRN",
            "config": {
                "LC": {
                    "icon": "custom/images/badges/LRN_lc.png",
                    "text": "Liste Rouge Nationale : Préoccupation mineure",
                },
                "NT": {
                    "icon": "custom/images/badges/LRN_nt.png",
                    "text": "Liste Rouge Nationale : Quasi menacé",
                },
                "VU": {
                    "icon": "custom/images/badges/LRN_vu.png",
                    "text": "Liste Rouge Nationale : Vulnérable",
                },
                "NA": {
                    "icon": "custom/images/badges/LRN_na.png",
                    "text": "Liste Rouge Nationale : Non Applicable",
                },
                "DD": {
                    "icon": "custom/images/badges/LRN_dd.png",
                    "text": "Liste Rouge Nationale : Données insuffisantes",
                },
                "EN": {
                    "icon": "custom/images/badges/LRN_en.png",
                    "text": "Liste Rouge Nationale : En Danger",
                },
                "NE": {
                    "icon": "custom/images/badges/LRN_ne.png",
                    "text": "Liste Rouge Nationale : Non évalué",
                },
                "CR": {
                    "icon": "custom/images/badges/LRN_cr.png",
                    "text": "Liste Rouge Nationale : En danger critique",
                },
            },
        }
    )
    BADGE_LRR = fields.Dict(
        load_default={
            "label": "LRR",
            "config": {
                "LC": {
                    "icon": "custom/images/badges/LRR_lc.png",
                    "text": "Liste Rouge Régionale : Préoccupation mineure",
                    "icon_mp": "custom/images/badges/LRR_MP_lc.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : Préoccupation mineure",
                },
                "NT": {
                    "icon": "custom/images/badges/LRR_nt.png",
                    "text": "Liste Rouge Régionale : Quasi menacé",
                    "icon_mp": "custom/images/badges/LRR_MP_nt.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : Quasi menacé",
                },
                "VU": {
                    "icon": "custom/images/badges/LRR_vu.png",
                    "text": "Liste Rouge Régionale : Vulnérable",
                    "icon_mp": "custom/images/badges/LRR_MP_vu.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : Vulnérable",
                },
                "NA": {
                    "icon": "custom/images/badges/LRR_na.png",
                    "text": "Liste Rouge Régionale : Non Applicable",
                    "icon_mp": "custom/images/badges/LRR_MP_na.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : Non Applicable",
                },
                "DD": {
                    "icon": "custom/images/badges/LRR_dd.png",
                    "text": "Liste Rouge Régionale : Données insuffisantes",
                    "icon_mp": "custom/images/badges/LRR_MP_dd.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : Données insuffisantes",
                },
                "EN": {
                    "icon": "custom/images/badges/LRR_en.png",
                    "text": "Liste Rouge Régionale : En Danger",
                    "icon_mp": "custom/images/badges/LRR_MP_en.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : En Danger",
                },
                "NE": {
                    "icon": "custom/images/badges/LRR_ne.png",
                    "text": "Liste Rouge Régionale : Non évalué",
                    "icon_mp": "custom/images/badges/LRR_MP_ne.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : Non évalué",
                },
                "CR": {
                    "icon": "custom/images/badges/LRR_cr.png",
                    "text": "Liste Rouge Régionale : En danger critique",
                    "icon_mp": "custom/images/badges/LRR_MP_cr.png",
                    "text_mp": "Liste Rouge Midi Pyrénées : En danger critique",
                },
            }
        }
    )
    BADGE_ZDET = fields.Dict(
        load_default={
            "label": "ZDET",
            "config": {
                "REGION": {
                    "icon": "custom/images/badges/ZDET_oc.png",
                    "text": "Espèce déterminante ZNIEFF sur l'ensemble de la région",  
                },
                "ZONE": {
                    "icon": "custom/images/badges/ZDET.png",
                    "text": "Espèce déterminante ZNIEFF dans une zone de la région",  
                },
            }
        }
    )
    BADGE_EEE = fields.Dict(
        load_default={
            "label": "EEE",
            "config": {
                "EEE": {
                    "icon": "custom/images/badges/EEE.png",
                    "text": "Espèce exotique envahissante",  
                },
            }
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
