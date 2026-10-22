---
url: https://docs.cloud.google.com/compute/docs/disks/benchmark-hyperdisk-performance/
title: Benchmark Hyperdisk performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:23.493976+00:00
---

# Benchmark Hyperdisk performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/benchmark-hyperdisk-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Benchmark Hyperdisk performance Stay organized with collections  Save and categorize content based on your preferences. 

To benchmark [Google Cloud Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisks), use [Flexible I/O tester (FIO)](https://fio.readthedocs.io/) instead of other disk benchmarking tools such as [`dd`](https://en.wikipedia.org/wiki/Dd_\(Unix\)). By default, `dd` uses a very low I/O queue depth, so it is difficult to ensure that the benchmark is generating a sufficient number of bytes and I/O operations to accurately test disk performance.

Additionally, special devices used with `dd` are often very slow and don't accurately reflect disk performance. In general, avoid using special devices such as `/dev/urandom`, `/dev/random`, and `/dev/zero` in your Hyperdisk performance benchmarks.

To measure IOPS and throughput of a disk in use on a running instance, benchmark the file system with its intended configuration. Use this option to test a realistic workload without losing the contents of your existing disk. Note that when you benchmark the file system on an existing disk, there are many factors specific to your development environment that may affect benchmarking results, and you may not reach the [disk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine_type_support).

To measure the raw performance of a Hyperdisk, benchmark the block device directly. Use this option to compare raw disk performance to [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits).

The following commands work with Debian or Ubuntu operating systems with the `apt` package manager.

## Benchmarking IOPS and throughput of a disk on a running instance

If you want to measure IOPS and throughput for a realistic workload on an active disk on a running VM instance without losing the contents of your disk, benchmark against a new directory on the existing file system.

### Prepare for testing

  1. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  2. Install dependencies:
         
         sudo apt update
         sudo apt install -y fio
         

  3. If your Hyperdisk volume is not yet formatted, [format and mount the disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).

  4. In the terminal, list the disks that are attached to your VM and find the disk that you want to test.
         
         sudo lsblk
         

The preceding command produces output similar to the following:
         
         NAME         MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
         nvme0n1      259:0    0    10G  0 disk
         ├─nvme0n1p1  259:1    0   9.9G  0 part  /
         ├─nvme0n1p14 259:2    0     4M  0 part
         └─nvme0n1p15 259:3    0   106M  0 part  /boot/efi
         nvme0n2      259:4    0   3.4T  0 disk
         

In this example, we're testing a 3,500 GiB Hyperdisk Extreme volume with device name `nvme0n2`.

**Note:** The command `lsblk` displays the prefix `nvme` for disks attached using the NVMe interface, and the prefix `sd` for disks attached using the SCSI interface.
  5. Create a new directory, `fiotest`, on the disk. In this example, the disk is mounted at `/mnt/disks/mnt_dir`:
         
         TEST_DIR=/mnt/disks/mnt_dir/fiotest
         sudo mkdir -p $TEST_DIR
         

  6. If the VM uses the NVMe disk interface for the Hyperdisk volume's attachment (if the raw disk name is prefixed with `nvme`), perform the following steps to obtain the number of NUMA nodes available to the VM.

The benchmarking strategy for NVMe disks differs for VMs with only one NUMA node and VMs with more than one NUMA node. When testing Hyperdisk performance using the NVMe disk interface, only 256 NVMe queue sizes are allocated per queue. Because of the limited NVMe queue sizes available and the potential contention coming from the other disks attached to the same VM, these benchmark tests use two NVMe disk queues to maintain an aggregated queue size capable of handling the iodepth of 256.

     1. Get the number of NUMA nodes.
            
            lscpu | grep -i 'numa node(s)' | awk '{print $NF}'
            

     2. If the VM has only 1 NUMA node, obtain the CPU-to-NVMe queue mapping. You will use this information later for the `--cpus-allowed` parameter.
            
            QUEUE_1_CPUS=$(cat /sys/class/block/nvme0n2/mq/*/cpu_list | sed -n 1p | tr -d " \t")
            QUEUE_2_CPUS=$(cat /sys/class/block/nvme0n2/mq/*/cpu_list | sed -n 2p | tr -d " \t")
            




### Test write throughput

Test write throughput by performing sequential writes with multiple parallel streams (16+), using an I/O block size of 1 MB and an I/O depth of at least 64.

  1. If the Hyperdisk volume uses the SCSI interface:
         
         sudo fio --directory=$TEST_DIR \
         --numjobs=16 --size=10G --time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
         --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
         --name=write_throughput
         

  2. If the Hyperdisk volume uses the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 \
            --size=10G --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
            --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
            --cpus_allowed_policy=split \
            --group_reporting \
            --name=write_throughput --cpus_allowed=$QUEUE_1_CPUS \
            --name=write_throughput_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 \
            --size=10G --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
            --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
            --group_reporting \
            --name=write_throughput --numa_cpu_nodes=0 \
            --name=write_throughput_2 --numa_cpu_nodes=1
            




### Test write IOPS

Test write IOPS by performing random writes, using an I/O block size of 4 KB and an I/O depth of at least 256.

  1. If the Hyperdisk volume is attached using SCSI interface:
         
         sudo fio --directory=$TEST_DIR \
         --numjobs=16 --size=10G -time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randwrite \
         --iodepth_batch_submit=256  --iodepth_batch_complete_max=256 \
         --name=write_iops
         

  2. If the Hyperdisk volume uses the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 \
            --size=10G --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randwrite \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --cpus_allowed_policy=split \
            --group_reporting \
            --name=write_iops --cpus_allowed=$QUEUE_1_CPUS \
            --name=write_iops_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 --size=10G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randwrite \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --group_reporting \
            --name=write_iops --numa_cpu_nodes=0 \
            --name=write_iops_2 --numa_cpu_nodes=1
            




### Test read throughput

Test read throughput by performing sequential reads with multiple parallel streams (16+), using an I/O block size of 1 MB, and an I/O depth of at least 64.

  1. If the Hyperdisk volume uses the SCSI interface:
         
         sudo fio --directory=$TEST_DIR \
         --numjobs=16 --size=10G --time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
         --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
         --name=read_throughput
         

  2. If the Hyperdisk volume uses the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 --size=10G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
            --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
            --cpus_allowed_policy=split \
            --group_reporting \
            --name=read_throughput --cpus_allowed=$QUEUE_1_CPUS \
            --name=read_throughput_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 --size=10G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
            --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
            --group_reporting \
            --name=read_throughput --numa_cpu_nodes=0 \
            --name=read_throughput_2 --numa_cpu_nodes=1
            




### Test read IOPS

Test read IOPS by performing random reads, using an I/O block size of 4 KB and an I/O depth of at least 256.

  1. If the Hyperdisk volume uses the SCSI interface:
         
         sudo fio --directory=$TEST_DIR \
         --numjobs=16 --size=10G --time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randread \
         --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
         --name=read_iops
         

  2. If the Hyperdisk volume uses the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 --size=10G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randread \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --cpus_allowed_policy=split \
            --group_reporting \
            --name=read_iops --cpus_allowed=$QUEUE_1_CPUS \
            --name=read_iops_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            sudo fio --directory=$TEST_DIR --numjobs=8 --size=10G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randread \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --group_reporting \
            --name=read_iops --numa_cpu_nodes=0 \
            --name=read_iops_2 --numa_cpu_nodes=1
            




### Clean up

Remove the test directories.
    
    
    sudo rm $TEST_DIR/write* $TEST_DIR/read*
    

## Benchmarking IOPS and throughput for Hyperdisk Extreme on C3 VMs

Google Cloud Hyperdisk Extreme offers higher performance on C3 VMs with 176 vCPUs. To reach the higher performance limits, you must attach multiple Hyperdisk Extreme volumes to the VM.

To measure I/O per second (IOPS) or throughput for a realistic workload on active disks on a running C3 VM without losing the contents of your existing data disks, benchmark against a new directory on the existing file system and attach new Hyperdisk Extreme volumes to the VM for the benchmarking tasks.

For disks attached with the NVMe interface it is recommended to distribute the I/O workload across all NVMe queues available to the VM. This maximizes the Hyperdisk volume's performance. On C3 VMs with 176 vCPUs, there are four NUMA nodes mapped 1-to-1 to four NVMe queues. This mapping is assumed for the benchmark tests in this section.

### Prepare for testing

  1. [Add new Hyperdisk Extreme disks to your VM](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk), and consult the [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits) to derive the disk setup needed for your target performance.

  2. Connect to your instance:

     * Instructions for [Linux](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance)
     * Instructions for [Windows](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)
  3. Install dependencies:
         
         sudo apt update
         sudo apt install -y fio
         

  4. List the disks that are attached to your VM and find the disk that you want to test.
         
         sudo lsblk
         

The preceding command produces output similar to the following:
         
         NAME         MAJ:MIN RM   SIZE RO TYPE  MOUNTPOINT
         nvme0n1      259:0    0    10G  0 disk
         ├─nvme0n1p1  259:1    0   9.9G  0 part  /
         ├─nvme0n1p14 259:2    0     4M  0 part
         └─nvme0n1p15 259:3    0   106M  0 part  /boot/efi
         nvme0n2      259:4    0   2.5T  0 disk
         nvme0n3      259:5    0   2.5T  0 disk
         nvme0n4      259:6    0   2.5T  0 disk
         

In this example, we're testing Google Cloud Hyperdisk performance across three 2,500 GiB Hyperdisk Extreme volumes with devices named `nvme0n2`, `nvme0n3` and `nvme0n4`.

**Note:** C3 only supports the NVMe disk interface, so all devices listed by the `lsblk` command have the prefix `nvme`.



### Benchmark throughput of Hyperdisk Extreme on C3

This section shows how to benchmark both read and write throughput for Hyperdisk Extreme disks.

#### Preparation for testing

Before you begin benchmarking the performance of Hyperdisk Extreme disks attached to a C3 VM with 176 vCPUs, complete the following steps.

  1. Create a new directory, `fiotest`, in your operating system. In this example, the root directory is `/mnt/disks/mnt_dir`:
         
         TEST_DIR=/mnt/disks/mnt_dir/fiotest
         sudo mkdir -p $TEST_DIR
         

  2. Because the VM requires more than one disk to reach the highest performance levels, for simplicity, perform RAID 0 on all attached Hyperdisk volumes. This makes it easier for data to be evenly distributed across multiple Hyperdisk volumes.

In this example, RAID 0 is performance on three Hyperdisk Extreme volumes attached to the C3 VM.
         
         sudo mdadm --create /dev/md0 --level=0 --raid-devices=3 /dev/nvme0n2 /dev/nvme0n3 /dev/nvme0n4
         

  3. [Format and mount](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux) the RAID volume `/dev/md0`.




#### Test write throughput

Test write throughput by performing sequential writes with multiple parallel streams (at least 16), using an I/O block size of 1 MiB and a total I/O depth of at least 32 per NVMe queue.
    
    
    # Running this command causes data loss on the targeted file on the device.
    # We strongly recommend using a throwaway disk.
    
    sudo fio --name=global --group_reporting=1 --filesize=1024G \
    --filename=$TEST_DIR/fiotestfile --numjobs=4 --size=64G \
    --offset_increment=64G --time_based --runtime=5m \
    --ramp_time=10s --ioengine=libaio --direct=1 --verify=0 \
    --bs=1M --iodepth=8 --rw=write \
    --name=write_throughput --numa_cpu_nodes=0 \
    --name=write_throughput_1 --numa_cpu_nodes=1 \
    --name=write_throughput_2 --numa_cpu_nodes=2 \
    --name=write_throughput_3 --numa_cpu_nodes=3
    

#### Test read throughput

Test read throughput by performing sequential reads with multiple parallel streams (at least 16), using an I/O block size of 1 MiB and a total I/O depth of at least 32 per NVMe queue.
    
    
    sudo fio --name=global --group_reporting=1 --filesize=1024G \
    --filename=$TEST_DIR/fiotestfile --numjobs=4 --size=64G \
    --offset_increment=64G --time_based --runtime=5m \
    --ramp_time=10s --ioengine=libaio --direct=1 \
    --verify=0 --bs=1M --iodepth=8 --rw=read \
    --name=read_throughput --numa_cpu_nodes=0 \
    --name=read_throughput_1 --numa_cpu_nodes=1 \
    --name=read_throughput_2 --numa_cpu_nodes=2 \
    --name=read_throughput_3 --numa_cpu_nodes=3
    

### Benchmark IOPS of Hyperdisk Extreme on C3

To benchmark for the I/O per second (IOPS) performance, we recommend performing parallel small I/O operations directly to or from raw disks (without RAID).

#### Test write IOPS

Test write IOPS by performing random writes, using an I/O block size of 4 KiB and an I/O depth of at least 256, utilizing at least 2 NVMe queues.
    
    
    # Running this command causes data loss on the targeted device.
    # We strongly recommend using a throwaway disk.
    
    sudo fio --name=global --group_reporting=1 \
    --directory=/ --bs=4K --direct=1 \
    --filesize=512G --iodepth=256 \
    --iodepth_batch_complete_max=256 --iodepth_batch_submit=256 \
    --ioengine=libaio --numjobs=5 --ramp_time=10s \
    --randrepeat=0 --runtime=5m --rw=randwrite \
    --time_based=1 --verify=0 \
    --name=write_iops_test --filename=/dev/nvme0n2 --numa_cpu_nodes=0 \
    --name=write_iops_test_1 --filename=/dev/nvme0n3  --numa_cpu_nodes=1 \
    --name=write_iops_test_2 --filename=/dev/nvme0n4 --numa_cpu_nodes=2
    

#### Test read IOPS

Test read IOPS by performing random reads, using an I/O block size of 4 KiB and an I/O depth of at least 256, utilizing at least 2 NVMe queues.
    
    
    sudo fio --name=global --group_reporting=1 --directory=/ \
    --bs=4K --direct=1 --filesize=512G --iodepth=256 \
    --iodepth_batch_complete_max=256 --iodepth_batch_submit=256 \
    --ioengine=libaio --numjobs=5 --ramp_time=10s \
    --randrepeat=0 --runtime=5m --rw=randread \
    --time_based=1 --verify=0 \
    --name=read_iops_test --filename=/dev/nvme0n2 --numa_cpu_nodes=0 \
    --name=read_iops_test_1 --filename=/dev/nvme0n3  --numa_cpu_nodes=1 \
    --name=read_iops_test_2 --filename=/dev/nvme0n4 --numa_cpu_nodes=2
    

### Benchmark latency of Hyperdisk Extreme on C3

While testing I/O latency, the VM must not reach maximum bandwidth or IOPS. If it does, the observed latency won't reflect the actual Hyperdisk I/O latency. For example, if the VM reaches the IOPS limit at an I/O depth of 30 and the `fio` command has doubled that, then the total IOPS remains the same and the reported I/O latency doubles.

It's sufficient to target a single raw disk device directly to obtain realistic I/O latencies.

#### Test write latency

Test write latency by performing random writes, using an I/O block size of 4 KiB and an I/O depth of 4.
    
    
    # Running this command causes data loss on the targeted device.
    # We strongly recommend using a throwaway disk.
    
    sudo fio --filename=/dev/nvme0n2  \
    --filesize=512G --time_based \
    --runtime=5m --ramp_time=10s --ioengine=libaio \
    --direct=1 --verify=0 --bs=4K --iodepth=4 --rw=randwrite \
    --iodepth_batch_submit=4 --iodepth_batch_complete_max=4 \
    --name=write_latency
    

#### Test read latency

Test read latency by performing random reads, using an I/O block size of 4 KiB and an I/O depth of 4.
    
    
    sudo fio --filename=/dev/nvme0n2  \
    --filesize=512G --time_based \
    --runtime=5m --ramp_time=10s --ioengine=libaio \
    --direct=1 --verify=0 --bs=4K --iodepth=4 --rw=randread \
    --iodepth_batch_submit=4 --iodepth_batch_complete_max=4 \
    --name=read_latency
    

### Clean up

  1. Remove the test files.
         
         sudo rm -rf $TEST_DIR/*
         

  2. Unmount and stop the RAID volume.
         
         sudo umount /dev/md0
         sudo mdadm --stop /dev/md0
         

  3. Detach and delete the attached Hyperdisk volumes. Refer to the [`gcloud compute instances detach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk) and [`gcloud compute disks delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete) commands.




## Benchmarking raw Hyperdisk performance

If you want to measure the performance of Hyperdisk volumes alone, outside of your development environment, you can test read and write performance for a block device on a throwaway disk and VM.

The following commands assume a 3,500 GiB Hyperdisk Extreme volume attached to your VM. This disk size is necessary to achieve the 32 vCPU VM throughput limits. If your device size is different, modify the value of the `--filesize` argument in the following commands. For more information about the performance limits for VM machine types, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support).

**Warning:** The commands in this section overwrite the contents of an attached disk. _We strongly recommend using a throwaway VM and disk_.

### Prepare for testing

  1. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

  2. Install dependencies:
         
         sudo apt-get update
         sudo apt-get install -y fio
         

  3. Obtain the path to the raw disk. Store the path in a variable. The following example uses `/dev/nvme0n2` as the raw disk path:
         
         TEST_DIR=/dev/nvme0n2
         

  4. Fill the disk with nonzero data. Hyperdisk reads from empty blocks have a latency profile that is different from blocks that contain data. We recommend filling the disk before running any read latency benchmarks.
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         
         sudo fio --name=fill_disk \
         --filename=$TEST_DIR --filesize=2500G \
         --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
         --bs=128K --iodepth=64 --rw=randwrite \
         --iodepth_batch_submit=64  --iodepth_batch_complete_max=64
         

  5. If the VM uses the NVMe disk interface for the Hyperdisk attachment (if the raw disk name is prefixed with `nvme`), perform the following steps to obtain the number of NUMA nodes available to the VM.

The benchmarking strategy for NVMe disks differs for VMs with only one NUMA node and VMs with more than one NUMA node. When testing Hyperdisk performance using the NVMe disk interface, only 256 NVMe queue sizes are allocated per queue. Because of the limited NVMe queue sizes available and the potential contention coming from the other disks attached to the same VM, these benchmark tests use two NVMe disk queues to maintain an aggregated queue size capable of handling the iodepth of 256.

     1. Get the number of NUMA nodes.
            
            lscpu | grep -i 'numa node(s)' | awk '{print $NF}'
            

     2. If the VM has only 1 NUMA node, obtain the CPU-to-NVMe queue mapping. You will use this information later for the `--cpus-allowed` parameter.
            
            QUEUE_1_CPUS=$(cat /sys/class/block/nvme0n2/mq/*/cpu_list | sed -n 1p | tr -d " \t")
            QUEUE_2_CPUS=$(cat /sys/class/block/nvme0n2/mq/*/cpu_list | sed -n 2p | tr -d " \t")
            




### Test write throughput

Test write throughput by performing sequential writes with multiple parallel streams (16+), using 1 MB as the I/O size and having an I/O depth that is 64 or greater.

  1. If the Hyperdisk is attached using the SCSI interface:
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         
         sudo fio --filename=$TEST_DIR \
         --numjobs=16 --size=500G --time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
         --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
         --offset_increment=20G \
         --name=write_throughput
         

  2. If the Hyperdisk volume uses the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            # Running this command causes data loss on the second device.
            # We strongly recommend using a throwaway VM and disk.
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
            --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
            --cpus_allowed_policy=split \
            --offset_increment=20G --group_reporting \
            --name=write_throughput --cpus_allowed=$QUEUE_1_CPUS \
            --name=write_throughput_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            # Running this command causes data loss on the second device.
            # We strongly recommend using a throwaway VM and disk.
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=write \
            --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
            --offset_increment=20G --group_reporting \
            --name=write_throughput --numa_cpu_nodes=0 \
            --name=write_throughput_2 --numa_cpu_nodes=1
            




### Test write IOPS

To achieve maximum Hyperdisk IOPS, you must maintain a deep I/O queue. If, for example, the write latency is 1 millisecond, the VM can achieve, at most, 1,000 IOPS for each I/O in flight. To achieve 15,000 write IOPS, the VM must maintain at least 15 I/O operations in flight. If your disk and VM can achieve 30,000 write IOPS, the number of I/O operations in flight must be at least 30. If the I/O size is larger than 4 KB, the VM might reach the bandwidth limit before it reaches the IOPS limit.

Test write IOPS by performing random writes, using an I/O block size of 4 KB and an I/O depth of at least 256.

  1. If the Hyperdisk Extreme volume is attached using SCSI interface:
         
         # Running this command causes data loss on the second device.
         # We strongly recommend using a throwaway VM and disk.
         
         sudo fio --filename=$TEST_DIR \
         --numjobs=16 --size=500G -time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randwrite \
         --iodepth_batch_submit=256  --iodepth_batch_complete_max=256 \
         --name=write_iops
         

  2. If the Hyperdisk Extreme volume is attached using the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            # Running this command causes data loss on the second device.
            # We strongly recommend using a throwaway VM and disk.
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randwrite \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --cpus_allowed_policy=split \
            --group_reporting \
            --name=write_write_iops --cpus_allowed=$QUEUE_1_CPUS \
            --name=write_write_iops_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            # Running this command causes data loss on the second device.
            # We strongly recommend using a throwaway VM and disk.
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randwrite \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --group_reporting \
            --name=write_iops --numa_cpu_nodes=0 \
            --name=write_iops_2 --numa_cpu_nodes=1
            




### Test write latency

While testing I/O latency, the VM must not reach maximum bandwidth or IOPS; otherwise, the observed latency won't reflect actual Hyperdisk I/O latency. For example, if the IOPS limit is reached at an I/O depth of 30 and the `fio` command has doubled that, then the total IOPS remains the same and the reported I/O latency doubles.
    
    
    # Running this command causes data loss on the second device.
    # We strongly recommend using a throwaway VM and disk.
    sudo fio --filename=$TEST_DIR \
    --filesize=500G --time_based \
    --runtime=5m --ramp_time=10s --ioengine=libaio \
    --direct=1 --verify=0 --bs=4K --iodepth=4 --rw=randwrite \
    --iodepth_batch_submit=4 --iodepth_batch_complete_max=4 \
    --name=write_latency
    

### Test read bandwidth

Test read bandwidth by performing sequential reads with multiple parallel streams (16+), using an I/O size of 1 MB and an I/O depth of at least 64.

  1. If the Hyperdisk Extreme volume is attached using the SCSI interface:
         
         sudo fio --filename=$TEST_DIR \
          --numjobs=16 --size=500G --time_based \
          --runtime=5m --ramp_time=10s --ioengine=libaio \
          --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
          --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
          --offset_increment=20G --name=read_bandwidth

  2. If the Hyperdisk Extreme volume is attached using the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
              --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
              --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
              --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
              --cpus_allowed_policy=split \
              --offset_increment=20G --group_reporting \
              --name=read_bandwidth --cpus_allowed=$QUEUE_1_CPUS \
              --name=read_bandwidth_2 --cpus_allowed=$QUEUE_2_CPUS

     2. If the VM has more than one NUMA node, use the following command:
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
              --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
              --direct=1 --verify=0 --bs=1M --iodepth=64 --rw=read \
              --iodepth_batch_submit=64 --iodepth_batch_complete_max=64 \
              --offset_increment=20G --group_reporting \
              --name=read_bandwidth --numa_cpu_nodes=0 \
              --name=read_bandwidth_2 --numa_cpu_nodes=1




### Test read IOPS

To achieve the maximum Hyperdisk IOPS, you must maintain a deep I/O queue. If, for example, the I/O size is larger than 4 KB, the VM might reach the bandwidth limit before it reaches the IOPS limit. To achieve the maximum read IOPS available for a machine type, specify `--iodepth=256` for this test.

  1. If the Hyperdisk Extreme volume is attached using the SCSI interface:
         
         sudo fio --filename=$TEST_DIR \
         --numjobs=16 --size=500G --time_based \
         --runtime=5m --ramp_time=10s --ioengine=libaio \
         --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randread \
         --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
         --name=read_iops
         

  2. If the Hyperdisk Extreme volume is attached using the NVMe interface:

     1. If the VM has only one NUMA node, use the following command:
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randread \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --cpus_allowed_policy=split \
            --group_reporting \
            --name=read_iops --cpus_allowed=$QUEUE_1_CPUS \
            --name=read_iops_2 --cpus_allowed=$QUEUE_2_CPUS
            

     2. If the VM has more than one NUMA node, use the following command:
            
            sudo fio --filename=$TEST_DIR --numjobs=8 --size=500G \
            --time_based --runtime=5m --ramp_time=10s --ioengine=libaio \
            --direct=1 --verify=0 --bs=4K --iodepth=256 --rw=randread \
            --iodepth_batch_submit=256 --iodepth_batch_complete_max=256 \
            --group_reporting \
            --name=read_iops --numa_cpu_nodes=0 \
            --name=read_iops_2 --numa_cpu_nodes=1
            




### Test read latency

It's important to fill the disk with data to get a realistic latency measurement. It's important that the VM not reach IOPS or throughput limits during this test because after the Hyperdisk volume reaches its saturation limit, it pushes back on incoming I/O operations. This push back is reflected as an artificial increase in I/O latency.
    
    
     sudo fio --filename=$TEST_DIR \
     --filesize=500G --time_based \
     --runtime=5m --ramp_time=10s --ioengine=libaio \
     --direct=1 --verify=0 --bs=4K --iodepth=4 --rw=randread \
     --iodepth_batch_submit=4 --iodepth_batch_complete_max=4 \
     --name=read_latency
    

### Clean up

If you used a throwaway disk and VM as recommended, after completing the benchmark tests, you can:

  * Detach and delete the disk.
  * Delete the VM.



## What's next

  * Learn about [Hyperdisk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
