---
date: 2023-09-26
authors: 
    - IkuoShige
categories:
  - terminal
  - Performance
search:
  exclude: true
---

# tmuxの基本ガイド

/// html | div#teaser
<script id="autostart">
const ctheme = 'css/w3-theme-44bb4f-mono';
document.getElementById('theme-auto').href = base_url + '/' + ctheme + '.css';
document.getElementById('theme-light').href = base_url + '/' + ctheme + '-light.css';
document.getElementById('theme-dark').href = base_url + '/' + ctheme + '-dark.css';
</script>

///
/// html | div#protected


<!-- ![Screenshot](./../img/Tmux_logo.svg.png) -->

<!--
<br />
 <a data-lightbox="group1" data-title="図1 hoge図" href="./../img/Tmux_logo.svg.png"><img alt="図1 hoge図" src="./../img/Tmux_logo.svg.png" /></a>
<br />
-->

**tmux**は、ターミナルでの作業を強化し、セッションやウィンドウの管理、ペイン(画面)の分割、ショートカットを利用して効率的な作業を可能にするツールです。以下はtmuxの基本的な使用法と設定に関するガイドです。

## インストール

tmuxをインストールするには、以下のコマンドを使用します。

```bash
sudo apt-get install tmux
```

<!-- more -->

## 設定ファイル（.tmux.conf）

.tmux.confはtmuxの設定ファイルで、カスタマイズ可能な多くのオプションがあります。これを作成または編集することで、自分の好みに合わせた設定を行えます。

## セッションの操作

tmuxはセッションと呼ばれる仮想環境を提供します。以下はセッションの操作方法です。

- **tmux**: tmuxを起動します。
- **tmux attach -t <セッション番号>**: 指定した番号のセッションにアタッチします。
- **tmux attach -t <セッション名>**: 指定したセッション名にアタッチします。
- **tmux kill-session -t <セッション番号>**: 指定した番号のセッションを終了します。
- **tmux kill-session -t <セッション名>**: 指定したセッション名を終了します。

## ショートカット

tmuxではショートカットを使用して機能を呼び出します。デフォルトの`prefix`キーは++ctrl+b++」ですが、設定ファイルで変更できます。

### まとめ

- **`prefix` + %** : 画面を横に分割します。
- **`prefix` + "** : 画面を縦に分割します。
- **`prefix` + ++c++** : 新しいウィンドウを作成します。ウィンドウはデフォルトで0からカウントされますが、設定で変更可能です。
- **`prefix` + ++1++** : 1番目のウィンドウを表示します。
- **`prefix` + ++z++** : 分割された画面の最大化と最小化を切り替えます。
- **`prefix` + ++q++ + 番号** : 指定した番号のペインに移動します。"q"を押すだけで番号が表示されます。
- **`prefix` + SPACE** : ペインの配置を提案してくれます。例: 横4つ、縦4つ、上1つ下3つ、左1つ右3つ、上下左右1つずつなど。
- **`prefix` + ++d++** : セッションをデタッチします。
- **`prefix` + [** : コピーモードを開始し、カーソルを移動します。Spaceキーで開始地点を、Enterキーで終了地点を確定します。
- **`prefix` + ]** : コピーしたテキストをペーストします。設定ファイルでviライクなコピーが可能で、クリップボードへの反映も設定できます。

### ペイン(画面)の分割・移動・レイアウト・最大化(最小化)

- **`prefix` + %** : 画面を横に分割します。
- **`prefix` + "** : 画面を縦に分割します。
- **`prefix` + ++q++ + 番号** : 指定した番号のペインに移動します。"q"を押すだけで番号が表示されます。
- **`prefix` + SPACE** : ペインの配置を提案してくれます。例: 横4つ、縦4つ、上1つ下3つ、左1つ右3つ、上下左右1つずつなど。
- **`prefix` + ++z++** : 分割された画面の最大化と最小化を切り替えます。

### ウィンドウ

