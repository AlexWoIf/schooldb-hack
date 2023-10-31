import random
from datacenter.models import (Schoolkid, Lesson, Commendation,
                               Mark, Chastisement)
from django.core.exceptions import (MultipleObjectsReturned,
                                    ObjectDoesNotExist)


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
    except ObjectDoesNotExist:
        print("Ученик не найден. Проверьте правильность ввода.")
    except MultipleObjectsReturned:
        print("Найдено больше одной записи удовлетворяющей условию"
              " поиска. Попробуйте ввести больше символов "
              "(например добавьте отчество).")


def create_commendation(name, subject):
    schoolkid = get_schoolkid(name)
    if schoolkid:
        lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title__contains=subject
        ).order_by('-date').first()
    else:
        return
    if (lesson):
        Commendation.objects.create(
            text=random.choice(COMMENDATION_TEMPLATES),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,)
    else:
        print("Такой предмет не найден. Уточните название и "
              "попробуйте еще раз")


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3,])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
