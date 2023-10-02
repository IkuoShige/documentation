import yaml

# YAMLファイルを読み込む
with open('extracted_nav.yaml', 'r', encoding='utf-8') as file:
    nav_data = yaml.safe_load(file)

# データ内のすべての文字列に対して置換を行う関数
def replace_md_with_en_md(data):
    if isinstance(data, str):
        return data.replace('.md', '.en.md')
    elif isinstance(data, list):
        return [replace_md_with_en_md(item) for item in data]
    elif isinstance(data, dict):
        return {key: replace_md_with_en_md(value) for key, value in data.items()}
    else:
        return data

# .md を .en.md に置換
nav_data_modified = replace_md_with_en_md(nav_data)

# 親タグに " EN" を追加する関数
def add_en_to_parent_tags(data):
    if isinstance(data, dict):
        return {key + " EN": add_en_to_parent_tags(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [add_en_to_parent_tags(item) for item in data]
    else:
        return data

# 親タグに " EN" を追加
nav_data_modified = add_en_to_parent_tags(nav_data)

# 置換後のデータを表示
print(yaml.dump(nav_data_modified, default_style='', allow_unicode=True))

# もし必要ならば、このデータを新しいファイルに書き込むこともできます
with open('modified_extracted_nav.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(nav_data_modified, file, default_style='', allow_unicode=True)
