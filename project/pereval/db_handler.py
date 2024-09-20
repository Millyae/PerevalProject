from models import Users, Coords, PerevalAdded, PerevalImage
from django.utils import timezone

class PerevalDataHandler:
    @staticmethod
    def add_user(email, phone=None, fam=None, name=None, otc=None):
        try:
            user, created = Users.objects.get_or_create(
                email=email,
                defaults={'phone': phone, 'fam': fam, 'name': name, 'otc': otc}
            )
            return user, created
        except Exception as e:
            raise ValueError(f"Error adding user: {e}")

    @staticmethod
    def add_coords(latitude, longitude, height):
        try:
            coords = Coords.objects.create(
                latitude=latitude,
                longitude=longitude,
                height=height
            )
            return coords
        except Exception as e:
            raise ValueError(f"Error adding coordinates: {e}")

    @staticmethod
    def add_pereval(title, coord, beauty_title=None, other_titles=None, connect=None,
                    level_winter=None, level_summer=None, level_autumn=None, level_spring=None):
        try:
            if isinstance(coord, int):
                coord = Coords.objects.get(id=coord)

            pereval = PerevalAdded.objects.create(
                date_added=timezone.now(),
                title=title,
                coord=coord,
                beauty_title=beauty_title,
                other_titles=other_titles,
                connect=connect,
                add_time=timezone.now(),
                level_winter=level_winter,
                level_summer=level_summer,
                level_autumn=level_autumn,
                level_spring=level_spring
            )
            return pereval
        except Exception as e:
            raise ValueError(f"Error adding pereval: {e}")

    @staticmethod
    def add_image(pereval, img, title):
        try:
            image = PerevalImage.objects.create(
                pereval=pereval,
                img=img,
                title=title
            )
            return image
        except Exception as e:
            raise ValueError(f"Error adding image: {e}")

