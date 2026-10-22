---
url: https://docs.cloud.google.com/compute/docs/samples/compute-start-enc-instance/
title: Start a VM with encrypted disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:15.789886+00:00
---

# Start a VM with encrypted disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-start-enc-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Start a VM with encrypted disks Stay organized with collections  Save and categorize content based on your preferences. 

Provide an encryption key and start a VM instance that has encrypted disks.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Stop or restart a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)



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
    
    // startInstanceWithEncKey starts a stopped Google Compute Engine instance (with encrypted disks).
    func startInstanceWithEncKey(w io.Writer, projectID, zone, instanceName, key string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// key := "your_encryption_key"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	instanceReq := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, instanceReq)
    	if err != nil {
    		return fmt.Errorf("unable to get instance: %w", err)
    	}
    
    	req := &computepb.StartWithEncryptionKeyInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    		InstancesStartWithEncryptionKeyRequestResource: &computepb.InstancesStartWithEncryptionKeyRequest{
    			Disks: []*computepb.CustomerEncryptionKeyProtectedDisk{
    				{
    					Source: proto.String(instance.GetDisks()[0].GetSource()),
    					DiskEncryptionKey: &computepb.CustomerEncryptionKey{
    						RawKey: proto.String(key),
    					},
    				},
    			},
    		},
    	}
    
    	op, err := instancesClient.StartWithEncryptionKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to start instance with encryption key: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance with encryption key started\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html);
    import com.google.cloud.compute.v1.[CustomerEncryptionKeyProtectedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKeyProtectedDisk.html);
    import com.google.cloud.compute.v1.[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesStartWithEncryptionKeyRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class StartEncryptedInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        /* project: project ID or project number of the Cloud project your instance belongs to.
           zone: name of the zone your instance belongs to.
           instanceName: name of the instance your want to start.
           key: bytes object representing a raw base64 encoded key to your machines boot disk.
                For more information about disk encryption see:
                https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#specifications
         */
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        String key = "raw-key";
    
        startEncryptedInstance(project, zone, instanceName, key);
      }
    
      // Starts a stopped Google Compute Engine instance (with encrypted disks).
      public static void startEncryptedInstance(String project, String zone, String instanceName,
          String key)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
           once, and can be reused for multiple requests. After completing all of your requests, call
           the `instancesClient.close()` method on the client to safely
           clean up any remaining background resources. */
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html) getInstanceRequest = [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName).build();
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(getInstanceRequest);
    
          // Prepare the information about disk encryption.
          [CustomerEncryptionKeyProtectedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKeyProtectedDisk.html) protectedDisk = [CustomerEncryptionKeyProtectedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKeyProtectedDisk.html)
              .newBuilder()
              /* Use raw_key to send over the key to unlock the disk
                 To use a key stored in KMS, you need to provide:
                 `kms_key_name` and `kms_key_service_account`
               */
              .setDiskEncryptionKey([CustomerEncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.html).newBuilder()
                  .[setRawKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CustomerEncryptionKey.Builder.html#com_google_cloud_compute_v1_CustomerEncryptionKey_Builder_setRawKey_java_lang_String_)(key).build())
              .setSource(instance.[getDisks](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getDisks_int_)(0).getSource())
              .build();
    
          [InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesStartWithEncryptionKeyRequest.html) startWithEncryptionKeyRequest =
              [InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesStartWithEncryptionKeyRequest.html).newBuilder()
                  .addDisks(protectedDisk).build();
    
          [StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest.html) encryptionKeyInstanceRequest =
              [StartWithEncryptionKeyInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest.html).newBuilder()
                  .setProject(project)
                  .setZone(zone)
                  .setInstance(instanceName)
                  .[setInstancesStartWithEncryptionKeyRequestResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartWithEncryptionKeyInstanceRequest.Builder.html#com_google_cloud_compute_v1_StartWithEncryptionKeyInstanceRequest_Builder_setInstancesStartWithEncryptionKeyRequestResource_com_google_cloud_compute_v1_InstancesStartWithEncryptionKeyRequest_)(startWithEncryptionKeyRequest)
                  .build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.[startWithEncryptionKeyAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_startWithEncryptionKeyAsync_com_google_cloud_compute_v1_StartWithEncryptionKeyInstanceRequest_)(
              encryptionKeyInstanceRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() == [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).DONE) {
            System.out.println("Encrypted instance started successfully ! ");
          }
        }
      }
    
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME'
    // const key = 'YOUR_KEY_STRING'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function startInstanceWithEncryptionKey() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instance] = await instancesClient.get({
        project: projectId,
        zone,
        instance: instanceName,
      });
    
      const [response] = await instancesClient.startWithEncryptionKey({
        project: projectId,
        zone,
        instance: instanceName,
        instancesStartWithEncryptionKeyRequestResource: {
          disks: [
            {
              source: instance.disks[0].source,
              diskEncryptionKey: {
                rawKey: key,
              },
            },
          ],
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance with encryption key started.');
    }
    
    startInstanceWithEncryptionKey();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\CustomerEncryptionKey;
    use Google\Cloud\Compute\V1\CustomerEncryptionKeyProtectedDisk;
    use Google\Cloud\Compute\V1\GetInstanceRequest;
    use Google\Cloud\Compute\V1\InstancesStartWithEncryptionKeyRequest;
    use Google\Cloud\Compute\V1\StartWithEncryptionKeyInstanceRequest;
    
    /**
     * Starts a stopped Google Compute Engine instance (with encrypted disks).
     *
     * @param string $projectId Project ID or project number of the Cloud project your instance belongs to.
     * @param string $zone Name of the zone your instance belongs to.
     * @param string $instanceName Name of the instance you want to stop.
     * @param string $key Bytes object representing a raw base64 encoded key to your instance's boot disk.
     *                    For more information about disk encryption see:
     *                    https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#specifications
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function start_instance_with_encryption_key(
        string $projectId,
        string $zone,
        string $instanceName,
        string $key
    ) {
        // Initiate the InstancesClient.
        $instancesClient = new InstancesClient();
    
        // Get data about the instance.
        $request = (new GetInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $instanceData = $instancesClient->get($request);
    
        // Use `setRawKey` to send over the key to unlock the disk
        // To use a key stored in KMS, you need to use `setKmsKeyName` and `setKmsKeyServiceAccount`
        $customerEncryptionKey = (new CustomerEncryptionKey())
            ->setRawKey($key);
    
        /** @var \Google\Cloud\Compute\V1\AttachedDisk */
        $disk = $instanceData->getDisks()[0];
    
        // Prepare the information about disk encryption.
        $diskData = (new CustomerEncryptionKeyProtectedDisk())
            ->setSource($disk->getSource())
            ->setDiskEncryptionKey($customerEncryptionKey);
    
        // Set request with one disk.
        $instancesStartWithEncryptionKeyRequest = (new InstancesStartWithEncryptionKeyRequest())
            ->setDisks(array($diskData));
    
        // Start the instance with encrypted disk.
        $request2 = (new StartWithEncryptionKeyInstanceRequest())
            ->setInstance($instanceName)
            ->setInstancesStartWithEncryptionKeyRequestResource($instancesStartWithEncryptionKeyRequest)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->startWithEncryptionKey($request2);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Instance %s started successfully' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Starting instance failed: %s' . PHP_EOL, $error?->getMessage());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    
    def start_instance_with_encryption_key(
        project_id: str, zone: str, instance_name: str, key: bytes
    ) -> None:
        """
        Starts a stopped Google Compute Engine instance (with encrypted disks).
        Args:
            project_id: project ID or project number of the Cloud project your instance belongs to.
            zone: name of the zone your instance belongs to.
            instance_name: name of the instance your want to start.
            key: bytes object representing a raw base64 encoded key to your machines boot disk.
                For more information about disk encryption see:
                https://cloud.google.com/compute/docs/disks/customer-supplied-encryption#specifications
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        instance_data = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
            project=project_id, zone=zone, instance=instance_name
        )
    
        # Prepare the information about disk encryption
        disk_data = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[CustomerEncryptionKeyProtectedDisk](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKeyProtectedDisk.html)()
        disk_data.source = instance_data.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html)[0].source
        disk_data.disk_encryption_key = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.CustomerEncryptionKey.html)()
        # Use raw_key to send over the key to unlock the disk
        # To use a key stored in KMS, you need to provide `kms_key_name` and `kms_key_service_account`
        disk_data.disk_encryption_key.raw_key = key
        enc_data = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesStartWithEncryptionKeyRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstancesStartWithEncryptionKeyRequest.html)()
        enc_data.[disks](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.disks.html) = [disk_data]
    
        operation = instance_client.[start_with_encryption_key](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_start_with_encryption_key)(
            project=project_id,
            zone=zone,
            instance=instance_name,
            instances_start_with_encryption_key_request_resource=enc_data,
        )
    
        wait_for_extended_operation(operation, "instance start (with encrypted disk)")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
