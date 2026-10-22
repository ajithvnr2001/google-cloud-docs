---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-single-project/
title: Create a reservation for a single project \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:34.896712+00:00
---

# Create a reservation for a single project  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-single-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a reservation for a single project Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a single-project reservation, which can be consumed only by virtual machine (VM) instances in the same project. To learn more about reservations, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

For other methods of creating reservations, see instead the following pages:

  * To create a reservation that can be used by multiple projects, see [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared).

  * To create a reservation when purchasing a resource-based commitment, see [Purchase hardware commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations). Commitments provide discounts, known as committed use discounts (CUDs), on your on-demand resource costs in exchange for purchasing a minimum level of resources or for spending a minimum amount.


**Note:** After you create a reservation, you are charged for the reserved resources, even if they are not used, until you delete the reservation. If you delete a reservation but don't delete the VMs that were using the reserved resources, the resources still incur charges. For more information, see [Billing](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing).

## Before you begin

  * Review the [ requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) and [ restrictions](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#restrictions) for reservations.
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




### Required roles

To get the permissions that you need to create single-project reservations, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create single-project reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create single-project reservations:

  * `compute.reservations.create` on the project
  * To specify an instance template: `compute.instanceTemplates.useReadOnly` on the instance template 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a single-project reservation

To consume a reservation, a VM must have [properties that _exactly_ match](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) that reservation. To specify the properties of the VMs that you want to reserve, select one of the following sections in this document:

  * Recommended: Specify an instance template

This section explains how to use an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) to define the properties of a reservation. By using an instance template, you can define the properties of a reservation and the VMs that can consume the reservation in the same place.

  * Specify an existing VM

This section explains how to use an existing VM to define the properties of a reservation. By using the properties of an existing VM, you can consume the reservation by creating VMs with properties that match the reference VM.

  * Specify properties directly

This section explains how to directly define the properties of a reservation. This method requires you to manually ensure that the properties of your VMs and reservations _exactly_ match—any mismatched properties prevent consumption.




By default, a reservation can be automatically consumed by any VMs with properties that match it. If you want to control reservation consumption, do one or more of the following:

  * Create a reservation that can only be consumed by VMs that specifically target it, as explained in the following sections in this document. Then, [configure VMs to consume that specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * [Configure VMs to not consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption).




Additionally, you can specify a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) when creating a single-project [specific reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation). A compact placement policy specifies that VMs are to be located as close to each other as possible to reduce network latency.

### Specify an instance template

To avoid errors when creating a reservation by specifying an instance template, make sure of the following:

  * Create your reservation in the same region and zone as the resources within the instance template. Any [regional](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources) or [zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource) specified in an instance template—such as a machine type or a Persistent Disk volume—restrict the use of the template to the locations where those resources exist. For example, if your instance template specifies an existing Persistent Disk volume in zone `us-central1-a`, then you can only create your reservation in the same zone. To check if an existing template specifies any resources that bind the template to a specific region or zone, [view the details of the instance template](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) and look for references to regional or zonal resources inside of it.

  * If the instance template specifies a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview), then make sure that the template specifies a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies. Otherwise, creating the reservation fails.




To create a single-project reservation by specifying an instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select where you want to reserve resources.

  5. Optional: To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, in the **Google Cloud services** section, select **Share reservation**.

  6. In the **Use with VM instance** section, select one of the following options:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically**.

     * To consume this reservation's resources only when you create matching VMs that specifically target the reservation by name, select **Select specific reservation**.

  7. In the **Resource details** section, do the following:

     * In the **Number of VM instances** field, enter the number of VMs that you want to reserve.

     * To specify VM configurations by using an instance template, select **Use instance template** , and then, in the list that appears, select the instance template.

  8. In the **Auto-delete** section, you can enable the auto-delete option to let Compute Engine automatically delete the reservation at a specific date and time. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  9. To create the reservation, click **Create**. The **Reservations** page appears. Creating the reservation can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).




###  gcloud 

To create a single-project reservation, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create).

To create a single-project reservation by specifying an instance template and without including any optional flags, run the following command:
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --source-instance-template=INSTANCE_TEMPLATE_URL \
        --vm-count=NUMBER_OF_VMS \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `INSTANCE_TEMPLATE_URL`: the URL of an existing instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `ZONE`: the zone in which to reserve resources.




