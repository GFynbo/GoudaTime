from django.core.management.base import BaseCommand, CommandError
from swiper.models import Match

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('match_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for match_id in options['match_id']:
            try:
                match = Match.objects.get(pk=poll_id)
            except Match.DoesNotExist:
                raise CommandError('Match "%s" does not exist' % match_id)

            match.opened = False
            match.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed match "%s"' % match_id))
