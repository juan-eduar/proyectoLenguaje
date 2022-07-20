from django.apps import AppConfig


class SocialConfig(AppConfig):
    name = 'Social'

    def ready(self):

    	import Social.signals
