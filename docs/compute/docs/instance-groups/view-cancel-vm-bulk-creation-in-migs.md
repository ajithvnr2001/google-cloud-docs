---
url: https://docs.cloud.google.com/compute/docs/instance-groups/view-cancel-vm-bulk-creation-in-migs/
title: View or cancel bulk creation of instances in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:37:26.412437+00:00
---

# View or cancel bulk creation of instances in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/view-cancel-vm-bulk-creation-in-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View or cancel bulk creation of instances in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to view the status of bulk creation of virtual machine (VM) instances in a managed instance group (MIG). It also explains how to cancel a bulk creation that is in progress.

To learn how bulk creation of instances works in a MIG, see [About bulk creation of instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode)

## View the status of bulk creation of instances

You can view the status of a bulk creation operation in a MIG. The status lets you check if the bulk creation is still in progress and, if the instances are not yet created, understand the reasons why.

The MIG details contain the following fields to help you monitor the bulk creation status:

  * `status.bulkInstanceOperation.inProgress`: this field indicates whether a bulk creation of instances is in progress (`true`) or not (`false`).

  * `lastProgressCheck`: this field provides details on why instances might not yet be created. The possible reasons are as follows:

    * Lack of capacity: when the MIG is waiting for the requested capacity to become available, you'll see the `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error code.

    * Insufficient quota: when there is insufficient quota to fulfill your request, you'll see the `QUOTA_EXCEEDED` error. To increase your project's quota, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).




###  gcloud 

To view the status of bulk creation of instances in a MIG, use the [`gcloud compute instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).

  * For a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
            --zone=ZONE
        

  * For a regional MIG, run the following command:
        
        gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
            --region=REGION
        

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.

  * `ZONE`: the zone where the MIG exists.

  * `REGION`: the region where the MIG exists.




The following example shows a response for a MIG in which a bulk creation is in progress and the `lastProgressCheck` field indicates that the bulk creation is waiting for resources due to a `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error and also has a `QUOTA_EXCEEDED` error.
    
    
    {
      "status": {
        "bulkInstanceOperation": {
          "inProgress": true,
          "lastProgressCheck": {
            "timestamp": "2024-01-01T12:00:00.712-08:00",
            "errors": [
              {
                "code": "ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS",
                "message": "Waiting for resources. Currently there are not enough resources available to fulfill the request."
              },
              {
                "code": "QUOTA_EXCEEDED",
                "message": "Quota 'NVIDIA_A100_GPUS' exceeded. Limit: 1500 in region us-central1."
              }
            ]
          }
        }
      }
    }
    

###  REST 

To view the status of bulk creation of instances in a MIG, make a `GET` request as follows:

  * For a zonal MIG, use the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME
        

  * For a regional MIG, use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
        




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone where the MIG exists.
  * `REGION`: the region where the MIG exists.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.



The following example shows a response for a MIG in which a bulk creation is in progress and the `lastProgressCheck` field indicates that the bulk creation is waiting for resources due to a `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error and also has a `QUOTA_EXCEEDED` error.
    
    
    {
      "status": {
        "bulkInstanceOperation": {
          "inProgress": true,
          "lastProgressCheck": {
            "timestamp": "2024-01-01T12:00:00.712-08:00",
            "errors": [
              {
                "code": "ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS",
                "message": "Waiting for resources. Currently there are not enough resources available to fulfill the request."
              },
              {
                "code": "QUOTA_EXCEEDED",
                "message": "Quota 'NVIDIA_A100_GPUS' exceeded. Limit: 1500 in region us-central1."
              }
            ]
          }
        }
      }
    }
    

## View the status of managed instances

You can monitor the status of individual managed instances by checking their current action and instance status.

  * While the bulk instance operation is in progress, managed instances display the following statuses:

    * `currentAction: CREATING`
    * `instanceStatus: PENDING`
  * After the bulk instance operation completes successfully, the managed instances' statuses change to the following:

    * `currentAction: NONE`
    * `instanceStatus: RUNNING`



To view this information about managed instances, see [Check the status of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

## Cancel bulk creation operation

To cancel a bulk creation operation, either resize the MIG to zero or delete the MIG.

### Resize the MIG to zero

###  Console 

  1. Go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG in which you want to resize.

  3. Click **Edit**.

  4. Click **Group size & autoscaling** to expand the section.

  5. Set the **Number of instances** to `0`.

  6. Click **Save**.




### gcloud

To resize a MIG to zero, use the [`gcloud compute instance-groups managed resize` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize) and set the `--size` flag to `0`.

  * For a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed resize INSTANCE_GROUP_NAME \
            --size=0 \
            --zone=ZONE
        

  * For a regional MIG, run the following command:
        
        gcloud compute instance-groups managed resize INSTANCE_GROUP_NAME \
            --size=0 \
            --region=REGION
        




Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `ZONE`: the zone where the MIG exists.
  * `REGION`: the region where the MIG exists.



  * REST

To resize a MIG to zero, make a `PATCH` request using one of the following methods. In the request body, set the `targetSize` to `0`.

    * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
          
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME
          
          {
            "targetSize": 0
          }
          

    * For a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
          
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
          
          {
            "targetSize": 0
          }
          

Replace the following:

    * `PROJECT_ID`: the project ID.
    * `ZONE`: the zone where the MIG exists.
    * `REGION`: the region where the MIG exists.
    * `INSTANCE_GROUP_NAME`: the name of the MIG.



### Delete a MIG

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the checkbox of the MIG that you want to delete.

  3. Click **Delete** to delete the MIG and all the instances in it.




###  gcloud 

To delete a MIG, use the [`delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete).

  * For a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed delete INSTANCE_GROUP_NAME \
            --zone ZONE
        

  * For a regional MIG, run the following command:
        
        gcloud compute instance-groups managed delete INSTANCE_GROUP_NAME \
            --region REGION
        




Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `ZONE`: the zone where the MIG exists.
  * `REGION`: the region where the MIG exists.



###  REST 

To delete a MIG, make a `PATCH` request using one of the following methods:

  * For a zonal MIG, use the [`instanceGroupManagers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/delete).
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME
        

  * For a regional MIG, use the [`regionInstanceGroupManagers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/delete)
        
        DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
        




Replace the following:

  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone where the MIG exists.
  * `REGION`: the region where the MIG exists.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.



## What's next

  * Learn how to [view information about the managed instances within a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
