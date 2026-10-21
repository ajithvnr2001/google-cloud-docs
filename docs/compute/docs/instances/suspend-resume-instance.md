---
url: https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance/
title: Suspend or resume a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:56.571796+00:00
---

# Suspend or resume a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Suspend or resume a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to suspend or resume Compute Engine instances. To learn more about suspending, stopping, or resetting instances, see [Suspend, stop, or reset Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview).

If you want to keep your Compute Engine instance around, but you don't want to incur charges for it when the instance isn't in use, then you can suspend the instance. Suspending an instance preserves the instance and migrates the contents of the instance's memory to storage. After resuming the instance, Compute Engine migrates the instance's memory from storage back to the instance, and the instance starts running again.

Suspending a Compute Engine instance is useful for the following:

  * Development and test environments that are not being fully used during off periods, such as during evenings or weekends, and that you want to maintain for costs saving or faster initialization than creating new instances.

  * Applications that require a long period of initialization after the instance has finished booting, but before the application is ready to service its first request, such as virtual developer workstations or complex Java applications.




## Limitations

When you suspend a compute instance, the following limitations apply:

  * You can only suspend an instance if the guest OS supports it. For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

  * You can only suspend an instance that uses the following OS images if you configure their OS, as described in this document:

    * Debian 8 or 9

    * Any Windows OS

  * You can suspend an instance for only up to 60 days before Compute Engine automatically transitions its state to `TERMINATED`.

  * You can suspend Spot VMs or preemptible instances—however, if Compute Engine preempts the instance before the suspend operation completes, Compute Engine ends the suspend operation and preempts the instance.

  * You can't suspend instances by using the standard processes that are built into their guest environment. Commands such as `systemctl suspend` in Ubuntu 16.04 or later aren't supported. If called, then Compute Engine ignores the in-guest signal.

  * You can't suspend the following types of instances:

    * Bare metal instances.

    * Confidential VMs.

    * Instances that have GPUs or TPUs attached.

    * Instances that have more than 208 GB of memory.

    * Instances that have CSEK-protected ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)) disks attached.




## Before you begin

  * Verify that your project has sufficient `Persistent disk standard (GB)` quota in the region where the instance is located. When you suspend an instance, Compute Engine stores the instance's memory in persistent storage, which consumes the `Persistent disk standard (GB)` quota. This requirement applies to all instances, including instances that only have Google Cloud Hyperdisk volumes attached. For more information, see [Disk quotas](https://docs.cloud.google.com/compute/resource-usage#disk_quota) and [Troubleshoot insufficient disk quota](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume#not_enough_persistent_disk_quota). 
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

To get the permissions that you need to suspend or resume a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to suspend or resume a compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to suspend or resume a compute instance:

  * To suspend an instance: `compute.instances.suspend`
  * To resume an instance: `compute.instances.resume`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable suspend operations on a guest OS

If your compute instance uses Debian 8 or 9 as its guest OS, or any Windows OS, then you must configure the OS before you can suspend and resume instances. If your instance uses a different guest OS, then skip this section.

### Enable suspend operations on Debian 8 or 9

Before you can suspend or resume compute instances that use Debian 8 or 9 as a guest OS, you must configure the guest OS by using one of the following methods:

  * Configure the ACPID

  * Install D-Bus




#### Configure the ACPID

