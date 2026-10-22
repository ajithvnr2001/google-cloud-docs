---
url: https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones/
title: Move a VM instance between zones or regions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:39.737956+00:00
---

# Move a VM instance between zones or regions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Move a VM instance between zones or regions Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to move a virtual machine (VM) instance between zones or regions.

## Before you begin

  * Read the [zones](https://docs.cloud.google.com/compute/docs/zones) documentation.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

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

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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




## Requirements

This section lists requirements for moving a VM between zones and regions:

  * **Project quota.** Your project must have enough quota to do the following:

    * Create new snapshots.
    * Promote any ephemeral external IP addresses.
    * Create new VMs and disks in your destination region.

For example, if you have three disks attached to the VM you want to move, you need enough quota to create three temporary persistent disk snapshots and three new disks. After you create your new disks, you can delete your temporary snapshots.

Check the **[Quotas](https://console.cloud.google.com/iam-admin/quotas)** page to ensure that you have enough quota for the preceding resources. For more information, see [Quotas and limits overview](https://docs.cloud.google.com/compute/quotas-limits).

  * **Persistent disks.** The persistent disks attached to the VM that you want to move are not attached to other VMs.

  * **Local SSDs.** Local SSDs are meant for temporary storage, and data on local SSDs is not preserved through manual VM terminations. If you need to preserve local SSD data, replicate it by using a [durable storage option](https://docs.cloud.google.com/compute/docs/disks) like persistent disks.

  * **GPUs.** If your VM includes GPUs, verify that the GPUs you want to use are available in the VM's destination zone. For a list of GPUs and the zones that they are available in, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

  * **Subnetwork.** If you want to move your VM between regions, such as between `us-west1-a` and `asia-south1-b`, and your VM belongs to a subnetwork, you must select a new subnetwork for your VM. For instructions on how to create subnets, see [Adding subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets).

**Note:** The method of moving a VM described in this section also works for VMs in a TERMINATED state, or [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) that use UEFI firmware.



## Limitation

If you move a VM across regions, you cannot preserve the VM's ephemeral internal or external IP address. You must choose a new IP address when you recreate the VM.

## Resource properties

To move your VM, you must shut down the VM, move it to the destination zone or region, and then restart it. After you move your VM, update any references that you have to the original resource, such as any target VMs or target pools that point to the earlier VM.

During the move, some server-generated properties of your VM and disks change.

### Properties that change for VMs

The following table describes properties that change for VMs:

Property name | Changes  
---|---  
Internal IP address | A new internal IP address is usually assigned, but the VM might keep the original internal IP address.  
External IP address |  If the VM is moving between zones in the _same region_ , the external IP address remains the same. Otherwise, pick a different external IP address for the VM instance.   
CPU platform | Depending on the available CPU platform in your destination zone, your VM might have a different CPU platform after it has been moved. For a full list of CPU platforms in each zone, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).   
Network/subnetwork | If your VM belongs to a subnetwork and you are moving a VM across regions, you must pick a new subnetwork for your VM. VMs moving across zones in the same region retain the same subnetwork.  
  
### Properties that change for disks

The following table describes properties that change for disks:

Property name | Changes  
---|---  
Source snapshot | The source snapshot of the new disk is set to the temporary snapshot that is created during the move.  
Source snapshot ID | The source snapshot ID is set to the temporary snapshot's ID.  
Source image | The source image field is empty.  
Image ID | The image ID is empty.  
Last detached timestamp | The last detached timestamp is empty.  
Last attached timestamp | The last attached timestamp changes to the timestamp when the new disk was attached to the new instance.  
  
### Properties changing for both VMs and disks

The following table describes properties that change for both VMs and disks:

Property name | Changes  
---|---  
ID | A new resource ID is generated.  
Creation timestamp | A new creation timestamp is generated.  
Zone resource URLs | All zone resource URLs change to reflect the destination zone. The following list shows the resource URLs that change: 

  * A VM's source disk URL
  * A VM's machine type URL
  * Self-link URLs
  * Zone URLs
  * Disk type URLs
  * Any URLs of VMs listed in a disk's [`users[]`](https://docs.cloud.google.com/compute/docs/reference/beta/disks#users) list

  
  
## Move a VM across zones or regions

To move a VM across zones or regions, you can do the following:

  1. [Create a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-machine-images) of your source VM.
  2. Create a VM from the machine image in a different zone or region.



The following examples show how to move a VM across zones.

###  gcloud 

In this example, you move a VM named `myinstance` that has two persistent disks named `mybootdisk` and `mydatadisk`, from `europe-west1-c` to `us-west1-b`.

  1. Identify the disks that are associated with the VM that you want to move:
         
         gcloud compute instances describe myinstance --format="list(name,status,disks)"
         

In this example, you find the following two associated disks for the `myinstance` VM:

     * A boot disk called `mybootdisk`
     * A data disk called `mydatadisk`
  2. Set the auto-delete state of `mybootdisk` and `mydatadisk` to `false` to ensure that the disks are not automatically deleted when the VM is deleted.
         
         gcloud compute instances set-disk-auto-delete myinstance --zone europe-west1-c \
             --disk mybootdisk --no-auto-delete

If the state was updated, `gcloud compute` returns the response `Updated [...]`. If the auto-delete state was already set to false, then `gcloud compute` returns:
         
         No change requested; skipping update for [myinstance].

  3. (Optional) Save your VM metadata.

When you delete your VM, the VM metadata is also removed. You can save that information in a separate file, then reapply the VM metadata to the new VM.

Describe your VM's metadata like so:
         
         gcloud compute instances describe myinstance --zone europe-west1-c

Save the contents to a separate file.

  4. Create backups of your data by using persistent disk snapshots.

As a precaution, create backups of your data while the persistent disks are still attached to the VM by using persistent disk snapshots. Before you take a snapshot, ensure that it is consistent with the state of the persistent disk by adhering to [snapshot best practices](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency).

**Note:** If you are running a Windows VM, the VM must be terminated before you can create a snapshot. Follow the steps to [create a snapshot for Windows VM](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

After you clear your disk buffers, create the snapshots:
         
         gcloud compute disks snapshot mybootdisk mydatadisk \
             --snapshot-names backup-mybootsnapshot,backup-mydatasnapshot \
             --zone europe-west1-c 

To verify that the snapshot is created, run `gcloud compute snapshots list`.

  5. (Optional) If you're moving a VM across zones within the same region, and you want to preserve its ephemeral internal or external IP address, promote the [internal](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#promote-in-use-internal-address) or [external](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#promote_ephemeral_ip) IP address to a static IP address, which you can reuse later.

**Note:** If you're moving your VM across regions, you cannot preserve an VM's ephemeral internal or external IP address . You must choose a new IP address when you recreate the VM.
  6. Delete your VM.

**Note:** If you already terminated your Windows VM in a previous step, skip this step.

Deleting your VM shuts it down cleanly and detach any persistent disks.
         
         gcloud compute instances delete myinstance --zone europe-west1-c

`gcloud` prompts you to confirm the deletion:
         
         The following VMs are deleted. Any attached disks configured to
         be auto-deleted are deleted unless they are attached to any other
         VMs or the `--keep-disks` flag is given and specifies them for keeping.
         Deleting a disk is irreversible and any data on the disk is lost.
         — [myinstance] in [europe-west1-c]
         
         
         Do you want to continue (Y/n)?

Because you turned off the auto-delete state for the disks earlier in this process, enter **Y** to continue and ignore the warning.

  7. Next, create another snapshot of both the boot disk and the data disk.
         
         gcloud compute disks snapshot mybootdisk mydatadisk \
             --snapshot-names mybootsnapshot,mydatasnapshot \
             --zone europe-west1-c 
         
         Created [.../mydatasnapshot].
         Created [.../mybootsnapshot].

  8. (Optional) Delete your persistent disks.

If you plan to reuse the names of the persistent disks for the new disks, you must delete the existing disks to release the names. Deleting your disks also saves on persistent disk storage costs.

If you do not plan to reuse the same disk names, you don't need to delete them.
         
         gcloud compute disks delete mybootdisk mydatadisk --zone europe-west1-c

  9. Create new persistent disks in `us-west1-b` from the snapshots you created. First create the boot disk.
         
         gcloud compute disks create mybootdiskb --source-snapshot mybootsnapshot \
             --zone us-west1-b
         
         Created [.../mybootdiskb].
         NAME        ZONE           SIZE_GB TYPE        STATUS
         mybootdiskb us-west1-b     100     pd-standard READY

Then create the data disk.
         
         gcloud compute disks create mydatadiskb --source-snapshot mydatasnapshot \
             --zone us-west1-b
         
         Created [.../mydatadiskb].
         NAME        ZONE           SIZE_GB TYPE        STATUS
         mydatadiskb us-west1-b 4000    pd-standard READY

  10. Recreate your VM in `us-west1-b`.

     * If you had opted to save your VM metadata in a file, for example `myinstance.describe`, you can use it to [set the same metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#updatinginstancemetadata) on your VM.

     * If your VM had a static external IP address, you can reassign that address to your new VM by specifying the `--address [ADDRESS]` option. If you are moving a VM across regions, you must pick a different external IP address for the new VM instance.

     * If your VM had a static internal IP address, you can reassign that address to your new VM by specifying the `--private-network-ip ADDRESS` option. If you are moving a VM across regions, you must pick a different internal IP address for the new VM instance.

     * If your VM included GPUs, add GPUs to the VM using the `--accelerator` option.

     * If the VM uses a specific subnet, add the `--subnet [SUBNET_NAME]` flag.

For a complete list of additional flags, see [gcloud compute instances create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    gcloud compute instances create myinstanceb --machine-type n1-standard-4 \
        --zone us-west1-b \
        --disk name=mybootdiskb,boot=yes,mode=rw \
        --disk name=mydatadiskb,mode=rw 
    
    Created [.../myinstanceb].
    NAME        ZONE           MACHINE_TYPE  INTERNAL_IP    EXTERNAL_IP     STATUS
    myinstanceb us-west1-b     n1-standard-4 10.240.173.229 146.148.112.106 RUNNING

  11. (Optional) Delete your persistent disk snapshots.

After you confirm that your virtual machines are moved, save on storage costs by deleting the temporary snapshots that you created.
         
         gcloud compute snapshots delete mybootsnapshot mydatasnapshot

If you no longer need your backup snapshots, delete those snapshots as well:
         
         gcloud compute snapshots delete backup-mybootsnapshot backup-mydatasnapshot




###  Go 

  1. Get the details of the VM and identify the disks that are attached to the VM.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         )
         
         // getInstance prints a name of a VM instance in the given zone in the specified project.
         func getInstance(w io.Writer, projectID, zone, instanceName string) error {
         	// projectID := "your_project_id"
         	// zone := "europe-central2-b"
         	// instanceName := "your_instance_name"
         
         	ctx := context.Background()
         	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewInstancesRESTClient: %w", err)
         	}
         	defer instancesClient.Close()
         
         	reqInstance := &computepb.GetInstanceRequest{
         		Project:  projectID,
         		Zone:     zone,
         		Instance: instanceName,
         	}
         
         	instance, err := instancesClient.Get(ctx, reqInstance)
         	if err != nil {
         		return fmt.Errorf("unable to get instance: %w", err)
         	}
         
         	fmt.Fprintf(w, "Instance: %s\n", instance.GetName())
         
         	return nil
         }
         

  2. Set the auto-delete state of the boot disk and data disk to `false` to ensure that the disks are not automatically deleted when the VM is deleted.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         )
         
         // setDiskAutodelete sets the autodelete flag of a disk to given value.
         func setDiskAutoDelete(
         	w io.Writer,
         	projectID, zone, instanceName, diskName string, autoDelete bool,
         ) error {
         	// projectID := "your_project_id"
         	// zone := "us-west3-b"
         	// instanceName := "your_instance_name"
         	// diskName := "your_disk_name"
         	// autoDelete := true
         
         	ctx := context.Background()
         	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewInstancesRESTClient: %w", err)
         	}
         	defer instancesClient.Close()
         
         	getInstanceReq := &computepb.GetInstanceRequest{
         		Project:  projectID,
         		Zone:     zone,
         		Instance: instanceName,
         	}
         
         	instance, err := instancesClient.Get(ctx, getInstanceReq)
         	if err != nil {
         		return fmt.Errorf("unable to get instance: %w", err)
         	}
         
         	diskExists := false
         
         	for _, disk := range instance.GetDisks() {
         		if disk.GetDeviceName() == diskName {
         			diskExists = true
         			break
         		}
         	}
         
         	if !diskExists {
         		return fmt.Errorf(
         			"instance %s doesn't have a disk named %s attached",
         			instanceName,
         			diskName,
         		)
         	}
         
         	req := &computepb.SetDiskAutoDeleteInstanceRequest{
         		Project:    projectID,
         		Zone:       zone,
         		Instance:   instanceName,
         		DeviceName: diskName,
         		AutoDelete: autoDelete,
         	}
         
         	op, err := instancesClient.SetDiskAutoDelete(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to set disk autodelete field: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "disk autoDelete field updated.\n")
         
         	return nil
         }
         

  3. Create backups of your data by using persistent disk snapshots.

As a precaution, create backups of your data while the persistent disks are still attached to the VM by using persistent disk snapshots. Before you take a snapshot, ensure that it is consistent with the state of the persistent disk by adhering to [snapshot best practices](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency).

**Note:** If you are running a Windows VM, the VM must be terminated before you can create a snapshot. Follow the steps to [create a snapshot for Windows VM](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

After you clear your disk buffers, create the snapshots:
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         	"google.golang.org/protobuf/proto"
         )
         
         // createSnapshot creates a snapshot of a disk.
         func createSnapshot(
         	w io.Writer,
         	projectID, diskName, snapshotName, zone, region, location, diskProjectID string,
         ) error {
         	// projectID := "your_project_id"
         	// diskName := "your_disk_name"
         	// snapshotName := "your_snapshot_name"
         	// zone := "europe-central2-b"
         	// region := "eupore-central2"
         	// location = "eupore-central2"
         	// diskProjectID = "YOUR_DISK_PROJECT_ID"
         
         	ctx := context.Background()
         
         	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
         	}
         	defer snapshotsClient.Close()
         
         	if zone == "" && region == "" {
         		return fmt.Errorf("you need to specify `zone` or `region` for this function to work")
         	}
         
         	if zone != "" && region != "" {
         		return fmt.Errorf("you can't set both `zone` and `region` parameters")
         	}
         
         	if diskProjectID == "" {
         		diskProjectID = projectID
         	}
         
         	disk := &computepb.Disk{}
         	locations := []string{}
         	if location != "" {
         		locations = append(locations, location)
         	}
         
         	if zone != "" {
         		disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
         		if err != nil {
         			return fmt.Errorf("NewDisksRESTClient: %w", err)
         		}
         		defer disksClient.Close()
         
         		getDiskReq := &computepb.GetDiskRequest{
         			Project: projectID,
         			Zone:    zone,
         			Disk:    diskName,
         		}
         
         		disk, err = disksClient.Get(ctx, getDiskReq)
         		if err != nil {
         			return fmt.Errorf("unable to get disk: %w", err)
         		}
         	} else {
         		regionDisksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
         		if err != nil {
         			return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
         		}
         		defer regionDisksClient.Close()
         
         		getDiskReq := &computepb.GetRegionDiskRequest{
         			Project: projectID,
         			Region:  region,
         			Disk:    diskName,
         		}
         
         		disk, err = regionDisksClient.Get(ctx, getDiskReq)
         		if err != nil {
         			return fmt.Errorf("unable to get disk: %w", err)
         		}
         	}
         
         	req := &computepb.InsertSnapshotRequest{
         		Project: projectID,
         		SnapshotResource: &computepb.Snapshot{
         			Name:             proto.String(snapshotName),
         			SourceDisk:       proto.String(disk.GetSelfLink()),
         			StorageLocations: locations,
         		},
         	}
         
         	op, err := snapshotsClient.Insert(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to create snapshot: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "Snapshot created\n")
         
         	return nil
         }
         

  4. Delete your VM from the source zone.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         )
         
         // deleteInstance sends a delete request to the Compute Engine API and waits for it to complete.
         func deleteInstance(w io.Writer, projectID, zone, instanceName string) error {
         	// projectID := "your_project_id"
         	// zone := "europe-central2-b"
         	// instanceName := "your_instance_name"
         	ctx := context.Background()
         	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewInstancesRESTClient: %w", err)
         	}
         	defer instancesClient.Close()
         
         	req := &computepb.DeleteInstanceRequest{
         		Project:  projectID,
         		Zone:     zone,
         		Instance: instanceName,
         	}
         
         	op, err := instancesClient.Delete(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to delete instance: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "Instance deleted\n")
         
         	return nil
         }
         

  5. Next, create another snapshot of both the boot disk and the data disks.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         	"google.golang.org/protobuf/proto"
         )
         
         // createSnapshot creates a snapshot of a disk.
         func createSnapshot(
         	w io.Writer,
         	projectID, diskName, snapshotName, zone, region, location, diskProjectID string,
         ) error {
         	// projectID := "your_project_id"
         	// diskName := "your_disk_name"
         	// snapshotName := "your_snapshot_name"
         	// zone := "europe-central2-b"
         	// region := "eupore-central2"
         	// location = "eupore-central2"
         	// diskProjectID = "YOUR_DISK_PROJECT_ID"
         
         	ctx := context.Background()
         
         	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
         	}
         	defer snapshotsClient.Close()
         
         	if zone == "" && region == "" {
         		return fmt.Errorf("you need to specify `zone` or `region` for this function to work")
         	}
         
         	if zone != "" && region != "" {
         		return fmt.Errorf("you can't set both `zone` and `region` parameters")
         	}
         
         	if diskProjectID == "" {
         		diskProjectID = projectID
         	}
         
         	disk := &computepb.Disk{}
         	locations := []string{}
         	if location != "" {
         		locations = append(locations, location)
         	}
         
         	if zone != "" {
         		disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
         		if err != nil {
         			return fmt.Errorf("NewDisksRESTClient: %w", err)
         		}
         		defer disksClient.Close()
         
         		getDiskReq := &computepb.GetDiskRequest{
         			Project: projectID,
         			Zone:    zone,
         			Disk:    diskName,
         		}
         
         		disk, err = disksClient.Get(ctx, getDiskReq)
         		if err != nil {
         			return fmt.Errorf("unable to get disk: %w", err)
         		}
         	} else {
         		regionDisksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
         		if err != nil {
         			return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
         		}
         		defer regionDisksClient.Close()
         
         		getDiskReq := &computepb.GetRegionDiskRequest{
         			Project: projectID,
         			Region:  region,
         			Disk:    diskName,
         		}
         
         		disk, err = regionDisksClient.Get(ctx, getDiskReq)
         		if err != nil {
         			return fmt.Errorf("unable to get disk: %w", err)
         		}
         	}
         
         	req := &computepb.InsertSnapshotRequest{
         		Project: projectID,
         		SnapshotResource: &computepb.Snapshot{
         			Name:             proto.String(snapshotName),
         			SourceDisk:       proto.String(disk.GetSelfLink()),
         			StorageLocations: locations,
         		},
         	}
         
         	op, err := snapshotsClient.Insert(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to create snapshot: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "Snapshot created\n")
         
         	return nil
         }
         

  6. (Optional) Delete your persistent disks.

