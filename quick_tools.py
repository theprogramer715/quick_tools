def remove_all(target_list, value_to_remove):
    return [i for i in target_list if i != value_to_remove]


def remove_duplicates(target_list):
    seen = set()
    return [x for x in target_list if not (x in seen or seen.add(x))]


def random_element(target_list):
    import random

    return random.choice(target_list) if target_list else None


def lists_to_dict(keys_list, values_list):
    return dict(zip(keys_list, values_list))


def is_alphanumeric(text):
    return text.isalnum()


def filter_by_condition(target_list, operator_str, threshold):
    import operator

    ops = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne,
    }

    op_func = ops.get(operator_str, operator.lt)

    return [i for i in target_list if not op_func(i, threshold)]


def get_by_condition(target_list, operator_str, threshold):
    import operator

    ops = {
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
        "==": operator.eq,
        "!=": operator.ne
    }

    op_func = ops.get(operator_str, operator.lt)

    return [i for i in target_list if op_func(i, threshold)]
