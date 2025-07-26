from businesslogic.models import Program


#


def get_program_list() -> list[Program]:
    return list(Program.objects.filter(is_active=True))
