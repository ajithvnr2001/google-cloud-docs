---
url: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/bms-oracle-best-practices/
title: Best practices for Oracle on Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:02.928046+00:00
---

# Best practices for Oracle on Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/solutions/oracle/bms-oracle-best-practices/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for Oracle on Bare Metal Solution

When implementing Oracle databases on Bare Metal Solution, we know that your goal is to bring up your environment easily and with as few issues as possible. To help you succeed in this goal, we've gathered feedback from customers, our Solution Architects, and support staff who have implemented Oracle databases on Bare Metal Solution. The following information provides you with recommendations learned from these experts to help you be as successful as possible when bringing up your own Oracle database environment on Bare Metal Solution.

## Software deployment

For the most successful Oracle software deployment, we recommend that you use the [Bare Metal Solution Toolkit](https://github.com/google/bms-toolkit). The toolkit provides several Ansible and JSON scripts to help you perform the Oracle software installation on Bare Metal Solution. For more information about the Bare Metal Solution Toolkit and how to install Oracle databases in a Bare Metal Solution environment, see the [toolkit user guide](https://github.com/google/bms-toolkit/blob/master/docs/user-guide.md).

## Operating system

When setting up your operating system on a Bare Metal Solution server, we recommend you perform the following actions.

### Validate your NTP servers

All Bare Metal Solution servers should be synchronized with a time source. Select an NTP server option, either physical or virtual, that best meets your needs.

**Note:** If you choose to use a public time source, you need to configure a [NAT gateway on a Compute Engine VM](https://docs.cloud.google.com/bare-metal/docs/bms-setup#bms-access-internet-vm-nat) to provide connectivity between your Bare Metal Solution environment and the NTP server.

When your servers use NTP for time synchronization, use the `timedatectl` or `ntpstat` command to see if the server is synchronized with a time source. The following examples show the output from these commands for a server that synchronizes successfully:
    
    
    timedatectl show -p NTPSynchronized
    NTPSynchronized=yes
    
    
    
    synchronised to NTP server (216.239.35.8) at stratum 3
       time correct to within 49 ms
       polling server every 1024 s
    

### View Oracle VM CPU count and memory details

To view information about an Oracle VM (OVM) host, including CPU and memory details, use the `xm info` command. For example:
    
    
    /usr/sbin/xm info
    

For more information, see [Oracle documentation on viewing host information](https://docs.oracle.com/cd/E15458_01/doc.22/e15444/admin.htm#sthref57)

### Check your `/etc/fstab` settings for the correct mount options

To prevent the boot process from hanging, always configure the non-root mount points you create (such as `/u01` and `/u02`) with the `nofail` mount option in place of the default settings. In rare cases, the underlying storage devices might not be available when a host restarts. Setting the `nofail` mount option allows the boot process to continue when the server cannot view the storage devices.

The following example shows the recommended settings for the `/u01` and `/u02` mount points in the `/etc/fstab` file:
    
    
    /dev/mapper/3600a098038314352513f4f765339624c1 /u01 xfs nofail 0 0
    /dev/mapper/3600a374927591837194d4j371563816c1 /u02 xfs nofail 0 0
    

You can modify the mount option from `defaults` to `nofail` without any impact to an operational system. However, to apply the new settings, you need to reboot your server.

### Confirm your shell limit settings

The Bare Metal Solution toolkit configures shell limits needed to configure Oracle RAC. You can skip this validation if you used the Bare Metal Solution toolkit and didn't change the shell limits. Shell limits must be set for all operating system accounts that own Oracle software, including Grid Infrastructure. Oracle recommends the following settings for Linux:

**Limit** | **Soft Value** | **Hard Value**  
---|---|---  
Open files | 1024 | 65536  
Maximum user processes | 16384 | 16384  
Stack size | 10240 | 32768  
Maximum locked memory | At least 90% of memory | At least 90% of memory  
  
Use the `ulimit` command to verify the soft and hard shell limits. For example, enter this command to verify the soft shell limit:
    
    
    ulimit -S -n -u -s -l
    

The following output shows the correct soft shell limit settings for a system with 384 GB of memory:
    
    
    open files                      (-n) 1024
    max user processes              (-u) 16384
    stack size              (kbytes, -s) 10240
    max locked memory       (kbytes, -l) 355263678
    

To verify the hard shell limits, use the following command:
    
    
    ulimit -H -n -u -s -l
    

The following output shows the correct hard shell limits for a system with 384 GB of memory:
    
    
    open files                      (-n) 65536
    max user processes              (-u) 16384
    stack size              (kbytes, -s) 32768
    max locked memory       (kbytes, -l) 355263678
    

If any of the shell limits are not set correctly, modify the entries in the `/etc/security/limits.conf` file, as shown in the following example:
    
    
    oracle  soft  nofile  1024
    oracle  hard  nofile  65536
    oracle  soft  nproc   2047
    oracle  hard  nproc   16384
    oracle  soft  stack   10240
    oracle  hard  stack   32768
    oracle  soft  memlock 355263678
    oracle  hard  memlock 355263678
    
    grid    soft  nofile  1024
    grid    hard  nofile  65536
    grid    soft  nproc   2047
    grid    hard  nproc   16384
    grid    soft  stack   10240
    grid    hard  stack   32768
    grid    soft  memlock 355263678
    grid    hard  memlock 355263678
    

**Note:** The autogenerated **memlock** value might not be appropriate. As a workaround, find the total memory with the following command and multiply it by 90% to generate a reasonable **memlock** value to include in the `/etc/security/limits.conf` file.
    
    
    grep MemTotal /proc/meminfo
    MemTotal:       16092952 kB
    

### Avoid changing your multipath settings

**Note:** Under normal situations, we do not recommend that you modify the multipath settings. Only update the `multipath.conf` settings after careful consideration. Modifications to the `multipath.conf` file can result in the loss of storage resiliency in the event of a hardware failure.

If you choose to change the multipath settings, do not configure the `path_grouping_policy` attribute if you use `multipath.conf` to create aliased names for devices. Such a change overrides the default policy set in the `devices` definition section.

Under normal operation, the `multipath -ll` command should show a status similar to the following example. Each device includes two active paths that are in the ready state.
    
    
    3600a0980383143524f2b50476d59554e dm-7 NETAPP  ,LUN C-Mode
    size=xxxG features='4 queue_if_no_path pg_init_retries 50 retain_attached_hw_handle' hwhandler='1 alua' wp=rw
    |-+- policy='service-time 0' prio=50 status=active
    | |- 14:0:3:2 sdf                8:80   active ready running
    | `- 16:0:5:2 sdv                65:80  active ready running
    `-+- policy='service-time 0' prio=10 status=enabled
      |- 14:0:2:2 sdc                8:32   active ready running
      `- 16:0:3:2 sdq                65:0   active ready running
    

### Use jumbo frames

To prevent fragmentation of packets as they travel from one server to another in a RAC environment, Oracle recommends configuring your server interfaces with jumbo frames. Jumbo frames have an MTU size of 9000 bytes and are large enough to support Oracle database block sizes of 8192 bytes. 

**Note:**

  * Always configure jumbo frames on your Bare Metal Solution servers before installing Oracle RAC.
  * Make sure your configuration uses jumbo frames on all servers in the cluster.
  * Partner Interconnect does not support jumbo frames, so do not enable jumbo frames between your Google Cloud project and your Bare Metal Solution environment.
  * A services IP address range uses the standard MTU size of 1500 bytes and does not use jumbo frames.



To configure jumbo frames on Bare Metal Solution servers for Oracle RAC:

  1. View the settings of your Bare Metal Solution private network to confirm that jumbo frames have been configured:
         
         gcloud bms networks describe NETWORK_NAME --project=PROJECT_ID --region=REGION | grep jumboFramesEnabled
         

Sample output:
         
         jumboFramesEnabled: true
         

  2. Identify the network interfaces and their `mtu` size:
         
         ip link show | grep mtu
         

Sample output:
         
         1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
         2: enp55s0f1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
         3: enp55s0f2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
         4: enp55s0f3: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN mode DEFAULT group default qlen 1000
         5: enp17s0f0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
         6: enp17s0f1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond1 state UP mode DEFAULT group default qlen 1000
         7: enp173s0f0: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond0 state UP mode DEFAULT group default qlen 1000
         8: enp173s0f1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond1 state UP mode DEFAULT group default qlen 1000
         9: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
         10: bond1.117@bond1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
         11: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
         12: bond0.118@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default qlen 1000
         13: virbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default qlen 1000
         14: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN mode DEFAULT group default qlen 1000
         

  3. Using root-level privileges, add `MTU=9000` to the interface configuration file for all servers in the Bare Metal Solution environment that use jumbo frames. You can find the file at `/etc/sysconfig/network-scripts/ifcfg-interface_name`. 

Sample output:
         
         BONDING_OPTS="lacp_rate=1 miimon=100 mode=802.3ad xmit_hash_policy=1"
         TYPE=Bond
         BONDING_MASTER=yes
         PROXY_METHOD=none
         BROWSER_ONLY=no
         DEFROUTE=yes
         IPV4_FAILURE_FATAL=no
         IPV6INIT=no
         IPV6_AUTOCONF=yes
         IPV6_DEFROUTE=yes
         IPV6_FAILURE_FATAL=no
         IPV6_ADDR_GEN_MODE=stable-privacy
         NAME=bond1
         UUID=0e7da685-64bf-44f3-812f-9846d747a801
         DEVICE=bond1
         ONBOOT=yes
         AUTOCONNECT_SLAVES=yes
         MTU=9000
         

  4. Restart networking services for the changes to take effect:
         
         service network restart
         

  5. Issue a `ping` command to test your new MTU configuration:
         
         ping -c 2 -M do -s 8972 svr001
          PING svr001 (172.16.1.10) 8972(9000) bytes of data.
          8980 bytes from svr001 (172.16.1.10): icmp_seq=1 ttl=64 time=0.153 ms
          8980 bytes from svr001 (172.16.1.10): icmp_seq=2 ttl=64 time=0.151 ms
         
         --- svr001 ping statistics ---
         2 packets transmitted, 2 received, 0% packet loss, time 1001ms
         rtt min/avg/max/mdev = 0.151/0.152/0.153/0.001 ms
         




## Oracle RMAN backups and latency impact

If the Oracle RMAN backup process is not limited by the `RATE` parameter, it can push storage throughput or IOPS to the performance limit for a storage volume. This causes storage IO to be throttled, thus increasing the latency on the storage volume.

We recommend that you implement the `RATE` channel parameter to limit the amount of bandwidth or throughput that the Oracle RMAN can use.

For more information, see [Oracle documentation: 23.2.1.4 RATE Channel Parameter](https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/tuning-rman-performance.html#GUID-5A55B177-B2A8-47AE-A6E9-693DFB5CC613)

## Oracle Automatic Storage Management

Our Cloud Customer Care team and several Bare Metal Solution customers have added Oracle Automatic Storage Management (ASM) to their Bare Metal Solution environments. Through their collective experience and wisdom, we have gathered the following list of best practices to help you be successful with your own ASM disk group installation. Our goal is to help you achieve the best [storage performance](https://docs.cloud.google.com/bare-metal/docs/bms-planning#storage_performance) for your Bare Metal Solution environment.

  * Use a uniform LUN size
  * Create no more than two ASM disk groups
  * Stripe ASM disk groups across all LUNs in all volumes
  * Use LUNs and volumes with the same performance characteristics in the same disk group
  * Do not share storage volumes across multiple RAC clusters
  * Know the required IOPS and throughput capacity before you create ASM disk groups
  * Leave the multipath configuration as-is
  * Configure important settings for ASM
  * Create your ASM disk group with external redundancy
  * Reboot your Bare Metal Solution servers after ASM disk creation



### Use a uniform LUN size

The LUN size you select should be representative of the unit of growth. ASM works best with LUNs that have an equal size and similar performance characteristics. For very large databases, we recommend a LUN size of 2 TB to optimize performance.

### Create no more than two ASM disk groups

You should send data files and one copy of the `REDO` logs to a single `DATA` disk group. Optionally, you can create a second `FRA` disk group to store on-disk backups and archive logs. When you store `REDO` logs on highly resilient storage, you do not need to have two copies. 

`REDO` log writes are sensitive to latency. As a result, only consider multiplexing `REDO` logs if the performance profile of the `FRA` disk group matches the performance profile of the `DATA` disk group.

### Stripe ASM disk groups across all LUNs in all volumes

When you create ASM disk groups, stripe the disk group across all LUNs of all volumes. If your LUNs belong to a single volume, you must include all the LUNs in the volume when you create a disk group. For example, if a volume has `X` number of LUNs, you should use all `X` LUNs when you create the disk group.

This guidance also applies to using multiple volumes, because we provide QoS limits on volumes. If you use multiple volumes for increased throughput (>900 Mbps), you need to include all the LUNs from every volume when you create the disk group to achieve the required performance.

**Note:** Do not use a partial volume to create an ASM disk group.

### Use LUNs and volumes with the same performance characteristics in the same disk group

If you use multiple volumes to enhance throughput, use the same volume size and performance characteristics when you create ASM disk groups.

Do not mix LUNs from volumes that have different performance characteristics. If you do include LUNs and volumes with different performance profiles in the same disk group, disks that perform I/O operations might have a much lower performance ceiling and might cause latency spikes.

For example, if you create an ASM disk group with 2 uneven volumes (1 X 16 TiB and 1 X 5 TiB), the I/O operations performed by the disks in the 5 TB volume might cause elevated latency. The 5 TiB volume has a much lower throughput and IOPS ceiling, so it would hit the throttling level long before the throttling level for the 16 TiB volume.

### Do not share storage volumes across multiple RAC clusters

For each RAC cluster, provision a unique storage volume. Do not share the same storage volume across multiple RAC clusters. Because storage devices apply QoS at the volume level, this practice minimizes the chance of noisy neighbors competing for a single pool of IOPS and throughput.

For example, if a single volume has 8 LUNs, do not assign some of the LUNs to one RAC database cluster and the remaining LUNs to a different RAC database cluster. Instead, provision two separate storage volumes and assign each volume to a separate, dedicated RAC cluster per volume.

### Know the required IOPS and throughput capacity before you create ASM disk groups

Be aware of the peak performance numbers for your on-premises environment. To find this information, generate AWR reports during peak workloads hours to record your system's peak IOPS and throughput values. You can also use our [Oracle Database Assessment tool](https://github.com/GoogleCloudPlatform/oracle-database-assessment) to gather your peak performance numbers.

With your on-premises performance numbers handy, check our Bare Metal Solution [storage performance table](https://cloud.google.com/bare-metal/docs/bms-planning#storage_performance) to calculate the amount of storage that you need to allocate to your ASM disk groups and achieve the required performance. When you have enhanced throughput requirements (>768 Mbps), you can create multiple volumes and stripe the ASM disk group across all LUNs and all volumes.

### Leave the multipath configuration as-is

You should not change the default `group_pathing_policy` in the `/etc/multipath.conf` file. You should always use the default value of `group_pathing_policy=group_by_prio` to avoid RAC node eviction in case of storage path failures.

For more details about leaving the multipath configuration intact, see Avoid changing your multipath settings.

### Configure important settings for ASM

If you are using Oracle Grid Infrastructure 12.1.0.2 or later on Linux, set up ASM with ASMFD or UDEV.

For prior versions of Oracle Grid Infrastructure, use ASMLib.

  * To stop Oracle ASM from selecting your single path ASM device first, set the scan order as follows:
        
        ORACLEASM_SCANORDER="dm"
        ORACLEASM_SCANEXCLUDE="sd"
        

We require this setting because the Bare Metal Solution storage environment uses DM devices that you can view in `/proc/partitions`.

  * To check if ASMLib is configured to manage your ASM disks, run the following command as the root user:
        
        /usr/sbin/oracleasm configure | grep SCAN
        

If you're using ASMLib, the output looks like the following:
        
        ORACLEASM_SCANBOOT=true
        ORACLEASM_SCANORDER="dm"
        ORACLEASM_SCANEXCLUDE="sd"
        ORACLEASM_SCAN_DIRECTORIES=""
        


**Note:**

  * Never use the **/dev/sd*** names directly when you create or label the ASM disks. Because of ASMLib, ASMFD, and UDEV rules, you need to use the **/dev/mapper** or **dm** device names directly so the application can survive a single path failure or OS reboot.
  * These instructions use 10g as a value, but the behavior is the same for 19c Grid Infrastructure as well. (Follow MOS Note : 1679409.1)



### Create your ASM disk group with external redundancy

The storage provided by Bare Metal Solution uses [NETAPP RAID-DP](https://library.netapp.com/ecmdocs/ECMP1636022/html/GUID-FB0C6807-89A2-41AF-A29B-D0D2A91A163B.html), which is a form of RAID 6 that protects data even if two disks fail. As a result, we recommend that you use external redundancy for ASM.

### Reboot your Bare Metal Solution servers after ASM disk creation

After you create your ASM disk groups, you should reboot all Bare Metal Solution servers in the cluster to make sure that both the ASM instance and the disk groups come online after the reboot. Follow this proactive step so that you can avoid issues that might happen after the database cluster is built on the ASM disk group.

## Oracle RAC

This section explains best practices when installing Oracle Real Application Clusters (RAC) on Bare Metal Solution.

### Oracle Grid Infrastructure cluster name length

Use a cluster name that is not more than 15 characters long.

A cluster name longer than 15 characters causes the `root.sh` script to fail.

### Tunnel VNC Viewer over SSH

Arbitrary servers, such as VNC Viewer, are blocked by the default OS firewall of the Bare Metal Solution server. Therefore, tunnel either X Window or VNC Viewer over SSH:
    
    
    ssh -L 5901:localhost:5901 bms-host
    vncviewer localhost:1
    

### Enough space for the root file system

Ensure that the root file system (/) has enough free space. Bare Metal Solution servers come with a 20GB root file system which might not be sufficient.

On your Bare Metal Solution server, check the size of the root '/' file system. The default size is 20GB which might not be sufficient. If the size is 20GB, increase it.

### Use a name server as a substitute for Cloud DNS

If you don't want to use the Cloud DNS, then install your own name server to resolve host IP addresses on the Bare Metal Solution server. The Oracle Grid Infrastructure uses the `nslookup` command to get the name of the DNS server. The `nslookup` command doesn't use the `/etc/hosts` file.

Follow these steps:

  1. Install `dnsmasq`.
         
         yum makecache
         yum install dnsmasq
         

  2. Open the `/etc/dnsmasq.conf` file in edit mode.
         
         vi /etc/dnsmasq.conf
         

  3. In the `/etc/dnsmasq.conf` file, add the following lines:
         
         port=53
         domain-needed
         bogus-priv
         
         strict-order
         expand-hosts
         domain=localdomain
         
         address=/.localdomain/127.0.0.1
         address=//127.0.0.1
         
         listen-address=127.0.0.1
         resolv-file=/etc/dnsmasq-resolv.conf
         

  4. Edit the `/etc/dnsmasq-resolv.conf` file and the `/etc/resolv.conf` file to contain only the following line:
         
         nameserver 127.0.0.1
         

  5. Start the `dnsmasq` service:
         
         systemctl restart dnsmasq
         
         systemctl status dnsmasq
         

  6. On both nodes, run the `nslookup` command.
         
         nslookup at-2811641-svr001
         Server:         127.0.0.1
         Address:        127.0.0.1#53
         
         Name:   at-2811641-svr001
         Address: 192.168.1.10
         
         nslookup at-2811641-svr002
         Server:         127.0.0.1
         Address:        127.0.0.1#53
         
         Name:   at-2811641-svr002
         Address: 192.168.1.11
         




### Install NTP

When you install NTP, ensure that all the RAC nodes sync with the time of your jump host or your internal NTP server. Follow these steps:

  1. Install NTP.
         
         yum install ntp
         

  2. Start the `ntpd` service.
         
         systemctl start ntpd
         

  3. In the `/etc/ntp.conf` file, add the following line to sync with the bastion host, which is `10.x.x.x` in this case. You can also use your internal NTP server. In this case, `192.x.x.x` is your Bare Metal Solution server.
         
         restrict 192.x.x.x mask 255.255.255.0 nomodify notrap
         server 10.x.x.x prefer
         

  4. To start syncing, update the time server to start syncing.
         
         ntpdate -qu SERVER_NAME
         




### Run root script on one node at a time

Run the root script `root.sh` on one node at a time. If the execution fails on the first node, don't proceed to the next node.

### Resolve the `Localhost`

Because the Bare Metal Solution server doesn't add the `Localhost` to `/etc/hosts` file, manually resolve the `Localhost` to `127.0.0.1`.

### Ensure sufficient resource limits

Before installing Oracle RAC on the Bare Metal Solution server, ensure that the resource limits for the `root` user and the `oracle` user are sufficient.

You can use the `ulimit` command to check the limits.

### Set the `ORACLEASM_SCANORDER` variable

If you're using Oracle ASMLib, then to stop Oracle ASM from selecting your single path ASM device first, set the scan order as follows:
    
    
    ORACLEASM_SCANORDER="dm"
    ORACLEASM_SCANEXCLUDE="sd"
    

We require this setting because the Bare Metal Solution storage environment uses DM devices that you can view in `/proc/partitions` file.

**Note:** This instruction is for Oracle 10g, but the behavior is the same for 19c Grid Infrastructure as well.

Oracle is a registered trademark of Oracle and/or its affiliates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
