---
url: https://docs.cloud.google.com/compute/docs/disks/benchmarking-local-ssd-performance/
title: Benchmarking Local SSD performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:00.000863+00:00
---

# Benchmarking Local SSD performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/benchmarking-local-ssd-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Benchmarking Local SSD performance Stay organized with collections  Save and categorize content based on your preferences. 

Local SSD performance limits provided in the [Choose a storage option section](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) were achieved by using specific settings on the Local SSD instance. If your virtual machine (VM) instance is having trouble reaching these performance limits and you have already configured the instance using the [recommended local SSD settings](https://docs.cloud.google.com/compute/docs/disks/optimizing-local-ssd-performance), you can compare your performance limits against the published limits by replicating the settings used by the Compute Engine team.

**Warning:** The script used in this section is intended for benchmarking and performance comparisons only and is not intended to optimize your disk for performance. We strongly recommend against running this script on a VM with a Local SSD where you want to keep the data because this script **discards any data on your Local SSD**.

These instructions assume that you are using a Linux operating system with the `apt` package manager installed.

**Note:** These instructions create Local SSDs connected to an instance using the NVMe interface. If you use the SCSI interface instead, replace the disk location `/dev/disk/by-id/google-local-nvme-ssd-0` with `/dev/disk/by-id/google-local-ssd-0` in the following commands.

## Create a VM with one Local SSD device

The number of Local SSD that a VM can have is based on the machine type you use to create the VM. For details, see [Choosing a valid number of Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_number_local_ssds).

  1. Create a Local SSD instance that has four or eight vCPUs for each device, depending on your workload.

For example, the following command creates a C3 VM with 4 vCPUs and 1 Local SSD.
         
         gcloud compute instances create c3-ssd-test-instance \
             --machine-type "c3-standard-4-lssd"
         

For second generation and earlier machine types, you specify the number of Local SSD to attach to the VM using the `--local-ssd` flag. The following command creates an N2 VM with 8 vCPUs and 1 Local SSD that uses the NVMe disk interface:
         
         gcloud compute instances create ssd-test-instance \
             --machine-type "n2-standard-8" \
             --local-ssd interface=nvme
         

  2. Run the following script on your VM. The script replicates the settings used to achieve the SSD performance figures provided in the [performance section](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance). Note that the `--bs` parameter defines the block size, which affects the results for different types of read and write operations.
         
         # install tools
         sudo apt-get -y update
         sudo apt-get install -y fio util-linux
         
         # discard Local SSD sectors
         sudo blkdiscard /dev/disk/by-id/google-local-nvme-ssd-0
         
         # full write pass - measures write bandwidth with 1M blocksize
         sudo fio --name=writefile \
         --filename=/dev/disk/by-id/google-local-nvme-ssd-0 --bs=1M --nrfiles=1 \
         --direct=1 --sync=0 --randrepeat=0 --rw=write --end_fsync=1 \
         --iodepth=128 --ioengine=libaio
         
         # rand read - measures max read IOPS with 4k blocks
         sudo fio --time_based --name=readbenchmark --runtime=30 --ioengine=libaio \
         --filename=/dev/disk/by-id/google-local-nvme-ssd-0  --randrepeat=0 \
         --iodepth=128 --direct=1 --invalidate=1 --verify=0 --verify_fatal=0 \
         --numjobs=4 --rw=randread --blocksize=4k --group_reporting
         
         # rand write - measures max write IOPS with 4k blocks
         sudo fio --time_based --name=writebenchmark  --runtime=30 --ioengine=libaio \
         --filename=/dev/disk/by-id/google-local-nvme-ssd-0 --randrepeat=0 \
         --iodepth=128 --direct=1 --invalidate=1 --verify=0 --verify_fatal=0 \
         --numjobs=4 --rw=randwrite --blocksize=4k --group_reporting
         




## Create a VM with the maximum number of Local SSD

  1. If you want to attach [24 or more Local SSD devices](https://docs.cloud.google.com/compute/docs/disks/local-ssd#capacity) to an instance, use a machine type with 32 or more vCPUs.

The following commands create a VM with the maximum allowed number of Local SSD disks using the NVMe interface:

###  Attach Local SSD to VM 
         
         gcloud compute instances create ssd-test-instance \
             --machine-type "n1-standard-32" \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme \
             --local-ssd interface=nvme
         

###  Use -lssd machine types 

Newer machine series offer `-lssd` machine types that come with a predetermined number of Local SSD disks. For example, to benchmark a VM with 32 Local SSD (12 TiB capacity), use the following command:
         
         gcloud compute instances create ssd-test-instance \
             --machine-type "c3-standard-176-lssd"
         

  2. Install the `mdadm` tool. The install process for `mdadm` includes a user prompt that halts scripts, so run the process manually:

###  Debian and Ubuntu 
         
         sudo apt update && sudo apt install mdadm --no-install-recommends
         

###  CentOS and RHEL 
         
         sudo yum install mdadm -y
         

###  SLES and openSUSE 
         
         sudo zypper install -y mdadm
         

  3. Use the `find` command to identify all of the Local SSDs that you want to mount together:
         
         find /dev/ | grep google-local-nvme-ssd
         

The output looks similar to the following:
         
         /dev/disk/by-id/google-local-nvme-ssd-23
         /dev/disk/by-id/google-local-nvme-ssd-22
         /dev/disk/by-id/google-local-nvme-ssd-21
         /dev/disk/by-id/google-local-nvme-ssd-20
         /dev/disk/by-id/google-local-nvme-ssd-19
         /dev/disk/by-id/google-local-nvme-ssd-18
         /dev/disk/by-id/google-local-nvme-ssd-17
         /dev/disk/by-id/google-local-nvme-ssd-16
         /dev/disk/by-id/google-local-nvme-ssd-15
         /dev/disk/by-id/google-local-nvme-ssd-14
         /dev/disk/by-id/google-local-nvme-ssd-13
         /dev/disk/by-id/google-local-nvme-ssd-12
         /dev/disk/by-id/google-local-nvme-ssd-11
         /dev/disk/by-id/google-local-nvme-ssd-10
         /dev/disk/by-id/google-local-nvme-ssd-9
         /dev/disk/by-id/google-local-nvme-ssd-8
         /dev/disk/by-id/google-local-nvme-ssd-7
         /dev/disk/by-id/google-local-nvme-ssd-6
         /dev/disk/by-id/google-local-nvme-ssd-5
         /dev/disk/by-id/google-local-nvme-ssd-4
         /dev/disk/by-id/google-local-nvme-ssd-3
         /dev/disk/by-id/google-local-nvme-ssd-2
         /dev/disk/by-id/google-local-nvme-ssd-1
         /dev/disk/by-id/google-local-nvme-ssd-0
         

`find` does not guarantee an ordering. It's alright if the devices are listed in a different order as long as number of output lines match the expected number of SSD partitions.

If using SCSI devices, use the following `find` command: 
         
         find /dev/ | grep google-local-ssd
         

NVMe devices should all be of form `google-local-nvme-ssd-#` and SCSI devices should all be of form `google-local-ssd-#`.

  4. Use the `mdadm` tool to combine multiple Local SSD devices into a single array named `/dev/md0`. The following example merges twenty four Local SSD devices that use the NVMe interface. For Local SSD devices that use SCSI, use the device names returned from the `find` command in step 3.
         
         sudo mdadm --create /dev/md0 --level=0 --raid-devices=24 \
         /dev/disk/by-id/google-local-nvme-ssd-0 \
         /dev/disk/by-id/google-local-nvme-ssd-1 \
         /dev/disk/by-id/google-local-nvme-ssd-2 \
         /dev/disk/by-id/google-local-nvme-ssd-3 \
         /dev/disk/by-id/google-local-nvme-ssd-4 \
         /dev/disk/by-id/google-local-nvme-ssd-5 \
         /dev/disk/by-id/google-local-nvme-ssd-6 \
         /dev/disk/by-id/google-local-nvme-ssd-7 \
         /dev/disk/by-id/google-local-nvme-ssd-8 \
         /dev/disk/by-id/google-local-nvme-ssd-9 \
         /dev/disk/by-id/google-local-nvme-ssd-10 \
         /dev/disk/by-id/google-local-nvme-ssd-11 \
         /dev/disk/by-id/google-local-nvme-ssd-12 \
         /dev/disk/by-id/google-local-nvme-ssd-13 \
         /dev/disk/by-id/google-local-nvme-ssd-14 \
         /dev/disk/by-id/google-local-nvme-ssd-15 \
         /dev/disk/by-id/google-local-nvme-ssd-16 \
         /dev/disk/by-id/google-local-nvme-ssd-17 \
         /dev/disk/by-id/google-local-nvme-ssd-18 \
         /dev/disk/by-id/google-local-nvme-ssd-19 \
         /dev/disk/by-id/google-local-nvme-ssd-20 \
         /dev/disk/by-id/google-local-nvme-ssd-21 \
         /dev/disk/by-id/google-local-nvme-ssd-22 \
         /dev/disk/by-id/google-local-nvme-ssd-23
         

The response is similar to the following:
         
         mdadm: Defaulting to version 1.2 metadata
         mdadm: array /dev/md0 started.
         

You can confirm the details of the array with `mdadm --detail`. Adding the `--prefer=by-id` flag will list the devices using the `/dev/disk/by-id` paths.
         
         sudo mdadm --detail --prefer=by-id /dev/md0
         

The output should look similar to the following for each device in the array.
         
         ...
          Number   Major   Minor   RaidDevice State
          0     259        0        0      active sync   /dev/disk/by-id/google-local-nvme-ssd-0
          ...
         

  5. Run the following script on your VM. The script replicates the settings used to achieve the SSD performance figures provided in the [performance section](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance). that the `--bs` parameter defines the block size, which affects the results for different types of read and write operations.
         
         # install tools
         sudo apt-get -y update
         sudo apt-get install -y fio util-linux
         
         # full write pass - measures write bandwidth with 1M blocksize
         sudo fio --name=writefile \
         --filename=/dev/md0 --bs=1M --nrfiles=1 \
         --direct=1 --sync=0 --randrepeat=0 --rw=write --end_fsync=1 \
         --iodepth=128 --ioengine=libaio
         
         # rand read - measures max read IOPS with 4k blocks
         sudo fio --time_based --name=benchmark  --runtime=30 \
         --filename=/dev/md0 --ioengine=libaio --randrepeat=0 \
         --iodepth=128 --direct=1 --invalidate=1 --verify=0 --verify_fatal=0 \
         --numjobs=48 --rw=randread --blocksize=4k --group_reporting --norandommap
         
         # rand write - measures max write IOPS with 4k blocks
         sudo fio --time_based --name=benchmark  --runtime=30 \
         --filename=/dev/md0 --ioengine=libaio --randrepeat=0 \
         --iodepth=128 --direct=1 --invalidate=1 --verify=0 --verify_fatal=0 \
         --numjobs=48 --rw=randwrite --blocksize=4k --group_reporting --norandommap
         




## Benchmarking Storage Optimized VMs

  1. Storage Optimized VMs (like the Z3 Family) should be benchmarked directly against the device partitions. You can get the partition names with `lsblk`
         
         lsblk -o name,size -lpn | grep 2.9T | awk '{print $1}'
         

The output looks similar to the following:
         
         /dev/nvme1n1
         /dev/nvme2n1
         /dev/nvme3n1
         /dev/nvme4n1
         /dev/nvme5n1
         /dev/nvme6n1
         /dev/nvme7n1
         /dev/nvme8n1
         /dev/nvme9n1
         /dev/nvme10n1
         /dev/nvme11n1
         /dev/nvme12n1
         

  2. Directly run the benchmarks against the Local SSD partitions by separating them with colon delimiters.
         
         # install benchmarking tools
         sudo apt-get -y update
         sudo apt-get install -y fio util-linux
         
         # Full Write Pass.
         # SOVM achieves max read performance on previously written/discarded ranges.
         sudo  fio --readwrite=write --blocksize=1m --iodepth=4 --ioengine=libaio \
         --direct=1 --group_reporting \
         --name=job1 --filename=/dev/nvme1n1 --name=job2 --filename=/dev/nvme2n1 \
         --name=job3 --filename=/dev/nvme3n1 --name=job4 --filename=/dev/nvme4n1 \
         --name=job5 --filename=/dev/nvme5n1 --name=job6 --filename=/dev/nvme6n1 \
         --name=job7 --filename=/dev/nvme7n1 --name=job8 --filename=/dev/nvme8n1 \
         --name=job9 --filename=/dev/nvme9n1 --name=job10 --filename=/dev/nvme10n1 \
         --name=job11  --filename=/dev/nvme11n1 --name=job12 --filename=/dev/nvme12n1
         
         # rand read - measures max read IOPS with 4k blocks
         sudo fio --readwrite=randread --blocksize=4k --iodepth=128  \
         --numjobs=4 --direct=1 --runtime=30 --group_reporting  --ioengine=libaio \
         --name=job1 --filename=/dev/nvme1n1 --name=job2 --filename=/dev/nvme2n1 \
         --name=job3 --filename=/dev/nvme3n1 --name=job4 --filename=/dev/nvme4n1 \
         --name=job5 --filename=/dev/nvme5n1 --name=job6 --filename=/dev/nvme6n1 \
         --name=job7 --filename=/dev/nvme7n1 --name=job8 --filename=/dev/nvme8n1 \
         --name=job9 --filename=/dev/nvme9n1 --name=job10 --filename=/dev/nvme10n1 \
         --name=job11  --filename=/dev/nvme11n1 --name=job12 --filename=/dev/nvme12n1
         
         # rand write - measures max write IOPS with 4k blocks
         sudo fio --readwrite=randwrite --blocksize=4k --iodepth=128 \
         --numjobs=4 --direct=1 --runtime=30 --group_reporting --ioengine=libaio \
         --name=job1 --filename=/dev/nvme1n1 --name=job2 --filename=/dev/nvme2n1 \
         --name=job3 --filename=/dev/nvme3n1 --name=job4 --filename=/dev/nvme4n1 \
         --name=job5 --filename=/dev/nvme5n1 --name=job6 --filename=/dev/nvme6n1 \
         --name=job7 --filename=/dev/nvme7n1 --name=job8 --filename=/dev/nvme8n1 \
         --name=job9 --filename=/dev/nvme9n1 --name=job10 --filename=/dev/nvme10n1 \
         --name=job11  --filename=/dev/nvme11n1 --name=job12 --filename=/dev/nvme12n1
         




## What's next

  * Learn about [Local SSD pricing](https://docs.cloud.google.com/compute/disks-image-pricing#localssdpricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
