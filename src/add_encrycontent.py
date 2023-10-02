import yaml

# mkdocs.yml ファイルのパス
mkdocs_yaml_path = 'mkdocs.yml'

# mkdocs.yml ファイルを読み込む
with open(mkdocs_yaml_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# 追加するプラグインの設定
encryptcontent_config = {
    'encryptcontent': {
    'title_prefix': '',
    'summary': '',
    'placeholder': 'Password',
    'placeholder_user': 'User',
    'password_button_text': 'ENTER',
    'decryption_failure_message': 'Wrong user name or password.',
    'encryption_info_message': 'Legitimation required.',
    'translations': {
        'de': {
            'title_prefix': '',
            'summary': '',
            'placeholder': 'Passwort',
            'placeholder_user': 'Benutzer',
            'password_button_text': 'ENTER',
            'decryption_failure_message': 'Falscher Benutzer oder Passwort.',
            'encryption_info_message': 'Legitimation erforderlich.',
            'password_file': 'passwords_ad.yml'
        }
    },
    'remember_keys': True,
    'remember_prefix': 'encryptcontent_plugin_',
    'encrypted_something': {
        'md-footer__inner': ['nav', 'class']
    },
    'inject': {
        'md-content': ['div', 'class']
    },
    'search_index': 'dynamically',
    'password_button': True,
    'selfhost': True,
    'selfhost_download': True,
    'reload_scripts': ['#autostart'],
    'password_file': 'passwords.yml',
    'sharelinks': True,
    'webcrypto': True,
    'sign_files': 'encryptcontent-plugin.json',
    'hash_filenames': {
        'extensions': ['png', 'jpg', 'jpeg', 'svg'],
        'except': ['logo.svg']
    }
    }
}

# plugins タグ内の i18n タグを削除
if 'plugins' in mkdocs_data and isinstance(mkdocs_data['plugins'], list):
    mkdocs_data['plugins'] = [plugin for plugin in mkdocs_data['plugins'] if not isinstance(plugin, dict) or 'i18n' not in plugin]

# plugins タグに encryptcontent タグを追加
if 'plugins' in mkdocs_data:
    if isinstance(mkdocs_data['plugins'], list):
        mkdocs_data['plugins'].append(encryptcontent_config)
    else:
        mkdocs_data['plugins'] = [encryptcontent_config]
else:
    mkdocs_data['plugins'] = [encryptcontent_config]

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

print("mkdocs.yml ファイルに指定された内容を追加しました。")
