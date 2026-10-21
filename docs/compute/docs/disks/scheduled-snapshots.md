---
url: https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots/
title: Create schedules for disk snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:21.995817+00:00
---

# Create schedules for disk snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create schedules for disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You create a snapshot schedule to regularly and automatically back up zonal and regional [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) and [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volumes. Use snapshot schedules as a best practice to back up your Compute Engine workloads.

If you want to create a snapshot schedule that captures the state of the application data at the time of back up, also referred to as an _application consistent_ , _guest-flush_ , or _VSS snapshot_ , see [Create Linux application consistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) or [Create a Windows application consistent disk snapshot](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

For more information about the snapshot schedule properties, see [Snapshot schedule properties](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules#properties).

## Before you begin

  * Review the [Limitations](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules#limitations) for snapshot schedules.
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to create a snapshot schedule, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a snapshot schedule. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a snapshot schedule:

  * To create a snapshot schedule: `compute.resourcePolicies.create` on the project or organization 
  * To attach a snapshot schedule to a disk: 
    * `compute.disks.addResourcePolicies` on the disk
    * `compute.resourcePolicies.use` on the resource policy
  * To create a disk with a snapshot schedule: 
    * `compute.disks.create` on the project
    * `compute.resourcePolicies.create` on the project
    * `compute.disks.addResourcePolicies` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview of creating snapshot schedules

When you create a snapshot schedule, you create a [resource policy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies) that you can apply to one or more Persistent Disk or Hyperdisk volumes.

You can create snapshot schedules in the following ways:

  * Create a snapshot schedule and then attach it to an existing disk.
  * Create a new disk with a snapshot schedule.



## Using encryption with snapshot schedules

If a disk uses a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/cmek), when you use a snapshot schedule to create snapshots of that disk, all the created snapshots are automatically encrypted with the same key.

You can't use snapshot schedules with disks that use a [customer-supplied encryption key (CSEK)](https://docs.cloud.google.com/docs/security/encryption/customer-supplied-encryption-keys).

## Create a snapshot schedule

You can create a snapshot schedule for your disks using the Google Cloud console, Google Cloud CLI, or REST. You must create your snapshot schedule in the same region where your disk resides. For example, if your disk resides in zone `us-west1-a`, you must create the snapshot schedule in the `us-west1` region. However, you can choose to store the snapshots generated by the snapshot schedule in a different location.

**Note:** If you use the gcloud CLI or the Google Cloud console, you must always set a retention policy when creating a snapshot schedule. If you make a request using REST, then you can omit this field and your snapshots will be retained indefinitely.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[ Go to VM instances](https://console.cloud.google.com/compute/instances?walkthrough_id=compute--storage--create-snapshot-schedule)   
school The remaining steps will appear automatically in the Google Cloud console. 

  2. Select the project that contains your VM instances. 
  3. In the **Name** column, click the name of the VM that has the persistent disk to create a snapshot schedule for. 
  4. In **Storage** , click the name of the **Boot disk** or the **Additional disk** to create a snapshot schedule for. 
  5. Click edit**Edit**. You might need to click the more_vert **More actions** menu and then edit**Edit**. 
  6. In **Snapshot schedule** , choose **Create a schedule**. 
  7. In **Name** , enter one of the following names for the snapshot schedule: 
     * `boot-disk-snapshot-schedule`
     * `attached-persistent-disk-snapshot-schedule`
  8. In the **Location** section, [choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). The predefined or customized default location defined in your snapshot settings is automatically selected. Optionally, you can override the snapshot settings and store your snapshots in a custom storage location by doing the following: 

     1. Choose the type of storage location that you want for your snapshot. 

        * Choose **[Multi-regional](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr)** for higher availability at a higher cost.  

        * Choose **[Regional snapshots](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r)** for more control over the physical location of your data at a lower cost. 
     2. In the **Select location** field, select the specific region or multi-region that you want to use. To use the region or multi-region that is closest to your source disk, select **Based on disk's location**. 

  9. To finish creating the snapshot schedule, click **Create**. 
  10. To attach this snapshot schedule to the persistent disk, click **Save**. 



###  gcloud 

  * To schedule globally scoped snapshots for a disk, use the [`gcloud compute resource-policies create snapshot-schedule` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/snapshot-schedule). Set your schedule frequency to hourly, daily, or weekly.
        
        gcloud compute resource-policies create snapshot-schedule SCHEDULE_NAME \
            --description "SCHEDULE_DESCRIPTION" \
            --max-retention-days MAX_RETENTION_DAYS \
            --start-time START_TIME \
            --hourly-schedule SNAPSHOT_INTERVAL \
            --daily-schedule \
            --weekly-schedule SNAPSHOT_INTERVAL or --weekly-schedule-from-file FILE_NAME \
            --on-source-disk-delete DELETION_OPTION \
            --storage-location=STORAGE_LOCATION
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To schedule regionally scoped snapshots for a disk, use the [`gcloud compute resource-policies create snapshot-schedule` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/snapshot-schedule) and specify the snapshot region.
        
        gcloud beta compute resource-policies create snapshot-schedule SCHEDULE_NAME \
            --description "SCHEDULE_DESCRIPTION" \
            --max-retention-days MAX_RETENTION_DAYS \
            --start-time START_TIME \
            --hourly-schedule SNAPSHOT_INTERVAL \
            --daily-schedule \
            --weekly-schedule SNAPSHOT_INTERVAL or --weekly-schedule-from-file FILE_NAME \
            --on-source-disk-delete DELETION_OPTION \
            --storage-location=STORAGE_LOCATION \
            --region REGION \
            --snapshot-region SNAPSHOT_REGION
        




Replace the following:

  * `SCHEDULE_NAME`: the name of the snapshot schedule.
  * `SCHEDULE_DESCRIPTION`: a description of the snapshot schedule. Use quotes around your description.
  * `REGION`: the location of the snapshot schedule resource policy.
  * `SNAPSHOT_REGION`: the region that the scheduled snapshot is scoped to.
  * `MAX_RETENTION_DAYS`: the number of days to retain the snapshot.

For example, a value of `3` means that the snapshots are retained for 3 days before being deleted. You must use a value of `1` or higher.

  * `START_TIME`: the start time in the UTC time zone. The time must start on the hour.

For example:

    * 2:00 PM PST must be specified as `22:00`.
    * If you set a start time of `22:13`, you receive an error.

If you use the `--weekly-schedule-from-file` flag and specify a start time within the file, you don't need to include this flag.

  * `SNAPSHOT_INTERVAL`: the interval between creating successive snapshots. The snapshot frequency flags `hourly-schedule`, `daily-schedule`, `weekly-schedule`, and `weekly-schedule-from-file` are mutually-exclusive. You can use only one for your snapshot schedule.

    * Set a daily schedule by including the `--daily-schedule` flag without any value.
    * Set an hourly schedule with the `--hourly-schedule` flag set to an integer value between 1 and 23. To generate snapshots at the same time every day, choose an hourly number that is evenly divided into 24. For example, setting `--hourly-schedule` to `12`, means a snapshot is created every 12 hours.
    * Set a weekly schedule with the `--weekly-schedule` flag set to the day of the week on which you want the snapshot to be created. You must spell out the week day; the values are not case-sensitive. For example, to back up your disk every Friday, your command would include `--weekly-schedule=friday`.
    * Set an advanced weekly schedule, specifying different days of the week and with different start times by including the `--weekly-schedule-from-file` flag. Replace `FILE_NAME` with the filename that contains the weekly snapshot schedule. While you can specify different days of the week and different start times using a file, you can't specify multiple weekly schedules directly on the command-line. For example, your file might specify two weekly schedules, on Monday and Wednesday, but you can't duplicate this setting on the command line:
          
          [
            {"day": "MONDAY", "startTime": "04:00"},
            {"day": "WEDNESDAY", "startTime": "02:00"}
          ]
          

If you include a start time in your file, you don't need to set the `--start-time` flag on the command line. The schedule uses the UTC time zone.

  * `DELETION_OPTION`: determines what happens to your snapshots if the source disk is deleted. If you want to keep all generated snapshots, you can omit this flag. Otherwise, specify `apply-retention-policy` to use the settings in a retention policy.

  * `STORAGE_LOCATION`: Optional: the [storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). If you omit this flag, the default storage location is used.




**Examples**

In all the following examples:

  * The disk deletion rule is included; the `--on-source-disk-delete` flag is set to the default of `keep-auto-snapshots` to permanently keep all auto-generated snapshots. The alternative is to set this flag to `apply-retention-policy` to use your snapshot retention policy.
  * The storage location is manually set to `US`, so all generated snapshots are stored in the US multi-region.
  * The labels `env=dev` and `media=images` are applied to all generated snapshots.
  * The retention policy is set to 10 days.



**Hourly schedule:** In this example, the snapshot schedule starts at 22:00 UTC (14:00 PST) and occurs every 4 hours.
    
    
      gcloud compute resource-policies create snapshot-schedule hourly-schedule1 \
          --description "MY HOURLY SNAPSHOT SCHEDULE" \
          --max-retention-days 10 \
          --start-time 22:00 \
          --hourly-schedule 4 \
          --region us-west1 \
          --on-source-disk-delete keep-auto-snapshots \
          --snapshot-labels env=dev,media=images \
          --storage-location US
    

**Daily schedule:** In this example, the snapshot schedule starts at 22:00 UTC (14:00 PST) and occurs every day at the same time. The `--daily-schedule` flag must be present, but without an associated value.
    
    
    gcloud compute resource-policies create snapshot-schedule daily-schedule2 \
        --description "MY DAILY SNAPSHOT SCHEDULE" \
        --max-retention-days 10 \
        --start-time 22:00 \
        --daily-schedule \
        --region us-west1 \
        --on-source-disk-delete keep-auto-snapshots \
        --snapshot-labels env=dev,media=images \
        --storage-location US
    

**Weekly schedule:** In this example, the snapshot schedule starts at 22:00 UTC (14:00 PST) and occurs every week on Tuesday.
    
    
    gcloud compute resource-policies create snapshot-schedule weekly-schedule3 \
        --description "MY WEEKLY SNAPSHOT SCHEDULE" \
        --max-retention-days 10 \
        --start-time 22:00 \
        --weekly-schedule tuesday \
        --region us-west1 \
        --on-source-disk-delete keep-auto-snapshots \
        --snapshot-labels env=dev,media=images \
        --storage-location US
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createSnapshotSchedule creates a snapshot schedule.
    func createSnapshotSchedule(w io.Writer, projectID, scheduleName, region string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    	// region := "eupore-central2"
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewResourcePoliciesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ResourcePoliciesClient_NewResourcePoliciesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.InsertResourcePolicyRequest{
    		Project: projectID,
    		Region:  region,
    		ResourcePolicyResource: &computepb.ResourcePolicy{
    			Name:        proto.String(scheduleName),
    			Description: proto.String("MY DAILY SNAPSHOT SCHEDULE"),
    			Region:      proto.String("europe-central2"),
    			SnapshotSchedulePolicy: &computepb.ResourcePolicySnapshotSchedulePolicy{
    				RetentionPolicy: &computepb.ResourcePolicySnapshotSchedulePolicyRetentionPolicy{
    					MaxRetentionDays: proto.Int32(10),
    					// Check the OnSourceDiskDelete enum for the list of possible values.
    					OnSourceDiskDelete: proto.String("KEEP_AUTO_SNAPSHOTS"),
    				},
    				Schedule: &computepb.ResourcePolicySnapshotSchedulePolicySchedule{
    					DailySchedule: &computepb.ResourcePolicyDailyCycle{
    						DaysInCycle: proto.Int32(1),
    						StartTime:   proto.String("22:00"),
    					},
    				},
    				SnapshotProperties: &computepb.ResourcePolicySnapshotSchedulePolicySnapshotProperties{
    					StorageLocations: []string{"eu"},
    					Labels: map[string]string{
    						"env":   "dev",
    						"media": "images",
    					},
    				},
    			},
    		},
    	}
    	op, err := snapshotsClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create snapshot schedule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprint(w, "Snapshot schedule created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[InsertResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertResourcePolicyRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html);
    import com.google.cloud.compute.v1.[ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html);
    import com.google.cloud.compute.v1.[ResourcePolicyHourlyCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyHourlyCycle.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html).[OnSourceDiskDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.OnSourceDiskDelete.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySchedule.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateSnapshotSchedule {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region in which you want to create the snapshot schedule.
        String region = "us-central1";
        // Name of the snapshot schedule you want to create.
        String snapshotScheduleName = "YOUR_SCHEDULE_NAME";
        // Description of the snapshot schedule.
        String scheduleDescription = "YOUR_SCHEDULE_DESCRIPTION";
        // Maximum number of days to retain snapshots.
        int maxRetentionDays = 10;
        // Storage location for the snapshots.
        // More about storage locations:
        // https://cloud.google.com/compute/docs/disks/snapshots?authuser=0#selecting_a_storage_location
        String storageLocation = "US";
    
        createSnapshotSchedule(projectId, region, snapshotScheduleName, scheduleDescription,
                maxRetentionDays, storageLocation);
      }
    
      // Creates a snapshot schedule policy.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createSnapshotSchedule(String projectId, String region,
                String snapshotScheduleName, String scheduleDescription, int maxRetentionDays,
                String storageLocation)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html) resourcePoliciesClient = [ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html).create()) {
          int snapshotInterval = 10; // Create a snapshot every 10 hours
          String startTime = "08:00"; // Define the hourly schedule
    
          [ResourcePolicyHourlyCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyHourlyCycle.html) hourlyCycle = [ResourcePolicyHourlyCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyHourlyCycle.html).newBuilder()
                  .[setHoursInCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyHourlyCycle.Builder.html#com_google_cloud_compute_v1_ResourcePolicyHourlyCycle_Builder_setHoursInCycle_int_)(snapshotInterval)
                  .setStartTime(startTime)
                  .build();
    
          [ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html) retentionPolicy =
                  [ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html).newBuilder()
                          .[setMaxRetentionDays](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicyRetentionPolicy_Builder_setMaxRetentionDays_int_)(maxRetentionDays)
                          .[setOnSourceDiskDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicyRetentionPolicy_Builder_setOnSourceDiskDelete_java_lang_String_)([OnSourceDiskDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.OnSourceDiskDelete.html).KEEP_AUTO_SNAPSHOTS.toString())
                  .build();
    
          [ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html) snapshotProperties =
                  [ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html).newBuilder()
                          .addStorageLocations(storageLocation)
                          .build();
    
          [ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.html) snapshotSchedulePolicy =
                  [ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.html).newBuilder()
                          .[setRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicy_Builder_setRetentionPolicy_com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicyRetentionPolicy_)(retentionPolicy)
                          .setSchedule([ResourcePolicySnapshotSchedulePolicySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySchedule.html).newBuilder()
                                   .[setHourlySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySchedule.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicySchedule_Builder_setHourlySchedule_com_google_cloud_compute_v1_ResourcePolicyHourlyCycle_)(hourlyCycle)
                                   .build())
                          .[setSnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicy_Builder_setSnapshotProperties_com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicySnapshotProperties_)(snapshotProperties)
                          .build();
    
          [ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html) resourcePolicy = [ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html).newBuilder()
                  .setName(snapshotScheduleName)
                  .setDescription(scheduleDescription)
                  .[setSnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicy_Builder_setSnapshotSchedulePolicy_com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicy_)(snapshotSchedulePolicy)
                  .build();
          [InsertResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertResourcePolicyRequest.html) request = [InsertResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertResourcePolicyRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRegion(region)
                  .setResourcePolicyResource(resourcePolicy)
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = resourcePoliciesClient.insertAsync(request)
                  .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Snapshot schedule creation failed! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a resourcePoliciesClient
    const resourcePoliciesClient = new computeLib.[ResourcePoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a regionOperationsClient
    const regionOperationsClient = new computeLib.[RegionOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project name.
    const projectId = await resourcePoliciesClient.getProjectId();
    
    // The location of the snapshot schedule resource policy.
    // region = 'us-central1';
    
    // The name of the snapshot schedule.
    // snapshotScheduleName = 'snapshot-schedule-name';
    
    // The description of the snapshot schedule.
    const snapshotScheduleDescription = 'snapshot schedule description...';
    
    async function callCreateSnapshotSchedule() {
      const [response] = await resourcePoliciesClient.insert({
        project: projectId,
        region,
        resourcePolicyResource: new compute.ResourcePolicy({
          name: snapshotScheduleName,
          description: snapshotScheduleDescription,
          snapshotSchedulePolicy:
            new compute.ResourcePolicyInstanceSchedulePolicySchedule({
              retentionPolicy:
                new compute.ResourcePolicySnapshotSchedulePolicyRetentionPolicy({
                  maxRetentionDays: 5,
                }),
              schedule: new compute.ResourcePolicySnapshotSchedulePolicySchedule({
                // Similarly, you can create a weekly or monthly schedule.
                // Review the resourcePolicies.insert method for details specific to setting a weekly or monthly schedule.
                // To see more details, open: `https://cloud.google.com/compute/docs/disks/scheduled-snapshots?authuser=0#create_snapshot_schedule`
                dailySchedule: new compute.ResourcePolicyDailyCycle({
                  startTime: '12:00',
                  daysInCycle: 1,
                }),
              }),
              snapshotProperties:
                new compute.ResourcePolicySnapshotSchedulePolicySnapshotProperties(
                  {
                    guestFlush: false,
                    labels: {
                      env: 'dev',
                      media: 'images',
                    },
                    // OPTIONAL: the storage location. If you omit this flag, the default storage location is used.
                    // storageLocations: 'storage-location',
                  }
                ),
            }),
        }),
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await regionOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          region,
        });
      }
    
      console.log(`Snapshot schedule: ${snapshotScheduleName} created.`);
    }
    
    await callCreateSnapshotSchedule();

###  Python 
    
    
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
    
    
    def snapshot_schedule_create(
        project_id: str,
        region: str,
        schedule_name: str,
        schedule_description: str,
        labels: dict,
    ) -> compute_v1.ResourcePolicy:
        """
        Creates a snapshot schedule for disks for a specified project and region.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the snapshot schedule will be created.
            schedule_name (str): The name of the snapshot schedule group.
            schedule_description (str): The description of the snapshot schedule group.
            labels (dict): The labels to apply to the snapshots. Example: {"env": "dev", "media": "images"}
        Returns:
            compute_v1.ResourcePolicy: The created resource policy.
        """
    
        # # Every hour, starts at 12:00 AM
        # hourly_schedule = compute_v1.ResourcePolicyHourlyCycle(
        #     hours_in_cycle=1, start_time="00:00"
        # )
        #
        # # Every Monday, starts between 12:00 AM and 1:00 AM
        # day = compute_v1.ResourcePolicyWeeklyCycleDayOfWeek(
        #     day="MONDAY", start_time="00:00"
        # )
        # weekly_schedule = compute_v1.ResourcePolicyWeeklyCycle(day_of_weeks=[day])
    
        # In this example we use daily_schedule - every day, starts between 12:00 AM and 1:00 AM
        daily_schedule = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicyDailyCycle](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicyDailyCycle.html)(
            days_in_cycle=1, start_time="00:00"
        )
    
        schedule = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicySnapshotSchedulePolicySchedule](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicySnapshotSchedulePolicySchedule.html)()
        # You can change the schedule type to daily_schedule, weekly_schedule, or hourly_schedule
        schedule.daily_schedule = daily_schedule
    
        # Autodelete snapshots after 5 days
        retention_policy = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html)(
            max_retention_days=5
        )
        snapshot_properties = (
            [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html)(
                guest_flush=False, labels=labels
            )
        )
    
        snapshot_policy = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicySnapshotSchedulePolicy.html)()
        snapshot_policy.schedule = schedule
        snapshot_policy.retention_policy = retention_policy
        snapshot_policy.snapshot_properties = snapshot_properties
    
        resource_policy_resource = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicy](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicy.html)(
            name=schedule_name,
            description=schedule_description,
            snapshot_schedule_policy=snapshot_policy,
        )
    
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePoliciesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html)()
        operation = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html#google_cloud_compute_v1_services_resource_policies_ResourcePoliciesClient_insert)(
            project=project_id,
            region=region,
            resource_policy_resource=resource_policy_resource,
        )
        wait_for_extended_operation(operation, "Resource Policy creation")
    
        return client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html#google_cloud_compute_v1_services_resource_policies_ResourcePoliciesClient_get)(project=project_id, region=region, resource_policy=schedule_name)
    
    