If you plan to reuse the names of the persistent disks for the new disks, you must delete the existing disks to release the names. Deleting your disks also saves on persistent disk storage costs.

If you do not plan to reuse the same disk names, you don't need to delete them.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         )
         
         // deleteDisk deletes a disk from a project.
         func deleteDisk(w io.Writer, projectID, zone, diskName string) error {
         	// projectID := "your_project_id"
         	// zone := "us-west3-b"
         	// diskName := "your_disk_name"
         
         	ctx := context.Background()
         	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewDisksRESTClient: %w", err)
         	}
         	defer disksClient.Close()
         
         	req := &computepb.DeleteDiskRequest{
         		Project: projectID,
         		Zone:    zone,
         		Disk:    diskName,
         	}
         
         	op, err := disksClient.Delete(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to delete disk: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "Disk deleted\n")
         
         	return nil
         }
         

  7. Create new persistent disks in the destination zone from the snapshots you created. First create the boot disk, and then the data disks.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         	"google.golang.org/protobuf/proto"
         )
         
         // createDiskFromSnapshot creates a new disk in a project in given zone.
         func createDiskFromSnapshot(
         	w io.Writer,
         	projectID, zone, diskName, diskType, snapshotLink string,
         	diskSizeGb int64,
         ) error {
         	// projectID := "your_project_id"
         	// zone := "us-west3-b" // should match diskType below
         	// diskName := "your_disk_name"
         	// diskType := "zones/us-west3-b/diskTypes/pd-ssd"
         	// snapshotLink := "projects/your_project_id/global/snapshots/snapshot_name"
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
         			Name:           proto.String(diskName),
         			Zone:           proto.String(zone),
         			Type:           proto.String(diskType),
         			SourceSnapshot: proto.String(snapshotLink),
         			SizeGb:         proto.Int64(diskSizeGb),
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
         

  8. Recreate your VM with the new disks in the destination zone.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         	"google.golang.org/protobuf/proto"
         )
         
         // createWithExistingDisks create a new VM instance using selected disks.
         // The first disk in diskNames will be used as boot disk.
         func createWithExistingDisks(
         	w io.Writer,
         	projectID, zone, instanceName string,
         	diskNames []string,
         ) error {
         	// projectID := "your_project_id"
         	// zone := "europe-central2-b"
         	// instanceName := "your_instance_name"
         	// diskNames := []string{"boot_disk", "disk1", "disk2"}
         
         	ctx := context.Background()
         	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewInstancesRESTClient: %w", err)
         	}
         	defer instancesClient.Close()
         
         	disksClient, err := compute.[NewDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_DisksClient_NewDisksRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewDisksRESTClient: %w", err)
         	}
         	defer disksClient.Close()
         
         	disks := [](*computepb.Disk){}
         
         	for _, diskName := range diskNames {
         		reqDisk := &computepb.GetDiskRequest{
         			Project: projectID,
         			Zone:    zone,
         			Disk:    diskName,
         		}
         
         		disk, err := disksClient.Get(ctx, reqDisk)
         		if err != nil {
         			return fmt.Errorf("unable to get disk: %w", err)
         		}
         
         		disks = append(disks, disk)
         	}
         
         	attachedDisks := [](*computepb.AttachedDisk){}
         
         	for _, disk := range disks {
         		attachedDisk := &computepb.AttachedDisk{
         			Source: proto.String(disk.GetSelfLink()),
         		}
         		attachedDisks = append(attachedDisks, attachedDisk)
         	}
         
         	attachedDisks[0].Boot = proto.Bool(true)
         
         	instanceResource := &computepb.Instance{
         		Name:        proto.String(instanceName),
         		Disks:       attachedDisks,
         		MachineType: proto.String(fmt.Sprintf("zones/%s/machineTypes/n1-standard-1", zone)),
         		NetworkInterfaces: []*computepb.NetworkInterface{
         			{
         				Name: proto.String("global/networks/default"),
         			},
         		},
         	}
         
         	req := &computepb.InsertInstanceRequest{
         		Project:          projectID,
         		Zone:             zone,
         		InstanceResource: instanceResource,
         	}
         
         	op, err := instancesClient.Insert(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to create instance: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "Instance created\n")
         
         	return nil
         }
         

  9. (Optional) Delete the temporary disk snapshots. After you confirm that your virtual machines are moved, save on storage costs by deleting the temporary snapshots that you created.
         
         import (
         	"context"
         	"fmt"
         	"io"
         
         	compute "cloud.google.com/go/compute/apiv1"
         	computepb "cloud.google.com/go/compute/apiv1/computepb"
         )
         
         // deleteSnapshot deletes a snapshot of a disk.
         func deleteSnapshot(w io.Writer, projectID, snapshotName string) error {
         	// projectID := "your_project_id"
         	// snapshotName := "your_snapshot_name"
         
         	ctx := context.Background()
         	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
         	if err != nil {
         		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
         	}
         	defer snapshotsClient.Close()
         
         	req := &computepb.DeleteSnapshotRequest{
         		Project:  projectID,
         		Snapshot: snapshotName,
         	}
         
         	op, err := snapshotsClient.Delete(ctx, req)
         	if err != nil {
         		return fmt.Errorf("unable to delete snapshot: %w", err)
         	}
         
         	if err = op.Wait(ctx); err != nil {
         		return fmt.Errorf("unable to wait for the operation: %w", err)
         	}
         
         	fmt.Fprintf(w, "Snapshot deleted\n")
         
         	return nil
         }
         




