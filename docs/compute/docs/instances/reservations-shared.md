---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-shared/
title: Create a shared reservation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:23.641445+00:00
---

# Create a shared reservation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-shared/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a shared reservation Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create shared reservations, which are reservations shared across multiple projects, and manage which projects in your organization can consume the shared reservations.

A shared reservation can be used by the project that hosts the reservation (owner project) and by the projects the reservation is shared with (consumer projects). Use shared reservations if your organization has multiple projects that need virtual machine (VM) instances with the same properties reserved. By using shared reservations, you can improve the utilization of your reservations and reduce the number of reservations that you need to create and manage. To learn more about reservations, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

For other methods of creating reservations, see instead the following pages:

  * To create a reservation that can only be used by a single project, see [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project).

  * To create a reservation when purchasing a resource-based commitment, see [Purchase hardware commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations). Commitments provide discounts, known as committed use discounts (CUDs), on your on-demand resource costs in exchange for purchasing a minimum level of resources or for spending a minimum amount.


**Note:** After you create a reservation, it incurs charges for its reserved resources, even when it's not being consumed, until you delete it. For more information, see [Billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

## Before you begin

  * Review the [best practices for shared reservations](https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations).
  * Review the [ quota requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-shared-reservations) and [ restrictions](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions-shared-reservations) for shared reservations.
  * Verify that the project you use to create shared reservations has been added to the allowlist for the **Shared reservations owner projects** (`compute.sharedReservationsOwnerProjects`) organization policy constraint by an organization policy administrator. This allowlist is empty by default, so you can't create shared reservations until your organization grants this permission to one or more projects. For more details on viewing and editing the organization policy constraint, see [Manage shared reservations creation](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).
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




### Required roles

To get the permissions that you need to create shared reservations, ask your administrator to grant you the following IAM roles: 

  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project
  * To view and edit organization policies: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create shared reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create shared reservations:

  * `compute.reservations.create` on the project
  * To view organization policies: `orgpolicy.policy.get` on the organization 
  * To edit organization policies: `orgpolicy.policy.set` on the organization 
  * To specify an instance template: `compute.instanceTemplates.useReadOnly` on the instance template 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a shared reservation

This section explains how to create shared reservations. After you create a shared reservation, it can be modified only by the owner project, but the resources for a shared reservation can be consumed by the owner project or any consumer projects.

To consume a reservation, a VM must have [properties that _exactly_ match](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) that reservation. To specify the properties of the VMs that you want to reserve, select one of the following sections in this document:

  * Recommended: Specify an instance template

This section explains how to use an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to define the properties of a shared reservation. By using an instance template, you can define the properties of a reservation and the VMs that can consume the reservation in the same place. However, because templates are project-specific, you can't use the same template to create VMs that can consume the reservation outside of the project that created the reservation. For the projects the reservation is shared with, you must create similar templates in those projects or create VMs by specifying properties directly.

  * Specify an existing VM

This section explains how to use an existing VM to define the properties of a reservation. By using the properties of an existing VM, you can consume the reservation by creating VMs with properties that match the reference VM.

  * Specify properties directly