For example, to create a reservation for ten VMs in zone `us-central1-a` by specifying a global instance template, run the following command:
    
    
    gcloud compute reservations create my-reservation \
        --source-instance-template=example-instance-template \
        --vm-count=10 \
        --zone=us-central1-a
    

Optionally, you can do one or more of the following:

  * To specify that only VMs that specifically target this reservation can consume it, include the `--require-specific-reservation` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            --source-instance-template=INSTANCE_TEMPLATE_URL \
            **--require-specific-reservation** \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To allow a reservation of GPU VMs to be consumed by [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI, include the `--reservation-sharing-policy` flag set to `ALLOW_ALL`.
        
        gcloud compute reservations create RESERVATION_NAME \
            --source-instance-template=INSTANCE_TEMPLATE_URL \
            **--reservation-sharing-policy=ALLOW_ALL** \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`--delete-at-time` and `--delete-after-duration` flags **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-at-time` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-at-time= DELETE_AT_TIME** \
              --source-instance-template=INSTANCE_TEMPLATE_URL \
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AT_TIME` with a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339), which must be as follows: `none YYYY-MM-DDTHH:MM:SSOFFSET`

Replace the following:

      * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and a 2-digit day of the month, separated by hyphens (`-`).

      * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

      * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. Alternatively, to use no offset, specify `Z`.

    * To delete the reservation after a specific duration, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-after-duration` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-after-duration= DELETE_AFTER_DURATION** \
              --source-instance-template=INSTANCE_TEMPLATE_URL \
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AFTER_DURATION` with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // Creates the reservation from given template in particular zone
    func createReservation(w io.Writer, projectID, zone, reservationName, sourceTemplate string) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-a"
    	// reservationName := "your_reservation_name"
    	// template: existing template path. Following formats are allowed:
    	//  	- projects/{project_id}/global/instanceTemplates/{template_name}
    	//  	- projects/{project_id}/regions/{region}/instanceTemplates/{template_name}
    	//  	- https://www.googleapis.com/compute/v1/projects/{project_id}/global/instanceTemplates/instanceTemplate
    	//  	- https://www.googleapis.com/compute/v1/projects/{project_id}/regions/{region}/instanceTemplates/instanceTemplate
    
    	ctx := context.Background()
    	reservationsClient, err := compute.[NewReservationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ReservationsClient_NewReservationsRESTClient)(ctx)
    	if err != nil {
    		return err
    	}
    	defer reservationsClient.Close()
    
    	req := &computepb.InsertReservationRequest{
    		Project: projectID,
    		ReservationResource: &computepb.Reservation{
    			Name: proto.String(reservationName),
    			Zone: proto.String(zone),
    			SpecificReservation: &computepb.AllocationSpecificSKUReservation{
    				Count:                  proto.Int64(2),
    				SourceInstanceTemplate: proto.String(sourceTemplate),
    			},
    		},
    		Zone: zone,
    	}
    
    	op, err := reservationsClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create reservation: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reservation created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AllocationSpecificSKUReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUReservation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html);
    import com.google.cloud.compute.v1.[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateReservationForInstanceTemplate {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone in which you want to create the reservation.
        String zone = "us-central1-a";
        // Name of the reservation you want to create.
        String reservationName = "YOUR_RESERVATION_NAME";
        // The number of virtual machines you want to create.
        int numberOfVms = 3;
        // The URI of the instance template with GLOBAL location
        // to be used for creating the reservation.
        String instanceTemplateUri =
            "projects/YOUR_PROJECT_ID/global/instanceTemplates/YOUR_INSTANCE_TEMPLATE_NAME";
        // The URI of the instance template with REGIONAL location
        // to be used for creating the reservation. For us-central1 region in this case.
        // String instanceTemplateUri =
        // "projects/YOUR_PROJECT_ID/regions/us-central1/instanceTemplates/YOUR_INSTANCE_TEMPLATE_NAME"
    
        createReservationForInstanceTemplate(
            projectId, reservationName, instanceTemplateUri, numberOfVms, zone);
      }
    
      // Creates a reservation in a project for the instance template.
      public static [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) createReservationForInstanceTemplate(
          String projectId, String reservationName, String instanceTemplateUri,
          int numberOfVms, String zone)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html) reservationsClient = [ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html).create()) {
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) reservation =
              [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html).newBuilder()
                  .setName(reservationName)
                  .setZone(zone)
                  .[setSpecificReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.Builder.html#com_google_cloud_compute_v1_Reservation_Builder_setSpecificReservation_com_google_cloud_compute_v1_AllocationSpecificSKUReservation_)(
                      [AllocationSpecificSKUReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUReservation.html).newBuilder()
                          // Set the number of instances
                          .setCount(numberOfVms)
                          // Set the instance template to be used for creating the reservation.
                          .setSourceInstanceTemplate(instanceTemplateUri)
                          .build())
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response =
              reservationsClient.insertAsync(projectId, zone, reservation).get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            return null;
          }
          return reservationsClient.get(projectId, zone, reservationName);
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a reservationsClient
    const reservationsClient = new computeLib.[ReservationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where you want to reserve resources and where the instance template exists.
    const projectId = await reservationsClient.getProjectId();
    // The zone in which to reserve resources.
    const zone = 'us-central1-a';
    // The name of the reservation to create.
    // reservationName = 'reservation-01';
    // The number of VMs to reserve.
    const vmsNumber = 3;
    
    /**
     * The name of an existing instance template.
     * TODO(developer): Uncomment and update instanceTemplateName before running the sample.
     */
    // const instanceTemplateName = 'pernament-region-template-name';
    
    /**
     * // The location of the instance template.
     * TODO(developer): Uncomment the `location` variable depending on which template you want to use.
     */
    
    // The location for a regional instance template: regions/{region}. Replace region with the region where the instance template is located.
    // If you specify a regional instance template, then you can only reserve VMs within the same region as the template's region.
    // const location = `regions/${zone.slice(0, -2)}`;
    
    // The location for a global instance template.
    // const location = 'global';
    
    async function callCreateComputeReservationInstanceTemplate() {
      // Create reservation for 3 VMs in zone us-central1-a by specifying a instance template.
      const specificReservation = new compute.AllocationSpecificSKUReservation({
        count: vmsNumber,
        sourceInstanceTemplate: `projects/${projectId}/${location}/instanceTemplates/${instanceTemplateName}`,
      });
    
      // Create a reservation.
      const reservation = new compute.Reservation({
        name: reservationName,
        specificReservation,
        // To specify that only VMs that specifically target this reservation can consume it,
        // set specificReservationRequired field to true.
        specificReservationRequired: true,
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
    }
    
    await callCreateComputeReservationInstanceTemplate();

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
    
    
    def create_reservation_from_template(
        project_id: str, reservation_name: str, template: str
    ) -> compute_v1.Reservation:
        """
        Create a new reservation based on an existing template.
    
        Args:
            project_id: project ID or project number of the Cloud project you use.
            reservation_name: the name of new reservation.
            template: existing template path. Following formats are allowed:
                - projects/{project_id}/global/instanceTemplates/{template_name}
                - projects/{project_id}/regions/{region}/instanceTemplates/{template_name}
                - https://www.googleapis.com/compute/v1/projects/{project_id}/global/instanceTemplates/instanceTemplate
                - https://www.googleapis.com/compute/v1/projects/{project_id}/regions/{region}/instanceTemplates/instanceTemplate
    
        Returns:
            Reservation object that represents the new reservation.
        """
    
        reservations_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html)()
        request = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InsertReservationRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InsertReservationRequest.html)()
        request.project = project_id
        request.zone = "us-central1-a"
    
        specific_reservation = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUReservation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUReservation.html)()
        specific_reservation.count = 1
        specific_reservation.source_instance_template = template
    
        reservation = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Reservation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Reservation.html)()
        reservation.name = reservation_name
        reservation.specific_reservation = specific_reservation
    
        request.reservation_resource = reservation
        operation = reservations_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_insert)(request)
        wait_for_extended_operation(operation, "Reservation creation")
    
        return reservations_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_get)(
            project=project_id, zone="us-central1-a", reservation=reservation_name
        )
    
    

