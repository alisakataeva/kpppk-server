from django.shortcuts import get_object_or_404

from businesslogic.models import Program


#


def get_program_list() -> list[Program]:
    return list(Program.objects.filter(is_active=True))


def get_landing_program_list() -> list[Program]:
    return list(Program.objects.filter(is_active=True))[:8]


def get_program_detail(id: int) -> Program:
    return get_object_or_404(Program, pk=id)
