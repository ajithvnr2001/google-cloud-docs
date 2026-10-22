---
url: https://docs.cloud.google.com/compute/docs/samples/compute-images-create-from-snapshot/
title: Create an image from a snapshot \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:06.319355+00:00
---

# Create an image from a snapshot  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-images-create-from-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create an image from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates an image based on a snapshot.

## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // Creates a disk image from an existing image
    func createImageFromSnapshot(
    	w io.Writer,
    	projectID, snapshotName, imageName string,
    ) error {
    	// projectID := "your_project_id"
    	// snapshotName := "your_image_name"
    	// imageName := "my_image"
    
    	// // If storageLocations empty, automatically selects the closest one to the source
    	storageLocations := []string{}
    
    	ctx := context.Background()
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	snapshotsClient, err := compute.[NewSnapshotsRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_SnapshotsClient_NewSnapshotsRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewSnapshotsRESTClient: %w", err)
    	}
    	defer snapshotsClient.Close()
    
    	// Get the source image
    	source_req := &computepb.GetSnapshotRequest{
    		Snapshot: snapshotName,
    		Project:  projectID,
    	}
    
    	snapshot, err := snapshotsClient.Get(ctx, source_req)
    	if err != nil {
    		return fmt.Errorf("unable to get source image: %w", err)
    	}
    
    	// Create the image
    	req := computepb.InsertImageRequest{
    		ImageResource: &computepb.Image{
    			Name:             &imageName,
    			SourceSnapshot:   snapshot.SelfLink,
    			StorageLocations: storageLocations,
    		},
    		Project: projectID,
    	}
    
    	op, err := imagesClient.Insert(ctx, &req)
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk image %s created\n", imageName)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html);
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import com.google.cloud.compute.v1.[InsertImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.html);
    import com.google.cloud.compute.v1.[Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html);
    import com.google.cloud.compute.v1.[SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateImageFromSnapshot {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Name of the snapshot you want to use as a base of your image.
        String sourceSnapshotName = "your-snapshot-name";
        // Name of the image you want to create.
        String imageName = "your-image-name";
        // Name of the project that hosts the source image. If left unset, it's assumed to equal
        // the `projectId`.
        String sourceProjectId = "your-source-project-id";
        // An iterable collection of guest features you want to enable for the bootable image.
        // Learn more about Guest OS features here:
        // https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features
        List<String> guestOsFeature = new ArrayList<>();
        // The storage location of your image. For example, specify "us" to store the image in the
        // `us` multi-region, or "us-central1" to store it in the `us-central1` region.
        // If you do not make a selection,
        // Compute Engine stores the image in the multi-region closest to your image's source location.
        String storageLocation = "your-storage-location";
    
        createImageFromSnapshot(projectId, sourceSnapshotName, imageName,
                sourceProjectId, guestOsFeature, storageLocation);
      }
    
      // Creates an image based on a snapshot.
      public static [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) createImageFromSnapshot(String projectId, String sourceSnapshotName,
                                                  String imageName, String sourceProjectId,
                                                  List<String> guestOsFeatures, String storageLocation)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        if (sourceProjectId == null) {
          sourceProjectId = projectId;
        }
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) imagesClient = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create();
             [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html) snapshotsClient = [SnapshotsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SnapshotsClient.html).create()) {
          [Snapshot](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html) snapshot = snapshotsClient.get(sourceProjectId, sourceSnapshotName);
    
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html).Builder imageResource = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html).newBuilder()
                  .setName(imageName)
                  .setSourceSnapshot(snapshot.[getSelfLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Snapshot.html#com_google_cloud_compute_v1_Snapshot_getSelfLink__)());
    
          if (storageLocation != null) {
            imageResource.addStorageLocations(storageLocation);
          }
          if (guestOsFeatures != null) {
            for (String feature : guestOsFeatures) {
              [GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html).Builder guestOsFeatureBuilder = [GuestOsFeature](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GuestOsFeature.html).newBuilder()
                      .setType(feature);
    
              imageResource.addGuestOsFeatures(guestOsFeatureBuilder);
            }
          }
    
          [InsertImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.html) request = [InsertImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertImageRequest.html).newBuilder()
                  .setProject(projectId)
                  .setRequestId(UUID.randomUUID().toString())
                  .setImageResource(imageResource)
                  .build();
          imagesClient.insertCallable().futureCall(request).get(60, TimeUnit.SECONDS);
    
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) image = imagesClient.get(projectId, imageName);
    
          System.out.printf("Image '%s' has been created successfully", image.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html#com_google_cloud_compute_v1_Image_getName__)());
    
          return image;
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    
    def create_image_from_snapshot(
        project_id: str,
        source_snapshot_name: str,
        image_name: str,
        source_project_id: str | None = None,
        guest_os_features: Iterable[str] | None = None,
        storage_location: str | None = None,
    ) -> compute_v1.Image:
        """
        Creates an image based on a snapshot.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to place your new image in.
            source_snapshot_name: name of the snapshot you want to use as a base of your image.
            image_name: name of the image you want to create.
            source_project_id: name of the project that hosts the source snapshot. If left unset, it's assumed to equal
                the `project_id`.
            guest_os_features: an iterable collection of guest features you want to enable for the bootable image.
                Learn more about Guest OS features here:
                https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features
            storage_location: the storage location of your image. For example, specify "us" to store the image in the
                `us` multi-region, or "us-central1" to store it in the `us-central1` region. If you do not make a selection,
                 Compute Engine stores the image in the multi-region closest to your image's source location.
    
        Returns:
            An Image object.
        """
        if source_project_id is None:
            source_project_id = project_id
    
        snapshot_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[SnapshotsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html)()
        image_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ImagesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html)()
        src_snapshot = snapshot_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.snapshots.SnapshotsClient.html#google_cloud_compute_v1_services_snapshots_SnapshotsClient_get)(
            project=source_project_id, snapshot=source_snapshot_name
        )
    
        image = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Image](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Image.html)()
        image.name = image_name
        image.source_snapshot = src_snapshot.self_link
    
        if storage_location:
            image.storage_locations = [storage_location]
    
        if guest_os_features:
            image.guest_os_features = [
                [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.GuestOsFeature.html)(type_=feature) for feature in guest_os_features
            ]
    
        operation = image_client.[insert](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html#google_cloud_compute_v1_services_images_ImagesClient_insert)(project=project_id, image_resource=image)
    
        wait_for_extended_operation(operation, "image creation from snapshot")
    
        return image_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html#google_cloud_compute_v1_services_images_ImagesClient_get)(project=project_id, image=image_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
