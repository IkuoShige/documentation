import yaml

# mkdocs.yml ファイルのパス
mkdocs_yaml_path = 'mkdocs.yml'

# mkdocs.yml ファイルを読み込む
with open(mkdocs_yaml_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# plugins タグに '- blog' を追加
if 'plugins' in mkdocs_data:
    if isinstance(mkdocs_data['plugins'], list):
        mkdocs_data['plugins'].append('blog')
    else:
        mkdocs_data['plugins'] = ['blog']
else:
    mkdocs_data['plugins'] = ['blog']

# オリジナルのスペースやコメントアウトを保持して mkdocs.yml ファイルに書き込む
with open(mkdocs_yaml_path, 'w', encoding='utf-8') as file:
    yaml.dump(mkdocs_data, file, default_style='', allow_unicode=True, sort_keys=False, width=float("inf"), line_break="\n", preserve_quotes=True)

print(f"'- blog' を mkdocs.yml の plugins タグに追記しました。")
