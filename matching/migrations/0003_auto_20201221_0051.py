# Generated by Django 3.1.4 on 2020-12-21 00:51

from django.db import migrations, models
import matching.validators


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0002_auto_20201221_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchingentry',
            name='match_adjectives',
            field=models.JSONField(blank=True, default=list, help_text='Select the adjectives you want your match to embody.', validators=[matching.validators.ListOfStringsValidator('Your match adjectives are invalid.', 'match adjectives', choices=('All over the place', 'Ambitious/epic', 'Angry/passionate/intense', 'Chill/slow-paced/ballads', 'Classic/influential', 'Concept album', 'Danceable/festival', 'Disturbing/disgusting', 'Domestic/wholesome/sincere', 'Dreamy/meditative', 'Empowering/proud', 'Experimental/strange', 'Fast-paced/Upbeat', 'Funny', 'Happy/joyful', 'Heartbreaking/break-up', 'Instrumental (i.e. no lyrics)', 'Loud', 'LGBT', 'Lyrical', 'Musically complex', 'Musically simple/acoustic', 'Political', 'Psychedelic', 'Quiet', 'Romantic', 'Sad/melancholic/sombre', 'Screaming/shouting', 'Silly', 'Summery', 'Vibey', 'Wintery'))]),
        ),
        migrations.AlterField(
            model_name='matchingentry',
            name='match_musical_elements',
            field=models.JSONField(blank=True, default=list, help_text='What musical elements/instruments do you want your match to have?', validators=[matching.validators.ListOfStringsValidator('Your match musical elements are invalid.')]),
        ),
    ]