To enable the suspend and resume operation in Debian 8 or 9, you can configure the [Advanced Configuration and Power Interface events Daemon (ACPID)](https://acpid.sourceforge.net/) to handle the sleep button event. After you enable the deep sleep button event, you can add a shell script for handling the sleep event as described in this section.

To configure the ACPID to support suspend and resume operations, do the following:

  1. If you haven't already, then [connect to your Linux instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).

  2. Create the `events` folder in the `acpi` folder:
         
         sudo mkdir -p /etc/acpi/events/
         

  3. Configure the ACPID to handle the sleep button event:
         
         cat <<EOF | sudo tee /etc/acpi/events/sleepbtn-acpi-support
         event=button[ /]sleep
         action=/etc/acpi/sleepbtn-acpi-support.sh
         EOF
         

  4. Create the sleep event handling script:
         
         cat <<EOF | sudo tee /etc/acpi/sleepbtn-acpi-support.sh
         #!/bin/sh
         echo mem > /sys/power/state
         EOF
         

  5. Set up the permissions for the script:
         
         sudo chmod 755 /etc/acpi/sleepbtn-acpi-support.sh
         

  6. To make the changes effective, restart the ACPID:
         
         sudo systemctl restart acpid.service
         




#### Install D-Bus

To enable the suspend and resume operation in Debian 8 or 9, you can install [D-Bus](https://en.wikipedia.org/wiki/D-Bus).

To install D-Bus in your compute instance's guest OS when the OS is using Debian 8 or 9, do the following:

  1. If you haven't already, then [connect to your Linux instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms).

  2. Install D-Bus:
         
         sudo apt-get install dbus
         

  3. To make the changes effective, restart `logind`:
         
         sudo systemctl restart systemd-logind.service
         




### Enable suspend operations on Windows

To suspend an instance that uses a Windows guest OS, you must disable hibernation in the OS. If you imported a Windows image, then hibernation might be enabled by default, and you must disable it to suspend the instance.

To disable hibernation in Windows, follow these steps:

  1. If you haven't already, then [connect to your Windows instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  2. Open PowerShell as an administrator.

  3. Disable hibernation:
         
         powercfg -h off
         

  4. Verify that hibernation is disabled:
         
         powercfg -a
         




## Suspend an instance

If the guest OS of your compute instance is using Debian 8 or 9, then, before suspending the instance, you must configure the guest OS to support suspend and resume operations as described in this document.

To suspend an instance, use of the following methods based on whether the instance has Local SSD disks attached:

  * If your instance doesn't have any Local SSD disks attached, then see Suspend an instance without Local SSD disks.

  * If your instance has any Local SSD disks attached, and you want to either discard or preserve ([Preview](https://cloud.google.com/products/#product-launch-stages)) the disks' Local SSD data, then see Suspend an instance with Local SSD disks.




### Suspend an instance without Local SSD disks

You can suspend multiple compute instances simultaneously or individual instances. For multiple instances, use the Google Cloud console or, for instances located in the same zone, the Google Cloud CLI. For individual instances, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select one or more instances to suspend.

  3. Click pause **Suspend** , and then click **Suspend** to confirm.




###  gcloud 

To suspend one or more instances in a single zone, use the [`gcloud compute instances suspend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/suspend):
    
    
    gcloud compute instances suspend INSTANCE_NAMES \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a whitespace-separated list of names of instances—for example, `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the instances are located.




###  Go 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	compute "cloud.google.com/go/compute/apiv1"
    	computepb "cloud.google.com/go/compute/apiv1/computepb"
    )
    
    // suspendInstance suspends a running Google Compute Engine instance.
    func suspendInstance(w io.Writer, projectID, zone, instanceName string) error {
    	// projectID := "your_project_id"
    	// zone := "europe-central2-b"
    	// instanceName := "your_instance_name"
    
    	ctx := context.Background()
    	instancesClient, err := compute.[NewInstancesRESTClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/compute/latest/apiv1.html#cloud_google_com_go_compute_apiv1_InstancesClient_NewInstancesRESTClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewInstancesRESTClient: %w", err)
    	}
    	defer instancesClient.Close()
    
    	req := &computepb.SuspendInstanceRequest{
    		Project:  projectID,
    		Zone:     zone,
    		Instance: instanceName,
    	}
    
    	op, err := instancesClient.Suspend(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to suspend instance: %w", err)
    	}
    
    	if err = op.Wait(ctx); err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Instance suspended\n")
    
    	return nil
    }
    

###  Java 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SuspendInstance {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // project: project ID or project number of the Cloud project your instance belongs to.
        // zone: name of the zone your instance belongs to.
        // instanceName: name of the instance your want to suspend.
    
        String project = "your-project-id";
        String zone = "zone-name";
        String instanceName = "instance-name";
    
        suspendInstance(project, zone, instanceName);
      }
    
      // Suspend a running Google Compute Engine instance.
      // For limitations and compatibility on which instances can be suspended,
      // see: https://cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations
      public static void suspendInstance(String project, String zone, String instanceName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Instantiates a client.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) operation = instancesClient.[suspendAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_suspendAsync_com_google_cloud_compute_v1_SuspendInstanceRequest_)(project, zone, instanceName)
              .get(300, TimeUnit.SECONDS);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)() || !instancesClient.get(project, zone, instanceName).getStatus()
              .equalsIgnoreCase([Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).SUSPENDED.toString())) {
            System.out.println("Cannot suspend instance. Try again!");
            return;
          }
    
          System.out.printf("Instance suspended successfully ! %s", instanceName);
        }
      }
    }