###  REST 

To create a single-project reservation, make a `POST` request to the [`reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/insert).

To create a single-project reservation by specifying an instance template and without including any optional flags, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
    
    {
      "name": "RESERVATION_NAME",
      "specificReservation": {
        "count": "NUMBER_OF_VMS",
        "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to reserve resources and where the instance template exists.

  * `ZONE`: the zone in which to reserve resources.

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `INSTANCE_TEMPLATE_URL`: the URL of an existing instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`




For example, to create a reservation for ten VMs in zone `us-central1-a` by specifying a global instance template, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations
    
    {
      "name": "my-reservation",
      "specificReservation": {
        "count": "10",
        "sourceInstanceTemplate": "example-instance-template"
      }
    }
    

Optionally, you can do one or more of the following:

  * To specify that only VMs that specifically target this reservation can consume it, include the `specificReservationRequired` field in the request body, and set the field to `true`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
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
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
          }
        }
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`deleteAtTime` and `deleteAfterDuration` fields **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, make a `POST` request to the [`beta.reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/reservations/insert). In the request body, include the `deleteAtTime` field.
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAtTime": " DELETE_AT_TIME"**,
            "name": "RESERVATION_NAME",
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
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAfterDuration": {
              "seconds": " DELETE_AFTER_DURATION"
            }**,
            "name": "RESERVATION_NAME",
            "specificReservation": {
              "count": "NUMBER_OF_VMS",
              "sourceInstanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          }
          

Replace `DELETE_AFTER_DURATION` with a duration in seconds. For example, specify `86400` for 86,400 seconds (1 day).




### Specify an existing VM

You can only create a reservation based on an existing VM in the same zone as the VM.

After creating the reservation, you can consume it by creating VMs with properties that match the reference VM. You can do this by doing one of the following:

  * Create and use an instance template as follows:

    1. [Create an instance template based on the reference VM](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) without overriding the reference VM's properties.

    2. Create VMs using the newly-created template by doing one or both of the following:

       * [Create a single VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)

       * [Create a zonal managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig)

  * [Create a VM based on the reference VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance) while ensuring that the properties of the new VM and the reference VM _exactly_ match.




To create a single-project reservation that uses the properties of an existing VM, do the following:

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select where you want to reserve resources.

  5. Optional: To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, in the **Google Cloud services** section, select **Share reservation**.

  6. In the **Use with VM instance** section, select one of the following options:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically**.

     * To consume this reservation's resources only when you create matching VMs that specifically target the reservation by name, select **Select specific reservation**.

  7. In the **Resource details** section, do the following:

     * In the **Number of VM instances** field, enter the number of VMs that you want to reserve.

     * To specify VM configurations by using an instance template, select **Use existing VM** , and then, in the list that appears, select the VM.

  8. Optional: To specify a compact placement policy for a reservation that meets the [requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-reservations-placement-policies), in the **Group placement policy** section, click the **Select or create a group placement policy** list, and then do one of the following:

     * To create a compact placement policy to specify in this reservation, do the following:

**Important:** By using this method, you can only create a compact placement policy with an unspecified maximum distance value. If you want to specify a new compact placement policy with a maximum distance value of `3` or `2`, then you must [create a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy) separately and select the existing compact placement policy instead.
       1. Click **Create group placement policy**. The **Create a group placement policy** pane appears.

       2. In the **Policy name** field, enter a name for your policy.

       3. Click **Create**. Creating the compact placement policy might take a few seconds to complete.

     * Otherwise, select an existing compact placement policy.

  9. In the **Auto-delete** section, you can enable the auto-delete option to let Compute Engine automatically delete the reservation at a specific date and time. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  10. To create the reservation, click **Create**. The **Reservations** page appears. Creating the reservation can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).




### Specify properties directly

To create a single-project reservation by specifying properties directly, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click add_box **Create reservation**. The **Create a reservation** page appears.

  3. In the **Name** field, enter a name for your reservation.

  4. In the **Region** and **Zone** lists, select where you want to reserve resources.

  5. Optional: To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, in the **Google Cloud services** section, select **Share reservation**.

  6. In the **Use with VM instance** section, select one of the following options:

     * To allow matching VMs to automatically consume this reservation, select **Use reservation automatically**.

     * To consume this reservation's resources only when you create matching VMs that specifically target the reservation by name, select **Select specific reservation**.

  7. In the **Resource details** section, do the following:

     * In the **Number of VM instances** field, enter the number of VMs that you want to reserve.

     * Specify the machine series and type that you want to reserve.

  8. Optional: To specify a compact placement policy for a reservation that meets the [reservation requirements](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-reservations-placement-policies), in the **Group placement policy** section, click the **Select or create a group placement policy** list, and then do one of the following:

     * To create a compact placement policy to specify in this reservation, do the following:

**Important:** By using this method, you can only create a compact placement policy with an unspecified maximum distance value. If you want to specify a new compact placement policy with a maximum distance value of `3` or `2`, then you must [create a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy) separately and select the existing compact placement policy instead.
       1. Click **Create group placement policy**. The **Create a group placement policy** pane appears.

       2. In the **Policy name** field, enter a name for your policy.

       3. Click **Create**. Creating the compact placement policy might take a few seconds to complete.

     * Otherwise, select an existing compact placement policy.

  9. In the **Auto-delete** section, you can enable the auto-delete option to let Compute Engine automatically delete the reservation at a specific date and time. Automatically deleting reservations can be useful to avoid unnecessary charges when you stop consuming the reservation.

  10. To create the reservation, click **Create**. The **Reservations** page appears. Creating the reservation can take up to a minute to complete. To verify when Compute Engine finishes creating it, [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-reservations).




###  gcloud 

To create a single-project reservation, use the [`gcloud compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/create).

