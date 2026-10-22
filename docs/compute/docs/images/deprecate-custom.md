---
url: https://docs.cloud.google.com/compute/docs/images/deprecate-custom/
title: Deprecate a custom image \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:08.701281+00:00
---

# Deprecate a custom image  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/deprecate-custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Deprecate a custom image Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Compute Engine lets you deprecate a custom image that you own by setting the deprecation status on the image. Each deprecation status causes a different response from the server, helping you transition users away from unsupported images in a manageable way. Use the Google Cloud console, the Google Cloud CLI, or the Compute Engine API method to deprecate an image.

## Deprecation states

The following deprecation states are supported:

  * `ACTIVE`: the image is active and can be used as normal. Image families point to the most recent and active image in a family.
  * `DEPRECATED`: the image is marked deprecated but can still be used to [create a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_vm_from_a_custom_image). New links to this image are allowed. Image families no longer point to this image even if it is the most recent image in the family. If you create a VM with a deprecated image using the Google Cloud CLI, the request succeeds with a warning.

**Important:** Deprecating an image is irreversible. If you deprecate an image, you can't set it to `ACTIVE` again.
  * `OBSOLETE`: the image is marked obsolete and is no longer available for use. An error message is returned if you try to use this image in a request. Existing links to this image are still allowed.

  * `DELETED`: this image is deleted. An error message is returned if you try to use a deleted image.




## Before you begin

  * Read the [Images](https://docs.cloud.google.com/compute/docs/images) document.
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




## Deprecate a custom image

###  Console 

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

  2. For the image you want to deprecate, click more_vert **Actions**.

  3. Select **Deprecate**.

  4. For state, select either **Deprecated** or **Obsolete**. For more information about states, see Deprecation states.

  5. Optional: Specify a replacement image.

  6. Click **Deprecate Image**.




###  gcloud 

Use the [`gcloud compute images deprecate` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/deprecate) to set the deprecation status of an image.
    
    
    gcloud compute images deprecate IMAGE_NAME \
        --state STATE \
        --replacement REPLACEMENT
    

Replace the following:

  * `IMAGE_NAME`: the name of the image to deprecate
  * `STATE`: the deprecation state
  * `REPLACEMENT`: the image to replace the one that is deprecated



###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // Geg a disk image from the given project
    func deprecateDiskImage(
    	w io.Writer,
    	projectID, imageName string,
    ) error {
    	// projectID := "your_project_id"
    	// imageName := "my_image"
    
    	deprecationStatus := &computepb.DeprecationStatus{
    		State: proto.String(computepb.[DeprecationStatus_DEPRECATED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1/computepb.html#cloud_google_com_go_compute_apiv1_computepb_DeprecationStatus_UNDEFINED_STATE_DeprecationStatus_ACTIVE_DeprecationStatus_DELETED_DeprecationStatus_DEPRECATED_DeprecationStatus_OBSOLETE).String()),
    	}
    
    	ctx := context.Background()
    	imagesClient, err := compute.[NewImagesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_ImagesClient_NewImagesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImagesRESTClient: %w", err)
    	}
    	defer imagesClient.Close()
    
    	source_req := &computepb.DeprecateImageRequest{
    		Project:                   projectID,
    		Image:                     imageName,
    		DeprecationStatusResource: deprecationStatus,
    	}
    
    	op, err := imagesClient.Deprecate(ctx, source_req)
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disk image %s deprecated\n", imageName)
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[DeprecateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecateImageRequest.html);
    import com.google.cloud.compute.v1.[DeprecationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecationStatus.html);
    import com.google.cloud.compute.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html);
    import com.google.cloud.compute.v1.[ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html);
    import java.io.IOException;
    import java.util.UUID;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SetImageDeprecationStatus {
      public static void main(String[] args)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Google Cloud project you want to use.
        String projectId = "your-project-id";
        // Name of the image you want to update.
        String imageName = "your-image-name";
        // The status you want to set for the image. Available values are available in
        // `compute_v1.DeprecationStatus.State` enum. Learn more about image deprecation statuses:
        // https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#deprecation-states
        [DeprecationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecationStatus.html).State status = [DeprecationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecationStatus.html).State.DEPRECATED;
    
        setDeprecationStatus(projectId, imageName, status);
      }
    
      // Modify the deprecation status of an image.
      public static [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) setDeprecationStatus(String projectId, String imageName,
                                               [DeprecationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecationStatus.html).State status)
              throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html) client = [ImagesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html).create()) {
          [DeprecationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecationStatus.html) deprecationStatusResource = [DeprecationStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecationStatus.html).newBuilder()
                  .setState(status.name())
                  .build();
          [DeprecateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecateImageRequest.html) request = [DeprecateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecateImageRequest.html).newBuilder()
                  .setProject(projectId)
                  .setImage(imageName)
                  .[setDeprecationStatusResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeprecateImageRequest.Builder.html#com_google_cloud_compute_v1_DeprecateImageRequest_Builder_setDeprecationStatusResource_com_google_cloud_compute_v1_DeprecationStatus_)(deprecationStatusResource)
                  .setRequestId(UUID.randomUUID().toString())
                  .build();
    
          client.[deprecateCallable](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ImagesClient.html#com_google_cloud_compute_v1_ImagesClient_deprecateCallable__)().futureCall(request).get(60, TimeUnit.SECONDS);
    
          [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html) image = client.get(projectId, imageName);
    
          System.out.printf("Status '%s' has been updated successfully",
                  image.[getDeprecated](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Image.html#com_google_cloud_compute_v1_Image_getDeprecated__)().getState());
    
          return image;
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
    
    
    def set_deprecation_status(
        project_id: str, image_name: str, status: [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeprecationStatus](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeprecationStatus.html).State
    ) -> None:
        """
        Modify the deprecation status of an image.
    
        Note: Image objects by default don't have the `deprecated` attribute at all unless it's set.
    
        Args:
            project_id: project ID or project number of the Cloud project that hosts the image.
            image_name: name of the image you want to modify
            status: the status you want to set for the image. Available values are available in
                `compute_v1.DeprecationStatus.State` enum. Learn more about image deprecation statuses:
                https://cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#deprecation-states
        """
        image_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ImagesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html)()
        deprecation_status = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DeprecationStatus](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.DeprecationStatus.html)()
        deprecation_status.state = status.name
        operation = image_client.[deprecate](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.images.ImagesClient.html#google_cloud_compute_v1_services_images_ImagesClient_deprecate)(
            project=project_id,
            image=image_name,
            deprecation_status_resource=deprecation_status,
        )
    
        wait_for_extended_operation(operation, "changing deprecation state of an image")
    
    

###  REST 

Make a `POST` request to the [`images().deprecate` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/deprecate). Specify the name of the image you want to deprecate.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images/RESOURCE_ID/deprecate
    
    {
      "state": "STATE",
      "replacement": "REPLACEMENT"
    }
    

Replace the following:

  * `PROJECT_ID`: the project to which the image belongs.
  * `RESOURCE_ID`: the name of the image that you are deprecating.
  * `STATE`: the deprecation state of this resource.
  * `REPLACEMENT`: the image to replace the one that is deprecated.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