This section explains how to directly define the properties of a shared reservation. This method requires you to manually ensure that the properties of your VMs and reservations match _exactly_ —any [mismatched properties prevent consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption#mismatched-vm-properties). 




By default, a reservation can be automatically consumed by any VMs with properties that match it. If you want to control reservation consumption, do one or more of the following:

  * Create a reservation that can only be consumed by VMs that specifically target it, as explained in the following sections in this document. Then, [configure VMs to consume that specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * [Configure VMs to not consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption).




### Specify an instance template

Before creating a reservation by specifying an instance template, make sure of the following:

  * An instance template contains project-specific settings, so you can only access and use an instance template within the same project. If you create a shared reservation by specifying an instance template, then you can't use the same template to create VMs that can consume the reservation outside of the project that created the reservation.

  * Create your reservation in the same region and zone as the resources within the instance template. Any [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) specified in an instance template—such as a machine type or a Persistent Disk volume—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk volume in zone `us-central1-a`, then you can only create your reservation in the same zone. To check if an existing template specifies any resources that bind the template to a specific region or zone, [view the details of the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.




To create a shared reservation by specifying an instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select where you want to reserve resources.

  5. In the **Share type** section, do the following:

     1. To share a reservation with other projects, select **Shared**.

     2. Click add **Add projects** , and then select the projects from the current project's organization that you want to share the reservation with. You can select up to 100 consumer projects.

  6. Optional: To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, in the **Google Cloud services** section, select **Share reservation**.

  7. In the **Use with VM instance** section, select one of the following options:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically**.

     * To consume this reservation's resources only when you create matching VMs that specifically target the reservation by name, select **Select specific reservation**.

  8. In the **Resource details** section, do the following:

     * In the **Number of VM instances** field, enter the number of VMs that you want to reserve.

     * To specify VM configurations by using an instance template, select **Use instance template** , and then, in the list that appears, select the instance template.

  9. In the **Auto-delete** section, you can enable the auto-delete option to let Compute Engine automatically delete the reservation at a specific date and time. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  10. To create the reservation, click **Create**. The **Reservations** page appears. Creating the reservation can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).




###  gcloud 

To create a shared reservation, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) with the `--share-setting=projects` and `--share-with` flags.

To create a shared reservation by specifying an instance template and without including any optional flags, run the following command:
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --share-setting=projects \
        --share-with=CONSUMER_PROJECT_IDS \
        --source-instance-template=INSTANCE_TEMPLATE_URL \
        --vm-count=NUMBER_OF_VMS \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `PROJECT_ID`: the ID of the project where you want to reserve resources and where the instance template exists.

  * `CONSUMER_PROJECT_IDS`: a comma-separated list of [IDs of projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that can consume this reservation—for example, `project-1,project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the owner project. By default, it's already allowed to consume the reservation.

  * `INSTANCE_TEMPLATE_URL`: the URL of an existing instance template, which must exist in your project. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `ZONE`: the zone in which to reserve resources.




For example, to create a reservation by specifying a global instance template in zone `us-central1-a`, share the reservation with projects `project-1` and `project-2`, and reserve ten VMs that each use an N2 predefined machine type with 4 vCPUs, run the following command:
    
    
    gcloud compute reservations create my-reservation \
        --share-setting=projects \
        --share-with=project-1,project-2 \
        --source-instance-template=projects/example-project/global/example-instance-template \
        --vm-count=10 \
        --zone=us-central1-a
    

Optionally, you can do one or more of the following:

  * To specify that only VMs that specifically target this reservation can consume it, include the `--require-specific-reservation` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            **--require-specific-reservation** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --source-instance-template=INSTANCE_TEMPLATE_URL \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, include the `--reservation-sharing-policy` flag set to `ALLOW_ALL`.
        
        gcloud compute reservations create RESERVATION_NAME \
            **--reservation-sharing-policy=ALLOW_ALL** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --source-instance-template=INSTANCE_TEMPLATE_URL \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`--delete-at-time` and `--delete-after-duration` flags **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-at-time` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-at-time= DELETE_AT_TIME** \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --source-instance-template=INSTANCE_TEMPLATE_URL \
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AT_TIME` with a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be as follows:
          
          YYYY-MM-DDTHH:MM:SSOFFSET
          

Replace the following:

      * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

      * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

      * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

    * To delete the reservation after a specific duration, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-after-duration` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-after-duration= DELETE_AFTER_DURATION** \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --source-instance-template=INSTANCE_TEMPLATE_URL \
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AFTER_DURATION` with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // Creates shared reservation from given template in particular zone
    func createSharedReservation(w io.Writer, client ClientInterface, projectID, baseProjectId, zone, reservationName, sourceTemplate string) error {
    	// client, err := compute.NewReservationsRESTClient(ctx)
    	// projectID := "your_project_id". Destination of sharing.
    	// baseProjectId := "your_project_id2". Project where the reservation will be created.
    	// zone := "us-west3-a"
    	// reservationName := "your_reservation_name"
    	// sourceTemplate: existing template path. Following formats are allowed:
    	//  	- projects/{project_id}/global/instanceTemplates/{template_name}
    	//  	- projects/{project_id}/regions/{region}/instanceTemplates/{template_name}
    	//  	- https://www.googleapis.com/compute/v1/projects/{project_id}/global/instanceTemplates/instanceTemplate
    	//  	- https://www.googleapis.com/compute/v1/projects/{project_id}/regions/{region}/instanceTemplates/instanceTemplate
    
    	ctx := context.Background()
    
    	shareSettings := map[string]*computepb.[ShareSettingsProjectConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_ShareSettingsProjectConfig){
    		projectID: {ProjectId: proto.String(projectID)},
    	}
    
    	req := &computepb.[InsertReservationRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_InsertReservationRequest){
    		Project: baseProjectId,
    		ReservationResource: &computepb.[Reservation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_Reservation){
    			Name: proto.String(reservationName),
    			Zone: proto.String(zone),
    			SpecificReservation: &computepb.[AllocationSpecificSKUReservation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_AllocationSpecificSKUReservation){
    				Count:                  proto.Int64(2),
    				SourceInstanceTemplate: proto.String(sourceTemplate),
    			},
    			ShareSettings: &computepb.[ShareSettings](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_ShareSettings){
    				ProjectMap: shareSettings,
    				ShareType:  proto.String("SPECIFIC_PROJECTS"),
    			},
    		},
    		Zone: zone,
    	}
    
    	op, err := client.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create reservation: %w", err)
    	}
    
    	if op != nil {
    		if err = op.Wait(ctx); err != nil {
    			return fmt.Errorf("unable to wait for the operation: %w", err)
    		}
    	}
    
    	fmt.Fprintf(w, "Reservation created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AllocationSpecificSKUReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUReservation.html);
    import com.google.cloud.compute.v1.[InsertReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertReservationRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html);
    import com.google.cloud.compute.v1.[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html);
    import com.google.cloud.compute.v1.[ShareSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettings.html);
    import com.google.cloud.compute.v1.[ShareSettingsProjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettingsProjectConfig.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateSharedReservation {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // The ID of the project where you want to reserve resources
        // and where the instance template exists.
        // By default, no projects are allowed to create or modify shared reservations
        // in an organization. Add projects to the Shared Reservations Owner Projects
        // (compute.sharedReservationsOwnerProjects) organization policy constraint
        // to allow them to create and modify shared reservations.
        // For more information visit this page:
        // https://cloud.google.com/compute/docs/instances/reservations-shared#shared_reservation_constraint
        String projectId = "YOUR_PROJECT_ID";
        // Zone in which to reserve resources.
        String zone = "us-central1-a";
        // Name of the reservation to be created.
        String reservationName = "YOUR_RESERVATION_NAME";
        // The URI of the global instance template to be used for creating the reservation.
        String instanceTemplateUri = String.format(
            "projects/%s/global/instanceTemplates/%s", projectId, "YOUR_INSTANCE_TEMPLATE_NAME");
        // Number of instances for which capacity needs to be reserved.
        int vmCount = 3;
    
        createSharedReservation(projectId, zone, reservationName, instanceTemplateUri, vmCount);
      }
    
      // Creates a shared reservation with the given name in the given zone.
      public static [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html) createSharedReservation(
              String projectId, String zone,
              String reservationName, String instanceTemplateUri, int vmCount)
              throws ExecutionException, InterruptedException, TimeoutException, IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html) reservationsClient = [ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html).create()) {
          [ShareSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettings.html) shareSettings = [ShareSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettings.html).newBuilder()
                  .[setShareType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettings.Builder.html#com_google_cloud_compute_v1_ShareSettings_Builder_setShareType_java_lang_String_)(String.valueOf([ShareSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettings.html).ShareType.SPECIFIC_PROJECTS))
                  // The IDs of projects that can consume this reservation. You can include up to
                  // 100 consumer projects. These projects must be in the same organization as
                  // the owner project. Don't include the owner project.
                  // By default, it is already allowed to consume the reservation.
                  .putProjectMap("CONSUMER_PROJECT_1", [ShareSettingsProjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettingsProjectConfig.html).newBuilder().build())
                  .putProjectMap("CONSUMER_PROJECT_2", [ShareSettingsProjectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ShareSettingsProjectConfig.html).newBuilder().build())
                  .build();
    
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) reservationResource =
                  [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html).newBuilder()
                          .setName(reservationName)
                          .setZone(zone)
                          .setSpecificReservationRequired(true)
                          .setShareSettings(shareSettings)
                          .[setSpecificReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.Builder.html#com_google_cloud_compute_v1_Reservation_Builder_setSpecificReservation_com_google_cloud_compute_v1_AllocationSpecificSKUReservation_)(
                                  [AllocationSpecificSKUReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUReservation.html).newBuilder()
                                          .setCount(vmCount)
                                          .setSourceInstanceTemplate(instanceTemplateUri)
                                          .build())
                          .build();
    
          [InsertReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertReservationRequest.html) request =
                  [InsertReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertReservationRequest.html).newBuilder()
                          .setProject(projectId)
                          .setZone(zone)
                          .setReservationResource(reservationResource)
                          .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = reservationsClient.insertAsync(request)
                  .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)("Reservation creation failed!!" + response);
          }
          return response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)();
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    /**
     * TODO(developer): Uncomment reservationsClient and zoneOperationsClient before running the sample.
     */
    // Instantiate a reservationsClient
    // reservationsClient = new computeLib.ReservationsClient();
    // Instantiate a zoneOperationsClient
    // zoneOperationsClient = new computeLib.ZoneOperationsClient();
    
    /**
     * TODO(developer): Update these variables before running the sample.
     */
    // The ID of the project where you want to reserve resources and where the instance template exists.
    const projectId = await reservationsClient.getProjectId();
    // The zone in which to reserve resources.
    const zone = 'us-central1-a';
    // The name of the reservation to create.
    const reservationName = 'reservation-01';
    // The number of VMs to reserve.
    const vmsNumber = 3;
    // The name of an existing instance template.
    const instanceTemplateName = 'global-instance-template-name';
    // The location of the instance template.
    const location = 'global';
    
    async function callCreateComputeSharedReservation() {
      // Create reservation for 3 VMs in zone us-central1-a by specifying a instance template.
      const specificReservation = new compute.AllocationSpecificSKUReservation({
        count: vmsNumber,
        sourceInstanceTemplate: `projects/${projectId}/${location}/instanceTemplates/${instanceTemplateName}`,
      });
    
      // Create share settings. Share reservation with one customer project.
      const shareSettings = new compute.ShareSettings({
        shareType: 'SPECIFIC_PROJECTS',
        projectMap: {
          // The IDs of projects that can consume this reservation. You can include up to 100 consumer projects.
          // These projects must be in the same organization as the owner project.
          // Don't include the owner project. By default, it is already allowed to consume the reservation.
          consumer_project_id: {
            projectId: 'consumer_project_id',
          },
        },
      });
    
      // Create a reservation.
      const reservation = new compute.Reservation({
        name: reservationName,
        specificReservation,
        specificReservationRequired: true,
        shareSettings,
      });
    
      const [response] = await reservationsClient.insert({
        project: projectId,
        reservationResource: reservation,
        zone,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the create reservation operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Reservation: ${reservationName} created.`);
      return response;
    }
    
    return await callCreateComputeSharedReservation();

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
    
    
    def create_compute_shared_reservation(
        project_id: str,
        zone: str = "us-central1-a",
        reservation_name="your-reservation-name",
        shared_project_id: str = "shared-project-id",
    ) -> compute_v1.Reservation:
        """Creates a compute reservation in GCP.
        Args:
            project_id (str): The ID of the Google Cloud project.
            zone (str): The zone to create the reservation.
            reservation_name (str): The name of the reservation to create.
            shared_project_id (str): The ID of the project that the reservation is shared with.
        Returns:
            Reservation object that represents the new reservation.
        """
    
        instance_properties = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUAllocationReservedInstanceProperties.html)(
            machine_type="n1-standard-1",
            # Optional. Specifies amount of local ssd to reserve with each instance.
            local_ssds=[
                [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk.html)(
                    disk_size_gb=375, interface="NVME"
                ),
            ],
        )
    
        reservation = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Reservation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Reservation.html)(
            name=reservation_name,
            specific_reservation=[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUReservation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUReservation.html)(
                count=3,  # Number of resources that are allocated.
                # If you use source_instance_template, you must exclude the instance_properties field.
                # It can be a full or partial URL.
                # source_instance_template="projects/[PROJECT_ID]/global/instanceTemplates/my-instance-template",
                instance_properties=instance_properties,
            ),
            share_settings=[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ShareSettings](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ShareSettings.html)(
                share_type="SPECIFIC_PROJECTS",
                project_map={
                    shared_project_id: [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ShareSettingsProjectConfig](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ShareSettingsProjectConfig.html)(
                        project_id=shared_project_id
                    )
                },
            ),
        )
    
        # Create a client
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html)()
    
        operation = client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_insert)(
            project=project_id,
            zone=zone,
            reservation_resource=reservation,
        )
        wait_for_extended_operation(operation, "Reservation creation")
    
        reservation = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_get)(
            project=project_id, zone=zone, reservation=reservation_name
        )
        shared_project = next(iter(reservation.share_settings.project_map.values()))
    
        print("Name: ", reservation.name)
        print("STATUS: ", reservation.status)
        print("SHARED PROJECT: ", shared_project)
        # Example response:
        # Name:  your-reservation-name
        # STATUS:  READY
        # SHARED PROJECT:  project_id: "123456789012"
    
        return reservation
    
    

