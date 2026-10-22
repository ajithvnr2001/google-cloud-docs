---
url: https://docs.cloud.google.com/compute/docs/disks/manage-snapshot-schedules/
title: Manage snapshot schedules for disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:57.055777+00:00
---

# Manage snapshot schedules for disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/manage-snapshot-schedules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage snapshot schedules for disks Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to manage snapshot schedules for your zonal and regional [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) and [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volumes.

You can manage snapshot schedules as follows:

  * View snapshot schedules
  * Change snapshot schedules
  * Delete snapshot schedules



You can also [configure alerts for scheduled snapshots](https://docs.cloud.google.com/compute/docs/disks/create-alert-snapshot-schedule).

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

  * To view snapshot schedules: `compute.resourcePolicies.list` on the project or organization 
  * To update a snapshot schedule: 
    * `compute.resourcePolicies.update` on the resource policy
    * `compute.resourcePolicies.get` on the resource policy
  * To replace a snapshot schedule: 
    * `compute.resourcePolicies.use` on the resource policy
    * `compute.disks.addResourcePolicies` on the disk
    * `compute.disks.removeResourcePolicies` on the disk
  * To delete a snapshot schedule: 
    * `compute.resourcePolicies.delete` on the resource policy
    * `compute.disks.removeResourcePolicies` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View snapshot schedules

To get a list of snapshot schedules, use the console, `gcloud` command, or the Compute Engine API method. This request displays the name, description, and region of all snapshot schedules within a project.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page. 

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Select the **Snapshot schedules** tab.
  3. Use the filter_list **Filter** field to narrow the list of snapshot schedules.
  4. Click the name of a snapshot schedule to see its details.



###  gcloud 

To see a list of your snapshot schedules, use the [`resource-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list).
    
    
     gcloud compute resource-policies list
    

To see the description of a specific snapshot schedule, use the [`resource-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/describe).
    
    
    gcloud compute resource-policies describe SCHEDULE_NAME
    

Replace `SCHEDULE_NAME` with the name of the snapshot schedule.

###  Go 

#### List snapshot schedules
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/protobuf/proto"
    )
    
    // listSnapshotSchedule retrieves a list of snapshot schedules.
    func listSnapshotSchedule(w io.Writer, projectID, region, filter string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    	// region := "eupore-central2"
    
    	// Formatting for filters:
    	// https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ListResourcePoliciesRequest
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewResourcePoliciesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ResourcePoliciesClient_NewResourcePoliciesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.ListResourcePoliciesRequest{
    		Project: projectID,
    		Region:  region,
    		Filter:  proto.String(filter),
    	}
    	it := snapshotsClient.List(ctx, req)
    
    	for {
    		policy, err := it.Next()
    		if err == iterator.[Done](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_Operation_Done) {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s", policy.GetName())
    	}
    	return nil
    }
    

#### Describe a snapshot schedule
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // getSnapshotSchedule gets a snapshot schedule.
    func getSnapshotSchedule(w io.Writer, projectID, scheduleName, region string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    	// region := "eupore-central2"
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewResourcePoliciesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ResourcePoliciesClient_NewResourcePoliciesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.GetResourcePolicyRequest{
    		Project:        projectID,
    		Region:         region,
    		ResourcePolicy: scheduleName,
    	}
    	schedule, err := snapshotsClient.Get(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get snapshot schedule: %w", err)
    	}
    
    	fmt.Fprintf(w, "Found snapshot schedule: %s\n", schedule.GetName())
    
    	return nil
    }
    

###  Java 

#### List snapshot schedules
    
    
    import com.google.cloud.compute.v1.[ListResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListResourcePoliciesRequest.html);
    import com.google.cloud.compute.v1.[ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html);
    import com.google.cloud.compute.v1.[ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html).ListPagedResponse;
    import com.google.cloud.compute.v1.[ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html);
    import java.io.IOException;
    
    public class ListSnapshotSchedules {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region you want to list snapshot schedules from.
        String region = "us-central1";
        // Name of the snapshot schedule you want to list.
        String snapshotScheduleName = "YOUR_SCHEDULE_NAME";
    
        listSnapshotSchedules(projectId, region, snapshotScheduleName);
      }
    
      // Lists snapshot schedules in a specified region, optionally filtered.
      public static ListPagedResponse listSnapshotSchedules(
              String projectId, String region, String snapshotScheduleName) throws IOException {
        String filter = String.format("name = %s", snapshotScheduleName);
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html) resourcePoliciesClient = [ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html).create()) {
    
          [ListResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListResourcePoliciesRequest.html) request = [ListResourcePoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListResourcePoliciesRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRegion(region)
                  .setFilter(filter)
                  .build();
          ListPagedResponse response = resourcePoliciesClient.list(request);
          for ([ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html) resourcePolicy : response.iterateAll()) {
            System.out.println(resourcePolicy);
          }
          return response;
        }
      }
    }