###  REST 

  * To create a snapshot schedule for globally scoped snapshots, construct a `POST` request to [`resourcePolicies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert). You must include the snapshot schedule name and snapshot frequency.

You can also [manually specify a snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location) and add [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources#adding_or_updating_labels_to_existing_resources) in your request.

By default, the `onSourceDiskDelete` parameter is set to `keepAutoSnapshots`. This means that if the source disk is deleted, the auto-generated snapshot for that disk is retained indefinitely. Alternatively, you can set the flag to `applyRetentionPolicy` to apply your retention policy.

The following example sets a daily snapshot schedule that starts at 12:00 UTC (04:00 PST) and repeats every day. The example also sets a retention policy of 5 days; after 5 days, snapshots are automatically removed.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
        
            {
            "name": "SCHEDULE_NAME",
            "description": "SCHEDULE_DESCRIPTION",
            "snapshotSchedulePolicy": {
              "schedule": {
                "dailySchedule": {
                  "startTime": "12:00",
                  "daysInCycle": "1"
                }
              },
              "retentionPolicy": {
                "maxRetentionDays": "5"
              },
              "snapshotProperties": {
                "guestFlush": "False",
                "labels": {
                  "env": "dev",
                  "media": "images"
                },
                "storageLocations": "STORAGE_LOCATION"
              }
            }
            }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a snapshot schedule for regionally scoped snapshots, construct a `POST` request to [`resourcePolicies.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert) and specify the snapshot region.
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/resourcePolicies
        
            {
            "name": "SCHEDULE_NAME",
            "description": "SCHEDULE_DESCRIPTION",
            "snapshotSchedulePolicy": {
              "schedule": {
                "dailySchedule": {
                  "startTime": "12:00",
                  "daysInCycle": "1"
                }
              },
              "retentionPolicy": {
                "maxRetentionDays": "5"
              },
              "snapshotProperties": {
                "guestFlush": "False",
                "region": "SNAPSHOT_REGION"
              }
            }
            }
        




