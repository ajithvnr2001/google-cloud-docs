---
url: https://docs.cloud.google.com/compute/docs/manage-pmu-in-vms/
title: Manage the PMU in Compute Engine instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:33:52.927332+00:00
---

# Manage the PMU in Compute Engine instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/manage-pmu-in-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage the PMU in Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

After you've enabled the PMU in a compute instance and run performance-monitoring software on the compute instance, you can do the following:

  * **Change the PMU type enabled in the compute instance**. This change is useful when you want to track different types of low-level CPU events.

  * **Disable the PMU in the compute instance**. This action is useful when you no longer need to access the performance counters in the PMU.




This document explains how to change the performance monitoring unit (PMU) type that is enabled in a Compute Engine instance, or disable it. To learn more about the PMU, see [PMU overview](https://docs.cloud.google.com/compute/docs/pmu-overview).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

To get the permissions that you need to change the PMU type enabled in a compute instance or disable it, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to change the PMU type enabled in a compute instance or disable it. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to change the PMU type enabled in a compute instance or disable it:

  * To update a compute instance: `compute.instances.update` on the compute instance 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Change the PMU type in a compute instance

Before you change the PMU type for an existing A4X, C4A, C4, or M4 instance, [view the details of the compute instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details) by using the Google Cloud CLI or REST API. In the output from the command or API request, verify the following:

  1. To verify that the PMU type is enabled in the compute instance, check the value of the `performanceMonitoringUnit` field. If the field is missing, then the PMU is disabled.

  2. If you want to enable the enhanced PMU type, then you must verify that the compute instance uses one of the following machine types by checking the value of the `machineType` field:

     * A C4 machine type with 144 or 288 vCPUs

     * One of the following M4 machine types:

       * `m4-megamem-112`

       * `m4-megamem-224`

       * `m4-ultramem-56`

       * `m4-ultramem-112`

       * `m4-ultramem-224`

If your compute instance uses a different machine type, then you must [change the machine type that the compute instance uses](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) before you can monitor enhanced PMU types.




You don't have to stop the compute instance to change the PMU type. However, to make the change effective, you must restart the compute instance as described in this section.

To change the PMU type enabled in an existing compute instance, select one of the following options:

###  gcloud 

  1. Create an empty YAML file.

  2. To export the properties of a compute instance into the YAML file that you've just created, use the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export):
         
         gcloud compute instances export INSTANCE_NAME \
             --destination=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance.

     * `YAML_FILE`: the path to the YAML file that you created in the previous step.

     * `ZONE`: the zone where the compute instance exists.

  3. In the YAML configuration file, locate the `performanceMonitoringUnit` field and change its value to specify a different PMU type:
         
         advancedMachineFeatures:
           performanceMonitoringUnit: PMU_TYPE
         

Replace `PMU_TYPE` with one of the following values:

     * Architectural PMU type: `ARCHITECTURAL`

     * Standard PMU type: `STANDARD`

     * Enhanced PMU type: `ENHANCED`

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  4. To update the compute instance and restart it, use the [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) with the `--most-disruptive-allowed-action` flag set to `RESTART`:
         
         gcloud compute instances update-from-file INSTANCE_NAME \
             --most-disruptive-allowed-action=RESTART \
             --source=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance.

     * `YAML_FILE`: the path to the YAML file with the configuration data that you modified in the previous step.

     * `ZONE`: the zone where the compute instance exists.




###  REST 

  1. To view the properties of an existing compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compute instance is located.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of an existing compute instance.

  2. To update the compute instance and restart it, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update) as follows:

     * In the request URL, include the `mostDisruptiveAllowedAction` query parameter set to `RESTART`.

     * For the request body, use the `GET` request output from the previous step. However, in the `advancedMachineFeatures` field, you must change the value of the `performanceMonitoringUnit` field to your chosen PMU type.

The `PUT` request is similar to the following:
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=RESTART
    
    {
      "advancedMachineFeatures": {
        "performanceMonitoringUnit": "PMU_TYPE"
      },
      ...
    }
    

Replace `PMU_TYPE` with one of the following values:

     * Architectural PMU type: `ARCHITECTURAL`

     * Standard PMU type: `STANDARD`

     * Enhanced PMU type: `ENHANCED`




For more information about updating the properties of a compute instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

## Disable the PMU in a compute instance

You can disable the PMU in a compute instance without stopping the compute instance. However, to make the change effective, you must restart the compute instance as described in this section.

To disable the PMU in an existing compute instance, select one of the following options:

###  gcloud 

  1. Create an empty YAML file.

  2. To export the properties of a compute instance into the YAML file that you've just created, use the [`gcloud compute instances export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/export):
         
         gcloud compute instances export INSTANCE_NAME \
             --destination=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance.

     * `YAML_FILE`: the path to the YAML file that you created in the previous step.

     * `ZONE`: the zone where the compute instance exists.

  3. In the YAML configuration file, remove the `performanceMonitoringUnit` field. If the `advancedMachineFeatures` field is empty, then remove it as well.
         
         advancedMachineFeatures:
           performanceMonitoringUnit: PMU_TYPE
         

**Tip:** To avoid getting an error such as `"ERROR: (gcloud.compute.instances.update-from-file) Cannot parse YAML: [Expected type  for field value, found True (type )]"`, add quotes (`' '`) around any label values of `yes` or `no` in the exported instance configuration file. This indicates the values are strings, not Boolean values.
  4. To update the compute instance and restart it, use the [`gcloud compute instances update-from-file` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update-from-file) with the `--most-disruptive-allowed-action` flag set to `RESTART`:
         
         gcloud compute instances update-from-file INSTANCE_NAME \
             --most-disruptive-allowed-action=RESTART \
             --source=YAML_FILE \
             --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance.

     * `YAML_FILE`: the path to the YAML file with the configuration data that you modified in the previous step.

     * `ZONE`: the zone where the compute instance exists.




###  REST 

  1. To view the properties of an existing compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compute instance exists.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of an existing compute instance.

  2. To update the compute instance and restart it, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). In the request, do the following:

     * In the request URL, include the `mostDisruptiveAllowedAction` query parameter set to `RESTART`.

     * For the request body, use the `GET` request output from the previous step. However, you must remove the `performanceMonitoringUnit` field and, if there aren't other fields in the `advancedMachineFeatures` field, the `advancedMachineFeatures` field too.

The `PUT` request is similar to the following:
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=RESTART
    
    {
      ~"advancedMachineFeatures": {
        ...
      }~,
      ...
    }
    




For more information about updating the properties of a compute instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

## What's next

  * [PMU overview](https://docs.cloud.google.com/compute/docs/pmu-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
