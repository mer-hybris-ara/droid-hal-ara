# These and other macros are documented in dhd/droid-hal-device.inc

%define device ara
%define vendor nokia

%define vendor_pretty nokia
%define device_pretty ara

%define installable_zip 1

%define straggler_files \
/init.class_main.sh\
/init.qcom.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}

%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}

%include rpm/dhd/droid-hal-device.inc
