---
url: https://docs.cloud.google.com/filestore/docs/testing-performance/
title: Test instance performance \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:18.232767+00:00
---

# Test instance performance  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/testing-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Test instance performance Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses performance testing for Filestore instances.

## Overview

If you are using Linux, you can use the [Flexible IO Tester (fio)](https://linux.die.net/man/1/fio) tool to benchmark read throughput, write throughput, read IOPS, and write IOPS, for basic , regional, zonal, and enterprise [tier](https://docs.cloud.google.com/filestore/docs/service-tiers) instances.

You can test performance of basic instances using a single client VM. We don't recommend using a single client VM to test regional, zonal or enterprise instances because scaleout service tiers are performance optimized for multiple client VMs and a single client usually can't achieve the maximum cluster IOPS or throughput.

For more information, see [Single and multiple client VM performance](https://docs.cloud.google.com/filestore/docs/performance#single-multiple-performance).

## Before you start

Mount the Filestore file share you want to test on all client VMs. It can be one or several client VMs depending on the service tier. For detailed instructions and mounting options, see [Mounting file shares on Compute Engine clients](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).

Make sure to specify the [`nconnect`](https://man7.org/linux/man-pages/man5/nfs.5.html) mount option for increased NFS performance. For specific service tiers, we recommend specifying the following number of connections between the client and server:

Tier | Capacity | Number of connections  
---|---|---  
Regional, zonal | 1-9.75 TiB | `nconnect=2`  
Regional, zonal | 10-100 TiB | `nconnect=7`  
Basic SSD | - | `nconnect=7`  
Enterprise | - | `nconnect=2`  
High scale SSD | - | `nconnect=7`  
  
You can optimize the NFS read throughput by adjusting the `read_ahead_kb` parameter value. For more information, see [Optimize the NFS read throughput with `read_ahead_kb` parameter](https://docs.cloud.google.com/filestore/docs/performance#read-ahead-kb).

## Test performance with a single client VM

Use the following scenarios to perform tests on basic instances. You can run the commands directly from your command line.

  * Maximum write throughput for basic instances smaller than 1 TiB:
        
        fio --ioengine=libaio --filesize=4G --ramp_time=2s
        --runtime=5m --numjobs=16 --direct=1 --verify=0 --randrepeat=0
        --group_reporting --directory=/mnt/nfs
        --name=write --blocksize=1m --iodepth=64 --readwrite=write
        

  * Maximum read throughput:
        
        fio --ioengine=libaio --filesize=32G --ramp_time=2s \
        --runtime=5m --numjobs=16 --direct=1 --verify=0 --randrepeat=0 \
        --group_reporting --directory=/mnt/nfs --buffer_compress_percentage=50 \
        --name=read --blocksize=1m --iodepth=64 --readwrite=read
        

  * Maximum write throughput:
        
        fio --ioengine=libaio --filesize=32G --ramp_time=2s \
        --runtime=5m --numjobs=16 --direct=1 --verify=0 --randrepeat=0 \
        --group_reporting --directory=/mnt/nfs --buffer_compress_percentage=50 \
        --name=write --blocksize=1m --iodepth=64 --readwrite=write
        

  * Maximum read IOPS:
        
        fio --ioengine=libaio --filesize=32G --ramp_time=2s \
        --runtime=5m --numjobs=16 --direct=1 --verify=0 --randrepeat=0 \
        --group_reporting --directory=/mnt/nfs --buffer_compress_percentage=50 \
        --name=randread --blocksize=4k --iodepth=256 --readwrite=randread
        

  * Maximum write IOPS:
        
        fio --ioengine=libaio --filesize=32G --ramp_time=2s \
        --runtime=5m --numjobs=16 --direct=1 --verify=0 --randrepeat=0 \
        --group_reporting --directory=/mnt/nfs --buffer_compress_percentage=50 \
        --name=randwrite --blocksize=4k --iodepth=256 --readwrite=randwrite
        




## Test performance with multiple client VMs

To achieve the maximum performance for zonal, regional, and enterprise instances, use multiple client VMs.

We recommend using eight client VMs per 1 TiB for instances between 1 and 9.75 TiB. For instances between 10 and 100 TiB use eight client VMs per 10 TiB.

  1. Start the fio server on all client VMs. Fio uses port `8765` to communicate, so this port must be open in your firewall policy.
         
         fio --server
         

  2. Select one client VM that will orchestrate the fio run. Create a [fio job file](https://fio.readthedocs.io/en/latest/fio_doc.html#job-file-format) on that client VM:
         
         cat << EOL > /tmp/fio_job.conf
         [global]
         ioengine=libaio
         ramp_time=2s
         runtime=3m
         time_based
         direct=1
         verify=0
         randrepeat=0
         group_reporting
         buffer_compress_percentage=50
         directory=\${TMP_DIR}
         create_only=\${CREATE_ONLY}
         
         [read-throughput]
         blocksize=1048576
         numjobs=8
         readwrite=read
         filesize=100M
         
         [write-throughput]
         blocksize=1048576
         numjobs=8
         readwrite=write
         filesize=100M
         
         [read-iops]
         blocksize=4k
         iodepth=64
         readwrite=randread
         filesize=1GB
         
         [write-iops]
         blocksize=4k
         iodepth=64
         readwrite=randwrite
         filesize=1GB
         
         EOL
         

  3. Create a `hosts.list` file that contains the IP addresses or DNS names of the fio client VMs:
         
         cat << EOL > /tmp/hosts.list
         <Client 1 IP/DNS>
         <Client 2 IP/DNS>
         ...
         <Client N IP/DNS>
         EOL
         

  4. Create the following dataset in a temporary directory on the client VM you created the job file for:
         
         export TMP_DIR=$(mktemp -d MOUNT_POINT_DIRECTORY/XXXXX)
         chmod 777 ${TMP_DIR}
         export CREATE_ONLY=1
         fio --client=/tmp/hosts.list \
         --section=read-throughput --section=read-iops /tmp/fio_job.conf
         

  5. Run benchmarks using the client VM you created the job file for:

     * Maximum read throughput
    
    export CREATE_ONLY=0
    fio --client=/tmp/hosts.list --section=read-throughput /tmp/fio_job.conf
    

     * Maximum write throughput
    
    export CREATE_ONLY=0
    fio --client=/tmp/hosts.list --section=write-throughput /tmp/fio_job.conf
    

     * Maximum read IOPS
    
    export CREATE_ONLY=0
    fio --client=/tmp/hosts.list --section=read-iops /tmp/fio_job.conf
    

     * Maximum write IOPS
    
    export CREATE_ONLY=0
    fio --client=/tmp/hosts.list --section=write-iops /tmp/fio_job.conf
    

  6. After you are done with testing, stop fio servers on all client VMs and delete their temporary directory:
         
         rm -rf ${TMP_DIR}
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
