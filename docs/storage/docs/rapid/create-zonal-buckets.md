---
url: https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets/
title: Create zonal buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:29.769411+00:00
---

# Create zonal buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create zonal buckets Stay organized with collections  Save and categorize content based on your preferences. 

Zonal buckets, offered through [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket), provide high-performance, low-latency storage for applications that require data within a specific geographic zone.

This page describes how to do the following:

  * Create a bucket with a [zonal location](https://docs.cloud.google.com/storage/docs/locations#location-z).

  * Mount the zonal bucket to your local file system using [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview).

  * Transfer data between an existing bucket to the zonal bucket by using Storage Transfer Service.




## Create a bucket in a zone

#### Before you begin

If you haven't already, [get the required roles](https://docs.cloud.google.com/storage/docs/creating-buckets#required-roles) for creating buckets.

**Note:** For a list of available zones you can locate a bucket in, see [Cloud Storage zones](https://docs.cloud.google.com/storage/docs/locations#location-z).

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.
  3. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        * Enter a globally unique name that meets the [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

     2. In the **Choose where to store your data** section, do the following:

        1. Select **Zone** as the [Location type](https://docs.cloud.google.com/storage/docs/locations).

        2. Use the location type's drop-down menu to select a [**Location**](https://docs.cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be permanently stored.

     3. In the **Choose how to store your data** section, Rapid storage is selected as the [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes).

     4. In the **Choose how to control access to objects** section, do the following:

        1. Select whether your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention).

**Note:** If public access prevention is already enforced by your project's [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention), the **Prevent public access** checkbox is locked. 
        2. Select **Uniform** to enable uniform bucket-level access on the bucket.

        3. Optionally, configure [IP filtering for the bucket](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).

  4. In the **Choose how to protect object data** section, do the following:

     * To choose how to [encrypt](https://docs.cloud.google.com/storage/docs/encryption) your object data, click the expand_more expander arrow labeled **Data encryption** , and do the following:

       * In the **Default encryption key type** section, select the default encryption key for the bucket. If you select **Cloud KMS key** , then provide a [Cloud Key Management Service key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).
       * In the **Encryption enforcement rules** section, for **Key types** , select [which encryption types to allow or restrict](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket.


* Click **Create**.

### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command:
         
         gcloud storage buckets create \
         gs://BUCKET_NAME --location=BUCKET_LOCATION --placement=BUCKET_ZONE \
         --default-storage-class=RAPID --enable-hierarchical-namespace --uniform-bucket-level-access

**Note:** The `--enable-hierarchical-namespace` and `--uniform-bucket-level-access` flags must be specified in the command.

Replace:

     * `BUCKET_NAME` with the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `rapid-storage-bucket`.

     * `BUCKET_LOCATION` with a [bucket region](https://docs.cloud.google.com/storage/docs/locations). For example, `us-east1`.

     * `BUCKET_ZONE` with the zone you want to locate your bucket in. For example, `us-east1-b`.

If the request is successful, the command returns the following message:
    
    Creating gs://rapid-storage-bucket/...




## Mount the zonal bucket using Cloud Storage FUSE

#### Before you begin

This section assumes you already have access to Cloud Storage FUSE. If you haven't already, perform the following prerequisite steps:

  1. [Install Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/install). Make sure you install Cloud Storage FUSE version 3.4.0 or later.
  2. [Authenticate Cloud Storage FUSE requests](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#authenticate-requests).
  3. If you didn't create the bucket you want to mount, [get required roles](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/mount-bucket#required-roles-for-mounting) for mounting the bucket.



To mount a zonal bucket using Cloud Storage FUSE, use the following commands:
    
    
    mkdir MOUNT_POINT
    gcsfuse BUCKET_NAME MOUNT_POINT

Replace:

  * `MOUNT_POINT` with the local directory to mount the bucket to. For example, `$HOME/example-bucket`.

  * `BUCKET_NAME` with the name of the bucket to mount.




For example, the following commands mount a bucket named `example-rapid-storage-bucket` to the `source-bucket` mountpoint:
    
    
    mkdir $HOME/source-bucket
    gcsfuse example-rapid-storage-bucket $HOME/source-bucket

If you want to transfer objects from an existing bucket to a zonal bucket, mount both buckets and then use the `cp` command to transfer the objects.

## Benchmark performance with a FIO test

To benchmark the speed of a zonal bucket, run a [FIO test](https://fio.readthedocs.io/en/latest/index.html).

###  Google Kubernetes Engine 

The following command applies a configuration to your Google Kubernetes Engine cluster that runs a FIO test against a Cloud Storage bucket. The bucket is mounted to the container's file system using the [FUSE CSI driver for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver).
    
    
    $ cat << EOF | kubectl apply -f -
    apiVersion: v1
    kind: Pod
    metadata:
      name: fio
      namespace: default
      annotations:
        gke-gcsfuse/volumes: "true"
    spec:
      containers:
      - name: fio
        image: mayadata/fio
        command: ["/bin/ash", "-c", "--"]
        args:
        - |
          fio --name=read_latency_test --filename=/data/fio --filesize=1G --time_based=1 --ramp_time=10s --runtime=1m --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 --bs=4K --iodepth=1 --rw=randread --disable_slat=1 --disable_clat=1 --lat_percentiles=1 --numjobs=1
        volumeMounts:
        - name: fio-bucket
          mountPath: /data
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: topology.kubernetes.io/zone
                operator: In
                values:
                - ZONE_NAME
      serviceAccountName: default
      volumes:
      - name: fio-bucket
        csi:
          driver: gcsfuse.csi.storage.gke.io
          volumeAttributes:
            bucketName: "BUCKET_NAME"
            gcsfuseLoggingSeverity: warning
      restartPolicy: Never
    EOF
    

Where:

  * `ZONE_NAME` is the zone in which your bucket is located. For example, `us-east4-a`.

  * `BUCKET_NAME` is the name of your bucket. For example, `my-bucket`.




If the test is successful, it outputs a response similar to the following:
    
    
    $ kubectl logs fio
    Defaulted container "fio" out of: fio, gke-gcsfuse-sidecar (init)
    read_latency_test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
    fio-3.36
    Starting 1 process
    
    read_latency_test: (groupid=0, jobs=1): err= 0: pid=11: Mon Mar  3 20:38:14 2025
      read: IOPS=591, BW=2365KiB/s (2422kB/s)(139MiB/60001msec)
        lat (usec): min=867, max=181966, avg=1685.32, stdev=2695.84
        lat percentiles (usec):
        |  1.00th=[  1074],  5.00th=[  1188], 10.00th=[  1254], 20.00th=[  1336],
        | 30.00th=[  1401], 40.00th=[  1467], 50.00th=[  1549], 60.00th=[  1614],
        | 70.00th=[  1713], 80.00th=[  1844], 90.00th=[  2057], 95.00th=[  2278],
        | 99.00th=[  3064], 99.50th=[  3654], 99.90th=[  8717], 99.95th=[ 73925],
        | 99.99th=[131597]
      bw (  KiB/s): min= 1290, max= 2736, per=100.00%, avg=2365.51, stdev=244.10, samples=120
      iops        : min=  322, max=  684, avg=591.34, stdev=61.10, samples=120
      cpu          : usr=0.81%, sys=1.61%, ctx=36011, majf=0, minf=36
      IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
        submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
        complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
        issued rwts: total=35473,0,0,0 short=0,0,0,0 dropped=0,0,0,0
        latency   : target=0, window=0, percentile=100.00%, depth=1
    
    Run status group 0 (all jobs):
      READ: bw=2365KiB/s (2422kB/s), 2365KiB/s-2365KiB/s (2422kB/s-2422kB/s), io=139MiB (145MB), run=60001-60001msec
    

###  Compute Engine VM 

The following instructions run a FIO test on a Compute Engine VM.

  1. Mount a rapid storage using Cloud Storage FUSE:


    
    
    mkdir $HOME/rapid-mnt
    gcsfuse --max-retry-attempts=5 BUCKET_NAME PATH
    

Replace:

  * `BUCKET_NAME` with the name of the bucket.

  * `PATH` with the local file system path you want to mount the bucket to.



  1. If you haven't already, install FIO:


    
    
    sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install fio -y
    

  1. Run an example FIO read latency test:


    
    
    fio --name=read_latency_test \
      --filename=BUCKET_PATH/1G --filesize=1G \
      --time_based=1 --ramp_time=10s --runtime=1m \
      --ioengine=libaio --direct=1 --verify=0 --randrepeat=0 \
      --bs=4K --iodepth=1 --rw=randread --numjobs=1
    

Replace:

  * `BUCKET_PATH` with the path to the bucket you mounted.



If the test is successful, it outputs a response similar to the following:
    
    
    read_latency_test: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=1
    fio-3.33
    Starting 1 process
    Jobs: 1 (f=1): [f(1)][100.0%][eta 00m:00s]
    read_latency_test: (groupid=0, jobs=1): err= 0: pid=78399: Tue Feb 11 21:14:35 2025
      read: IOPS=622, BW=2490KiB/s (2550kB/s)(146MiB/60001msec)
        slat (usec): min=108, max=13857, avg=1596.92, stdev=243.32
        clat (nsec): min=1539, max=141717, avg=5872.92, stdev=3230.74
        lat (usec): min=112, max=13866, avg=1602.80, stdev=244.13
        clat percentiles (nsec):
        |  1.00th=[ 2960],  5.00th=[ 3856], 10.00th=[ 4320], 20.00th=[ 4704],
        | 30.00th=[ 4896], 40.00th=[ 5088], 50.00th=[ 5280], 60.00th=[ 5536],
        | 70.00th=[ 5856], 80.00th=[ 6240], 90.00th=[ 7072], 95.00th=[ 8512],
        | 99.00th=[21120], 99.50th=[26240], 99.90th=[40704], 99.95th=[51968],
        | 99.99th=[75264]
      bw (  KiB/s): min= 2024, max= 2672, per=100.00%, avg=2491.15, stdev=105.69, samples=120
      iops        : min=  506, max=  668, avg=622.77, stdev=26.41, samples=120
      lat (usec)   : 2=0.06%, 4=6.21%, 10=89.91%, 20=2.61%, 50=1.15%
      lat (usec)   : 100=0.05%, 250=0.01%
      cpu          : usr=0.67%, sys=1.79%, ctx=37361, majf=0, minf=37
      IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
        submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
        complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
        issued rwts: total=37355,0,0,0 short=0,0,0,0 dropped=0,0,0,0
        latency   : target=0, window=0, percentile=100.00%, depth=1
    
    Run status group 0 (all jobs):
      READ: bw=2490KiB/s (2550kB/s), 2490KiB/s-2490KiB/s (2550kB/s-2550kB/s), io=146MiB (153MB), run=60001-60001msec

## Transfer data with Storage Transfer Service

You can use [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/create-transfers) to transfer data between zonal buckets and other Cloud Storage buckets.

### Required permissions

Transfers between Cloud Storage buckets require the IAM roles listed in [Agentless transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud).

In addition, because zonal buckets use [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), the Storage Transfer Service service agent must be granted the following IAM permissions:

  * When the source is a zonal bucket:

    * No additional action is required when using the predefined roles listed in [Agentless transfer permissions](https://docs.cloud.google.com/storage-transfer/docs/iam-cloud). The necessary permission (`storage.folders.list`) is already included in the Storage Object Viewer (`roles/storage.objectViewer`) role.
  * When the destination is a zonal bucket:

    * You must grant the Storage Object User (`roles/storage.objectUser`) role to the service agent. This provides the required `storage.folders.create` permission.



For instructions on adding roles to the service agent, see:

  * [Configure access to a source: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/source-cloud-storage#grant_the_required_permissions)
  * [Configure access to a sink: Cloud Storage](https://docs.cloud.google.com/storage-transfer/docs/sink-cloud-storage#grant_the_required_permissions)



### Limitations

  * **Supported transfers:**

    * Transfers are supported between zonal buckets and buckets in any other Cloud Storage location, including other zonal buckets.
  * **Unsupported features:**

    * Event-driven transfers
    * Cross-bucket replication
    * Agent-based transfers
  * **Unfinalized objects:**

    * When transferring unfinalized objects from a zonal bucket, the data in the destination bucket might not reflect changes to the objects that are made while the transfer is in progress.
    * Unfinalized source objects are marked as finalized in the destination bucket.



### Create a transfer

To get started, see [Create a transfer with Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/create-transfers).

## What's next

  * [Upload objects to your zonal bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).

  * [Read and append to objects in your zonal bucket](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets).

  * [Download objects from your zonal bucket](https://docs.cloud.google.com/storage/docs/downloading-objects).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
