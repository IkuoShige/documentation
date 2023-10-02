# Jetsonのクローン/リストア

## 1. クローンイメージの取得

以下のコマンドを使用してクローンイメージを取得する。

```bash
sudo ./flash.sh -r -k APP -G demo_backup.img jetson-xavier-nx-devkit mmcblk0p1
```

## 2. クローンイメージのフラッシュ
!!! warning
    この方法で有効なのは、使用しているJetsonがemmc対応している場合のみ

クローンイメージをJetsonデバイスにフラッシュする。

```bash
sudo ./flash.sh -r jetson-xavier-nx-devkit mmcblk0p1
```

もしJetsonが起動しない場合、以下のコマンドを試してみてください。

```bash
sudo ./flash.sh -r -k APP jetson-xavier-nx-devkit mmcblk0p1
```


## 3. ddコマンドを用いたクローン
!!! note
    emmcに対応していないJetsonはこの方法が有効

=== "SDカード→SDカード"

    [ddコマンドによるSDカードのクローン](https://jetsonhacks.com/2020/08/08/clone-sd-card-jetson-nano-and-xavier-nx/)を使用してSDカードをクローンします。以下は手順の概要です。

    1. `sudo parted -l` を使用してSDカードのパスを確認
    1. `sudo umount /dev/sdX` を実行してSDカードをアンマウント

        !!! example
            - クローン元: /dev/sdX
            - クローン先: /dev/sdY

    1. ディスクのイメージを作成
        ```bash
        sudo dd if=/dev/sdX conv=sync,noerror bs=4M status=progress | gzip -c > ~/backup_jetson_dd/230822_backup_image.img.gz
        ```
    1. ディスクのイメージのリストア
        <!-- gunzip -c 230822_backup_image.img.gz | sudo dd of=/dev/mmcblk0 bs=4M status=progress -->
        ```bash
        gunzip -c 230822_backup_image.img.gz | sudo dd of=/dev/sdY bs=4M status=progress
        ```
    1. クローンが完了したらSDカードをJetsonデバイスに挿し、起動する

=== "nvme→nvme"
    [ddコマンドによるSDカードのクローン](https://jetsonhacks.com/2020/08/08/clone-sd-card-jetson-nano-and-xavier-nx/)を使用してSDカードをクローンします。以下は手順の概要です。

    1. `sudo parted -l` を使用してnvme_ssdのパスを確認
    1. `sudo umount /dev/sdX` を実行してnvme_ssdをアンマウント

        !!! example
            - クローン元: /dev/sdX
            - クローン先: /dev/sdY

    1. ディスクのイメージを作成
        ```bash
        sudo dd if=/dev/sdX conv=sync,noerror bs=4M status=progress | gzip -c > ~/backup_jetson_dd/230822_backup_image.img.gz
        ```
    1. ディスクのイメージのリストア
        <!-- gunzip -c 230822_backup_image.img.gz | sudo dd of=/dev/nvme0n1 bs=4M status=progress -->
        ```bash
        gunzip -c 230822_backup_image.img.gz | sudo dd of=/dev/sdY bs=4M status=progress
        ```
    1. クローンが完了したらSDカードをJetsonデバイスに挿し、起動する

=== "nvme→SDカード"
    
    1. GpartedでパーティションをまるごとSDカードにコピー

        !!! warning
            パーティションの順番に注意
        
    1. SDカードをマウントし、/boot/extlinux/extlinux.confをsudo権限で編集する
    ```diff linenums="11"
    -   APPEND ${cbootargs} root=PARTUUID=ec4e95cb-c321-4554-9e9e-7b34b17ffe35 rw rootwait rootfstype=ext4 console=ttyTCU0,115200n8 console=tty0 fbcon=map:0 net.ifnames=0 video=efifb:off nv-auto-config
    +  	APPEND ${cbootargs} root=/dev/mmcblk0p1 rw rootwait rootfstype=ext4 console=ttyTCU0,115200n8 console=tty0 fbcon=map:0 net.ifnames=0 video=efifb:off nv-auto-config
    ```
    1. SDカードをアンマウントして外し、Jetsonデバイスに挿し、起動する

    !!! info
        `ec4e95cb-c321-4554-9e9e-7b34b17ffe35` は、nvmeでのbootのパーティションのUUIDを示している


## 4. 参考

<iframe class="hatenablogcard" style="width:100%;height:155px;max-width:680px;" title="%text%" src="https://hatenablog-parts.com/embed?url=https://jetsonhacks.com/2020/08/08/clone-sd-card-jetson-nano-and-xavier-nx/" width="300" height="150" frameborder="0" scrolling="no"> </iframe> 