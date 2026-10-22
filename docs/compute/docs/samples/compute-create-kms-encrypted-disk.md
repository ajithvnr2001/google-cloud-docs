---
url: https://docs.cloud.google.com/compute/docs/samples/compute-create-kms-encrypted-disk/
title: Create a KMS encrypted disk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:33.513284+00:00
---

# Create a KMS encrypted disk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-create-kms-encrypted-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Create a KMS encrypted disk Stay organized with collections  Save and categorize content based on your preferences. 

This sample creates a new disk encrypted with a customer-supplied encryption key from Cloud KMS.

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
    	"google.golang.org/protobuf/proto"
    )
    
    // createKmsEncryptedDisk creates a new disk in a project in given zone.
    // If you do not provide diskLink or imageLink, an empty disk will be created.
    func createKmsEncryptedDisk(
    	w io.Writer,
    	projectID, zone, diskName, diskType string,
    	diskSizeGb int64,
    	kmsKeyLink, imageLink, diskLink, snapshotLink string,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "us-west3-b" // should match diskType below
    	// diskName := "your_disk_name"
    	// diskType := "zones/us-west3/diskTypes/pd-ssd"
    	// diskSizeGb := 120
    	// kmsKeyLink := "projects/your_kms_project_id/locations/us-central1/keyRings/your_key_ring/cryptoKeys/your_key"
    	// // Only use one of these at a time
    	// diskLink := "projects/your_project_id/global/disks/disk_name"
    	// imageLink := "projects/your_project_id/global/images/image_name"
    	// snapshotLink := "projects/your_project_id/global/snapshots/snapshot_name"
    
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
    			Name:   proto.String(diskName),
    			Zone:   proto.String(zone),
    			Type:   proto.String(diskType),
    			SizeGb: proto.Int64(diskSizeGb),
    			DiskEncryptionKey: &computepb.CustomerEncryptionKey{
    				KmsKeyName: &kmsKeyLink,
    			},
    		},
    	}
    
    	// if a source disk, image or snapshot has been specified, apply it.
    	// These arguments are mutually exclusive.
    	if diskLink != "" {
    		req.DiskResource.SourceDisk = proto.String(diskLink)
    	} else if imageLink != "" {
    		req.DiskResource.SourceImage = proto.String(imageLink)
    	} else if snapshotLink != "" {
    		req.DiskResource.SourceSnapshot = proto.String(snapshotLink)
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
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html);
    import com.google.cloud.compute.v1.[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html);
    import com.google.cloud.compute.v1.[DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html);
    import com.google.cloud.compute.v1.[InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateKmsEncryptedDisk {
    
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
    
        // URL of the key from KMS. The key might be from another project, as
        // long as you have access to it. The data will be encrypted with the same key
        // in the new disk. This value uses following format:
        // "projects/{kms_project_id}/locations/{region}/keyRings/{key_ring}/cryptoKeys/{key}"
        String kmsKeyName = "kms-key-name";
    
        // A link to the disk you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/zones/{zone}/disks/{disk_name}"
        String diskLink = String.format("projects/%s/zones/%s/disks/%s", "PROJECT_NAME", "ZONE",
            "DISK_NAME");
    
        // A link to the image you want to use as a source for the new disk.
        // This value uses the following format:
        // "projects/{project_name}/global/images/{image_name}"
        String imageLink = String.format("projects/%s/global/images/%s", "PROJECT_NAME", "IMAGE_NAME");
    
        createKmsEncryptedDisk(project, zone, diskName, diskType, diskSizeGb, kmsKeyName, diskLink,
            imageLink);
      }
    
      // Creates a zonal disk in a project. If you do not provide values for diskLink or imageLink,
      // an empty disk will be created.
      public static void createKmsEncryptedDisk(String project, String zone, String diskName,
          String diskType, int diskSizeGb, String kmsKeyName, String diskLink, String imageLink)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `disksClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html) disksClient = [DisksClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DisksClient.html).create()) {
    
          // Create a disk and set the KMS encryption key name.
          [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).Builder diskBuilder = [Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Disk.html).newBuilder()
              .setZone(zone)
              .setName(diskName)
              .setType(diskType)
              .setSizeGb(diskSizeGb)
              .setDiskEncryptionKey([CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html).newBuilder()
                  .setKmsKeyName(kmsKeyName)
                  .build());
    
          // Set source disk if diskLink is not empty.
          if (!diskLink.isEmpty()) {
            diskBuilder.setSourceDisk(diskLink);
          }
    
          // Set source image if imageLink is not empty.
          if (!imageLink.isEmpty()) {
            diskBuilder.setSourceImage(imageLink);
          }
    
          // Wait for the insert disk operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = disksClient.insertAsync(
              [InsertDiskRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertDiskRequest.html).newBuilder()
                  .setProject(project)
                  .setZone(zone)
                  .setDiskResource(diskBuilder.build())
                  .build()).get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Disk creation failed!");
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(operation.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)().toString());
          }
          System.out.println(
              "Disk created with KMS encryption key. Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    
    def create_kms_encrypted_disk(
        project_id: str,
        zone: str,
        disk_name: str,
        disk_type: str,
        disk_size_gb: int,
        kms_key_name: str,
        disk_link: str | None = None,
        image_link: str | None = None,
    ) -> compute_v1.Disk:
        """
        Creates a zonal disk in a project. If you do not provide values for disk_link or image_link,
        an empty disk will be created.
    
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
            kms_key_name: URL of the key from KMS. The key might be from another project, as
                long as you have access to it. The data will be encrypted with the same key
                in the new disk. This value uses following format:
                "projects/{kms_project_id}/locations/{region}/keyRings/{key_ring}/cryptoKeys/{key}"
            disk_link: a link to the disk you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/zones/{zone}/disks/{disk_name}"
            image_link: a link to the image you want to use as a source for the new disk.
                This value uses the following format: "projects/{project_name}/global/images/{image_name}"
    
        Returns:
            An attachable disk.
        """
        disk_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[DisksClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.DisksClient.html)()
        disk = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Disk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Disk.html)()
        disk.zone = zone
        disk.size_gb = disk_size_gb
        if disk_link:
            disk.source_disk = disk_link
        if image_link:
            disk.source_image = image_link
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