Replace the following:

  * `PROJECT_ID`: the project name
  * `REGION`: the location of the snapshot schedule resource policy
  * `SNAPSHOT_REGION`: the region that the scheduled snapshot is scoped to
  * `SCHEDULE_DESCRIPTION`: the description of the snapshot schedule
  * `SCHEDULE_NAME`: the name of the snapshot schedule
  * `STORAGE_LOCATION`: Optional: the [storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). If you omit this flag, the default storage location is used.



Similarly, you can create a weekly or monthly schedule. Review the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert) for details specific to setting a weekly or monthly schedule.

For example, the following request creates a weekly schedule that runs on Tuesday at 9:00 UTC.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
    
    {
       "name": "SCHEDULE_NAME",
       "description": "SCHEDULE_DESCRIPTION",
       "snapshotSchedulePolicy": {
          "schedule": {
            "weeklySchedule": {
              "dayOfWeeks": [
              {
                "day": "Tuesday",
                "startTime": "9:00"
              }
              ]
            }
          },
          "retentionPolicy": {
              "maxRetentionDays": "5"
          },
          "snapshotProperties": {
              "guestFlush": "False",
              "labels": {
                   "production": "webserver"
              },
              "storageLocations": "US"
          }
      }
    }
    

## Attach a snapshot schedule to a disk

