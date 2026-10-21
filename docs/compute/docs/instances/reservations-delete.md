---
url: https://docs.cloud.google.com/compute/docs/instances/reservations-delete/
title: Delete reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:35:32.115325+00:00
---

# Delete reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/reservations-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Delete reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to delete reservations. To learn how to delete future reservation requests, see [Cancel or delete future reservation requests](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations) instead.

Delete a reservation to stop incurring charges for reserved resources that you no longer need.

## Limitations

Before you delete a reservation, consider the following:

  * You can only delete a shared reservation in the same project where you created it.

  * You can only delete a [_specifically targeted_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) if no Compute Engine instances consume it. If any instances consume the reservation, then, before you delete it, do one of the following:

    * [Delete the instances](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)

    * [Stop](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm) or [suspend the instances](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)

**Caution:** If you stop or suspend instances that you created to consume a specific reservation, then you can only restart or resume them if you create a new specific reservation with the same name, zone, and properties as the deleted reservation.
  * You can only delete an auto-created reservation for a future reservation after its reservation period ends.

  * For reservations that are attached to commitments, if your commitment specifies any [resource types that require attached reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#committed_resources_that_require_attached_reservations), then you can't manually delete the reservation. However, you can [replace the existing attached reservation with a new one](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#modifying_reservations_that_are_attached_to_commitments).




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




### Required roles

To get the permission that you need to delete reservations, ask your administrator to grant you the [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.reservations.delete` permission, which is required to delete reservations. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a reservation

If you delete a reservation that can be automatically consumed by any matching compute instances, then any instances that consume the deleted reservation keep running. You continue to incur charges for those instances.

You can delete single reservations or multiple reservations at once. For multiple reservations, use the Google Cloud console. For single reservations, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. On the **On-demand reservations** tab (default), select the reservations that you want to delete.

  3. Click delete **Delete**.

  4. To confirm, click **Delete**.




###  gcloud 

To delete a reservation, use the [`gcloud compute reservations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/delete):
    
    
    gcloud compute reservations delete RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.

  * `ZONE`: the zone where the reservation exists.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // Deletes the reservation for given project and zone
    func deleteReservation(w io.Writer, projectID, zone, reservationName string) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-a"
    	// reservationName := "your_reservation_name"
    
    	ctx := context.Background()
    	reservationsClient, err := compute.[NewReservationsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ReservationsClient_NewReservationsRESTClient)(ctx)
    	if err != nil {
    		return err
    	}
    	defer reservationsClient.Close()
    
    	req := &computepb.DeleteReservationRequest{
    		Project:     projectID,
    		Reservation: reservationName,
    		Zone:        zone,
    	}
    
    	op, err := reservationsClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete reservation: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reservation deleted\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteReservationRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteReservation {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "YOUR_PROJECT_ID";
        // Name of the reservation you want to delete.
        String reservationName = "YOUR_RESERVATION_NAME";
        // Name of the zone.
        String zone = "us-central1-a";
    
        deleteReservation(projectId, zone, reservationName);
      }
    
      // Delete a reservation from the project.
      public static void deleteReservation(String projectId, String zone, String reservationName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
           once, and can be reused for multiple requests. */
        try ([ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html) reservationsClient = [ReservationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationsClient.html).create()) {
    
          [DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteReservationRequest.html) deleteReservationRequest = [DeleteReservationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteReservationRequest.html).newBuilder()
              .setProject(projectId)
              .setZone(zone)
              .setReservation(reservationName)
              .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = reservationsClient.deleteAsync(
              deleteReservationRequest).get(5, TimeUnit.MINUTES);
    
          if (response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() == [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).Status.DONE) {
            System.out.println("Deleted reservation: " + reservationName);
          }
        }
      }
    }

###  Node.js 
    
    
    // Import the Compute library
    const computeLib = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    // Instantiate a reservationsClient
    const reservationsClient = new computeLib.[ReservationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    // Instantiate a zoneOperationsClient
    const zoneOperationsClient = new computeLib.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    /**
     * TODO(developer): Update/uncomment these variables before running the sample.
     */
    // The ID of the project where your reservation is located.
    const projectId = await reservationsClient.getProjectId();
    // The zone where your reservation is located.
    const zone = 'us-central1-a';
    // The name of the reservation to delete.
    // reservationName = 'reservation-01';
    
    async function callDeleteReservation() {
      // Delete the reservation
      const [response] = await reservationsClient.delete({
        project: projectId,
        reservation: reservationName,
        zone,
      });
    
      let operation = response.latestResponse;
    
      // Wait for the delete reservation operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await zoneOperationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log(`Reservation: ${reservationName} deleted.`);
    }
    await callDeleteReservation();

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
    
    
    def delete_compute_reservation(
        project_id: str,
        zone: str = "us-central1-a",
        reservation_name="your-reservation-name",
    ) -> ExtendedOperation:
        """
        Deletes a compute reservation in Google Cloud.
        Args:
            project_id (str): The ID of the Google Cloud project.
            zone (str): The zone of the reservation.
            reservation_name (str): The name of the reservation to delete.
        Returns:
            The operation response from the reservation deletion request.
        """
    
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ReservationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html)()
    
        operation = client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.reservations.ReservationsClient.html#google_cloud_compute_v1_services_reservations_ReservationsClient_delete)(
            project=project_id,
            zone=zone,
            reservation=reservation_name,
        )
    
        wait_for_extended_operation(operation, "Reservation deletion")
        print(operation.status)
        # Example response:
        # Status.DONE
        return operation
    
    

###  REST 

To delete a reservation, make a `DELETE` request to the [`reservation.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created the reservation.

  * `ZONE`: the zone where the reservation exists.

  * `RESERVATION_NAME`: the name of the reservation.




## What's next

  * Learn how to [view your reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-view).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
