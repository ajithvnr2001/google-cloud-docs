---
url: https://docs.cloud.google.com/compute/docs/instances/update-instance-properties/
title: Update instance properties \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:51:08.714062+00:00
---

# Update instance properties  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/update-instance-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Update instance properties Stay organized with collections  Save and categorize content based on your preferences. 

You can use a single request from the [Google Cloud CLI](https://docs.cloud.google.com/sdk/install) or the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) to update multiple instance properties and optionally restart the instance if necessary. The update method handles the logic for validating the updated instance properties and ensuring that the necessary resources are available to complete the update successfully. If the request includes invalid properties or if the requested resources are not available, the request returns an error and makes no changes to your instance. This protects the instance from partial updates and protects the instance from being stopped and unable to access resources to start up again.

To update the network interfaces (`networkInterfaces`) of an instance, see instead [Update the network interfaces for an instance](https://docs.cloud.google.com/compute/docs/networking/update-network-interfaces).

To add or remove Dynamic Network Interfaces from an instance, use the following procedures instead of updating the instance properties:

  * [Delete Dynamic NICs from an instance](https://docs.cloud.google.com/vpc/docs/delete-dynamic-nics)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)



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




## Restrictions

  * Instance update requests through the gcloud CLI or the Compute Engine API don't support `PATCH` semantics. The instance resource in the update request must include all of the properties of the instance. Properties that are missing from the instance configuration in your update request are considered to be deleted from the instance.
  * You can update only a specific list of properties.
  * If the instance has Local SSD disks attached, you can't update properties that require the instance to restart while the instance is running. You can delete and then recreate the instance, or [stop the instance](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance), update the properties,and then restart it.
  * You can update the `networkInterfaces` property of an instance, but you can't add virtual NICs (vNICs) to or remove vNICs from an instance.
  * If an instance uses resources that are available only in the beta Compute Engine API, you must use the correct version of the `instances.update` method to update those properties. For example, if you create an instance using the beta Compute Engine API and configure the instance with a resource that only the beta API recognizes, you must also use the beta version of the `instances.update` method to update those resources. The v1 version of the `instances.update` method doesn't recognize the beta resources that your instance uses, so it deletes those beta resources from the instance configuration during the update process. This behavior also applies to resources in the alpha API.



## Permissions

You must have the `compute.instances.update` permission to update instances. This permission is included in several [existing Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/roles-permissions/compute). You must also have permission to use the resources that you want to modify on the instance. For example, to add a disk to an instance you must have the following permissions:

  * The `compute.instances.update` permission on the instance that you want to update.
  * Either `compute.disks.use` permission for an existing disk or `compute.disks.create` on a project where you want to create a new disk.



## Best practices

To ensure that the instance update interface works most effectively for you, use the following best practices:

  * If possible, consistently use the same version of the Compute Engine API to create, set, and update instances. This ensures that you can update and modify any instance resources if they are available only in one version of the API.
  * Although you can use the `instances.update` method to update instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), for most situations it is better to change the [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) of the group and [roll that update out to the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups) instead.
  * If updating a resource that is used by the instance, use the command to update that resource instance of updating the instance properties, for example: 
    * You can modify disks with the `disks.update` method
    * To change the network used by the instance, you can use the `instances.updateNetworkInterface` method, which doesn't require stopping the instance.



## Properties that you can update

You can change only a specific set of instance properties through the update method. Updates to some properties require the instance to restart. To prevent accidental restarts on your instances, your request must define what action is allowed to be taken on your instances. Your request can specify one of the following actions:

  * **`NO_EFFECT`** : the update request checks to see if the request is valid and if the resources are available, but it doesn't execute the update. Use this action to test commands without initiating any actual updates.
  * **`REFRESH`** : the update request runs only if the modified instance properties don't require the instance to restart. The request returns an `INFEASIBLE` error if the request is valid but a restart is required.
  * **`RESTART`** : if the update requires the instance to restart, then the system will restart your instance.



The following properties require a restart (`RESTART`) to update:

  * `disks`: boot disks, including all disks (`disks.deviceName`)
  * `displayDevice`
  * `enableNestedVirtualization`
  * `guestAccelerators`
  * `machineType`
  * `minCpuPlatform`
  * `networkInterfaces`
  * `networkPerformanceConfig`
  * `performanceMonitoringUnit`
  * `reservationAffinity`: You can only update how the instance consumes reservations (`reservationAffinity.consumeReservationType`) as follows: 
    * From consuming any matching reservation (`ANY_RESERVATION`) to not consuming reservations (`NO_RESERVATION`)
    * From not consuming reservations (`NO_RESERVATION`) to consuming any matching reservations (`ANY_RESERVATION`)
  * `resourcePolicies`
  * `scheduling`
  * `serviceAccounts`
  * `shieldedInstanceConfig`
  * `threadsPerCore`
  * `visibleCoreCount`



The following properties only require a refresh (`REFRESH`) to update:

  * `canIpForward`
  * `deletionProtection`
  * `description`
  * `disks`: non-boot disk properties, excluding `deviceName`
  * `labels`
  * `metadata`
  * `nodeAffinities`
  * `tags`



## Update instance properties

Update your instances using the following steps:

  1. Export the existing instance configuration properties.
  2. Modify the properties of the instance configuration.
  3. Run a test request by specifying `NO_EFFECT` as the most disruptive action. The response indicates invalid fields in the instance configuration and indicates the action required to apply the changes.
  4. If the configuration is acceptable, request an instance update and specify the most disruptive action that is acceptable for your instance update.



The system starts the update process only if your request meets the following requirements:

  * The instance `fingerprint` property in your request must match the `fingerprint` of the instance that you are updating. This prevents simultaneous update requests on the same instance from overwriting each other.
  * The properties in your update request must be valid.
  * The resources that you requested must be available.
  * If the properties in your request require the instance to restart, your request must specify `RESTART` as an allowed action.



If the requirements are met, the system starts the instance update process. Otherwise, the system makes no changes to your existing instance or its configuration.

You can initiate updates using either the gcloud CLI or the Compute Engine API.

###  gcloud 

  1. Use the [`instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export) to export the existing instance properties:
         
         gcloud compute instances export INSTANCE_NAME \
             --project PROJECT_ID \
             --zone ZONE \
             --destination=FILE_PATH
         

Replace the following:

     * `INSTANCE_NAME`: the name for the instance that you want to export.
     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `FILE_PATH`: the output path where you want to save the instance configuration file on your local workstation.
  2. Use a text editor to modify one or more properties in the exported instance configuration file. To learn which properties you can update, see the list of updatable properties in this document. For example, to change the machine type of the instance, change the `machineType` property:
         
         ...
         machineType: https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE
         ...
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of the instance, for example, `n1-standard-2`.
**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  3. Use the [`instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) to run a test update of the target instance. Specify the `--most-disruptive-allowed-action=NO_EFFECT` flag. The response identifies misconfigured properties and indicates whether a `RESTART` or `REFRESH` action is required to apply the update.
         
         gcloud compute instances update-from-file INSTANCE_NAME \
             --project PROJECT_ID \
             --zone ZONE \
             --source=FILE_PATH \
             --most-disruptive-allowed-action NO_EFFECT
         

Replace the following:

     * `INSTANCE_NAME`: the name for the instance you want to export.
     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `FILE_PATH`: the path to the modified instance configuration file on your local workstation.
  4. Use the [`instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) to update the target instance. If you are updating a property that requires the instance to restart, include the `--most-disruptive-allowed-action=RESTART` flag. If the properties don't require a restart, specify the `--most-disruptive-allowed-action=REFRESH` flag. To learn which properties require a restart, see the updatable properties list in this document.
         
         gcloud compute instances update-from-file INSTANCE_NAME \
             --project PROJECT_ID \
             --zone ZONE \
             --source=FILE_PATH \
             --most-disruptive-allowed-action ALLOWED_ACTION
         

Replace the following:

     * `INSTANCE_NAME`: the name for the instance you want to export.
     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `FILE_PATH`: the path to the modified instance configuration file on your local workstation.
     * `ALLOWED_ACTION`: defines how disruptive the update can be. Specify `RESTART` to allow for a full restart of the instance. Specify `REFRESH` to update the instance only if the modified properties don't require the instance to restart.



If the update request is valid and the required resources are available, the instance update process begins. You can monitor the status of this operation by [viewing the audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging). If the update requires a restart and your command allows for a `RESTART`, the instance restarts to apply the changes.

###  REST 

  1. Use the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) in the Compute Engine API to export the existing instance properties:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `INSTANCE_NAME`: the name for the instance you want to export.

This request returns an [instance resource definition](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances).

  2. In the response, modify the instance resource properties. To learn which properties are updatable, see the updatable properties list in this document. For example, to change the machine type of the instance, change the `machineType` property. You can change multiple properties.
         
         {
           ...
           "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
           ...
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) of the instance, for example, `n1-standard-2`.
  3. Use the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update) in the Compute Engine API and specify the `mostDisruptiveAllowedAction=NO_EFFECT` query parameter to run a test update of the target instance. The response identifies misconfigured properties and indicates if a `RESTART` or `REFRESH` action is required to apply the update.
         
         PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=NO_EFFECT
         
         {
           ...
           "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/n1-standard-2",
           ...
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `INSTANCE_NAME`: the name for the instance you want to export.
  4. Use the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update) in the Compute Engine API to update the target instance. If you are updating a property that requires an instance restart, include the `mostDisruptiveAllowedAction=RESTART` query parameter to indicate that the instance can be restarted during the update. If the properties don't require a restart, specify the `mostDisruptiveAllowedAction=REFRESH` query parameter. To learn which properties require a restart, see the updatable properties list in this document. Include the full body for the instance resource that you modified. In the following example, the body changes the machine type to `n1-standard-2`:
         
         PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=ALLOWED_ACTION
         
         {
           ...
           "machineType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/n1-standard-2",
           ...
         }
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for this instance.
     * `INSTANCE_NAME`: the name for the instance you want to export.
     * `ALLOWED_ACTION`: defines how disruptive the update can be. Specify `RESTART` to allow for a full restart of the instance. Specify `REFRESH` to update the instance only if the modified properties don't require the instance to restart.



If the update request is valid and the required resources are available, the instance update process begins. You can monitor the status of this operation by [viewing the audit logs](https://docs.cloud.google.com/compute/docs/logging/audit-logging). If the update requires a restart and your command allows for a `RESTART`, the instance restarts to apply the changes.

## What's next

  * Check the instance's [state](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).
  * Learn how to [reserve resources](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) in a specific zone.
  * Learn how to [Update the network interfaces for an instance](https://docs.cloud.google.com/compute/docs/networking/update-network-interfaces).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
