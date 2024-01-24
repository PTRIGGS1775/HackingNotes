Mounting directories you find

If the box is running a nfs network file share start with showmount to list what is available:
```bash
showmount -e {Target IP}
```

This should show you a directory list that's being shared.

Then you'll need to mount the file to do that:
```bash
mkdir /mnt/{name you want}
mount -t nfs {Target IP}:{Name of fileshare listed in showmount} /mnt/{name you wanted}
cd /mnt/{name you wanted}
```
