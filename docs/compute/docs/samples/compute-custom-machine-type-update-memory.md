---
url: https://docs.cloud.google.com/compute/docs/samples/compute-custom-machine-type-update-memory/
title: Add memory to an existing VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:07.910904+00:00
---

# Add memory to an existing VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-custom-machine-type-update-memory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Add memory to an existing VM Stay organized with collections  Save and categorize content based on your preferences. 

Update a VM with extended memory per vCPU.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a VM with a custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    	"google.golang.org/protobuf/proto"
    )
    
    // modifyInstanceWithExtendedMemory sends an instance creation request
    // to the Compute Engine API and waits for it to complete.
    func modifyInstanceWithExtendedMemory(
    	w io.Writer,
    	projectID, zone, instanceName string,
    	newMemory int,
    ) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	// newMemory := 256 // the amount of memory for the VM instance, in megabytes.
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	reqInstance := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, reqInstance)
    	if err != nil {
    		return fmt.Errorf("unable to get instance: %w", err)
    	}
    
    	containsString := func(s []string, str string) bool {
    		for _, v := range s {
    			if v == str {
    				return true
    			}
    		}
    
    		return false
    	}
    
    	if !(strings.Contains(instance.GetMachineType(), "machineTypes/n1-") ||
    		strings.Contains(instance.GetMachineType(), "machineTypes/n2-") ||
    		strings.Contains(instance.GetMachineType(), "machineTypes/n2d-")) {
    		return fmt.Errorf("extra memory is available only for N1, N2 and N2D CPUs")
    	}
    
    	// Make sure that the machine is turned off
    	if !containsString([]string{"TERMINATED", "STOPPED"}, instance.GetStatus()) {
    		reqStop := &computepb.StopInstanceRequest{
    			Project:  projectID,
    			Zone:     zone,
    			Instance: instanceName,
    		}
    
    		op, err := instancesClient.Stop(ctx, reqStop)
    		if err != nil {
    			return fmt.Errorf("unable to stop instance: %w", err)
    		}
    
    		if err = op.Wait(ctx); err != nil {
    			return fmt.Errorf("unable to wait for the operation: %w", err)
    		}
    	}
    
    	// Modify the machine definition, remember that extended memory
    	// is available only for N1, N2 and N2D CPUs
    	machineType := instance.GetMachineType()
    	start := machineType[:strings.LastIndex(machineType, "-")]
    
    	updateReq := &computepb.SetMachineTypeInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    		InstancesSetMachineTypeRequestResource: &computepb.InstancesSetMachineTypeRequest{
    			MachineType: proto.String(fmt.Sprintf("%s-%v-ext", start, newMemory)),
    		},
    	}
    	op, err := instancesClient.SetMachineType(ctx, updateReq)
    	if err != nil {
    		return fmt.Errorf("unable to update instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance updated\n")
    
    	return nil
    
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[InstancesSetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineTypeRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest.html);
    import com.google.cloud.compute.v1.[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateMemory {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
        // Name of the zone to create the instance in. For example: "us-west3-b".
        String zone = "google-cloud-zone";
        // Name of the new virtual machine (VM) instance.
        String instanceName = "instance-name";
        // The amount of memory for the VM instance, in megabytes.
        int newMemory = 256;
    
        modifyInstanceWithExtendedMemory(projectId, zone, instanceName, newMemory);
      }
    
      // Modify an existing VM to use extended memory and return the modified Instance.
      public static void modifyInstanceWithExtendedMemory(
          String project, String zone, String instanceName, int newMemory)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          // Create the get instance request object.
          [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html) getInstanceRequest = [GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName)
              .build();
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(getInstanceRequest);
    
          // Check the machine type.
          if (!(instance.[getMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getMachineType__)().contains("machineTypes/n1-")
              || instance.[getMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getMachineType__)().contains("machineTypes/n2-")
              || instance.[getMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getMachineType__)().contains("machineTypes/n2d-"))) {
            System.out.println("extra memory is available only for N1, N2 and N2D CPUs");
            return;
          }
    
          // Make sure that the machine is turned off.
          if (!(instance.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getStatus__)().equals([Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).TERMINATED.toString())
              || instance.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getStatus__)().equals([Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).STOPPED.toString()))) {
    
            [StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest.html) stopInstanceRequest = [StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest.html).newBuilder()
                .setProject(project)
                .setZone(zone)
                .setInstance(instanceName)
                .build();
    
            OperationFuture<Operation, Operation> operation = instancesClient.[stopAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_stopAsync_com_google_cloud_compute_v1_StopInstanceRequest_)(
                stopInstanceRequest);
            [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
            if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
              System.out.printf("Unable to stop instance %s", response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
              return;
            }
          }
    
          // Modify the machine definition. Note that extended memory
          // is available only for N1, N2 and N2D CPUs.
          String machineType = instance.[getMachineType](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getMachineType__)();
          String start = machineType.substring(0, machineType.lastIndexOf("-"));
    
          // Create the machine type instance request object.
          [SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest.html) setMachineTypeInstanceRequest =
              [SetMachineTypeInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest.html).newBuilder()
                  .setProject(project)
                  .setZone(zone)
                  .setInstance(instanceName)
                  .[setInstancesSetMachineTypeRequestResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SetMachineTypeInstanceRequest.Builder.html#com_google_cloud_compute_v1_SetMachineTypeInstanceRequest_Builder_setInstancesSetMachineTypeRequestResource_com_google_cloud_compute_v1_InstancesSetMachineTypeRequest_)([InstancesSetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineTypeRequest.html).newBuilder()
                      .setMachineType(String.format("%s-%d-ext", start, newMemory))
                      .build())
                  .build();
    
          // Invoke the API with the request object and wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient.[setMachineTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_setMachineTypeAsync_com_google_cloud_compute_v1_SetMachineTypeInstanceRequest_)(setMachineTypeInstanceRequest)
              .get(3, TimeUnit.MINUTES);
    
          // Check for errors.
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.printf("Unable to update instance %s", response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
            return;
          }
          System.out.println("Instance updated!");
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
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    // const newMemory = 256;
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function modifyInstanceWithExtendedMemory() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instance] = await instancesClient.get({
        project: projectId,
        zone,
        instance: instanceName,
      });
    
      if (
        !['machineTypes/n1-', 'machineTypes/n2-', 'machineTypes/n2d-'].some(
          type => instance.machineType.includes(type)
        )
      ) {
        throw new Error('extra memory is available only for N1, N2 and N2D CPUs');
      }
    
      // Make sure that the machine is turned off
      if (!['TERMINATED', 'STOPPED'].some(status => instance.status === status)) {
        const [response] = await instancesClient.stop({
          project: projectId,
          zone,
          instance: instanceName,
        });
    
        let operation = response.latestResponse;
        const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
        // Wait for the stop operation to complete.
        while (operation.status !== 'DONE') {
          [operation] = await operationsClient.wait({
            operation: operation.name,
            project: projectId,
            zone: operation.zone.split('/').pop(),
          });
        }
      }
    
      // Modify the machine definition, remember that extended memory
      // is available only for N1, N2 and N2D CPUs
    
      const start = instance.machineType.substring(
        0,
        instance.machineType.lastIndexOf('-')
      );
    
      const [response] = await instancesClient.setMachineType({
        project: projectId,
        zone,
        instance: instanceName,
        instancesSetMachineTypeRequestResource: {
          machineType: `${start}-${newMemory}-ext`,
        },
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the update operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance updated.');
    }
    
    modifyInstanceWithExtendedMemory();

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from __future__ import annotations
    
    import sys
    import time
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
    
    
    def add_extended_memory_to_instance(
        project_id: str, zone: str, instance_name: str, new_memory: int
    ):
        """
        Modify an existing VM to use extended memory.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone to create the instance in. For example: "us-west3-b"
            instance_name: name of the new virtual machine (VM) instance.
            new_memory: the amount of memory for the VM instance, in megabytes.
    
        Returns:
            Instance object.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
        instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
            project=project_id, zone=zone, instance=instance_name
        )
    
        if not (
            "n1-" in instance.machine_type
            or "n2-" in instance.machine_type
            or "n2d-" in instance.machine_type
        ):
            raise RuntimeError("Extra memory is available only for N1, N2 and N2D CPUs.")
    
        # Make sure that the machine is turned off
        if instance.status not in (
            instance.Status.TERMINATED.name,
            instance.Status.STOPPED.name,
        ):
            operation = instance_client.[stop](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_stop)(
                project=project_id, zone=zone, instance=instance_name
            )
            wait_for_extended_operation(operation, "instance stopping")
            start = time.time()
            while instance.status not in (
                instance.Status.TERMINATED.name,
                instance.Status.STOPPED.name,
            ):
                # Waiting for the instance to be turned off.
                instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
                    project=project_id, zone=zone, instance=instance_name
                )
                time.sleep(2)
                if time.time() - start >= 300:  # 5 minutes
                    raise TimeoutError()
    
        # Modify the machine definition, remember that extended memory is available only for N1, N2 and N2D CPUs
        start, end = instance.machine_type.rsplit("-", maxsplit=1)
        instance.machine_type = start + f"-{new_memory}-ext"
        # TODO: If you prefer to use the CustomMachineType helper class, uncomment this code and comment the 2 lines above
        # Using CustomMachineType helper
        # cmt = CustomMachineType.from_str(instance.machine_type)
        # cmt.memory_mb = new_memory
        # cmt.extra_memory_used = True
        # instance.machine_type = str(cmt)
        operation = instance_client.[update](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_update)(
            project=project_id,
            zone=zone,
            instance=instance_name,
            instance_resource=instance,
        )
        wait_for_extended_operation(operation, "instance update")
    
        return instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
