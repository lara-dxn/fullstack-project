from django.apps import AppConfig


class CharacterSheetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'character_sheet'

    def ready(self):
        import character_sheet.signals  # Ensure signals are imported
