#!/usr/bin/bash

DIR="/etc/calamares"
KERNEL=`uname -r`

if [[ -d "/run/archiso/copytoram" ]]; then
	doas sed -i -e 's|/run/archiso/bootmnt/arch/x86_64/airootfs.sfs|/run/archiso/copytoram/airootfs.sfs|g' "$DIR"/modules/unpackfs.conf
	doas sed -i -e "s|/run/archiso/bootmnt/arch/boot/x86_64/vmlinuz-linux|/usr/lib/modules/$KERNEL/vmlinuz|g" "$DIR"/modules/unpackfs.conf
fi

doas pkexec calamares
