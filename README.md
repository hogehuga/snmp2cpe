# snmp2cpe (SNMP sysDescription To CPE)

sysDescriptionのデータが足りなくて開発ができません。情報をください！

- snmp2cpe を実行してください
- `cpeName:` が `Can not match CPE.` と出ている場合は、以下の情報をIssueで下さい。
  - `snmpDescr` の情報
  - 可能なら、ファームウェアや機器の情報(例えば、`Cisco IOS 12.2(17d)SXB11` など)。なくても大丈夫。
  - 余力のある人は、 `cpe.py` , `test_cpe.py` を書き換えてPullRequest下さい。

Unable to develop due to lack of sysDescription data. Please tell me the information!

- execute snmp2cpe
- If cpeName "does not match CPE", pull request the following:
  - `snmpDescr` information.
  - If possible, firmware and device information (for example, `Cisco IOS 12.2 (17d) SXB11`). (Not requred)
  - If possible, please rewrite `cpe.py`,` test_cpe.py` and pull request.

## Abstruct

SNMPGETを用いて、機器のファームウェアバージョンを取得し、CPEに変換します
現時点ではPoCなので、snmpget/snmpwalkはOSパッケージのコマンドを利用しています。

注意；まだ一部のCPE変換しか実装していません。IssueでのsysDescription提供ご協力をお願いします。

- PoCという位置づけです。sysDescriptionの情報が少なすぎる
- Cisco IOSの一部に対応

Use SNMPGET to get the firmware version of the device and convert it to CPE.
Since it is a PoC at the moment, snmpget / snmpwalk uses the commands of the OS package.

Note: Only some CPE conversions have been implemented yet. Thank you for your cooperation in providing sysDescription in Issue.

- It is positioned as PoC. Too little information on sysDescription
- Compatible with parts of Cisco IOS

## Prerequisites

OSパッケージのsnmp、python3の環境が必要です。
パッケージのSNMPを利用するのは、ライブラリインストールによる環境変化を避けるためです。 (PoC)
対象機器がSNMP応答をする必要があります。

- Ubuntu 20.04 LTS + `apt-get install snmp` で開発しています。
- sysDescription および sysName を取得します。


OS package snmp, python3 environment is required.
The purpose of using the package SNMP is to avoid changes in the environment due to library installation.
The target device needs to make an SNMP response.

- I developing on Ubuntu 20.04 LTS + `apt-get install snmp` 
- Get sysDescription and sysName by snmpget.

## Usage

1. このリポジトリをCloneします
2. helpを確認します。
3. 対象機器のIP/SNMPバージョン/CommunityNameを指定します。
4. CPEを推定できた場合は、CPENameを返します。

1. Clone this repository
2. Check for help.
3. Specify the IP / SNMP version / Community Name of the target device.
4. If the CPE can be estimated, return the CPEName.

```
$ git clone https://github.com/hogehuga/snmp2cpe
$ cd snmp2cpe
$ ./snmp2cpe.py
usage: snmp2cpe.py [-h] -ip IPADDRESS -v {2c,3c} -c COMMUNITY

program description

optional arguments:
  -h, --help            show this help message and exit
  -ip IPADDRESS, --ipaddress IPADDRESS
                        scan ip address
  -v {2c,3c}, --version {2c,3c}
                        SNMP version
  -c COMMUNITY, --community COMMUNITY
                        SNMP community name
$ ./snmp2cpe.py -v 2c -c public 192.168.0.1
sysName   :device-SysName
cpeName   :cpe:2.3:o:cisco:ios:15.1\(4\)M4:*:*:*:*:*:*:*
snmpDescr :"Cisco IOS Software, C181X Software (C181X-ADVENTERPRISEK9-M), Version 15.1(4)M4, RE...(snip"
```

まだCPE推定が実装できていないものは、`Can not match CPE.` を返します。
対象はネットワーク機器を想定しています。


If the CPE estimation has not been implemented yet, it returns `Can not match CPE.`.
The target is assumed to be network equipment.

```
ex) scan to Ubuntuserver.

$ ./snmp2cpe.py -ip 192.168.1.26 -c public -v 2c
INFO:Can't match CPE regexp. Plz pull-request cpe.py and/or write snmpSysDescList.txt and/or Issue(welcome to issue only).
sysName  :snmptarget
cpeName  :Can not match CPE.
sysDescr :"Linux snmptarget 5.4.0-73-generic #82-Ubuntu SMP Wed Apr 14 17:39:42 UTC 2021 x86_64"
```

取得したCPEをVulsなどで利用することで、脆弱性の管理が可能になります。

By using the acquired CPE in Vuls etc., it is possible to manage vulnerabilities.

# Why i made this

ネットワーク機器の脆弱性管理をしたい為。
既存サービスでssh接続で確認するものもあるが、定期的な自動sshはしたくない。
ネットワーク機器の管理ではSNMPを用いることも多いので、その情報を利用したほうが安全と考えた。
既存の脆弱性管理システムでは、バージョンやCPEが分からないと管理できない。しかしながら、リモートで正しくバージョンを拾えるような仕組みがない。

Because I want to manage the vulnerability of network devices.
Some existing services check with ssh connection, but I don't want to do regular automatic ssh.
Since SNMP is often used to manage network devices, I thought it would be safer to use that information.
Existing vulnerability management systems cannot manage without knowing the version and CPE. However, there is no mechanism to pick up the version correctly remotely.

# Future implementation

- CPE推定パターンを増やしたい。
- 設定ファイルによる一括定期取得、ができるようにしたい。
  - IP, SNMPバージョン, community のリストを基に一括チェック
- 設定ファイルチェック機能も実装したい
- コードをきれいにしたい(私はプログラマーではない為、汚い)

- I want to increase the CPE estimation pattern.
- I want to be able to perform batch periodic acquisition using a configuration file.
  - Batch check based on IP, SNMP version, community list
- I want to implement a configuration file check function as well.
- I want to clean the code (dirty because I'm not a programmer)

# License

GPLv3を指定します。
利用に問題がある際は連絡をください。
個人的には、CC-BY-ND 程度の想定です。

Specify GPLv3.
Please contact us if you have any problems using it.
Personally, I'm assuming about CC-BY-ND.