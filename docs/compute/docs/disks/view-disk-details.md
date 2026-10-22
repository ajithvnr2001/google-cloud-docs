---
url: https://docs.cloud.google.com/compute/docs/disks/view-disk-details/
title: View disk details \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:36.408671+00:00
---

# View disk details  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/view-disk-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View disk details Stay organized with collections  Save and categorize content based on your preferences. 

After you create a Persistent Disk or Hyperdisk in Compute Engine, you can review information about the disk's configuration. You can use this information to monitor disk performance, enhance data security, and optimize your storage and costs. This document explains how to view the following essential disk details:

  * A list of all disks available in a project, including disks that aren't attached to an instance
  * Attached instances
  * Whether a disk will be automatically deleted with its instance
  * Access mode
  * Throughput and input/output operations per second (IOPS) performance metrics
  * Encryption information



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




## View all disks in a project

For a comprehensive view of your storage resources, you can list all of the disks within a project, including disks that aren't attached to an instance.

###  Console 

In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

The **Disks** page lists all of the disks in your project.

###  gcloud 

Run the [`disks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list).
    
    
    gcloud compute disks list
    

**Command output**

A list of all Persistent Disk and Hyperdisk volumes in your project.

To view disks in a specific region or zone, use the `--zone` or `--region` flag to specify the location.

###  REST 

Make a `POST` request to the [`compute.disks.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/aggregatedList).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/disks/
    

Replace the following:

  * `PROJECT_ID`: your project ID.



**Request response**

A list of all Persistent Disk and Hyperdisk volumes in your project.

## View the instances that a disk is attached to

Understand how your disk is being used, and prevent incurring costs from unused disks, by identifying which instances are attached to it.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the **Name** column, click the name of the disk.

  3. In the **Properties** table, the row labeled **In use by** lists all instances that are attached to the disk.




###  gcloud 

Run the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe).
    
    
    gcloud compute disks describe DISK_NAME \
        --zone=ZONE
        --format="json(users)"
    

Replace the following:

  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk.



**Command output**

If the output is `null`, the disk isn't attached to any instances. Otherwise, the output is a JSON object that contains a field named `users`. The `users` field lists the URLs of all instances that use the disk.

###  REST 

Make a `POST` request to the [`compute.disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get).
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk.



**Request response**

The REST response is a JSON object that contains a field named `users`.

If the value for the `users` field is `null`, the disk isn't attached to any instances. Otherwise, the users object lists the URLs of all instances that use the disk.

## View if a disk has autodelete enabled

To prevent accidental data loss, check if your boot or non-boot disk will be deleted when you delete the attached instance.

By default, boot disks have `autoDelete` enabled, meaning that deleting an instance also deletes its attached boot disk. However, you can override this setting if you want to preserve the attached boot disk. Non-boot disks will also be deleted if they have `autoDelete` enabled.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the instance.

  3. In the **Storage** section, navigate to the **When deleting instance** column. **When deleting instance** can be one of the following values:

     * Delete disk: the disk will be deleted with the instance.
     * Keep disk: the disk won't be deleted with the instance.



###  gcloud 

Run the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe).
    
    
    gcloud compute disks describe DISK_NAME \
        --zone=ZONE
    

Replace the following:

  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk.



**Command output**

A JSON object that contains a field named `autoDelete`. `autoDelete` describes if the disk will be deleted with its attached instance, and can be one of the following values:

  * `true`: the disk will be deleted with the instance.
  * `false`: the disk won't be deleted with the instance.



###  REST 

Make a `POST` request to the [`compute.disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get).
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk.



**Request response**

A JSON object that contains a field named `autoDelete`. `autodelete` describes if the disk will be deleted with its attached instance, and can be one of the following values:

  * `true`: the disk will be deleted with the instance.
  * `false`: the disk won't be deleted with the instance.



