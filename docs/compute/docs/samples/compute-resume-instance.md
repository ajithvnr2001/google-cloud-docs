---
url: https://docs.cloud.google.com/compute/docs/samples/compute-resume-instance/
title: Resume a suspended VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:52.255589+00:00
---

# Resume a suspended VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-resume-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Resume a suspended VM Stay organized with collections  Save and categorize content based on your preferences. 

Resume a suspended VM in the specified project and zone.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Suspend or resume a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)



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
    
    // resumeInstance resumes a suspended Google Compute Engine instance
    // (with unencrypted disks).
    func resumeInstance(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	getInstanceReq := &computepb.GetInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	instance, err := instancesClient.Get(ctx, getInstanceReq)
    	if err != nil {
    		return fmt.Errorf("unable to get instance: %w", err)
    	}
    
    	if instance.GetStatus() != "SUSPENDED" {
    		return fmt.Errorf(
    			"only suspended instances can be resumed, instance %s is in %s state",
    			instanceName,
    			instance.GetStatus(),
    		)
    	}
    
    	resumeInstanceReq := &computepb.ResumeInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	op, err := instancesClient.Resume(ctx, resumeInstanceReq)
    	if err != nil {
    		return fmt.Errorf("unable to resume instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance resumed\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ResumeInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // project: project ID or project number of the Cloud project your instance belongs to.
        // zone: name of the zone your instance belongs to.
        // instanceName: name of the instance your want to resume.
    
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
    
        resumeInstance(project, zone, instanceName);
      }
    
      // Resume a suspended Google Compute Engine instance (with unencrypted disks).
      // Instance state changes to RUNNING, if successfully resumed.
      public static void resumeInstance(String project, String zone, String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Instantiates a client.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          String currentInstanceState = instancesClient.get(project, zone, instanceName).getStatus();
    
          // Check if the instance is currently suspended.
          if (!currentInstanceState.equalsIgnoreCase([Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).SUSPENDED.toString())) {
            throw new RuntimeException(
                String.format("Only suspended instances can be resumed. Instance %s is in %s state.",
                    instanceName, currentInstanceState));
          }
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instancesClient.resumeAsync(project, zone, instanceName)
              .get(300, TimeUnit.SECONDS);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)() || !instancesClient.get(project, zone, instanceName).getStatus()
              .equalsIgnoreCase(
                  [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).RUNNING.toString())) {
            System.out.println("Cannot resume instance. Try again!");
            return;
          }
    
          System.out.printf("Instance resumed successfully ! %s", instanceName);
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
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Resumes a suspended Google Compute Engine instance (with unencrypted disks).
    async function resumeInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [instance] = await instancesClient.get({
        project: projectId,
        zone,
        instance: instanceName,
      });
    
      if (instance.status !== 'SUSPENDED') {
        throw new Error(
          'Only suspended instances can be resumed.' +
            `Instance ${instanceName} is in ${instance.status} state.`
        );
      }
    
      const [response] = await instancesClient.resume({
        project: projectId,
        zone,
        instance: instanceName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      // Wait for the create operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance resumed.');
    }
    
    resumeInstance();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\ResumeInstanceRequest;
    
    /**
     * Resume a suspended Google Compute Engine instance (with unencrypted disks).
     *
     * @param string $projectId Project ID or project number of the Cloud project your instance belongs to.
     * @param string $zone Name of the zone your instance belongs to.
     * @param string $instanceName Name of the instance you want to resume.
      *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function resume_instance(
        string $projectId,
        string $zone,
        string $instanceName
    ) {
        // Resume the suspended Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new ResumeInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->resume($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Instance %s resumed successfully' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Failed to resume instance: %s' . PHP_EOL, $error?->getMessage());
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
    
    
    def resume_instance(project_id: str, zone: str, instance_name: str) -> None:
        """
        Resume a suspended Google Compute Engine instance (with unencrypted disks).
        Args:
            project_id: project ID or project number of the Cloud project your instance belongs to.
            zone: name of the zone your instance belongs to.
            instance_name: name of the instance you want to resume.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        instance = instance_client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(
            project=project_id, zone=zone, instance=instance_name
        )
        if instance.status != [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Instance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Instance.html).Status.SUSPENDED.name:
            raise RuntimeError(
                f"Only suspended instances can be resumed. "
                f"Instance {instance_name} is in {instance.status} state."
            )
    
        operation = instance_client.[resume](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_resume)(
            project=project_id, zone=zone, instance=instance_name
        )
    
        wait_for_extended_operation(operation, "instance resumption")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
