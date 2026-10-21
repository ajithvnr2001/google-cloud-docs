---
url: https://docs.cloud.google.com/compute/docs/instances/deleting-instance/
title: Delete a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:54:04.089090+00:00
---

# Delete a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/deleting-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Delete a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to delete a Compute Engine instance. To learn more about the lifecycle of an instance, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

If you no longer need an instance, then delete it to stop incurring charges for the instance and its attached resources.

**Caution:** If you delete an instance in a managed instance group (MIG) that uses autoscaler, then the MIG may automatically create a new instance to replace the deleted instance. To prevent this, [resize the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size) or [reconfigure its autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler).

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

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

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

### PHP

To use the PHP samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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

### Ruby

To use the Ruby samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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

To get the permissions that you need to delete a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to delete a compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete a compute instance:

  * `compute.instances.delete` on the instance
  * To force the deletion of an attached disk: `compute.disks.delete` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Billing implications

After you delete a compute instance, you stop incurring charges for the instance and its attached resources, except in the following cases:

  * If you delete an instance that is hosted on a [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes), then you still incur charges for the sole-tenant node.

  * If you delete an instance that is using a [reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview), then you continue to pay for the reserved resources until one of the following occurs:

    * Compute Engine automatically deletes the reservation at your chosen date and time.

    * You delete the reservation.

    * You reduce the number of reserved instances in the reservation.

  * If you have a [committed use discount](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts), then you continue to pay for the committed resources, regardless if you use them or not.

  * If you preserve any resources attached to the instance, such as disks, then you continue to pay for those resources until you delete them.




For more information, see [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).

### Preserve attached resources