###  Java 

  1. Get the details of the VM and identify the disks that are attached to the VM.
         
         import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
         import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
         import java.io.IOException;
         
         public class GetInstance {
         
           public static void main(String[] args) throws IOException {
             // TODO(developer): Replace these variables before running the sample.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // Name of the zone you want to use. For example: 'us-west3-b'.
             String zone = "europe-central2-b";
         
             // Name of the VM instance you want to query.
             String instanceName = "YOUR_INSTANCE_NAME";
         
             getInstance(projectId, zone, instanceName);
           }
         
           // Prints information about a VM instance in the given zone in the specified project.
           public static void getInstance(String projectId, String zone, String instanceName)
               throws IOException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `instancesClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
         
               [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(projectId, zone, instanceName);
         
               System.out.printf("Retrieved the instance %s", instance.toString());
             }
           }
         }

  2. Set the auto-delete state of the boot disk and data disk to `false` to ensure that the disks are not automatically deleted when the VM is deleted.
         
         import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
         import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import com.google.cloud.compute.v1.[SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class SetDiskAutodelete {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // The zone of the disk that you want to modify.
             String zone = "europe-central2-b";
         
             // Name of the instance the disk is attached to.
             String instanceName = "YOUR_INSTANCE_NAME";
         
             // The name of the disk for which you want to modify the autodelete flag.
             String diskName = "YOUR_DISK_NAME";
         
             // The new value of the autodelete flag.
             boolean autoDelete = true;
         
             setDiskAutodelete(projectId, zone, instanceName, diskName, autoDelete);
           }
         
           // Sets the autodelete flag of a disk to given value.
           public static void setDiskAutodelete(String projectId, String zone, String instanceName,
               String diskName, boolean autoDelete)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `instancesClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
         
               // Retrieve the instance given by the instanceName.
               [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(projectId, zone, instanceName);
         
               // Check if the instance contains a disk that matches the given diskName.
               boolean diskNameMatch = instance.[getDisksList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getDisksList__)()
                   .stream()
                   .anyMatch(disk -> disk.getDeviceName().equals(diskName));
         
               if (!diskNameMatch) {
                 throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(
                     String.format("Instance %s doesn't have a disk named %s attached", instanceName,
                         diskName));
               }
         
               // Create the request object.
               [SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest.html) request = [SetDiskAutoDeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetDiskAutoDeleteInstanceRequest.html).newBuilder()
                   .setProject(projectId)
                   .setZone(zone)
                   .setInstance(instanceName)
                   .setDeviceName(diskName)
                   // Update the autodelete property.
                   .setAutoDelete(autoDelete)
                   .build();
         
               // Wait for the update instance operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.[setDiskAutoDeleteAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_setDiskAutoDeleteAsync_com_google_cloud_compute_v1_SetDiskAutoDeleteInstanceRequest_)(request)
                   .get(3, TimeUnit.MINUTES);
         
               if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Failed to update Disk autodelete field!" + response);
                 return;
               }
               System.out.println(
                   "Disk autodelete field updated. Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
             }
           }
         }

  3. Create backups of your data by using persistent disk snapshots.

