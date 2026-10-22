---
url: https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig/
title: View, cancel, or delete resize requests in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:53.938516+00:00
---

# View, cancel, or delete resize requests in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View, cancel, or delete resize requests in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to do the following after you [create a resize request](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig) in a managed instance group (MIG):

  * View resize requests to monitor their states or troubleshoot them.

  * Cancel resize requests to stop the MIG from creating the requested number of virtual machine (VM) instances.

  * Delete resize requests when you no longer need them.




## Before you begin

  * If you haven't already, then see [ how resize requests work](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig#how-resize-requests-work).
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

To get the permissions that you need to view, cancel, or delete resize requests in a MIG, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view, cancel, or delete resize requests in a MIG. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view, cancel, or delete resize requests in a MIG:

  * To cancel or delete resize requests in a MIG: `compute.instanceGroupManagers.update`
  * To view a list of resize requests in a MIG: `compute.instanceGroupManagers.list`
  * To view the details of a resize request: `compute.instanceGroupManagers.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View your resize requests

To view information about the resize requests in a MIG, use one of the following methods:

  * For an overview of all requests in a MIG, view a list of resize requests in a MIG.

  * For the full details of a specific request, view the details of a resize request.




### View a list of resize requests in a MIG

To view a list of all resize requests in a MIG, select one of the following options:

To view a list of all resize requests in a regional MIG, use the gcloud CLI or REST API. Otherwise, to view a list of all resize requests in a zonal MIG, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. In the **Name** column, click the name of the MIG that contains resize requests.

The overview page of the MIG opens.

  3. In the **Resize requests** row, click edit **Edit resize requests**.

The **Resize requests** pane appears. If a resize request's **Details** column shows the **Quota exceeded** or **ETA: indefinite** value, then your request has encountered an error. You can click these values to learn more.

For more information about troubleshooting errors, see View the details of a resize request in this document.




###  gcloud 

To view a list of resize requests in a MIG, use the [`instance-groups managed resize-requests list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/list).

  * In a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests list MIG_NAME \
            --zone=ZONE
        

  * In a regional MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests list MIG_NAME \
            --region=REGION
        




Replace the following:

  * `MIG_NAME`: the name of a MIG with accepted, successful, canceled, or failed resize requests.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.




The output is similar to the following for a zonal MIG:
    
    
    NAME: rr-01
    LOCATION: us-central1-a
    SCOPE: zone
    RESIZE_BY: 5
    STATE: SUCCEEDED
    REQUESTED_RUN_DURATION: P1D
    
    NAME: rr-02
    LOCATION: us-central1-a
    SCOPE: zone
    RESIZE_BY: 10
    STATE: ACCEPTED
    REQUESTED_RUN_DURATION: P3D
    

###  REST 

  * To view a list of resize requests in a zonal MIG, send a `GET` request using the [`instanceGroupManagerResizeRequests.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/list).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
        

  * To view a list of resize requests in a regional MIG, send a `GET` request using the [`regionInstanceGroupManagerResizeRequests.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/list).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/regionInstanceGroupManagers/MIG_NAME/resizeRequests
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where a MIG with accepted, successful, canceled, or failed resize requests is located.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.

  * `MIG_NAME`: the name of an existing MIG with accepted, successful, canceled, or failed resize requests.




