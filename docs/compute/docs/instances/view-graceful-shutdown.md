---
url: https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown/
title: View graceful shutdown in a Compute Engine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:41.860897+00:00
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

This document explains how to view the settings and progress of a graceful shutdown in a Compute Engine instance.

When you view the details of a compute instance, you can do the following:

  * **View graceful shutdown settings** : check if graceful shutdown is enabled and, if so, view its maximum duration.

  * **Monitor a graceful shutdown** : if a graceful shutdown is in progress, then you can check the time remaining and whether Compute Engine is stopping or deleting the compute instance.




To learn more about the requirements and limitations that you apply when you gracefully shut down a compute instance, see [About graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview).

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

To get the permissions that you need to view the graceful shutdown for a compute instance, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)
  * To view the logs for a compute instance: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view the graceful shutdown for a compute instance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view the graceful shutdown for a compute instance:

  * To view the details of a compute instance: `compute.instances.get` on the project 
  * To view a list of compute instances: `compute.instances.list` on the project 
  * To view a list of Compute Engine operations globally: `compute.globalOperations.list` on the project 
  * To view a list of Compute Engine operations in a region: `compute.regionOperations.list` on the project 
  * To view a list of Compute Engine operations in a zone: `compute.zoneOperations.list` on the project 
  * To view a list of logs: `logging.logEntries.list` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View graceful shutdown settings

To view the graceful shutdown settings in a compute instance, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of your compute instance. The details page of the compute instance opens on the **Details** tab.

  3. To check the graceful shutdown settings, in the **Availability policies** section, check the value of the **Graceful shutdown maximum duration** field. This field shows the graceful shutdown period. If it shows a hyphen (**-**), then graceful shutdown is disabled.




###  gcloud 

To view the graceful shutdown settings in a compute instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `ZONE`: the zone where the compute instance exists.




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
    

The output includes the `MAX_DURATION` value, indicating the maximum duration of the graceful shutdown in seconds. If you didn't specify a custom duration when you enabled graceful shutdown, then Compute Engine omits the `maxDuration` field and uses a default duration of 10 minutes.

###  REST 

