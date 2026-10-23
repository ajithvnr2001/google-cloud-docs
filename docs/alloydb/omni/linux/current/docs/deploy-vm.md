---
url: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/deploy-vm/
title: Install AlloyDB Omni using RPM \u00a0|\u00a0 AlloyDB Omni using RPM: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:17.400813+00:00
---

# Install AlloyDB Omni using RPM  |  AlloyDB Omni using RPM: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/current/docs/deploy-vm/

This page documents AlloyDB Omni version **18.4.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview)



Send feedback 

#  Install AlloyDB Omni using RPM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/deploy-vm)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/deploy-vm)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/deploy-vm)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/deploy-vm)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/deploy-vm)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/linux/17.5.0/docs/deploy-vm)



You can perform single instance installations of AlloyDB Omni on any Linux machine or bare metal server that supports RHEL 9 runtimes.

## Before you begin

Before you install AlloyDB Omni, read [Plan your AlloyDB Omni installation](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/plan-installation-linux).

### Create a directory where AlloyDB Omni stores data

If you're using a storage system that runs AlloyDB Omni along with other applications, you can create the AlloyDB Omni directory on your device's existing file system. Otherwise, you can create a new file system on your dedicated device.

#### Existing file system

To create a directory in an existing file system, run the following command:
    
    
    mkdir -p DATA_DIR

Replace the following variable:

  * DATA_DIR: the host directory path that your data is stored in.



#### Dedicated device

To create a directory in a dedicated file system, perform the following steps:

  1. Create a directory on the host where the disk will be mounted.
         
         mkdir -p MOUNT_POINT

Replace the following variable:

     * MOUNT_POINT: top-level directory path that should contain your AlloyDB Omni instance.
  2. Create a `gpt` partition table and file system, and mount the disk device.

### EXT4
         
         parted -s DEVICE_PATH mklabel gpt
         parted -s DEVICE_PATH mkpart primary 0% 100%
         mkfs.ext4 -q -m 1 -L FS_LABEL -F PARTITION_PATH
         echo -e "LABEL=FS_LABEL\tMOUNT_POINT\text4\tdefaults\t0 0" | tee -a /etc/fstab
         mount MOUNT_POINT

Replace the following variables:

     * DEVICE_PATH: path assigned by the operating system to the disk device.
     * FS_LABEL: label for the file system. The maximum length is 12 characters for `xfs`.
     * PARTITION_PATH: path for the disk partition that's used to store the file system data.

### XFS
    
    parted -s DEVICE_PATH mklabel gpt
    parted -s DEVICE_PATH mkpart primary 0% 100%
    dnf install xfsprogs
    mkfs.xfs -L FS_LABEL -f PARTITION_PATH
    echo -e "LABEL=FS_LABEL\tMOUNT_POINT\txfs\tdefaults\t0 0" | tee -a /etc/fstab
    mount MOUNT_POINT

Replace the following variables:

     * DEVICE_PATH: path assigned by the operating system to the disk device.
     * FS_LABEL: label for the file system. The maximum length is 16 characters for `ext4`.
     * PARTITION_PATH: path for the disk partition that's used to store the file system data.

  3. Create a data directory in this file system. We recommend creating `DATA_DIR` as a subdirectory inside the mount point—for example, `MOUNT_POINT/18`.
         
         mkdir -p DATA_DIR

Replace `DATA_DIR` with host directory path to store database-related data in—for example, `MOUNT_POINT/18`.




### Configure SELinux policy

Install the required `policycoreutils-python-utils` package so that the `SELinux` policy is configured to allow AlloyDB Omni database service while installing the AlloyDB Omni RPM package.

## Install AlloyDB Omni

  1. Configure the YUM repository in your local directory.
         
         sudo tee -a /etc/yum.repos.d/alloydbomni.repo << EOF
         [alloydbomni]
         name=alloydbomni
         baseurl=ALLOYDB_OMNI_URL
         enabled=1
         repo_gpgcheck=1
         gpgcheck=1
         gpgkey=https://dl.google.com/linux/linux_signing_key.pub
         EOF
         
         
         sudo yum makecache
         

Replace `ALLOYDB_OMNI_URL` with the AlloyDB Omni URL that you receive.

**Note:** Package integrity is verified at the individual RPM level.
  2. Install the AlloyDB Omni RPM package.
         
         sudo dnf install alloydbomni18

  3. Initialize and configure the AlloyDB Omni database.
         
         sudo PGPASSWORD=POSTGRES_PASSWORD PGDATA=DATA_DIR /usr/lib/postgresql/18/bin/alloydbomni18-setup initdb

