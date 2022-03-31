def show_bread_crumbs(env_now, detail, area='area'):
    msg = '%s %s at %s' % (str(env_now).zfill(5), detail, area)
    print(msg)


def log_op_time(op_time, detail):
    msg = '%s %s at %s' % (str(op_time).zfill(5), detail)
    print(msg)