To view the graceful shutdown settings in a compute instance, make a `GET` request to [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created the compute instance.

  * `ZONE`: the zone where the compute instance exists.

  * `INSTANCE_NAME`: the name of the compute instance.




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
    

The output includes the `MAX_DURATION` value, indicating the maximum duration of the graceful shutdown in seconds. If you didn't specify a custom duration when you enabled graceful shutdown, then Compute Engine omits the `maxDuration` field and uses a default duration of 10 minutes.

## Monitor graceful shutdown

To monitor an ongoing graceful shutdown in a compute instance, use one of the following methods:

  * Monitor graceful shutdown by using the Google Cloud console, gcloud CLI, or REST API

  * Monitor graceful shutdown by querying metadata server

  * Monitor graceful shutdown by viewing audit logs

  * Monitor graceful shutdown by viewing Compute Engine operations




### Monitor graceful shutdown by using the Google Cloud console, gcloud CLI, or REST API

After Compute Engine stops or deletes a compute instance and a graceful shutdown starts, you can view the details of the compute instance to monitor when the graceful shutdown starts and completes.

To monitor an ongoing graceful shutdown in a compute instance by using the Google Cloud console, gcloud CLI, or REST API, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of your compute instance. The details page of the compute instance opens on the **Details** tab.

  3. If a graceful shutdown is in progress, check the following fields in the **Basic information** section:

     * **Status** : Shows the [state of your compute instance](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle#instance-states). During a graceful shutdown, this displays **Pending stop** with a countdown timer indicating when the graceful shutdown ends.

     * **Target state** : Shows whether Compute Engine is stopping (**Stopped**) or deleting (**Deleted**) the compute instance.




###  gcloud 

To monitor an ongoing graceful shutdown in a compute instance, use the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
    
    
    gcloud compute instances describe INSTANCE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance.

  * `ZONE`: the zone where the compute instance exists.




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

  * `MAX_DURATION`: the maximum duration of the graceful shutdown, in seconds. When `STOP_STATE` changes to `STOPPING`, Compute Engine deletes the `maxDuration` field.

  * `REQUEST_TIMESTAMP`: the timestamp indicating when the `STOP_STATE` started.

  * `STOP_STATE`: the stopping phase of the compute instance. The value can be one of the following:

    * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The compute instance remains in this state until you manually end the graceful shutdown or the timer expires.

    * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

  * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the compute instance.




When Compute Engine finishes stopping the compute instance, Compute Engine changes the state of the compute instance to `TERMINATE` and deletes the `shutdownDetails` field.

###  REST 

To monitor an ongoing graceful shutdown in a compute instance, make a `GET` request to the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you created the compute instance.

  * `ZONE`: the zone where the compute instance exists.

  * `INSTANCE_NAME`: the name of the compute instance.




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

  * `MAX_DURATION`: the maximum duration of the graceful shutdown, in seconds. When `STOP_STATE` changes to `STOPPING`, Compute Engine deletes the `maxDuration` field.

  * `REQUEST_TIMESTAMP`: the timestamp indicating when the `STOP_STATE` started.

  * `STOP_STATE`: the stopping phase of the compute instance. The value can be one of the following:

    * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The compute instance remains in this state until you manually end the graceful shutdown or the timer expires.

    * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

  * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the compute instance.




When Compute Engine finishes stopping the compute instance, Compute Engine changes the state of the compute instance to `TERMINATE` and deletes the `shutdownDetails` field.

### Monitor graceful shutdown by querying metadata server

To monitor an ongoing graceful shutdown by querying the metadata server, use one of the following options. For more information about viewing and querying the metadata for a compute instance, see [View and query VM metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata).

###  Linux 

  1. Connect to your Linux compute instance.

  2. To query the `shutdown-details` metadata key, run the following command by using the [`curl` tool](https://curl.se/):
         
         user@myinst:~$ curl -s -H "Metadata-Flavor: Google" http://metadata.google.internal/computeMetadata/v1/instance/shutdown-details
         

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

     * `STOP_STATE`: the stopping phase of the compute instance. The value can be one of the following:

       * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The compute instance remains in this state until you manually end the graceful shutdown or the timer expires.

       * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

     * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the compute instance.




###  Windows 

  1. Connect to your Windows compute instance.

  2. To query the `shutdown-details` metadata key, use the [`Invoke-RestMethod` cmdlet](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-restmethod):
         
         PS C:\> 
         $value = (Invoke-RestMethod `
                 -Headers @{'Metadata-Flavor' = 'Google'} `
                 -Uri "http://metadata.google.internal/computeMetadata/v1/instance/shutdown-details")
         $value
         

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

     * `STOP_STATE`: the stopping phase of the compute instance. The value can be one of the following:

       * **`PENDING_STOP`** : Compute Engine has started the graceful shutdown. The compute instance remains in this state until you manually end the graceful shutdown or the timer expires.

       * **`STOPPING`** : the graceful shutdown has ended, and Compute Engine continues with the stop or delete operation.

     * `TARGET_STATE`: whether Compute Engine is stopping (`STOPPED`) or deleting (`DELETED`) the compute instance.




### Monitor graceful shutdown by viewing audit logs

After Compute Engine stops or deletes a compute instance and a graceful shutdown starts, Compute Engine creates Cloud Audit Logs to track the graceful shutdown. You can review these logs to track when a graceful shutdown starts and completes.

To monitor a graceful shutdown by using Cloud Audit Logs logs, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the query pane, enter the following query:
         
         resource.type="gce_instance"
         protoPayload.serviceName="compute.googleapis.com"
         protoPayload.methodName:"compute.instances.gracefulShutdown"
         

  3. Click **Run query**.




###  gcloud 

To view Cloud Audit Logs logs after a graceful shutdown starts, use one of the following [`gcloud logging read` commands](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read):

  * To monitor graceful shutdown for all your compute instances that are gracefully shutting down, run the following command:
        
        gcloud logging read 'resource.type="gce_instance" AND protoPayload.serviceName="compute.googleapis.com" AND protoPayload.methodName:"compute.instances.gracefulShutdown"'
        

  * To monitor graceful shutdown for a single compute instance, run the following command:
        
        gcloud logging read 'resource.type="gce_instance" AND protoPayload.serviceName="compute.googleapis.com" AND protoPayload.methodName:"compute.instances.gracefulShutdown" AND "INSTANCE_NAME"'
        

Replace `INSTANCE_NAME` with the name of the compute instance.




The output is similar to the following:
    
    
    insertId: -gvb9n5drmdg
    labels:
      compute.googleapis.com/root_trigger_id: e23093bc-2c55-4ee4-b7cf-ea8b295f0d9a
    logName: projects/example-project/logs/cloudaudit.googleapis.com%2Fsystem_event
    operation:
      id: gracefulShutdown-1783417965660-656025a544aa5-0eefacb0-38dc7152
      last: true
      producer: compute.instances.gracefulShutdown
    protoPayload:
      '@type': type.googleapis.com/google.cloud.audit.AuditLog
      authenticationInfo:
        principalEmail: system@google.com
      methodName: compute.instances.gracefulShutdown
      request:
        '@type': type.googleapis.com/compute.instances.gracefulShutdown
      resourceName: projects/example-project/zones/us-central1-a/instances/vm-01
      serviceName: compute.googleapis.com
      status:
        message: Instance graceful shutdown completed.
    receiveTimestamp: '2026-07-07T10:04:06.109088155Z'
    resource:
      labels:
        instance_id: '4210316577417032387'
        project_id: example-project
        zone: us-central1-a
      type: gce_instance
    severity: INFO
    timestamp: '2026-07-07T10:04:05.846992Z'
    

###  REST 

To view Cloud Audit Logs logs after a graceful shutdown starts, make a `POST` request to the [`entries.list` method](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list):
    
    
    POST https://logging.googleapis.com/v2/entries:list
    
    {
      "resourceNames": [
        "projects/PROJECT_ID"
      ],
      "filter": "resource.type=\"gce_instance\" AND protoPayload.serviceName=\"compute.googleapis.com\" AND protoPayload.methodName:\"compute.instances.gracefulShutdown\""
    }
    

Replace `PROJECT_ID` with the ID of the project in which your compute instance exists.

The output is similar to the following:
    
    
    {
      "insertId": "-gvb9n5drmdg",
      "labels": {
        "compute.googleapis.com/root_trigger_id": "e23093bc-2c55-4ee4-b7cf-ea8b295f0d9a"
      },
      "logName": "projects/example-project/logs/cloudaudit.googleapis.com%2Fsystem_event",
      "operation": {
        "id": "gracefulShutdown-1783417965660-656025a544aa5-0eefacb0-38dc7152",
        "last": true,
        "producer": "compute.instances.gracefulShutdown"
      },
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {
          "principalEmail": "system@google.com"
        },
        "methodName": "compute.instances.gracefulShutdown",
        "request": {
          "@type": "type.googleapis.com/compute.instances.gracefulShutdown"
        },
        "resourceName": "projects/example-project/zones/us-central1-a/instances/vm-01",
        "serviceName": "compute.googleapis.com",
        "status": {
          "message": "Instance graceful shutdown completed."
        }
      },
      "receiveTimestamp": "2026-07-07T10:04:06.109088155Z",
      "resource": {
        "labels": {
          "instance_id": "4210316577417032387",
          "project_id": "example-project",
          "zone": "us-central1-a"
        },
        "type": "gce_instance"
      },
      "severity": "INFO",
      "timestamp": "2026-07-07T10:04:05.846992Z"
    }
    

For more information, see [Viewing audit logs](https://docs.cloud.google.com/logging/docs/audit#view-logs).

### Monitor graceful shutdown by viewing Compute Engine operations

After Compute Engine stops or deletes a compute instance and a graceful shutdown starts, you can view the running stop or delete operations to monitor the graceful shutdown.

To monitor a graceful shutdown by view Compute Engine operations, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Operations** page.

[Go to Operations](https://console.cloud.google.com/compute/operations)

  2. Optional: To refine your list of operations to only show the ongoing graceful shutdowns in a specific region or zone, in the filter_list **Filter** field, enter one of the following filters:

     * To view all operations across a region, use the following filter:
           
           Target:https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION
           

     * To view all operations in a single zone, use the following filter:
           
           Target:https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE
           

Replace the following:

     * `PROJECT_ID`: the ID of the project in which your compute instances exist.

     * `REGION`: the region in which your compute instances exist.

     * `ZONE`: the zone in which your compute instances exist.

  3. To view the details of a specific operation, in the **Operation summary** column, click the summary of the operation. A page that gives the details of the operation opens.




###  gcloud 

To view all ongoing or completed graceful shutdowns among the compute instances in your project, use the following [`gcloud compute operations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list):
    
    
    gcloud compute operations list \
        --filter="operationType=compute.instances.gracefulShutdown"
    

The output is similar to the following:
    
    
    NAME: operation-1782409401831-65517873d8fe0-76bb4c47-978a64be
    TYPE: compute.instances.gracefulShutdown
    TARGET: vm-01
    HTTP_STATUS: 200
    STATUS: RUNNING
    TIMESTAMP: 2026-07-07T10:04:05.846992Z
    
    NAME: operation-1783420590456-656035b8e9fa0-84dc2a39-1b9c83fe
    TYPE: compute.instances.gracefulShutdown
    TARGET: vm-02
    HTTP_STATUS: 200
    STATUS: RUNNING
    TIMESTAMP: 2026-07-07T10:04:05.846992Z
    

If you want to see the ongoing graceful shutdowns across specific regions or zones, then use the same command with the [`--regions`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list#--regions) or [`--zones` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/operations/list#--zones).

###  REST 

To view all ongoing or completed graceful shutdowns among the compute instances in your project, make one of the following requests:

  * To view all ongoing or completed graceful shutdowns across all regions and zones, make a `GET` request to the [`globalOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations/list):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/operations?filter=operationType=compute.instances.gracefulShutdown
        

  * To view all ongoing or completed graceful shutdowns across a region, make a `GET` request to the [`regionOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations/list):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/operations?filter=operationType=compute.instances.gracefulShutdown
        

  * To view all ongoing or completed graceful shutdowns in a single zone, make a `GET` request to the [`zoneOperations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/list):
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/operations?filter=operationType=compute.instances.gracefulShutdown
        




Replace the following:

  * `PROJECT_ID`: the ID of the project in which your compute instances exist.

  * `REGION`: the region in which your compute instances exist.

  * `ZONE`: the zone in which your compute instances exist.




The output is similar to the following:
    
    
    {
      "kind": "compute#operationList",
      "id": "projects/example-project/zones/us-central1-a/operations",
      "items": [
        {
          "kind": "compute#operation",
          "id": "4210316577417032387",
          "name": "operation-1782409401831-65517873d8fe0-76bb4c47-978a64be",
          "operationType": "compute.instances.gracefulShutdown",
          "targetLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/vm-01",
          "status": "RUNNING",
          "user": "system@google.com",
          "progress": 0,
          "insertTime": "2026-07-07T10:04:05.846992Z",
          "startTime": "2026-07-07T10:04:05.846992Z",
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/operations/operation-1782409401831-65517873d8fe0-76bb4c47-978a64be"
        },
        ...
      ]
    }
    

For more information, see [View Compute Engine operations](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations).

## What's next

  * [Disable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
