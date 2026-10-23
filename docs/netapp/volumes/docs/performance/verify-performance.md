---
url: https://docs.cloud.google.com/netapp/volumes/docs/performance/verify-performance/
title: Verify performance \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:25.124202+00:00
---

# Verify performance  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/performance/verify-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Verify performance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to verify volume performance using the [Fio](https://fio.readthedocs.io/en/latest/fio_doc.html) tool. To optimize your applications, it's important to establish a baseline performance for your volumes.

## Measure volume performance using Fio

Use the I/O generator tool, [Fio](https://fio.readthedocs.io/en/latest/fio_doc.html), to measure baseline performance.

## Using Fio

Fio applies a workload which you can specify through a command line interface or a configuration file. While it runs, Fio shows a progress indicator with current throughput and input and output per second (IOPS) numbers. After it ends, a detailed summary displays.

## Fio results example

The following examples show a single-threaded, 4k random write job running for 60 seconds, which is a useful way to measure baseline latency. In the following commands, the `--directory` parameter points to a folder with a mounted NetApp Volumes share:
    
    
      $ FIO_COMMON_ARGS=--size=10g --fallocate=none --direct=1 --runtime=60 --time_based --ramp_time=5
      $ fio $FIO_COMMON_ARGS --directory=/netapp --ioengine=libaio --rw=randwrite --bs=4k --iodepth=1 --name=nv
      cvs: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
      fio-3.28
      Starting 1 process
      cvs: Laying out IO file (1 file / 10240MiB)
      Jobs: 1 (f=1): [w(1)][100.0%][w=7856KiB/s][w=1964 IOPS][eta 00m:00s]
      cvs: (groupid=0, jobs=1): err= 0: pid=1891: Wed Dec 21 14:56:37 2022
        write: IOPS=1999, BW=7999KiB/s (8191kB/s)(469MiB/60001msec); 0 zone resets
          slat (usec): min=4, max=417, avg=12.06, stdev= 5.71
          clat (usec): min=366, max=27978, avg=483.59, stdev=91.34
          lat (usec): min=382, max=28001, avg=495.96, stdev=91.89
          clat percentiles (usec):
          |  1.00th=[  408],  5.00th=[  429], 10.00th=[  437], 20.00th=[  449],
          | 30.00th=[  461], 40.00th=[  469], 50.00th=[  482], 60.00th=[  490],
          | 70.00th=[  498], 80.00th=[  515], 90.00th=[  529], 95.00th=[  553],
          | 99.00th=[  611], 99.50th=[  652], 99.90th=[  807], 99.95th=[  873],
          | 99.99th=[ 1020]
        bw (  KiB/s): min= 7408, max= 8336, per=100.00%, avg=8002.05, stdev=140.09, samples=120
        iops        : min= 1852, max= 2084, avg=2000.45, stdev=35.06, samples=120
        lat (usec)   : 500=70.67%, 750=29.17%, 1000=0.15%
        lat (msec)   : 2=0.01%, 4=0.01%, 50=0.01%
        cpu          : usr=2.04%, sys=3.25%, ctx=120561, majf=0, minf=58
        IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
          submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
          complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
          issued rwts: total=0,119984,0,0 short=0,0,0,0 dropped=0,0,0,0
          latency   : target=0, window=0, percentile=100.00%, depth=1
    
      Run status group 0 (all jobs):
        WRITE: bw=7999KiB/s (8191kB/s), 7999KiB/s-7999KiB/s (8191kB/s-8191kB/s), io=469MiB (491MB), run=60001-60001msec
    

Read the following lines for details about the performance results:

  * **Latency** : `lat (usec): min=382, max=28001, avg=495.96, stdev=91.89`

The average latency is 495.96 microseconds (usec), roughly 0.5 ms, which is an ideal latency.

  * **IOPS** : `min= 1852, max= 2084, avg=2000.45, stdev=35.06, samples=120`

The preceding example shows an average of 2,000 IOPS. That value is expected for a single-threaded job with 0.5 ms latency (`IOPS = 1000 ms/0.5 ms = 2000`).

  * **Throughput** : `bw ( KiB/s): min= 7408, max=8336, per=100.00%, avg=8002.05, stdev=140.09`

The throughput average is 8002 KiBps, which is the expected result for 2,000 IOPS with a block size of 4 KiB (`2000 1/s * 4 KiB = 8,000 KiB/s`).




### Measure latency

Latency is a fundamental metric for volume performance. It's a result of client and server capabilities, the distance between client and server (your volume), and equipment in between. The main component of the metric is distance-induced latency.

You can ping the IP of your volume to get the round-trip time, which is a rough estimate of your latency.

Latency is affected by the block size and whether you are doing read or write operations. We recommend that you use the following parameters to measure the baseline latency between your client and a volume:

### Linux
    
    
    fio --directory=/netapp \
     --ioengine=libaio \
     --rw=randwrite \
     --bs=4k --iodepth=1 \
     --size=10g \
     --fallocate=none \
     --direct=1 \
     --runtime=60 \
     --time_based \
     --ramp_time=5 \
     --name=latency

### Windows
    
    
    fio --directory=Z\:\
    --ioengine=windowsaio
    --thread
    --rw=randwrite
    --bs=4k
    --iodepth=1
    --size=10g
    --fallocate=none
    --direct=1
    --runtime=60
    --time_based
    --ramp_time=5
    --name=latency

Replace the parameters `rw` (read/write/randread/randwrite) and `bs` (block size) to fit your workload. Larger block sizes result in higher latency, where reads are faster than writes. The results can be found in the `lat` row.

### Measure IOPS

IOPS are a direct result of the latency and concurrency. Use one of the following tabs based on your client type to measure IOPS:

### Linux
    
    
    fio --directory=/netapp \
    --ioengine=libaio \
    --rw=randread \
    --bs=4k \
    --iodepth=32 \
    --size=10g \
    --fallocate=none \
    --direct=1 \
    --runtime=60 \
    --time_based \
    --ramp_time=5 \
    --name=iops

### Windows
    
    
    fio --directory=Z\:\
    --ioengine=windowsaio
    --thread
    --rw=randread
    --bs=4k
    --iodepth=32
    --size=10g
    --fallocate=none
    --direct=1
    --runtime=60
    --time_based
    --ramp_time=5
    --numjobs=16
    --name=iops

Replace the parameters `rw` (read/write/randread/randwrite), `bs` (blocksize), and `iodepth` (concurrency) to fit your workload. The results can be found in the `iops` row.

### Measure throughput

Throughput is IOPS multiplied by blocksize. Use one of the following tabs based on your client type to measure throughput:

### Linux
    
    
    fio --directory=/netapp \
    --ioengine=libaio \
    --rw=read \
    --bs=64k \
    --iodepth=32 \
    --size=10g \
    --fallocate=none \
    --direct=1 \
    --runtime=60 \
    --time_based \
    --ramp_time=5 \
    --numjobs=16 \
    --name=throughput

### Windows
    
    
    fio --directory=Z\:\
    --ioengine=windowsaio
    --thread
    --rw=read
    --bs=64k
    --iodepth=32
    --size=10g
    --fallocate=none
    --direct=1
    --runtime=60
    --time_based
    --ramp_time=5
    --numjobs=16
    --name=throughput

Replace the parameters `rw` (read/write/randread/randwrite), `bs` (blocksize), and `iodepth` (concurrency) to fit your workload. You can only achieve high throughput using block sizes 64k or larger and high concurrency.

## What's next

Review [performance benchmarks](https://docs.cloud.google.com/netapp/volumes/docs/performance/performance-benchmarks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
