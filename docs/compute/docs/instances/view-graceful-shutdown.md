---
url: https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown/
title: View graceful shutdown in a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:02:35.211084+00:00
---

# View graceful shutdown in a Compute Engine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View graceful shutdown in a Compute Engine instance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to view the settings and progress of a graceful shutdown in a Compute Engine instance. To learn more about graceful shutdown, see [Graceful shutdown overview](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview).

When you view the details of an instance, you can do the following:

  * **View graceful shutdown settings**. You can verify if graceful shutdown is enabled and how long it lasts.

  * **Monitor graceful shutdown**. When a graceful shutdown is in progress, you can check the following:

    * When the graceful shutdown process times out.

    * If a stop or delete operation is in progress.




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

To get the permission that you need to view the graceful shutdown of a compute instance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.instances.get` on the project permission, which is required to view the graceful shutdown of a compute instance. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View graceful shutdown settings

To view the graceful shutdown settings in a compute instance, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of your instance.

The details page of the instance opens on the **Details** tab.

  3. To check the graceful shutdown settings, in the **Availability policies** section, check the value of the **Graceful shutdown maximum duration** field. This field shows the graceful shutdown period. If it shows a hyphen (**-**), then graceful shutdown is disabled.




###  gcloud 

To view the graceful shutdown settings in an instance, use the [`gcloud beta compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/describe):
    
    
    gcloud beta compute instances describe INSTANCE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `ZONE`: the zone where the instance exists.




If graceful shutdown is enabled, then the output is similar to the following:
    
    
    ...
    scheduling:
      ...
      gracefulShutdown:
        enabled: true
        maxDuration:
          seconds: 'MAX_DURATION'
      ...
    ...
    

The output includes the `MAX_DURATION` value. This value indicates how long the graceful shutdown period lasts in seconds. If you didn't specify a custom shutdown period when you enabled graceful shutdown in the instance, then Compute Engine omits the `maxDuration` field and sets the graceful shutdown period to 10 minutes.

###  REST 

To view the graceful shutdown settings in an instance, make a `GET` request to [beta `instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/get):
    
    
    GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created the instance.

  * `ZONE`: the zone where the instance exists.

  * `INSTANCE_NAME`: the name of the instance.




If graceful shutdown is enabled, then the output is similar to the following:
    
    
    {
      ...
      "scheduling": {
        ...
        "gracefulShutdown": {
          "enabled": true,
          "maxDuration": {
            "seconds": "MAX_DURATION"
          }
        }
      },
      ...
    }
    

The output includes the `MAX_DURATION` value. This value indicates how long the graceful shutdown period lasts in seconds. If you didn't specify a custom shutdown period when you enabled graceful shutdown in the instance, then Compute Engine omits the `maxDuration` field and sets the graceful shutdown period to 10 minutes.

## Monitor graceful shutdown

To monitor an ongoing graceful shutdown in a compute instance, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of your instance.

The details page of the instance opens on the **Details** tab.

  3. If a graceful shutdown is in progress, then, in the **Basic information** section, check the following fields:

     * **Status** : this field shows the [state of your instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle#instance-states). During a graceful shutdown, this field displays **Pending stop** and a countdown timer. The timer counts down to the moment when the graceful shutdown ends.

     * **Target state** : this field shows whether Compute Engine is stopping (**Stopped**) or deleting (**Deleted**) the instance.




###  gcloud 

To monitor an ongoing graceful shutdown in an instance, use the [`gcloud beta compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/describe):
    
    
    gcloud beta compute instances describe INSTANCE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.

  * `ZONE`: the zone where the instance exists.




If a graceful shutdown is in progress, then the output is similar to the following:
    
    
    ...
    resourceStatus:
      ...
      shutdownDetails:
        maxDuration:
          seconds: 'MAX_DURATION'
        requestTimestamp: 'REQUEST_TIMESTAMP'
        stopState: STOP_STATE
        targetState: TARGET_STATE
    ...
    status: PENDING_STOP
    ...
    

This output includes the following values:

  * `MAX_DURATION`: the duration of the graceful shutdown period in seconds. After Compute Engine sets `STOP_STATE` to `STOPPING`, it deletes the `maxDuration` field.

  * `REQUEST_TIMESTAMP`: the timestamp when the `STOP_STATE` started.

  * `STOP_STATE`: the stopping phase of the instance. The value can be one of the following:

    * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The instance remains in this state until you manually end the graceful shutdown or the graceful shutdown period times out.

    * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

  * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the instance.




If a stop operation is running, then, after Compute Engine sets the `status` field to `TERMINATE`, it deletes the `shutdownDetails` field.

###  REST 

To monitor an ongoing graceful shutdown in an instance, make a `GET` request to the [beta `instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instances/get):
    
    
    GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created the instance.

  * `ZONE`: the zone where the instance exists.

  * `INSTANCE_NAME`: the name of the instance.




If a graceful shutdown is in progress, then the output is similar to the following:
    
    
    {
      ...
      "resourceStatus": {
        ...
        "shutdownDetails": {
          "maxDuration": {
            "seconds": "MAX_DURATION"
          },
          "requestTimestamp": "REQUEST_TIMESTAMP",
          "stopState": "STOP_STATE",
          "targetState": "TARGET_STATE"
        }
      },
      ...
      "status": "PENDING_STOP",
      ...
    }
    

This output includes the following values:

  * `MAX_DURATION`: the duration of the graceful shutdown period in seconds. After Compute Engine sets `STOP_STATE` to `STOPPING`, it deletes the `maxDuration` field.

  * `REQUEST_TIMESTAMP`: the timestamp when the `STOP_STATE` started.

  * `STOP_STATE`: the stopping phase of the instance. The value can be one of the following:

    * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The instance remains in this state until you manually end the graceful shutdown or the graceful shutdown period times out.

    * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

  * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the instance.




If a stop operation is running, then, after Compute Engine sets the `status` field to `TERMINATE`, it deletes the `shutdownDetails` field.

###  Metadata server 

  1. Connect to the instance.

  2. Query the metadata server:
         
         curl "http://metadata.google.internal/computeMetadata/v1/instance/shutdown-details/?recursive=true?alt=json" \-H "Metadata-Flavor: Google"
         

If a graceful shutdown is in progress, then the output is similar to the following:
         
         {
           "maxDuration": "MAX_DURATION",
           "requestTimestamp": "REQUEST_TIMESTAMP",
           "stopState": "STOP_STATE",
           "targetState": "TARGET_STATE"
         }
         

The output includes the following values:

     * `MAX_DURATION`: the duration of the graceful shutdown period in seconds. After Compute Engine sets `STOP_STATE` to `STOPPING`, it deletes the `maxDuration` field.

     * `REQUEST_TIMESTAMP`: the timestamp when the `STOP_STATE` started.

     * `STOP_STATE`: the stopping phase of the instance. The value can be one of the following:

       * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The instance remains in this state until you manually end the graceful shutdown or the graceful shutdown period times out.

       * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

     * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the instance.




## What's next

  * [Disable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
