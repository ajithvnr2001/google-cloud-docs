---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-delete/
title: Delete a VM instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:08.138332+00:00
---

# Delete a VM instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Delete a VM instance Stay organized with collections  Save and categorize content based on your preferences. 

Delete an instance based on the project, zone, and instance name that you provide.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Delete a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)
  * [Move a VM instance between zones or regions](https://docs.cloud.google.com/compute/docs/instances/moving-instance-across-zones)
  * [Using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.Compute.V1;
    using System.Threading.Tasks;
    
    public class DeleteInstanceAsyncSample
    {
        public async Task DeleteInstanceAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string zone = "us-central1-a",
            string machineName = "test-machine")
        {
    
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            InstancesClient client = await InstancesClient.CreateAsync();
    
            // Make the request to delete a VM instance.
            var instanceDeletion = await client.DeleteAsync(projectId, zone, machineName);
    
            // Wait for the operation to complete using client-side polling.
            await instanceDeletion.PollUntilCompletedAsync();
        }
    }
    

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
    
    // deleteInstance sends a delete request to the Compute Engine API and waits for it to complete.
    func deleteInstance(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    	ctx := context.Background()
    	instancesClient, err := compute.NewInstancesRESTClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.DeleteInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	op, err := instancesClient.Delete(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance deleted\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.OperationFuture;
    import com.google.cloud.compute.v1.DeleteInstanceRequest;
    import com.google.cloud.compute.v1.InstancesClient;
    import com.google.cloud.compute.v1.Operation;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteInstance {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
        deleteInstance(project, zone, instanceName);
      }
    
      // Delete the instance specified by `instanceName`
      // if it's present in the given project and zone.
      public static void deleteInstance(String project, String zone, String instanceName)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try (InstancesClient instancesClient = InstancesClient.create()) {
    
          System.out.printf("Deleting instance: %s ", instanceName);
    
          // Describe which instance is to be deleted.
          DeleteInstanceRequest deleteInstanceRequest = DeleteInstanceRequest.newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName).build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.deleteAsync(
              deleteInstanceRequest);
          // Wait for the operation to complete.
          Operation response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.hasError()) {
            System.out.println("Instance deletion failed ! ! " + response);
            return;
          }
          System.out.println("Operation Status: " + response.getStatus());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('@google-cloud/compute');
    
    // Delete the instance specified by `instanceName` if it's present in the given project and zone.
    async function deleteInstance() {
      const instancesClient = new compute.InstancesClient();
    
      console.log(`Deleting ${instanceName} from ${zone}...`);
    
      const [response] = await instancesClient.delete({
        project: projectId,
        zone,
        instance: instanceName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.ZoneOperationsClient();
    
      // Wait for the delete operation to complete.
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Instance deleted.');
    }
    
    deleteInstance();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\DeleteInstanceRequest;
    
    /**
     * Delete an instance.
     *
     * @param string $projectId Your Google Cloud project ID.
     * @param string $zone Zone where the instance you want to delete is (like "us-central1-a").
     * @param string $instanceName Unique name for the Compute instance to delete.
     *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function delete_instance(
        string $projectId,
        string $zone,
        string $instanceName
    ) {
        // Delete the Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new DeleteInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->delete($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Deleted instance %s' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Failed to delete instance: %s' . PHP_EOL, $error?->getMessage());
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    
    def delete_instance(project_id: str, zone: str, machine_name: str) -> None:
        """
        Send an instance deletion request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            machine_name: name of the machine you want to delete.
        """
        instance_client = compute_v1.InstancesClient()
    
        print(f"Deleting {machine_name} from {zone}...")
        operation = instance_client.delete(
            project=project_id, zone=zone, instance=machine_name
        )
        wait_for_extended_operation(operation, "instance deletion")
        print(f"Instance {machine_name} deleted.")
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    # Sends an instance deletion request to the Compute Engine API and waits for it to complete.
    #
    # @param [String] project project ID or project number of the Cloud project you want to use.
    # @param [String] zone name of the zone you want to use. For example: "us-west3-b"
    # @param [String] instance_name name of the instance you want to delete.
    def delete_instance project:, zone:, instance_name:
      # Initialize client that will be used to send requests. This client only needs to be created
      # once, and can be reused for multiple requests.
      client = ::Google::Cloud::Compute::V1::Instances::Rest::Client.new
    
      puts "Deleting #{instance_name} from #{zone}..."
      begin
        # Make the request to delete a VM instance.
        operation = client.delete project: project, zone: zone, instance: instance_name
        # Wait for the delete operation to complete.
        operation = wait_until_done operation: operation
    
        compute_operation = operation.operation
        if operation.error?
          warn "Error during deletion:", compute_operation.error.errors.map { |e| "#{e.code}: #{e.message}" }
        else
          warn "Warning during deletion:", compute_operation.warnings unless compute_operation.warnings.empty?
          puts "Instance #{instance_name} deleted."
        end
      rescue ::Google::Cloud::Error => e
        warn "Exception during deletion:", e
      end
    end

### Rust
    
    
    use google_cloud_compute_v1::client::Instances;
    use google_cloud_lro::Poller;
    
    pub async fn sample(client: &Instances, project_id: &str, name: &str) -> anyhow::Result<()> {
        const ZONE: &str = "us-central1-a";
    
        let operation = client
            .delete()
            .set_project(project_id)
            .set_zone(ZONE)
            .set_instance(name)
            .poller()
            .until_done()
            .await?
            .to_result()?;
        println!("Instance successfully deleted: {operation:?}");
    
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