###  REST 

To create a shared reservation, make a `POST` request to the [`reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/insert). In the request body, include the following:

  * The `projectMap` field.

  * The `shareType` field set to `SPECIFIC_PROJECTS`.




For example, to create a shared reservation by specifying an instance template without including any optional fields, and share the reservation with two consumer projects, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
    
    {
      "name": "RESERVATION_NAME",
      "shareSettings": {
        "shareType": "SPECIFIC_PROJECTS",
        "projectMap": {
          "CONSUMER_PROJECT_ID_1": {
            "projectId": "CONSUMER_PROJECT_ID_1"
          },
          "CONSUMER_PROJECT_ID_2": {
            "projectId": "CONSUMER_PROJECT_ID_2"
          }
        }
      },
      "specificReservation": {
        "count": "NUMBER_OF_VMS",
        "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to reserve resources and where the instance template exists.

  * `ZONE`: the zone in which to reserve resources.

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: the [IDs of projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that can consume this reservation. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the owner project. By default, it is already allowed to consume the reservation.

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `INSTANCE_TEMPLATE_URL`: the URL of an existing instance template, which must exist in your project. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`




For example, to create a reservation for ten VMs in zone `us-central1-a` by specifying a global instance template, and share the reservation with projects `project-1` and `project-2`, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations
    
    {
      "name": "my-reservation",
      "shareSettings": {
        "shareType": "SPECIFIC_PROJECTS",
        "projectMap": {
          "project-1": {
            "projectId": "project-1"
          },
          "project-2": {
            "projectId": "project-2"
          }
        }
      },
      "specificReservation": {
        "count": "10",
        "sourceInstanceTemplate": "example-instance-template"
      }
    }
    

Optionally, you can do one or more of the following:

  * To specify that only VMs that specifically target this reservation can consume it, include the `specificReservationRequired` field in the request body, and set the field to `true`.

For example, to create a specific reservation by specifying an instance template, and share the reservation with two consumer projects, make a request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
          },
          **"specificReservationRequired": true**
        }
        

  * To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, include the `serviceShareType` field and set it to `ALLOW_ALL`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          **"reservationSharingPolicy": {
            "serviceShareType": "ALLOW_ALL"
          }** ,
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
          }
        }
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`deleteAtTime` and `deleteAfterDuration` fields **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, make a `POST` request to the [`beta.reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/insert). In the request body, include the `deleteAtTime` field.

For example, to create a reservation by specifying an instance template, auto delete the reservation at a specific date and time, and share the reservation with two consumer projects, make a request as follows:
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAtTime": " DELETE_AT_TIME"**,
            "name": "RESERVATION_NAME",
            "shareSettings": {
              "shareType": "SPECIFIC_PROJECTS",
              "projectMap": {
                "CONSUMER_PROJECT_ID_1": {
                  "projectId": "CONSUMER_PROJECT_ID_1"
                },
                "CONSUMER_PROJECT_ID_2": {
                  "projectId": "CONSUMER_PROJECT_ID_2"
                }
              }
            },
            "specificReservation": {
              "count": "NUMBER_OF_VMS",
              "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          }
          

Replace `DELETE_AT_TIME` with a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be as follows:
          
          YYYY-MM-DDTHH:MM:SSOFFSET
          

Replace the following:

      * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

      * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

      * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

    * To delete the reservation after a specific duration, make a `POST` request to the [`beta.reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/insert). In the request body, include the `deleteAfterDuration` field.