To create a single-project reservation by specifying properties directly and without including any optional flags, run the following command:
    
    
    gcloud compute reservations create RESERVATION_NAME \
        --machine-type=MACHINE_TYPE \
        --vm-count=NUMBER_OF_VMS \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation to create.

  * `MACHINE_TYPE`: a machine type to use for each VM.

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `ZONE`: the zone in which to reserve resources.




For example, to create a reservation in zone `us-central1-a` for ten VMs that each use an N2 predefined machine type with 4 vCPUs, run the following command:
    
    
    gcloud compute reservations create my-reservation \
        --machine-type=n2-standard-4 \
        --vm-count=10 \
        --zone=us-central1-a
    

Optionally, you can do one or more of the following:

  * To attach GPUs to your reserved N1 VMs, include the `--accelerator` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            **--accelerator=count= NUMBER_OF_ACCELERATORS,type=ACCELERATOR_TYPE** \
            --machine-type=MACHINE_TYPE \
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
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

Replace `MIN_CPU_PLATFORM` with a minimum CPU platform. To make sure that a CPU platform is available in the zone where you're reserving resources, [view the available CPU platforms by zone](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#cpusbyzone).

  * To specify that only VMs that specifically target this reservation can consume it, include the `--require-specific-reservation` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            --machine-type=MACHINE_TYPE \
            **--require-specific-reservation** \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To specify a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) for lower network latency among VMs, include the `--resource-policies=policy` flag.
        
        gcloud compute reservations create RESERVATION_NAME \
            --machine-type=MACHINE_TYPE \
            **--resource-policies=policy= COMPACT_PLACEMENT_POLICY_NAME** \
            --require-specific-reservation \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

