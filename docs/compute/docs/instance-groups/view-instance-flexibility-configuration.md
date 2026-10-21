---
url: https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration/
title: View instance flexibility \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:51:55.725357+00:00
---

# View instance flexibility  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View instance flexibility Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view the instance flexibility configuration in a managed instance group (MIG) and the machine types used by each VM in the group.

After you add or make changes to instance flexibility in a MIG, you can do the following:

  * View the instance flexibility configuration to verify if a configuration has been applied or to check if a MIG already has instance flexibility.

  * View the machine types used by each VM to make sure that the machine type that you want to remove from an instance selection is not used by any VM or to check the different machine types used in the MIG.

  * Monitor live runtime VM distributions across machine types and zones to observe and potentially identify improvements for your selected ranks and machine types.




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




## View the instance flexibility configuration

### Console

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. In the **Name** column, click the name of the MIG of which you want to view the instance flexibility configuration.

The overview page of the MIG opens.

  3. Click the **Details** tab.

In the **Instance flexibility** section, the **Instance selections** table shows the instance selection name, rank, and the machine types in a selection. If the MIG doesn't have instance flexibility configured, the **Instance flexibility** section is not shown.




### gcloud

To view the instance flexibility configuration, use the [`instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe). Include the `--format` flag to filter the `instanceFlexibilityPolicy.instanceSelections` properties.
    
    
      gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
          --region REGION \
          --format="json(instanceFlexibilityPolicy.instanceSelections)"
    

The following is a sample output:
    
    
    {
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "instance-selection-1": {
            "machineTypes": [
              "n1-standard-16",
              "n2-standard-16",
              "e2-standard-16"
            ],
            "rank": 1
          }
        }
      }
    }
    

If a MIG doesn't have instance flexibility configured, the output returns `null`.

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG of which you want to view the instance flexibility configuration.
  * `REGION`: the region where the MIG is located.



###  REST 

To view the instance flexibility configuration, use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get). Include the `fields` parameter in the request URL to filter the `instanceFlexibilityPolicy.instanceSelections` properties.
    
    
      GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME?fields=instanceFlexibilityPolicy.instanceSelections
    

The following is a sample output:
    
    
    {
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "instance-selection-1": {
            "machineTypes": [
              "n1-standard-16",
              "n2-standard-16",
              "e2-standard-16"
            ],
            "rank": 1
          }
        }
      }
    }
    

If a MIG doesn't have instance flexibility configured, the output returns `null`.

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG of which you want to view the instance flexibility configuration.



## View the machine types used by each VM

### Console

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. In the **Name** column, click the name of the MIG in which you want view the machine types used by each VM.

The **Overview** page of the MIG opens, which lists all VMs in the group, their machine types, and other details.




### gcloud

To view the machine types used by each VM in a MIG, list the VMs using the [`instance-groups managed list-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances) and include the `--format` flag to filter the `propertiesFromFlexibilityPolicy.machineType` field. You can also filter other fields as needed.
    
    
      gcloud compute instance-groups managed list-instances INSTANCE_GROUP_NAME \
          --region REGION \
          --format='(name,instanceStatus,currentAction,propertiesFromFlexibilityPolicy.machineType,lastAttempt.errors.errors)'
    

The following is a sample output:
    
    
    NAME: example-mig-0md2
    STATUS: RUNNING
    ACTION: NONE
    MACHINE_TYPE: n1-standard-16
    LAST_ERROR:
    
    NAME: example-mig-vbgg
    STATUS: RUNNING
    ACTION: NONE
    MACHINE_TYPE: n1-standard-16
    LAST_ERROR:
    

Replace the following:

  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG of which you want to view the instance flexibility configuration.



###  REST 

To view the machine types used by each VM in a MIG, list the VMs using the [`listManagedInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances) and check the `propertiesFromFlexibilityPolicy.machineType` field in the response.
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/listManagedInstances
    

The following is a sample output; look for the `propertiesFromFlexibilityPolicy` field in which the `machineType` field of a VM is set.
    
    
    {
      "managedInstances": [
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-b/instances/example-mig-0md2",
          "instanceStatus": "RUNNING",
          "id": "2656095434923471959",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-instance-template"
          },
          "targetStatus": "RUNNING",
          "name": "example-mig-0md2",
          "propertiesFromFlexibilityPolicy": {
            "machineType": "n1-standard-16"
          }
        },
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-b/instances/example-mig-vbgg",
          "instanceStatus": "RUNNING",
          "currentAction": "NONE",
          "id": "9171259522409694366",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-instance-template"
          },
          "targetStatus": "RUNNING",
          "name": "example-mig-vbgg",
          "propertiesFromFlexibilityPolicy": {
            "machineType": "n1-standard-16"
          }
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG of which you want to view the instance flexibility configuration.



## Monitor instance distribution

While checking your static instance flexibility policy and listing individual VM machine types provides a snapshot of your current configuration, observing how your MIG allocates capacity over time requires real-time monitoring.

You can use the **GCE MIG Instance Distribution Monitoring** dashboard in Cloud Monitoring to observe runtime instance distributions across zones and machine types in real-time. This visibility helps you verify that your VMs are distributed across your intended ranks and locations when demand or capacity shifts.

For instructions on how to access the monitoring dashboard, see [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

## What's next

  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution).

  * [Change or remove instance flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration).

  * If your MIG doesn't have instance flexibility, [add instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