To change this setting, see [Modify a disk's auto-delete setting](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete).

## View how much space is left on a disk

To view how much space is left on a disk without connecting to the attached instance, you need to install the [Ops Agent](https://docs.cloud.google.com/monitoring/api/metrics_opsagent) on your instances. Ops Agent provides additional metrics for [`bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-disk) (disk bytes used) and [`percent_used`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-disk) (disk utilization).

To learn more about monitoring disk space, see [Ops Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent).

## View a Hyperdisk's access mode

Access mode determines if a Hyperdisk volume can be attached to multiple instances and if the attached instances have read-only or read-write access to the disk.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the **Name** column, click the name of the disk.

  3. In the **Properties** table, the row labeled **Access mode** describes how instances can access the data on the disk, and can be one of the following values:

     * Single VM read-write (default), for read-write access from one instance.
     * Multiple VMs read-write, for read-write access from multiple instances.
     * Multiple VMs read-only, for read-only access from multiple instances.



###  gcloud 

Run the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe).
    
    
    gcloud compute disks describe DISK_NAME \
        --zone=ZONE \
        --format="json(accessMode)"
    

Replace the following:

  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk.



**Command output**

A JSON object that contains a field named `accessMode`. `accessMode` describes how instances can access the data on the disk, and can be one of the following values:

  * `READ_ONLY_MANY`, for read-only access from multiple instances.
  * `READ_WRITE_MANY`, for read-write access from multiple instances.
  * `READ_WRITE_SINGLE`, for read-write access from one instance.



###  REST 

Make a `POST` request to the [`compute.disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get).
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk



**Request response**

The REST response is a JSON object that contains a field named `accessMode`. `accessMode` describes how instances can access the data on the disk, and can be one of the following values:

  * `READ_ONLY_MANY`, for read-only access from multiple instances.
  * `READ_WRITE_MANY`, for read-write access from multiple instances.
  * `READ_WRITE_SINGLE`, for read-write access from one instance.



## Determine if a disk is performing as expected

Disks have limits for the maximum IOPS and throughput that they can perform at. These limits depend on the disk size and connected instance. A disk's maximum performance can't exceed the [limits of the instance](https://docs.cloud.google.com/compute/docs/disks/performance#machine-type-disk-limits) that it's attached to.

To determine if a Hyperdisk or Persistent Disk volume is performing at the expected level based on its size and attached instance, complete the following steps:

  1. Check the disk's provisioned or maximum performance.
  2. Compare the provisioned or maximum performance with the disk's actual performance.



The steps to check for a disk's provisioned or maximum performance depend on if the disk is a Hyperdisk or Persistent Disk.

### View a Hyperdisk's provisioned performance

To view the provisioned IOPS and throughput values for a Hyperdisk volume, see [View the provisioned performance settings for Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk#view_provisioned).

### View a Persistent Disk's maximum performance

Persistent Disk volumes have throughput and IOPS limits per GiB and per instance that they can sustain. The following sections provide detailed information on the performance limits for zonal and regional Persistent Disk:

  * IOPS and throughput limits for [zonal Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/performance#zonal_pd)
  * IOPS and throughput limits for [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/performance#regional_pd)



Balanced Persistent Disk and SSD (performance) Persistent Disk also offer [baseline performance](https://docs.cloud.google.com/compute/docs/disks/performance#baseline_performance) for sustained IOPS and throughput. To calculate the maximum IOPS and throughput values for a Balanced Persistent Disk or SSD Persistent Disk volume, use the following equation:

`Maximum expected performance = Baseline performance + (Per GiB performance limit * Combined disk size in GiB)`

For more information, see [Baseline performance](https://docs.cloud.google.com/compute/docs/disks/performance#baseline_performance).

### View a disk's actual performance

To view a disk's IOPS and throughput performance, use the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM that the disk is attached to.

  3. Click **Observability**.

  4. In the menu, select **Disk** > **Performance**

Graphs appear that illustrate the disk's IOPS and Throughput performance. To view all graphs, you must install [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent).




To view a more detailed report on a disk's performance, see [Review disk performance metrics](https://docs.cloud.google.com/compute/docs/disks/review-disk-metrics).

If the disk isn't performing as expected, review the guidance in [Monitor a disk's health](https://docs.cloud.google.com/compute/docs/disks/disk-health).

## View information about a disk's encryption

**Caution:** Customer-supplied encryption keys (CSEK) for Compute Engine are [deprecated](https://docs.cloud.google.com/compute/docs/deprecations). For more information and instructions on alternatives, see [CSEK deprecation in Compute Engine](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine). 

Disks in Compute Engine are encrypted with one of the following types of encryption keys:

  * Google-owned and managed keys
  * Customer-managed encryption keys (CMEKs)
  * Customer-supplied encryption keys (CSEKs)



By default, Compute Engine uses Google-owned and managed keys.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the **Name** column, click the name of the disk.

  3. In the **Properties** table, the row labeled **Encryption** indicates the type of encryption: _Google managed_ , _Customer-managed_ , or _Customer-supplied_.




###  gcloud 

Run the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe).
    
    
    gcloud compute disks describe DISK_NAME \
        --zone=ZONE \
        --format="json(diskEncryptionKey)"
    

Replace the following:

  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk.



**Command output**

If the output is `null`, the disk uses a Google-owned and managed key.

Otherwise, the output is a JSON object.

If the JSON object contains a field named `diskEncryptionKey`, the disk is encrypted. The `diskEncryptionKey` object contains information about whether the disk is CMEK- or CSEK-encrypted: 

  * If the `diskEncryptionKey.kmsKeyName` property is present, the disk is CMEK-encrypted. The `kmsKeyName` property indicates the name of the specific key used to encrypt the disk: 
        
        {
          "diskEncryptionKey": {
            "kmsKeyName": "projects/my-proj/.."
          }
        }
        

  * If the `diskEncryptionKey.sha256` property is present, the disk is CSEK-encrypted. The `sha256` property is the SHA-256 hash of the customer-supplied encryption key that protects the disk. 
        
        {
            "diskEncryptionKey": {
              "sha256": "abcdefghijk134560459345dssfd"
            }
          }
            




###  REST 

Make a `POST` request to the [`compute.disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get).
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk



**Request response**

If the response is `null`, the disk uses a Google-owned and managed key.

Otherwise, the response is a JSON object.

If the JSON object contains a field named `diskEncryptionKey`, the disk is encrypted. The `diskEncryptionKey` object contains information about whether the disk is CMEK- or CSEK-encrypted: 

  * If the `diskEncryptionKey.kmsKeyName` property is present, the disk is CMEK-encrypted. The `kmsKeyName` property indicates the name of the specific key used to encrypt the disk: 
        
        {
          "diskEncryptionKey": {
            "kmsKeyName": "projects/my-proj/.."
          }
        }
        

  * If the `diskEncryptionKey.sha256` property is present, the disk is CSEK-encrypted. The `sha256` property is the SHA-256 hash of the customer-supplied encryption key that protects the disk. 
        
        {
            "diskEncryptionKey": {
              "sha256": "abcdefghijk134560459345dssfd"
            }
          }
            




If the disk uses CMEKs, you can find detailed information about the key, its key ring, and location by following the steps in [View keys by project](https://docs.cloud.google.com/kms/docs/view-keys-by-project).

If the disk uses CSEKs, contact your organization's administrator for details about the key. By using a CMEK, you can also see what resources that key protects with key usage tracking. For more information, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

## View all of a disk's details

For general information about your disk, you can view all of a disk's properties at once.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the **Name** column, click the name of the disk.

The **Properties** table appears with a summary of basic disk information.

  3. To view additional disk information, click **EQUIVALENT REST**.

A dialog window appears with the original REST response from the Compute Engine API.




###  gcloud 

Run the [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe).
    
    
    gcloud compute disks describe DISK_NAME \
        --zone=ZONE
    

Replace the following:

  * `DISK_NAME`: the name of the disk.
  * `ZONE`: the zone where your disk is located.



**Command output**

All data associated with the Compute Engine disk.

###  REST 

Make a `POST` request to the [`compute.disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get).
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your disk is located.
  * `DISK_NAME`: the name of the disk



**Request response**

The REST response contains all data associated with the Compute Engine disk.

## What's next

  * [Modify the size and performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks)
  * [Modify a disk's settings](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