- **`prefix` + ++c++** : 新しいウィンドウを作成します。ウィンドウはデフォルトで0からカウントされますが、設定で変更可能です。
- **`prefix` + `<number>`** : `<number>`番目のウィンドウを表示します。

### セッションのデタッチ

作業を一時停止してバックグラウンドでセッションを残すには、以下を使用します。

- **`prefix` + ++d++** : セッションをデタッチします。

### テキストのコピー

tmuxでテキストをコピーする方法については以下の通りです。

- **`prefix` + [** : コピーモードを開始し、カーソルを移動します。Spaceキーで開始地点を、Enterキーで終了地点を確定します。
- **`prefix` + ]** : コピーしたテキストをペーストします。設定ファイルでviライクなコピーが可能で、クリップボードへの反映も設定できます。

## クリップボードの共有

tmuxでクリップボードを共有するために、xselをインストールし、.tmux.confに以下の設定を追加します。

### インストール

```bash
sudo apt-get install xsel
```

### .tmux.confに記載

```bash
# コピーしたテキストをクリップボードに反映
bind-key -T copy-mode-vi y send -X copy-pipe-and-cancel "xsel -ip && xsel -op | xsel -ib"
bind-key -T copy-mode-vi Enter send -X copy-pipe-and-cancel "xsel -ip && xsel -op | xsel -ib"

# マウスで選択した範囲をコピー
bind -T copy-mode-vi MouseDragEnd1Pane send -X copy-pipe-and-cancel "xsel -ip && xsel -op | xsel -ib"
```

## 私の.tmux.conf

```bash
# prefixキーをC-aに変更する
set -g prefix C-a

# C-bのキーバインドを解除する
unbind C-b

#マウス操作を有効にする
set-option -g mouse on

# スクロールアップするとコピーモードに入る
bind-key -n WheelUpPane if-shell -F -t = "#{mouse_any_flag}" "send-keys -M" "if -Ft= '#{pane_in_mode}' 'send-keys -M' 'select-pane -t=; copy-mode -e; send-keys -M'"

# 最後までスクロールダウンするとコピーモードを抜ける
bind-key -n WheelDownPane select-pane -t= \; send-keys -M

# ウィンドウのインデックスを1から始める
set-option -g base-index 1

# ペインのインデックスを1から始める
set-window-option -g pane-base-index 1

# 画面の分割: terminatorと揃えた
bind C-O split-window -v
bind C-E split-window -h

# copy-pipe と競合する場合があるので無効化
set -s set-clipboard off

# コピーモード中に Vim 風に v で選択範囲を定める
bind -Tcopy-mode-vi v send -X begin-selection

# コピーモード（vi）を有効化
set-window-option -g mode-keys vi

# マウスをドラッグして選択範囲を定め、それをヤンクしてコピーモードを終了する
bind -Tcopy-mode-vi MouseDragEnd1Pane send -X copy-pipe-and-cancel "xsel -ip && xsel -op | xsel -ib"

#set -s set-clipboard external
bind-key -T copy-mode-vi y send -X copy-pipe-and-cancel "xsel -ip && xsel -op | xsel -ib"
bind-key -T copy-mode-vi Enter send -X copy-pipe-and-cancel "xsel -ip && xsel -op | xsel -ib"
```

## 参考文献

<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://qiita.com/yuki-k/items/2a28b40f0bd49b2bcb21" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://yomura.hatenablog.com/entry/2019/07/24/235045" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://jsstudy.hatenablog.com/entry/How-to-increase-multiple-Linux-SSH-connection-screens-with-tmux" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://qiita.com/nmrmsys/items/03f97f5eabec18a3a18b" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://qiita.com/vintersnow/items/be4b29652ff665c45198" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://golang.hateblo.jp/entry/2019/10/11/133000" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://gist.github.com/rummelonp/8452595" width="300" height="150" frameborder="0" scrolling="no"> </iframe>
<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://dev.classmethod.jp/articles/tmux_create_devenv_display/" width="300" height="150" frameborder="0" scrolling="no"> </iframe>

///
