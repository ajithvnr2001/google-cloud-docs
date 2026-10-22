---
url: https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks/
title: Duplicate a disk with clones \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:34.352494+00:00
---

# Duplicate a disk with clones  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Duplicate a disk with clones Stay organized with collections  Save and categorize content based on your preferences. 

Disk cloning lets you create an instantly usable copy of an existing disk in the same location (zone or region) as the source disk. Create a disk clone in scenarios where you want a copy of an existing disk that you can quickly attach to an instance, such as the following:

  * Creating staging environments by duplicating production data to debug without disturbing production
  * Performing non-disruptive malware scans of a disk without impacting the performance of a production workload
  * Creating copies for database backup verification
  * Moving non-boot disk data to a new project
  * Duplicating disks while scaling out your VMs



This document provides information about how disk clones work and how to create a disk clone.

To enable disaster recovery for your data, back up your disk with [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) instead of using disk clones. To capture disk contents at regular intervals without creating new disks, use [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) because they're more storage-efficient than clones. For additional disk protection options, see [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).

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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Summary of use cases

In addition to duplicating a disk for quick testing and debugging, you can enable [high availability for a zonal disk](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) by creating a regional clone from the zonal disk. When you create a regional disk from a zonal disk, the regional disk has a replica of the disk in two zones within the same region. After you create the regional disk, you then use the new regional disk instead of the zonal disk. In the rare event of an outage in one zone, you can still access the data from the replica in the other zone.

This table summarizes the different types of clones that Compute Engine supports.

Cloning type | When to use | Supported disk types  
---|---|---  
**Zonal clone from a zonal disk** |  Create an identical copy of a disk in the same zone for any of the following tasks: 

  * Scaling out workloads by duplicating existing disks for new VMs.
  * Staging, debugging, or test environments with production data.
  * Scanning a disk that's in production for malware.
  * Moving a disk to a new project.

| 

  * **Persistent Disk** : Standard, Balanced, and SSD Persistent Disk
  * **Google Cloud Hyperdisk** : All Hyperdisk types, except Hyperdisk Balanced High Availability

  
**Regional clone of a zonal disk** | 

  * Making a zonal workload highly available by adding a replica of the data in another zone. 
  * Scanning a disk that's in production for malware.
  * Creating a regional boot disk from a zonal boot disk.

| 

  * **Persistent Disk** : Standard, Balanced, and SSD Persistent Disk
  * **Hyperdisk** : Hyperdisk Extreme and Hyperdisk Balanced

  
**Regional clone of a regional disk** |  Create an identical copy of a regional disk in the same region for: 

  * Testing or scaling out regional, highly available (HA) workloads.
  * Maintaining data redundancy across two zones while performing administrative tasks or testing.
  * Creating copies of HA database volumes for verification.

| 

  * **Persistent Disk** : Regional Balanced, SSD, and Standard Persistent Disk
  * **Hyperdisk** : Hyperdisk Balanced High Availability

  
  
## How disk cloning works

When you clone a disk, you create a new disk that contains all the data on the source disk. You can create a disk clone even if the existing disk is attached to a VM instance. After you clone a disk, you can delete the source disk without any risk of deleting the clone.

By default, a disk's clones inherit its size, performance limits, type, and the exact zone or region. You can change some of these properties, as follows:

  * **Size** : you can create a clone that has a larger size than its source disk, but not a smaller size.

  * **Performance** : for Hyperdisk volumes, you can specify a different performance limit for the clone. Regional clones of zonal Hyperdisk volumes are Hyperdisk Balanced High Availability volumes and might have different performance limits.

  * **Location** : by default, a disk's clone is created in the same zone for zonal disks and the same region for regional disks. However, to create a regional clone of a zonal disk, you can specify a second zone that's within the same region of the zonal disk. The new clone is also referred to as a _regional clone_ and has one replica each in the zone of the source disk and the second zone that you specified.

  * **Type** : Regional clones of a zonal Hyperdisk Balanced or Hyperdisk Extreme volumes are Hyperdisk Balanced High Availability volumes.




### Cloning latency for data disks

Compute Engine typically clones developer-scale data (non-boot) disks up to 32 GiB in under ten seconds. For enterprise-scale data disks, benchmarked at 1 TiB, clones typically complete in under one minute.

Cloned disks don't require pre-warming, can be attached to instances and achieve full performance immediately after creation, eliminating initialization delays and significantly accelerating high-scale workflows like security scanning and dev-test environment setups.

### Regional Hyperdisk volumes cloned from zonal Hyperdisk volumes

A regional clone of an existing zonal Hyperdisk volume is always a new Hyperdisk Balanced High Availability volume. This is because Hyperdisk Balanced High Availability is the only supported regional Hyperdisk.

The way you create a regional Hyperdisk from a zonal Hyperdisk depends on its type.

  * You can create a regional disk by cloning the source disk if the source disk is a Hyperdisk Balanced or Hyperdisk Extreme volume.

  * You can't create a regional disk by cloning the source disk if the source disk is a Hyperdisk ML or Hyperdisk Throughput volume. You must [create a new Hyperdisk Balanced High Availability volume from a snapshot of the zonal disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha). 




#### Performance of Hyperdisk Balanced High Availability volumes cloned from zonal disks

When you create a new Hyperdisk Balanced High Availability volume from a Hyperdisk Balanced or Hyperdisk Extreme volume, the new disk inherits the size of the source disk, but you can specify a different size.

The new disk's maximum provisioned performance might be less than those of the source disk, because Hyperdisk Extreme and Hyperdisk Balanced have higher performance limits than Hyperdisk Balanced High Availability, as listed in the following table.

Hyperdisk type | Max I/O operations per second (IOPS) | Max throughput ( MiB/s)  
---|---|---  
Hyperdisk Balanced High Availability | 100,000 | 2,400  
Hyperdisk Balanced | 160,000 | 2,400  
Hyperdisk Extreme |  350,000 | 5,000  
  