The output from a zonal MIG is similar to the following:
    
    
    {
      "kind": "compute#instanceGroupManagerResizeRequestList",
      "id": "projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests",
      "items": [
        {
          "kind": "compute#instanceGroupManagerResizeRequest",
          "id": "4247139565532196982",
          "creationTimestamp": "2024-01-08T07:51:53.034-08:00",
          "name": "rr-01",
          "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
          "count": 5,
          "resizeBy": 5,
          "requestedRunDuration": {
            "seconds": "86400",
            "nanos": 0
          },
          "state": "SUCCEEDED",
          "status": {},
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/rr-01",
          "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/4247139565532196982"
        },
        {
          "kind": "compute#instanceGroupManagerResizeRequest",
          "id": "8095866098849525652",
          "creationTimestamp": "2024-01-11T08:04:11.851-08:00",
          "name": "rr-02",
          "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
          "count": 10,
          "resizeBy": 10,
          "requestedRunDuration": {
            "seconds": "259200",
            "nanos": 0
          },
          "state": "ACCEPTED",
          "status": {},
          "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/rr-02",
          "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/8095866098849525652"
        }
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests"
    }
    

### View the details of a resize request

You can view the details of a resize request to review its configuration and, optionally, troubleshoot it if the request hasn't succeeded yet.

If an accepted resize request isn't succeeding, then you can troubleshoot it by checking the `status.lastAttempt.error.errors.code` field in the request's details. The possible error codes are as follows:

  * **`QUOTA_EXCEEDED`** : your project lacks quota for the requested resources. To increase your project's quota, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

  * **`ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS`** : the requested resources are temporarily unavailable. Compute Engine has scheduled the creation of the requested resources and plans to create them when they become available. If the `message` field contains `Expected time is indefinite`, then Google recommends canceling the request and trying one or more of the following:

    * Create a new resize request with a lower number of requested VMs.

    * Use a different machine type in the MIG, and then create a new resize request. To use a different machine type, [create a new instance template](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig#create-instance-template), and then use that template to [create or update a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig#create-mig).

    * Create a resize request in a MIG located in a different region or zone.




To view the details of a resize request, select one of the following options:

###  gcloud 

To view the details of a resize request in a MIG, use the [`instance-groups managed resize-requests describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/describe).

  * In a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests describe MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --zone=ZONE
        

  * In a regional MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests describe MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --region=REGION
        




Replace the following:

  * `MIG_NAME`: the name of a MIG.

  * `RESIZE_REQUEST_NAME`: the name of a resize request that you want to view the details of.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.




The output is similar to the following for a zonal MIG:
    
    
    creationTimestamp: '2024-09-23T02:27:09.575-07:00'
    id: '6386622402379156098'
    kind: compute#instanceGroupManagerResizeRequest
    name: example-request
    requestedRunDuration:
      nanos: 0
      seconds: '86400'
    resizeBy: 10
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/example-request
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/6386622402379156098
    state: ACCEPTED
    status:
      lastAttempt:
        error:
          errors:
          - code: QUOTA_EXCEEDED
            message: Quota 'NVIDIA_A100_GPUS' exceeded. Limit: 1500 in region us-central1.
          - code: ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS
            message: There are currently not enough resources available to fulfill the request. Expected time is indefinite.
            - errorDetails:
              - errorInfo:
                - metadatas:
                  - estimatedAvailabilityTime: '9999-12-31T23:59:59.999999999Z'
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a
    

###  REST 

  * To view the details of a resize request in a zonal MIG, send a `GET` request using the [`instanceGroupManagerResizeRequests.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests/RESIZE_REQUEST_NAME
        

  * To view the details of a resize request in a regional MIG, send a `GET` request using the [`regionInstanceGroupManagerResizeRequests.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/regionInstanceGroupManagers/MIG_NAME/resizeRequests/RESIZE_REQUEST_NAME
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the zonal MIG is located.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.

  * `MIG_NAME`: the name of a MIG where the resize request is located.

  * `RESIZE_REQUEST_NAME`: the name of an existing resize request that you want to view the details of.




The output is similar to the following:
    
    
    {
      "kind": "compute#instanceGroupManagerResizeRequest",
      "id": "6386622402379156098",
      "creationTimestamp": "2024-09-23T02:27:09.575-07:00",
      "name": "example-request",
      "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
      "resizeBy": 10,
      "requestedRunDuration": {
        "seconds": "86400",
        "nanos": 0
      },
      "state": "SUCCEEDED",
      "status": {
        "lastAttempt": {
          "error": {
            "errors": [
              {
                "code": "QUOTA_EXCEEDED",
                "message": "Quota 'NVIDIA_A100_GPUS' exceeded. Limit: 1500 in region us-central1."
              },
              {
                "code": "ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS",
                "message": "There are currently not enough resources available to fulfill the request. Expected time is indefinite.",
                "errorDetails": [
                  {
                    "errorInfo":{
                      "metadatas":{
                        "estimatedAvailabilityTime": "9999-12-31T23:59:59.999999999Z"
                      }
                    }
                  }
                ]
              }
            ]
          }
        }
      },
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/example-request",
      "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instanceGroupManagers/example-mig/resizeRequests/6386622402379156098"
    }
    

## Cancel resize requests in a MIG

You can cancel resize requests in a MIG to stop the MIG from attempting to create the requested number of VMs. You can cancel accepted (`ACCEPTED`) resize requests only. After canceling a resize request, you can either delete it or let Compute Engine automatically delete it after 14 days.

To cancel multiple resize requests simultaneously, use the Google Cloud console or Google Cloud CLI. Otherwise, to cancel a single resize request, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. In the **Name** column, click the name of the MIG that contains resize requests.

The overview page of the MIG opens.

  3. In the **Resize requests** row, click edit **Edit resize requests**.

The **Resize requests** pane appears.

  4. Select the resize requests to cancel.

  5. Click cancel **Cancel** , and then click **Confirm**.




###  gcloud 

To cancel resize requests in a MIG, use the [`instance-groups managed resize-requests cancel` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/cancel).

  * In a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests cancel MIG_NAME \
            --resize-requests=RESIZE_REQUEST_NAMES \
            --zone=ZONE
        

  * In a regional MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests cancel MIG_NAME \
            --resize-requests=RESIZE_REQUEST_NAMES \
            --region=REGION
        




Replace the following:

  * `MIG_NAME`: the name of a MIG with accepted resize requests.

  * `RESIZE_REQUEST_NAMES`: a comma-separated list of names of accepted resize requests in the specified zonal MIG. For example, specify `request-1,request-2`.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.




###  REST 

  * To cancel a resize request in a zonal MIG, send a `POST` request using the [`instanceGroupManagerResizeRequests.cancel` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/cancel).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests/RESIZE_REQUEST_NAME/cancel
        

  * To cancel a resize request in a regional MIG, send a `POST` request using the [`regionInstanceGroupManagerResizeRequests.cancel` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/cancel).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/regionInstanceGroupManagers/MIG_NAME/resizeRequests/RESIZE_REQUEST_NAME/cancel
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where an existing zonal MIG with an accepted resize request is located.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.

  * `MIG_NAME`: the name of the MIG.

  * `RESIZE_REQUEST_NAME`: the name of the resize request to cancel.




## Delete resize requests in a MIG

By default, Compute Engine automatically deletes a resize request 14 days after setting the request's state to one of the following:

  * Successful (`SUCCEEDED`)

  * Failed (`FAILED`)

  * Canceled (`CANCELLED`)




However, you can immediately delete a resize request before then, as described in this section.

Deleting a successful resize request doesn't delete the VMs created through the request. The MIG automatically deletes those VMs at the end of their requested run duration. However, if your job has finished running and you no longer need the VMs, then [delete the VMs](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

To delete multiple resize requests simultaneously, use the Google Cloud console or gcloud CLI. Otherwise, to delete a single resize request, select any of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. In the **Name** column, click the name of the MIG that contains resize requests.

The overview page of the MIG opens.

  3. In the **Resize requests** row, click edit **Edit resize requests**.

The **Resize requests** pane appears.

  4. Select the resize requests to delete.

  5. Click delete **Delete** , and then click **Confirm**.




###  gcloud 

To delete resize requests in a MIG, use the [`instance-groups managed resize-requests delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/delete).

  * In a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests delete MIG_NAME \
            --resize-requests=RESIZE_REQUEST_NAMES \
            --zone=ZONE
        

  * In a regional MIG, run the following command:
        
        gcloud compute instance-groups managed resize-requests delete MIG_NAME \
            --resize-requests=RESIZE_REQUEST_NAMES \
            --region=REGION
        




Replace the following:

  * `MIG_NAME`: the name of a MIG with successful, failed, or canceled resize requests.

  * `RESIZE_REQUEST_NAMES`: a comma-separated list of names of resize requests to delete in the MIG. For example, specify `request-1,request-2`.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.




###  REST 

  * To delete a resize request in a zonal MIG, send a `DELETE` request using the [`instanceGroupManagerResizeRequests.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/delete).
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests/RESIZE_REQUEST_NAME
        

  * To delete a resize request in a regional MIG, send a `DELETE` request using the [`regionInstanceGroupManagerResizeRequests.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/delete).
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/regionInstanceGroupManagers/MIG_NAME/resizeRequests/RESIZE_REQUEST_NAME
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where an existing zonal MIG with successful, failed, or canceled resize requests is located.

  * `ZONE`: the zone where the MIG is located.

  * `REGION`: the region where the MIG is located.

  * `MIG_NAME`: the name of the MIG.

  * `RESIZE_REQUEST_NAME`: the name of the resize request to delete.




## What's next

  * Learn how to [view information about the managed VMs within a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_info_about_managed_instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
