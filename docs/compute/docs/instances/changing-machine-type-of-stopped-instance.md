---
url: https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance/
title: Edit the machine type of a compute instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:08:08.864895+00:00
---

# Edit the machine type of a compute instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Edit the machine type of a compute instance Stay organized with collections  Save and categorize content based on your preferences. 

If your virtual machine (VM) instance doesn't have attached Local SSD and is not part of a managed instance group (MIG), you can change the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of your instance after [stopping](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance) it.

If your existing machine type is not a good fit for the workloads you run on your VM, change the machine type of that VM. For example, you can start a VM with a smaller machine type during setup, development, and testing and change the VM to use a larger machine type when you are ready for production workloads.

You can use this procedure in the following situations:

  * To change to a similar machine type but with a different number of vCPUs or memory within the same machine series, for example: 
    * You can change `n2-highcpu-4` to `n2-standard-4`.
    * You can change `c3d-standard-30` to `c3d-highmem-30`.
  * To change the machine type to use a different machine series. This is supported for only [first and second generation machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology), excluding the T2A and A2 machine series. For example: 
    * You can change `n2-standard-4` to `c2-standard-8`.
    * You can change `n1-highmem-4` to `n2d-standard-16`.



If you want to change the machine type for a VM that uses a first or second generation machine series (N1, N2, M1, etc.) to a machine type for a third generation or later machine series (M3, C3, N4, etc.), you must use the procedure documented in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).

You can change the machine type without affecting the following resources:

  * The VM's SSH keys
  * The VM configurations, such as VM metadata
  * The data on attached Persistent Disk or Hyperdisk, including installed applications and application data



To change the machine type of VMs within a MIG, see [Automatically apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).

**Caution** : 

  * If you stop a VM that belongs to a MIG, the VM might be recreated. Recreating the VM can cause data loss from VM's disks and can also prevent you from changing the machine type.
  * The PCI device order can change when you restart the VM after changing the machine type, which can cause `udev` to change the network device name. The change in the network device name might cause startup issues.



