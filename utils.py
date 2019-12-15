def get_data_from_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
        data = data.split('\n')

    return data


def show_menu(menu):
    for k, item in menu.items():
        msg = '{}. {}'.format(k, item)
        print(msg)


def save_permanent_data(filename, data):
    with open(filename, 'a') as f:
        f.write('\n')
        f.write(data)