For example, to create a reservation by specifying an instance template, auto delete the reservation after a specific duration, and share the reservation with two consumer projects, make a request as follows:
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAfterDuration": {
              "seconds": " DELETE_AFTER_DURATION"
            }**,
            "name": "RESERVATION_NAME",
            "shareSettings": {
              "shareType": "SPECIFIC_PROJECTS",
              "projectMap": {
                "CONSUMER_PROJECT_ID_1": {
                  "projectId": "CONSUMER_PROJECT_ID_1"
                },
                "CONSUMER_PROJECT_ID_2": {
                  "projectId": "CONSUMER_PROJECT_ID_2"
                }
              }
            },
            "specificReservation": {
              "count": "NUMBER_OF_VMS",
              "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          }
          

Replace `DELETE_AFTER_DURATION` with a duration in seconds. For example, specify `86400` for 86,400 seconds (1 day).




### Specify an existing VM

You can only create a shared reservation based on an existing VM in the same project and zone as the VM.

After creating the reservation, you can consume it by creating VMs with properties that match the reference VM. You can do this by doing one of the following:

  * Create and use an instance template as follows:

    1. [Create an instance template based on the reference VM](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) without overriding the reference VM's properties.

**Note:** You can't create an instance template based on the reference VM outside of the VM's project. For the projects that the reservation is shared with, you must create similar instance templates in those projects.
    2. Create VMs using the newly-created template by doing one or both of the following:

       * [Create a single VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)

       * [Create a zonal managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig)

  * Create a VM with properties that _exactly_ match the reference VM as follows:

    * In the owner project, [create a VM based on the reference VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance) without changing the properties of the VM that you're creating.

    * In the consumer projects, create a VM while manually ensuring that its properties and the reference VM's properties match.




To create a shared reservation that uses the properties of an existing VM, do the following:

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select where you want to reserve resources.

  5. In the **Share type** section, do the following:

     1. To share a reservation with other projects, select **Shared**.

     2. Click add **Add projects** , and then select the projects from the current project's organization that you want to share the reservation with. You can select up to 100 consumer projects.

  6. Optional: To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, in the **Google Cloud services** section, select **Share reservation**.

  7. In the **Use with VM instance** section, select one of the following options:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically**.

     * To consume this reservation's resources only when you create matching VMs that specifically target the reservation by name, select **Select specific reservation**.

  8. In the **Resource details** section, do the following:

     * In the **Number of VM instances** field, enter the number of VMs that you want to reserve.

     * To specify VM configurations by using a reference VM, select **Use existing VM** , and then, in the list that appears, select the VM.

  9. In the **Auto-delete** section, you can enable the auto-delete option to let Compute Engine automatically delete the reservation at a specific date and time. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  10. To create the reservation, click **Create**. The **Reservations** page appears. Creating the reservation can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).