Replace COMPACT_PLACEMENT_POLICY_NAME with the name of an existing compact placement policy. Additionally, to avoid errors when creating a single-project reservation that specifies a compact placement policy, make sure to specify the following:

    * A [supported machine type and maximum number of VMs](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions-compact-policies) for compact placement policies.

    * A zone within the region where the compact placement policy is located.

    * The `--require-specific-reservation` flag. This indicates that only VMs that specifically target the reservation can consume it.

  * To let [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI consume a reservation of GPU VMs, include the `--reservation-sharing-policy` flag set to `ALLOW_ALL`.
        
        gcloud compute reservations create RESERVATION_NAME \
            --machine-type=MACHINE_TYPE \
            **--reservation-sharing-policy=ALLOW_ALL** \
            --vm-count=NUMBER_OF_VMS \
            --zone=ZONE
        

  * To enable Compute Engine to [automatically delete the reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#auto-delete), select one of the following methods:

**Preview — The`--delete-at-time` and `--delete-after-duration` flags **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

    * To delete the reservation at a specific date and time, use the [`gcloud beta compute reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/reservations/create) with the `--delete-at-time` flag.
          
          gcloud beta compute reservations create RESERVATION_NAME \
              **--delete-at-time= DELETE_AT_TIME** \
              --machine-type=MACHINE_TYPE \
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
              --vm-count=NUMBER_OF_VMS \
              --zone=ZONE
          

Replace `DELETE_AFTER_DURATION` with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // Creates the reservation with accelerated image
    func createBaseReservation(w io.Writer, projectID, zone, reservationName string) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-a"
    	// reservationName := "your_reservation_name"
    
    	ctx := context.Background()
    	reservationsClient, err := compute.[NewReservationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ReservationsClient_NewReservationsRESTClient)(ctx)
    	if err != nil {
    		return err
    	}
    	defer reservationsClient.Close()
    
    	// Creating reservation based on direct properties
    	req := &computepb.InsertReservationRequest{
    		Project: projectID,
    		ReservationResource: &computepb.Reservation{
    			Name: proto.String(reservationName),
    			Zone: proto.String(zone),
    			SpecificReservation: &computepb.AllocationSpecificSKUReservation{
    				Count: proto.Int64(2),
    				// Properties, which allows customising instances
    				InstanceProperties: &computepb.AllocationSpecificSKUAllocationReservedInstanceProperties{
    					// Attaching GPUs to the reserved VMs
    					// Read more: https://cloud.google.com/compute/docs/gpus#n1-gpus
    					GuestAccelerators: []*computepb.AcceleratorConfig{
    						{
    							AcceleratorCount: proto.Int32(1),
    							AcceleratorType:  proto.String("nvidia-tesla-t4"),
    						},
    					},
    					// Including local SSD disks
    					LocalSsds: []*computepb.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk{
    						{
    							DiskSizeGb: proto.Int64(375),
    							Interface:  proto.String("NVME"),
    						},
    					},
    					MachineType: proto.String("n1-standard-2"),
    					// Specifying minimum CPU platform
    					// Read more: https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform
    					MinCpuPlatform: proto.String("Intel Skylake"),
    				},
    			},
    		},
    		Zone: zone,
    	}
    
    	op, err := reservationsClient.Insert(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create reservation: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reservation created\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[AcceleratorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AcceleratorConfig.html);
    import com.google.cloud.compute.v1.[AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk.html);
    import com.google.cloud.compute.v1.[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationReservedInstanceProperties.html);
    import com.google.cloud.compute.v1.[AllocationSpecificSKUReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUReservation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html);
    import com.google.cloud.compute.v1.[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateReservation {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the zone in which you want to create the disk.
        String zone = "us-central1-a";
        // Name of the reservation you want to create.
        String reservationName = "YOUR_RESERVATION_NAME";
        // Number of instances in the reservation.
        int numberOfVms = 3;
    
        createReservation(projectId, reservationName, numberOfVms, zone);
      }
    
      // Creates reservation with optional flags
      public static [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) createReservation(
          String projectId, String reservationName, int numberOfVms, String zone)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Create the reservation with optional properties:
        // Machine type of the instances in the reservation.
        String machineType = "n1-standard-2";
        // Number of accelerators to be attached to the instances in the reservation.
        int numberOfAccelerators = 1;
        // Accelerator type to be attached to the instances in the reservation.
        String acceleratorType = "nvidia-tesla-t4";
        // Minimum CPU platform to be attached to the instances in the reservation.
        String minCpuPlatform = "Intel Skylake";
        // Local SSD size in GB to be attached to the instances in the reservation.
        int localSsdSize = 375;
        // Local SSD interfaces to be attached to the instances in the reservation.
        String localSsdInterface1 = "NVME";
        String localSsdInterface2 = "SCSI";
        boolean specificReservationRequired = true;
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html) reservationsClient = [ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html).create()) {
          [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html) reservation =
              [Reservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.html).newBuilder()
                  .setName(reservationName)
                  .setZone(zone)
                  .setSpecificReservationRequired(specificReservationRequired)
                  .[setSpecificReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Reservation.Builder.html#com_google_cloud_compute_v1_Reservation_Builder_setSpecificReservation_com_google_cloud_compute_v1_AllocationSpecificSKUReservation_)(
                      [AllocationSpecificSKUReservation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUReservation.html).newBuilder()
                          // Set the number of instances
                          .setCount(numberOfVms)
                          // Set instance properties
                          .setInstanceProperties(
                              [AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationReservedInstanceProperties.html).newBuilder()
                                  .setMachineType(machineType)
                                  .setMinCpuPlatform(minCpuPlatform)
                                  .addGuestAccelerators(
                                      [AcceleratorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AcceleratorConfig.html).newBuilder()
                                          .setAcceleratorCount(numberOfAccelerators)
                                          .setAcceleratorType(acceleratorType)
                                          .build())
                                  .[addLocalSsds](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationReservedInstanceProperties.Builder.html#com_google_cloud_compute_v1_AllocationSpecificSKUAllocationReservedInstanceProperties_Builder_addLocalSsds_com_google_cloud_compute_v1_AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk_)(
                                [AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk.html)
                                          .newBuilder()
                                          .setDiskSizeGb(localSsdSize)
                                          .setInterface(localSsdInterface1)
                                          .build())
                                  .[addLocalSsds](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationReservedInstanceProperties.Builder.html#com_google_cloud_compute_v1_AllocationSpecificSKUAllocationReservedInstanceProperties_Builder_addLocalSsds_com_google_cloud_compute_v1_AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk_)(
                                [AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk.html)
                                          .newBuilder()
                                          .setDiskSizeGb(localSsdSize)
                                          .setInterface(localSsdInterface2)
                                          .build())
                                  .build())
                          .build())
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response =
              reservationsClient.insertAsync(projectId, zone, reservation).get(7, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            return null;
          }
          return reservationsClient.get(projectId, zone, reservationName);
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    const compute = computeLib.protos.google.cloud.compute.v1;
    
    // Instantiate a reservationsClient
    const reservationsClient = new computeLib.[ReservationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where you want to reserve resources.
    const projectId = await reservationsClient.getProjectId();
    // The zone in which to reserve resources.
    const zone = 'us-central1-a';
    // The name of the reservation to create.
    // reservationName = 'reservation-01';
    // The number of VMs to reserve.
    const vmsNumber = 3;
    // Machine type to use for each VM.
    const machineType = 'n1-standard-4';
    
    async function callCreateComputeReservationFromProperties() {
      // Create specific reservation for 3 VMs that each use an N1 predefined machine type with 4 vCPUs.
      const specificReservation = new compute.AllocationSpecificSKUReservation({
        count: vmsNumber,
        instanceProperties: {
          machineType,
          // To have the reserved VMs use a specific minimum CPU platform instead of the zone's default CPU platform.
          minCpuPlatform: 'Intel Skylake',
          // If you want to attach GPUs to your reserved N1 VMs, update and uncomment guestAccelerators if needed.
          // guestAccelerators: [
          //   {
          //     // The number of GPUs to add per reserved VM.
          //     acceleratorCount: 1,
          //     // Supported GPU model for N1 VMs. Ensure that your chosen GPU model is available in the zone,
          //     // where you want to reserve resources.
          //     acceleratorType: 'nvidia-tesla-t4',
          //   },
          // ],
          // If you want to add local SSD disks to each reserved VM, update and uncomment localSsds if needed.
          // You can specify up to 24 Local SSD disks. Each Local SSD disk is 375 GB.
          // localSsds: [
          //   {
          //     diskSizeGb: 375,
          //     // The type of interface you want each Local SSD disk to use. Specify one of the following values: NVME or SCSI.
          //     // Make sure that the machine type you specify for the reserved VMs supports the chosen disk interfaces.
          //     interface: 'NVME',
          //   },
          // ],
        },
      });
    
      // Create a reservation.
      const reservation = new compute.Reservation({
        name: reservationName,
        zone,
        specificReservation,
        // To specify that only VMs that specifically target this reservation can consume it,
        // set specificReservationRequired field to true.
        specificReservationRequired: true,
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
    }
    
    await callCreateComputeReservationFromProperties();

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
    
    
    def create_compute_reservation(
        project_id: str,
        zone: str = "us-central1-a",
        reservation_name="your-reservation-name",
    ) -> compute_v1.Reservation:
        """Creates a compute reservation in GCP.
        Args:
            project_id (str): The ID of the Google Cloud project.
            zone (str): The zone to create the reservation.
            reservation_name (str): The name of the reservation to create.
        Returns:
            Reservation object that represents the new reservation.
        """
    
        instance_properties = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUAllocationReservedInstanceProperties](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUAllocationReservedInstanceProperties.html)(
            machine_type="n1-standard-1",
            # Optional. Specifies the minimum CPU platform for the VM instance.
            min_cpu_platform="Intel Ivy Bridge",
            # Optional. Specifies amount of local ssd to reserve with each instance.
            local_ssds=[
                [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk.html)(
                    disk_size_gb=375, interface="NVME"
                ),
                [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.AllocationSpecificSKUAllocationAllocatedInstancePropertiesReservedDisk.html)(
                    disk_size_gb=375, interface="SCSI"
                ),
            ],
            # Optional. Specifies the GPUs allocated to each instance.
            # guest_accelerators=[
            #     compute_v1.AcceleratorConfig(
            #         accelerator_count=1, accelerator_type="nvidia-tesla-t4"
            #     )
            # ],
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
    
        print("Name: ", reservation.name)
        print("STATUS: ", reservation.status)
        print(reservation.specific_reservation)
        # Example response:
        # Name:  your-reservation-name
        # STATUS:  READY
        # count: 3
        # instance_properties {
        #   machine_type: "n1-standard-1"
        #   local_ssds {
        #     disk_size_gb: 375
        #     interface: "NVME"
        #   }
        # ...
    
        return reservation
    
    

###  Terraform 

To create a single-project reservation, use the [`google_compute_reservation` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_reservation).

For example, to create a single-project reservation for one N2 predefined machine type with 2 vCPUs, use the following resource:
    
    
    resource "google_compute_reservation" "default" {
      name = "gce-reservation-local"
      zone = "us-central1-b"
    
      /**
       * To specify a single-project reservation, omit the share_settings block
       * (default) or set the share_type field to LOCAL.
       */
      share_settings {
        share_type = "LOCAL"
      }
    
      specific_reservation {
        count = 1
        instance_properties {
          machine_type = "e2-micro"
        }
      }
    
      /**
       * To let VMs with affinity for any reservation consume this reservation, omit
       * the specific_reservation_required field (default) or set it to false.
       */
      specific_reservation_required = false
    }
    

For more information about how to use Terraform, see [Using Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

###  REST 

To create a single-project reservation, make a `POST` request to the [`reservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/insert).

To create a single-project reservation by specifying properties directly and without any including any optional fields, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
    
    {
      "name": "RESERVATION_NAME",
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

  * `NUMBER_OF_VMS`: the number of VMs to reserve.

  * `MACHINE_TYPE`: a machine type to use for each VM.




For example, to create a reservation in zone `us-central1-a` for ten VMs that each use an N2 predefined machine type with 4 vCPUs, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations
    
    {
      "name": "my-reservation",
      "specificReservation": {
        "count": "10",
        "instanceProperties": {
          "machineType": "n2-standard-4",
        }
      }
    }
    

Optionally, you can do one or more of the following:

  * To attach GPUs to your reserved N1 VMs, include the `guestAccelerators` field in the request body.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
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

For example, to attach two Local SSD disks to the machine type that you want to reserve, make a request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
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
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              "machineType": "MACHINE_TYPE",
              **"minCpuPlatform": " MIN_CPU_PLATFORM"**
            }
          }
        }
        