As a precaution, create backups of your data while the persistent disks are still attached to the VM by using persistent disk snapshots. Before you take a snapshot, ensure that it is consistent with the state of the persistent disk by adhering to [snapshot best practices](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency).

**Note:** If you are running a Windows VM, the VM must be terminated before you can create a snapshot. Follow the steps to [create a snapshot for Windows VM](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

After you clear your disk buffers, create the snapshots:
         
         import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
         import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
         import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
         import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class CreateSnapshot {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
             // You need to pass `zone` or `region` parameter relevant to the disk you want to
             // snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
             // regional disks.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // Name of the disk you want to create.
             String diskName = "YOUR_DISK_NAME";
         
             // Name of the snapshot that you want to create.
             String snapshotName = "YOUR_SNAPSHOT_NAME";
         
             // The zone of the source disk from which you create the snapshot (for zonal disks).
             String zone = "europe-central2-b";
         
             // The region of the source disk from which you create the snapshot (for regional disks).
             String region = "your-disk-region";
         
             // The Cloud Storage multi-region or the Cloud Storage region where you
             // want to store your snapshot.
             // You can specify only one storage location. Available locations:
             // https://cloud.google.com/storage/docs/locations#available-locations
             String location = "europe-central2";
         
             // Project ID or project number of the Cloud project that
             // hosts the disk you want to snapshot. If not provided, the value will be defaulted
             // to 'projectId' value.
             String diskProjectId = "YOUR_DISK_PROJECT_ID";
         
             createSnapshot(projectId, diskName, snapshotName, zone, region, location, diskProjectId);
           }
         
           // Creates a snapshot of a disk.
           public static void createSnapshot(String projectId, String diskName, String snapshotName,
               String zone, String region, String location, String diskProjectId)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `snapshotsClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
         
               if (zone.isEmpty() && region.isEmpty()) {
                 throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You need to specify 'zone' or 'region' for this function to work");
               }
         
               if (!zone.isEmpty() && !region.isEmpty()) {
                 throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You can't set both 'zone' and 'region' parameters");
               }
         
               // If Disk's project id is not specified, then the projectId parameter will be used.
               if (diskProjectId.isEmpty()) {
                 diskProjectId = projectId;
               }
         
               // If zone is not empty, use the DisksClient to create a disk.
               // Else, use the RegionDisksClient.
               [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk;
               if (!zone.isEmpty()) {
                 [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create();
                 disk = disksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html#com_google_cloud_compute_v1_DisksClient_get_com_google_cloud_compute_v1_GetDiskRequest_)(projectId, zone, diskName);
               } else {
                 [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) regionDisksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create();
                 disk = regionDisksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html#com_google_cloud_compute_v1_RegionDisksClient_get_com_google_cloud_compute_v1_GetRegionDiskRequest_)(diskProjectId, region, diskName);
               }
         
               // Set the snapshot properties.
               [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshotResource;
               if (!location.isEmpty()) {
                 snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                     .setName(snapshotName)
                     .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                     .addStorageLocations(location)
                     .build();
               } else {
                 snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                     .setName(snapshotName)
                     .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                     .build();
               }
         
               // Wait for the operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = snapshotsClient.insertAsync(projectId, snapshotResource)
                   .get(3, TimeUnit.MINUTES);
         
               if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Snapshot creation failed!" + operation);
                 return;
               }
         
               // Retrieve the created snapshot.
               [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshot = snapshotsClient.get(projectId, snapshotName);
               System.out.printf("Snapshot created: %s", snapshot.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html#com_google_cloud_compute_v1_Snapshot_getName__)());
         
             }
           }
         }

  4. Delete your VM from the source zone.
         
         import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
         import com.google.cloud.compute.v1.[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html);
         import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class DeleteInstance {
         
           public static void main(String[] args)
               throws IOException, InterruptedException, ExecutionException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
             String project = "your-project-id";
             String zone = "zone-name";
             String instanceName = "instance-name";
             deleteInstance(project, zone, instanceName);
           }
         
           // Delete the instance specified by `instanceName`
           // if it's present in the given project and zone.
           public static void deleteInstance(String project, String zone, String instanceName)
               throws IOException, InterruptedException, ExecutionException, TimeoutException {
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `instancesClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
         
               System.out.printf("Deleting instance: %s ", instanceName);
         
               // Describe which instance is to be deleted.
               [DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html) deleteInstanceRequest = [DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html).newBuilder()
                   .setProject(project)
                   .setZone(zone)
                   .setInstance(instanceName).build();
         
               OperationFuture<Operation, Operation> operation = instancesClient.deleteAsync(
                   deleteInstanceRequest);
               // Wait for the operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
         
               if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Instance deletion failed ! ! " + response);
                 return;
               }
               System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
             }
           }
         }

  5. Next, create another snapshot of both the boot disk and the data disks.
         
         import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
         import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import com.google.cloud.compute.v1.[RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html);
         import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
         import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class CreateSnapshot {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
             // You need to pass `zone` or `region` parameter relevant to the disk you want to
             // snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
             // regional disks.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // Name of the disk you want to create.
             String diskName = "YOUR_DISK_NAME";
         
             // Name of the snapshot that you want to create.
             String snapshotName = "YOUR_SNAPSHOT_NAME";
         
             // The zone of the source disk from which you create the snapshot (for zonal disks).
             String zone = "europe-central2-b";
         
             // The region of the source disk from which you create the snapshot (for regional disks).
             String region = "your-disk-region";
         
             // The Cloud Storage multi-region or the Cloud Storage region where you
             // want to store your snapshot.
             // You can specify only one storage location. Available locations:
             // https://cloud.google.com/storage/docs/locations#available-locations
             String location = "europe-central2";
         
             // Project ID or project number of the Cloud project that
             // hosts the disk you want to snapshot. If not provided, the value will be defaulted
             // to 'projectId' value.
             String diskProjectId = "YOUR_DISK_PROJECT_ID";
         
             createSnapshot(projectId, diskName, snapshotName, zone, region, location, diskProjectId);
           }
         
           // Creates a snapshot of a disk.
           public static void createSnapshot(String projectId, String diskName, String snapshotName,
               String zone, String region, String location, String diskProjectId)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `snapshotsClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
         
               if (zone.isEmpty() && region.isEmpty()) {
                 throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You need to specify 'zone' or 'region' for this function to work");
               }
         
               if (!zone.isEmpty() && !region.isEmpty()) {
                 throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("You can't set both 'zone' and 'region' parameters");
               }
         
               // If Disk's project id is not specified, then the projectId parameter will be used.
               if (diskProjectId.isEmpty()) {
                 diskProjectId = projectId;
               }
         
               // If zone is not empty, use the DisksClient to create a disk.
               // Else, use the RegionDisksClient.
               [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk;
               if (!zone.isEmpty()) {
                 [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create();
                 disk = disksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html#com_google_cloud_compute_v1_DisksClient_get_com_google_cloud_compute_v1_GetDiskRequest_)(projectId, zone, diskName);
               } else {
                 [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html) regionDisksClient = [RegionDisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html).create();
                 disk = regionDisksClient.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RegionDisksClient.html#com_google_cloud_compute_v1_RegionDisksClient_get_com_google_cloud_compute_v1_GetRegionDiskRequest_)(diskProjectId, region, diskName);
               }
         
               // Set the snapshot properties.
               [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshotResource;
               if (!location.isEmpty()) {
                 snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                     .setName(snapshotName)
                     .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                     .addStorageLocations(location)
                     .build();
               } else {
                 snapshotResource = [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html).newBuilder()
                     .setName(snapshotName)
                     .setSourceDisk(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                     .build();
               }
         
               // Wait for the operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = snapshotsClient.insertAsync(projectId, snapshotResource)
                   .get(3, TimeUnit.MINUTES);
         
               if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Snapshot creation failed!" + operation);
                 return;
               }
         
               // Retrieve the created snapshot.
               [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshot = snapshotsClient.get(projectId, snapshotName);
               System.out.printf("Snapshot created: %s", snapshot.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html#com_google_cloud_compute_v1_Snapshot_getName__)());
         
             }
           }
         }

  6. (Optional) Delete your persistent disks.

If you plan to reuse the names of the persistent disks for the new disks, you must delete the existing disks to release the names. Deleting your disks also saves on persistent disk storage costs.

If you do not plan to reuse the same disk names, you don't need to delete them.
         
         import com.google.cloud.compute.v1.[DeleteDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteDiskRequest.html);
         import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class DeleteDisk {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // The zone from where you want to delete the disk.
             String zone = "europe-central2-b";
         
             // Name of the disk you want to delete.
             String diskName = "YOUR_DISK_NAME";
         
             deleteDisk(projectId, zone, diskName);
           }
         
           // Deletes a disk from a project.
           public static void deleteDisk(String projectId, String zone, String diskName)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `disksClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
         
               // Create the request object.
               [DeleteDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteDiskRequest.html) deleteDiskRequest = [DeleteDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteDiskRequest.html).newBuilder()
                   .setProject(projectId)
                   .setZone(zone)
                   .setDisk(diskName)
                   .build();
         
               // Wait for the delete disk operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.deleteAsync(deleteDiskRequest)
                   .get(3, TimeUnit.MINUTES);
         
               if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Disk deletion failed!" + response);
                 return;
               }
               System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
             }
           }
         }

  7. Create new persistent disks in the destination zone from the snapshots you created. First create the boot disk, and then the data disks.
         
         import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
         import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
         import com.google.cloud.compute.v1.[InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class CreateDiskFromSnapshot {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // Name of the zone in which you want to create the disk.
             String zone = "europe-central2-b";
         
             // Name of the disk you want to create.
             String diskName = "YOUR_DISK_NAME";
         
             // The type of disk you want to create. This value uses the following format:
             // "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
             // For example: "zones/us-west3-b/diskTypes/pd-ssd"
             String diskType = String.format("zones/%s/diskTypes/pd-ssd", zone);
         
             // Size of the new disk in gigabytes.
             long diskSizeGb = 10;
         
             // The full path and name of the snapshot that you want to use as the source for the new disk.
             // This value uses the following format:
             // "projects/{projectName}/global/snapshots/{snapshotName}"
             String snapshotLink = String.format("projects/%s/global/snapshots/%s", projectId,
                 "SNAPSHOT_NAME");
         
             createDiskFromSnapshot(projectId, zone, diskName, diskType, diskSizeGb, snapshotLink);
           }
         
           // Creates a new disk in a project in given zone, using a snapshot.
           public static void createDiskFromSnapshot(String projectId, String zone, String diskName,
               String diskType, long diskSizeGb, String snapshotLink)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `disksClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
         
               // Set the disk properties and the source snapshot.
               [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
                   .setName(diskName)
                   .setZone(zone)
                   .setSizeGb(diskSizeGb)
                   .setType(diskType)
                   .setSourceSnapshot(snapshotLink)
                   .build();
         
               // Create the insert disk request.
               [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html) insertDiskRequest = [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html).newBuilder()
                   .setProject(projectId)
                   .setZone(zone)
                   .setDiskResource(disk)
                   .build();
         
               // Wait for the create disk operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.insertAsync(insertDiskRequest)
                   .get(3, TimeUnit.MINUTES);
         
               if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Disk creation failed!" + response);
                 return;
               }
               System.out.println("Disk created. Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
             }
           }
         }

  8. Recreate your VM with the new disks in the destination zone.
         
         import com.google.cloud.compute.v1.[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html);
         import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
         import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
         import com.google.cloud.compute.v1.[InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html);
         import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
         import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
         import com.google.cloud.compute.v1.[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html);
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import java.io.IOException;
         import java.util.ArrayList;
         import java.util.List;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class CreateInstanceWithExistingDisks {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // Name of the zone to create the instance in. For example: "us-west3-b"
             String zone = "europe-central2-b";
         
             // Name of the new virtual machine (VM) instance.
             String instanceName = "YOUR_INSTANCE_NAME";
         
             // Array of disk names to be attached to the new virtual machine.
             // First disk in this list will be used as the boot disk.
             List<String> diskNames = List.of("your-boot-disk", "another-disk1", "another-disk2");
         
             createInstanceWithExistingDisks(projectId, zone, instanceName, diskNames);
           }
         
           // Create a new VM instance using the selected disks.
           // The first disk in diskNames will be used as the boot disk.
           public static void createInstanceWithExistingDisks(String projectId, String zone,
               String instanceName, List<String> diskNames)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `instancesClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create();
                 [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
         
               if (diskNames.size() == 0) {
                 throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("At least one disk should be provided");
               }
         
               // Create the list of attached disks to be used in instance creation.
               List<AttachedDisk> attachedDisks = new ArrayList<>();
               for (int i = 0; i < diskNames.size(); i++) {
                 String diskName = diskNames.get(i);
                 [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = disksClient.get(projectId, zone, diskName);
                 [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html) attDisk = null;
         
                 if (i == 0) {
                   // Make the first disk in the list as the boot disk.
                   attDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                       .setSource(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                       .setBoot(true)
                       .build();
                 } else {
                   attDisk = [AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk.html).newBuilder()
                       .setSource(disk.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html#com_google_cloud_compute_v1_Disk_getSelfLink__)())
                       .build();
                 }
                 attachedDisks.add(attDisk);
               }
         
               // Create the instance.
               [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).newBuilder()
                   .setName(instanceName)
                   // Add the attached disks to the instance.
                   .addAllDisks(attachedDisks)
                   .setMachineType(String.format("zones/%s/machineTypes/n1-standard-1", zone))
                   .addNetworkInterfaces(
                       [NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.NetworkInterface.html).newBuilder().setName("global/networks/default").build())
                   .build();
         
               // Create the insert instance request.
               [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html) insertInstanceRequest = [InsertInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertInstanceRequest.html).newBuilder()
                   .setProject(projectId)
                   .setZone(zone)
                   .setInstanceResource(instance)
                   .build();
         
               // Wait for the create operation to complete.
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.insertAsync(insertInstanceRequest)
                   .get(3, TimeUnit.MINUTES);
         
               if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Instance creation failed!" + response);
                 return;
               }
               System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
         
             }
           }
         }

  9. (Optional) Delete the temporary disk snapshots. After you confirm that your virtual machines are moved, save on storage costs by deleting the temporary snapshots that you created.
         
         import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
         import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
         import java.io.IOException;
         import java.util.concurrent.ExecutionException;
         import java.util.concurrent.TimeUnit;
         import java.util.concurrent.TimeoutException;
         
         public class DeleteSnapshot {
         
           public static void main(String[] args)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
             // TODO(developer): Replace these variables before running the sample.
         
             // Project ID or project number of the Cloud project you want to use.
             String projectId = "YOUR_PROJECT_ID";
         
             // Name of the snapshot to be deleted.
             String snapshotName = "YOUR_SNAPSHOT_NAME";
         
             deleteSnapshot(projectId, snapshotName);
           }
         
           // Delete a snapshot of a disk.
           public static void deleteSnapshot(String projectId, String snapshotName)
               throws IOException, ExecutionException, InterruptedException, TimeoutException {
         
             // Initialize client that will be used to send requests. This client only needs to be created
             // once, and can be reused for multiple requests. After completing all of your requests, call
             // the `snapshotsClient.close()` method on the client to safely
             // clean up any remaining background resources.
             try ([SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
         
               [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = snapshotsClient.deleteAsync(projectId, snapshotName)
                   .get(3, TimeUnit.MINUTES);
         
               if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
                 System.out.println("Snapshot deletion failed!" + operation);
                 return;
               }
         
               System.out.println("Snapshot deleted!");
             }
           }
         }




###  Node.js 

  1. Get the details of the VM and identify the disks that are attached to the VM.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const zone = 'europe-central2-b'
         // const instanceName = 'YOUR_INSTANCE_NAME'
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function getInstance() {
           const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           const [instance] = await instancesClient.get({
             project: projectId,
             zone,
             instance: instanceName,
           });
         
           console.log(
             `Instance ${instanceName} data:\n${JSON.stringify(instance, null, 4)}`
           );
         }
         getInstance();

  2. Set the auto-delete state of the boot disk and data disk to `false` to ensure that the disks are not automatically deleted when the VM is deleted.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const zone = 'europe-central2-b';
         // const instanceName = 'YOUR_INSTANCE_NAME';
         // const diskName = 'YOUR_DISK_NAME';
         // const autoDelete = true;
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function setDiskAutodelete() {
           const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           const [instance] = await instancesClient.get({
             project: projectId,
             zone,
             instance: instanceName,
           });
         
           if (!instance.disks.some(disk => disk.deviceName === diskName)) {
             throw new Error(
               `Instance ${instanceName} doesn't have a disk named ${diskName} attached.`
             );
           }
         
           const [response] = await instancesClient.setDiskAutoDelete({
             project: projectId,
             zone,
             instance: instanceName,
             deviceName: diskName,
             autoDelete,
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the update instance operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
               zone: operation.zone.split('/').pop(),
             });
           }
         
           console.log('Disk autoDelete field updated.');
         }
         
         setDiskAutodelete();

  3. Create backups of your data by using persistent disk snapshots.

