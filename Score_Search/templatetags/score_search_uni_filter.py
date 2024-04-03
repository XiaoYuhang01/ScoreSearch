from django import template

register = template.Library()

@register.filter(name='uni_average')
def average(score_list):
    val_list = []
    for score_record in score_list:
        val_list.append(score_record.score)
    return sum(val_list) / len(val_list)