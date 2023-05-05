def dict_data_set_values(datas):
    if isinstance(datas, dict):
        for key, value in datas.items():
            if isinstance(value, dict):
                dict_data_set_values(value)
            elif isinstance(value, list):
                value = list_data_set_values(value)
                datas = datas.update(dict({key: value}))
            else:
                datas = datas
        return datas
    elif isinstance(datas, list):
        return list_data_set_values(datas)
    else:
        return datas


def list_data_set_values(datas):
    if isinstance(datas, list):
        items = []
        for item in datas:
            if isinstance(item, dict):
                items.append(dict_data_set_values(item))
            elif isinstance(item, list):
                items.append(list_data_set_values(item))
            else:
                items.append(item)
        return item_data_set_values(datas)
    elif isinstance(datas, dict):
        return dict_data_set_values(datas)
    else:
        return item_data_set_values(datas)


def item_data_set_values(datas):
    if "{{" and "}}" in str(datas):  # yaml文件中{{}}格式需要加引号
        start_index = str(datas).index("{{")
        end_index = str(datas).index("}}")
        fun_name = str(datas)[start_index + 2:end_index]
        datas = eval(fun_name)
        return datas