Optionally, you can pass standard `initdb` options as a single string in the `POSTGRES_INITDB_ARGS` variable.

  4. If you are using a custom data directory, run the following commands to configure SELinux to allow the AlloyDB Omni service to read and write data in that directory. This step requires that the `policycoreutils-python-utils` package is installed.
         
         /usr/sbin/semanage fcontext -a -t postgresql_db_t "DATA_DIR(/.*)?"
         
         
         sudo PWFILE=PASSWORD_FILE_PATH PGDATA=DATA_DIR /usr/lib/postgresql/18/bin/alloydbomni18-setup initdb
         

Replace the following variables:

     * `POSTGRES_PASSWORD`: your password.
     * `PASSWORD_FILE_PATH`: the path containing only the password in plain text.
     * `DATA_DIR`: the host directory path to store database-related data. For example, `MOUNT_POINT/18`.

Optionally, you can pass standard `initdb` options as a single string in the `POSTGRES_INITDB_ARGS` variable.

  5. If you are using a custom data directory and if SELinux is enabled, run the following commands to configure SELinux to allow the AlloyDB Omni service to read and write data in that directory. This step requires that the `policycoreutils-python-utils` package is installed.
         
         sudo /usr/sbin/semanage fcontext -a -t postgresql_db_t "DATA_DIR(/.*)?"
           sudo /sbin/restorecon -R -F DATA_DIR
         /sbin/restorecon -R -F DATA_DIR

  6. Prepare the AlloyDB Omni database.
         
         sudo PGPASSWORD=POSTGRES_PASSWORD /usr/lib/postgresql/18/bin/alloydbomni18-setup preparedb

  7. Optional. For optimized execution of the AlloyDB Omni service, run the following command.
         
         sudo /usr/lib/postgresql/18/bin/alloydbomni18-setup-host

Running the earlier command sets the following system configurations to their recommended values:

System setting | Recommended value  
---|---  
`/sys/kernel/mm/transparent_hugepage/shmem_enabled` | `within_size`  
`/sys/kernel/mm/transparent_hugepage/khugepaged/max_ptes_swap` | `511`  
`/sys/kernel/mm/transparent_hugepage/khugepaged/max_ptes_shared` | `511`  
`/proc/sys/vm/nr_overcommit_hugepages` | value equal to the size of MemTotal in MB  
`/proc/sys/vm/max_map_count` | `1073741824`  
  
To pass custom values for these configurations, include arguments in the `<system_setting>=<value>` format in the `alloydbomni18-setup-host` command, as in the following example:
         
         sudo /usr/lib/postgresql/18/bin/alloydbomni18-setup-host /proc/sys/vm/max_map_count=2097152 /proc/sys/vm/nr_overcommit_hugepages=524288
         

  8. Start the AlloyDB Omni `systemd` service.
         
         sudo systemctl enable alloydbomni18
         
         
         sudo systemctl start alloydbomni18
         

  9. Check whether the AlloyDB Omni service is running successfully.
         
         sudo systemctl status alloydbomni18

The following is an example response. Verify that the status is active (running).
         
         Loaded: loaded (/usr/lib/systemd/system/alloydbomni18.service; enabled; preset: disabled)
            Drop-In: /etc/systemd/system/alloydbomni18.service.d
              Active: active (running) since Wed 2025-11-19 07:37:31 UTC; 1 day 6h ago "
            Process: 120228 ExecStartPre=/usr/lib/postgresql/18/bin/alloydbomni18-check-db-dir ${PGDATA} (code=exited, status=0 SUCCESS)
           Main PID: 120231 (postgres)
              Tasks: 19 (limit: 203438)
             Memory: 161.7M (peak: 170.0M)
                CPU: 28min 10.149s
             CGroup: /system.slice/alloydbomni18.service
                     ├─120231 /usr/lib/postgresql/18/bin/postgres -D /var/lib/postgresql/18/data
                     ├─120232 "postgres: alloydb internal logger "
                     ├─120233 "postgres: checkpointer "
                     ├─120234 "postgres: background writer "
                     ├─120237 "postgres: walwriter "
                     ├─120243 "postgres: lux wal preallocator "
                     ├─120244 "postgres: autovacuum launcher "
                     ├─120246 "postgres: free buffer manager "
                     ├─120247 "postgres: buffer control "
         




## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/run-connect#connect-rpm). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