As a precaution, create backups of your data while the persistent disks are still attached to the VM by using persistent disk snapshots. Before you take a snapshot, ensure that it is consistent with the state of the persistent disk by adhering to [snapshot best practices](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency).

**Note:** If you are running a Windows VM, the VM must be terminated before you can create a snapshot. Follow the steps to [create a snapshot for Windows VM](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

After you clear your disk buffers, create the snapshots:
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const diskName = 'YOUR_DISK_NAME';
         // const snapshotName = 'YOUR_SNAPSHOT_NAME';
         // const zone = 'europe-central2-b';
         // const region = '';
         // const location = 'europe-central2';
         // let diskProjectId = 'YOUR_DISK_PROJECT_ID';
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function createSnapshot() {
           const snapshotsClient = new compute.[SnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           let disk;
         
           if (!zone && !region) {
             throw new Error(
               'You need to specify `zone` or `region` for this function to work.'
             );
           }
         
           if (zone && region) {
             throw new Error("You can't set both `zone` and `region` parameters");
           }
         
           if (!diskProjectId) {
             diskProjectId = projectId;
           }
         
           if (zone) {
             const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
             [disk] = await disksClient.get({
               project: diskProjectId,
               zone,
               disk: diskName,
             });
           } else {
             const regionDisksClient = new compute.[RegionDisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
             [disk] = await regionDisksClient.get({
               project: diskProjectId,
               region,
               disk: diskName,
             });
           }
         
           const snapshotResource = {
             name: snapshotName,
             sourceDisk: disk.selfLink,
           };
         
           if (location) {
             snapshotResource.storageLocations = [location];
           }
         
           const [response] = await snapshotsClient.insert({
             project: projectId,
             snapshotResource,
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the create snapshot operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
             });
           }
         
           console.log('Snapshot created.');
         }
         
         createSnapshot();

  4. Delete your VM from the source zone.
         
         /**
          * TODO(developer): Uncomment these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const zone = 'europe-central2-b'
         // const instanceName = 'YOUR_INSTANCE_NAME';
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         // Delete the instance specified by `instanceName` if it's present in the given project and zone.
         async function deleteInstance() {
           const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           console.log(`Deleting ${instanceName} from ${zone}...`);
         
           const [response] = await instancesClient.delete({
             project: projectId,
             zone,
             instance: instanceName,
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the delete operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
               zone: operation.zone.split('/').pop(),
             });
           }
         
           console.log('Instance deleted.');
         }
         
         deleteInstance();

  5. Next, create another snapshot of both the boot disk and the data disks.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const diskName = 'YOUR_DISK_NAME';
         // const snapshotName = 'YOUR_SNAPSHOT_NAME';
         // const zone = 'europe-central2-b';
         // const region = '';
         // const location = 'europe-central2';
         // let diskProjectId = 'YOUR_DISK_PROJECT_ID';
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function createSnapshot() {
           const snapshotsClient = new compute.[SnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           let disk;
         
           if (!zone && !region) {
             throw new Error(
               'You need to specify `zone` or `region` for this function to work.'
             );
           }
         
           if (zone && region) {
             throw new Error("You can't set both `zone` and `region` parameters");
           }
         
           if (!diskProjectId) {
             diskProjectId = projectId;
           }
         
           if (zone) {
             const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
             [disk] = await disksClient.get({
               project: diskProjectId,
               zone,
               disk: diskName,
             });
           } else {
             const regionDisksClient = new compute.[RegionDisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
             [disk] = await regionDisksClient.get({
               project: diskProjectId,
               region,
               disk: diskName,
             });
           }
         
           const snapshotResource = {
             name: snapshotName,
             sourceDisk: disk.selfLink,
           };
         
           if (location) {
             snapshotResource.storageLocations = [location];
           }
         
           const [response] = await snapshotsClient.insert({
             project: projectId,
             snapshotResource,
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the create snapshot operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
             });
           }
         
           console.log('Snapshot created.');
         }
         
         createSnapshot();

  6. (Optional) Delete your persistent disks.

If you plan to reuse the names of the persistent disks for the new disks, you must delete the existing disks to release the names. Deleting your disks also saves on persistent disk storage costs.

If you do not plan to reuse the same disk names, you don't need to delete them.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const zone = 'europe-central2-b';
         // const diskName = 'YOUR_DISK_NAME';
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function deleteDisk() {
           const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           const [response] = await disksClient.delete({
             project: projectId,
             zone,
             disk: diskName,
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the create disk operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
               zone: operation.zone.split('/').pop(),
             });
           }
         
           console.log('Disk deleted.');
         }
         
         deleteDisk();

  7. Create new persistent disks in the destination zone from the snapshots you created. First create the boot disk, and then the data disks.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const zone = 'europe-central2-b';
         // const diskName = 'YOUR_DISK_NAME';
         // const diskType = 'zones/us-west3-b/diskTypes/pd-ssd';
         // const diskSizeGb = 10;
         // const snapshotLink = 'projects/project_name/global/snapshots/snapshot_name';
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function createDiskFromSnapshot() {
           const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           const [response] = await disksClient.insert({
             project: projectId,
             zone,
             diskResource: {
               sizeGb: diskSizeGb,
               name: diskName,
               zone,
               type: diskType,
               sourceSnapshot: snapshotLink,
             },
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the create disk operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
               zone: operation.zone.split('/').pop(),
             });
           }
         
           console.log('Disk created.');
         }
         
         createDiskFromSnapshot();

  8. Recreate your VM with the new disks in the destination zone.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const zone = 'europe-central2-b';
         // const instanceName = 'YOUR_INSTANCE_NAME';
         // const diskNames = ['boot_disk', 'disk1', 'disk2'];
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function createWithExistingDisks() {
           const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
           const disksClient = new compute.[DisksClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           if (diskNames.length < 1) {
             throw new Error('At least one disk should be provided');
           }
         
           const disks = [];
           for (const diskName of diskNames) {
             const [disk] = await disksClient.get({
               project: projectId,
               zone,
               disk: diskName,
             });
             disks.push(disk);
           }
         
           const attachedDisks = [];
         
           for (const disk of disks) {
             attachedDisks.push({
               source: disk.selfLink,
             });
           }
         
           attachedDisks[0].boot = true;
         
           const [response] = await instancesClient.insert({
             project: projectId,
             zone,
             instanceResource: {
               name: instanceName,
               disks: attachedDisks,
               machineType: `zones/${zone}/machineTypes/n1-standard-1`,
               networkInterfaces: [
                 {
                   name: 'global/networks/default',
                 },
               ],
             },
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the create operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
               zone: operation.zone.split('/').pop(),
             });
           }
         
           console.log('Instance created.');
         }
         
         createWithExistingDisks();

  9. (Optional) Delete the temporary disk snapshots. After you confirm that your virtual machines are moved, save on storage costs by deleting the temporary snapshots that you created.
         
         /**
          * TODO(developer): Uncomment and replace these variables before running the sample.
          */
         // const projectId = 'YOUR_PROJECT_ID';
         // const snapshotName = 'YOUR_SNAPSHOT_NAME';
         
         const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
         
         async function deleteSnapshot() {
           const snapshotsClient = new compute.[SnapshotsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           const [response] = await snapshotsClient.delete({
             project: projectId,
             snapshot: snapshotName,
           });
           let operation = response.latestResponse;
           const operationsClient = new compute.[GlobalOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
         
           // Wait for the create disk operation to complete.
           while (operation.status !== 'DONE') {
             [operation] = await operationsClient.wait({
               operation: operation.name,
               project: projectId,
             });
           }
         
           console.log('Snapshot deleted.');
         }
         
         deleteSnapshot();




###  Python 

  1. Get the details of the VM and identify the disks that are attached to the VM.
         
         from google.cloud import compute_v1
         
         
         def get_instance(project_id: str, zone: str, instance_name: str) -> compute_v1.Instance:
             """
             Get information about a VM instance in the given zone in the specified project.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone you want to use. For example: “us-west3-b”
                 instance_name: name of the VM instance you want to query.
             Returns:
                 An Instance object.
             """
             instance_client = compute_v1.InstancesClient()
             instance = instance_client.get(
                 project=project_id, zone=zone, instance=instance_name
             )
         
             return instance
         
         

  2. Set the auto-delete state of the boot disk and data disk to `false` to ensure that the disks are not automatically deleted when the VM is deleted.
         
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
         
         
         def set_disk_autodelete(
             project_id: str, zone: str, instance_name: str, disk_name: str, autodelete: bool
         ) -> None:
             """
             Set the autodelete flag of a disk to given value.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone in which is the disk you want to modify.
                 instance_name: name of the instance the disk is attached to.
                 disk_name: the name of the disk which flag you want to modify.
                 autodelete: the new value of the autodelete flag.
             """
             instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
             instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
                 project=project_id, zone=zone, instance=instance_name
             )
         
             for disk in instance.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html):
                 if disk.device_name == disk_name:
                     break
             else:
                 raise RuntimeError(
                     f"Instance {instance_name} doesn't have a disk named {disk_name} attached."
                 )
         
             disk.auto_delete = autodelete
         
             operation = instance_client.[update](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_update)(
                 project=project_id,
                 zone=zone,
                 instance=instance_name,
                 instance_resource=instance,
             )
         
             wait_for_extended_operation(operation, "disk update")
         
         

  3. Create backups of your data by using persistent disk snapshots.

As a precaution, create backups of your data while the persistent disks are still attached to the VM by using persistent disk snapshots. Before you take a snapshot, ensure that it is consistent with the state of the persistent disk by adhering to [snapshot best practices](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency).

**Note:** If you are running a Windows VM, the VM must be terminated before you can create a snapshot. Follow the steps to [create a snapshot for Windows VM](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

After you clear your disk buffers, create the snapshots:
         
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
         
         
         def create_snapshot(
             project_id: str,
             disk_name: str,
             snapshot_name: str,
             *,
             zone: str | None = None,
             region: str | None = None,
             location: str | None = None,
             disk_project_id: str | None = None,
         ) -> compute_v1.Snapshot:
             """
             Create a snapshot of a disk.
         
             You need to pass `zone` or `region` parameter relevant to the disk you want to
             snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
             regional disks.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want
                     to use to store the snapshot.
                 disk_name: name of the disk you want to snapshot.
                 snapshot_name: name of the snapshot to be created.
                 zone: name of the zone in which is the disk you want to snapshot (for zonal disks).
                 region: name of the region in which is the disk you want to snapshot (for regional disks).
                 location: The Cloud Storage multi-region or the Cloud Storage region where you
                     want to store your snapshot.
                     You can specify only one storage location. Available locations:
                     https://cloud.google.com/storage/docs/locations#available-locations
                 disk_project_id: project ID or project number of the Cloud project that
                     hosts the disk you want to snapshot. If not provided, will look for
                     the disk in the `project_id` project.
         
             Returns:
                 The new snapshot instance.
             """
             if zone is None and region is None:
                 raise RuntimeError(
                     "You need to specify `zone` or `region` for this function to work."
                 )
             if zone is not None and region is not None:
                 raise RuntimeError("You can't set both `zone` and `region` parameters.")
         
             if disk_project_id is None:
                 disk_project_id = project_id
         
             if zone is not None:
                 disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
                 disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=disk_project_id, zone=zone, disk=disk_name)
             else:
                 regio_disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
                 disk = regio_disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_get)(
                     project=disk_project_id, region=region, disk=disk_name
                 )
         
             snapshot = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Snapshot](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Snapshot.html)()
             snapshot.source_disk = disk.self_link
             snapshot.name = snapshot_name
             if location:
                 snapshot.storage_locations = [location]
         
             snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
             operation = snapshot_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_insert)(project=project_id, snapshot_resource=snapshot)
         
             wait_for_extended_operation(operation, "snapshot creation")
         
             return snapshot_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_get)(project=project_id, snapshot=snapshot_name)
         
         

  4. Delete your VM from the source zone.
         
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
         
         
         def delete_instance(project_id: str, zone: str, machine_name: str) -> None:
             """
             Send an instance deletion request to the Compute Engine API and wait for it to complete.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone you want to use. For example: “us-west3-b”
                 machine_name: name of the machine you want to delete.
             """
             instance_client = comp[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)t[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)    print(f"Deleting {machine_name} from {zone}...")
             operation = instinstance_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_delete)      project=project_id, zone=zone, instance=machine_name
             )
             wait_for_extended_operation(operation, "instance deletion")
             print(f"Instance {machine_name} deleted.")
         
         

  5. Next, create another snapshot of both the boot disk and the data disks.
         
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
         
         
         def create_snapshot(
             project_id: str,
             disk_name: str,
             snapshot_name: str,
             *,
             zone: str | None = None,
             region: str | None = None,
             location: str | None = None,
             disk_project_id: str | None = None,
         ) -> compute_v1.Snapshot:
             """
             Create a snapshot of a disk.
         
             You need to pass `zone` or `region` parameter relevant to the disk you want to
             snapshot, but not both. Pass `zone` parameter for zonal disks and `region` for
             regional disks.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want
                     to use to store the snapshot.
                 disk_name: name of the disk you want to snapshot.
                 snapshot_name: name of the snapshot to be created.
                 zone: name of the zone in which is the disk you want to snapshot (for zonal disks).
                 region: name of the region in which is the disk you want to snapshot (for regional disks).
                 location: The Cloud Storage multi-region or the Cloud Storage region where you
                     want to store your snapshot.
                     You can specify only one storage location. Available locations:
                     https://cloud.google.com/storage/docs/locations#available-locations
                 disk_project_id: project ID or project number of the Cloud project that
                     hosts the disk you want to snapshot. If not provided, will look for
                     the disk in the `project_id` project.
         
             Returns:
                 The new snapshot instance.
             """
             if zone is None and region is None:
                 raise RuntimeError(
                     "You need to specify `zone` or `region` for this function to work."
                 )
             if zone is not None and region is not None:
                 raise RuntimeError("You can't set both `zone` and `region` parameters.")
         
             if disk_project_id is None:
                 disk_project_id = project_id
         
             if zone is not None:
                 disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
                 disk = disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=disk_project_id, zone=zone, disk=disk_name)
             else:
                 regio_disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionDisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html)()
                 disk = regio_disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_disks.RegionDisksClient.html#google_cloud_compute_v1_services_region_disks_RegionDisksClient_get)(
                     project=disk_project_id, region=region, disk=disk_name
                 )
         
             snapshot = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Snapshot](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Snapshot.html)()
             snapshot.source_disk = disk.self_link
             snapshot.name = snapshot_name
             if location:
                 snapshot.storage_locations = [location]
         
             snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
             operation = snapshot_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_insert)(project=project_id, snapshot_resource=snapshot)
         
             wait_for_extended_operation(operation, "snapshot creation")
         
             return snapshot_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_get)(project=project_id, snapshot=snapshot_name)
         
         

  6. (Optional) Delete your persistent disks.

