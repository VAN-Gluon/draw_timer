# draw_timer

ジェスチャードローイング用タイマーソフトです。以下の条件を満たすものがサクッと見つからなかったので、作ってみました。
- 非アクティブでもホットキーに反応する
- 指定した音声ファイルを鳴らす
- 無限に待機し、入力があった時だけ動作する

## 使い方

1. 以下のファイルを、ひとつのディレクトリーに入れて下さい。
    - 実行ファイル(timer.exe)
    - 設定ファイル(settings.json)
    - 音声ファイル(任意のWAVファイル)

2. 設定ファイルの項目を書き換えて下さい。
    - time(タイマー時間、秒単位)
    - wave(1.で用意した音声ファイルの名前)
    - hotkey(タイマーを起動するキーの組み合わせ)

3. 実行ファイルを起動すると、プロンプトが立ち上がります。

4. 指定したキーの組み合わせを入力すると、timeで設定した秒数のカウントが表示されます。

5. カウントし終わると音声ファイルが再生され、終了次第4.に戻ります。

## 動かない場合

- 「使い方」の1.を参考に、もう一度ファイルの配置を見直して下さい。
- 起動後に操作を受け付けなくなった場合は、このツールを再起動して下さい。

## TIPS

- Windows 10 Home(22H2)で動作確認しています。
- CLIP STUDIO TABMATEで操作したい場合、JoyToKey( https://joytokey.net/ja/ )等を経由してご利用下さい。

## 使用ライブラリー

このソフトは下記のライブラリーを使用して開発されています。
Name                       Version   License                                                         URL                                                       Description                                                                              
altgraph                   0.17.4    MIT License                                                     https://altgraph.readthedocs.io                           Python graph (network) package                                                           
keyboard                   0.13.5    MIT License                                                     https://github.com/boppreh/keyboard                       Hook and simulate keyboard events on Windows and Linux                                   
pefile                     2023.2.7  MIT                                                             https://github.com/erocarrera/pefile                      Python PE parsing module                                                                 
pyinstaller                5.13.0    GNU General Public License v2 (GPLv2)                           https://www.pyinstaller.org/                              PyInstaller bundles a Python application and all its dependencies into a single package. 
pyinstaller-hooks-contrib  2023.9    Apache Software License; GNU General Public License v2 (GPLv2)  https://github.com/pyinstaller/pyinstaller-hooks-contrib  Community maintained hooks for PyInstaller                                               
pywin32-ctypes             0.2.2     BSD-3-Clause                                                    https://github.com/enthought/pywin32-ctypes               A (partial) reimplementation of pywin32 using ctypes/cffi                                
simpleaudio                1.0.4     MIT License                                                     https://github.com/hamiltron/py-simple-audio              Simple, asynchronous audio playback for Python 3.                                        
