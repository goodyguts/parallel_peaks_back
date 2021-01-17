# Generated by Django 3.1.4 on 2020-12-21 01:37

from django.db import migrations, models
import matching.validators


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0003_auto_20201221_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchingentry',
            name='album_adjectives',
            field=models.JSONField(blank=True, default=list, help_text='What adjectives would you use to describe your album? Valid choices are <select><option>All over the place</option><option>Ambitious/epic</option><option>Angry/passionate/intense</option><option>Chill/slow-paced/ballads</option><option>Classic/influential</option><option>Concept album</option><option>Danceable/festival</option><option>Disturbing/disgusting</option><option>Domestic/wholesome/sincere</option><option>Dreamy/meditative</option><option>Empowering/proud</option><option>Experimental/strange</option><option>Fast-paced/Upbeat</option><option>Funny</option><option>Happy/joyful</option><option>Heartbreaking/break-up</option><option>Instrumental (i.e. no lyrics)</option><option>Loud</option><option>LGBT</option><option>Lyrical</option><option>Musically complex</option><option>Musically simple/acoustic</option><option>Political</option><option>Psychedelic</option><option>Quiet</option><option>Romantic</option><option>Sad/melancholic/sombre</option><option>Screaming/shouting</option><option>Silly</option><option>Summery</option><option>Vibey</option><option>Wintery</option></select>', validators=[matching.validators.ListOfStringsValidator('Your album adjectives were invalid.', 'album adjectives', choices=('All over the place', 'Ambitious/epic', 'Angry/passionate/intense', 'Chill/slow-paced/ballads', 'Classic/influential', 'Concept album', 'Danceable/festival', 'Disturbing/disgusting', 'Domestic/wholesome/sincere', 'Dreamy/meditative', 'Empowering/proud', 'Experimental/strange', 'Fast-paced/Upbeat', 'Funny', 'Happy/joyful', 'Heartbreaking/break-up', 'Instrumental (i.e. no lyrics)', 'Loud', 'LGBT', 'Lyrical', 'Musically complex', 'Musically simple/acoustic', 'Political', 'Psychedelic', 'Quiet', 'Romantic', 'Sad/melancholic/sombre', 'Screaming/shouting', 'Silly', 'Summery', 'Vibey', 'Wintery'))]),
        ),
        migrations.AlterField(
            model_name='matchingentry',
            name='match_adjectives',
            field=models.JSONField(blank=True, default=list, help_text='Select the adjectives you want your match to embody.Valid choices are <select><option>All over the place</option><option>Ambitious/epic</option><option>Angry/passionate/intense</option><option>Chill/slow-paced/ballads</option><option>Classic/influential</option><option>Concept album</option><option>Danceable/festival</option><option>Disturbing/disgusting</option><option>Domestic/wholesome/sincere</option><option>Dreamy/meditative</option><option>Empowering/proud</option><option>Experimental/strange</option><option>Fast-paced/Upbeat</option><option>Funny</option><option>Happy/joyful</option><option>Heartbreaking/break-up</option><option>Instrumental (i.e. no lyrics)</option><option>Loud</option><option>LGBT</option><option>Lyrical</option><option>Musically complex</option><option>Musically simple/acoustic</option><option>Political</option><option>Psychedelic</option><option>Quiet</option><option>Romantic</option><option>Sad/melancholic/sombre</option><option>Screaming/shouting</option><option>Silly</option><option>Summery</option><option>Vibey</option><option>Wintery</option></select>', validators=[matching.validators.ListOfStringsValidator('Your match adjectives are invalid.', 'match adjectives', choices=('All over the place', 'Ambitious/epic', 'Angry/passionate/intense', 'Chill/slow-paced/ballads', 'Classic/influential', 'Concept album', 'Danceable/festival', 'Disturbing/disgusting', 'Domestic/wholesome/sincere', 'Dreamy/meditative', 'Empowering/proud', 'Experimental/strange', 'Fast-paced/Upbeat', 'Funny', 'Happy/joyful', 'Heartbreaking/break-up', 'Instrumental (i.e. no lyrics)', 'Loud', 'LGBT', 'Lyrical', 'Musically complex', 'Musically simple/acoustic', 'Political', 'Psychedelic', 'Quiet', 'Romantic', 'Sad/melancholic/sombre', 'Screaming/shouting', 'Silly', 'Summery', 'Vibey', 'Wintery'))]),
        ),
        migrations.AlterField(
            model_name='matchingentry',
            name='match_country',
            field=models.CharField(blank=True, help_text='Are there any particular country(/ies) that you want your match album to be from?', max_length=100),
        ),
        migrations.AlterField(
            model_name='matchingentry',
            name='match_macrogenre',
            field=models.JSONField(help_text='Which macrogenres would you be happy to receive recommendations from, in order of preference? Select at least 2. Valid choices are <select><option>CFB (Country, Folk & Blues)</option><option>Classical (Classical)</option><option>ED (Electronic and Dance)</option><option>HHRB (Hip Hop and R&B)</option><option>IIPEPP (Indie, Indie Pop, Emo and Pop Punk)</option><option>JSNSF (Jazz, Soul, Neo-Soul and Funk)</option><option>Pop (Pop)</option><option>RMPNPPRI (Rock, Metal, Punk, Noise, Prog, Post-Rock, Industrial)</option><option>Other (Other)</option></select>', validators=[matching.validators.ListOfStringsValidator('Your match macrogenre was invalid, you might not have selected enough genres.', 'match macrogenre', choices=[('CFB', 'Country, Folk & Blues'), ('Classical', 'Classical'), ('ED', 'Electronic and Dance'), ('HHRB', 'Hip Hop and R&B'), ('IIPEPP', 'Indie, Indie Pop, Emo and Pop Punk'), ('JSNSF', 'Jazz, Soul, Neo-Soul and Funk'), ('Pop', 'Pop'), ('RMPNPPRI', 'Rock, Metal, Punk, Noise, Prog, Post-Rock, Industrial'), ('Other', 'Other')], min_items=2)]),
        ),
    ]