#### Describe a snapshot schedule
    
    
    import com.google.cloud.compute.v1.[GetResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetResourcePolicyRequest.html);
    import com.google.cloud.compute.v1.[ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html);
    import com.google.cloud.compute.v1.[ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html);
    import java.io.IOException;
    
    public class GetSnapshotSchedule {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region in which your snapshot schedule is located.
        String region = "us-central1";
        // Name of your snapshot schedule.
        String snapshotScheduleName = "YOUR_SCHEDULE_NAME";
    
        getSnapshotSchedule(projectId, region, snapshotScheduleName);
      }
    
      // Retrieves the details of a snapshot schedule.
      public static [ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html) getSnapshotSchedule(
            String projectId, String region, String snapshotScheduleName) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html) resourcePoliciesClient = [ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html).create()) {
          [GetResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetResourcePolicyRequest.html) request = [GetResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetResourcePolicyRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRegion(region)
                  .setResourcePolicy(snapshotScheduleName)
                  .build();
          [ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html) resourcePolicy = resourcePoliciesClient.get(request);
          System.out.println(resourcePolicy);
    
          return resourcePolicy;
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Instantiate a resourcePoliciesClient
    const resourcePoliciesClient = new computeLib.[ResourcePoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project name.
    const projectId = await resourcePoliciesClient.getProjectId();
    
    // The location of the snapshot schedule resource policy.
    // region = 'us-central1';
    
    // The name of the snapshot schedule.
    // snapshotScheduleName = 'snapshot-schedule-name';
    
    async function callGetSnapshotSchedule() {
      const [response] = await resourcePoliciesClient.get({
        project: projectId,
        region,
        resourcePolicy: snapshotScheduleName,
      });
    
      console.log(JSON.stringify(response));
    }
    
    await callGetSnapshotSchedule();

###  Python 

#### List snapshot schedules
    
    
    from google.cloud import compute_v1
    from google.cloud.compute_v1.services.resource_policies import pagers
    
    
    def snapshot_schedule_list(project_id: str, region: str) -> pagers.ListPager:
        """
        Lists snapshot schedules for a specified project and region.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the snapshot schedules are located.
        Returns:
            ListPager: A pager for iterating through the list of snapshot schedules.
        """
        client = compute_v1.ResourcePoliciesClient()
    
        request = compute_v1.ListResourcePoliciesRequest(
            project=project_id,
            region=region,
            filter='status = "READY"',  # Optional filter
        )
    
        schedules = client.list(request=request)
        return schedules
    
    

#### Describe a snapshot schedule
    
    
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def snapshot_schedule_get(
        project_id: str, region: str, snapshot_schedule_name: str
    ) -> compute_v1.ResourcePolicy:
        """
        Retrieves a snapshot schedule for a specified project and region.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the snapshot schedule is located.
            snapshot_schedule_name (str): The name of the snapshot schedule.
        Returns:
            compute_v1.ResourcePolicy: The retrieved snapshot schedule.
        """
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePoliciesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html)()
        schedule = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html#google_cloud_compute_v1_services_resource_policies_ResourcePoliciesClient_get)(
            project=project_id, region=region, resource_policy=snapshot_schedule_name
        )
        return schedule
    
    

###  REST 

Make a `GET` request to [`resourcePolicies.aggregatedList`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/aggregatedList) to return a list of the snapshot schedules for a project.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/resourcePolicies
    

Replace `PROJECT_ID` with the project name.

## View snapshot schedules by region

To view the snapshot schedules for a project within a particular region, use the Google Cloud console, gcloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page. 

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Select the **Snapshot schedules** tab.
  3. Use the filter_list **Filter** field to list snapshot schedules for a specific region.



###  gcloud 

To view the snapshot schedules for a project within a specific region, use the [`resource-policies list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/list).
    
    
    gcloud compute resource-policies list PROJECT_ID --filter REGION
    

Replace the following:

  * `PROJECT_ID`: the project name
  * `REGION`: the region, for example `us-west1`



###  REST 

Make a `GET` request to [`resourcePolicies.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/list) to retrieve the snapshot schedules created within a region.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
    

Replace the following:

  * `PROJECT_ID`: the project name
  * `REGION`: the region, for example `us-west1`



## Change a snapshot schedule

After you create a snapshot schedule, you can modify the following fields dynamically, using the Update a snapshot schedule procedure:

  * Description
  * Snapshot schedule
  * Labels applied to the generated snapshots
  * Source disk deletion policy for handling auto-generated snapshots if the source disk is deleted
  * Retention policy to define how long to keep snapshots that are generated from the snapshot schedule



To update other values for a snapshot schedule, you must delete the snapshot schedule and create a new one, as described in Replace a snapshot schedule.

The snapshot schedule updates take effect in the first snapshot after the updates. If a snapshot is running while you update the snapshot schedule, the changes take effect in the following snapshot.

**Note:** When you update a snapshot schedule, only the snapshots created after the update use the updated snapshot schedule values; existing snapshots are not updated.

### Update a snapshot schedule

You can use Google Cloud CLI or the Compute Engine API to change some of the properties of your snapshot schedule, as described in Change a snapshot schedule.

To change other properties of your snapshot schedule, use the method described in Replace a snapshot schedule.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page. 

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Select **Snapshot schedules** to see a list of your schedules.
  3. Click the name of the snapshot schedule that you want to modify.
  4. On the snapshot schedule detail page, click the edit **Edit schedule** button.



###  gcloud 

Use the [`compute resource-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/update) to update a snapshot schedule's description, schedule, retention policy, or labels.
    
    
    gcloud compute resource-policies update snapshot-schedule SCHEDULE_NAME \
       --region=REGION \
       --description="DESCRIPTION" \
       --snapshot-labels="KEY=VALUE" \
       --max-retention-days=DAYS \
       --on-source-disk-delete=DELETE_OPTION \
       --start-time=START_TIME \
       SCHEDULE_FLAG
    

Replace the following:

  * SCHEDULE_NAME: the name of the snapshot schedule.
  * REGION: the region where your snapshot schedule resides.
  * DESCRIPTION: a description of the snapshot schedule. Use quotes around your description.
  * KEY and VALUE: a key-value pair that can be used to [group related or associated resources](https://docs.cloud.google.com/compute/docs/labeling-resources).
  * DAYS: Maximum number of days snapshot is retained before being deleted.
  * DELETE_OPTION: Retention behavior of automatic snapshots after the original disk is deleted. The value must be one of: 
    * `apply-retention-policy`: When the source disk is deleted, continue to apply the retention window for any snapshots created by the snapshot schedule.
    * `keep-auto-snapshots`: (Default) If the source disk is deleted, keep any snapshots created by the snapshot schedule, regardless of the retention window.
  * START_TIME: the UTC start time. The time must start on the hour. For example: 
    * 2:00 PM PST is `22:00`.
    * If you set a start time of `22:13`, you will receive an error.
  * SCHEDULE_FLAG: one of the following flags:

    * `--hourly-schedule=``HOURLY_INTERVAL`: the number of hours between every snapshot. The `HOURLY_INTERVAL` must be an integer between `1` and `23`. For example, setting `--hourly-schedule` to 12, means the snapshot is generated every 12 hours.
    * `--daily-schedule`: performs a snapshot daily, at the `START_TIME`
    * `--weekly-schedule=``WEEKLY_INTERVAL`: defines the day you want the snapshotting to occur. You must spell out the week day; the values are not case-sensitive.

**Note:** If you want to specify a weekly schedule with different days of the week and with different start times, use the `--weekly-schedule-from-file` flag instead of `--weekly-schedule`.
    * `--weekly-schedule-from-file=``FILE_NAME`: specifies a file that contains the weekly snapshot schedule. You can specify weekly schedules on different days of the week and at different times using a file. For example, your file might specify a snapshot schedule on Monday and Wednesday: `none [{"day": "MONDAY", "startTime": "04:00"}, {"day": "WEDNESDAY", "startTime": "02:00"}]` If you include a start time in your file, you don't need to set the `--start-time` flag. The schedule uses the UTC time zone. The time must start on the hour. For example:

      * 2:00 PM PST is `22:00`.
      * If you set a start time of `22:13`, you will receive an error.

The snapshot frequency flags `hourly-schedule`, `daily-schedule`, `weekly-schedule`, and `weekly-schedule-from-file` are mutually-exclusive. You can use only one for your snapshot schedule.




**Examples:**

To change a snapshot schedule to a daily schedule:
    
    
    gcloud compute resource-policies update snapshot-schedule SCHEDULE_NAME \
        --region=REGION --daily-schedule --start-time=START_TIME
    

To change a snapshot to an hourly schedule, and also update the description and snapshot label:
    
    
    gcloud compute resource-policies update snapshot-schedule SCHEDULE_NAME \
        --region=REGION --description="DESCRIPTION" \
        --hourly-schedule=HOURLY_INTERVAL --start-time=START_TIME \
        --snapshot-labels="KEY=VALUE"
    

To change a snapshot retention and source disk deletion policies for a snapshot schedule:
    
    
    gcloud compute resource-policies update snapshot-schedule SCHEDULE_NAME \
        --region=REGION --max-retention-days=DAYS \
        --on-source-disk-delete=DELETE_OPTION
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // editSnapshotSchedule edits a snapshot schedule.
    func editSnapshotSchedule(w io.Writer, projectID, scheduleName, region string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    	// region := "eupore-central2"
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewResourcePoliciesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ResourcePoliciesClient_NewResourcePoliciesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.PatchResourcePolicyRequest{
    		Project:        projectID,
    		Region:         region,
    		ResourcePolicy: scheduleName,
    		ResourcePolicyResource: &computepb.ResourcePolicy{
    			Name:        proto.String(scheduleName),
    			Description: proto.String("MY HOURLY SNAPSHOT SCHEDULE"),
    			SnapshotSchedulePolicy: &computepb.ResourcePolicySnapshotSchedulePolicy{
    				Schedule: &computepb.ResourcePolicySnapshotSchedulePolicySchedule{
    					HourlySchedule: &computepb.ResourcePolicyHourlyCycle{
    						HoursInCycle: proto.Int32(12),
    						StartTime:    proto.String("22:00"),
    					},
    				},
    			},
    		},
    	}
    	op, err := snapshotsClient.Patch(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create snapshot schedule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprint(w, "Snapshot schedule changed\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[PatchResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchResourcePolicyRequest.html);
    import com.google.cloud.compute.v1.[ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html);
    import com.google.cloud.compute.v1.[ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html).[OnSourceDiskDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.OnSourceDiskDelete.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySchedule.html);
    import com.google.cloud.compute.v1.[ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html);
    import com.google.cloud.compute.v1.[ResourcePolicyWeeklyCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycle.html);
    import com.google.cloud.compute.v1.[ResourcePolicyWeeklyCycleDayOfWeek](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycleDayOfWeek.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class EditSnapshotSchedule {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region where your snapshot schedule is located.
        String region = "us-central1";
        // Name of the snapshot schedule you want to update.
        String snapshotScheduleName = "YOUR_SCHEDULE_NAME";
    
        editSnapshotSchedule(projectId, region, snapshotScheduleName);
      }
    
      // Edits a snapshot schedule.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) editSnapshotSchedule(
              String projectId, String region, String snapshotScheduleName)
              throws IOException, InterruptedException, ExecutionException, TimeoutException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html) resourcePoliciesClient = [ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html).create()) {
          Map<String, String> snapshotLabels = new HashMap<>();
          snapshotLabels.put("key", "value");
    
          [ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html).Builder snapshotProperties =
                  [ResourcePolicySnapshotSchedulePolicySnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySnapshotProperties.html).newBuilder();
          snapshotProperties.putAllLabels(snapshotLabels);
    
          [ResourcePolicyWeeklyCycleDayOfWeek](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycleDayOfWeek.html) dayOfWeek = [ResourcePolicyWeeklyCycleDayOfWeek](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycleDayOfWeek.html).newBuilder()
                  .setDay("Tuesday")
                  .setStartTime("09:00")
                  .build();
          [ResourcePolicyWeeklyCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycle.html) weeklySchedule = [ResourcePolicyWeeklyCycle](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycle.html).newBuilder()
                  .[addDayOfWeeks](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicyWeeklyCycle.Builder.html#com_google_cloud_compute_v1_ResourcePolicyWeeklyCycle_Builder_addDayOfWeeks_com_google_cloud_compute_v1_ResourcePolicyWeeklyCycleDayOfWeek_)(dayOfWeek)
                  .build();
    
          int maxRetentionDays = 3;
    
          [ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html).Builder retentionPolicy =
                  [ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html).newBuilder();
          retentionPolicy.[setOnSourceDiskDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicyRetentionPolicy_Builder_setOnSourceDiskDelete_java_lang_String_)([OnSourceDiskDelete](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.OnSourceDiskDelete.html).APPLY_RETENTION_POLICY.toString());
          retentionPolicy.[setMaxRetentionDays](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicyRetentionPolicy_Builder_setMaxRetentionDays_int_)(maxRetentionDays);
    
          String description = "Updated description";
    
          [ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html) updatedSchedule = [ResourcePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.html).newBuilder()
                  .setName(snapshotScheduleName)
                  .setDescription(description)
                  .[setSnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicy_Builder_setSnapshotSchedulePolicy_com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicy_)(
                          [ResourcePolicySnapshotSchedulePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.html).newBuilder()
                                  .setSchedule([ResourcePolicySnapshotSchedulePolicySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySchedule.html).newBuilder()
                                          .[setWeeklySchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicySchedule.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicySchedule_Builder_setWeeklySchedule_com_google_cloud_compute_v1_ResourcePolicyWeeklyCycle_)(weeklySchedule))
                                  .[setSnapshotProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicy_Builder_setSnapshotProperties_com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicySnapshotProperties_)(snapshotProperties)
                                  .[setRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePolicySnapshotSchedulePolicy.Builder.html#com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicy_Builder_setRetentionPolicy_com_google_cloud_compute_v1_ResourcePolicySnapshotSchedulePolicyRetentionPolicy_)(retentionPolicy.build())
                                  .build())
                  .build();
    
          [PatchResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchResourcePolicyRequest.html) request = [PatchResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchResourcePolicyRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRegion(region)
                  .setResourcePolicy(snapshotScheduleName)
                  .setResourcePolicyResource(updatedSchedule)
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = resourcePoliciesClient.patchAsync(request).get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Failed to update snapshot schedule! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
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
    
    async function callEditSnapshotSchedule() {
      const [response] = await resourcePoliciesClient.patch({
        project: projectId,
        region,
        resourcePolicy: snapshotScheduleName,
        resourcePolicyResource: compute.ResourcePolicy({
          snapshotSchedulePolicy:
            compute.ResourcePolicyInstanceSchedulePolicySchedule({
              schedule: compute.ResourcePolicySnapshotSchedulePolicySchedule({
                weeklySchedule: compute.ResourcePolicyWeeklyCycle({
                  dayOfWeeks: [
                    compute.ResourcePolicyWeeklyCycleDayOfWeek({
                      day: 'Tuesday',
                      startTime: '9:00',
                    }),
                  ],
                }),
              }),
            }),
        }),
      });
    
      let operation = response.latestResponse;
    
      // Wait for the edit operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await regionOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          region,
        });
      }
    
      console.log(`Snapshot schedule: ${snapshotScheduleName} edited.`);
    }
    
    await callEditSnapshotSchedule();

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
    
    
    def snapshot_schedule_update(
        project_id: str,
        region: str,
        schedule_name: str,
        schedule_description: str,
        labels: dict,
    ) -> compute_v1.ResourcePolicy:
        """
        Updates a snapshot schedule for a specified project and region.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the snapshot schedule is located.
            schedule_name (str): The name of the snapshot schedule to update.
            schedule_description (str): The new description for the snapshot schedule.
            labels (dict): A dictionary of new labels to apply to the snapshot schedule.
        Returns:
            compute_v1.ResourcePolicy: The updated snapshot schedule.
        """
    
        # Every Monday, starts between 12:00 AM and 1:00 AM
        day = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicyWeeklyCycleDayOfWeek](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicyWeeklyCycleDayOfWeek.html)(
            day="MONDAY", start_time="00:00"
        )
        weekly_schedule = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicyWeeklyCycle](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicyWeeklyCycle.html)(day_of_weeks=[day])
    
        schedule = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicySnapshotSchedulePolicySchedule](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicySnapshotSchedulePolicySchedule.html)()
        # You can change the schedule type to daily_schedule, weekly_schedule, or hourly_schedule
        schedule.weekly_schedule = weekly_schedule
    
        # Autodelete snapshots after 10 days
        retention_policy = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePolicySnapshotSchedulePolicyRetentionPolicy](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourcePolicySnapshotSchedulePolicyRetentionPolicy.html)(
            max_retention_days=10
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
        operation = client.[patch](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html#google_cloud_compute_v1_services_resource_policies_ResourcePoliciesClient_patch)(
            project=project_id,
            region=region,
            resource_policy=schedule_name,
            resource_policy_resource=resource_policy_resource,
        )
        wait_for_extended_operation(operation, "Resource Policy updating")
    
        return client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html#google_cloud_compute_v1_services_resource_policies_ResourcePoliciesClient_get)(project=project_id, region=region, resource_policy=schedule_name)
    
    

###  REST 

Construct a `PATCH` request to the [`resourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies) to update a snapshot schedule's description, schedule, retention policy, source disk deletion policy, or labels. In the request body, you only need to specify the `name` and the fields you want to update.

  * Change the description and label:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/SCHEDULE_NAME
        {
            "name": "SCHEDULE_NAME",
            "description": "DESCRIPTION",
            "snapshotProperties": {
                "labels": {"KEY": "VALUE"}
            }
        }
        

  * Change the snapshot schedule to hourly:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/SCHEDULE_NAME
        {
            "name": "SCHEDULE_NAME",
            "snapshotSchedulePolicy": {
                "schedule": {
                  "hourlySchedule": {
                      "hoursInCycle": HOURLY_INTERVAL,
                      "startTime": START_TIME
                   }
                }
            }
        }
        

  * Change the snapshot schedule to daily:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/SCHEDULE_NAME
        {
            "name": "SCHEDULE_NAME",
            "snapshotSchedulePolicy": {
                "schedule": {
                  "dailySchedule": {
                      "daysInCycle": DAILY_INTERVAL,
                      "startTime": START_TIME
                   }
                }
            }
        }
        

  * Change the snapshot schedule to weekly:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/SCHEDULE_NAME
        {
            "name": "SCHEDULE_NAME",
            "snapshotSchedulePolicy": {
                "schedule": {
                   "weeklySchedule": {
                      "dayOfWeeks": [
                         {
                            "day": WEEKLY_INTERVAL,
                            "startTime": START_TIME
                         }
                      ]
                   }
                }
            }
        }
        

  * Change the snapshot retention policy:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/SCHEDULE_NAME
        {
            "name": "SCHEDULE_NAME",
            "snapshotSchedulePolicy": {
                "retentionPolicy": {
                    "maxRetentionDays": DAYS,
                    "onSourceDiskDelete":"DELETE_OPTION"
                }
           }
        }
        




Replace the following:

  * PROJECT_ID: the project name.
  * REGION: the region where the snapshot schedule is located.
  * SCHEDULE_NAME: the name of the snapshot schedule.
  * DESCRIPTION: a description of the snapshot schedule. Use quotes around your description.
  * KEY and VALUE: a key- value pair that can be used to [group related or associated resources](https://docs.cloud.google.com/compute/docs/labeling-resources).
  * HOURLY_INTERVAL: defines the interval at which you want snapshotting to occur. Set the hourly schedule using an integer between `1` and `23`. To have the snapshots created at the same time every day, choose a number that divides evenly into 24 (1, 2, 3, 4, 6, 8, or 12). For example, setting `--hourly-schedule` to 12, means the snapshot is generated every 12 hours.
  * DAILY_INTERVAL: defines the number of days between each snapshot. To create a snapshot every day, use the value `1`.
  * WEEKLY_INTERVAL: defines a schedule that runs on specific days of the week. Specify one or more days. The following options are available: `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, and `SUNDAY`. You must spell out the week days; they are not case-sensitive. You can define up to 7 intervals for `dayOfWeeks`, one for each day of the week.
  * START_TIME: the UTC start time. The time must start on the hour. For example: 
    * 2:00 PM PST is `22:00` UTC.
    * If you set a start time of `22:13`, you will receive an error.
  * DAYS: Maximum number of days snapshot is retained before being deleted.
  * DELETE_OPTION: Retention behavior of automatic snapshots after the original disk is deleted. The value must be one of: 
    * `APPLY_RETENTION_POLICY`: When the source disk is deleted, continue to apply the retention window for any snapshots created by the snapshot schedule.
    * `KEEP_AUTO_SNAPSHOTS`: (Default) If the source disk is deleted, keep any snapshots created by the snapshot schedule, regardless of the retention window.



### Replace a snapshot schedule

Follow these steps to delete the snapshot schedule and create a new one. Use this method to modify snapshot schedule properties that can't be changed by using the update a snapshot schedule procedure.

If you are replacing a snapshot schedule that is already attached to a disk, you must first detach the schedule from the disk and delete it. Then you can create a new schedule, and attach it to the disk.

Snapshots that are generated from the detached snapshot schedule won't be managed by the new policy. Those snapshots will be retained indefinitely until you delete them.

Use the Google Cloud console, gcloud CLI, or REST to remove and replace your snapshot schedule.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page. 

[Go to the Disks page](https://console.cloud.google.com/compute/disks)

  2. Select the disk that has the schedule you want to detach.
  3. On the **Manage disk** page, click edit**Edit**. You might need to click the more_vert**More actions** menu first.
  4. Open the **Snapshot schedule** drop-down menu.
  5. Click **No schedule** to detach the schedule from the disk.
  6. You can create a new schedule, or swap the schedule while you are editing the disk options.
  7. Click **Save** to complete the task.



###  gcloud 

  1. Use the [`gcloud compute disks remove-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/remove-resource-policies) to detach the snapshot schedule from the disk with the schedule that you want to change.
         
         gcloud compute disks remove-resource-policies DISK_NAME \
             --resource-policies SCHEDULE_NAME \
             --region REGION \
             --zone ZONE
         

Replace the following:

     * `DISK_NAME`: the name of the disk with the snapshot schedule attached to it
     * `SCHEDULE_NAME`: the name of the snapshot schedule that you want to detach from this disk
     * `REGION`: the region where your snapshot schedule resides
     * `ZONE`: the zone where your zonal disk resides
  2. Use the [`gcloud compute disks add-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/add-resource-policies) to add the new snapshot schedule to the disk.
         
         gcloud compute disks add-resource-policies DISK_NAME \
              --resource-policies SCHEDULE_NAME \
              --zone ZONE
         

Replace the following:

     * `DISK_NAME`: the name of the disk with the snapshot schedule resource policy
     * `SCHEDULE_NAME`: the name of the snapshot schedule that you want to add to this disk
     * `ZONE`: the zone where your disk resides



###  REST 

  1. Detach the current snapshot schedule from a disk by constructing a `POST` request to [`disks.removeResourcePolicies`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/removeResourcePolicies).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/removeResourcePolicies
         
         {
           "resourcePolicies": [
              "regions/REGION/resourcePolicies/SCHEDULE_NAME"
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project name
     * `ZONE`: the zone where the disk resides
     * `DISK_NAME`: the name of the disk with the associated snapshot schedule
     * `REGION`: the location of the snapshot schedule
     * `SCHEDULE_NAME`: the name of the snapshot schedule that you are removing from this disk
  2. Attach the new snapshot schedule to the disk by constructing a `POST` request to the [`disks.addResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/addResourcePolicies).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME/addResourcePolicies
         
         {
           "resourcePolicies": [
             "regions/REGION/resourcePolicies/SCHEDULE_NAME"
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the project name
     * `ZONE`: the location of the disk
     * `DISK_NAME`: the name of the disk
     * `REGION`: the location of the snapshot schedule
     * `SCHEDULE_NAME`: the name of the snapshot schedule that you are applying to this disk



## Delete a snapshot schedule

If you delete a snapshot schedule, all auto-generated snapshots associated with the snapshot schedule are kept permanently. However, after the schedule is deleted, it can no longer generate snapshots.

Your retention policy is part of your snapshot schedule. After the schedule is deleted, your retention policy no longer applies. Snapshots that have already been generated are kept permanently until you manually delete them.

To delete an existing snapshot schedule, use the Google Cloud console, Google Cloud CLI, or the Compute Engine API method. If the schedule is already attached to a disk, detach the schedule from the disk first, then delete the schedule. You cannot delete a snapshot schedule that is attached to a disk.

###  Console 

  1. In the Google Cloud console, go to the **Snapshots** page. 

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Select **Snapshot schedules** to see a list of your schedules.
  3. Select any schedule not associated with a disk.
  4. Click delete **Delete**.

**Note:** If the schedule is already attached to a disk, you must first detach the schedule from its disk, then you can delete the schedule.



###  gcloud 

To delete a snapshot schedule, use the [`resource-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/delete).
    
    
    gcloud compute resource-policies delete SCHEDULE_NAME \
        --region REGION
    

Replace the following:

  * `SCHEDULE_NAME`: the name of the snapshot schedule
  * `REGION`: the location of the snapshot schedule



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // deleteSnapshotSchedule deletes a snapshot schedule.
    func deleteSnapshotSchedule(w io.Writer, projectID, scheduleName, region string) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_snapshot_name"
    	// region := "eupore-central2"
    
    	ctx := context.Background()
    
    	snapshotsClient, err := compute.[NewResourcePoliciesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ResourcePoliciesClient_NewResourcePoliciesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	req := &computepb.DeleteResourcePolicyRequest{
    		Project:        projectID,
    		Region:         region,
    		ResourcePolicy: scheduleName,
    	}
    	op, err := snapshotsClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete snapshot schedule: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprint(w, "Snapshot schedule deleted\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DeleteResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteResourcePolicyRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteSnapshotSchedule {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the region where your snapshot schedule is located.
        String region = "us-central1";
        // Name of the snapshot schedule you want to delete.
        String snapshotScheduleName = "YOUR_SCHEDULE_NAME";
    
        deleteSnapshotSchedule(projectId, region, snapshotScheduleName);
      }
    
      // Deletes a snapshot schedule policy.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) deleteSnapshotSchedule(
              String projectId, String region, String snapshotScheduleName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html) resourcePoliciesClient = [ResourcePoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ResourcePoliciesClient.html).create()) {
          [DeleteResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteResourcePolicyRequest.html) request = [DeleteResourcePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteResourcePolicyRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRegion(region)
                  .setResourcePolicy(snapshotScheduleName)
                  .build();
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = resourcePoliciesClient.deleteAsync(request).get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Snapshot schedule deletion failed! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
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
    // snapshotScheduleName = 'snapshot-schedule-name'
    
    async function callDeleteSnapshotSchedule() {
      // If the snapshot schedule is already attached to a disk, you will receive an error.
      const [response] = await resourcePoliciesClient.delete({
        project: projectId,
        region,
        resourcePolicy: snapshotScheduleName,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the delete operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await regionOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          region,
        });
      }
    
      console.log(`Snapshot schedule: ${snapshotScheduleName} deleted.`);
    }
    
    await callDeleteSnapshotSchedule();

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
    
    
    def snapshot_schedule_delete(
        project_id: str, region: str, snapshot_schedule_name: str
    ) -> None:
        """
        Deletes a snapshot schedule for a specified project and region.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the snapshot schedule is located.
            snapshot_schedule_name (str): The name of the snapshot schedule to delete.
        Returns:
            None
        """
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ResourcePoliciesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html)()
        operation = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.resource_policies.ResourcePoliciesClient.html#google_cloud_compute_v1_services_resource_policies_ResourcePoliciesClient_delete)(
            project=project_id, region=region, resource_policy=snapshot_schedule_name
        )
        wait_for_extended_operation(operation, "Resource Policy deletion")
    
    

###  REST 

To delete a snapshot schedule, make a `DELETE` request to [`resourcePolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/delete). If the snapshot schedule is already attached to a disk, you will receive an error.
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/SCHEDULE_NAME
    

Replace the following:

  * `PROJECT_ID`: the project name
  * `REGION`: the location of the snapshot schedule
  * `SCHEDULE_NAME`: the name of the snapshot schedule



## Logging and monitoring

Every scheduled snapshot associated with a disk is continuously creating a [system event](https://docs.cloud.google.com/logging/docs/audit#system-event), which is monitored and logged at all times. The system event audit logs are always enabled.

These logs provide behavioral information about your scheduled snapshots for each associated disk. You can view your logs from the Logging menu in the Google Cloud console.

For more information about using the Logs Explorer, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. In the **All resource** drop-down list, point to **Disk** and select **All disk_id**.

  3. In the **All logs** drop-down list, select **cloudaudit.googleapis.com/system_event** and click **OK**.

  4. In the **Any log level** drop-down list, select the log type.




## What's next

  * Learn about snapshot schedule frequencies, retention policies, and naming rules in [About snapshot schedules for disks](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).
  * View and delete the generated snapshots, as described in [Manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots).
  * Learn how to [view logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
