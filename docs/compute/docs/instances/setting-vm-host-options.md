---
url: https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options/
title: Set the host maintenance policy for a compute instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:20:39.049256+00:00
---

# Set the host maintenance policy for a compute instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set the host maintenance policy for a compute instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to set the host maintenance policy for a Compute Engine instance to determine its behavior during host events. To learn more about host maintenance policies, see [Host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#schedulingoptions).

A host maintenance policy determines how your instance responds when the host on which the instance is running requires maintenance or encounters an error. Configuring the host maintenance policy for an instance helps you do the following:

  * Minimize downtime.

  * Prevent data loss.




## Limitations

For host maintenance policies, the following limitations apply:

  * Virtual machine instances using E2 machine types can only live migrate during host maintenance events, unless they're Spot VMs or preemptible VMs.

  * The following instances can only stop during host maintenance events:

    * Instances that [don't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations), such as the following: 
      * H4D instances
      * Z3 instances with more than 18 TiB of attached Titanium SSD
      * Z4D instances with more than 42 TiB of attached Titanium SSD
      * Bare metal instances
      * VMs with GPUs or TPUs attached
    * Spot VMs or preemptible VMs.
  * Spot VMs and preemptible VMs can't automatically restart after host errors or programmed stops.




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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to set the host maintenance policy for a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to set the host maintenance policy for a compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to set the host maintenance policy for a compute instance:

  * To create an instance: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk
  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To update the host maintenance policy for an instance: `compute.instances.setScheduling` on the instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Available host maintenance properties

You can customize how your compute instance behaves during scheduled maintenance or unexpected host events. Unless you specify otherwise, Compute Engine uses default settings when you create an instance, instances in bulk, or an instance template. 

You can configure the following host maintenance properties:

  * **Maintenance behavior (`onHostMaintenance`)**: what happens to your instance during a maintenance event on its host that might cause the instance to restart. You can set this property to one of the following:

    * **Migrate** : Compute Engine automatically live migrates your instance to another host. This is the default setting for all types of instances, except Spot VMs and preemptible VMs.

**Important:** You must configure instances that [don't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations) to stop (**Terminate**) during maintenance events. Otherwise, you encounter errors.
    * **Terminate** : Compute Engine stops your instance. This is the default setting for Spot VMs or preemptible VMs, and it's the only supported setting for H4D instances, Z3 instances with more than 18 TiB of attached Titanium SSD, Z4D instances with more than 42 TiB of attached Titanium SSD, bare metal instances, and instances with GPUs or TPUs attached.

  * **Automatic restart (`automaticRestart`)**: whether your instance restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. You can set this property to one of the following:

    * **On** : Compute Engine automatically restarts the instance. This is the default setting for all types of instances, except for Spot VMs and preemptible VMs. You specify this setting as follows:

      * For the Google Cloud console, in the **Advanced** pane, in the **Automatic restart** list, select **On (recommended)**.

      * For the Google Cloud CLI, use the `--restart-on-failure` flag.

      * For REST, set the `automaticRestart` field to `true`.

    * **Off** : Compute Engine doesn't restart the instance. This is the default setting for Spot VMs or preemptible VMs. You specify this setting as follows:

      * For the Google Cloud console, in the **Advanced** pane, in the **Automatic restart** list, select **Off**.

      * For the gcloud CLI, use the `--no-restart-on-failure` flag.

      * For REST, set the `automaticRestart` field to `false`.



  * **Local SSD data recovery timeout (`localSsdRecoveryTimeout`)**: this setting applies only to instances that have Local SSD disks attached. It determines how long Compute Engine waits to recover data from your Local SSD disks after host errors. By default, this property is unset.

**Important:** The time spent attempting to recover Local SSD data doesn't count towards instance availability SLA downtime. While the instance is in this recovery phase, the [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't cover the instance.

You can set the `localSsdRecoveryTimeout` property to one of the following:

    * **Unset** : Compute Engine uses the default wait time:

      * For Z4D and Z3 VMs: 6 hours

      * For all other types of instances: 1 hour

    * **An integer from 0 to 168** : the number of hours to wait. Setting this property to `0` means that Compute Engine doesn't recover Local SSD data and restarts the instance immediately.

  * **Host error timeout (`hostErrorTimeoutSeconds`)**: this property determines how long Compute Engine waits to restart an unresponsive instance. You must configure this setting before the instance becomes unresponsive. Use a timeout that is long enough for an instance to recover from being unresponsive. You can set this property to one of the following:

    * **Unset** : Compute Engine waits up to 330 seconds (5 minutes and 30 seconds). This is the default setting for any type of instance.

    * **An integer from 90 to 330** : the wait time in seconds, in increments of 30 seconds.




## Set the host maintenance policy for an instance

By default, compute instances use the default settings for their host maintenance policy. To customize these settings, use one of the following methods:

  * Set the policy for an existing instance
  * Set the policy while creating an instance
  * Set the policy while creating instances in bulk
  * Set the policy while creating an instance template



### Set the policy for an existing instance

Before you change the host maintenance policy of an existing instance, ensure the following:

  * You can't change the maintenance behavior (`onHostMaintenance`) of the following types of instances:

    * VMs that use E2 machine types.

    * Spot VMs or preemptible VMs.

    * Instances that [don't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations).

  * You can't configure Spot VMs or preemptible VMs to automatically restart after host errors or programmed stops.




To change the Local SSD data recovery timeout in an instance that has Local SSD disks attached, use the gcloud CLI or REST API. Otherwise, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of the instance that you want to update. A page that gives the details of the instance appears.

  3. Click edit **Edit**. A page that lets you edit instance properties appears.

  4. In the **Management** section, you can do one or more of the following:

     * To change the behavior during maintenance events, select another option from the **On host maintenance** list

     * To change the timeout period before restarting an unresponsive instance, select another option from the **Host error timeout** list.

     * To change whether to restart the instance or not after host errors or programmed stops, select another option from the **Automatic restart** list.

  5. Click **Save**.




###  gcloud 

To change the host maintenance policy in an existing instance, use the [`gcloud compute instances set-scheduling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling) with one or more of the following flags:

  * To change host maintenance behavior, include the `--maintenance-policy` flag.

  * To change automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `--restart-on-failure` flag.

    * To prevent the instance from automatically restarting, include the `--no-restart-on-failure` flag.

  * To change the Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `--local-ssd-recovery-timeout` flag.

  * To change the host error timeout, include the `--host-error-timeout-seconds` flag.




For example, to change host maintenance behavior, automatically restart the instance after host errors or programmed stops, change the Local SSD data recovery timeout, and change the host error timeout, run the following command:
    
    
    gcloud compute instances set-scheduling INSTANCE_NAME \
        --host-error-timeout-seconds=ERROR_DETECTION_TIMEOUT \
        --local-ssd-recovery-timeout=LOCAL_SSD_RECOVERY_TIMEOUT \
        --maintenance-policy=MAINTENANCE_POLICY \
        --restart-on-failure \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of your instance.

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before Compute Engine restarts an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instance. The value can be either `TERMINATE` or `MIGRATE`.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `ZONE`: the zone where your instance exists.




###  REST 

To change the host maintenance policy in an existing instance, make a `POST` request to the [`instances.setScheduling` method](https://docs.cloud.google.com/compute/docs/reference/latest/instances/setScheduling). In the request body, include one or more of the following fields:

  * To change host maintenance behavior, include the `onHostMaintenance` field.

  * To change automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `automaticRestart` field.

    * To prevent the instance from automatically restarting, include the `automaticRestart` field.

  * To change the Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `localSsdRecoveryTimeout` field.

  * To change the host error timeout, include the `hostErrorTimeoutSeconds` field.




For example, to change host maintenance behavior, automatically restart the instance after host errors or programmed stops, change the Local SSD data recovery timeout, and change the host error timeout, make a request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/setScheduling
    
    {
      "automaticRestart": AUTOMATIC_RESTART,
      "hostErrorTimeoutSeconds": ERROR_DETECTION_TIMEOUT,
      "localSsdRecoveryTimeout": LOCAL_SSD_RECOVERY_TIMEOUT,
      "onHostMaintenance": "MAINTENANCE_POLICY"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where your instance exists.

  * `ZONE`: the zone where your instance exists.

  * `INSTANCE_NAME`: the name of your instance.

  * `AUTOMATIC_RESTART`: the automatic restart behavior of the instance if it crashes or Compute Engine stops it for a programmed stop. Specify one of the following values:

    * To let Compute Engine automatically restart your instance: `true`

    * To prevent automatic restarts: `false`

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instance. The value can be either `TERMINATE` or `MIGRATE`.




### Set the policy while creating an instance

You can set the host maintenance policy of a compute instance while creating it.

To set the Local SSD data recovery timeout while creating an instance that has Local SSD disks attached, use the gcloud CLI or REST API. Otherwise, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Name** field, enter a name for the instance.

  3. In the **Region** and **Zone** fields, specify in which region and zone to create the instance.

  4. Specify the machine type for the instance.

  5. In the navigation menu, click **Advanced**.

  6. In the **Provisioning model** section, expand **VM provisioning model advanced settings** , and then do one or more of the following:

     * To set the behavior during maintenance events, in the **On host maintenance** list, select one of the following options:

       * To migrate the instance during host maintenance events, select **Migrate VM instance (recommended)**.

       * To stop the instance during host maintenance events, select **Terminate VM instance**.

     * To set the timeout period before restarting an unresponsive instance, in the **Host error timeout** list, select one of the following options:

       * To not specify a host error timeout, select **Unspecified (default)**.

       * To specify a host error timeout, select one of the available options, up to **5 minutes and 30 seconds**.

     * To set whether to restart the instance if it crashes or is stopped, In the **Automatic restart** list, select one of the following options:

       * To automatically restart the instance after host errors or programmed stops, select **On (recommended)**.

       * To prevent the instance from automatically restarting after host errors or programmed stops, select **Off**.

  7. Click **Create**.




###  gcloud 

To set the host maintenance policy of an instance while creating it, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with one or more of the following flags:

  * To set the host maintenance behavior, include the `--maintenance-policy` flag.

  * To set the automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `--restart-on-failure` flag.

    * To prevent the instance from automatically restarting, include the `--no-restart-on-failure` flag.

  * To set a Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `--local-ssd-recovery-timeout` flag.

  * To set a host error timeout, include the `--host-error-timeout-seconds` flag.




For example, to set the host maintenance behavior, automatically restart the instance after host errors or programmed stops, set a Local SSD data recovery timeout, and set a host error timeout, run the following command:

**Important:** Spot VMs and preemptible VMs don't support automatic restarts after host errors or programmed stops. If you include the `--restart-on-failure` flag when you create these types of VMs, then Compute Engine ignores it. This behavior is the same as using the `--no-restart-on-failure` flag.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --host-error-timeout-seconds=ERROR_DETECTION_TIMEOUT \
        --local-ssd-recovery-timeout=LOCAL_SSD_RECOVERY_TIMEOUT \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=MAINTENANCE_POLICY \
        --restart-on-failure \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MACHINE_TYPE`: the machine type to use.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instance. The value can be either `TERMINATE` or `MIGRATE`. If you're creating a Spot VM, preemptible VM, or an instance that [doesn't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations), then you can only use `TERMINATE`.

  * `ZONE`: the zone in which to create the instance.




###  REST 

To set the host maintenance policy of an instance while creating it, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include one or more of the following fields in the `scheduling` field:

  * To set the host maintenance behavior, include the `onHostMaintenance` field.

  * To set the automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `automaticRestart` field.

    * To prevent the instance from automatically restarting, include the `automaticRestart` field.

  * To set a Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `localSsdRecoveryTimeout` field.

  * To set a host error timeout, include the `hostErrorTimeoutSeconds` field.




For example, to set the host maintenance behavior, automatically restart the instance after host errors or programmed stops, set a Local SSD data recovery timeout, and set a host error timeout, make a request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "scheduling": {
        "automaticRestart": AUTOMATIC_RESTART,
        "hostErrorTimeoutSeconds": ERROR_DETECTION_TIMEOUT,
        "localSsdRecoveryTimeout": LOCAL_SSD_RECOVERY_TIMEOUT,
        "onHostMaintenance": "MAINTENANCE_POLICY"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance.

  * `ZONE`: the zone in which to create the instance.

  * `INSTANCE_NAME`: the name of the instance.

  * `MACHINE_TYPE`: the machine type to use.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `AUTOMATIC_RESTART`: the automatic restart behavior of the instance if it crashes or Compute Engine stops it for a programmed stop. Specify one of the following values:

    * To let Compute Engine automatically restart your instance: `true`

    * To prevent automatic restarts: `false`

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instance. The value can be either `TERMINATE` or `MIGRATE`. If you're creating a Spot VM or an instance that [doesn't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations), then you can only use `TERMINATE`.




For more information about creating an instance, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

### Set the policy while creating instances in bulk

To set the host maintenance policy while creating instances in bulk, select one of the following options:

###  gcloud 

To set the host maintenance policy while creating instances in bulk, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create) with one or more of the following flags:

  * To set the host maintenance behavior, include the `--maintenance-policy` flag.

  * To set the automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `--restart-on-failure` flag.

    * To prevent the instance from automatically restarting, include the `--no-restart-on-failure` flag.

  * To set a Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `--local-ssd-recovery-timeout` flag.

  * To set a host error timeout, include the `--host-error-timeout-seconds` flag.




For example, to set the host maintenance behavior, automatically restart the instance after host errors or programmed stops, set a Local SSD data recovery timeout, and set a host error timeout, run the following command. The following example also creates instances in a single zone and specifies a name pattern for the instances:

**Important:** Spot VMs and preemptible VMs don't support automatic restarts after host errors or programmed stops. If you include the `--restart-on-failure` flag when you create these types of VMs, then Compute Engine ignores it. This behavior is the same as using the `--no-restart-on-failure` flag.
    
    
    gcloud compute instances bulk create \
        --count=COUNT \
        --host-error-timeout-seconds=ERROR_DETECTION_TIMEOUT \
        --local-ssd-recovery-timeout=LOCAL_SSD_RECOVERY_TIMEOUT \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=MAINTENANCE_POLICY \
        --name-pattern=NAME_PATTERN \
        --restart-on-failure \
        --zone=ZONE
    

Replace the following:

  * `COUNT`: the number of instances to create.

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MACHINE_TYPE`: the machine type to use.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instances. The value can be either `TERMINATE` or `MIGRATE`. If you're creating Spot VMs, preemptible VMs, or instances that [don't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations), then you can only use `TERMINATE`.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of instance specified by `COUNT`.

  * `ZONE`: the zone in which to create the instances.




###  REST 

To set the host maintenance policy while creating instances in bulk, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). In the request body, include one or more of the following fields in the `scheduling` field:

  * To set the host maintenance behavior, include the `onHostMaintenance` field.

  * To set the automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `automaticRestart` field.

    * To prevent the instance from automatically restarting, include the `automaticRestart` field.

  * To set a Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `localSsdRecoveryTimeout` field.

  * To set a host error timeout, include the `hostErrorTimeoutSeconds` field.




For example, to set the host maintenance behavior, automatically restart the instance after host errors or programmed stops, set a Local SSD data recovery timeout, and set a host error timeout, make a request as follows. The following example also creates instances in a single zone and specifies a name pattern for the instances:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    
    {
      "count": COUNT,
      "namePattern": "NAME_PATTERN",
      "instanceProperties": {
        "machineType": "MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "automaticRestart": AUTOMATIC_RESTART,
          "hostErrorTimeoutSeconds": ERROR_DETECTION_TIMEOUT,
          "localSsdRecoveryTimeout": LOCAL_SSD_RECOVERY_TIMEOUT,
          "onHostMaintenance": "MAINTENANCE_POLICY"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instances.

  * `ZONE`: the zone in which to create the instances.

  * `COUNT`: the number of instances to create.

  * `NAME_PATTERN`: the name pattern for the instances. To replace a sequence of numbers in an instance name, use a sequence of hash (`#`) characters. For example, using `instance-#` for the name pattern generates instances with names starting with `instance-1`, `instance-2`, and continuing up to the number of instance specified by `COUNT`.

  * `MACHINE_TYPE`: the machine type to use.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `AUTOMATIC_RESTART`: the automatic restart behavior of the instance if it crashes or Compute Engine stops it for a programmed stop. Specify one of the following values:

    * To let Compute Engine automatically restart your instance: `true`

    * To prevent automatic restarts: `false`

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instances. The value can be either `TERMINATE` or `MIGRATE`. If you're creating Spot VMs, preemptible VMs, or instances that [don't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations), then you can only use `TERMINATE`.




For more information about creating instances in bulk, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

### Set the policy while creating an instance template

You can set the host maintenance policy while creating an instance template. All compute instances that you create using the template inherit the host maintenance policy specified in the template.

To set the Local SSD data recovery timeout while creating an instance template that specifies Local SSD disks, use the gcloud CLI or REST API. Otherwise, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create instance template** page appears.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select one of the following options:

     * To create a regional instance template, select **Regional (recommended)** , and then select the region in which to create the template.

     * To create a global instance template, select **Global**.

  5. In the **Machine configuration** section, specify the machine type for the instance template.

  6. In the **Provisioning model** section, expand **VM provisioning model advanced settings** , and then do one or more of the following:

     * To change the behavior during maintenance events, in the **On host maintenance** list, select one of the following options:

       * To migrate the instance during host maintenance events, select **Migrate VM instance (recommended)**.

       * To stop the instance during host maintenance events, select **Terminate VM instance**.

     * To change the timeout period before restarting an unresponsive instance, in the **Host error timeout** list, select one of the following options:

       * To not specify a host error timeout, select **Unspecified (default)**.

       * To specify a host error timeout, select one of the available options, up to **5 minutes and 30 seconds**.

     * To change whether to restart the instance if it crashes or is stopped, In the **Automatic restart** list, select one of the following options:

       * To automatically restart the instance after host errors or programmed stops, select **On (recommended)**.

       * To prevent the instance from automatically restarting after host errors or programmed stops, select **Off**.

  7. Click **Create**.




###  gcloud 

To set the host maintenance policy while creating an instance template, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with one or more of the following flags:

  * To set the host maintenance behavior, include the `onHostMaintenance` field.

  * To set the automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `automaticRestart` field.

    * To prevent the instance from automatically restarting, include the `automaticRestart` field.

  * To set a Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `localSsdRecoveryTimeout` field.

  * To set a host error timeout, include the `hostErrorTimeoutSeconds` field.




For example, to set the host maintenance behavior, automatically restart the instance after host errors or programmed stops, set a Local SSD data recovery timeout, and set a host error timeout, run the following command. The following example also creates a regional instance template. To create a global instance template, use the same command without the `--instance-template-region` flag.

**Important:** Spot VMs and preemptible VMs don't support automatic restarts after host errors or programmed stops. If you include the `--restart-on-failure` flag when you create these types of VMs, then Compute Engine ignores it. This behavior is the same as using the `--no-restart-on-failure` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --host-error-timeout-seconds=ERROR_DETECTION_TIMEOUT \
        --instance-template-region=REGION \
        --local-ssd-recovery-timeout=LOCAL_SSD_RECOVERY_TIMEOUT \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=MAINTENANCE_POLICY \
        --restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `REGION`: the region in which to create the instance template.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MACHINE_TYPE`: the machine type to use.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instances. The value can be either `TERMINATE` or `MIGRATE`. If you're specifying a Spot VM, preemptible VM, or instance type that [doesn't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations) in the instance template, then you can only use `TERMINATE`.




###  REST 

To set the host maintenance policy while creating an instance template, make a `POST` request to one of the following methods:

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert)




In the request body, include one or more of the following fields in the `scheduling` field:

  * To set the host maintenance behavior, include the `onHostMaintenance` field.

  * To set the automatic restart behavior, do one of the following:

    * To automatically restart the instance, include the `automaticRestart` field.

    * To prevent the instance from automatically restarting, include the `automaticRestart` field.

  * To set a Local SSD data recovery timeout if your instance has Local SSD disks attached, include the `localSsdRecoveryTimeout` field.

  * To set a host error timeout, include the `hostErrorTimeoutSeconds` field.




For example, to set the host maintenance behavior, automatically restart the instance after host errors or programmed stops, set a Local SSD data recovery timeout, and set a host error timeout, make a request as follows. The following example also creates a regional instance template.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "scheduling": {
          "automaticRestart": AUTOMATIC_RESTART,
          "hostErrorTimeoutSeconds": ERROR_DETECTION_TIMEOUT,
          "localSsdRecoveryTimeout": LOCAL_SSD_RECOVERY_TIMEOUT,
          "onHostMaintenance": "MAINTENANCE_POLICY"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `REGION`: the region in which to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type to use.

  * `AUTOMATIC_RESTART`: the automatic restart behavior of the instance if it crashes or Compute Engine stops it for a programmed stop. Specify one of the following values:

    * To let Compute Engine automatically restart your instance: `true`

    * To prevent automatic restarts: `false`

  * `ERROR_DETECTION_TIMEOUT`: the number of seconds before restarting an unresponsive instance. The value must be between `90` (90 seconds) and `330` (330 seconds, or 5 minutes and 30 seconds). Only 30-second increments are allowed.

  * `LOCAL_SSD_RECOVERY_TIMEOUT`: the number of hours to spend recovering data from the attached Local SSD disks. The value must be between `0` (0 hours) and `168` (168 hours, or 7 days). Setting this field to `0` means that Compute Engine doesn't recover Local SSD data.

  * `MAINTENANCE_POLICY`: the maintenance behavior of the instances. The value can be either `TERMINATE` or `MIGRATE`. If you're specifying a Spot VM, preemptible VM, or instance type that [doesn't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations) in the instance template, then you can only use `TERMINATE`.




For more information about creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## View host maintenance policy of an instance

You can view the host maintenance policy of an instance by [viewing the instance's details](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).

When viewing the instance's details using the gcloud CLI or REST API, you can only view the `localSsdRecoveryTimeout` and `hostErrorTimeoutSeconds` fields if you specified them while creating or updating the instance.

To view the Local SSD data recovery timeout in an instance that has Local SSD disks attached, use the gcloud CLI or REST API. Otherwise, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the instance that you want to view. A page that gives the details of the instance appears.

  3. On the **Details** tab, in the **Management** section, in the **Availability policies** section, you can view the following:

     * In the **On host maintenance** field, you can see the instance's host maintenance behavior events.

     * In the **Host error timeout** field, you can see the amount of time the instance waits before restarting or stopping the instance after detecting that it's unresponsive. If the value is unset (**—**), then the default wait time is 5 minutes and 30 seconds.

     * In the **Automatic restart** restart field, you can see whether the instance automatically restarts the instance after it crashes or Compute Engine stops it for a programmed stop.




###  gcloud 

To view the host maintenance policy for an instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) with the `--flatten` flag set to `scheduling`:
    
    
     gcloud compute instances describe INSTANCE_NAME \
        --flatten=scheduling \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `ZONE`: the zone where the instance is located.




The output is similar to the following:
    
    
    ---
    scheduling:
      automaticRestart: true
      hostErrorTimeoutSeconds: 120
      localSsdRecoveryTimeout:
        nanos: 0
        seconds: '10800'
      onHostMaintenance: MIGRATE
      preemptible: false
      provisioningModel: STANDARD
    

###  REST 

To view the host maintenance policy for an instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get). In the request URL, include the `fields` query parameter and set it to `scheduling`:
    
    
      GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?fields=scheduling
    

Replace the following:

  * `PROJECT_ID`: the project where the instance exists.

  * `ZONE`: the zone where the instance exists.

  * `INSTANCE_NAME`: the name of the instance.




The output is similar to the following:
    
    
    {
      "scheduling": {
        "onHostMaintenance": "MIGRATE",
        "automaticRestart": true,
        "preemptible": false,
        "provisioningModel": "STANDARD",
        "localSsdRecoveryTimeout": {
          "seconds": "10800",
          "nanos": 0
        }
      }
    }
    

## What's next

  * [Live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process)

  * [Query the metadata server for maintenance event notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
