def show_bread_crumbs(env_now, detail, area='area'):
    msg = '%s %s at %s' % (str(env_now).zfill(5), detail, area)
    print(msg)

