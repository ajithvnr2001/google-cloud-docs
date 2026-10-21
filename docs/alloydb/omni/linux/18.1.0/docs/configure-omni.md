---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-omni/
title: Set up AlloyDB Omni using RPM for production \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:40.911262+00:00
---

# Set up AlloyDB Omni using RPM for production  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-omni/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Set up AlloyDB Omni using RPM for production Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/configure-omni)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/configure-omni)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-omni)

This page shows common settings when using AlloyDB Omni for production workloads. 

## Enable huge pages

AlloyDB Omni, just like PostgreSQL, supports the use of huge pages. This requires your machine to have huge pages enabled, and you also need to enable a database setting `huge_pages`.

To enable huge pages on your Linux machine, run the following command:
    
    
    sudo /usr/lib/postgresql/MAJOR_VERSION/bin/alloydbomniMAJOR_VERSION-setup-host

Add the following line to your `postgresql.conf` to enable huge pages: 
    
    
       huge_pages=on

## Enable swapping

Swapping in the operating system lets you extend available physical memory by moving inactive memory pages between random access memory (RAM) and the hard disk to free up RAM space for active processes. AlloyDB Omni uses swapping when it is under high load and requires extra memory.

To check how much swapping space is enabled on your system, run the following:
    
    
       cat /proc/meminfo | grep SwapTotal

The output looks similar to the following:
    
    
       SwapTotal:      165748732 kB
    

To enable swapping on your operating system if the output value is `0`, see the following:

* [Red Hat Enterprise Linux 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/getting-started-with-swap_managing-storage-devices#creating-an-lvm2-logical-volume-for-swap_getting-started-with-swap)

## Enable core dumps

If AlloyDB Omni encounters an unrecoverable error and crashes, it is helpful to have a core dump for analysis. A core dump is a snapshot of the memory of the AlloyDB Omni process at the point of its crash.

To set up core dumps, set up `kernel.core_pattern` as follows:

  1. Use the `sysctl` command to configure run time kernel parameters.
  2. To set the `kernel.core_pattern` immediately, use:
         
         sysctl -w kernel.core_pattern="CORE_PATTERN"

Replace `CORE_PATTERN` with a core filename pattern such as "%e-%t.core".

For more information on core filename patterns, see [How to set process core file names](https://access.redhat.com/solutions/901293#:%7E:text=an%20unknown%20key-,Resolution,-In%20current%20linux%22) for details.

The [systemd-coredump handler](https://systemd.io/COREDUMP/) allows further configuration of your coredump settings. The tool is installed by default in RHEL.




To ensure the AlloyDB Omni process can generate full core dumps without any size limitations, configure the systemd service by adding `LimitCORE=infinity` to the `[Service]` section of your `alloydbomniMAJOR_VERSION.service` file.

  1. Create an override file for `alloydbomniMAJOR_VERSION.service` in `/etc/systemd/system/alloydbomniMAJOR_VERSION.service.d/override.conf`. Add the following to the `override.conf` file:
         
         [Service]
           LimitCORE=infinity
         

  2. Reload the systemd daemon to apply the changes:
         
         sudo systemctl daemon-reload

  3. Restart the AlloyDB Omni service:
         
         sudo systemctl restart alloydb-omniMAJOR_VERSION




## Enable internal logging

AlloyDB Omni provides more messages in addition to regular [PostgreSQL logs](https://www.postgresql.org/docs/current/runtime-config-logging.html). These messages are intended for AlloyDB for PostgreSQL support because of their technical nature. However, additional information can assist in the debugging of database issues.

To enable internal logging, complete these steps:

  1. Set the database parameter `enable_alloydb_internal_log` to `on`:
         
         ALTER SYSTEM SET enable_alloydb_internal_log=on;
         

For more information about modifying AlloyDB Omni settings, see [Configure AlloyDB Omni database parameters](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-database-flags).

  2. Restart the AlloyDB Omni service:



    
    
       sudo systemctl restart alloydb-omniMAJOR_VERSION

To customize internal logging such as configuring log file names and rotation policies further, use [PostgreSQL parameters](https://www.postgresql.org/docs/current/runtime-config-logging.html).

For example, the `log_directory` parameter specifies the directory where to save a log file and the `log_filename` parameter defines the name of the individual log file.

AlloyDB Omni combines the `log_directory` and `log_filename` parameters and saves internal logs as follows:
    
    
    LOG_DIRECTORY/LOG_FILENAME.internal
    

## Set up systemd units to run operations automatically

If you run AlloyDB Omni on a dedicated server, then you may want to configure certain operations to start automatically when the server boots up. One way to do this is through `systemd` units.

For example, the following steps configure `systemd` so that huge pages are enabled automatically whenever the server boots up.

Create a file in `/etc/systemd/system/alloydb-setup-env.service`:
    
    
       [Unit]
       Description=Setup huge pages for AlloyDB Omni
    
       [Service]
       Type=oneshot
    
       ExecStart=/usr/lib/postgresql/MAJOR_VERSION/bin/alloydbomniMAJOR_VERSION-setup-host
    
       [Install]
       WantedBy=multi-user.target
    

Enable the service as follows:
    
    
       sudo systemctl enable alloydb-setup-env.service

## What's next

  * [Protect your data using Barman](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-configure-barman).

  * [Create a read-only replica in Linux](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/set-up-read-replica). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