### Specify properties directly

To create a shared reservation by specifying properties directly, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select where you want to reserve resources.

  5. In the **Share type** section, do the following:

     1. To share a reservation with other projects, select **Shared**.

     2. Click add **Add projects** , and then select the projects from the current project's organization that you want to share the reservation with. You can select up to 100 consumer projects.

  6. Optional: To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, in the **Google Cloud services** section, select **Share reservation**.

  7. In the **Use with VM instance** section, select one of the following options:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically**.

     * To consume this reservation's resources only when you create matching VMs that specifically target the reservation by name, select **Select specific reservation**.

  8. In the **Resource details** section, do the following:

     * In the **Number of VM instances** field, enter the number of VMs that you want to reserve.

     * Specify the machine series and type that you want to reserve.

  9. In the **Auto-delete** section, you can enable the auto-delete option to let Compute Engine automatically delete the reservation at a specific date and time. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  10. To create the reservation, click **Create**. The **Reservations** page appears. Creating the reservation can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).




###  gcloud 

To create a shared reservation, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create) with the `--share-setting=projects` and `--share-with` flags.

To create a shared reservation by specifying properties directly and without including any optional flags, run the following command:
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --machine-type=MACHINE_TYPE \
        --share-setting=projects \
        --share-with=CONSUMER_PROJECT_IDS \
        --vm-count=NUMBER_OF_VMS \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `MACHINE_TYPE`: a machine type to use for each VM.

  * `CONSUMER_PROJECT_IDS`: a comma-separated list of [IDs of projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that can consume this reservation—for example, `project-1,project-2`. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the owner project. By default, it is already allowed to consume the reservation.

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `ZONE`: the zone in which to reserve resources.




For example, to create a reservation in zone `us-central1-a` for ten VMs that each use an N2 predefined machine type with 4 vCPUs, and share the reservation with projects `project-1` and `project-2`, run the following command:
    
    
    gcloud compute reservations create my-reservation \
        --machine-type=n2-standard-4 \
        --share-setting=projects \
        --share-with=project-1,project-2 \
        --vm-count=10 \
        --zone=us-central1-a
    

Optionally, you can do one or more of the following:

  * To attach GPUs to your reserved N1 VMs, include the `--accelerator` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            **--accelerator=count= NUMBER_OF_ACCELERATORS,type=ACCELERATOR_TYPE**
            --machine-type=MACHINE_TYPE \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

Replace the following:

    * `NUMBER_OF_ACCELERATORS`: the number of GPUs to add per reserved VM.

    * `ACCELERATOR_TYPE`: a [supported GPU model for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). Ensure that your chosen GPU model [is available in the zone](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) where you want to reserve resources. Otherwise, creating the reservation fails.

  * To attach Local SSD disks to a [machine type that doesn't include Local SSD disks by default](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options), include the `--local-ssd` flag. You can only attach Local SSD disks of 375 GB.
        
        gcloud compute reservations create RESERVATION_NAME \
            **--local-ssd=count= NUMBER_OF_LOCAL_SSD_DISKS,size=375,interface=INTERFACE_TYPE** \
            --machine-type=MACHINE_TYPE \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

Replace the following:

    * `NUMBER_OF_LOCAL_SSD_DISKS`: the number of Local SSD disks to attach.

    * `INTERFACE_TYPE`: the type of disk interface that you want each Local SSD disk to use and that [your specified machine type supports](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface). Specify one of the following values:

      * For the NVME disk interface: `nvme`

      * For the SCSI disk interface: `scsi`

  * To have the reserved VMs use a specific [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) instead of the zone's default CPU platform, include the `--min-cpu-platform` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            --machine-type=MACHINE_TYPE \
            **--min-cpu-platform=" MIN_CPU_PLATFORM"** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

Replace `MIN_CPU_PLATFORM` with a minimum CPU platform. To make sure that a CPU platform is available in the zone where you're reserving resources, [view the available CPU platforms by zone](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#cpusbyzone).

  * To specify that only VMs that specifically target this reservation can consume it, include the `--require-specific-reservation` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            --machine-type=MACHINE_TYPE \
            **--require-specific-reservation** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, include the `--reservation-sharing-policy` flag set to `ALLOW_ALL`.
        
        gcloud compute reservations create RESERVATION_NAME \
            --machine-type=MACHINE_TYPE \
            **--reservation-sharing-policy=ALLOW_ALL** \
            --share-setting=projects \
            --share-with=CONSUMER_PROJECT_IDS \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`--delete-at-time` and `--delete-after-duration` flags **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-at-time` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-at-time= DELETE_AT_TIME** \
              --machine-type=MACHINE_TYPE \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AT_TIME` with a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be as follows:
          
          YYYY-MM-DDTHH:MM:SSOFFSET
          

Replace the following:

      * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

      * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

      * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

    * To delete the reservation after a specific duration, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-after-duration` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-after-duration= DELETE_AFTER_DURATION** \
              --machine-type=MACHINE_TYPE \
              --share-setting=projects \
              --share-with=CONSUMER_PROJECT_IDS \
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AFTER_DURATION` with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds.




###  Terraform 

To create a reservation, use the [`google_compute_reservation` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_reservation). To share a reservation with other projects, define the `share_settings` block:

  * Set the `share_type` field to `SPECIFIC_PROJECTS`.
  * In the `project_map` block, specify the [project IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the projects that you want to share this reservation with.



For more information about how to use Terraform, see [Using Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

###  REST 

To create a shared reservation, make a `POST` request to the [`reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/insert). In the request body, include the following:

  * The `projectMap` field.

  * The `shareType` field set to `SPECIFIC_PROJECTS`.




For example, to create a shared reservation without including any optional fields and share the reservation with two consumer projects, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
    
    {
      "name": "RESERVATION_NAME",
      "shareSettings": {
        "shareType": "SPECIFIC_PROJECTS",
        "projectMap": {
          "CONSUMER_PROJECT_ID_1": {
            "projectId": "CONSUMER_PROJECT_ID_1"
          },
          "CONSUMER_PROJECT_ID_2": {
            "projectId": "CONSUMER_PROJECT_ID_2"
          }
        }
      },
      "specificReservation": {
        "count": "NUMBER_OF_VMS",
        "instanceProperties": {
          "machineType": "MACHINE_TYPE"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to reserve resources.

  * `ZONE`: the zone in which to reserve resources.

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: the [IDs of projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that can consume this reservation. You can include up to 100 consumer projects. These projects must be in the same organization as the owner project. Don't include the owner project. By default, it is already allowed to consume the reservation.

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `MACHINE_TYPE`: a machine type to use for each VM.




For example, to create a reservation by specifying a global instance template in zone `us-central1-a`, share the reservation with projects `project-1` and `project-2`, and reserve ten VMs that each use an N2 predefined machine type with 4 vCPUs, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations
    
    {
      "name": "my-reservation",
      "shareSettings": {
        "shareType": "SPECIFIC_PROJECTS",
        "projectMap": {
          "project-1": {
            "projectId": "project-1"
          },
          "project-2": {
            "projectId": "project-2"
          }
        }
      },
      "specificReservation": {
        "count": "10",
        "instanceProperties": {
          "machineType": "n2-standard-4",
        }
      }
    }
    

Optionally, you can do one or more of the following:

  * To attach GPUs to your reserved N1 VMs, include the `guestAccelerators` field in the request body.

For example, to create a reservation shared with two consumer projects, and attach GPUs to any reserved N1 VMs, make a request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              **"guestAccelerators": [
                {
                  "acceleratorCount": NUMBER_OF_ACCELERATORS,
                  "acceleratorType": "ACCELERATOR_TYPE"
                }
              ]**,
              "machineType": "MACHINE_TYPE"
            }
          }
        }
        

Replace the following:

    * `NUMBER_OF_ACCELERATORS`: the number of GPUs to add per reserved VM.

    * `ACCELERATOR_TYPE`: a [supported GPU model for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus). Ensure that your chosen GPU model [is available in the zone](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) where you want to reserve resources. Otherwise, creating the reservation fails.

  * To attach Local SSD disks to a [machine type that doesn't include Local SSD disks by default](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options), include the `localSsds` field in the request body. You can only attach Local SSD disks of 375 GB.

For example, to attach two Local SSD disks to the machine type that you want to reserve while specifying two consumer projects, make a request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              **"localSsds": [
                {
                  "diskSizeGb": "375",
                  "interface": " INTERFACE_TYPE"
                },
                {
                  "diskSizeGb": "375",
                  "interface": "INTERFACE_TYPE"
                }
              ]**,
              "machineType": "MACHINE_TYPE"
            }
          }
        }
        

Replace `INTERFACE_TYPE` with the type of disk interface that you want each Local SSD disk to use and that [your specified machine type supports](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface). Specify one of the following values:

    * For the NVME disk interface: `NVME`

    * For the SCSI disk interface: `SCSI`

  * To have the reserved VMs use a specific [minimum CPU platform](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform) instead of the zone's default CPU platform, include the `minCpuPlatform` field in the request body.

For example, to create a shared reservation while specifying a minimum CPU platform and two consumer projects, make a request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              "machineType": "MACHINE_TYPE",
              **"minCpuPlatform": " MIN_CPU_PLATFORM"**
            }
          }
        }
        

Replace `MIN_CPU_PLATFORM` with a minimum CPU platform. To make sure that a CPU platform is available in the zone where you're reserving resources, [view the available CPU platforms by zone](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#cpusbyzone).

  * To specify that only VMs that [specifically target this reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation) can consume it, include the `specificReservationRequired` field in the request body, and set the field to `true`.

For example, to create a specific reservation and share it with two consumer projects, make a request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              "machineType": "MACHINE_TYPE"
            }
          },
          **"specificReservationRequired": true**
        }
        

  * To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, include the `serviceShareType` field and set it to `ALLOW_ALL`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          **"reservationSharingPolicy": {
            "serviceShareType": "ALLOW_ALL"
          }** ,
          "shareSettings": {
            "shareType": "SPECIFIC_PROJECTS",
            "projectMap": {
              "CONSUMER_PROJECT_ID_1": {
                "projectId": "CONSUMER_PROJECT_ID_1"
              },
              "CONSUMER_PROJECT_ID_2": {
                "projectId": "CONSUMER_PROJECT_ID_2"
              }
            }
          },
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              "machineType": "MACHINE_TYPE"
            }
          }
        }
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`deleteAtTime` and `deleteAfterDuration` fields **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, make a `POST` request to the [`beta.reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/insert). In the request body, include the `deleteAtTime` field.

For example, to create a reservation while specifying a date and time to delete a reservation, and share the reservation with two consumer projects, make a request as follows:
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAtTime": " DELETE_AT_TIME"**,
            "name": "RESERVATION_NAME",
            "shareSettings": {
              "shareType": "SPECIFIC_PROJECTS",
              "projectMap": {
                "CONSUMER_PROJECT_ID_1": {
                  "projectId": "CONSUMER_PROJECT_ID_1"
                },
                "CONSUMER_PROJECT_ID_2": {
                  "projectId": "CONSUMER_PROJECT_ID_2"
                }
              }
            },
            "specificReservation": {
              "count": "NUMBER_OF_VMS",
              "instanceProperties": {
                "machineType": "MACHINE_TYPE"
              }
            }
          }
          

Replace `DELETE_AT_TIME` with a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be as follows:
          
          YYYY-MM-DDTHH:MM:SSOFFSET
          

Replace the following:

      * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

      * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

      * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

    * To delete the reservation after a specific duration, make a `POST` request to the [`beta.reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/insert). In the request body, include the `deleteAfterDuration` field.

For example, to create a reservation that Compute Engine deletes after a specific duration, and share the reservation with two consumer projects, make a request as follows:
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAfterDuration": {
              "seconds": " DELETE_AFTER_DURATION"
            }**,
            "name": "RESERVATION_NAME",
            "shareSettings": {
              "shareType": "SPECIFIC_PROJECTS",
              "projectMap": {
                "CONSUMER_PROJECT_ID_1": {
                  "projectId": "CONSUMER_PROJECT_ID_1"
                },
                "CONSUMER_PROJECT_ID_2": {
                  "projectId": "CONSUMER_PROJECT_ID_2"
                }
              }
            },
            "specificReservation": {
              "count": "NUMBER_OF_VMS",
              "instanceProperties": {
                "machineType": "MACHINE_TYPE"
              }
            }
          }
          

Replace `DELETE_AFTER_DURATION` with a duration in seconds. For example, specify `86400` for 86,400 seconds (1 day).




## Troubleshooting

Learn how to [troubleshoot reservation creation](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-creation).

## What's next

  * Learn how to [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view).

  * Learn how to [attach reservations to commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments).

  * Learn how to [consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).

  * Learn how to [monitor reservations consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-monitor).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
