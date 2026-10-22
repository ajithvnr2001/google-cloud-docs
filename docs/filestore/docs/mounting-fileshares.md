---
url: https://docs.cloud.google.com/filestore/docs/mounting-fileshares/
title: Mounting file shares on Compute Engine clients \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:56.914352+00:00
---

# Mounting file shares on Compute Engine clients  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/mounting-fileshares/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Mounting file shares on Compute Engine clients Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to mount a Filestore file share on a Compute Engine virtual machine (VM) instance that's in the same Google Cloud project and [VPC network](https://docs.cloud.google.com/vpc/docs/vpc). To learn how to mount file shares on clients in a remote network, see [Mounting file shares on remote clients](https://docs.cloud.google.com/filestore/docs/remote-mounting). If you're looking to access Filestore instances from Google Kubernetes Engine clusters instead, see [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver).

## Before you begin

Ensure that the network firewall is properly configured for use with Filestore. See [Configuring firewall rules](https://docs.cloud.google.com/filestore/docs/configuring-firewall) for details.

## Mounting a file share on a Compute Engine VM instance

Use one of the following procedures to mount a Filestore file share on a Compute Engine VM. We recommend mounting to a `n1-standard-8` VM or greater for optimal performance.

###  Linux: mount 

**Note:** When mounting with the `mount` command, the file share is unmounted when the client VM reboots. To keep the file share mounted when the client VM reboots, use `fstab` or `autofs` instead.

To manually mount a file share to a Linux client VM:

  1. In the Google Cloud console, go to the VM Instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the Linux VM you want to use as a client, then click **SSH** to open a terminal on that VM.

  3. **Optional** : Mounting a file share on a client VM with multiple network interfaces through a secondary network.

**Details** (Click to expand)

If you want to mount the file share through a secondary network, namely an interface other than `nic0`, you must modify the client VM's routing policy. Run:
         
         sudo ip route \
             add filestore-reserved-address-range \
             via default-gateway-of-nic-to-filestore
         

where:

     * `filestore-reserved-address-range` is the reserved address range for use by the Filestore instance.
     * `default-gateway-of-nic-to-filestore` is the default gateway IP address of the NIC connected to the VPC network that is shared with the Filestore instance.

For more information about using Compute Engine instances with multiple NICs, see [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).

  4. Install NFS: 

###  Debian/Ubuntu 

Use the following commands to install NFS on Debian or Ubuntu.
         
         sudo apt-get -y update &&  
         sudo apt-get install nfs-common

###  RHEL/CentOS 

Use the following commands to install NFS on Red Hat Enterprise Linux or CentOS.
         
         sudo yum update &&  
         sudo yum install nfs-utils

###  SUSE 

Use the following commands to install NFS on SUSE.
         
         sudo zypper update &&  
         sudo zypper -n install nfs-client

  5. Make a local directory to map to the Filestore file share:
         
         sudo mkdir -p mount-point-directory
         

where `mount-point-directory` is the directory to create, for example `/mnt/filedir`.

  6. Mount the file share from the Filestore instance by running the [`mount`](https://linux.die.net/man/8/mount) command. You can use any [NFS mount options](https://linux.die.net/man/5/nfs). For the best performance, we recommend using the following NFS `mount` options:

Option | Description  
---|---  
`hard` | The NFS client retries NFS requests indefinitely. To reduce the possibility of I/O disruptions when the Filestore instance reboots, we recommend using the `hard` mount option for both Linux and Windows clients.  
`timeo=600` | The NFS client waits 600 deciseconds (60 seconds) before retrying an NFS request.  
`retrans=3` | The NFS client attempts NFS requests three times before taking further recovery action.  
`rsize=524288` | The NFS client can receive a maximum of 524,288 bytes from the NFS server per `READ` request.   
**Note** : For basic-tier instances, set the `rsize` value to `1048576`.  
`wsize=524288` | The NFS client can send a maximum of 524,288 bytes to the NFS server per `WRITE` request.  
`resvport` | The NFS client uses a privileged source port when communicating with the NFS server for this mount point.  
`async` | The NFS client delays sending application writes to the NFS server until certain conditions are met.   
**Caution** : Using the `sync` option significantly reduces performance.  
  
     * For reduced mounting latency, specify the `-o tcp` option.
     * If you are mounting a regional, zonal or enterprise instance to a client VM that's running Linux kernel version 5.3+, consider specifying the [`nconnect`](https://man7.org/linux/man-pages/man5/nfs.5.html) mount option for increased NFS performance. For specific service tiers, we recommend specifying the following number of connections between the client and server:

Tier | Capacity | Number of connections  
---|---|---  
Regional, zonal | 1-9.75 TiB | `nconnect=2`  
Regional, zonal | 10-100 TiB | `nconnect=7`  
Basic SSD | - | `nconnect=7`  
Enterprise | - | `nconnect=2`  
High scale SSD | - | `nconnect=7`  
  
In general, the larger the file share capacity and the fewer the connecting client VMs, the more performance you gain by specifying additional connections with `nconnect`.

Run the `mount` command with your preferred options, similar to the following:
    
    sudo mount -o rw ip-address:/file-share mount-point-directory
    

where:

     * `ip-address` is the IP address for the Filestore instance.
     * `file-share` is the name of the file share on the instance.
     * `mount-point-directory` is the path where you want to map the Filestore file share to.

You can get the IP address and file share name of an instance from any of following sources:

     * The Filestore instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances).

     * The `IP_ADDRESS` field in the results from the [`filestore instances list`](https://docs.cloud.google.com/filestore/docs/getting-instance-information#get-all-instances) command.

     * The `ipAddresses` section in the results from the [`filestore instances describe`](https://docs.cloud.google.com/filestore/docs/getting-instance-information#get-instance) command.

For example, given a Filestore instance with an IP address `10.0.1.2` and a file share named `share1`, the following command mounts the file share to the local mount point directory `/mnt/render`:
    
    sudo mount 10.0.1.2:/share1 /mnt/render
    

**Note:** We recommend optimizing the NFS read throughput by adjusting the `read_ahead_kb` parameter value. For more information, see [Optimize the NFS read throughput with `read_ahead_kb` parameter](https://docs.cloud.google.com/filestore/docs/performance#read-ahead-kb).
  7. **Optional** : Run [`chmod`](https://linux.die.net/man/1/chmod) to set permissions on the mount directory so that someone other than root users can write to it. To set directory permissions, run the following command:
         
         sudo chmod permissions mount-point-directory
         

where:

     * `permissions` is the set of permissions to grant. For example, `chmod go+rw` makes the directory readable and writable by members in the group that owns the directory and all other users. For more information about setting permissions, see [Configuring access on a file share](https://docs.cloud.google.com/filestore/docs/access-control#file-share-access).
     * `mount-point-directory` is the path to the directory where the Filestore file share is mounted.
  8. **Optional** : Confirm that the Filestore file share is mounted:
         
         df -h --type=nfs
         

The output should contain an entry similar to the following:
         
         Filesystem        Size    Used  Avail  Use%  Mounted on
         10.0.1.2:/share1  1018G   76M   966G   1%    /mnt/render
         10.0.2.2:/vol3    1018G   76M   966G   1%    /mnt/filestore3

  9. If you need to use NFS file locking, you might need to [set the ports](https://docs.cloud.google.com/filestore/docs/setting-nfs-ports) used by the `statd` and `nlockmgr` daemons and [configure firewall rules](https://docs.cloud.google.com/filestore/docs/configure-firewall) to open up those ports.




###  Linux: /etc/fstab 

You can make file shares automatically mount to client VMs during boot up by modifying the client's `/etc/fstab` file:

  1. In the Google Cloud console, go to the VM Instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the Linux VM you want to use as a client, then click **SSH** to open a terminal on that VM.

  3. **Optional** : Mounting a file share on a client VM that has multiple network interfaces through a secondary network.

**Details** (Click to expand)

If you want to mount the file share through a secondary network, namely an interface other than `nic0`, you must modify the client VM's routing policy:

     * In `/etc/default/instance_configs.cfg`, set the `setup` flag for `NetworkInterfaces` to `false`: 
           
           [NetworkInterfaces]
           dhclient_script = /sbin/google-dhclient-script
           dhcp_command =
           ip_forwarding = true
              setup = **false**

     * In `/etc/network/interfaces`, add the following lines:
           
           auto eth1
           iface eth1 inet dhcp
               up ip route add filestore-reserved-address-range via default-gateway-of-nic-to-filestore
           

where:

     * `filestore-reserved-address-range` is the reserved address range for use by the Filestore instance.
     * `default-gateway-of-nic-to-filestore` is the default gateway IP address of the NIC connected to the VPC network that is shared with the Filestore instance.

For more information about using Compute Engine instances with multiple NICs, see [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).

  4. Install NFS: 

###  Debian/Ubuntu 

Use the following commands to install NFS on Debian or Ubuntu.
         
         sudo apt-get -y update &&  
         sudo apt-get install nfs-common

###  RHEL/CentOS 

Use the following commands to install NFS on Red Hat Enterprise Linux or CentOS.
         
         sudo yum update &&  
         sudo yum install nfs-utils

###  SUSE 

Use the following commands to install NFS on SUSE.
         
         sudo zypper update &&  
         sudo zypper -n install nfs-client

  5. Make a local directory to map to the Filestore file share:
         
         sudo mkdir -p mount-point-directory
         

where `mount-point-directory` is the directory to create, for example `/mnt/filedir`.

  6. Open the `/etc/fstab` file:
         
         sudo vim /etc/fstab
         

  7. Add the following line in the `/etc/fstab` file:
         
         ip-address:/file-share mount-point-directory nfs options,_netdev 0 0
         

where:

     * `ip-address` is the IP address for the Filestore instance.
     * `file-share` is the name of the file share on the instance.
     * `mount-point-directory` is the path you want to map the Filestore file share to.
     * `options` are the NFS mount options. We recommend keeping the default NFS mount options, with the following exceptions:

       * For automounting, we recommend specifying `-o tcp` to reduce the latency when mounting and unmounting.
       * If you are mounting a regional, zonal or enterprise instance to a client VM that's running Linux kernel version 5.3+, consider specifying the [`nconnect`](https://man7.org/linux/man-pages/man5/nfs.5.html) mount option for increased NFS performance. For specific service tiers, we recommend specifying the following number of connections between the client and server:
Tier | Capacity | Number of connections  
---|---|---  
Regional, zonal | 1-9.75 TiB | `nconnect=2`  
Regional, zonal | 10-100 TiB | `nconnect=7`  
Basic SSD | - | `nconnect=7`  
Enterprise | - | `nconnect=2`  
High scale SSD | - | `nconnect=7`  
  
In general, the larger the file share capacity and the fewer the connecting client VMs, the more performance you gain by specifying additional connections with `nconnect`.

**Example** : The following line in `/etc/fstab` mounts file share `vol1` of the Filestore instance with IP address `10.0.0.2` in the mount point directory `/mnt` with the default mount options:
    
    10.0.0.2:/vol1 /mnt nfs defaults,_netdev 0 0
    

  8. Mount everything in `/etc/fstab`:
         
         sudo mount -a
         

The file share is now automatically mounted each time the client VM boots up.




###  Linux: autofs 

You can configure `autofs` to automatically mount a file share only when it's accessed and keep it unmounted when it's not used. Compared to having a file share statically mounted in `/etc/fstab`, this method helps conserve client VM resources in situations where the client needs to map to many mount points.

### Install `NFS` and `autofs` on the client VM

  1. In the Google Cloud console, go to the VM Instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the Linux VM you want to use as a client, then click **SSH** to open a terminal on that VM.

  3. **Optional** : Mounting a file share on a client VM with multiple network interfaces through a secondary network.

**Details** (Click to expand)

If you want to mount the file share through a secondary network, namely an interface other than `nic0`, you must modify the client VM's routing policy:

     * In `/etc/default/instance_configs.cfg`, set the `setup` flag for `NetworkInterfaces` to `false`: 
           
           [NetworkInterfaces]
           dhclient_script = /sbin/google-dhclient-script
           dhcp_command =
           ip_forwarding = true
              setup = **false**

     * In `/etc/network/interfaces`, add the following lines: auto eth1 iface eth1 inet dhcp up ip route add filestore-reserved-address-range via default-gateway-of-nic-to-filestore

where:

     * `filestore-reserved-address-range` is the reserved address range for use by the Filestore instance.
     * `default-gateway-of-nic-to-filestore` is the default gateway IP address of the NIC connected to the VPC network that is shared with the Filestore instance.

For more information about using Compute Engine instances with multiple NICs, see [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).

  4. Install NFS by running the following commands: 

###  Debian/Ubuntu 

Use the following commands to install NFS on Debian or Ubuntu.
         
         sudo apt-get -y update &&  
         sudo apt-get install nfs-common

###  RHEL/CentOS 

Use the following commands to install NFS on Red Hat Enterprise Linux or CentOS.
         
         sudo yum update &&  
         sudo yum install nfs-utils

###  SUSE 

Use the following commands to install NFS on SUSE.
         
         sudo zypper update &&  
         sudo zypper -n install nfs-client

  5. From the terminal window of the client VM, install `autofs`: 

###  Debian/Ubuntu 
         
         sudo apt-get install autofs
         

###  RHEL/CentOS 
         
         sudo yum install autofs
         

###  SUSE 
         
         sudo zypper -n install autofs
         




### Configure `autofs` to dynamically mount the file share to the client VM

  1. Enable `autofs`:
         
         sudo systemctl enable --now autofs
         

  2. Make a local directory to map to the Filestore file share:
         
         sudo mkdir -p mount-point-directory
         

where `mount-point-directory` is the directory to create. It must not contain any subdirectories. In this guide, we use `/nfs` as the mount point directory.

  3. Open the `/etc/auto.master` file:
         
         sudo vim /etc/auto.master
         

  4. Add the following line in the `/etc/auto.master` file:
         
         /nfs /etc/auto.nfs --timeout seconds
         

where `seconds` is the duration in seconds before the mount timeout. The default value is `300`. Setting this value to `0` disables unmounting by `autofs`.

  5. Create a file called `/etc/auto.nfs`:
         
         sudo vim /etc/auto.nfs
         

  6. Add the following line in the `/etc/auto.nfs` file:
         
         mount-point-subdir options ip-address:/file-share
         

where:

     * `mount-point-subdir` is the subdirectory in `/nfs` you want to map the Filestore file share to. This subdirectory is dynamically generated and shouldn't exist in the client VM.
     * `options` are the NFS mount options. We recommend keeping the default NFS mount options, with the following exceptions:

       * For automounting, we recommend specifying `-o tcp` to reduce the latency when mounting and unmounting.
       * If you are mounting a regional, zonal or enterprise instance to a client VM that's running Linux kernel version 5.3+, consider specifying the [`nconnect`](https://man7.org/linux/man-pages/man5/nfs.5.html) mount option for increased NFS performance. For specific service tiers, we recommend specifying the following number of connections between the client and server:
Tier | Capacity | Number of connections  
---|---|---  
Regional, zonal | 1-9.75 TiB | `nconnect=2`  
Regional, zonal | 10-100 TiB | `nconnect=7`  
Basic SSD | - | `nconnect=7`  
Enterprise | - | `nconnect=2`  
High scale SSD | - | `nconnect=7`  
  
In general, the larger the file share capacity and the fewer the connecting client VMs, the more performance you gain by specifying additional connections with `nconnect`.

       * `ip-address` is the IP address for the Filestore instance.
       * `file-share` is the name of the file share on the instance.

**Example** : The following line in `/etc/auto.nfs` mounts file share `vol1` of the Filestore instance with IP address `10.0.0.2` in the dynamically generated subdirectory `file-shares` with `read/write` access granted:
    
    file-shares -rw 10.0.0.2:/vol1
    




### Test your configuration

  1. If the file share is mounted, you need to unmount it:
         
         sudo umount mount-point-directory
         

where `mount-point-directory` is the path where the Filestore file share is mapped to.

If there is an `/etc/fstab` entry that mounts the file share at system boot, make sure to remove it.

  2. Reload `autofs`:
         
         sudo service autofs reload
         

  3. Confirm that your configuration works:
         
         ls mount-point-directory/mount-point-subdir
         

where:

     * `mount-point-directory` is the mount point directory indicated in the `/etc/auto.master` file.
     * `mount-point-subdir` is the mount point subdirectory indicated in the `/etc/auto.nfs` file.

From our example, the command would be:
    
    ls /nfs/file-shares
    

If the automount is configured correctly, the system first mounts the file share and then returns the results of the `ls` command. The file share is automatically unmounted after a period of inactivity, which is defined in the `timeout` value specified in the `/etc/auto.master` file.




###  Windows 

### Connect to the Windows VM

  1. In the Google Cloud console, go to the VM Instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Locate the Windows VM that you want to use as a client, then click **RDP** to open a remote desktop connection to that VM. For more information, see [Connecting to Windows instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).




### Install NFS on the Windows VM

  1. On the Windows VM, open PowerShell as an administrator to ensure proper NFS access and permissions.
  2. In PowerShell, install the NFS client:
         
         Install-WindowsFeature -Name NFS-Client
         

  3. Restart the Windows VM instance as prompted, then open a new remote desktop connection.




### Configure the user ID used by the NFS client

  1. In PowerShell, run the following commands to create two new registry entries, `AnonymousUid` and `AnonymousGid`:
         
         New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" `
             -Name "AnonymousUid" -Value "0" -PropertyType DWORD
         
         
         New-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\ClientForNFS\CurrentVersion\Default" `
             -Name "AnonymousGid" -Value "0" -PropertyType DWORD
         

  2. Restart the NFS client service:
         
         nfsadmin client stop
         
         
         nfsadmin client start
         




### Map the file share to the Windows VM

  1. Exit PowerShell to leave the administrator's session. If you omit this step, applications running in the standard user's session won't be able to see or access this file share.
         
         exit
         

  2. **Optional** : Mounting a file share on a client VM with multiple network interfaces through a secondary network.

**Details** (Click to expand)

If you want to mount the file share through a secondary network, namely an interface other than `nic0`, you must modify the client VM's routing policy. Run:
         
         route -p ^
             add filestore-reserved-address-range ^
             mask address-range-subnet-mask ^
             default-gateway-of-nic-to-filestore
         

where:

     * `filestore-reserved-address-range` is the reserved address range for use by the Filestore instance.
     * `address-range-subnet-mask` is the subnet mask of `filestore-reserved-address-range`. For example, a /29 reserved address range would use the 255.255.255.248 subnet mask.
     * `default-gateway-of-nic-to-filestore` is the default gateway IP address of the NIC connected to the VPC network that is shared with the Filestore instance.

**Example** :
    
    route -p add 10.65.21.176 mask 255.255.255.248 10.128.0.1
    

For more information about using Compute Engine instances with multiple NICs, see [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).

  3. From `Command Prompt`, map the file share to a drive letter:
         
         net use drive-letter: \\filestore-ip\file-share-name
         

where:

     * filestore-ip is the IP address of the Filestore instance.
     * file-share-name is the name of the file share on the Filestore instance.
     * drive-letter is the letter of the drive you want to assign for the mapping.

**Example**

The following command maps file share `vol1` on the Filestore instance with the IP address `10.0.0.2` to drive `z:` on the client Windows VM:
    
    net use Z: \\10.0.0.2\vol1
    

  4. **Optional** : To use NFS file locking, verify the following:

     1. Ensure that the [firewall rules are configured](https://docs.cloud.google.com/filestore/docs/configuring-firewall#creating_a_firewall_egress_rule) for all required NFS ports, including `statd` and `nlockmgr`.

     2. Ensure that the Windows NFS client is configured with reserved ports using a command similar to the following in PowerShell:
            
            nfsadmin client config protocol=tcp UseReservedPorts=yes
            nfsadmin client stop
            nfsadmin client start
            




## Creating and mounting subdirectories on the file share

Once your file share is mounted on a client VM, you can create subdirectories on the file share, which clients can then mount directly instead of mounting the entire file share:

  1. To create a subdirectory on the mounted file share, run:
         
         sudo mkdir -p mount-point-directory/file-share-sub-dir
         

where:

     * `mount-point-directory` is the path where you map the file share to.
     * `file-share-sub-dir` is the path of the subdirectory in the file share that you want to create.

This command creates the subdirectory on both the client VM and the file share. For example, if you mounted file share `10.0.0.2:/vol1` to the directory `/mnt` on the client VM, the command `sudo mkdir -p /mnt/nfs` creates `10.0.0.2:/vol1/nfs` on the file share and `/mnt/nfs` on the client VM.

  2. **Optional** : If you want to mount the file share subdirectory to the directory on the client VM where the file share is mounted, you must unmount the file share first:
         
         sudo umount mount-point-directory
         

where `mount-point-directory` is the directory that the file share is mapped to.

  3. Mount the subdirectory:
         
         sudo mount ip-address:/file-share/file-share-sub-dir mount-point-directory
         

where:

     * `ip-address` is the IP address for the Filestore instance.
     * `file-share` is the name of the file share on the instance.
     * `file-share-sub-dir` is the path of the subdirectory in the file share to mount.
     * `mount-point-directory` is the path where you want to map the Filestore file share to.

**Example** : In the following command:
    
    sudo mount 10.0.0.2:/vol1/nfs /mnt/nfs
    

     * `10.0.0.2` is the IP address of the Filestore instance.
     * `vol1` is the name of the file share.
     * `nfs` is a file share subdirectory.
     * `/mnt/nfs` is the directory on the client VM where the file share subdirectory `nfs` is mapped to.



## What's next

  * Learn how to [copy data to the mounted file share](https://docs.cloud.google.com/filestore/docs/copying-data).
  * Learn how to [mount file shares on clients in a remote network](https://docs.cloud.google.com/filestore/docs/remote-mounting).
  * [Troubleshoot mounting issues](https://docs.cloud.google.com/filestore/docs/troubleshooting#unable_to_mount_file_share) related to Filestore.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