###  Node.js 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const zone = 'europe-central2-b';
    // const instanceName = 'YOUR_INSTANCE_NAME';
    
    const compute = require('[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)');
    
    // Suspends a running Google Compute Engine instance.
    async function suspendInstance() {
      const instancesClient = new compute.[InstancesClient](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)();
    
      const [response] = await instancesClient.suspend({
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
    
      console.log('Instance suspended.');
    }
    
    suspendInstance();

###  PHP 
    
    
    use Google\Cloud\Compute\V1\Client\InstancesClient;
    use Google\Cloud\Compute\V1\SuspendInstanceRequest;
    
    /**
     * Suspend a running Google Compute Engine instance.
     *
     * @param string $projectId Project ID or project number of the Cloud project your instance belongs to.
     * @param string $zone Name of the zone your instance belongs to.
     * @param string $instanceName Name of the instance you want to suspend.
      *
     * @throws \Google\ApiCore\ApiException if the remote call fails.
     * @throws \Google\ApiCore\ValidationException if local error occurs before remote call.
     */
    function suspend_instance(
        string $projectId,
        string $zone,
        string $instanceName
    ) {
        // Suspend the running Compute Engine instance using InstancesClient.
        $instancesClient = new InstancesClient();
        $request = (new SuspendInstanceRequest())
            ->setInstance($instanceName)
            ->setProject($projectId)
            ->setZone($zone);
        $operation = $instancesClient->suspend($request);
    
        // Wait for the operation to complete.
        $operation->pollUntilComplete();
        if ($operation->operationSucceeded()) {
            printf('Instance %s suspended successfully' . PHP_EOL, $instanceName);
        } else {
            $error = $operation->getError();
            printf('Failed to suspend instance: %s' . PHP_EOL, $error?->getMessage());
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
    
    
    def suspend_instance(project_id: str, zone: str, instance_name: str) -> None:
        """
        Suspend a running Google Compute Engine instance.
        Args:
            project_id: project ID or project number of the Cloud project your instance belongs to.
            zone: name of the zone your instance belongs to.
            instance_name: name of the instance you want to suspend.
        """
        instance_client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
    
        operation = instance_client.[suspend](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_suspend)(
            project=project_id, zone=zone, instance=instance_name
        )
    
        wait_for_extended_operation(operation, "suspend instance")
    
    

###  REST 

To suspend an instance, make a `POST` request to the [`instances.suspend` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/suspend):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/suspend
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the instance is located.

  * `ZONE`: the zone where the instance is located.

  * `INSTANCE_NAME`: the name of the instance.




### Suspend an instance with Local SSD disks

Based on how many compute instances you want to suspend simultaneously and whether you need to preserve the data of their attached Local SSD disks, do the following:

  * To preserve the data of the Local SSD disks attached to an instance (excluding instances with Titanium SSD disks), suspend the instance using the gcloud CLI or REST API. 

**Caution:** Compute Engine uses persistent storage to store your Local SSD data. Before suspending an instance, ensure that you have enough quota for the storage space used. Otherwise, suspending the instance fails. For more information, see [Stop or suspend a VM with Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance).
  * To suspend multiple instances simultaneously, use the Google Cloud console or, for instances located in the same zone, the gcloud CLI.




To suspend one or more instances that have Local SSD disks attached, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select one or more instances to suspend.

  3. Click pause **Suspend** , and then click **Suspend** to confirm.




###  gcloud 

When suspending one or more instances in a single zone that have Local SSD disks attached, specify whether to discard or preserve Local SSD data as follows:

  * To discard Local SSD data, use the [`gcloud compute instances suspend` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/suspend) with the `--discard-local-ssd=true` flag:
        
        gcloud compute instances suspend INSTANCE_NAMES \
            --discard-local-ssd=true \
            --zone=ZONE
        

  * To preserve Local SSD data, use the [`gcloud beta compute instances suspend` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/suspend) with the `--discard-local-ssd=false` flag:

**Preview — The`--discard-local-ssd=false` flag **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        gcloud beta compute instances suspend INSTANCE_NAMES \
            --discard-local-ssd=false \
            --zone=ZONE
        




Replace the following:

  * `INSTANCE_NAMES`: a whitespace-separated list of names of instances—for example, `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the instances are located.




###  REST 

When suspending an instance that has Local SSD disks attached, specify whether to discard or preserve Local SSD data as follows:

  * To discard Local SSD data, make a `POST` request to the [`instances.suspend` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/suspend). In the request URL, include the `discardLocalSsd` query parameter set to `true`:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/suspend?discardLocalSsd=true
        

  * To preserve Local SSD data, make a `POST` request to the [`beta.instances.suspend` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/suspend). In the request URL, include the `discardLocalSsd` query parameter set to `false`:

**Preview — The`discardLocalSsd=false` query parameter **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/suspend?discardLocalSsd=false
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the instance is located.

  * `ZONE`: the zone where the instance is located.

  * `INSTANCE_NAME`: the name of the instance.




## Resume a suspended instance

Before resuming a suspended compute instance, consider the following:

  * You can resume an instance only if there is sufficient capacity in the zone where the instance is located. This isn't usually a problem. If you have troubles resuming an instance, then try again later.

  * If you attached Local SSD disks to the instance and chose to preserve Local SSD data when suspending it, then you might need to remount the Local SSD disks after resuming it. For more information, see how to remount non-boot disks on [Linux instances](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux) or [Windows instances](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows).




You can resume multiple instances simultaneously or individual instances. For multiple instances, use the Google Cloud console or, for instances located in the same zone, the gcloud CLI. For individual instances, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select one or more suspended instances to resume.

  3. Click play_arrow **Start / Resume** , and then click **Start**.




###  gcloud 

To resume one or more suspended instances in a single zone, use the [`gcloud compute instances resume` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/resume):
    
    
    gcloud compute instances resume INSTANCE_NAMES \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a whitespace-separated list of names of instances—for example, `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the suspended instances are located.




###  Go 
    
    
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
    

###  Java 
    
    
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

###  Node.js 
    
    
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

###  PHP 
    
    
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
    
    

###  REST 

To resume a suspended instance, make a `POST` request to the [`instances.resume` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/resume):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/resume
    

Replace the following:

  * `INSTANCE_NAME`: the name of the suspend instance to resume.

  * `PROJECT_ID`: the ID of the project where the suspended instance is located.

  * `ZONE`: the zone where the suspended instance is located.




## What's next

  * [Delete a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)

  * [Stop or restart a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)

  * [Troubleshooting VM suspension](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
