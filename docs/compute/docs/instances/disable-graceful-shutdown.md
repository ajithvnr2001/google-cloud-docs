---
url: https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown/
title: Disable graceful shutdown in a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:07.797230+00:00
---

# Disable graceful shutdown in a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Disable graceful shutdown in a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to disable graceful shutdown in an existing Compute Engine instance.

To speed up stop or delete operations and avoid unnecessary charges, it's possible to disable graceful shutdown for a compute instance. This action configures your compute instances to immediately transition to the `STOPPING` state after a stop or delete operation starts. You don't have to wait for the graceful shutdown timer to expire or manually end the graceful shutdown.

To learn more about the requirements and limitations that you apply when you gracefully shutdown a compute instance, see [About graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview).

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

To get the permission that you need to disable graceful shutdown in a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.instances.update` on the compute instance permission, which is required to disable graceful shutdown in a compute instance. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Disable graceful shutdown in a compute instance

You can disable graceful shutdown in a compute instance without restarting the compute instance. However, if the compute instance is gracefully shutting down (`PENDING_STOP`), you must end the graceful shutdown before you can disable it.

To disable graceful shutdown in a compute instance, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of your compute instance. The details page of the compute instance opens on the **Details** tab.

  3. Click edit **Edit**.

  4. In the **Management** section, clear the **Gracefully shut down the VM** checkbox.

  5. Click **Save**.




###  gcloud 

To disable graceful shutdown in a compute instance, use the [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update) with the `--no-graceful-shutdown` flag:
    
    
    gcloud compute instances update INSTANCE_NAME \
        --no-graceful-shutdown \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `ZONE`: the zone where the compute instance exists.




###  REST 

  1. Create an empty JSON file.

  2. To view the properties of an existing compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the compute instance exists.

     * `ZONE`: the zone where the compute instance exists.

     * `INSTANCE_NAME`: the name of an existing compute instance.

  3. In the empty JSON file that you created in the previous steps, do the following:

     1. Enter the compute instance configuration details from the output of the `GET` request.

     2. Locate the `gracefulShutdown.enabled` field, and then change its value to `false`:
            
            {
              ...
              "scheduling": {
                ...
                **"gracefulShutdown": {
                  "enabled": false
                }**
              },
              ...
            }
            

  4. To update the compute instance, make a `PUT` request to the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). Include the following:

     * In the request URL, include the `mostDisruptiveAllowedAction` query parameter.

     * In the request body, include the properties of the compute instance from the JSON file that you created and updated in the previous steps.

The `PUT` request to update the compute instance is similar to the following:
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME?mostDisruptiveAllowedAction=ALLOWED_ACTION
    
    {
      ...
      "scheduling": {
        ...
        "gracefulShutdown": {
          "enabled": false
        }
      },
      ...
    }
    

Replace `ALLOWED_ACTION` with one of the following values:

     * **`NO_EFFECT`** : the request checks if your update request is valid and if the resources are available, but it doesn't update the compute instance.

     * **`REFRESH`** : if the modified properties don't require the compute instance to restart, then Compute Engine updates the compute instance.




For more information about updating the properties of a compute instance, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#update).

## What's next

  * [Limit the runtime of a compute instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)

  * [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
