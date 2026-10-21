---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups/
title: Manage consistency groups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:50:09.034251+00:00
---

# Manage consistency groups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage consistency groups Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to manage consistency groups. Consistency groups are resource policies that align replication across multiple disks in the same region or zone.

To learn more about consistency groups, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#consistency_groups).

## Limitations

  * A disk can belong to only one consistency group at a time.
  * Consistency groups aren't supported for disks in sole-tenant nodes.
  * Consistency groups can have a maximum of 128 disks.
  * All disks in a consistency group must be in the same project as the consistency group resource policy.
  * A consistency group can contain primary disks or secondary disks, but not both.
  * To enable Asynchronous Replication for the disks in a consistency group, all the disks must be in the same zone, for zonal disks, or in the same pair of zones, for regional disks.
  * You can't add or remove a primary disk to or from a consistency group while the disk is replicating. If you want to add or remove a primary disk to or from a consistency group, you must first [stop replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#stop_replication). You can add or remove secondary disks to or from consistency groups at any time.
  * You can attach a maximum of 16 disks that are in different consistency groups, or disks that aren't in a consistency group to a VM. Disks that are in the same consistency group count as one disk towards the 16 disk limit.



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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Required roles and permissions

To get the permissions that you need to clone disks in a consistency group, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to an instance that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to clone disks in a consistency group. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to clone disks in a consistency group:

  * `compute.disks.create`
  * `compute.disks.useReadOnly` on the source disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a consistency group

If you need to align replication across multiple disks, create a consistency group in the same region as the primary disks. If you need to align disk clones, create a consistency group in the same region as the secondary disks.

Create a consistency group using the Google Cloud console, the Google Cloud CLI, REST, or Terraform.

###  Console 

Create a consistency group by doing the following:

  1. In the Google Cloud console, go to the **Consistency Groups** page.