If you plan to reuse the names of the persistent disks for the new disks, you must delete the existing disks to release the names. Deleting your disks also saves on persistent disk storage costs.

If you do not plan to reuse the same disk names, you don't need to delete them.
         
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
         
         
         def delete_disk(project_id: str, zone: str, disk_name: str) -> None:
             """
             Deletes a disk from a project.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone in which is the disk you want to delete.
                 disk_name: name of the disk you want to delete.
             """
             disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
             operation = disk_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_delete)(project=project_id, zone=zone, disk=disk_name)
             wait_for_extended_operation(operation, "disk deletion")
         
         

  7. Create new persistent disks in the destination zone from the snapshots you created. First create the boot disk, and then the data disks.
         
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
         
         
         def create_disk_from_snapshot(
             project_id: str,
             zone: str,
             disk_name: str,
             disk_type: str,
             disk_size_gb: int,
             snapshot_link: str,
         ) -> compute_v1.Disk:
             """
             Creates a new disk in a project in given zone.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone in which you want to create the disk.
                 disk_name: name of the disk you want to create.
                 disk_type: the type of disk you want to create. This value uses the following format:
                     "zones/{zone}/diskTypes/(pd-standard|pd-ssd|pd-balanced|pd-extreme)".
                     For example: "zones/us-west3-b/diskTypes/pd-ssd"
                 disk_size_gb: size of the new disk in gigabytes
                 snapshot_link: a link to the snapshot you want to use as a source for the new disk.
                     This value uses the following format: "projects/{project_name}/global/snapshots/{snapshot_name}"
         
             Returns:
                 An unattached Disk instance.
             """
             disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
             disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
             disk.zone = zone
             disk.size_gb = disk_size_gb
             disk.source_snapshot = snapshot_link
             disk.type_ = disk_type
             disk.name = disk_name
             operation = disk_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_insert)(project=project_id, zone=zone, disk_resource=disk)
         
             wait_for_extended_operation(operation, "disk creation")
         
             return disk_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_get)(project=project_id, zone=zone, disk=disk_name)
         
         

  8. Recreate your VM with the new disks in the destination zone.
         
         from __future__ import annotations
         
         import re
         import sys
         from typing import Any
         import warnings
         
         from google.api_core.extended_operation import ExtendedOperation
         from google.cloud import compute_v1
         
         
         def get_disk(project_id: str, zone: str, disk_name: str) -> compute_v1.Disk:
             """
             Gets a disk from a project.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone where the disk exists.
                 disk_name: name of the disk you want to retrieve.
             """
             disk_client = compute_v1.DisksClient()
             return disk_client.get(project=project_id, zone=zone, disk=disk_name)
         
         
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
         
         
         def create_instance(
             project_id: str,
             zone: str,
             instance_name: str,
             disks: list[compute_v1.AttachedDisk],
             machine_type: str = "n1-standard-1",
             network_link: str = "global/networks/default",
             subnetwork_link: str = None,
             internal_ip: str = None,
             external_access: bool = False,
             external_ipv4: str = None,
             accelerators: list[compute_v1.AcceleratorConfig] = None,
             preemptible: bool = False,
             spot: bool = False,
             instance_termination_action: str = "STOP",
             custom_hostname: str = None,
             delete_protection: bool = False,
         ) -> compute_v1.Instance:
             """
             Send an instance creation request to the Compute Engine API and wait for it to complete.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone to create the instance in. For example: "us-west3-b"
                 instance_name: name of the new virtual machine (VM) instance.
                 disks: a list of compute_v1.AttachedDisk objects describing the disks
                     you want to attach to your new instance.
                 machine_type: machine type of the VM being created. This value uses the
                     following format: "zones/{zone}/machineTypes/{type_name}".
                     For example: "zones/europe-west3-c/machineTypes/f1-micro"
                 network_link: name of the network you want the new instance to use.
                     For example: "global/networks/default" represents the network
                     named "default", which is created automatically for each project.
                 subnetwork_link: name of the subnetwork you want the new instance to use.
                     This value uses the following format:
                     "regions/{region}/subnetworks/{subnetwork_name}"
                 internal_ip: internal IP address you want to assign to the new instance.
                     By default, a free address from the pool of available internal IP addresses of
                     used subnet will be used.
                 external_access: boolean flag indicating if the instance should have an external IPv4
                     address assigned.
                 external_ipv4: external IPv4 address to be assigned to this instance. If you specify
                     an external IP address, it must live in the same region as the zone of the instance.
                     This setting requires `external_access` to be set to True to work.
                 accelerators: a list of AcceleratorConfig objects describing the accelerators that will
                     be attached to the new instance.
                 preemptible: boolean value indicating if the new instance should be preemptible
                     or not. Preemptible VMs have been deprecated and you should now use Spot VMs.
                 spot: boolean value indicating if the new instance should be a Spot VM or not.
                 instance_termination_action: What action should be taken once a Spot VM is terminated.
                     Possible values: "STOP", "DELETE"
                 custom_hostname: Custom hostname of the new VM instance.
                     Custom hostnames must conform to RFC 1035 requirements for valid hostnames.
                 delete_protection: boolean value indicating if the new virtual machine should be
                     protected against deletion or not.
             Returns:
                 Instance object.
             """
             instance_client = compute_v1.InstancesClient()
         
             # Use the network interface provided in the network_link argument.
             network_interface = compute_v1.NetworkInterface()
             network_interface.network = network_link
             if subnetwork_link:
                 network_interface.subnetwork = subnetwork_link
         
             if internal_ip:
                 network_interface.network_i_p = internal_ip
         
             if external_access:
                 access = compute_v1.AccessConfig()
                 access.type_ = compute_v1.AccessConfig.Type.ONE_TO_ONE_NAT.name
                 access.name = "External NAT"
                 access.network_tier = access.NetworkTier.PREMIUM.name
                 if external_ipv4:
                     access.nat_i_p = external_ipv4
                 network_interface.access_configs = [access]
         
             # Collect information into the Instance object.
             instance = compute_v1.Instance()
             instance.network_interfaces = [network_interface]
             instance.name = instance_name
             instance.disks = disks
             if re.match(r"^zones/[a-z\d\-]+/machineTypes/[a-z\d\-]+$", machine_type):
                 instance.machine_type = machine_type
             else:
                 instance.machine_type = f"zones/{zone}/machineTypes/{machine_type}"
         
             instance.scheduling = compute_v1.Scheduling()
             if accelerators:
                 instance.guest_accelerators = accelerators
                 instance.scheduling.on_host_maintenance = (
                     compute_v1.Scheduling.OnHostMaintenance.TERMINATE.name
                 )
         
             if preemptible:
                 # Set the preemptible setting
                 warnings.warn(
                     "Preemptible VMs are being replaced by Spot VMs.", DeprecationWarning
                 )
                 instance.scheduling = compute_v1.Scheduling()
                 instance.scheduling.preemptible = True
         
             if spot:
                 # Set the Spot VM setting
                 instance.scheduling.provisioning_model = (
                     compute_v1.Scheduling.ProvisioningModel.SPOT.name
                 )
                 instance.scheduling.instance_termination_action = instance_termination_action
         
             if custom_hostname is not None:
                 # Set the custom hostname for the instance
                 instance.hostname = custom_hostname
         
             if delete_protection:
                 # Set the delete protection bit
                 instance.deletion_protection = True
         
             # Prepare the request to insert an instance.
             request = compute_v1.InsertInstanceRequest()
             request.zone = zone
             request.project = project_id
             request.instance_resource = instance
         
             # Wait for the create operation to complete.
             print(f"Creating the {instance_name} instance in {zone}...")
         
             operation = instance_client.insert(request=request)
         
             wait_for_extended_operation(operation, "instance creation")
         
             print(f"Instance {instance_name} created.")
             return instance_client.get(project=project_id, zone=zone, instance=instance_name)
         
         
         def create_with_existing_disks(
             project_id: str, zone: str, instance_name: str, disk_names: list[str]
         ) -> compute_v1.Instance:
             """
             Create a new VM instance using selected disks. The first disk in disk_names will
             be used as boot disk.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 zone: name of the zone to create the instance in. For example: "us-west3-b"
                 instance_name: name of the new virtual machine (VM) instance.
                 disk_names: list of disk names to be attached to the new virtual machine.
                     First disk in this list will be used as the boot device.
         
             Returns:
                 Instance object.
             """
             assert len(disk_names) >= 1
             disks = [get_disk(project_id, zone, disk_name) for disk_name in disk_names]
             attached_disks = []
             for disk in disks:
                 adisk = compute_v1.AttachedDisk()
                 adisk.source = disk.self_link
                 attached_disks.append(adisk)
             attached_disks[0].boot = True
             instance = create_instance(project_id, zone, instance_name, attached_disks)
             return instance
         
         

  9. (Optional) Delete the temporary disk snapshots. After you confirm that your virtual machines are moved, save on storage costs by deleting the temporary snapshots that you created.
         
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
         
         
         def delete_snapshot(project_id: str, snapshot_name: str) -> None:
             """
             Delete a snapshot of a disk.
         
             Args:
                 project_id: project ID or project number of the Cloud project you want to use.
                 snapshot_name: name of the snapshot to delete.
             """
         
             snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
             operation = snapshot_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_delete)(project=project_id, snapshot=snapshot_name)
         
             wait_for_extended_operation(operation, "snapshot deletion")
         
         




## What's next

  * Learn how to [change the default zone/region](https://docs.cloud.google.com/compute/docs/regions-zones/changing-default-zone-region) for your project.
  * Learn about [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
  * Check a VM's [status](https://docs.cloud.google.com/compute/docs/instances/checking-instance-status).
  * Learn about [migrating VMs to Compute Engine](https://docs.cloud.google.com/compute/docs/vm-migration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
