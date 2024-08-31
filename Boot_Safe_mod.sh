#!/bin/bash

kvm=""

if [ $(arch) != "arm64" ]; then
    kvm="-enable-kvm -cpu host"
    echo "[$(arch)] kvm enabled"
else
    kvm="-accel tcg,tb-size=512"
    echo "[$(arch)] no kvm"
fi
#init=/bin/bash
qemu-system-x86_64 \
    -machine q35 \
    -smp 8 \
    $kvm \
    -m 8G \
    -drive file=/home/fbardeau/Downloads/Darkly_i386.iso,format=raw \
    -netdev user,id=vmnic,hostname=lfshost,hostfwd=tcp::8080-10.0.2.15:80 \
    -device virtio-net,netdev=vmnic \
    -device virtio-rng-pci \
    -boot menu=on
