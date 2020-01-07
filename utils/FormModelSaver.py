def ObjCacher(obj, form, *args):
    if obj and form and args:
        for attr in args:
            if form.cleaned_data[attr]:
                setattr(obj, attr, form.cleaned_data[attr])
    return obj