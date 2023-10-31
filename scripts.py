import random
from datacenter.models import (Schoolkid, Lesson, Commendation,
                               Mark, Chastisement)


COMMENDATION_TEMPLATES = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!',]


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except Schoolkid.DoesNotExist:
        print("Ученик не найден. Проверьте правильность ввода.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено больше одной записи удовлетворяющей условию "
              "поиска. Попробуйте ввести больше символов (например, "
              "добавьте отчество).")


def create_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    if not schoolkid:
        return
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title__contains=subject
    ).order_by('-date').first()
    if not lesson:
        print("Такой предмет не найден. Уточните название и "
              "попробуйте еще раз")
        return
    Commendation.objects.create(
        text=random.choice(COMMENDATION_TEMPLATES),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,)


def fix_marks(schoolkid):
    Mark.objects.filter(
        schoolkid=schoolkid, 
        points__in=[2, 3,]).update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
