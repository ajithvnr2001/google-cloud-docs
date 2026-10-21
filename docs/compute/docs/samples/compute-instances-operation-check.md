---
url: https://docs.cloud.google.com/compute/docs/samples/compute-instances-operation-check/
title: Check operation status \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:14:08.897875+00:00
---

# Check operation status  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/samples/compute-instances-operation-check/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Samples ](https://docs.cloud.google.com/compute/docs/samples)



#  Check operation status Stay organized with collections  Save and categorize content based on your preferences. 

Request to wait until an operation completes and get the operation status before continuing code execution.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating API requests and handling responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses)
  * [Using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
    using System.Threading.Tasks;
    
    public class CreateInstanceAsyncSample
    {
        public async Task CreateInstanceAsync(
            // TODO(developer): Set your own default values for these parameters or pass different values when calling this method.
            string projectId = "your-project-id",
            string zone = "us-central1-a",
            string machineName = "test-machine",
            string machineType = "n1-standard-1",
            string diskImage = "projects/debian-cloud/global/images/family/debian-12",
            long diskSizeGb = 10,
            string networkName = "default")
        {
            [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instance.html) instance = new [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Instance.html)
            {
                Name = machineName,
                // See https://cloud.google.com/compute/docs/machine-types for more information on machine types.
                MachineType = $"zones/{zone}/machineTypes/{machineType}",
                // Instance creation requires at least one persistent disk.
                Disks =
                {
                    new [AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDisk.html)
                    {
                        AutoDelete = true,
                        Boot = true,
                        Type = [ComputeEnumConstants](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.html).[AttachedDisk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.html).[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.Type.html).[Persistent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants.AttachedDisk.Type.html#Google_Cloud_Compute_V1_ComputeEnumConstants_AttachedDisk_Type_Persistent),
                        InitializeParams = new [AttachedDiskInitializeParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AttachedDiskInitializeParams.html) 
                        {
                            // See https://cloud.google.com/compute/docs/images for more information on available images.
                            SourceImage = diskImage,
                            DiskSizeGb = diskSizeGb
                        }
                    }
                },
                NetworkInterfaces = { new [NetworkInterface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkInterface.html) { Name = networkName } }
            };
    
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests.
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Insert the instance in the specified project and zone.
            var instanceCreation = await client.[InsertAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_InsertAsync_Google_Cloud_Compute_V1_InsertInstanceRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone, instance);
    
            // Wait for the operation to complete using client-side polling.
            // The server-side operation is not affected by polling,
            // and might finish successfully even if polling times out.
            await instanceCreation.PollUntilCompletedAsync();
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
    )
    
    // waitForOperation waits for an operation to be completed. Calling this function will block until the operation is finished.
    func waitForOperation(w io.Writer, projectID string, operation *compute.Operation) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// opName := "your_operation_name"
    
    	ctx := context.Background()
    
    	if err := operation.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Operation finished\n")
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html);
    import java.io.IOException;
    
    public class WaitForOperation {
    
      public static void main(String[] args) throws IOException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        // operation: Specify the operation to wait.
        String project = "your-project-id";
        [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).newBuilder().build();
    
        waitForOperation(project, operation);
      }
    
      // Waits for the specified operation to complete.
      public static void waitForOperation(String project, [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation)
          throws IOException {
        try ([ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html) zoneOperationsClient = [ZoneOperationsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ZoneOperationsClient.html).create()) {
    
          // Check if the operation hasn't been completed already.
          if (operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() != [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).DONE) {
            String zone = operation.[getZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getZone__)();
            zone = zone.substring(zone.lastIndexOf("/") + 1);
    
            // Wait for the operation to complete.
            [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = zoneOperationsClient.wait(project, zone, operation.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getName__)());
    
            // Check if the operation has errors.
            if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
              System.out.println("Error in executing the operation ! ! " + response.[getError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getError__)());
              return;
            }
            System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
            return;
          }
          System.out.println("Operation Status: " + operation.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
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
    // const operationString = 'YOUR_OPERATION_STRING'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Parse stringified operation to the object instance.
    let operation = JSON.parse(operationString);
    
    async function waitForOperation() {
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      while (operation.status !== 'DONE') {
        [operation] = await operationsClient.wait({
          operation: operation.name,
          project: projectId,
          zone: operation.zone.split('/').pop(),
        });
      }
    
      console.log('Operation finished.');
    }
    
    waitForOperation();

### PHP

Before trying this sample, follow the PHP setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine PHP API reference documentation](https://docs.cloud.google.com/php/docs/reference/cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Wait for the operation to complete.
    $operation->pollUntilComplete();
    if ($operation->operationSucceeded()) {
        printf('Created instance %s' . PHP_EOL, $instanceName);
    } else {
        $error = $operation->getError();
        printf('Instance creation failed: %s' . PHP_EOL, $error?->getMessage());
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google.cloud import [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)
    
    
    def wait_for_operation(
        operation: [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Operation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Operation.html), project_id: str
    ) -> compute_v1.Operation:
        """
        This method waits for an operation to be completed. Calling this function
        will block until the operation is finished.
    
        Args:
            operation: The Operation object representing the operation you want to
                wait on.
            project_id: project ID or project number of the Cloud project you want to use.
    
        Returns:
            Finished Operation object.
        """
        kwargs = {"project": project_id, "operation": operation.name}
        if operation.zone:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[ZoneOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.zone_operations.ZoneOperationsClient.html)()
            # Operation.zone is a full URL address of a zone, so we need to extract just the name
            kwargs["zone"] = operation.zone.rsplit("/", maxsplit=1)[1]
        elif operation.region:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[RegionOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.region_operations.RegionOperationsClient.html)()
            # Operation.region is a full URL address of a region, so we need to extract just the name
            kwargs["region"] = operation.region.rsplit("/", maxsplit=1)[1]
        else:
            client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[GlobalOperationsClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_operations.GlobalOperationsClient.html)()
    
        while True:
            result = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.global_operations.GlobalOperationsClient.html#google_cloud_compute_v1_services_global_operations_GlobalOperationsClient_get)(**kwargs)
    
            if result.status == [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Operation](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Operation.html).Status.DONE:
                print("Operation finished.")
                if result.error:
                    print(f"Error during operation: {result.error}")
                return result
    
            print("Waiting for operation to complete...")
            time.sleep(2)
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/compute/v1"
    
    require "time"
    
    # Waits for an operation to be completed. Calling this method
    # will block until the operation is finished or timed out.
    #
    # @param [::Gapic::GenericLRO::Operation] operation The operation to wait for.
    # @param [Numeric] timeout seconds until timeout (default is 3 minutes)
    # @return [::Gapic::GenericLRO::Operation] Finished Operation object.
    def wait_until_done operation:, timeout: 3 * 60
      retry_policy = ::Gapic::Operation::RetryPolicy.new initial_delay: 0.2, multiplier: 2, max_delay: 1, timeout: timeout
      operation.wait_until_done! retry_policy: retry_policy
    end

### Rust
    
    
    use google_cloud_compute_v1::client::{Instances, ZoneOperations};
    use google_cloud_compute_v1::model::{
        AttachedDisk, AttachedDiskInitializeParams, Instance, NetworkInterface,
    };
    use google_cloud_compute_v1::model::{Operation, operation::Status};
    
    pub async fn sample(client: &Instances, project_id: &str, name: &str) -> anyhow::Result<()> {
        const ZONE: &str = "us-central1-a";
        let operations_client = ZoneOperations::builder().build().await?;
    
        // Start an operation, in this example we use a VM creation.
        let mut op = start_instance_insert(client, project_id, ZONE, name).await?;
    
        // Manually wait for the operation.
        let operation = loop {
            if op.status.as_ref().is_some_and(|s| s == &Status::Done) {
                break op;
            }
            let Some(name) = op.name.clone() else {
                return Err(anyhow::Error::msg(format!(
                    "the operation name should be set, operation={op:?}"
                )));
            };
            println!("polling operation {op:?}");
            op = operations_client
                .wait()
                .set_project(project_id)
                .set_zone(ZONE)
                .set_operation(name)
                .send()
                .await?;
        };
    
        println!("Instance creation finished: {operation:?}");
        // Check if there was an error.
        if let Err(error) = operation.to_result() {
            println!("Instance creation failed: {error:?}");
            return Err(anyhow::Error::msg(format!(
                "instance creation failed with: {error:?}"
            )));
        }
    
        Ok(())
    }
    
    async fn start_instance_insert(
        client: &Instances,
        project_id: &str,
        zone: &str,
        name: &str,
    ) -> anyhow::Result<Operation> {
        let instance = Instance::new()
            .set_machine_type(format!("zones/{zone}/machineTypes/f1-micro"))
            .set_name(name)
            .set_description("A test VM created by the Rust client library.")
            .set_labels([("source", "compute_instances_create")])
            .set_disks([AttachedDisk::new()
                .set_initialize_params(
                    AttachedDiskInitializeParams::new()
                        .set_source_image("projects/cos-cloud/global/images/family/cos-stable"),
                )
                .set_boot(true)
                .set_auto_delete(true)])
            .set_network_interfaces([NetworkInterface::new().set_network("global/networks/default")]);
    
        // Start the operation without waiting for it to complete. This will require
        // manually waiting for the operation. In most cases we recommend you use
        // `.poller().until_done()` instead of `.send()`:
        let op = client
            .insert()
            .set_project(project_id)
            .set_zone(zone)
            .set_body(instance)
            .send()
            .await?;
        Ok(op)
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=computeengine). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