Replace `MIN_CPU_PLATFORM` with a minimum CPU platform. To make sure that a CPU platform is available in the zone where you're reserving resources, [view the available CPU platforms by zone](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#cpusbyzone).

  * To specify a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies) to reduce network latency among your reserved VMs, include the `resourcePolicies` field in the request body.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          **"resourcePolicies": {
            "policy" : "projects/ PROJECT_ID/regions/REGION/resourcePolicies/COMPACT_PLACEMENT_POLICY_NAME"
          }**,
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              "machineType": "MACHINE_TYPE"
            }
          },
          "specificReservationRequired": true
        }
        

Replace the following:

    * `REGION`: the region where the compact placement policy is located. You can only create the reservation within the region of the placement policy.

    * `COMPACT_PLACEMENT_POLICY_NAME`: the name of an existing compact placement policy.

Additionally, to avoid errors when creating a single-project reservation that specifies a compact placement policy, make sure to specify the following:

    * A [supported machine type](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for compact placement policies.

    * The `specificReservationRequired` field set to `true`. This indicates that only VMs that specifically target this reservation can consume it.

  * To specify that only VMs that specifically target this reservation can consume it, include the `specificReservationRequired` field in the request body and set the field to `true`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          "specificReservation": {
            "count": "NUMBER_OF_VMS",
            "instanceProperties": {
              "machineType": "MACHINE_TYPE"
            }
          },
          **"specificReservationRequired": true**
        }
        

  * To allow a reservation of GPU VMs to be consumed by [custom training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) or [prediction jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) in Vertex AI, include the `serviceShareType` field and set it to `ALLOW_ALL`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations
        
        {
          "name": "RESERVATION_NAME",
          **"reservationSharingPolicy": {
            "serviceShareType": "ALLOW_ALL"
          }** ,
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
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAtTime": " DELETE_AT_TIME"**,
            "name": "RESERVATION_NAME",
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
          
          POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/reservations
          
          {
            **"deleteAfterDuration": {
              "seconds": " DELETE_AFTER_DURATION"
            }**,
            "name": "RESERVATION_NAME",
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