In some cases, before you delete a compute instance, you might want to preserve one of its attached resources. You can preserve attached resources by doing the following:

  * To preserve a GPU attached to an N1 virtual machine (VM) instance, [remove the GPU from the VM](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus#remove-gpu).

  * To preserve an attached disk, do one of the following:

    * To preserve a boot disk, [detach the boot disk from the instance](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk).

    * To preserve a boot or non-boot disk, set the [auto-delete setting of the disk to `false`](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete).

  * To preserve the data of a Local SSD disk, copy the data of the disk to a persistent [storage option](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_backup).

  * To reuse the static external IP address of an instance, [unassign the IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#unassign_ip).




## Delete instances

When you delete a compute instance, Compute Engine [stops the instance](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance) before deleting it.

If you delete one or more instances simultaneously, then you must decide what happens to the attached disks:

  * Delete instances and all attached resources

This option deletes the instances and deletes, or forces the deletion of, boot, non-boot, or all attached disks.

  * Delete instances and preserve disks

This option deletes the instances but preserves boot, non-boot, or all attached disks for later use.




### Delete instances and all attached resources

Depending on what you want to do when deleting a compute instance, use the following options:

  * If you [configured an attached disk to be preserved](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete) upon instance deletion, then you can override this setting and force its deletion using the Google Cloud CLI.

**Caution:** Forcefully deleting a disk that is attached to an instance also deletes all its instant snapshots. You can't recover these snapshots. To retain the data in an instant snapshot, [create a standard snapshot from it](https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot) before deleting the instance.
  * If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in the instance, then you can delete the instance without gracefully shutting it down or end an ongoing graceful shutdown using the Google Cloud console, gcloud CLI, or REST API.

  * To delete multiple instances simultaneously, use the Google Cloud console or, for instances located in the same zone, the gcloud CLI.




To delete one or more instances and all attached resources, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instances that you want to delete.

  3. Click delete **Delete**.

  4. In the dialog, do the following:

     1. Optional: To delete the instances without gracefully shut them down, or end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Delete**.




###  gcloud 

To delete one or more instances in the same zone, use the [`gcloud compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete):
    
    
    gcloud compute instances delete INSTANCE_NAMES \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of instance names separated by spaces—for example, `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the instances are located.




Optionally, you can do one or both of the following:

  * To force the deletion of the disks attached to one or more instances, include the `--delete-disks` flag:
        
        gcloud compute instances delete INSTANCE_NAMES \
            **--delete-disks= DELETE_DISK_TYPE** \
            --zone=ZONE
        

Replace `DELETE_DISK_TYPE` with one of the following values:

    * To delete attached boot and non-boot persistent storage: `all`

    * To delete only attached boot persistent storage: `boot`

    * To delete only non-boot persistent storage: `data`

  * If you've enabled graceful shutdown in one or more instances, then you can delete the instances without gracefully shutting them down, or manually end an ongoing graceful shutdown. To do so, use the [`gcloud beta compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/delete) with the `--no-graceful-shutdown` flag:

**Preview — The`--no-graceful-shutdown` flag **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        gcloud beta compute instances delete INSTANCE_NAMES \
            **--no-graceful-shutdown** \
            --zone=ZONE
        




###  C# 
    
    
    using [Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.html);
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
            [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html) client = await [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html).[CreateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_CreateAsync_System_Threading_CancellationToken_)();
    
            // Make the request to delete a VM instance.
            var instanceDeletion = await client.[DeleteAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient.html#Google_Cloud_Compute_V1_InstancesClient_DeleteAsync_Google_Cloud_Compute_V1_DeleteInstanceRequest_Google_Api_Gax_Grpc_CallSettings_)(projectId, zone, machineName);
    
            // Wait for the operation to complete using client-side polling.
            await instanceDeletion.PollUntilCompletedAsync();
        }
    }
    

###  Go 
    
    
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
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
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
    

###  Java 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
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
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          System.out.printf("Deleting instance: %s ", instanceName);
    
          // Describe which instance is to be deleted.
          [DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html) deleteInstanceRequest = [DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName).build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.deleteAsync(
              deleteInstanceRequest);
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Instance deletion failed ! ! " + response);
            return;
          }
          System.out.println("Operation Status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Delete the instance specified by `instanceName` if it's present in the given project and zone.
    async function deleteInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      console.log(`Deleting ${instanceName} from ${zone}...`);
    
      const [response] = await instancesClient.delete({
        project: projectId,
        zone,
        instance: instanceName,
      });
      let operation = response.latestResponse;
      const operationsClient = new compute.[ZoneOperationsClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
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

###  PHP 
    
    
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
    
    
    def delete_instance(project_id: str, zone: str, machine_name: str) -> None:
        """
        Send an instance deletion request to the Compute Engine API and wait for it to complete.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone you want to use. For example: “us-west3-b”
            machine_name: name of the machine you want to delete.
        """
        instance_client = comp[compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest)t[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)    print(f"Deleting {machine_name} from {zone}...")
        operation = instinstance_client.[delete](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_delete)      project=project_id, zone=zone, instance=machine_name
        )
        wait_for_extended_operation(operation, "instance deletion")
        print(f"Instance {machine_name} deleted.")
    
    

###  Ruby 
    
    
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

###  REST 

To delete an instance, make a `DELETE` request to the [`instances delete` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the instance is located.

  * `ZONE`: the zone of the instance.

  * `INSTANCE_NAME`: the instance name.




Optionally, if you've enabled graceful shutdown in the instance, you can delete the instances without gracefully shutting it down, or manually end an ongoing graceful shutdown. To do so, make a `DELETE` request to the [beta `instances.delete` method](https://docs.cloud.google.com/compute/docs/reference/beta/instances/delete). In the request URL, include the `noGracefulShutdown` query parameter set to `true`:

**Preview — The`noGracefulShutdown` query parameter **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
    DELETE https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME**?noGracefulShutdown=true**
    

### Delete instances and preserve disks

By default, deleting a compute instance deletes the instance and its attached resources. However, when you delete an instance using the gcloud CLI, you can specify to preserve the attached disks, regardless of their [auto-delete settings](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete).

To delete one or more instances in the same zone while preserving their attached disks, use the [`gcloud compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) with the `--keep-disks` flag:
    
    
    gcloud compute instances delete INSTANCE_NAMES \
        --keep-disks=KEEP_DISK_TYPE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of instance names separated by spaces—for example, `instance-01 instance-02 instance-03`.

  * `KEEP_DISK_TYPE`: specify one of the following values:

    * To preserve attached boot and non-boot persistent storage: `all`

    * To preserve only attached boot persistent storage: `boot`

    * To preserve only attached non-boot persistent storage: `data`

  * `ZONE`: the zone where the instances are located.




Optionally, if you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in one or more instances, you can delete the instances without gracefully shutting them down, or manually end an ongoing graceful shutdown. To do so, use the [`gcloud beta compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/delete) with the `--no-graceful-shutdown` flag:

**Preview — The `--no-graceful-shutdown` flag**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
    
    
    gcloud beta compute instances delete VM_NAMES \
        --keep-disks=KEEP_DISK_TYPE \
        **--no-graceful-shutdown** \
        --zone=ZONE
    

## What's next

  * [Pricing for stopping an instance](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#pricing-stop-instance)

  * [Limit the runtime of a VM](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
