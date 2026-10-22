---
url: https://docs.cloud.google.com/compute/docs/instances/stop-start-instance/
title: Stop or restart a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:30.494086+00:00
---

# Stop or restart a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/stop-start-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Stop or restart a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to manually stop or restart a Compute Engine instance. Alternatively, to automate when a compute instance stops or restarts, see the following:

  * [Schedule a compute instance to start and stop](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop)

  * [Limit the runtime of a compute instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)




It's possible to manually stop a compute instance. After a stop operation completes and the state of the compute instance transitions to `TERMINATED`, you can either restart the compute instance to resume your workload, or permanently delete the compute instance if you no longer need it. Manually stopping a compute instance is useful when you want to do the following:

  * **Save costs while keeping your configurations** : you no longer want to run workloads on the compute instance. However, you want to retain the compute instance and its attached disks, configuration settings, IP addresses, MAC addresses, and metadata. If you also need to retain in-memory data and application state, then [suspend the compute instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance) instead.

  * **Update properties** : you want to modify one or more properties that require you to stop and restart the compute instance before the changes can take effect—for example, you want to change machine type or detach a disk. For more information, see [Properties that you can update](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#updatable-properties).


**Caution:** After a stop operation completes, you continue to incur charges for any disks, disk snapshots, or external IP addresses that remain attached to a compute instance. To avoid unexpected costs, detach and delete any resources that you no longer need. For instructions, see how to [detach disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk), [manage disk snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots), or [manage external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).

## Limitations

When you stop a compute instance, the following limitations apply:

  * You can only stop or restart a compute instance if the [state of the compute instance allows it](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

  * You can only restart a compute instance if there are sufficient resources in the zone where the compute instance exists.

  * You can't restart TPU compute instances. After you stop TPU compute instances, you can only delete them.




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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to stop or restart a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to stop or restart a compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to stop or restart a compute instance:

  * To stop a compute instance: `compute.instances.stop` on the compute instance 
  * To stop a compute instance from the guest OS: `compute.instances.setMetadata` on the compute instance if it uses [instance-level public SSH keys](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#add_ssh_keys_to_instance_metadata). 
  * To restart a compute instance: `compute.instances.start` on the compute instance 
  * To restart a compute instance that uses encryption keys: `compute.instances.startWithEncryptionKey` on the compute instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Stop a compute instance

To stop your compute instance, use one of the following methods. The best approach for your use case depends on whether you have Local SSD disks attached to your compute instance and how you want to handle any [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript):

  * **Stop a compute instance from Google Cloud**. You can stop one or more compute instances simultaneously from Google Cloud. If the compute instances have Local SSD disks attached, then you can choose whether to discard or preserve ([Preview](https://cloud.google.com/products/#product-launch-stages)) Local SSD data. Any shutdown scripts in the compute instance must finish running before the compute instance stops. For instructions, see one of the following:

    * Stop a compute instance with no Local SSD disks

    * Stop a compute instance with Local SSD disks

  * **Stop a compute instance from the guest OS**. This approach ensures your shutdown scripts finish running before the compute instance stops. If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview), then you can skip or end the graceful shutdown. However, stopping a compute instance from the guest OS discards data on any attached Local SSD disks unless you first back the data up to durable storage. For instructions, see Stop a compute instance from the guest OS.




### Stop a compute instance with no Local SSD disks

To stop a compute instance that doesn't have Local SSD disks attached, review the following options:

  * If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in the compute instance, then you can save costs by skipping or ending an ongoing graceful shutdown. To do so, use the Google Cloud console, gcloud CLI, or REST API.

  * To stop multiple compute instances simultaneously, use the Google Cloud console or, for compute instances that exist in the same zone, the gcloud CLI.




To stop one or more compute instances, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the running compute instances to stop.

  3. Click stop **Stop**. If there is no **Stop** option, then click **More actions** , and then select **Stop**.

  4. In the dialog that appears, do the following:

     1. Optional: To stop the compute instances without gracefully shutting them down, or to end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Stop**.




###  gcloud 

To stop one or more compute instances that exist in the same zone, use the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
    
    
    gcloud compute instances stop INSTANCE_NAMES \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of names of compute instances that you want to stop, separated by spaces. For example, specify `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the compute instances exist.




If you want to skip or end an ongoing graceful shutdown, then use the same command with the `--no-graceful-shutdown` flag:
    
    
    gcloud compute instances stop INSTANCE_NAMES \
        **--no-graceful-shutdown** \
        --zone=ZONE
    

###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // stopInstance stops a started Google Compute Engine instance
    func stopInstance(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.StopInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	op, err := instancesClient.Stop(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to stop instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance stopped\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class StopInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        /* project: project ID or project number of the Cloud project your instance belongs to.
           zone: name of the zone your instance belongs to.
           instanceName: name of the instance your want to stop.
         */
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
    
        stopInstance(project, zone, instanceName);
      }
    
      // Stops a started Google Compute Engine instance.
      public static void stopInstance(String project, String zone, String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
           once, and can be reused for multiple requests. After completing all of your requests, call
           the `instancesClient.close()` method on the client to safely
           clean up any remaining background resources. */
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest.html) stopInstanceRequest = [StopInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StopInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName)
              .build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.[stopAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_stopAsync_com_google_cloud_compute_v1_StopInstanceRequest_)(
              stopInstanceRequest);
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() == [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).DONE) {
            System.out.println("Instance stopped successfully ! ");
          }
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function stopInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.stop({
        project: projectId,
        zone,
        instance: instanceName,
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
    
      console.log('Instance stopped.');
    }
    
    stopInstance();

###  PHP 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\StopInstanceRequest;
    
    /**
     * Stops a running Google Compute Engine instance.
     *
     * @param string $projectId Project ID or project number of the Cloud project your instance belongs to.
     * @param string $zone Name of the zone your instance belongs to.
     * @param string $instanceName Name of the instance you want to stop.
      *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function stop_instance(
        string $projectId,
        string $zone,
        string $instanceName
    ) {
        // Stop the Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new StopInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->stop($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Instance %s stopped successfully' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Failed to stop instance: %s' . PHP_EOL, $error?->getMessage());
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
    
    
    def stop_instance(project_id: str, zone: str, instance_name: str) -> None:
        """
        Stops a running Google Compute Engine instance.
        Args:
            project_id: project ID or project number of the Cloud project your instance belongs to.
            zone: name of the zone your instance belongs to.
            instance_name: name of the instance your want to stop.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        operation = instance_client.[stop](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_stop)(
            project=project_id, zone=zone, instance=instance_name
        )
        wait_for_extended_operation(operation, "instance stopping")
    
    

###  REST 

To stop a compute instance, make a `POST` request to the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/stop):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/stop
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `PROJECT_ID`: the ID of the project where the compute instance exists.

  * `ZONE`: the zone where the compute instance exists.




If you want to skip or end an ongoing graceful shutdown, then include the `noGracefulShutdown=true` query parameter in the request URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop**?noGracefulShutdown=true**
    

### Stop a compute instance with Local SSD disks

The best method to stop a compute instance that has Local SSD disks attached depends on your use case. Use one of the following options: 

  * If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in a compute instance, then you can save costs by skipping or ending an ongoing graceful shutdown. To do so, use the Google Cloud console, gcloud CLI, or REST API.

  * To preserve Local SSD data (excluding for [machine types that use Titanium SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types)), use the gcloud CLI or REST API. 

**Caution:** If you opt to preserve Local SSD data, then Compute Engine stores Local SSD data on durable storage while the compute instance is stopped. Before you stop your compute instance, verify that you have enough disk quota to store Local SSD data.
  * To stop multiple compute instances simultaneously, use the Google Cloud console or, for compute instances that exist in the same zone, the gcloud CLI.




To stop one or more compute instances that have Local SSD disks attached, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the running compute instances to stop.

  3. Click stop **Stop**. If there is no **Stop** option, click **More actions** , and then select **Stop**.

  4. In the dialog that appears, do the following:

     1. Optional: To stop the compute instances without gracefully shut them down, or end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Stop**.




###  gcloud 

When you stop one or more compute instances in the same zone that have Local SSD disks attached, specify whether to discard or preserve Local SSD data as follows:

  * To discard Local SSD data, use the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) with the `--discard-local-ssd=true` flag:
        
        gcloud compute instances stop INSTANCE_NAMES \
            --discard-local-ssd=true \
            --zone=ZONE
        

  * To preserve Local SSD data, use the [`gcloud beta compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/stop) with the `--discard-local-ssd=false` flag:

**Preview — The`--discard-local-ssd=false` flag **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        gcloud beta compute instances stop INSTANCE_NAMES \
            --discard-local-ssd=false \
            --zone=ZONE
        




Replace the following:

  * `INSTANCE_NAMES`: a list of names of compute instances that you want to stop, separated by spaces. For example, specify `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the compute instances exist.




If you want to skip or end an ongoing graceful shutdown, then include the `--no-graceful-shutdown` flag in the command:
    
    
    gcloud compute instances stop INSTANCE_NAMES \
        --discard-local-ssd=DISCARD_LOCAL_SSD \
        **--no-graceful-shutdown** \
        --zone=ZONE
    

Replace `DISCARD_LOCAL_SSD` with `true` to discard the data in the Local SSD disks, or `false` to preserve the data. If you specify `false`, then you must use the [`gcloud beta compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/stop).

###  REST 

When you stop one or more compute instances in the same zone that have Local SSD disks attached, specify whether to discard or preserve Local SSD data as follows:

  * To discard Local SSD data, make a `POST` request to the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop). In the request URL, include the `discardLocalSsd` query parameter set to `true`:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/stop?discardLocalSsd=true
        

  * To preserve Local SSD data, make a `POST` request to the [`beta.instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/stop). In the request URL, include the `discardLocalSsd` query parameter set to `false`:

**Preview — The`discardLocalSsd=false` query parameter **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/stop?discardLocalSsd=false
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the compute instance exists.

  * `ZONE`: the zone where the compute instance exists.

  * `INSTANCE_NAME`: the name of the compute instance.




If you want to skip or end an ongoing graceful shutdown, then include the `noGracefulShutdown=true` query parameter in the request URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop?discardLocalSsd=DISCARD_LOCAL_SSD&**noGracefulShutdown=true**
    

Replace `DISCARD_LOCAL_SSD` with `true` to discard the data in the Local SSD disks, or `false` to preserve the data. If you specify `false`, then you must make a `POST` request to the [`beta.instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/stop).

### Stop a compute instance from the guest OS

If a compute instance has Local SSD disks attached, then shutting down the guest OS automatically discards the Local SSD data. To preserve this data, manually copy the data to a persistent storage option before you stop the compute instance.

To stop a compute instance from the guest OS, select one of the following options:

###  Linux 

  1. If you haven't already, then [connect to the compute instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

  2. To stop the compute instance from within its guest OS, select one of the following methods:

     * To cleanly shut down the guest OS only after all shutdown scripts have finished running, run the following command:
           
           sudo shutdown -h now
           

     * To force a shutdown of the guest OS, run the following command:
           
           sudo poweroff
           




###  Windows 

  1. If you haven't already, then connect to the compute instance using one of the following methods:

     * [PowerShell](https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell)

     * [Remote Desktop Protocol (RDP)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)

     * [Secure Shell (SSH)](https://docs.cloud.google.com/compute/docs/connect/windows-ssh)

     * [Special Administration Console (SAC)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac)

  2. To stop the compute instance from within its guest OS, select one of the following methods:

     * To cleanly shut down the guest OS only after all shutdown scripts have finished running, run the following command:
           
           shutdown /s
           

     * To force a shutdown of the guest OS, run the following command:
           
           shutdown /f
           




## Restart a compute instance

You can restart a compute instance that has been fully stopped, which is when the compute instance state is `TERMINATED`. If you opted to preserve Local SSD data when you stopped your compute instance, then you might need to remount the Local SSD disks after you restart the compute instance. For more information, see [Format and mounting a Local SSD device](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#formatandmount).

To restart a compute instance, use one of the following methods. The best method for your use case depends on whether the compute instance has disks that were encrypted with [customer-supplied encryption keys (CSEK)](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption):

  * Restart a compute instance that doesn't have CSEK-encrypted disks

  * Restart a compute instance with CSEK-encrypted disks




### Restart a compute instance that doesn't have CSEK-encrypted disks

To restart multiple compute instances simultaneously across different zones, use the Google Cloud console. For compute instances that exist in the same zone, you can use the gcloud CLI. Otherwise, for other restart scenarios, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the compute instances that you want to restart.

  3. Click play_arrow **Start / Resume**.




###  gcloud 

To restart one or more compute instances that exist in the same zone, use the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
    
    
    gcloud compute instances start INSTANCE_NAMES \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of names of compute instances that you want to restart, separated by spaces. For example, specify `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the compute instances exist.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // startInstance starts a stopped Google Compute Engine instance (with unencrypted disks).
    func startInstance(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.StartInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	op, err := instancesClient.Start(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to start instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance started\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class StartInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        /* project: project ID or project number of the Cloud project your instance belongs to.
           zone: name of the zone your instance belongs to.
           instanceName: name of the instance your want to start. */
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
    
        startInstance(project, zone, instanceName);
      }
    
      // Starts a stopped Google Compute Engine instance (with unencrypted disks).
      public static void startInstance(String project, String zone, String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        /* Initialize client that will be used to send requests. This client only needs to be created
           once, and can be reused for multiple requests. After completing all of your requests, call
           the `instancesClient.close()` method on the client to safely
           clean up any remaining background resources. */
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          // Create the request.
          [StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest.html) startInstanceRequest = [StartInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.StartInstanceRequest.html).newBuilder()
              .setProject(project)
              .setZone(zone)
              .setInstance(instanceName)
              .build();
    
          OperationFuture<Operation, Operation> operation = instancesClient.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_startAsync_com_google_cloud_compute_v1_StartInstanceRequest_)(
              startInstanceRequest);
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = operation.get(3, TimeUnit.MINUTES);
    
          if (response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)() == [Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).DONE) {
            System.out.println("Instance started successfully ! ");
          }
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b'
    // const instanceName = 'YOUR_INSTANCE_NAME'
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    async function startInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.start({
        project: projectId,
        zone,
        instance: instanceName,
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
    
      console.log('Instance started.');
    }
    
    startInstance();

###  PHP 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\StartInstanceRequest;
    
    /**
     * Starts a stopped Google Compute Engine instance (with unencrypted disks).
     *
     * @param string $projectId Project ID or project number of the Cloud project your instance belongs to.
     * @param string $zone Name of the zone your instance belongs to.
     * @param string $instanceName Name of the instance you want to stop.
      *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function start_instance(
        string $projectId,
        string $zone,
        string $instanceName
    ) {
        // Start the Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new StartInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->start($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Instance %s started successfully' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Failed to start instance: %s' . PHP_EOL, $error?->getMessage());
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
    
    
    def start_instance(project_id: str, zone: str, instance_name: str) -> None:
        """
        Starts a stopped Google Compute Engine instance (with unencrypted disks).
        Args:
            project_id: project ID or project number of the Cloud project your instance belongs to.
            zone: name of the zone your instance belongs to.
            instance_name: name of the instance your want to start.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        operation = instance_client.[start](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_start)(
            project=project_id, zone=zone, instance=instance_name
        )
    
        wait_for_extended_operation(operation, "instance start")
    
    

###  REST 

To restart a compute instance, make a `POST` request to the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/start):
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/start
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `PROJECT_ID`: the ID of the project where the compute instance exists.

  * `ZONE`: the zone where the compute instance exists.




### Restart a compute instance with CSEK-encrypted disks

When you restart a stopped compute instance that has attached disks that were encrypted by using [customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption), you must supply the encryption key information.

To restart multiple compute instances simultaneously across different zones, use the Google Cloud console. For compute instances that exist in the same zone, you can use the gcloud CLI. Otherwise, for other restart scenarios, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the compute instances that you want to restart.

  3. Click play_arrow **Start / Resume**.

  4. In the dialog that appears, do the following:

     1. Specify encryption keys for each of the encrypted disks that are attached to the compute instances.

     2. Click **Start**.




###  gcloud 

To restart one or more compute instances that use encrypted disks that exist in the same zone, use the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start) with the `--csek-key-file` flag. If you're using an RSA-wrapped key, then use the [`gcloud beta compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/start) with the `--csek-key-file` flag instead:
    
    
    gcloud compute instances start INSTANCE_NAMES \
        --csek-key-file=ENCRYPTION_KEY_FILE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of names of compute instances that you want to restart, separated by spaces. For example, specify `instance-01 instance-02 instance-03`.

  * `ENCRYPTION_KEY_FILE`: the relative path to the JSON file that contains the customer-supplied encryption key. You can only restart multiple compute instances simultaneously if the compute instances use the same customer-supplied encryption key. The format of the file is described in [Key file format](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#key_file_format).

  * `ZONE`: the zone where the compute instances exist.




###  Go 
    
    
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
    

###  Java 
    
    
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

###  Node.js 
    
    
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

###  PHP 
    
    
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
    
    

###  REST 

To restart a compute instance that uses encrypted disks, make a `POST` request to the [`instances.startWithEncryptionKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/startWithEncryptionKey):
    
    
    POST  https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/startWithEncryptionKey
    
    {
      "disks": [
        {
          "source": "DISK_URL",
          "diskEncryptionKey": {
            "ENCRYPTION_TYPE": "ENCRYPTION_KEY"
          }
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the compute instance exists.

  * `ZONE`: the zone where the compute instance exists.

  * `INSTANCE_NAME`: the name of the compute instance.

  * `DISK_URL`: the [resource URL](https://docs.cloud.google.com/apis/design/resource_names#resource_name_vs_url) corresponding to the full resource name of the attached disk that is encrypted with a customer-supplied encryption key.

  * `ENCRYPTION_TYPE`: the type of disk encryption that you're using, which can be one of the following: `rawKey`, `kmsKeyName`, or `rsaEncryptedKey`. If you use the `rsaEncryptedKey` type, then make a `POST` request to the [`beta.instances.startWithEncryptionKey` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/startWithEncryptionKey).

  * `ENCRYPTION_KEY`: the encryption key used to encrypt the persistent disks attached to the compute instance. `rawKey` or `rsaEncryptedKey` keys must be [base64-encoded](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#required_key_format). Additionally, to prepare a `rsaEncryptedKey` key, see [RSA key wrapping](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption).




## What's next

  * [Troubleshoot compute instance shutdowns and reboots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reboots)

  * [Troubleshoot compute instance by using the serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console)

  * [Edit the machine type of a compute instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance)

  * [Delete a compute instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
