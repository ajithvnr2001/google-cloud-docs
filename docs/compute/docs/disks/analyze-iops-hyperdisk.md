---
url: https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk/
title: Analyze the provisioned IOPS and throughput for Hyperdisk volumes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:59:19.827328+00:00
---

# Analyze the provisioned IOPS and throughput for Hyperdisk volumes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Analyze the provisioned IOPS and throughput for Hyperdisk volumes Stay organized with collections  Save and categorize content based on your preferences. 

You can view the disk description to see the provisioned input/output operations per second (IOPS) or the provisioned throughput for Google Cloud Hyperdisk volumes.

You can change the provisioned IOPS or throughput once every 6 hours for Hyperdisk ML or once every 4 hours for all other Hyperdisk types. Each change of the IOPS or throughput level is logged. You can review the log history and compare it with performance metrics to understand how the provisioned IOPS and throughput levels relate to the performance level observed by your workload.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## View the provisioned performance settings for Hyperdisk

To view the provisioned IOPS or throughput for your Hyperdisk volumes, view the disk information.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click the name of the disk to view the configuration details.


![A Hyperdisk Balanced disk's properties](https://docs.cloud.google.com/static/compute/images/disks/hdb-config-console-screenshot.png)Screenshot of the configured properties for a Hyperdisk

###  gcloud 

  * Use the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe) to view the disk details.
        
        gcloud compute disks describe DISK_NAME \
          --zone ZONE_NAME \
          --format="text(name, provisionedIops, provisionedThroughput, sizeGb)"
        

Replace the following:

    * `DISK_NAME`: the name of the Hyperdisk volume.
    * `ZONE_NAME`: the zone where the Hyperdisk volume was created.

The output shows the name of the disk, the current disk size and the provisioned IOPS or throughput, for example:
    
    name: my-hyperdisk-b
    provisionedIops: '8500'
    provisionedThroughput: '140'
    sizeGb: '150'
    




###  REST 

Construct a `GET` request to the [`compute.disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get). In the request body, specify the name of the Hyperdisk volume.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/get
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your Hyperdisk volume is located.
  * `DISK_NAME`: the name of the Hyperdisk volume to view.



In the response body, you can view the current disk size, provisioned IOPS, and throughput, for example:
    
    
    {
      ...
      "name": "my-hyperdisk-x",
      "physicalBlockSizeBytes": "4096",
      "provisionedIops": "100000",
      ...
      "sizeGb": "1000",
      "status": "READY",
      ...
    }
    

You can use a query filter to return only the information you want to view. To view only the fields shown in the preceding example output, append a query parameter similar to the following to your request.
    
    
    ?fields=name,physicalBlockSizeBytes,provisionedIops,provisionedThroughput,sizeGb,status
    

## View disk performance metrics

To view performance metrics for your VMs, use the Cloud Monitoring observability metrics available in the Google Cloud console.

  1. In the Google Cloud console, go to the **VM Instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. To view metrics for individual VMs:

     1. Click the name of the VM you want to view performance metrics for. The VM **Details** page opens.

     2. Click the **Observability** tab to open the Observability **Overview** page.

  3. Explore the VM's performance metrics. The following are key metrics related to disk performance for a VM:

     * On the **Overview** page:

       * **CPU Utilization.** The percent of CPU used by the VM.

       * **Network Traffic.** The average rate of bytes sent and received in one minute intervals.

       * **Disk Throughput.** The average rate of bytes written to and read from disks.

       * **Disk IOPS.** The average rate of I/O read and write operations to disks.

     * On the **Disks Performance** page, view the following charts:

       * **Operations (IOPS).** The average rate of I/O read and write operations to the disk in one-minute time periods.

       * **IOPS by Storage Type** The average rate of I/O operations to the disk in one-minute time periods, grouped by the storage type and device type.

       * **Throughput (MB/s)** The average rate of bytes written to and read from the VM's disks in one-minute time periods.

       * **Throughput by Storage Type** The average rate of bytes written to and read from the VM's disks in one-minute time periods, grouped by the storage type and device type.

       * **I/O Size Avg.** The average size of I/O read and write operations to disks. Small (4 to 16 KiB) random I/O operations are usually limited by IOPS and sequential or large (256 KiB-1 MiB) I/O operations are usually limited by throughput.

       * **Queue Length Avg.** The number of queued and running disk I/O operations, also called _queue depth_ , for the top 5 devices. To reach the performance limits of your Hyperdisk and Persistent Disk volumes, [use a high I/O queue depth](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#io-queue-depth).

       * **I/O Latency Avg.** The average latency of I/O read and write operations aggregated across operations of all block storage devices attached to the VM, measured by the Ops Agent in the VM. This value includes operating system and file system processing time.




## Analyze the IOPS needed for your workload

To determine the IOPS needed for your workload, make note of the peak and average IOPS and throughput rates during times of peak usage, and also during a normal workload cycle, to get an idea of your workload requirements.

Observe the IOPS requirements of your workload using any of the following methods:

  * Use the **Monitoring** tab on the disk details page in the Google Cloud console.
  * Use the **Observability page** for your VM, as described in View disk performance metrics.



Based on the observed metric values, determine if you should adjust the provisioned IOPS for your VM. For example:

  * If the peak IOPS rate is close to the provisioned IOPS for the Hyperdisk volume, then you can try increasing the provisioned IOPS for the Hyperdisk volume to boost the performance of your application.
  * If the peak IOPS rate is consistently lower than the provisioned IOPS, then you can lower the provisioned IOPS for the Hyperdisk volume to reduce the cost of the disk.



## Analyze the throughput needed for your workload

You can provision throughput separately from disk capacity for the following Hyperdisk types:

  * Hyperdisk Balanced
  * Hyperdisk Balanced High Availability
  * Hyperdisk Throughput
  * Hyperdisk ML



You can specify the target throughput level for a given volume. Individual volumes have full performance isolation - each volume gets the performance provisioned to it. However, the throughput is ultimately capped by per-VM limits for the VM to which your volumes are attached. To review these limits, see [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits).

Both read and write operations count against the throughput limit provisioned for a Hyperdisk volume. The provisioned throughput and the maximum limits apply to the combined total of read and write throughput.

Observe the throughput requirements of your workload using any of the following methods:

  * Use the **Monitoring** tab on the disk details page in the Google Cloud console.
  * Use the **Observability page** for your VM, as described in View disk performance metrics.



If the total throughput provisioned for one or more Hyperdisk volumes exceeds the total throughput available at the VM level, the performance is limited to the VM-level performance.

## What's next

  * Learn how to [optimize Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk).
  * Learn how to [modify the size and provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks)
  * Learn about [Hyperdisk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#section-2).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
