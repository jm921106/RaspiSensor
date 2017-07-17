
# I2C setting 하는법

우선,

$ sudo nano /etc/modules

내용이 있음을 확인 (없다면 추가)

i2c-dev

다음, 파일이 있음을 확인

$sudo nano /etc/modprobe.d/raspi-blacklist.conf

blacklist i2c-bcm2708 이 있다면

# 처리

다음,

$ sudo apt-get install python3-smbus

$ sudo reboot

$ sudo apt-get install i2c-tools