def make_list(objs, attrs):
    my_list = []
    for obj in objs:
        tmp_list = []
        for attr in attrs:
            if hasattr(obj, attr):
                tmp_list.append(getattr(obj, attr))
        my_list.append(tmp_list)
    return my_list

