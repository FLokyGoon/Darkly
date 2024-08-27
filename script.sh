#!/bin/bash

kvm=""

if [ $(arch) != "arm64" ]; then
    kvm="-enable-kvm -cpu host"
    echo "[$(arch)] kvm enabled"
else
    kvm="-accel tcg,tb-size=512"
    echo "[$(arch)] no kvm"
fi

qemu-system-x86_64 \
    -machine q35 \
    -smp 8 \
    $kvm \
    -m 8G \
    -hda ./goinfre/Darkly_i386.iso \
    -netdev user,id=vmnic,hostname=lfshost,hostfwd=tcp::8080-10.0.2.15:80 \
    -device virtio-net,netdev=vmnic \
    -device virtio-rng-pci

