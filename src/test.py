import yaml

# YAMLファイルのパス
yaml_file_path = "mkdocs.yml"

# YAMLファイルを読み込む
with open(yaml_file_path, "r", encoding="utf-8") as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# 'nav' タグから全てのパラメータを抽出する
nav_params = yaml_data.get("nav", [])

# 'nav' タグから全てのパラメータを表示する
for item in nav_params:
    print(f"- {item}:")
    subitems = nav_params[item]
    for subitem in subitems:
        if isinstance(subitem, dict):
            for subsubitem in subitem:
                print(f"  - {subsubitem}: {subitem[subsubitem]}")
        else:
            print(f"  - {subitem}")

# または、抽出した情報を辞書として返すこともできます
nav_parameters_dict = {}
for item in nav_params:
    subitems = nav_params[item]
    subitems_list = []
    for subitem in subitems:
        if isinstance(subitem, dict):
            subitem_dict = {}
            for subsubitem in subitem:
                subitem_dict[subsubitem] = subitem[subsubitem]
            subitems_list.append(subitem_dict)
        else:
            subitems_list.append(subitem)
    nav_parameters_dict[item] = subitems_list

# 辞書として抽出した情報を表示する
print(nav_parameters_dict)
