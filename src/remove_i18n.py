import yaml

# mkdocs.yml ファイルのパス
mkdocs_yaml_path = 'mkdocs.yml'

# mkdocs.yml ファイルを読み込む
with open(mkdocs_yaml_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# plugins タグ内の - i18n タグを削除
if 'plugins' in mkdocs_data and isinstance(mkdocs_data['plugins'], list):
    mkdocs_data['plugins'] = [plugin for plugin in mkdocs_data['plugins'] if not isinstance(plugin, dict) or 'i18n' not in plugin]

# plugins タグに 'blog' を追加
if 'plugins' in mkdocs_data:
    if isinstance(mkdocs_data['plugins'], list):
        mkdocs_data['plugins'].append('blog')
    else:
        mkdocs_data['plugins'] = ['blog']
else:
    mkdocs_data['plugins'] = ['blog']

# mkdocs.yml ファイルに新しい内容を書き込む
with open(mkdocs_yaml_path, 'w', encoding='utf-8') as file:
    yaml.dump(mkdocs_data, file, default_style='', allow_unicode=True, sort_keys=False)

print("mkdocs.yml ファイルから '- i18n' タグの内容を削除し、'blog' タグを追加しました。")