## Before you begin

  * Understand how to [stop a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance). 
  * Understand [machine types](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

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

To get the permissions that you need to change the machine type of a VM, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to change the machine type of a VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to change the machine type of a VM:

  * `compute.instances.setMachineType` on VM
  * `compute.instances.start` on VM
  * `compute.instances.stop` on VM



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * If your compute instance has one or more Local SSD attached, then use the instructions in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).
  * If your compute instance uses an [ephemeral external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#ephemeraladdress), the IP address might change when you modify the instance's machine type. To preserve the IP address, [promote it to a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#promote_ephemeral_ip) before you change the machine type.
  * Changing the machine type of a compute instance isn't available for some configurations: 
    * You can't change the machine type for bare metal instances.
    * If you want to change the machine type from a first or second generation [machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) to a machine type for a third generation or later machine series, you can't use this procedure. Instead, follow the instructions in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).
    * If you want to change the machine type to an Arm machine type, you can't use this procedure. Instead, follow the instructions in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).
    * For accelerator-optimized instances, you can't change the machine type by using this procedure. However, for G4, G2, A2 Standard, and N1 instances, to change to a similar machine type but with a different number of GPUs within the same accelerator-optimized machine series follow the instructions in [Modify GPU count for accelerator-optimized instances](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus#modify-gpu-count).
    * If you want to change the machine type to a newer machine type, but also want to add additional network interfaces to the instance, then you can't use this procedure. Instead, follow the instructions in [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).



## Billing implications

Each machine type is billed at a different rate, so make sure you understand the [pricing](https://cloud.google.com/compute/vm-instance-pricing) implications of changing machine types. For example, an `e2-standard-2` machine type costs more than an `e2-micro` machine type.

Changing a machine type might also affect the sustained use discounts for that VM. Sustained use discounts are calculated [separately for different categories](https://docs.cloud.google.com/compute/docs/sustained-use-discounts#calculating_discounts) in the same region. If you change machine types so that the new machine type is in a different category, the subsequent running time of the VM counts toward the sustained use discount of the new category.

For example, assume you have a VM with `n2-standard-2` machine type running for half a month. You then decide to change the machine type to `m1-ultramem-40`. Once you make that change, Compute Engine starts counting the running time of the VM towards the sustained use discount of the memory-optimized vCPU and memory category.

On your bill, you would see a sustained use discount applied to the `n2-standard-2` machine type from before you made the machine type change, and a separate sustained use discount for `m1-ultramem-40`, if your VM remains running on `m1-ultramem-40` for at least a 25% of the rest of the month.

**Note:** If you plan to change the machine type to a newer generation machine series within the same family, the [committed use discount (CUD)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for the new machine type might not be combinable with your current CUD.

## Move to a smaller machine type

If you move from a machine type with more resources to a machine type with fewer resources, such as moving from a `e2-standard-8` machine type to a `e2-standard-2`, you could run into hardware resource issues or performance limitations because smaller machine types are less powerful than larger machine types. Make sure that your new machine type is able to support any applications or services that are running on your current VM, or that you update your services and applications to run on the smaller machine types.

Review the _rightsizing recommendations_ before changing the machine type. For information about Compute Engine sizing recommendations, see [Applying machine type recommendations for VM instances](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).

## Best practices

Here are some best practices to help you successfully change the VM machine type.

  * **Make regular backups of your Persistent Disk data using snapshots**. Consider [taking a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) of your Persistent Disk data before you change the machine type. If you want to make sure the new machine type is able to support the data on the existing VM, you can take a Persistent Disk snapshot and use it to start a second VM with the new machine type to confirm that the VM starts up successfully.

  * **Add additional disks to the`/etc/fstab` file**. If you have additional disks attached to your VM, make sure they are added to the `/etc/fstab` file so that they are automatically mounted when the VM reboots.

  * **Create a reservation before changing the machine type**. To avoid errors related to resource availability, create [Compute Engine reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) for the new machine types when they _are available_ to reserve them within a zone. Reservations help ensure that the resources are available when you need them.




To create a reservation, complete the following steps:

  1. [Create a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project) (or identify existing reservations) with identical [properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements) as the planned VMs. The reservation's VM count needs to be equal to or greater than the number of VMs that you want to change. Optionally, to prevent other VMs from consuming this reservation, use the `specificReservationRequired` option.

  2. Verify that the planned VMs will be able to consume the reservation:

     1. [Verify that the VMs have the correct reservation affinity](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption#vm-reservation-affinity-incorrect).
     2. Immediately before changing the VMs, [ensure the reservation has enough capacity](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption#reservation-already-consumed).



## Change a machine type

You can only change the machine type of a stopped VM. A VM is considered stopped only when the VM is in the `TERMINATED` state. You can't change the machine type of a running VM. 

If you are upgrading your machine type to the latest generation, review [Evaluate VM migration options](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm#evaluate-vm-migration-options) before proceeding.

**Caution:** If you don't have reservations for the new machine types, changing the machine type can result in resource availability errors. Resource availability errors are more likely for uncommon resource types and large requests, and can be avoided by requesting different resources, requesting fewer resources at a time, or using reservations. For more information, see [resource availability errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation#resource_availability).

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the VM for which you want to change machine type.

  3. From the **VM instance details** page, complete the following steps:

     1. If the VM is running, click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.
     2. To edit the VM, click edit **Edit**.
     3. In the **Machine configuration** section, select the machine type that you want to use, or create a [custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

     4. To save your changes, click **Save**.

     5. Restart the VM.




###  gcloud 

  1. Stop the VM by using the [`gcloud compute instances stop` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop):
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the VM containing the machine type to change.

  2. Change the machine type by using the [`gcloud compute instances set-machine-type` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-machine-type):
         
         gcloud compute instances set-machine-type VM_NAME \
             --machine-type NEW_MACHINE_TYPE
         

Replace `NEW_MACHINE_TYPE` with the new machine type for the VM. The machine type can be one of the following:

     * A [predefined machine type](https://docs.cloud.google.com/compute/docs/machine-resource)

For example: `e2-standard-2`

     * A [custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)

For example, you can specify `--machine-type e2-custom-4-2048` to set a custom machine type that has 4 vCPUs and 2 GB of memory.

  3. Start the VM by using the [`gcloud compute instances start` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start):
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the VM that you changed.




###  Java 

### Java

Before trying this sample, follow the Java setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/overview). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html);
    import com.google.cloud.compute.v1.[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html).[Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html);
    import com.google.cloud.compute.v1.[InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html);
    import com.google.cloud.compute.v1.[InstancesSetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineTypeRequest.html);
    import com.google.cloud.compute.v1.[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class ChangeInstanceMachineType {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // Project ID or project number of the Cloud project you want to use.
        String projectId = "your-project-id";
        // Name of the zone your instance belongs to.
        String zone = "zone-name";
        // Name of the VM you want to modify.
        String instanceName = "instance-name";
        // The new machine type you want to use for the VM.
        // For example: "e2-standard-8", "e2-custom-4-2048" or "m1-ultramem-40"
        // More about machine types: https://cloud.google.com/compute/docs/machine-resource
        String newMachineType = "e2-standard-8";
        changeMachineType(projectId, zone, instanceName, newMachineType);
      }
    
      // Changes the machine type of VM.
      // The VM needs to be in the 'TERMINATED' state for this operation to be successful.
      public static void changeMachineType(String projectId, String zone, String instanceName,
          String newMachineType)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the `instancesClient.close()` method on the client to safely
        // clean up any remaining background resources.
        try ([InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html) instancesClient = [InstancesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html).create()) {
    
          [Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html) instance = instancesClient.get(projectId, zone, instanceName);
          if (!instance.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getStatus__)().equals([Status](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Status.html).TERMINATED.name())) {
            throw new [Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Error.html)(String.format(
                "Only machines in TERMINATED state can have their machine type changed. "
                    + "%s is in %s state.", instance.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getName__)(), instance.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Instance.html#com_google_cloud_compute_v1_Instance_getStatus__)()));
          }
    
          [InstancesSetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineTypeRequest.html) machineTypeRequest =
              [InstancesSetMachineTypeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesSetMachineTypeRequest.html).newBuilder()
                  .setMachineType(String.format("projects/%s/zones/%s/machineTypes/%s",
                      projectId, zone, newMachineType))
                  .build();
    
          [Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html) response = instancesClient
              .[setMachineTypeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstancesClient.html#com_google_cloud_compute_v1_InstancesClient_setMachineTypeAsync_com_google_cloud_compute_v1_SetMachineTypeInstanceRequest_)(projectId, zone, instanceName, machineTypeRequest)
              .get(3, TimeUnit.MINUTES);
    
          if (response.[hasError](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_hasError__)()) {
            System.out.println("Machine type update failed! " + response);
            return;
          }
          System.out.println("Machine type update - operation status: " + response.[getStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation.html#com_google_cloud_compute_v1_Operation_getStatus__)());
        }
      }
    }

###  Python 

### Python

Before trying this sample, follow the Python setup instructions in the [Compute Engine quickstart using client libraries](https://docs.cloud.google.com/compute/docs/api/using-libraries). For more information, see the [Compute Engine Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/compute/latest). 

To authenticate to Compute Engine, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/compute/docs/authentication#client-libs). 
    
    
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
    
    
    def change_machine_type(
        project_id: str, zone: str, instance_name: str, new_machine_type: str
    ) -> None:
        """
        Changes the machine type of VM. The VM needs to be in the 'TERMINATED' state for this operation to be successful.
    
        Args:
            project_id: project ID or project number of the Cloud project you want to use.
            zone: name of the zone your instance belongs to.
            instance_name: name of the VM you want to modify.
            new_machine_type: the new machine type you want to use for the VM.
                For example: `e2-standard-8`, `e2-custom-4-2048` or `m1-ultramem-40`
                More about machine types: https://cloud.google.com/compute/docs/machine-resource
        """
        client = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesClient](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html)()
        instance = client.[get](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_get)(project=project_id, zone=zone, instance=instance_name)
    
        if instance.status != [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[Instance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.Instance.html).Status.TERMINATED.name:
            raise RuntimeError(
                f"Only machines in TERMINATED state can have their machine type changed. "
                f"{instance.name} is in {instance.status}({instance.status_message}) state."
            )
    
        machine_type = [compute_v1](https://docs.cloud.google.com/python/docs/reference/compute/latest).[InstancesSetMachineTypeRequest](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.InstancesSetMachineTypeRequest.html)()
        machine_type.machine_type = (
            f"projects/{project_id}/zones/{zone}/machineTypes/{new_machine_type}"
        )
        operation = client.[set_machine_type](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient.html#google_cloud_compute_v1_services_instances_InstancesClient_set_machine_type)(
            project=project_id,
            zone=zone,
            instance=instance_name,
            instances_set_machine_type_request_resource=machine_type,
        )
    
        wait_for_extended_operation(operation, "changing machine type")
    
    

###  REST 

  1. Stop the VM by using the [`instances.stop` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop): 
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: the project ID

     * `ZONE`: the zone containing the VM

     * `VM_NAME`: the VM containing the machine type to change

  2. Change the machine type by using the [`instances.setMachineType` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setMachineType):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMachineType
         

In the body of the request, provide the updated `machineType`:
         
         {
             machineType: "zones/MACHINE_TYPE_ZONE/machineTypes/NEW_MACHINE_TYPE"
         }
         

Replace the following:

     * `MACHINE_TYPE_ZONE`: the zone containing the machine type

     * `NEW_MACHINE_TYPE`: the new machine type for the VM

The machine type can be one of the following:

       * A [predefined machine type](https://docs.cloud.google.com/compute/docs/machine-resource)

For example: `e2-standard-2`

       * A [custom machine type](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)

For example, you can specify `--machine-type e2-custom-4-2048` to set a custom machine type that has 4 vCPUs and 2 GB of memory.

  3. Start the VM by using the [`instances.start` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/start): 
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `ZONE`: the zone containing the VM
     * `VM_NAME`: the name of the VM that you changed



## What's next

  * Learn about [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).
  * Learn about [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * Learn about [patterns for scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
  * To update a first or second generation VM to use a third generation or later machine series, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