After you create a schedule, attach it to an existing disk. Use the console, gcloud CLI, or the Compute Engine API.

###  Console 

Attach a snapshot schedule to an existing disk.

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Select the name of the disk to which you want to attach a snapshot schedule. This opens the **Manage disk** page.

  3. On the **Manage disk** page, click edit**Edit**. You might need to click the more_vert**More actions** menu first.

  4. Use the **Snapshot schedule** drop-down menu to add the schedule to the disk. Or create a new schedule.

  5. If you created a new schedule, click **Create**.

  6. Click **Save** to complete the task.




###  gcloud 

To attach a snapshot schedule to a disk, use the [`gcloud compute disks add-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/add-resource-policies).
    
    
    gcloud compute disks add-resource-policies DISK_NAME \
        --resource-policies SCHEDULE_NAME \
        --zone ZONE
    

Replace the following:

  * `DISK_NAME`: the name of the existing disk
  * `SCHEDULE_NAME`: the name of the snapshot schedule
  * `ZONE`: the location of your disk



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // attachSnapshotSchedule attaches a snapshot schedule to disk.
    func attachSnapshotSchedule(w io.Writer, projectID, scheduleName, diskName, region string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    	// diskName := "your_disk_name"
    	// region := "europe-central2"
    
    	ctx := context.Background()
    
    	disksClient, err := compute.[NewRegionDisksRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_RegionDisksClient_NewRegionDisksRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.AddResourcePoliciesRegionDiskRequest{
    		Project: projectID,
    		Region:  region,
    		Disk:    diskName,
    		RegionDisksAddResourcePoliciesRequestResource: &computepb.RegionDisksAddResourcePoliciesRequest{
    			ResourcePolicies: []string{
    				fmt.Sprintf("projects/%s/regions/%s/resourcePolicies/%s", projectID, region, scheduleName),
    			},
    		},
    	}
    	op, err := disksClient.AddResourcePolicies(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to attach schedule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprint(w, "Snapshot schedule attached\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AddResourcePoliciesDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesDiskRequest.html);
    import com.google.cloud.compute.v1.[DisksAddResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksAddResourcePoliciesRequest.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class AttachSnapshotScheduleToDisk {
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone where your disk is located.
        String zone = "us-central1-a";
        // Name of the disk you want to attach the snapshot schedule to.
        String diskName = "YOUR_DISK_NAME";
        // Name of the snapshot schedule you want to attach.
        String snapshotScheduleName = "YOUR_SNAPSHOT_SCHEDULE_NAME";
        // Name of the region where your snapshot schedule is located.
        String region = "us-central1";
    
        attachSnapshotScheduleToDisk(projectId, zone, diskName, snapshotScheduleName, region);
      }
    
      // Attaches a snapshot schedule to a disk.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) attachSnapshotScheduleToDisk(
            String projectId, String zone, String diskName, String snapshotScheduleName, String region)
            throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        String resourcePolicyLink = String.format(
                "projects/%s/regions/%s/resourcePolicies/%s", projectId, region, snapshotScheduleName);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          [AddResourcePoliciesDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesDiskRequest.html) request = [AddResourcePoliciesDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesDiskRequest.html).newBuilder()
                  .setProject(projectId)
                  .setZone(zone)
                  .setDisk(diskName)
                  .[setDisksAddResourcePoliciesRequestResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddResourcePoliciesDiskRequest.Builder.html#com_google_cloud_compute_v1_AddResourcePoliciesDiskRequest_Builder_setDisksAddResourcePoliciesRequestResource_com_google_cloud_compute_v1_DisksAddResourcePoliciesRequest_)(
                          [DisksAddResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksAddResourcePoliciesRequest.html).newBuilder()
                                  .addResourcePolicies(resourcePolicyLink)
                                  .build())
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.addResourcePoliciesAsync(request).get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Error attaching snapshot schedule to disk: " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Python 
    
    
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
    
    
    def snapshot_schedule_attach(
        project_id: str, zone: str, region: str, disk_name: str, schedule_name: str
    ) -> None:
        """
        Attaches a snapshot schedule to a specified disk.
        Args:
            project_id (str): The ID of the Google Cloud project.
            zone (str): The zone where the disk is located.
            region (str): The region where the snapshot schedule was created
            disk_name (str): The name of the disk to which the snapshot schedule will be attached.
            schedule_name (str): The name of the snapshot schedule that you are applying to this disk
        Returns:
            None
        """
        disks_add_request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksAddResourcePoliciesRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DisksAddResourcePoliciesRequest.html)(
            resource_policies=[f"regions/{region}/resourcePolicies/{schedule_name}"]
        )
    
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        operation = client.[add_resource_policies](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html#google_cloud_compute_v1_services_disks_DisksClient_add_resource_policies)(
            project=project_id,
            zone=zone,
            disk=disk_name,
            disks_add_resource_policies_request_resource=disks_add_request,
        )
        wait_for_extended_operation(operation, "Attaching snapshot schedule to disk")
    
    

###  REST 

Construct a `POST` request to [`disks.addResourcePolicies`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/addResourcePolicies) to attach a snapshot schedule to an existing disk.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/addResourcePolicies
    
    {
      "resourcePolicies": [
        "regions/REGION/resourcePolicies/SCHEDULE_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project name
  * `ZONE`: the zone where the disk is located
  * `REGION`: the region where the snapshot schedule was created
  * `DISK_NAME`: the name of the disk
  * `SCHEDULE_NAME`: the name of the snapshot schedule that you are applying to this disk



## Create a disk with a snapshot schedule

You can use the Google Cloud console or gcloud CLI to create a disk and a snapshot schedule at the same time.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. Click **Create Disk**.

  3. Complete the required fields to create a zonal or regional disk.

  4. Create your disk in the same region as your snapshot schedule.

  5. Populate the fields for your **Snapshot schedule**.

  6. Use the drop-down menu and complete the fields to create the schedule.

  7. Click **Create** to create the schedule.

  8. Click **Create** to create the disk.




###  gcloud 

Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) to create a zonal or regional Persistent Disk or Hyperdisk and attach a snapshot schedule to it.
    
    
    gcloud compute disks create DISK_NAME \
         --resource-policies SCHEDULE_NAME \
         --zone ZONE
    

Replace the following:

  * `DISK_NAME`: the name of the new disk
  * `SCHEDULE_NAME`: the name of the snapshot schedule
  * `ZONE`: the location where you are creating the disk. The disk must be in a zone that is in the same region as the snapshot schedule.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createDiskWithSnapshotSchedule creates a new empty regional disk with snapshot schedule
    func createDiskWithSnapshotSchedule(
    	w io.Writer,
    	projectID, region, diskName, diskType, scheduleName string,
    	replicaZones []string,
    	diskSizeGb int64,
    ) error {
    	// projectID := "your_project_id"
    	// region := "us-west3" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "regions/us-west3/diskTypes/pd-ssd"
    	// scheduleName := "your_schedule_name"
    	// replicaZones := []string{"us-west3-a", "us-west3-b"}
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
    			SizeGb:       proto.Int64(diskSizeGb),
    			ReplicaZones: replicaZoneURLs,
    			ResourcePolicies: []string{
    				fmt.Sprintf("projects/%s/regions/%s/resourcePolicies/%s", projectID, region, scheduleName),
    			},
    		},
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create disk with schedule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk with schedule created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDiskWithSnapshotSchedule {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone in which you want to create the disk.
        String zone = "us-central1-a";
        // Name of the disk you want to create.
        String diskName = "YOUR_DISK_NAME";
        // Name of the schedule you want to link to the disk.
        String snapshotScheduleName = "YOUR_SCHEDULE_NAME";
    
        createDiskWithSnapshotSchedule(projectId, zone, diskName, snapshotScheduleName);
      }
    
      // Creates disk with linked snapshot schedule.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createDiskWithSnapshotSchedule(
          String projectId, String zone, String diskName, String snapshotScheduleName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
          String region = zone.substring(0, zone.lastIndexOf('-'));
          // Get the resource policy to link to the disk
          String resourcePolicyLink = String.format("projects/%s/regions/%s/resourcePolicies/%s",
                  projectId, region, snapshotScheduleName);
    
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html) disk = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
                  .setName(diskName)
                  .setZone(zone)
                  .addAllResourcePolicies(List.of(resourcePolicyLink))
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = disksClient.insertAsync(projectId, zone, disk).get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Disk creation failed! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

## What's next

  * Learn about [managing snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/manage-snapshot-schedules).
  * Learn about scheduled snapshot frequencies, retention policies, and naming rules in [About snapshot schedules for disks](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).
  * Learn how to [create a custom image from your snapshot](https://docs.cloud.google.com/compute/docs/images/create-custom#create_image).
  * Learn how to [view logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
