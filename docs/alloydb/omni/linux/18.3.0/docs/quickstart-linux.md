---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/quickstart-linux/
title: Install AlloyDB Omni using RPM \u00a0|\u00a0 AlloyDB Omni using RPM: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:39.756935+00:00
---

# Install AlloyDB Omni using RPM  |  AlloyDB Omni using RPM: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/quickstart-linux/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)



Send feedback 

#  Install AlloyDB Omni using RPM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/quickstart-linux)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/quickstart-linux)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/quickstart-linux)

This quickstart shows you how to use the RPM package to install AlloyDB Omni on a Linux machine or bare metal server that supports RHEL 9. 

For an overview of AlloyDB Omni, see [AlloyDB Omni overview](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview).

## Before you begin

Before you install AlloyDB Omni, make sure that you meet the following requirements.

### Choose a download or installation option

AlloyDB Omni can be downloaded and installed using a YUM repository for RHEL environments. See [Available download and installation options](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/available-download-install-options).

### Fulfill hardware and software requirements

Make sure that you meet the following minimum hardware and software requirements:

OS/Platform | Minimum hardware | Minimum software  
---|---|---  
Linux | 

  * x86-64 or Arm (*) CPU with AVX2 support
  * 2 GB of RAM
  * 10 GB of disk space

| 
* RHEL 9
* Linux kernel version 5.3 or higher
* Cgroupsv2 enabled  
(*) Arm support is in [Preview](https://cloud.google.com/products#product-launch-stages).  
  
#### Verify that cgroupsv2 is enabled

To determine whether cgroupsv2 is enabled on your machine, run the following command:
    
    
    grep cgroup /proc/filesystems

If your machine supports cgroupsv2, you see the following output:
    
    
    nodev cgroup
    nodev cgroupsv2
    

If your machine doesn't support cgroupsv2, you see the following output:
    
    
    nodev cgroup
    

#### Verify SELinux configuration

If your system uses SELinux, ensure it is configured to let AlloyDB Omni run. For this quickstart, you can temporarily set SELinux to permissive mode by running the following command:
    
    
    sudo setenforce 0

## Install AlloyDB Omni using RPM

To install and start AlloyDB Omni, follow these steps:

  1. Configure the YUM repository:
         
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

Replace `ALLOYDB_OMNI_URL` with the AlloyDB Omni URL you received after filling out the [download sign-up form](https://forms.gle/zxuHekMtV67Bw9Av9).

  2. Install the AlloyDB Omni RPM package:
         
         sudo dnf install alloydbomni18

  3. Initialize the AlloyDB Omni database:
         
         sudo PGPASSWORD=POSTGRES_PASSWORD PGDATA=DATA_DIR /usr/lib/postgresql/18/bin/alloydbomni18-setup initdb POSTGRES_INITDB_ARGS

Replace the following:

     * `POSTGRES_PASSWORD`: your password.
     * `DATA_DIR`: host directory path to store database-related data in—for example, `MOUNT_POINT/18`.
     * `POSTGRES_INITDB_ARGS`: (Optional) use to pass standard `initdb` options as a single string.
  4. Prepare the AlloyDB Omni database:
         
         sudo PGPASSWORD=POSTGRES_PASSWORD /usr/lib/postgresql/18/bin/alloydbomni18-setup preparedb

  5. (Optional) For optimized execution on the host, run the setup-host script. This host-level tuning is separate from the `POSTGRES_INITDB_ARGS` database initialization arguments:
         
         sudo /usr/lib/postgresql/18/bin/alloydbomni18-setup-host

  6. Enable and start the AlloyDB Omni service:
         
         sudo systemctl enable alloydbomni18
         sudo systemctl start alloydbomni18

  7. Connect to AlloyDB Omni using `psql`:
         
         sudo -u postgres psql -h localhost

The terminal window displays `psql` login text that ends with a `postgres=#` prompt.




## Clean up

To uninstall the AlloyDB Omni package and clean up the service you created during this quickstart, use these steps:

  1. Stop the AlloyDB Omni service:
         
         sudo systemctl stop alloydbomni18

  2. Remove the AlloyDB Omni package:
         
         sudo dnf remove alloydbomni18




## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/run-connect)
  * [Install AlloyDB Omni using RPM](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/deploy-vm)
  * [Run AlloyDB Omni in production](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/run-alloydb-omni-production)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