[Go to Consistency Groups](https://console.cloud.google.com/compute/consistencyGroups)

  2. Click the **Disk consistency groups** tab.

  3. Click **Create consistency group**.

  4. In the **Name** field, enter a name for the consistency group.

  5. In the **Region** field, select the region where your disks are located. If you want to add primary disks to consistency group, select the primary region. If you want to add secondary disks to the consistency group, select the secondary region.

  6. Click **Create**.




###  gcloud 

Create a consistency group using the [`gcloud compute resource-policies create disk-consistency-group` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/disk-consistency-group):
    
    
    gcloud compute resource-policies create disk-consistency-group CONSISTENCY_GROUP_NAME \
        --region=REGION
    

Replace the following:

  * `CONSISTENCY_GROUP_NAME`: the name for the consistency group.
  * `REGION`: the region for the consistency group. If you want to add primary disks to consistency group, use the primary region. If you want to add secondary disks to the consistency group, use the secondary region.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // createConsistencyGroup creates a new consistency group for a project in a given region.
    func createConsistencyGroup(w io.Writer, projectID, region, groupName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-west4"
    	// groupName := "your_group_name"
    
    	ctx := context.Background()
    	disksClient, err := compute.NewResourcePoliciesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.InsertResourcePolicyRequest{
    		Project: projectID,
    		ResourcePolicyResource: &computepb.ResourcePolicy{
    			Name:                       proto.String(groupName),
    			DiskConsistencyGroupPolicy: &computepb.ResourcePolicyDiskConsistencyGroupPolicy{},
    		},
    		Region: region,
    	}
    
    	op, err := disksClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create group: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Group created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.InsertResourcePolicyRequest;
    import com.google.cloud.compute.v1.Operation;
    import com.google.cloud.compute.v1.Operation.Status;
    import com.google.cloud.compute.v1.ResourcePoliciesClient;
    import com.google.cloud.compute.v1.ResourcePolicy;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateConsistencyGroup {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
        // Name of the region in which you want to create the consistency group.
        String region = "us-central1";
        // Name of the consistency group you want to create.
        String consistencyGroupName = "YOUR_CONSISTENCY_GROUP_NAME";
    
        createConsistencyGroup(project, region, consistencyGroupName);
      }
    
      // Creates a new consistency group resource policy in the specified project and region.
      public static Status createConsistencyGroup(
          String project, String region, String consistencyGroupName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (ResourcePoliciesClient  regionResourcePoliciesClient = ResourcePoliciesClient.create()) {
          ResourcePolicy resourcePolicy =
              ResourcePolicy.newBuilder()
                  .setName(consistencyGroupName)
                  .setRegion(region)
                  .setDiskConsistencyGroupPolicy(
                      ResourcePolicy.newBuilder().getDiskConsistencyGroupPolicy())
                  .build();
    
          InsertResourcePolicyRequest request = InsertResourcePolicyRequest.newBuilder()
                  .setProject(project)
                  .setRegion(region)
                  .setResourcePolicyResource(resourcePolicy)
                  .build();
    
          Operation response =
              regionResourcePoliciesClient.insertAsync(request).get(1, TimeUnit.MINUTES);
    
          if (response.hasError()) {
            throw new Error("Error creating consistency group! " + response.getError());
          }
          return response.getStatus();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a resourcePoliciesClient
    const resourcePoliciesClient = new computeLib.ResourcePoliciesClient();
    // Instantiate a regionOperationsClient
    const regionOperationsClient = new computeLib.RegionOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the consistency group.
    const projectId = await resourcePoliciesClient.getProjectId();
    
    // The region for the consistency group.
    // If you want to add primary disks to consistency group, use the same region as the primary disks.
    // If you want to add secondary disks to the consistency group, use the same region as the secondary disks.
    // region = 'europe-central2';
    
    // The name for consistency group.
    // consistencyGroupName = 'consistency-group-name';
    
    async function callCreateConsistencyGroup() {
      // Create a resourcePolicyResource
      const resourcePolicyResource = new compute.ResourcePolicy({
        diskConsistencyGroupPolicy:
          new compute.ResourcePolicyDiskConsistencyGroupPolicy({}),
        name: consistencyGroupName,
      });
    
      const [response] = await resourcePoliciesClient.insert({
        project: projectId,
        region,
        resourcePolicyResource,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create group operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await regionOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          region,
        });
      }
    
      console.log(`Consistency group: ${consistencyGroupName} created.`);
    }
    
    await callCreateConsistencyGroup();

###  Python 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
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
    
    
    def create_consistency_group(
        project_id: str, region: str, group_name: str, group_description: str
    ) -> compute_v1.ResourcePolicy:
        """
        Creates a consistency group in Google Cloud Compute Engine.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the consistency group will be created.
            group_name (str): The name of the consistency group.
            group_description (str): The description of the consistency group.
        Returns:
            compute_v1.ResourcePolicy: The consistency group object
        """
    
        # Initialize the ResourcePoliciesClient
        client = compute_v1.ResourcePoliciesClient()
    
        # Create the ResourcePolicy object with the provided name, description, and policy
        resource_policy_resource = compute_v1.ResourcePolicy(
            name=group_name,
            description=group_description,
            disk_consistency_group_policy=compute_v1.ResourcePolicyDiskConsistencyGroupPolicy(),
        )
    
        operation = client.insert(
            project=project_id,
            region=region,
            resource_policy_resource=resource_policy_resource,
        )
        wait_for_extended_operation(operation, "Consistency group creation")
    
        return client.get(project=project_id, region=region, resource_policy=group_name)
    
    

###  REST 

Create a consistency group using the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies
    {
     "name": "CONSISTENCY_GROUP_NAME",
     "diskConsistencyGroupPolicy": {
      }
    }
    

Replace the following:

  * `PROJECT`: the project that contains the consistency group.
  * `REGION`: the region for the consistency group. If you want to add primary disks to consistency group, use the same region as the primary disks. If you want to add secondary disks to the consistency group, use the same region as the secondary disks.
  * `CONSISTENCY_GROUP_NAME`: the name for the consistency group.



###  Terraform 

To create a consistency group, use the [`compute_resource_policy` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_resource_policy).
    
    
    resource "google_compute_resource_policy" "default" {
      name   = "test-consistency-group"
      region = "us-central1"
      disk_consistency_group_policy {
        enabled = true
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View disks in a consistency group

View disks in a consistency group using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

View the disks included in a consistency group by doing the following:

  1. In the Google Cloud console, go to the **Consistency Groups** page.

[Go to Consistency Groups](https://console.cloud.google.com/compute/consistencyGroups)

  2. Click the **Disk consistency groups** tab.

  3. Click the name of the consistency group that you want to view the disks for. The **Manage consistency group** page opens.

  4. View the **Consistency group members** section to see all disks included in the consistency group.




###  gcloud 

View the disks included in a consistency group using the [`gcloud compute disks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/list):
    
    
    gcloud compute disks list \
        --LOCATION_FLAG=LOCATION \
        --filter=resourcePolicies=CONSISTENCY_GROUP_NAME
    

Replace the following:

  * `LOCATION_FLAG`: the location flag for the disks in the consistency group. If the disks in the consistency group are regional, use `--region`. If the disks in the consistency group are zonal, use `--zone`.
  * `LOCATION`: the region or zone of the disks in the consistency group. For regional disks, use the region. For zonal disks, use the zone.
  * `CONSISTENCY_GROUP_NAME`: the name of the consistency group.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/api/iterator"
    )
    
    // listRegionalConsistencyGroup get list of disks in consistency group for a project in a given region.
    func listRegionalConsistencyGroup(w io.Writer, projectID, region, groupName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-west4"
    	// groupName := "your_group_name"
    
    	if groupName == "" {
    		return fmt.Errorf("group name cannot be empty")
    	}
    
    	ctx := context.Background()
    	// To check for zonal disks in consistency group use compute.NewDisksRESTClient
    	disksClient, err := compute.NewRegionDisksRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewRegionDisksRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	// If using zonal disk client, use computepb.ListDisksRequest
    	req := &computepb.ListRegionDisksRequest{
    		Project: projectID,
    		Region:  region,
    	}
    
    	it := disksClient.List(ctx, req)
    	for {
    		disk, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    
    		for _, diskPolicy := range disk.GetResourcePolicies() {
    			if strings.Contains(diskPolicy, groupName) {
    				fmt.Fprintf(w, "- %s\n", disk.GetName())
    			}
    		}
    	}
    
    	return nil
    }
    

###  Java 

#### List zonal disks in a consistency group
    
    
    import com.google.cloud.compute.v1.Disk;
    import com.google.cloud.compute.v1.DisksClient;
    import com.google.cloud.compute.v1.ListDisksRequest;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class ListZonalDisksInConsistencyGroup {
      public static void main(String[] args)
              throws IOException, InterruptedException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
        // Name of the consistency group.
        String consistencyGroupName = "CONSISTENCY_GROUP_ID";
        // Zone of the disk.
        String disksLocation = "us-central1-a";
        // Region of the consistency group.
        String consistencyGroupLocation = "us-central1";
    
        listZonalDisksInConsistencyGroup(
                project, consistencyGroupName, consistencyGroupLocation, disksLocation);
      }
    
      // Lists disks in a consistency group.
      public static List<Disk> listZonalDisksInConsistencyGroup(String project,
          String consistencyGroupName, String consistencyGroupLocation, String disksLocation)
              throws IOException {
        String filter = String
                .format("https://www.googleapis.com/compute/v1/projects/%s/regions/%s/resourcePolicies/%s",
                        project, consistencyGroupLocation, consistencyGroupName);
        List<Disk> disksList = new ArrayList<>();
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (DisksClient disksClient = DisksClient.create()) {
          ListDisksRequest request =
                  ListDisksRequest.newBuilder()
                          .setProject(project)
                          .setZone(disksLocation)
                          .build();
          DisksClient.ListPagedResponse response = disksClient.list(request);
    
          for (Disk disk : response.iterateAll()) {
            if (disk.getResourcePoliciesList().contains(filter)) {
              disksList.add(disk);
            }
          }
        }
        System.out.println(disksList.size());
        return disksList;
      }
    }

#### List regional disks in a consistency group
    
    
    import com.google.cloud.compute.v1.Disk;
    import com.google.cloud.compute.v1.ListRegionDisksRequest;
    import com.google.cloud.compute.v1.RegionDisksClient;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class ListRegionalDisksInConsistencyGroup {
      public static void main(String[] args)
              throws IOException, InterruptedException, ExecutionException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
        // Name of the consistency group.
        String consistencyGroupName = "CONSISTENCY_GROUP_ID";
        // Region of the disk.
        String disksLocation = "us-central1";
        // Region of the consistency group.
        String consistencyGroupLocation = "us-central1";
    
        listRegionalDisksInConsistencyGroup(
                project, consistencyGroupName, consistencyGroupLocation, disksLocation);
      }
    
      // Lists disks in a consistency group.
      public static List<Disk> listRegionalDisksInConsistencyGroup(String project,
          String consistencyGroupName, String consistencyGroupLocation, String disksLocation)
              throws IOException {
        String filter = String
                .format("https://www.googleapis.com/compute/v1/projects/%s/regions/%s/resourcePolicies/%s",
                        project, consistencyGroupLocation, consistencyGroupName);
        List<Disk> disksList = new ArrayList<>();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (RegionDisksClient disksClient = RegionDisksClient.create()) {
          ListRegionDisksRequest request =
                  ListRegionDisksRequest.newBuilder()
                          .setProject(project)
                          .setRegion(disksLocation)
                          .build();
    
          RegionDisksClient.ListPagedResponse response = disksClient.list(request);
          for (Disk disk : response.iterateAll()) {
            if (disk.getResourcePoliciesList().contains(filter)) {
              disksList.add(disk);
            }
          }
        }
        System.out.println(disksList.size());
        return disksList;
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    
    // If you want to get regional disks, you should use: RegionDisksClient.
    // Instantiate a disksClient
    const disksClient = new computeLib.DisksClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the disks.
    const projectId = await disksClient.getProjectId();
    
    // If you use RegionDisksClient- define region, if DisksClient- define zone.
    // The zone or region of the disks.
    // disksLocation = 'europe-central2-a';
    
    // The name of the consistency group.
    // consistencyGroupName = 'consistency-group-name';
    
    // The region of the consistency group.
    // consistencyGroupLocation = 'europe-central2';
    
    async function callConsistencyGroupDisksList() {
      const filter = `https://www.googleapis.com/compute/v1/projects/${projectId}/regions/${consistencyGroupLocation}/resourcePolicies/${consistencyGroupName}`;
    
      const [response] = await disksClient.list({
        project: projectId,
        // If you use RegionDisksClient, pass region as an argument instead of zone.
        zone: disksLocation,
      });
    
      // Filtering must be done manually for now, since list filtering inside disksClient.list is not supported yet.
      const filteredDisks = response.filter(disk =>
        disk.resourcePolicies.includes(filter)
      );
    
      console.log(JSON.stringify(filteredDisks));
    }
    
    await callConsistencyGroupDisksList();

###  Python 
    
    
    from google.cloud import compute_v1
    
    
    def list_disks_consistency_group(
        project_id: str,
        disk_location: str,
        consistency_group_name: str,
        consistency_group_region: str,
    ) -> list:
        """
        Lists disks that are part of a specified consistency group.
        Args:
            project_id (str): The ID of the Google Cloud project.
            disk_location (str): The region or zone of the disk
            disk_region_flag (bool): Flag indicating if the disk is regional.
            consistency_group_name (str): The name of the consistency group.
            consistency_group_region (str): The region of the consistency group.
        Returns:
            list: A list of disks that are part of the specified consistency group.
        """
        consistency_group_link = (
            f"https://www.googleapis.com/compute/v1/projects/{project_id}/regions/"
            f"{consistency_group_region}/resourcePolicies/{consistency_group_name}"
        )
        # If the final character of the disk_location is a digit, it is a regional disk
        if disk_location[-1].isdigit():
            region_client = compute_v1.RegionDisksClient()
            disks = region_client.list(project=project_id, region=disk_location)
        # For zonal disks we use DisksClient
        else:
            client = compute_v1.DisksClient()
            disks = client.list(project=project_id, zone=disk_location)
        return [disk for disk in disks if consistency_group_link in disk.resource_policies]
    
    

###  REST 

View the disks in a consistency group by using a query filter with one of the following methods:

  * View zonal disks in a consistency group using the [`disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/disks?filter=resourcePolicies%3DCONSISTENCY_GROUP_NAME
        

  * View regional disks in a consistency group using the [`regionDisks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/get):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/disks?filter=resourcePolicies%3DCONSISTENCY_GROUP_NAME
        




Replace the following:

  * `PROJECT`: the project that contains the consistency group
  * `ZONE`: the zone of the disks in the consistency group
  * `REGION`: the region of the disks in the consistency group
  * `CONSISTENCY_GROUP_NAME`: the name of the consistency group



## Add a disk to a consistency group

To add primary disks to a consistency group, you must add the disks to the consistency group before you start replication. You can add secondary disks to a consistency group at any time. To enable Asynchronous Replication for the disks in a consistency group, all the disks must be in the same zone, for zonal disks, or in the same pair of zones, for regional disks.

Add a disk to a consistency group using the Google Cloud console, the Google Cloud CLI, REST, or Terraform.

###  Console 

Add disks to a consistency group by doing the following:

  1. In the Google Cloud console, go to the **Consistency Groups** page.

[Go to Consistency Groups](https://console.cloud.google.com/compute/consistencyGroups)

  2. Click the **Disk consistency groups** tab.

  3. Click the name of the consistency group that you want to add disks to. The **Manage consistency group** page opens.

  4. Click **Assign disks**. The **Assign disks** page opens.

  5. Select the disks that you want to add to the consistency group.

  6. Click **Assign disks**. When prompted, click **Add**.




###  gcloud 

Add a disk to a consistency group using the [`gcloud compute disks add-resource-policies`command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/add-resource-policies):
    
    
    gcloud compute disks add-resource-policies DISK_NAME \
        --LOCATION_FLAG=LOCATION \
        --resource-policies=CONSISTENCY_GROUP
    

Replace the following:

  * `DISK_NAME`: the name of the disk to add to the consistency group.
  * `LOCATION_FLAG`: the location flag for the disk. For a regional disk, use `--region`. For a zonal disk, use `--zone`.
  * `LOCATION`: the region or zone of the disk. For regional disks, use the region. For zonal disks, use the zone.
  * `CONSISTENCY_GROUP`: the URL of the consistency group. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // addDiskConsistencyGroup adds a disk to a consistency group for a project in a given region.
    func addDiskConsistencyGroup(w io.Writer, projectID, region, groupName, diskName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-west4"
    	// diskName := "your_disk_name"
    	// groupName := "your_group_name"
    
    	ctx := context.Background()
    	disksClient, err := compute.NewRegionDisksRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	consistencyGroupUrl := fmt.Sprintf("projects/%s/regions/%s/resourcePolicies/%s", projectID, region, groupName)
    
    	req := &computepb.AddResourcePoliciesRegionDiskRequest{
    		Project: projectID,
    		Disk:    diskName,
    		RegionDisksAddResourcePoliciesRequestResource: &computepb.RegionDisksAddResourcePoliciesRequest{
    			ResourcePolicies: []string{consistencyGroupUrl},
    		},
    		Region: region,
    	}
    
    	op, err := disksClient.AddResourcePolicies(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to add disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk added\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.AddResourcePoliciesDiskRequest;
    import com.google.cloud.compute.v1.AddResourcePoliciesRegionDiskRequest;
    import com.google.cloud.compute.v1.DisksAddResourcePoliciesRequest;
    import com.google.cloud.compute.v1.DisksClient;
    import com.google.cloud.compute.v1.Operation;
    import com.google.cloud.compute.v1.Operation.Status;
    import com.google.cloud.compute.v1.RegionDisksAddResourcePoliciesRequest;
    import com.google.cloud.compute.v1.RegionDisksClient;
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class AddDiskToConsistencyGroup {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project that contains the disk.
        String project = "YOUR_PROJECT_ID";
        // Zone or region of the disk.
        String location = "us-central1";
        // Name of the disk.
        String diskName = "DISK_NAME";
        // Name of the consistency group.
        String consistencyGroupName = "CONSISTENCY_GROUP";
        // Region of the consistency group.
        String consistencyGroupLocation = "us-central1";
    
        addDiskToConsistencyGroup(
            project, location, diskName, consistencyGroupName, consistencyGroupLocation);
      }
    
      // Adds a disk to a consistency group.
      public static Status addDiskToConsistencyGroup(
          String project, String location, String diskName,
          String consistencyGroupName, String consistencyGroupLocation)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        String consistencyGroupUrl = String.format(
            "https://www.googleapis.com/compute/v1/projects/%s/regions/%s/resourcePolicies/%s",
            project, consistencyGroupLocation, consistencyGroupName);
        Operation response;
        if (Character.isDigit(location.charAt(location.length() - 1))) {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try (RegionDisksClient disksClient = RegionDisksClient.create()) {
            AddResourcePoliciesRegionDiskRequest request =
                    AddResourcePoliciesRegionDiskRequest.newBuilder()
                        .setDisk(diskName)
                        .setRegion(location)
                        .setProject(project)
                        .setRegionDisksAddResourcePoliciesRequestResource(
                                RegionDisksAddResourcePoliciesRequest.newBuilder()
                                    .addAllResourcePolicies(Arrays.asList(consistencyGroupUrl))
                                    .build())
                        .build();
            response = disksClient.addResourcePoliciesAsync(request).get(1, TimeUnit.MINUTES);
          }
        } else {
          try (DisksClient disksClient = DisksClient.create()) {
            AddResourcePoliciesDiskRequest request =
                    AddResourcePoliciesDiskRequest.newBuilder()
                        .setDisk(diskName)
                        .setZone(location)
                        .setProject(project)
                        .setDisksAddResourcePoliciesRequestResource(
                                DisksAddResourcePoliciesRequest.newBuilder()
                                    .addAllResourcePolicies(Arrays.asList(consistencyGroupUrl))
                                    .build())
                        .build();
            response = disksClient.addResourcePoliciesAsync(request).get(1, TimeUnit.MINUTES);
          }
        }
        if (response.hasError()) {
          throw new Error("Error adding disk to consistency group! " + response.getError());
        }
        return response.getStatus();
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // If you want to add regional disk,
    // you should use: RegionDisksClient and RegionOperationsClient.
    // Instantiate a disksClient
    const disksClient = new computeLib.DisksClient();
    // Instantiate a zone
    const zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the disk.
    const projectId = await disksClient.getProjectId();
    
    // The name of the disk.
    // diskName = 'disk-name';
    
    // If you use RegionDisksClient- define region, if DisksClient- define zone.
    // The zone or region of the disk.
    // diskLocation = 'europe-central2-a';
    
    // The name of the consistency group.
    // consistencyGroupName = 'consistency-group-name';
    
    // The region of the consistency group.
    // consistencyGroupLocation = 'europe-central2';
    
    async function callAddDiskToConsistencyGroup() {
      const [response] = await disksClient.addResourcePolicies({
        disk: diskName,
        project: projectId,
        // If you use RegionDisksClient, pass region as an argument instead of zone.
        zone: diskLocation,
        disksAddResourcePoliciesRequestResource:
          new compute.DisksAddResourcePoliciesRequest({
            resourcePolicies: [
              `https://www.googleapis.com/compute/v1/projects/${projectId}/regions/${consistencyGroupLocation}/resourcePolicies/${consistencyGroupName}`,
            ],
          }),
      });
    
      let operation = response.latestResponse;
    
      // Wait for the add disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          // If you use RegionDisksClient, pass region as an argument instead of zone.
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(
        `Disk: ${diskName} added to consistency group: ${consistencyGroupName}.`
      );
    }
    
    await callAddDiskToConsistencyGroup();

###  Python 
    
    
    from google.cloud import compute_v1
    
    
    def add_disk_consistency_group(
        project_id: str,
        disk_name: str,
        disk_location: str,
        consistency_group_name: str,
        consistency_group_region: str,
    ) -> None:
        """Adds a disk to a specified consistency group.
        Args:
            project_id (str): The ID of the Google Cloud project.
            disk_name (str): The name of the disk to be added.
            disk_location (str): The region or zone of the disk
            consistency_group_name (str): The name of the consistency group.
            consistency_group_region (str): The region of the consistency group.
        Returns:
            None
        """
        consistency_group_link = (
            f"regions/{consistency_group_region}/resourcePolicies/{consistency_group_name}"
        )
    
        # Checking if the disk is zonal or regional
        # If the final character of the disk_location is a digit, it is a regional disk
        if disk_location[-1].isdigit():
            policy = compute_v1.RegionDisksAddResourcePoliciesRequest(
                resource_policies=[consistency_group_link]
            )
            disk_client = compute_v1.RegionDisksClient()
            disk_client.add_resource_policies(
                project=project_id,
                region=disk_location,
                disk=disk_name,
                region_disks_add_resource_policies_request_resource=policy,
            )
        # For zonal disks we use DisksClient
        else:
            print("Using DisksClient")
            policy = compute_v1.DisksAddResourcePoliciesRequest(
                resource_policies=[consistency_group_link]
            )
            disk_client = compute_v1.DisksClient()
            disk_client.add_resource_policies(
                project=project_id,
                zone=disk_location,
                disk=disk_name,
                disks_add_resource_policies_request_resource=policy,
            )
    
        print(f"Disk {disk_name} added to consistency group {consistency_group_name}")
    
    

###  REST 

Add disks to a consistency group using one of the following methods:

  * Add zonal disks to a consistency group using the [`disks.addResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/addResourcePolicies):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/LOCATION/disks/DISK_NAME/addResourcePolicies
        
        {
        "resourcePolicies": "CONSISTENCY_GROUP"
        }
        

  * Add regional disks to a consistency group using the [`regionDisks.addResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/addResourcePolicies):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/LOCATION/disks/DISK_NAME/addResourcePolicies
        
        {
        "resourcePolicies": "CONSISTENCY_GROUP"
        }
        




Replace the following:

  * `PROJECT`: the project that contains the disk.
  * `LOCATION`: the zone or region of the disk. For zonal disks, use the zone. For regional disks, use the region.
  * `DISK_NAME`: the name of the disk to add to the consistency group.
  * `CONSISTENCY_GROUP`: the URL of the consistency group. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.



###  Terraform 

To add the disk to the consistency group, use the [`compute_disk_resource_policy_attachment` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk_resource_policy_attachment).

  * In case of Regional disk specify region in place of zone.
        
        resource "google_compute_disk_resource_policy_attachment" "default" {
          name = google_compute_resource_policy.default.name
          disk = google_compute_disk.default.name
          zone = "us-central1-a"
        }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).




## Remove a disk from a consistency group

Before you can remove a disk from a consistency group, you must [stop replication for the disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#stop_replication_for_a_single_disk).

Remove a disk from a consistency group using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

Remove primary disks from a consistency group by doing the following:

  1. In the Google Cloud console, go to the **Consistency Groups** page.

[Go to Consistency Groups](https://console.cloud.google.com/compute/consistencyGroups)

  2. Click the **Disk consistency groups** tab.

  3. Click the name of the consistency group that you want to add disks to. The **Manage consistency group** page opens.

  4. In the **Consistency group members** section, select the disks that you want to remove from the consistency group.

  5. Click **Remove disks**. When prompted, click **Remove**.




###  gcloud 

Remove a disk from a consistency group using the [`gcloud compute disks remove-resource-policies` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/remove-resource-policies):
    
    
    gcloud compute disks remove-resource-policies DISK_NAME \
        --LOCATION_FLAG=LOCATION \
        --resource-policies=CONSISTENCY_GROUP
    

Replace the following:

  * `DISK_NAME`: the name of the disk to remove from the consistency group.
  * `LOCATION_FLAG`: the location flag for the disk. For a regional disk, use `--region`. For a zonal disk, use `--zone`.
  * `LOCATION`: the region or zone of the disk. For regional disks, use the region. For zonal disks, use the zone.
  * `CONSISTENCY_GROUP`: the URL of the consistency group. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // removeDiskConsistencyGroup removes a disk from consistency group for a project in a given region.
    func removeDiskConsistencyGroup(w io.Writer, projectID, region, groupName, diskName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-west4"
    	// diskName := "your_disk_name"
    	// groupName := "your_group_name"
    
    	ctx := context.Background()
    	disksClient, err := compute.NewRegionDisksRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	consistencyGroupUrl := fmt.Sprintf("projects/%s/regions/%s/resourcePolicies/%s", projectID, region, groupName)
    
    	req := &computepb.RemoveResourcePoliciesRegionDiskRequest{
    		Project: projectID,
    		Disk:    diskName,
    		RegionDisksRemoveResourcePoliciesRequestResource: &computepb.RegionDisksRemoveResourcePoliciesRequest{
    			ResourcePolicies: []string{consistencyGroupUrl},
    		},
    		Region: region,
    	}
    
    	op, err := disksClient.RemoveResourcePolicies(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to remove disk: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk removed\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.DisksClient;
    import com.google.cloud.compute.v1.DisksRemoveResourcePoliciesRequest;
    import com.google.cloud.compute.v1.Operation;
    import com.google.cloud.compute.v1.Operation.Status;
    import com.google.cloud.compute.v1.RegionDisksClient;
    import com.google.cloud.compute.v1.RegionDisksRemoveResourcePoliciesRequest;
    import com.google.cloud.compute.v1.RemoveResourcePoliciesDiskRequest;
    import com.google.cloud.compute.v1.RemoveResourcePoliciesRegionDiskRequest;
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class RemoveDiskFromConsistencyGroup {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project that contains the disk.
        String project = "YOUR_PROJECT_ID";
        // Zone or region of the disk.
        String location = "us-central1";
        // Name of the disk.
        String diskName = "DISK_NAME";
        // Name of the consistency group.
        String consistencyGroupName = "CONSISTENCY_GROUP";
        // Region of the consistency group.
        String consistencyGroupLocation = "us-central1";
    
        removeDiskFromConsistencyGroup(
            project, location, diskName, consistencyGroupName, consistencyGroupLocation);
      }
    
      // Removes a disk from a consistency group.
      public static Status removeDiskFromConsistencyGroup(
          String project, String location, String diskName,
          String consistencyGroupName, String consistencyGroupLocation)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        String consistencyGroupUrl = String.format(
            "https://www.googleapis.com/compute/v1/projects/%s/regions/%s/resourcePolicies/%s",
            project, consistencyGroupLocation, consistencyGroupName);
        Operation response;
        if (Character.isDigit(location.charAt(location.length() - 1))) {
          // Initialize client that will be used to send requests. This client only needs to be created
          // once, and can be reused for multiple requests.
          try (RegionDisksClient disksClient = RegionDisksClient.create()) {
            RemoveResourcePoliciesRegionDiskRequest request =
                RemoveResourcePoliciesRegionDiskRequest.newBuilder()
                    .setDisk(diskName)
                    .setRegion(location)
                    .setProject(project)
                    .setRegionDisksRemoveResourcePoliciesRequestResource(
                        RegionDisksRemoveResourcePoliciesRequest.newBuilder()
                            .addAllResourcePolicies(Arrays.asList(consistencyGroupUrl))
                            .build())
                    .build();
    
            response = disksClient.removeResourcePoliciesAsync(request).get(1, TimeUnit.MINUTES);
          }
        } else {
          try (DisksClient disksClient = DisksClient.create()) {
            RemoveResourcePoliciesDiskRequest request =
                RemoveResourcePoliciesDiskRequest.newBuilder()
                    .setDisk(diskName)
                    .setZone(location)
                    .setProject(project)
                    .setDisksRemoveResourcePoliciesRequestResource(
                        DisksRemoveResourcePoliciesRequest.newBuilder()
                            .addAllResourcePolicies(Arrays.asList(consistencyGroupUrl))
                            .build())
                    .build();
            response = disksClient.removeResourcePoliciesAsync(request).get(1, TimeUnit.MINUTES);
          }
        }
        if (response.hasError()) {
          throw new Error("Error removing disk from consistency group! " + response.getError());
        }
        return response.getStatus();
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // If you want to remove regional disk,
    // you should use: RegionDisksClient and RegionOperationsClient.
    // Instantiate a disksClient
    const disksClient = new computeLib.DisksClient();
    // Instantiate a zone
    const zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the disk.
    const projectId = await disksClient.getProjectId();
    
    // The name of the disk.
    // diskName = 'disk-name';
    
    // If you use RegionDisksClient- define region, if DisksClient- define zone.
    // The zone or region of the disk.
    // diskLocation = 'europe-central2-a';
    
    // The name of the consistency group.
    // consistencyGroupName = 'consistency-group-name';
    
    // The region of the consistency group.
    // consistencyGroupLocation = 'europe-central2';
    
    async function callDeleteDiskFromConsistencyGroup() {
      const [response] = await disksClient.removeResourcePolicies({
        disk: diskName,
        project: projectId,
        // If you use RegionDisksClient, pass region as an argument instead of zone.
        zone: diskLocation,
        disksRemoveResourcePoliciesRequestResource:
          new compute.DisksRemoveResourcePoliciesRequest({
            resourcePolicies: [
              `https://www.googleapis.com/compute/v1/projects/${projectId}/regions/${consistencyGroupLocation}/resourcePolicies/${consistencyGroupName}`,
            ],
          }),
      });
    
      let operation = response.latestResponse;
    
      // Wait for the delete disk operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          // If you use RegionDisksClient, pass region as an argument instead of zone.
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(
        `Disk: ${diskName} deleted from consistency group: ${consistencyGroupName}.`
      );
    }
    
    await callDeleteDiskFromConsistencyGroup();

###  Python 
    
    
    from google.cloud import compute_v1
    
    
    def remove_disk_consistency_group(
        project_id: str,
        disk_name: str,
        disk_location: str,
        consistency_group_name: str,
        consistency_group_region: str,
    ) -> None:
        """Removes a disk from a specified consistency group.
        Args:
            project_id (str): The ID of the Google Cloud project.
            disk_name (str): The name of the disk to be deleted.
            disk_location (str): The region or zone of the disk
            consistency_group_name (str): The name of the consistency group.
            consistency_group_region (str): The region of the consistency group.
        Returns:
            None
        """
        consistency_group_link = (
            f"regions/{consistency_group_region}/resourcePolicies/{consistency_group_name}"
        )
        # Checking if the disk is zonal or regional
        # If the final character of the disk_location is a digit, it is a regional disk
        if disk_location[-1].isdigit():
            policy = compute_v1.RegionDisksRemoveResourcePoliciesRequest(
                resource_policies=[consistency_group_link]
            )
            disk_client = compute_v1.RegionDisksClient()
            disk_client.remove_resource_policies(
                project=project_id,
                region=disk_location,
                disk=disk_name,
                region_disks_remove_resource_policies_request_resource=policy,
            )
        # For zonal disks we use DisksClient
        else:
            policy = compute_v1.DisksRemoveResourcePoliciesRequest(
                resource_policies=[consistency_group_link]
            )
            disk_client = compute_v1.DisksClient()
            disk_client.remove_resource_policies(
                project=project_id,
                zone=disk_location,
                disk=disk_name,
                disks_remove_resource_policies_request_resource=policy,
            )
    
        print(f"Disk {disk_name} removed from consistency group {consistency_group_name}")
    
    

###  REST 

Remove a disk from a consistency group using the [`disks.removeResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/removeResourcePolicies) for zonal disks, or the [`regionDisks.removeResourcePolicies` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/removeResourcePolicies) for regional disks.

  * Remove a zonal disk from a consistency group:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/LOCATION/disks/DISK_NAME/removeResourcePolicies
        
        {
        "resourcePolicies": "CONSISTENCY_GROUP"
        }
        

  * Remove a regional disk from a consistency group:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/LOCATION/disks/DISK_NAME/removeResourcePolicies
        
        {
        "resourcePolicies": "CONSISTENCY_GROUP"
        }
        




Replace the following:

  * `PROJECT`: the project that contains the disk.
  * `LOCATION`: the zone or region of the disk. For zonal disks, use the zone. For regional disks, use the region.
  * `DISK_NAME`: the name of the disk to remove from the consistency group.
  * `CONSISTENCY_GROUP`: the URL of the consistency group. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.



## Delete a consistency group

Delete a consistency group using the Google Cloud console, the Google Cloud CLI, or REST.

###  Console 

Delete a consistency by doing the following:

  1. In the Google Cloud console, go to the **Consistency Groups** page.

[Go to Consistency Groups](https://console.cloud.google.com/compute/consistencyGroups)

  2. Click the **Disk consistency groups** tab.

  3. Select the consistency group that you want to delete.

  4. Click **Delete**. The **Delete consistency group** window opens.

  5. Click **Delete**.




###  gcloud 

Delete the resource policy using the [`gcloud compute resource-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/delete):
    
    
    gcloud compute resource-policies delete CONSISTENCY_GROUP \
        --region=REGION
    

Replace the following:

  * `CONSISTENCY_GROUP`: the name of the consistency group
  * `REGION`: the region of the consistency group



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // deleteConsistencyGroup deletes consistency group for a project in a given region.
    func deleteConsistencyGroup(w io.Writer, projectID, region, groupName string) error {
    	// projectID := "your_project_id"
    	// region := "europe-west4"
    	// groupName := "your_group_name"
    
    	ctx := context.Background()
    	disksClient, err := compute.NewResourcePoliciesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewResourcePoliciesRESTClient: %w", err)
    	}
    	defer disksClient.Close()
    
    	req := &computepb.DeleteResourcePolicyRequest{
    		Project:        projectID,
    		ResourcePolicy: groupName,
    		Region:         region,
    	}
    
    	op, err := disksClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete group: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Group deleted\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.Operation;
    import com.google.cloud.compute.v1.Operation.Status;
    import com.google.cloud.compute.v1.ResourcePoliciesClient;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteConsistencyGroup {
    
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String project = "YOUR_PROJECT_ID";
        // Region in which your consistency group is located.
        String region = "us-central1";
        // Name of the consistency group you want to delete.
        String consistencyGroupName = "YOUR_CONSISTENCY_GROUP_NAME";
    
        deleteConsistencyGroup(project, region, consistencyGroupName);
      }
    
      // Deletes a consistency group resource policy in the specified project and region.
      public static Status deleteConsistencyGroup(
          String project, String region, String consistencyGroupName)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try (ResourcePoliciesClient resourcePoliciesClient = ResourcePoliciesClient.create()) {
          Operation response = resourcePoliciesClient
              .deleteAsync(project, region, consistencyGroupName).get(1, TimeUnit.MINUTES);
    
          if (response.hasError()) {
            throw new Error("Error deleting disk! " + response.getError());
          }
          return response.getStatus();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('@google-cloud/compute');
    
    // Instantiate a resourcePoliciesClient
    const resourcePoliciesClient = new computeLib.ResourcePoliciesClient();
    // Instantiate a regionOperationsClient
    const regionOperationsClient = new computeLib.RegionOperationsClient();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The project that contains the consistency group.
    const projectId = await resourcePoliciesClient.getProjectId();
    
    // The region of the consistency group.
    // region = 'europe-central2';
    
    // The name of the consistency group.
    // consistencyGroupName = 'consistency-group-name';
    
    async function callDeleteConsistencyGroup() {
      // Delete a resourcePolicyResource
      const [response] = await resourcePoliciesClient.delete({
        project: projectId,
        region,
        resourcePolicy: consistencyGroupName,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the delete group operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await regionOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          region,
        });
      }
    
      console.log(`Consistency group: ${consistencyGroupName} deleted.`);
    }
    
    await callDeleteConsistencyGroup();
    

###  Python 
    
    
    from __future__ import annotations
    
    import sys
    from typing import Any
    
    from google.api_core.extended_operation import ExtendedOperation
    from google.cloud import compute_v1
    
    
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
    
    
    def delete_consistency_group(project_id: str, region: str, group_name: str) -> None:
        """
        Deletes a consistency group in Google Cloud Compute Engine.
        Args:
            project_id (str): The ID of the Google Cloud project.
            region (str): The region where the consistency group is located.
            group_name (str): The name of the consistency group to delete.
        Returns:
            None
        """
    
        # Initialize the ResourcePoliciesClient
        client = compute_v1.ResourcePoliciesClient()
    
        # Delete the (consistency group) from the specified project and region
        operation = client.delete(
            project=project_id,
            region=region,
            resource_policy=group_name,
        )
        wait_for_extended_operation(operation, "Consistency group deletion")
    
    

###  REST 

Delete a consistency using the [`resourcePolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME
    

Replace the following:

  * `PROJECT`: the project that contains the consistency group
  * `REGION`: the region of the consistency group
  * `CONSISTENCY_GROUP`: the name of the consistency group



## What's next

  * Learn how to [manage disks that use Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-async-disks).
  * Learn how to [failover and failback](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback).
  * Learn how to [monitor Asynchronous Replication performance](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
