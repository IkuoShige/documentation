データ
------

-   Python

    -   [[f文字列(フォーマット文字列)の基本的な使い方]{.underline}](https://note.nkmk.me/python-f-strings/)

        -   print(F'{a} and {b}')

            -   で変数a and 変数b と出力される

            -   Fでもfでも変わらない

            -   シングルでもダブルでもトリプルでも変わらない(クォーテーション)

-   c++

    -   [[vectorの使い方]{.underline}](https://zenn.dev/reputeless/books/standard-cpp-for-competitive-programming/viewer/library-vector)

    -   [[sleep関数]{.underline}](https://www.techiedelight.com/ja/sleep-in-cpp/)

-   Markdown記法

    -   [[サンプル集]{.underline}](https://qiita.com/tbpgr/items/989c6badefff69377da7)

-   Google document

    -   ドキュメントの横の枠を広げる方法

        -   ファイル→ページ設定→ページ分けなしを選択

-   bash

    -   終了ステータス

        -   echo \$?

        -   0が返されれば正常終了

    -   ディレクトリ内のファイル容量を表示

        -   `du -h -s \*/`

            -   カレントディレクトリの容量を適当な単位で表示

            -   -h

                -   単位を適当な単位で表示する

            -   -s

                -   指定したファイルやディレクトリの総計を表示する

    -   [[ファイルの数を数えるコマンド]{.underline}](https://www-creators.com/archives/5820)

        `-   find . -type f \| wc -l`

            -   現在のディレクトリのファイルをカウント

        -   `ls -1U \|\| wc -l`

            -   -Uオプションがないとソートするので、ファイルが多いと遅くなる

        -   参考：単語数や行数、文字数を数えるwcコマンド

            -   -l

                -   行数を数える

            -   -c

                -   文字数を数える

            -   -w

                -   単語数を数える、スペースで囲まれた文字列を1単語

    -   zipコマンド

        -   圧縮

            -   `zip -r \<zipファイル名\> \<ディレクトリ名\>`

        -   解凍

            -   `unzip \<zipファイル名\>`

    -   [[linuxファイルの圧縮・解凍方法]{.underline}](https://qiita.com/supersaiakujin/items/c6b54e9add21d375161f)

    -   [[特定の拡張子のファイルを検索したい]{.underline}](https://eng-entrance.com/linux-command-find)

        -   find ./\<今の階層からの検索したいディレクトリの相対パス\>/> \*.\<検索したい拡張子\>

            -   ex: `find ./work/ \*.dat`

    -   ubuntuバージョン確認コマンド

        -   `lsb\_release -a`

-   jetson関係

    -   sdカードを焼く

        -   nvidiaからイメージをダウンロードする

            -   [[https://developer.nvidia.com/embedded/downloads\#?search=SD]{.underline}](https://developer.nvidia.com/embedded/downloads#?search=SD)

        -   balena Etcherでイメージを焼く

            -   balena Etcherのインストール

                -   `sudo add-apt-repository universe`

                -   `sudo apt install ./Downloads/balena-etcher\_1.18.11\_amd64.deb`

    -   dockerを用いたjetpackのflash

        -   docker Imageのインストール

            -   [[nvidiaのdocker\_sdkmanagerのマニュアル]{.underline}](https://docs.nvidia.com/sdk-manager/docker-containers/index.html)

            -   下記リンクから希望するディストリビューションのDockerImageをダウンロード

                -   [[https://developer.nvidia.com/sdk-manager]{.underline}](https://developer.nvidia.com/sdk-manager)

                -   jetpackのバージョンに対応するubuntuと同じディストリビューションを選択する

            -   `docker load -i ./sdkmanager-<version>.<build-number>-<base-OS>_docker.tar.gz`

                -   18.04の場合

                -   `sudo docker load -i \~/Downloads/sdkmanager-1.9.3.10904-Ubuntu_18.04_docker.tar.gz`

            -   `docker tag sdkmanager:<version>.<build-number>-<base-OS> sdkmanager:latest`

                -   `sudo docker tag sdkmanager:1.9.3.10904-Ubuntu_18.04 sdkmanager:latest`

        -   dockerの起動

            -   sudo docker run -it \--privileged -v
                > /dev/bus/usb:/dev/bus/usb/ \--name JetPack\_NX\_Devkit
                > \--entrypoint /bin/bash sdkmanager

            -   or

            -   docker run -it \--privileged -v
                > /dev/bus/usb:/dev/bus/usb/ \--name JetPack\_NX\_Devkit
                > sdkmanager \--cli install \--logintype devzone
                > \--product Jetson \--version 4.5.1 \--targetos Linux
                > \--ta

            -   rget JETSON\_XAVIER\_NX\_TARGETS \--flash all \--license
                > accept \--staylogin true \--datacollection enable
                > \--exitonfinish

        -   リカバリーモードでjetsonとpcをusb-microbで繋ぐ

            -   sdkmanager \--cli install \--logintype devzone
                > \--product Jetson \--version 4.6.2 \--targetos Linux
                > \--host \--target JETSON\_XAVIER\_NX\_TARGETS \--flash
                > all \--additionalsdk \'DeepStream 6.0.1\'

            -   sdkmanager \--cli install \--logintype devzone
                > \--product Jetson \--version 5.1 \--targetos Linux
                > \--host \--target JETSON\_XAVIER\_NX\_TARGETS \--flash
                > all --additionalsdk 'DeepStream 6.2'

            -   sdkmanager \--cli install \--logintype devzone
                > \--product Jetson \--version 5.0.2 \--targetos Linux
                > \--host \--target JETSON\_XAVIER\_NX\_TARGETS \--flash
                > all

    -   gpartedのインストール

        -   コマンドライン

            -   sudo apt intall gparted

        -   ubuntuのstoreでinstallする

    -   firefoxのコマンドラインのインストール

        -   sudo apt -y update && sudo apt -y upgrade

        -   sudo apt -y install firefox firefox-locale-ja

    -   sshの設定

        -   ネットワークの設定

            -   github参照

            -   [[https://www.mizutan.com/wordpress/?p=11347]{.underline}](https://www.mizutan.com/wordpress/?p=11347)

    -   [[ssh接続できない問題に遭遇した]{.underline}](https://www.codelab.jp/blog/?p=3569)

        -   ssh -V

            -   sshが入っているかどうかの確認

        -   sudo ufw status

            -   非アクティブならok

        -   sudo systemctl status ssh

            -   could not be foundってでた

            -   sudo apt update

            -   sudo apt install openssh-server

                -   したけどすでに入っている

        -   念の為自動起動と起動処理

            -   sudo systemctl enable ssh

            -   sudo systemctl start ssh

        -   sudo systemctl status ssh

            -   Activeならok

        -   ssh jetson\@192.168.23.181

            -   成功

    -   [[vncのインストール]{.underline}](https://dev.classmethod.jp/articles/jetson-remote-desktop-with-vnc/)

        -   18.04

            -   sudo apt install tigervnc-common
                > tigervnc-standalone-server tigervnc-scraping-serv

            -   vncpasswd

                -   \# Would you like to enter a view-only password
                    > (y/n)? n

                -   パスワードと確認用パスワードを入力した後にnと入力

            -   sudo vim /etc/X11/xorg.conf

            -   以下を追記

                -   Section \"Monitor\"

                -   Identifier \"DSI-0\"

                -   Option \"Ignore\"

                -   EndSection

                -   

                -   Section \"Screen\"

                -   Identifier \"Default Screen\"

                -   Monitor \"Configured Monitor\"

                -   Device \"Default Device\"

                -   SubSection \"Display\"

                -   Depth 24

                -   Virtual 1280 800

                -   EndSubSection

                -   EndSection

            -   設定終わったら再起動する

            -   起動

                -   x0vncserver -display :0 -passwordfile \~/.vnc/passwd

        -   [~~[20.04]{.underline}~~](https://ao-tela.com/vnc-vino/)

            -   ~~設定\[settings\]の共有\[sharing\]の画面共有\[Screen
                > Sharing\]を選択する~~

            -   ~~左上のボタンをクリックしてオン\[Active\]にする~~

            -   ~~パスワードを要求する\[Require a
                > password\]を選択し、設定する~~

            -   ~~gsettings set org.gnome.Vino require-encryption
                > false~~

                -   ~~暗号化を無効にする必要がある~~

            -   ~~一度オンにしておけば、再起動しても使えるようになっている~~

    -   [[vncの起動コマンドをデーモンで処理]{.underline}](https://qiita.com/iwatake2222/items/a3bd8d0527dec431ef0f)

        -   sudo vi /etc/systemd/system/x0vncserver.service

            -   \[Unit\]

            -   Description=Remote desktop service (VNC)

            -   After=syslog.target

            -   After=network.target remote-fs.target nss-lookup.target

            -   After=x11-common.service

            -   

            -   \[Service\]

            -   Type=forking

            -   User=\<username\>

            -   Group=\<username\>

            -   WorkingDirectory=/home/\<username\>

            -   ExecStart=/bin/sh -c \'sleep 30 && /usr/bin/x0vncserver
                > -display :0 -rfbport 5900 -passwordfile
                > /home/\<username\>/.vnc/passwd &\'

            -   

            -   \[Install\]

            -   WantedBy=multi-user.target

                -   sleepを10から30に変更したらうまく行った

        -   手動で確認

            -   sudo systemctl start x0vncserver.service

            -   sudo systemctl status x0vncserver.service

                -   緑でactiveってなってる

        -   有効化

            -   sudo systemctl enable x0vncserver.service

            -   sudo reboot

        -   再起動後の確認

            -   systemctl list-units \| grep vnc

        -   デーモンがfaildしている

            -   sleep時間を延ばすことで対応できた

    -   [[vnc
        > :vino]{.underline}](https://qiita.com/iwatake2222/items/a3bd8d0527dec431ef0f),
        > [[nvidia公式]{.underline}](https://developer.nvidia.com/embedded/learn/tutorials/vnc-setup)

        -   cd /usr/lib/systemd/user/graphical-session.target.wants

        -   sudo ln -s ../vino-server.service ./.

        -   gsettings set org.gnome.Vino authentication-methods
            > \"\[\'vnc\'\]\"

        -   gsettings set org.gnome.Vino vnc-password \$(echo -n
            > \'jetson\'\|base64)

            -   jetsonをパスワードに設定する場合

        -   sudo vim
            > /usr/share/glib-2.0/schemas/org.gnome.Vino.gschema.xml

            -   \<key name=\'enabled\' type=\'b\'\>

            -   \<summary\>Enable remote access to the
                > desktop\</summary\>

            -   \<description\>

            -   If true, allows remote access to the desktop via the RFB

            -   protocol. Users on remote machines may then connect to
                > the

            -   desktop using a VNC viewer.

            -   \</description\>

            -   \<default\>false\</default\>

            -   \</key\>

        -   sudo glib-compile-schemas /usr/share/glib-2.0/schemas

        -   gsettings set org.gnome.Vino require-encryption false

        -   gsettings set org.gnome.Vino prompt-enabled false

        -   sudo reboot

    -   [[vnc用ダミーディスプレイ]{.underline}](https://www.techlife-hacking.com/?p=1720)

        -   sudo apt install xserver-xorg-video-dummy

        -   sudo vim /usr/share/X11/xorg.conf.d/80-dummy.conf

            -   Section \"Device\"

            -   Identifier \"Configured Video Device\"

            -   Driver \"dummy\"

            -   VideoRam 256000

            -   EndSection

            -   

            -   Section \"Monitor\"

            -   Identifier \"Configured Monitor\"

            -   HorizSync 5.0 - 1000.0

            -   VertRefresh 5.0 - 200.0

            -   \# 1280x800 59.81 Hz (CVT 1.02MA) hsync: 49.70 kHz;
                > pclk: 83.50 MHz

            -   Modeline \"1280x800\_60.00\" 83.50 1280 1352 1480 1680
                > 800 803 809 831 -hsync +vsync

            -   EndSection

            -   

            -   Section \"Screen\"

            -   Identifier \"Default Screen\"

            -   Monitor \"Configured Monitor\"

            -   Device \"Configured Video Device\"

            -   DefaultDepth 24

            -   SubSection \"Display\"

            -   Depth 24

            -   Modes \"1280x800\"

            -   EndSubSection

            -   EndSection

            -   

            -   Section \"InputClass\"

            -   Identifier \"system-keyboard\"

            -   MatchIsKeyboard \"on\"

            -   Option \"XkbLayout\" \"jp,us\"

            -   Option \"XkbModel\" \"jp106\"

            -   Option \"XkbVariant\" \",dvorak\"

            -   Option \"XkbOptions\" \"grp:alt\_shift\_toggle\"

            -   EndSection

        -   sudo reboot

        -   ダミーディスプレイでなくしたいなら

            -   生成したファイルを削除し、reboot

            -   or

            -   xserver-xorg-video-dummyをremoveする

    -   日本語配列のキーボードに設定

        -   上のバーの言語をクリックする

        -   ＋ボタンでJapaneseを追加

    -   [[service削除コマンド]{.underline}](https://qiita.com/osorezugoing/items/ec53965bc5a026cdb9db)

    -   [[ssdboot]{.underline}](https://qiita.com/kitazaki/items/da5fb46c03781eb7b406)

        -   ssdを挿した状態でsdカードで起動

        -   git clone
            > [[https://github.com/jetsonhacks/rootOnNVMe.git]{.underline}](https://github.com/jetsonhacks/rootOnNVMe.git)

        -   nvme ssdが認識しているか確認

            -   sudo dmesg \| grep nvme

                -   出力

                -   \[ 2.845569\] nvme nvme0: pci function 0005:01:00.0

                -   \[ 2.845615\] nvme 0005:01:00.0: enabling device
                    > (0000 -\> 0002)

                -   \[ 2.973016\] nvme0n1:

        -   予めssdに既存のパーティションがある場合は、すべて削除しておくこと

        -   ./copy-rootfs-ssd.sh

            -   出力

            -   mount: /mnt: special device /dev/nvme0n1p1 does not
                > exist.

            -   1,190,613,704 13% 12.48MB/s 0:01:30 (xfr\#601,
                > to-chk=0/202383)

        -   ./setup-service.sh

            -   出力

            -   ==== AUTHENTICATING FOR
                > org.freedesktop.systemd1.reload-daemon ===

            -   Authentication is required to reload the systemd state.

            -   Authenticating as: jetson,,, (jetson)

            -   Password:

            -   ==== AUTHENTICATION COMPLETE ===

            -   Service to set the rootfs to the SSD installed.

            -   Make sure that you have copied the rootfs to SSD.

            -   Reboot for changes to take effect.

        -   sudo reboot

    -   imuのbuild

        -   git clone
            > [[https://github.com/RTIMULib/RTIMULib2]{.underline}](https://github.com/RTIMULib/RTIMULib2)
            > && cd RTIMULib2

        -   mkdir build && cd build

        -   ccmake ..

        -   make -j4

        -   sudo make install

        -   sudo ldconfig

    -   backupイメージの取得

        -   ssdbootを行っている場合

            -   sudo ./flash.sh -r -k APP -G backup.img
                > jetson-xavier-nx-devkit nvme0n1p

            -   backup.imgは自分側が指定するファイル名なので変更しても良い

        -   sdカードでbootしている場合

            -   sudo ./flash.sh -r -k APP -G backup.img
                > jetson-xavier-nx-devkit mmcblk0p1

        -   途中経過

            -   以下の部分でだいぶ時間かかる

            -   \[ 8.6891 \] tegradevflash\_v2 \--read APP
                > /home/nvidia/nvidia/nvidia\_sdk/JetPack\_4.6.2\_Linux\_JETSON\_XAVIER\_NX\_TARGETS/Linux\_for\_Tegra/backup.img

            -   \[ 8.6896 \] Bootloader version 01.00.0000

            -   \[ 8.7338 \] \[\...\...\... \] 018%

        -   成功結果

            -   \*\*\* The \[APP\] has been read successfully. \*\*\*

            -   Converting RAW image to Sparse image\... size of
                > /home/nvidia/nvidia/nvidia\_sdk/JetPack\_4.6.2\_Linux\_JETSON\_XAVIER\_NX\_TARGETS/Linux\_for\_Tegra/backup.img.raw
                > is not mulple of 4096.

    -   クローンイメージデータのflash

        -   コピーしたイメージデータの移動

            -   backup.imgを\~/nvidia/nvidia\_sdk/JetPack.../Linux\_for\_Tegra/bootloader/system.imgと置き換える

            -   xxxxx.img.rawは使用しない

        -   flash

            -   sudo ./flash.sh -r jetson-xavier-nx-devkit mmcblk0p1

    -   [[jetpackのアップデート]{.underline}](https://hellkite.hatenablog.com/entry/hello_jetson_nx_jetpack502):
        > 5.0.2

        -   dockerでubuntu20.04ベースのイメージをダウンロードする

        -   docker runする

            -   注意点：18.04ベースのイメージとdockerのNameがかぶらないようにする

            -   例

                -   sudo docker run -it \--privileged -v
                    > /dev/bus/usb:/dev/bus/usb/ \--name
                    > JetPack\_NX\_Devkit\_20.04 \--entrypoint /bin/bash
                    > sdkmanager:1.9.3.10904-Ubuntu\_20.04

        -   sudo apt install unzip

        -   sdkmanager \--cli install \--logintype devzone \--product
            > Jetson \--version 5.0.2 \--targetos Linux \--host
            > \--target JETSON\_XAVIER\_NX\_TARGETS \--flash all

        -   chroot関連

            -   sudo apt update

            -   sudo apt install vim binfmt-support binutils

            -   sudo vim /usr/share/binfmts/qemu-aarch64

                -   package qemu-user-static

                -   interpreter /usr/bin/qemu-aarch64-static

                -   flags: OC

                -   offset 0

                -   magic
                    > \\x7fELF\\x02\\x01\\x01\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x02\\x00\\xb7\\x00

                -   mask
                    > \\xff\\xff\\xff\\xff\\xff\\xff\\xff\\x00\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xff\\xfe\\xff\\xff\\xff

            -   sudo mount binfmt\_misc -t binfmt\_misc
                > /proc/sys/fs/binfmt\_misc/

            -   sudo update-binfmts \--enable qemu-aarch64

            -   確認

                -   update-binfmts \--display qemu-aarch64

                    -   enableならok

        -   error: mknod:
            > /home/nvidia/nvidia/nvidia\_sdk/JetPack\_5.0.2\_Linux\_JETSON\_XAVIER\_NX\_TARGETS/Linux\_for
            > \_Tegra/rootfs/dev/random: File exists

            -   sudo rm
                > /home/nvidia/nvidia/nvidia\_sdk/JetPack\_5.0.2\_Linux\_JETSON\_XAVIER\_NX\_TARGETS/Linux\_for\_Tegra/rootfs/dev/random

            -   urandomならそっちも同様に削除する

        -   sdカードを選択すること

            -   nvmeでやったら99%で止まった

            -   次挑戦するならnvmeの中身全部消してからやること

        -   componentsのinstallをスキップすると強制的にリカバリーモードでなくなり起動する

            -   installできないのでスキップせざるを得ない

        -   sudo ./flash.sh jetson-xavier-nx-devkit mmcblk0p1

    -   [[jetson上でdockerでros2の設定]{.underline}](https://developer.nvidia.com/ja-jp/blog/accelerating-ai-modules-for-ros-and-ros-2-on-jetson/)

        -   git clone https://github.com/dusty-nv/jetson-containers

        -   cd jetson-containers

        -   ./scripts/docker\_build\_ros.sh all \# build all: melodic,
            > noetic, eloquent, foxy

        -   ./scripts/docker\_build\_ros.sh melodic \# build only
            > melodic

        -   ./scripts/docker\_build\_ros.sh noetic \# build only noetic

        -   ./scripts/docker\_build\_ros.sh eloquent \# build only
            > eloquent

        -   ./scripts/docker\_build\_ros.sh foxy \# build only foxy

    -   [[jetson AGX
        > OrinでROS2Humbleを動かす]{.underline}](https://qiita.com/porizou1/items/3ad4b0ed1e80c0dd42cf)

        -   git clone https://github.com/dusty-nv/jetson-containers

        -   cd jetson-containers

        -   docker pull dustynv/ros:humble-desktop-l4t-r35.3.1

        -   docker images

            -   以下が出力される

            -   REPOSITORY TAG IMAGE ID CREATED SIZE

            -   dustynv/ros humble-desktop-l4t-r35.3.1 9b298d9c584d 2
                > months ago 12.8GB

            -   nvcr.io/nvidia/l4t-jetpack r35.3.1 ff2dd43d5687 3 months
                > ago 9.77GB

        -   ./scripts/docker\_run.sh -c
            > dustynv/ros:humble-desktop-l4t-r35.3.1

        -   rviz2

            -   rviz2などが動くか確認

        -   

-   Docker

    -   Dockerfileやdocker内でなにかをinstallする場合は以下のようにすること

        -   apt-get update && apt-get install
            > \<インストールするパッケージ\>

        -   [[dockerのapt関係でのエラーの対処法]{.underline}](https://qiita.com/teriyakisan/items/e5cf7d5228dc02500562)

    -   [[バインドマウント]{.underline}](https://www.ogis-ri.co.jp/otc/hiroba/technical/docker/part7.html)

        -   適用例（strateagy\_dev）

            -   -v \$PWD/../src/pyfiles:/pyfiles:rw \\

    -   [[変更を加えたコンテナを保存する]{.underline}](https://www.mtioutput.com/entry/it/docker-containercommit)

        -   docker psで変更を加えたコンテナIDを確認

        -   docker container commit \<コンテナID\> \<イメージ名\>

        -   docker push \<user-name\>/\<イメージ名\>:\<tag\>

    -   [[コンテナ名のコンフリクト]{.underline}](https://medium.com/@rukurx/docker%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E5%90%8D%E3%81%8C%E3%82%B3%E3%83%B3%E3%83%95%E3%83%AA%E3%82%AF%E3%83%88%E3%81%97%E3%81%9F-1ae48a8a722c)

        -   コンテナの削除

            -   docker rm \<container-name\>

        -   コンテナが起動中であれば -f オプションをつけて強制削除

            -   docker rm -f \<container-name\>

        -   コンテナをrename

            -   docker rename \<container-name\> \<new-container-name\>

    -   [[停止中 or
        > 稼働中のUbuntuコンテナのBashに入る]{.underline}](https://kei-s-lifehack.hatenablog.com/entry/docker-use-stopped-or-running-ubuntu-container-bash)

        -   停止している（exitした）コンテナを動かす

            -   docker start \<container-ID\>

            -   docker attach \<container-ID\>

-   ROS 2

    -   ROS 2のインストール

        -   [[授業用ROS
            > 2資料]{.underline}](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson8.md)

        -   [[上田先生のROS
            > 2インストーラー]{.underline}](https://github.com/ryuichiueda/ros2_setup_scripts)でcloneして./setup.bash

        -   \~/.bashrcに以下を追加

            -   source \~/ros2\_ws/install/setup.bash

            -   source \~/ros2\_ws/install/local\_setup.bash

        -   [[池邉先輩のインストールスクリプト]{.underline}](https://github.com/uhobeike/ros2_humble_install_script/blob/main/install_desktop.sh)を実行

        -   gazeboのインストール

            -   sudo apt update && sudo apt install curl

            -   sudo curl -sSL
                > https://raw.githubusercontent.com/ros/rosdistro/master/ros.key
                > -o /usr/share/keyrings/ros-archive-keyring.gpg

            -   echo \"deb \[arch=\$(dpkg \--print-architecture)
                > signed-by=/usr/share/keyrings/ros-archive-keyring.gpg\]
                > http://packages.ros.org/ros2/ubuntu \$(.
                > /etc/os-release && echo \$UBUNTU\_CODENAME) main\" \|
                > sudo tee /etc/apt/sources.list.d/ros2.list \>
                > /dev/null

            -   sudo apt update -y && sudo apt upgrade -y

            -   sudo apt install gazebo

            -   sudo apt install ros-humble-gazebo-\*

            -   source \~/.bashrc

            -   メモ：ros-humble-gazebo-\*をインストールしようとした際に、libgazebo11...みたいなものの依存関係がどうたらこうたらと出力された際には、依存関係にあるパッケージをsudo
                > apt remove \<パッケージ名\> && sudo apt
                > autoremoveで削除し、sudo apt install
                > gazeboからやり直す

            -   aptの特にupdateでエラーが起きた時には/etc/apt/source.list.d/の中の、エラーにあるリンクの書かれたファイルを削除し、再度updateする

    -   [[公式ドキュメント]{.underline}](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html)：humble

    -   launchファイルが共有ディレクトリに見つかりませんでしたエラー

        -   launchファイルをlaunchした時に起こった

        -   CMakeLists.txtに以下が必要

            -   install(DIRECTORY launch

            -   DESTINATION share/\${PROJECT\_NAME})

    -   yamlでのパラメータの定義

        -   パッケージ直下にconfig/ディレクトリを作成しそこに保存する

        -   node\_name1:

        -   ros\_\_parameters:

        -   param1: 30

        -   param2: "string"

        -   param3: true

        -   param4: \[0, 1, 2\]

    -   [[launchファイルでyamlをパラメータとして読み込ませる]{.underline}](https://roboticsbackend.com/ros2-yaml-params/)

        -   yamlファイルの準備

        -   launchファイルでconfig(yaml)のパスをわからせる

            -   config = os.path.join(get\_package\_share\_directory(\
                > \'パッケージ名\'),\
                > \'config\', \'params.yaml\')

            -   Node(\
                > ....\
                > parameters = \[config\])

        -   setup.pyの編集

            -   ...

            -   data\_files=\[\
                > ...,\
                > (os.path.join('share', package\_name,
                > 'config'),glob('config/\*.yaml')) \]

        -   CMakeLists.txtの編集

            -   ...

            -   install(DIRECTORY\
                > launch\
                > DESTINATION share/\${PROJECT\_NAME}\
                > )

            -   install(DIRECTORY\
                > config\
                > DESTINATION share/\${PROJECT\_NAME}\
                > )

            -   ...

        -   launchファイルではなく、ros2 runでyamlでパラメータ渡す方法

            -   ros2 run \<package\_name\> \<node\_name\> --ros-args -r
                > \_\_ns:=/ns1 --params-file
                > \<yamlファイルへの絶対パス\>

    -   [[パラメータの使い方]{.underline}](https://qiita.com/shigeharu_shibahata/items/82e8f562d2e6395ba115)

        -   declare\_parameter()する

    -   github/actionsでのtestのやり方：ロボシス

        -   [[mypkgでのtest.yml]{.underline}](https://github.com/IkuoShige/mypkg/blob/main/.github/workflows/test.yml)

    -   [[backward-ros]{.underline}](https://zenn.dev/ame_b/articles/043dea8ecc9d8e)

        -   sudo apt install ros-humble-backward-ros

        -   CMakeLists.txtに以下を追記

            -   find\_package(abckward\_ros REQUIRED)

            -   ament\_auto\_executable(hoge hoge.cpp)

            -   add\_backward(hoge)

        -   buildのやり方

            -   colcon build --symlink-install --camke-args
                > -DCMAKE\_BUILD\_TYPE=Debug

    -   特定のパッケージのみをbuildする

        -   colcon build \--packages-select \[パッケージ名\]

    -   [[ROS
        > 2ノードをgdbでデバッグ]{.underline}](https://zenn.dev/shotaak/articles/e03f4c85497395)

        -   これでgdbによるデバッグができる

    -   [[1つのプロセスに複数のノードを実装]{.underline}](https://qiita.com/shigeharu_shibahata/items/60f547d2ea9ccd8c1b6b)

        -   実装方法

            -   rclcpp::executors::SingleThreadedExecutorを使う

            -   auto node\_1 = std::make\_shared\<コンストラクタ\>()

            -   exec.add\_node(node\_1)

            -   exec.spin()

    -   [[ament\_cmake\_autoを使ったROS2
        > CMake]{.underline}](https://hans-robo.hatenablog.com/entry/2020/12/15/153503)

-   emcl2ros2移行作業ログ

    -   buildコマンド

        -   colcon build --symlink -install --cmake-args
            > -DCMALE\_BUILD\_TYPE=Debug

    -   動作確認コマンド

        -   ros2 launch raspicat\_gazebo
            > raspicat\_with\_iscas\_museum.launch.py gui:=false

        -   ros2 launch raspicat\_navigation raspicat\_nav2.launch.py

        -   ros2 run emcl2 emcl2\_node --ros-args --params-file
            > ./src/emcl2\_ros/config/emcl2.param.yaml

    -   MCLの宣言はmap等の情報を受け取ってから

        -   尤度がカンストする

    -   上田研githubでのcommit messageの頭文字は大文字

    -   **間違えたpushをなかったことにしたコマンド：要調査**

        -   git push --force-with-lease

        -   コミットそのものを消した

    -   rvizにパーティクルや尤度、センサデータが描画されない状態で、以下のエラーが見られた

        -   tf関係のマップ情報と座標系の計算が噛み合っていないから

        -   lidar\_linkのフレームがフィルタードロップしている

        -   global\_constmapがタイムアウト、base\_linkからmap情報にtransformするのがエラーしている

        -   解決方法

            -   githubのプルリクに変更の履歴が残っているのでそれを参照

-   github

    -   github開発ブランチにデフォルトブランチのコミットを反映する

        -   開発ブランチに移動

        -   git fetch

        -   git merge origin/main

        -   コンフリクトがあれば、解消してからコミットする

        -   git push origin \<開発ブランチ\>

    -   github開発ブランチのマージ

        -   mainブランチに移動

        -   git pullしてmianブランチを最新にする

        -   git merge \<開発ブランチ\>

        -   mainにpushする

    -   githubコンフリクト解消方法

        -   \<\<\<\<\<\<HEAD と \>\>\>\>\>\>\>\>\>merge先のブランチ名

            -   の内容が差分なのでどちらを残すか選び、それ以外を削除する

        -   コンフリクトが起こっているファイルをgit add して、git commit
            > する

        -   コンフリクトが起こる直前にしようとしていたコマンドを実行する

    -   [[gitで管理されたファイルをignoreする]{.underline}](https://qiita.com/sf213471118/items/efbc0abf028a3ead72e7)

        -   git rm \--cached \<file or directory\>

            -   指定ファイルを上記コマンドでgitの管理外に変更

        -   その後.gitignoreに記述するなりなんかする

        -   特定のファイルをignoreする

            -   src/test.cpp

        -   特定のフォルダをignoreする

            -   /hoge/

    -   [[github/actionsでのテスト構築方法]{.underline}](https://github.com/ryuichiueda/my_slides/blob/master/robosys_2022/lesson7.md)

        -   mkdir -p .github/workflows

        -   cd .github/workflows

        -   touch test.yml

        -   test.ymlの中身

            -   参考：[[ロボシス]{.underline}](https://github.com/IkuoShige/mypkg/blob/main/.github/workflows/test.yml)、[[ROS2勉強会]{.underline}](https://github.com/IkuoShige/myname_pubsub/blob/main/.github/workflows/build.yml)

            -   上田先生流だとdockerコンテナで仮想環境立ててbuildする

    -   [[fatal: Need to specify how to reconcile divergent
        > branches.のエラーが発生]{.underline}](https://qiita.com/aogangcun/items/9d43c7b1aa6b616f9ce8)

        -   pullしようとしたらエラーにぶつかった

        -   git config pull.rebase false

        -   git pull origin main

    -   [[error: failed to push some refs to
        > \'github.com:IkuoShige/\<repository\>\']{.underline}](https://qiita.com/cccccccccc/items/118a5b3237c78d720582)

        -   hint: Updates were rejected because the tip of your current
            > branch is behind

        -   hint: its remote counterpart. Integrate the remote changes
            > (e.g.

        -   hint: \'git pull \...\') before pushing again.

        -   hint: See the \'Note about fast-forwards\' in \'git push
            > \--help\' for details.

        -   解決法

            -   git fetch

            -   git merge origin/main main

                -   リモートブランチ ローカルブランチ

            -   git push origin main

    -   git add を取り消す

        -   git init直後

            -   git rm --cached -r .

                -   すべてのファイルを取り消し

            -   git rm --cached -r file\_name

                -   特定のファイルのみ取り消し

        -   2回目以降のgit add を取り消す

            -   git reset HEAD

                -   すべてのファイルを取り消し

            -   git reset HEAD file\_name

                -   特定のファイルのみ取り消し

    -   **git rebaseの調査**

    -   **git push --force-with-leaceの調査**

    -   **ただのmergeとsquash and mergeの違いの調査**

-   anydeskのDisplay\_Server\_Not\_Supportedエラーの解決方法をどこかに記す完了

    -   [[サイト]{.underline}](https://medium.com/@Dylan.Wang/how-to-fix-anydesk-of-display-server-not-supported-error-for-ubuntu-22-04-c98c44de89c0)

    -   /etc/gdm3/custom.confを以下のように変更する

        -   WaylandEnable=false

        -   AutomaticLoginEnable = true

        -   AutomaticLogin = \$USERNAME

-   GAS

    -   [[GAS経由でslackbotにスレッド返信で通知させる]{.underline}](https://zenn.dev/scnsh/articles/6791519a806463)

        -   これでGASからslackにスレッドで飛ばせるかも

-   GPUドライバーの再インストール方法：5/2更新

    -   参考リンク(手順通り)

        -   [[リンク1]{.underline}](https://misoji-engineer.com/archives/reinstall-cuda-on-ubuntu.html)で既存のdriverとcudaをアンインストール

        -   [[リンク2]{.underline}](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local)からcuda-tool-kitのインストール

        -   [[リンク3]{.underline}](https://qiita.com/Menrui/items/01d525b11d91b970c279)でnvidia-docker2の再インストール

    -   作業履歴：gpuドライバの再インストール0

        -   [[出力結果]{.underline}](https://www.google.com/search?channel=fs&client=ubuntu&q=NVIDIA-SMI+has+failed+because+it+couldn%27t+communicate+with+the+NVIDIA+driver.+Make+sure+that+the+latest+NVIDIA+driver+is+installed+and+running.)

        -   とりあえずシミュレータは使えるようになったけどvnccは再インストールしないといけない

        -   多分cudaのバージョンは10.1だけど12.1まで上げることができる

        -   cudaのディレクトリがおかしい気がする

        -   時間があれば再インストールすべき

            -   runfileとか？

            -   今回はdebのlocalでやった

    -   作業フロー最新版

        -   [[リンク1]{.underline}](https://misoji-engineer.com/archives/reinstall-cuda-on-ubuntu.html)で既存のdriverとcudaをアンインストール

            -   sudo apt-get \--purge remove nvidia\*

            -   sudo apt-get \--purge remove cuda\*

            -   sudo apt-get \--purge remove cudnn\*

            -   sudo apt-get \--purge remove libnvidia\*

            -   sudo apt-get \--purge remove libcuda\*

            -   sudo apt-get \--purge remove libcudnn\*

            -   sudo apt-get autoremove

            -   sudo apt-get autoclean

            -   sudo apt-get update

            -   うまく行かないときはsudo apt-get --purge
                > するときに前回インストールしたときにダウンロードしたものを極力削除する

                -   ex: rm
                    > cuda-repo-ubuntu2004-12.1.1-530.30.02-1\_amd64.deb

        -   [[リンク2]{.underline}](https://qiita.com/2yuu/items/e62367007380e3c564f7)でcudaをインストールする

            -   wget
                > https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86\_64/cuda-ubuntu2004.pin

            -   sudo mv cuda-ubuntu2004.pin
                > /etc/apt/preferences.d/cuda-repository-pin-600

            -   wget
                > https://developer.download.nvidia.com/compute/cuda/12.1.1/local\_installers/cuda-repo-ubuntu2004-12-1-local\_12.1.1-530.30.02-1\_amd64.deb

            -   sudo dpkg -i
                > cuda-repo-ubuntu2004-12-1-local\_12.1.1-530.30.02-1\_amd64
                > deb

            -   sudo cp
                > /var/cuda-repo-ubuntu2004-12-1-local/cuda-\*-keyring.gpg
                > /usr/share/keyrings/

            -   sudo apt-get update

            -   sudo apt-get -y install cuda

            -   sudo reboot

        -   [[リンク2]{.underline}](https://qiita.com/2yuu/items/e62367007380e3c564f7)でcudnnをインストールする

            -   [[ここ]{.underline}](https://developer.nvidia.com/rdp/cudnn-archive)からTarのやつをダウンロードする

            -   Tar型のファイルがある階層に移動する

            -   tar -xvf
                > cudnn-linux-x86\_64-8.9.0.131\_cuda12-archive.tar.xz

            -   sudo cp cudnn-\*-archive/include/cudnn\*.h
                > /usr/local/cuda-12.1/include

            -   sudo cp -P cudnn-\*-archive/lib/libcudnn\*
                > /usr/local/cuda-12.1/lib64

            -   sudo chmod a+r /usr/local/cuda-12.1/include/cudnn\*.h
                > /usr/local/cuda-12.1/lib64/libcudnn\*

            -   \~/.bashrcに以下を記述

                -   export PATH=\"/usr/local/cuda/bin:\$PATH\"

                -   export
                    > LD\_LIBRARY\_PATH=\"/usr/local/cuda/lib64:\$LD\_LIBRARY\_PATH\"

            -   cpで上書きできないときはちゃんとパスを指定して上げるとうまく行く

        -   nvidia-smi, nvcc -Vでバージョンを確認する

        -   main.cuで動作確認する

            -   main.cu

                -   \#include \<stdio.h\>

                -   

                -   \_\_global\_\_ void hello(){

                -   printf(\"Hoge\\n\");

                -   }

                -   

                -   int main () {

                -   hello\<\<\<1,1\>\>\>();

                -   cudaDeviceSynchronize();

                -   }

            -   nvcc main.cuでコンパイルし, ./a.outで実行

                -   Hogeが出力されればok

    -   dockerでgpu使えるようにする方法

        -   [[リンク]{.underline}](https://jskangaroo.hatenablog.com/entry/2021/08/17/150002)

        -   docker: Error response from daemon: could not select device
            > driver \"\" with capabilities:
            > \[\[gpu\]\].のエラーが出るときに有効

-   ROS 2課題のみんなの総評まとめ

    -   みんなの総評

        -   pubsubで2つのノードを一つのファイルでやることを指定した理由が気になる

            -   興味本位

        -   buildが2個あるから消す

        -   rosの構築のactionsに時間かかっているからそのツール使うのやめる

        -   backward-rosはpackage.xmlに書いとけばインストールする必要なし

        -   executorで、同じ変数をコール罰kうで読もうとするとエラーが起きるかもしれない

            -   multiよりもsingleの方が安全

            -   バグのもととなる可能性が高い

        -   thisを毎回かいた方が明示的で良いのでは？yazawa

        -   コメントアウトに!をつけることで、ドキシジェンを表現することができる

            -   ローカルルールかも、見直すべき

        -   変数の初期化はコンストラクタのとなるに書いたほうがいい

            -   本来そこに記述するべき

        -   ros2のシバンは書いている人あまりいない

            -   いらないかも

            -   上田先生曰くros2 では勝手に読み込んでくれるらしい

        -   長ったらしいですねんながき

            -   それぞれの関数を作ったほうが短くする

            -   コンストラクタはスマートに書くべき

            -   1つの関数には10行まで上田先生いわく

        -   NodeOptionsはコンポーネントの名残

            -   今はなくても良い

        -   paramファイルのパラメタを使いまわしたいからparamの1行目はのーどの名前でなくても良い

            -   /\*\*

                -   名前すべてに対応

        -   コンストラクタがスマートけんぞー

        -   左でパラメータが入るから←そこは直打ちでもよい

        -   declearでyamlファイルからパラメータは受け取れない、get\_parameterのみから受け取れる

-   imuの値取得周期

    -   humanoid\_robotを参照する

    -   サンプリングレートは1000000usecぽい？(1Hz)

        -   サンプリングレートとは？

    -   自己位置のimuのデータ自体はHPLの周期に依存している

        -   HPLの周期の中で一番遅いのがvisionの30Hzで随時更新している

        -   imuの値の取得自体はべつスコープでやっていて100Hz

        -   visionが30Hzで最新のimuの値が入る

        -   使用パラメータはyawのみ

        -   スライドにまとめた[[230511\_ゼミ発表資料\_茂郁良]{.underline}](https://docs.google.com/presentation/d/1j3zh6BB7M8k9jdOtjHslxNc1V4UOaTSG/edit?usp=sharing&ouid=100434429296543889494&rtpof=true&sd=true)

-   raspicat\_sim

    -   エラー

        -   ERROR: the following rosdeps failed to install

        -   apt: command \[sudo -H apt-get install -y
            > ros-humble-gazebo-plugins\] failed

        -   apt: command \[sudo -H apt-get install -y
            > ros-humble-gazebo-ros\] failed

        -   apt: command \[sudo -H apt-get install -y
            > ros-humble-turtlebot3-gazebo\] failed

        -   apt: Failed to detect successful installation of
            > \[ros-humble-gazebo-plugins\]

        -   apt: Failed to detect successful installation of
            > \[ros-humble-gazebo-ros\]

        -   apt: Failed to detect successful installation of
            > \[ros-humble-turtlebot3-gazebo\]

-   ポスター作成

    -   上田先生の指摘を修正する

        -   背景の理由が書いてあるけどなんの理由なのかが書いていない意味不明

            -   回復を図るなぜ

                -   自己位置推定が破綻する可能性があるなぜ

                    -   MCLは位置推定が常に成功することが前提で結果が使用されるから

                    -   なんの理由？

                        -   主語らしきものがない？

            -   MCLが出てくる理由

                -   自立型二足歩行ロボット: GankenKun\[1\]の自己位置推定

            -   なんの位置推定かが書かれていない

        -   自己位置の回復ってなあに？

            -   自己位置推定の破綻からの回復

        -   これ赤井さんの話？

            -   研究目的にカメラの話が出るのでそれよりまえにカメラを使う導入の話を入れる必要があるが、入れる場所に困って関連研究の後半に入れた

        -   目的は「カメラベースの自己位置推定に赤井さん手法を適用する」でいいんじゃない？

            -   目的を「カメラベースの自己位置推定に赤井さん手法を適用する」に変更

        -   「置き換える」を体言止めに→置き換え or 置換

            -   「置き換え」に統一

-   [[BalenaEtcherのインストール方法（ubuntu22.04）]{.underline}](https://linux.how2shout.com/how-to-install-balenaetcher-on-ubuntu-22-04-lts/)

    -   [[https://github.com/balena-io/etcher/releases/tag/v1.18.11]{.underline}](https://github.com/balena-io/etcher/releases/tag/v1.18.11)

        -   上記リンクからdebファイルをダウンロードする

    -   Ubuntu Universeリポジトリを有効にする

        -   sudo add-apt-reposistory universe

    -   22.04へのインストール

        -   sudo apt install ./Downloads/\<downloaded-filename\>
