* マニュアル作成編
    * sdkmanagerでのjetsonにインストールするためのjetpackのダウンロードを行った後、jetsonが起動するまで待つ
    * 設定したパスワードでloginする
    * wifiの設定をする
        * ipアドレス固定
        * 無線でも有線でも可
        * 設定完了後、wifi再起動
    * ジャンパ線外す
    * ダウンロード後に出てきたウィンドウのinstallを押す
    * cloneimageの取得
        * sudo ./flash.sh -r -k APP -G demo_backup.img jetson-xavier-nx-devkit mmcblk0p1
        * 出力
            * [   7.8018 ] tegradevflash_v2 --read APP /home/nvidia/nvidia/nvidia_sdk/JetPack_5.1.1_Linux_JETSON_XAVIER_NX_TARGETS/Linux_for_Tegra/demo_backup.img
            * [   7.8026 ] Bootloader version 01.00.0000
            * [   7.8539 ] 000000000d0f010e: E> NV3P_SERVER: Could not read 1048576 bytes from partition APP.
            * [ 4291.4967 ]
            * [ 4291.4969 ]
            * Error: Return value 14
            * Command tegradevflash_v2 --read APP /home/nvidia/nvidia/nvidia_sdk/JetPack_5.1.1_Linux_JETSON_XAVIER_NX_TARGETS/Linux_for_Tegra/demo_backup.img
            * *** The [APP] has been read successfully. ***
            *     Converting RAW image to Sparse image…
    * clone imageのflash
        * sudo ./flash.sh -r jetson-xavier-nx-devkit mmcblk0p1
        * 出力
            * [ 4030.1865 ] Flashing completed      	 
            *                                       	 
            * [ 4030.1866 ] Coldbooting the device     	 
            * [ 4030.1897 ] tegrarcm_v2 --ismb2     	 
            * [ 4030.2213 ] tegradevflash_v2 --reboot coldboot
            * [ 4030.2224 ] Bootloader version 01.00.0000
            * *** The target t186ref has been flashed successfully. ***
            * Reset the board to boot from internal eMMC.
        * biosのnvidiaの画面から進まない
        * sudo ./flash.sh -r -k APP jetson-xavier-nx-devkit mmcblk0p1
        * 再度実行-rのみのflash: 1834
            * bootしない
        * demo_backup.img.rawをsystem.imgに変換してflash -r
            * sdカードの中身そのまま
            * 失敗
                * Error: Return value  3
                * Command tegradevflash_v2 --pt flash.xml.bin --create
                * Failed flashing t186ref.
            * sdカードの中身削除して再度flash -r
                * 失敗
                * -k APPでflashしてみる
                * 時間足りなくて強制終了
        * 既存のイメージでも起動しなくなっていたので、sdkmanager_dockerで再度インストール
        * backupの取得失敗
            * e nv3p_server could not read from partitionAPP
        * flash.shでできるのは、emmcが搭載されているTX2やボードのxavier-nxとかじゃないとできない
    * [ddコマンドによるsdカードのクローン](https://jetsonhacks.com/2020/08/08/clone-sd-card-jetson-nano-and-xavier-nx/)
        * microsdカードとusb変換器よりもmicro→sdカード変換器のほうが速度早いかもしれない
        * sudo parted -l
            * 警告出たら無視（I）でおｋ
            * sdカードがどのパスか確かめる
            * 出力一部
                * モデル: Generic- SD/MMC (scsi)
                * ディスク /dev/sda: 125GB
                * セクタサイズ (論理/物理): 512B/512B
                * パーティションテーブル: gpt
            * パス
                * /dev/sda
        * sudo umount /dev/sda
        * sudo dd if=/dev/sda conv=sync,noerror bs=4M status=progress | gzip -c > ~/backup_jetson_dd/230822_backup_image.img.gz
        * sudo su
            * 必要
        * gunzip -c 230822_backup_image.img.gz | dd of=/dev/sda bs=4M status=progress
            * root権限なので、~/がつかえないので注意
            * sdcardスロット
                * gunzip -c 230822_backup_image.img.gz | dd of=/dev/mmcblk0 bs=4M status=progress
        * 終わり
            * ddしたsdカードをjetsonに挿して起動できる