You can specify limits for the new regional disk but the limits can't exceed the maximum performance limits offered by Hyperdisk Balanced High Availability—100,000 IOPS and 2,400 MiB/s.

If you don't specify a performance limit for the new disk, then Compute Engine provisions the disk with the default IOPS and throughput that depends on the Hyperdisk Balanced High Availability volume's size. For the default limits, see [Default size and performance limits of Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#default-perf).

To reach 100,000 IOPS, a Hyperdisk Balanced High Availability volume's size must be at least 200 GiB, so you might also need to increase the provisioned size of the regional clone.

#### Example

Consider a 150 GiB Hyperdisk Extreme volume, `hdx-1`, provisioned with 180,000 IOPS.

If you create a regional clone of `hdx-1` and you don't specify a new size or performance limit, then the new regional disk is a 150 GiB Hyperdisk Balanced High Availability volume that has the default IOPS limit for that size: 3,900 IOPS.

The maximum IOPS you can specify for a 150 GiB Hyperdisk Balanced High Availability volume is 75,000 IOPS, based on the formulas described in [Limits for configurable IOPS for Hyperdisk Balanced High Availability volumes](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#provisioned-iops-limits).

Therefore, if you don't increase the size of the new regional disk, then you can specify up to 75,000 IOPS for the new regional disk.

### Regional Persistent Disk volumes cloned from zonal Persistent Disk volumes

A regional Persistent Disk volume that was cloned from a zonal Persistent Disk has the same type as the clone. For example, if you clone a zonal Standard Persistent Disk, you create a regional Standard Persistent Disk volume.

However, regional clones of Persistent Disk volumes might have different size and performance limits than the zonal source disk, as follows.

  * **Lower performance limits** : Regional clones of Persistent Disk might have lower IOPS and throughput performance limit than the source disk. This is because zonal Persistent Disk offers higher maximum instance performance limits. For example, zonal Balanced Persistent Disk has a maximum instance limit of 80,000 write IOPS, but regional Balanced Persistent Disk has a limit of 60,000 write IOPS.

For detailed performance limits, compare the [performance limits for zonal Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/performance#zonal_pd) and the [performance limits for regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/performance#regional_pd).

  * **For regional Standard Persistent Disk, a 200 GiB minimum size** : regional Standard Persistent Disk has a minimum size of 200 GiB. So to create a regional clone of a 10 to 199 GiB zonal Standard Persistent Disk volume, you must specify a size of at least 200 GiB for the regional disk.




## Supported disk types

You can clone all Persistent Disk and Hyperdisk types if the clone is in the same location (zone or region) as the source disk.

Cloning a zonal disk to a regional disk is supported only for the following disk types:

  * **Hyperdisk** :

    * Hyperdisk Balanced
    * Hyperdisk Extreme To create a regional disk from a Hyperdisk ML or Hyperdisk Throughput volume, follow the steps in [Change a zonal disk to a Hyperdisk Balanced High Availability volume](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha).
  * **Persistent Disk** :

    * Balanced Persistent Disk
    * SSD Persistent Disk
    * Standard Persistent Disk

Extreme Persistent Disk volumes are zonal only and don't support regional disks.




## Restrictions

The following restrictions and limitations apply to disk clones.

### General limitations

The following limitations apply to all disk cloning operations.

  * You can't clone a disk that's in a Hyperdisk pool.
  * The size of the clone must be at least the size of the source disk. If you create a clone using the Google Cloud console, then you can't specify a disk size and the clone will be the same size as the source disk.
  * You can't create a zonal disk clone of an existing zonal disk in a different zone.
  * You can't delete the source disk while its clone is being created.
  * The compute instance that the source disk is attached to won't be able to power on while the clone is being created.
  * If the source disk was marked to be deleted along with the instance that it is attached to, then you can't delete the instance while the clone is being created.
  * If you clone a Hyperdisk or Persistent Disk volume from the Google Cloud console, then you can't specify the provisioned performance for the cloned disk.
  * If you use a [customer-supplied encryption key (CSEK)](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations/csek-deprecation-in-compute-engine)) or a [customer-managed encryption key](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption) (CMEK) to encrypt the source disk, then you must use the same key to encrypt the clone.

For more information, see Creating a clone of an encrypted source disk.

  * You can't create a zonal disk by cloning a regional disk.

  * To create a regional disk clone from a zonal source disk, one of the [replica zones](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create#--replica-zones) of the regional disk clone must match the zone of the source disk.

  * After creation, a regional disk clone is usable within three minutes, on average. However, the disk might take tens of minutes to become fully replicated and reach a state where the [recovery point objective (RPO)](https://wikipedia.org/wiki/Recovery_point_objective) is near zero.

  * Creating a regional disk from a zonal boot disk that was created from an image is slower than cloning zonal data disks or zonal boot disks created from snapshots. The duration for the process is comparable to that of taking a snapshot of the source disk and then creating a regional disk from that snapshot.

  * For zonal disks that were either created from an image or by cloning a disk that was created from an image, creating a regional clone of such a disk can take longer if you are creating standard snapshots of other disks at the same time.

  * You can't create a regional disk by cloning the source disk if the source disk is a Hyperdisk ML or Hyperdisk Throughput volume. You must [create a new Hyperdisk Balanced High Availability volume from a snapshot of the zonal disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha). 




### Rate limits for cloning disks

The following limits apply to how frequently you can clone disks.

  * For regional clones of a zonal boot disk, if the zonal disk was created from an image or by cloning a disk that was created from an image, then the following limitations apply:

    * You can create at most six regional clones of the source disk within a 60-minute window, after which operations are limited to one regional clone of the source disk every ten minutes.
    * The limit of six regional clones in 60 minutes is shared with snapshots of the source disk. This means that the maximum number of regional clones and snapshots of the same zonal disk that you can create within 60 minutes is six. If you create five standard snapshots of the source disk in 60 minutes, then you can create one regional clone or one more snapshot of the same disk within the same 60-minute period.
  * For clones of other regional or zonal disks, the following limitations apply:

    * You can create one clone of a given source disk or its clones every 30 seconds.
    * You can have at most 1,000 simultaneous disk clones of a given source disk or its clones. Exceeding this limit returns an [`internalError`](https://docs.cloud.google.com/resource-manager/docs/core_errors#INTERNAL_SERVER_ERROR). However, if you create a disk clone and delete it later, then the deleted disk clone is not included in this limit.
    * After a disk is cloned, any subsequent clones of that disk or of its clones are counted against the limit of 1,000 simultaneous disk clones for the original source disk and are counted against the limit of creating at most one clone every 30 seconds.
  * If you create a regional disk by cloning a zonal disk, then you can clone at most 1 TiB of capacity every 15 minutes, with a burst request limit of 257 TiB.




### Error messages

If you exceed the cloning frequency limits, the request fails with the following error:
    
    
    RATE LIMIT: ERROR: (gcloud.compute.disks.create) Could not fetch resource:
     - Operation rate exceeded for resource RESOURCE. Too frequent operations from the source resource.
    

**Note:** Error messages are subject to change, and Google recommends that you rely on error message codes instead of error message texts for building automation.

## Create disk clones

This section explains how you can duplicate an existing disk and create a disk clone.

For detailed steps, depending on the type of disk clone creation, see one of the following sections in this document:

  * To clone a disk for quick testing, debugging, or scaling out, Create a disk clone in the same location as the source
  * To make a zonal disk highly available, Create a regional disk clone from a zonal disk
  * Create a clone of an encrypted source disk



#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.disks.create` on the project
  * `compute.disks.useReadOnly` on the source disk



### Create a disk clone in the same location as the source

This section describes how to create a clone of an existing disk that's in the same zone, for zonal disks, or the same region, for regional disks, as the source disk. You can use the Google Cloud console, the Google Cloud CLI, REST, or Cloud Client Libraries.

To create a regional disk by cloning a zonal disk, see Create a regional disk clone from a zonal disk.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the list of disks, navigate to the disk that you want to clone.

  3. In the **Actions** column, click the more_vert menu button and select **Clone disk**.

![Create clone.](https://docs.cloud.google.com/static/compute/images/disk_clone.png)

In the **Clone disk** panel that appears, do the following:

     1. In the **Name** field, specify a name for the cloned disk.
     2. Optional: For zonal disks, under **Location** , verify that **Single zone** is selected.
     3. Under **Properties** , review other details for the cloned disk.
     4. To finish creating the cloned disk, click **Create**.



###  Google Cloud CLI 

To clone a zonal source disk and create a new zonal disk, run the [`disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) and specify the `--source-disk` flag:
    
    
    gcloud compute disks create TARGET_DISK_NAME \
        --description="cloned disk" \
        --source-disk=projects/PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME
    

Replace the following:

  * `TARGET_DISK_NAME`: the name for the new disk.
  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `ZONE`: the zone of the source and new disk.
  * `SOURCE_DISK_NAME`: the name of the source disk.



###  Terraform 

To create a disk clone, use the [`google_compute_disk` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk).
    
    
    resource "google_compute_disk" "default" {
      name  = "disk-name1"
      type  = "pd-ssd"
      zone  = "us-central1-a"
      image = "debian-13-trixie-v20260908"
      labels = {
        environment = "dev"
      }
      physical_block_size_bytes = 4096
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createDiskFromDisk creates a new disk with the contents of
    // an already existitng disk. Type, and size and zone may differ.
    func createDiskFromDisk(
    	w io.Writer,
    	projectID, zone, diskName, diskType, sourceDiskLink string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "zones/us-west3-b/diskTypes/pd-ssd"
    	// sourceDiskLink := "projects/your_project_id/global/disks/disk_name"
    	// diskSizeGb := 120
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.InsertDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		DiskResource: &computepb.Disk{
    			Name:       proto.String(diskName),
    			Zone:       proto.String(zone),
    			Type:       proto.String(diskType),
    			SourceDisk: proto.String(sourceDiskLink),
    			SizeGb:     proto.Int64(diskSizeGb),
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateFromSource {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
    
        // Name of the zone in which you want to create the disk.
        String zone = "europe-central2-b";
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        // For example: "zones/us-west3-b/diskTypes/pd-ssd"
        String diskType = String.format("zones/%s/diskTypes/pd-ssd", zone);
    
        // Size of the new disk in gigabytes.
        int diskSizeGb = 10;
    
        // A link to the disk you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/zones/{zone}/disks/{disk_name}"
        String diskLink = String.format("projects/%s/zones/%s/disks/%s", "PROJECT_NAME", "ZONE",
            "DISK_NAME");
    
        createDiskFromDisk(project, zone, diskName, diskType, diskSizeGb, diskLink);
      }
    
      // Creates a disk in a project in a given zone.
      public static void createDiskFromDisk(String project, String zone, String diskName,
          String diskType, int diskSizeGb, String diskLink)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          // Create the disk.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setZone(zone)
              .setSizeGb(diskSizeGb)
              .setSourceDisk(diskLink)
              .setType(diskType)
              .setName(diskName)
              .build();
    
          // Wait for the insert instance operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = disksClient.insertAsync(project, zone, disk)
              .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
          System.out.println(
              "Disk created from source. Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_disk_from_disk(
        project_id: str,
        zone: str,
        disk_name: str,
        disk_type: str,
        disk_size_gb: int,
        disk_link: str,
    ) -> compute_v1.Disk:
        """
        Creates a disk in a project in a given zone.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone in which you want to create the disk.
            disk_name: name of the disk you want to create.
            disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            disk_link: a link to the disk you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/zones/{zone}/disks/{disk_name}"
    
        Returns:
            An attachable disk.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.zone = zone
        disk.size_gb = disk_size_gb
        disk.source_disk = disk_link
        disk.type_ = disk_type
        disk.name = disk_name
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(project=project_id, zone=zone, disk_resource=disk)
    
        wait_for_extended_operation(operation, "disk creation")
    
        return disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=project_id, zone=zone, disk=disk_name)
    
    

###  REST 

To clone a zonal source disk and create a new zonal disk, make a `POST` request to the [`compute.disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert). In the request body, specify the `name` and `sourceDisk` parameters. The disk clone inherits all omitted properties from the source disk.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    
    {
      "name": "TARGET_DISK_NAME"
      "sourceDisk": "projects/PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME"
    }
    

Replace the following:

  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `ZONE`: the zone of the source and new disk.
  * `TARGET_DISK_NAME`: the name for the new disk.
  * `SOURCE_DISK_NAME`: the name of the source disk



### Create a regional disk clone from a zonal disk

**Preview — Creating a regional clone of a zonal boot disk**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can create a new regional disk by cloning an existing zonal boot or data disk of any of the following types:

  * Hyperdisk Balanced
  * Hyperdisk Extreme
  * Standard, Balanced, and SSD Persistent Disk



You can't create a regional disk by cloning the source disk if the source disk is a Hyperdisk ML or Hyperdisk Throughput volume. You must [create a new Hyperdisk Balanced High Availability volume from a snapshot of the zonal disk](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk#migrate-to-hdbha). 

**Note:** Creating a regional clone of a zonal boot disk is in [Preview](https://cloud.google.com/products/#product-launch-stages) and might be slower than cloning zonal data disks or zonal boot disks that were created from snapshots.

If the source disk is a Hyperdisk Balanced or Hyperdisk Extreme volume, then the regional disk is always a Hyperdisk Balanced High Availability volume and doesn't inherit the provisioned performance of the zonal disk. If you don't specify a size, or if you clone the disk with the Google Cloud console, then Compute Engine creates the new disk with the default performance limits for its size.

To set the size, and for Hyperdisk Balanced High Availability disks, the provisioned performance of the regional disk, you must clone the disk with the Google Cloud CLI or REST; you can't use the Google Cloud console.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the list of disks, navigate to the zonal Persistent Disk volume that you want to clone.

  3. In the **Actions** column, click the more_vert menu button and select **Clone disk**.

![Create clone.](https://docs.cloud.google.com/static/compute/images/disk_clone.png)

In the **Clone disk** panel that appears, do the following:

     1. In the **Name** field, specify a name for the cloned disk.
     2. For **Location** , select **Regional** and then select the secondary replica zone for the new regional cloned disk.
     3. Under **Properties** , review other details for the cloned disk.
     4. To finish creating the cloned disk, click **Create**.



###  gcloud 

To create a regional disk clone from a zonal disk, run the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) and specify the `--region` and `--replica-zones` parameters.

If the zonal disk is a Hyperdisk Balanced or Hyperdisk Extreme volume, specify the `--type=hyperdisk-balanced-high-availability` flag since the regional disk must be a Hyperdisk Balanced High Availability volume. If you specify provisioned performance, you must also specify the disk size, even if it's the same size as the source disk.

To clone a Persistent Disk volume, omit the `--type` flag.
    
    
    gcloud compute disks create TARGET_DISK_NAME \
      --description="zonal to regional cloned disk" \
      --region=CLONED_REGION \
      --source-disk=SOURCE_DISK_NAME \
      --source-disk-zone=SOURCE_DISK_ZONE \
      --replica-zones=SOURCE_DISK_ZONE,REPLICA_ZONE_2 \
      --project=PROJECT_ID \
      --type=hyperdisk-balanced-high-availability  \
      --size=DISK_SIZE \
      --provisioned-iops=IOPS_LIMIT  \
      --provisioned-throughput=THROUGHPUT_LIMIT
    

Replace the following:

  * `TARGET_DISK_NAME`: the name for the new regional disk clone.
  * `CLONED_REGION`: the region of the source and cloned disks.
  * `SOURCE_DISK_NAME`: the name of the zonal disk to clone.
  * `SOURCE_DISK_ZONE`: the zone for the source disk. This will also be the first replica zone for the regional disk clone.
  * `REPLICA_ZONE_2`: the second replica zone for the new regional disk clone.
  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `DISK_SIZE`: Optional: The size of the new regional disk, in GB. The size must be at least the same size as the source disk. If you specify an IOPS or throughput limit, then you must use this flag to specify the disk size, even if it is the same as the source disk.
  * `IOPS_LIMIT`: Optional: To create a regional Hyperdisk Balanced High Availability disk, you can specify a number of IOPS that the disk can achieve, up to 100,000 IOPS. If you include this flag, then you must also specify the disk size with the `--size` flag.
  * `THROUGHPUT_LIMIT`: Optional: To create a regional Hyperdisk Balanced High Availability disk, you can specify the maximum throughput in MiB/s, that the disk can achieve, up to 2,400 MiB/s. If you include this flag, then you must also specify the disk size with the `--size` flag.



###  Terraform 

To create a regional disk clone from a zonal disk use the following resource. If the source disk is a Hyperdisk Balanced or Hyperdisk Extreme volume, set the `type` argument to `hyperdisk-balanced-high-availability`.

  * [`google_compute_region_disk`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk)


    
    
    resource "google_compute_region_disk" "regiondisk" {
      name                      = "region-disk-name"
      snapshot                  = google_compute_snapshot.snapdisk.id
      type                      = "pd-ssd"
      region                    = "us-central1"
      physical_block_size_bytes = 4096
      size                      = 11
    
      replica_zones = ["us-central1-a", "us-central1-f"]
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createRegionalDiskFromDisk creates a new regional disk with the contents of
    // an already existitng zonal disk. Disk type and size may differ.
    func createRegionalDiskFromDisk(
    	w io.Writer,
    	projectID, region string, replicaZones []string,
    	diskName, diskType, sourceDiskLink string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// region := "us-west3" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "regions/us-west3/diskTypes/pd-ssd"
    	// sourceDiskLink := "projects/your_project_id/global/disks/disk_name"
    	// diskSizeGb := 120
    
    	// Exactly two replica zones must be specified
    	replicaZoneURLs := []string{
    		fmt.Sprintf("projects/%s/zones/%s", projectID, replicaZones[0]),
    		fmt.Sprintf("projects/%s/zones/%s", projectID, replicaZones[1]),
    	}
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.InsertRegionDiskRequest{
    		Project: projectID,
    		Region:  region,
    		DiskResource: &computepb.Disk{
    			Name:         proto.String(diskName),
    			Region:       proto.String(region),
    			Type:         proto.String(diskType),
    			SourceDisk:   proto.String(sourceDiskLink),
    			SizeGb:       proto.Int64(diskSizeGb),
    			ReplicaZones: replicaZoneURLs,
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Optional;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class RegionalCreateFromSource {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
    
        // Name of the zone in which you want to create the disk.
        String region = "europe-central2";
    
        // An iterable collection of zone names in which you want to keep
        // the new disks' replicas. One of the replica zones of the clone must match
        // the zone of the source disk.
        List<String> replicaZones = new ArrayList<>();
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        // For example: "zones/us-west3-b/diskTypes/pd-ssd"
        String diskType = String.format("zones/%s/diskTypes/pd-ssd", "ZONE_NAME");
    
        // Size of the new disk in gigabytes.
        int diskSizeGb = 10;
    
        // A link to the disk you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/zones/{zone}/disks/{disk_name}"
        String diskLink = String.format("projects/%s/zones/%s/disks/%s", "PROJECT_NAME", "ZONE",
            "DISK_NAME");
    
        // A link to the snapshot you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/global/snapshots/{snapshot_name}"
        String snapshotLink = String.format("projects/%s/global/snapshots/%s", "PROJECT_NAME",
            "SNAPSHOT_NAME");
    
        createRegionalDisk(project, region, replicaZones, diskName, diskType, diskSizeGb,
            Optional.ofNullable(diskLink), Optional.ofNullable(snapshotLink));
      }
    
      // Creates a regional disk from an existing zonal disk in a given project.
      public static void createRegionalDisk(
          String project, String region, List<String> replicaZones, String diskName, String diskType,
          int diskSizeGb, Optional<String> diskLink, Optional<String> snapshotLink)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `regionDisksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) regionDisksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create()) {
    
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).Builder diskBuilder = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .addAllReplicaZones(replicaZones)
              .setName(diskName)
              .setType(diskType)
              .setSizeGb(diskSizeGb)
              .setRegion(region);
    
          // Set source disk if diskLink is not empty.
          diskLink.ifPresent(diskBuilder::setSourceDisk);
    
          // Set source snapshot if the snapshot link is not empty.
          snapshotLink.ifPresent(diskBuilder::setSourceSnapshot);
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = regionDisksClient.insertAsync(project, region, diskBuilder.build())
              .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
          System.out.println(
              "Regional disk created. Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    from collections.abc import Iterable
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_regional_disk(
        project_id: str,
        region: str,
        replica_zones: Iterable[str],
        disk_name: str,
        disk_type: str,
        disk_size_gb: int,
        disk_link: str | None = None,
        snapshot_link: str | None = None,
    ) -> compute_v1.Disk:
        """
        Creates a regional disk from an existing zonal disk in a given project.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            region: name of the region in which you want to create the disk.
            replica_zones: an iterable collection of zone names in which you want to keep
                the new disks' replicas. One of the replica zones of the clone must match
                the zone of the source disk.
            disk_name: name of the disk you want to create.
            disk_type: the type of disk you want to create. This value uses the following format:
                "regions/{region}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "regions/us-west3/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            disk_link: a link to the disk you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/zones/{zone}/disks/{disk_name}"
            snapshot_link: a link to the snapshot you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/global/snapshots/{snapshot_name}"
    
        Returns:
            An attachable regional disk.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.replica_zones = replica_zones
        disk.size_gb = disk_size_gb
        if disk_link:
            disk.source_disk = disk_link
        if snapshot_link:
            disk.source_snapshot = snapshot_link
        disk.type_ = disk_type
        disk.region = region
        disk.name = disk_name
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_insert)(
            project=project_id, region=region, disk_resource=disk
        )
    
        wait_for_extended_operation(operation, "disk creation")
    
        return disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_get)(project=project_id, region=region, disk=disk_name)
    
    

###  REST 

To create a regional disk clone from a zonal disk, make a `POST` request to the [`compute.disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) and specify the `sourceDisk` and `replicaZone` parameters.

If the zonal disk is a Hyperdisk Balanced or Hyperdisk Extreme volume, include the `type` field to create a Hyperdisk Balanced High Availability volume. If you specify provisioned performance, you must also specify the disk size, even if it's the same size as the source disk.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/CLONED_REGION/disks
    
    {
      "name": "TARGET_DISK_NAME",
      "sourceDisk": "projects/PROJECT_ID/zones/SOURCE_DISK_ZONE/disks/SOURCE_DISK_NAME",
      "replicaZone": "SOURCE_DISK_ZONE,REPLICA_ZONE_2",
      "type": "projects/PROJECT_ID/regions/CLONED_REGION/diskTypes/hyperdisk-balanced-high-availability",
      "sizeGb": "DISK_SIZE",
      "provisionedIops": "IOPS_LIMIT",
      "provisionedThroughput": "THROUGHPUT_LIMIT"
    }
    

Replace the following:

  * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `TARGET_DISK_NAME`: the name for the new regional disk clone.
  * `CLONED_REGION`: the region of the source and cloned disks.
  * `SOURCE_DISK_NAME`: the name of the zonal disk to clone.
  * `SOURCE_DISK_ZONE`: the zone for the source disk. This will also be the first replica zone for the regional disk clone.
  * `REPLICA_ZONE_2`: the second replica zone for the new regional disk clone.
  * `DISK_SIZE`: Optional: The size of the new regional disk, in GB. The size must be at least the same size as the source disk. If you specify an IOPS or throughput limit, then you must include this field to specify the disk size, even if it is the same as the source disk.
  * `IOPS_LIMIT`: Optional: To create a regional Hyperdisk Balanced High Availability disk, you can specify a number of IOPS that the disk can handle, up to 100,000 IOPS. If you include this field, then you must also specify the disk size with the `size` field.
  * `THROUGHPUT_LIMIT`: Optional: To create a regional Hyperdisk Balanced High Availability disk, you can specify the maximum throughput in MiB/s, that the disk can provide, up to 2,400 MiB/s. If you include this field, then you must also specify the disk size with the `size` field.



## Create a disk clone of a CMEK- or CSEK- encrypted source disk

To create a zonal or regional clone of a disk that is encrypted with CSEK or CMEK, follow the procedures described in the preceding sections. However, you must also provide the key used to encrypt the source disk.

### Create disk clones for CSEK-encrypted disks

If you use a CSEK to encrypt your source disk, you must also use the same key to encrypt the clone.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the list of zonal persistent disks, find the disk that you want to clone.

  3. In the **Actions** column, click the more_vert menu button and select **Clone disk**.

![Create clone.](https://docs.cloud.google.com/static/compute/images/disk_clone.png)

In the **Clone disk** panel that appears, do the following:

     1. In the **Name** field, specify a name for the cloned disk.
     2. In the **Decryption and encryption** field, provide the source disk encryption key.
     3. Under **Properties** , review other details for the cloned disk.
     4. To finish creating the cloned disk, click **Create**.



###  gcloud 

To create a disk clone for a CSEK-encrypted source disk, run the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) and provide the source disk encryption key using the `--csek-key-file` flag. If you are using an RSA-wrapped key, use the [`gcloud beta compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/create).
    
    
    gcloud compute disks create TARGET_DISK_NAME \
      --description="cloned disk" \
      --source-disk=projects/PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME \
      --csek-key-file example-key-file.json
    

Replace the following:

  * `TARGET_DISK_NAME`: the name for the new disk.
  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `ZONE`: the zone of the source and new disk.
  * `SOURCE_DISK_NAME`: the name of the source disk



###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // Creates a zonal non-boot persistent disk in a project with the copy of data from an existing disk.
    // The encryption key must be the same for the source disk and the new disk.
    // The disk type and size may differ.
    func createDiskFromCustomerEncryptedDisk(
    	w io.Writer,
    	projectID, zone, diskName, diskType string,
    	diskSizeGb int64,
    	diskLink, encryptionKey string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "zones/us-west3/diskTypes/pd-ssd"
    	// diskSizeGb := 120
    	// diskLink := "projects/your_project_id/global/disks/disk_name"
    	// encryptionKey := "SGVsbG8gZnJvbSBHb29nbGUgQ2xvdWQgUGxhdGZvcm0=" // in base64
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.InsertDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		DiskResource: &computepb.Disk{
    			Name:       proto.String(diskName),
    			Zone:       proto.String(zone),
    			Type:       proto.String(diskType),
    			SizeGb:     proto.Int64(diskSizeGb),
    			SourceDisk: proto.String(diskLink),
    			DiskEncryptionKey: &computepb.CustomerEncryptionKey{
    				RawKey: &encryptionKey,
    			},
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html);
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CloneEncryptedDisk {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
    
        // Name of the zone in which you want to create the disk.
        String zone = "europe-central2-b";
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        // For example: "zones/us-west3-b/diskTypes/pd-ssd"
        String diskType = String.format("zones/%s/diskTypes/pd-ssd", zone);
    
        // Size of the new disk in gigabytes.
        int diskSizeGb = 10;
    
        // A link to the disk you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/zones/{zone}/disks/{disk_name}"
        String diskLink = String.format("projects/%s/zones/%s/disks/%s", "PROJECT_NAME", "ZONE",
            "DISK_NAME");
    
        // Customer-supplied encryption key used for encrypting data in the source disk.
        // The data will be encrypted with the same key in the new disk.
        byte[] encryptionKey = null;
    
        createDiskFromCustomerEncryptedKey(project, zone, diskName, diskType, diskSizeGb, diskLink,
            encryptionKey);
      }
    
      // Creates a zonal non-boot persistent disk in a project with the copy of data
      // from an existing disk.
      // The encryption key must be the same for the source disk and the new disk.
      public static void createDiskFromCustomerEncryptedKey(String project, String zone,
          String diskName, String diskType, int diskSizeGb, String diskLink, byte[] encryptionKey)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          // Create a disk and set the encryption key.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setZone(zone)
              .setName(diskName)
              .setType(diskType)
              .setSizeGb(diskSizeGb)
              .setSourceDisk(diskLink)
              .setDiskEncryptionKey([CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html)
                  .newBuilder()
                  .[setRawKeyBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.Builder.html#com_google_cloud_compute_v1_CustomerEncryptionKey_Builder_setRawKeyBytes_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(encryptionKey))
                  .build())
              .build();
    
          // Wait for the insert disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = disksClient.insertAsync(
              [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html).newBuilder()
                  .setProject(project)
                  .setZone(zone)
                  .setDiskResource(disk)
                  .build()).get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
          System.out.println(
              "Disk cloned with customer encryption key. Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_disk_from_customer_encrypted_disk(
        project_id: str,
        zone: str,
        disk_name: str,
        disk_type: str,
        disk_size_gb: int,
        disk_link: str,
        encryption_key: bytes,
    ) -> compute_v1.Disk:
        """
        Creates a zonal non-boot persistent disk in a project with the copy of data from an existing disk.
    
        The encryption key must be the same for the source disk and the new disk.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone in which you want to create the disk.
            disk_name: name of the disk you want to create.
            disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            disk_link: a link to the disk you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/zones/{zone}/disks/{disk_name}"
            encryption_key: customer-supplied encryption key used for encrypting
                data in the source disk. The data will be encrypted with the same key
                in the new disk.
    
        Returns:
            An attachable copy of an existing disk.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.zone = zone
        disk.size_gb = disk_size_gb
        disk.source_disk = disk_link
        disk.type_ = disk_type
        disk.name = disk_name
        disk.disk_encryption_key = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKey.html)()
        disk.disk_encryption_key.raw_key = encryption_key
        operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(project=project_id, zone=zone, disk_resource=disk)
    
        wait_for_extended_operation(operation, "disk creation")
    
        return disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=project_id, zone=zone, disk=disk_name)
    
    

###  REST 

To create a disk clone for a CSEK-encrypted source disk, make a `POST` request to the [`compute.disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) and provide the source disk encryption key using the `diskEncryptionKey` property. If you are using an RSA-wrapped key, use [the `beta` version of the method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/disks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    
    {
      "name": "TARGET_DISK_NAME"
      "sourceDisk": "projects/PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME"
      "diskEncryptionKey": {
        "rsaEncryptedKey": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA=="
      },
    }
    

Replace the following:

  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `ZONE`: the zone of the source and new disk.
  * `TARGET_DISK_NAME`: the name for the new disk.
  * `SOURCE_DISK_NAME`: the name of the source disk



### Create disk clones for CMEK-encrypted disks

If you use a CMEK to encrypt your source disk, you must also use the same key to encrypt the clone.

###  Console 

Compute Engine automatically encrypts the clone using the source disk encryption key.

###  gcloud 

To create a disk clone for a CMEK-encrypted source disk, run the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) and provide the source disk encryption key using the `--kms-key` flag. If you are using an RSA-wrapped key, use the [`gcloud beta compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disks/create).
    
    
    gcloud compute disks create TARGET_DISK_NAME \
      --description="cloned disk" \
      --source-disk=projects/PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME \
      --kms-key projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY
    

Replace the following:

  * `TARGET_DISK_NAME`: the name for the new disk.
  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `ZONE`: the zone of the source and new disk.
  * `SOURCE_DISK_NAME`: the name of the source disk.
  * `KMS_PROJECT_ID`: the project ID for the encryption key.
  * `REGION`: the region of the encryption key.
  * `KEY_RING`: the [key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings) of the encryption key.
  * `KEY`: the name of the encryption key.



###  Go 

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // Creates a zonal non-boot persistent disk in a project with the copy of data from an existing disk.
    // The encryption key must be the same for the source disk and the new disk.
    // The disk type and size may differ.
    func createDiskFromKmsEncryptedDisk(
    	w io.Writer,
    	projectID, zone, diskName, diskType string,
    	diskSizeGb int64,
    	diskLink, kmsKeyLink string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "zones/us-west3/diskTypes/pd-ssd"
    	// diskSizeGb := 120
    	// diskLink := "projects/your_project_id/global/disks/disk_name"
    	// kmsKeyLink := "projects/your_kms_project_id/locations/us-central1/keyRings/your_key_ring/cryptoKeys/your_key"
    
    	ctx := context.Background()
    	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.InsertDiskRequest{
    		Project: projectID,
    		Zone:    zone,
    		DiskResource: &computepb.Disk{
    			Name:       proto.String(diskName),
    			Zone:       proto.String(zone),
    			Type:       proto.String(diskType),
    			SizeGb:     proto.Int64(diskSizeGb),
    			SourceDisk: proto.String(diskLink),
    			DiskEncryptionKey: &computepb.CustomerEncryptionKey{
    				KmsKeyName: &kmsKeyLink,
    			},
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk created\n")
    
    	return nil
    }
    

###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html);
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CloneEncryptedDiskManagedKey {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
    
        // Name of the zone in which you want to create the disk.
        String zone = "europe-central2-b";
    
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
    
        // The type of disk you want to create. This value uses the following format:
        // "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
        // For example: "zones/us-west3-b/diskTypes/pd-ssd"
        String diskType = String.format("zones/%s/diskTypes/pd-ssd", zone);
    
        // Size of the new disk in gigabytes.
        int diskSizeGb = 10;
    
        // A link to the disk you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/zones/{zone}/disks/{disk_name}"
        String diskLink = String.format("projects/%s/zones/%s/disks/%s", "PROJECT_NAME", "ZONE",
            "DISK_NAME");
    
        // URL of the key from KMS. The key might be from another project, as
        // long as you have access to it. The data will be encrypted with the same key
        // in the new disk. This value uses following format:
        // "projects/{kms_project_id}/locations/{region}/keyRings/{key_ring}/cryptoKeys/{key}"
        String kmsKeyName = "kms-key-name";
    
        createDiskFromKmsEncryptedDisk(project, zone, diskName, diskType, diskSizeGb, diskLink,
            kmsKeyName);
      }
    
      // Creates a zonal non-boot disk in a project with the copy of data from an existing disk.
      // The encryption key must be the same for the source disk and the new disk.
      public static void createDiskFromKmsEncryptedDisk(String project, String zone, String diskName,
          String diskType, int diskSizeGb, String diskLink, String kmsKeyName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          // Create a disk and set the KMS encryption key name.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setZone(zone)
              .setName(diskName)
              .setType(diskType)
              .setSizeGb(diskSizeGb)
              .setSourceDisk(diskLink)
              .setDiskEncryptionKey([CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html).newBuilder()
                  .setKmsKeyName(kmsKeyName)
                  .build())
              .build();
    
          // Wait for the insert disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = disksClient.insertAsync(
              [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html).newBuilder()
                  .setProject(project)
                  .setZone(zone)
                  .setDiskResource(disk)
                  .build()).get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
          System.out.println(
              "Disk cloned with KMS encryption key. Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.exceptions import BadRequest
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_extended_operation(
        operation: ExtendedOperation, verbose_name: str = "operation", timeout: int = 300
    ) -> Any:
        """
        Waits for the extended (long-running) operation to complete.
    
        If the operation is successful, it will return its result.
        If the operation ends with an error, an exception will be raised.
        If there were any warnings during the execution of the operation
        they will be printed to sys.stderr.
    
        Args:
            operation: a long-running operation you want to wait on.
            verbose_name: (optional) a more verbose name of the operation,
                used only during error and warning reporting.
            timeout: how long (in seconds) to wait for operation to finish.
                If None, wait indefinitely.
    
        Returns:
            Whatever the operation.result() returns.
    
        Raises:
            This method will raise the exception received from `operation.exception()`
            or RuntimeError if there is no exception set, but there is an `error_code`
            set for the `operation`.
    
            In case of an operation taking longer than `timeout` seconds to complete,
            a `concurrent.futures.TimeoutError` will be raised.
        """
        result = operation.result(timeout=timeout)
    
        if operation.error_code:
            print(
                f"Error during {verbose_name}: [Code: {operation.error_code}]: {operation.error_message}",
                file=sys.stderr,
                flush=True,
            )
            print(f"Operation ID: {operation.name}", file=sys.stderr, flush=True)
            raise operation.exception() or RuntimeError(operation.error_message)
    
        if operation.warnings:
            print(f"Warnings during {verbose_name}:\n", file=sys.stderr, flush=True)
            for warning in operation.warnings:
                print(f" - {warning.code}: {warning.message}", file=sys.stderr, flush=True)
    
        return result
    
    
    def create_disk_from_kms_encrypted_disk(
        project_id: str,
        zone: str,
        disk_name: str,
        disk_type: str,
        disk_size_gb: int,
        disk_link: str,
        kms_key_name: str,
    ) -> compute_v1.Disk:
        """
        Creates a zonal non-boot disk in a project with the copy of data from an existing disk.
    
        The encryption key must be the same for the source disk and the new disk.
    
        To run this method, the service-<project_id>@compute-system.iam.gserviceaccount.com
        service account needs to have the cloudkms.cryptoKeyEncrypterDecrypter role,
        as described in documentation:
        https://cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone in which you want to create the disk.
            disk_name: name of the disk you want to create.
            disk_type: the type of disk you want to create. This value uses the following format:
                "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                For example: "zones/us-west3-b/diskTypes/pd-ssd"
            disk_size_gb: size of the new disk in gigabytes
            disk_link: a link to the disk you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/zones/{zone}/disks/{disk_name}"
            kms_key_name: URL of the key from KMS. The key might be from another project, as
                long as you have access to it. The data will be encrypted with the same key
                in the new disk. This value uses following format:
                "projects/{kms_project_id}/locations/{region}/keyRings/{key_ring}/cryptoKeys/{key}"
    
        Returns:
            An attachable copy of an existing disk.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.zone = zone
        disk.size_gb = disk_size_gb
        disk.source_disk = disk_link
        disk.type_ = disk_type
        disk.name = disk_name
        disk.disk_encryption_key = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKey.html)()
        disk.disk_encryption_key.kms_key_name = kms_key_name
        try:
            operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(
                project=project_id, zone=zone, disk_resource=disk
            )
        except BadRequest as err:
            if "Permission 'cloudkms.cryptoKeyVersions.useToEncrypt' denied" in err.message:
                print(
                    f"Please provide the cloudkms.cryptoKeyEncrypterDecrypter role to"
                    f"service-{project_id}@compute-system.iam.gserviceaccount.com"
                )
            raise err
    
        wait_for_extended_operation(operation, "disk creation")
    
        return disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=project_id, zone=zone, disk=disk_name)
    
    

###  REST 

To create a disk clone for a CMEK-encrypted source disk, make a `POST` request to the [`compute.disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert) and provide the source disk encryption key using the `kmsKeyName` property. If you are using an RSA-wrapped key, use [the `beta` version of the method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/disks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks
    
    {
      "name": "TARGET_DISK_NAME"
      "sourceDisk": "projects/PROJECT_ID/zones/ZONE/disks/SOURCE_DISK_NAME"
      "diskEncryptionKey": {
        "kmsKeyName": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY"
      },
    }
    

Replace the following:

  * `PROJECT_ID`: the [ID of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) where you want to clone the disk.
  * `ZONE`: the zone of the source and new disk.
  * `TARGET_DISK_NAME`: the name for the new disk.
  * `SOURCE_DISK_NAME`: the name of the source disk.
  * `KMS_PROJECT_ID`: the project ID for the encryption key.
  * `REGION`: the region of the encryption key.
  * `KEY_RING`: the [key ring](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_rings) of the encryption key.
  * `KEY`: the name of the encryption key.



## What's next

  * Learn how to regularly [backup your disks using standard snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) to prevent unintended data loss.
  * Learn how to [backup your disks in place using instant snapshots](https://docs.cloud.google.com/compute/docs/disks/create-instant-snapshots).
  * Learn about using [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) for synchronous replication between two zones.
  * Learn about [Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
