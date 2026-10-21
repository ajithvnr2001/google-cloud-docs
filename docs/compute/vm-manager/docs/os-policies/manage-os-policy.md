---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy/
title: Manage OS policy assignments \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:48:19.182986+00:00
---

# Manage OS policy assignments  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Manage OS policy assignments Stay organized with collections  Save and categorize content based on your preferences. 

After you [create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment), review and manage your assignments using the following procedures:

  * Update OS policy assignments: modify the configurations for your OS policy assignment
  * Describe OS policy assignments: get details about a specific OS policy assignment
  * List OS policy assignments: view a list of OS policy assignments in a specific zone
  * List OS policy assignment revisions: view a list of revisions that are available for a specific OS policy assignment
  * Delete an OS policy assignment: delete a specific OS policy assignment
  * Debug an OS policy assignment: troubleshoot an OS policy assignment



You can manage your OS policy assignments using either the [Google Cloud console](https://console.cloud.google.com/), the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or the [OS Config API](https://docs.cloud.google.com/compute/docs/osconfig/rest).

## Before you begin

  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
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




## Permissions

Owners of a project have full access to manage OS policy assignments. For all other users, you need to grant permissions. To manage OS policy assignments, you can grant one of the following granular roles:

  * OSPolicyAssignment Admin (`roles/osconfig.osPolicyAssignmentAdmin`). Contains permissions to create, delete, update, get and list OS policy assignments.
  * OSPolicyAssignment Editor (`roles/osconfig.osPolicyAssignmentEditor`). Contains permissions to update, get, and list OS policy assignments.
  * OSPolicyAssignment Viewer (`roles/osconfig.osPolicyAssignmentViewer`). Contains permissions for read-only access to get and list OS policy assignments.



#### Example command to set permissions

To grant a user admin access to OS policy assignments, run the following command:
    
    
        gcloud projects add-iam-policy-binding PROJECT_ID \
            --member user:USER_ID@gmail.com \
            --role roles/osconfig.osPolicyAssignmentAdmin
    

Replace the following:

  * `PROJECT_ID`: the project ID
  * `USER_ID`: the user's Google Workspace username



## Update OS policy assignments

To update an OS policy assignment, complete the following steps:

  1. Update the YAML or JSON file that has the OS policy assignment.

The update request supports field masks. You might need to update only certain fields in the OS policy assignment while leaving the other fields unchanged. The update or patch command uses field masks to tell the API which fields are changed. The update or patch request ignores any fields that aren't specified in the field mask, leaving them with their current values. For more information about field masks, see [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask).

  2. Update the OS policy assignment using either the Google Cloud console, Google Cloud CLI, or the OS Config API.

When you update an OS policy assignment, a rollout is created. You can view the progress of the update by monitoring the rollout. For more information, see [Getting details for a rollout](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment#viewing-rollouts).

###  Console 

     1. In the Google Cloud console, go to the **OS policies > Assignments** page.

[Go to Google Cloud console](https://console.cloud.google.com/compute/config/assignments/)

     2. For the OS policy assignment that you want to edit, click **Action ( more_vert) > Edit Assignment**.

     3. Make the needed updates. For example, you can upload the updated OS policy file.

     4. Click **Start rollout**.

###  gcloud 

Use the [`os-config os-policy-assignments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/update) to update an OS policy assignment.
    
    gcloud compute os-config os-policy-assignments update OS_POLICY_ASSIGNMENT_ID \
        --location=ZONE \
        --file=FILE
    

Replace the following:

     * `OS_POLICY_ASSIGNMENT_ID`: the name of the OS policy assignment that you want to update
     * `ZONE`: the zone where the OS policy assignment is located
     * `FILE`: the absolute path to the JSON or YAML file that contains the updated OS policy assignment specifications

If the OS policy assignment doesn't exist, and if you specify the `--allow-missing` flag, VM Manager creates the OS policy assignment with the specified ID and specifications.

###  REST 

In the API, create a `PATCH` request to the [`projects.locations.osPolicyAssignments.patch` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/patch).
    
    PATCH https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments/OS_POLICY_ASSIGNMENT_ID
    
    {
     JSON_OS_POLICY
    }
    

Replace the following:

     * `PROJECT_ID`: your project ID
     * `OS_POLICY_ASSIGNMENT_ID`: name of the OS policy assignment that you want to update
     * `JSON_OS_POLICY`: the OS policy assignment specifications created in the previous step. This must be in JSON format. For more information about the parameters and format, see [`Resource: OSPolicyAssignment`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#OSPolicyAssignment).
     * `ZONE`: the zone where the OS policy assignment is located




## List OS policy assignments

###  Console 

  1. In the Google Cloud console, go to the **OS policies > Assignments** page.

[Go to Google Cloud console](https://console.cloud.google.com/compute/config/assignments/)




###  gcloud 

To view a list of OS policy assignments in a specific zone, use the [`os-config os-policy-assignments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/list).
    
    
     gcloud compute os-config os-policy-assignments list \
         --location=ZONE
    

Replace `ZONE` with the zone where the OS policy assignments are located.

###  REST 

In the API, create a `GET` request to the [`projects.locations.osPolicyAssignments.list` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/list).
    
    
    GET https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone where the OS policy assignments are located



## Describe an OS policy assignment

###  Console 

  1. In the Google Cloud console, go to the **OS policies > Assignments** page.

[Go to Google Cloud console](https://console.cloud.google.com/compute/config/assignments/)

  2. Click the name of the assignment that you want to view details for.




###  gcloud 

To view details about an OS policy assignment, use the [`compute os-config os-policy-assignments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/describe).
    
    
    gcloud compute os-config os-policy-assignments describe OS_POLICY_ASSIGNMENT_ID \
         --location=ZONE
    

Replace the following:

  * `OS_POLICY_ASSIGNMENT_ID`: the name of the OS policy assignment that you want to view
  * `ZONE`: the zone where the OS policy assignment is located



###  REST 

In the API, create a `GET` request to the [`projects.locations.osPolicyAssignments.get` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/get).
    
    
    GET https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments/OS_POLICY_ASSIGNMENT_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `OS_POLICY_ASSIGNMENT_ID`: name of the OS policy assignment that you want to view
  * `ZONE`: the zone where the OS policy assignment is located



## List OS policy assignment revisions

###  gcloud 

A revision ID is generated when you create an OS policy assignment. A new revision ID is also generated each time you update or delete the OS policy assignment.

To view a list of revisions that are available for an OS policy assignment, use the [`os-config os-policy-assignments list-revisions` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/list-revisions).
    
    
    gcloud compute os-config os-policy-assignments list-revisions OS_POLICY_ASSIGNMENT_ID \
        --location=ZONE
    

Replace the following:

  * `OS_POLICY_ASSIGNMENT_ID`: the name of the OS policy assignment whose revisions you want to view
  * `ZONE`: the zone where the OS policy assignment is located



###  REST 

In the API, create a `GET` request to the [`projects.locations.osPolicyAssignments.listRevisions` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/listRevisions).
    
    
    GET https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments/OS_POLICY_ASSIGNMENT_ID:listRevisions
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `OS_POLICY_ASSIGNMENT_ID`: the name of the OS policy assignment whose revisions you want to view
  * `ZONE`: the zone where the OS policy assignment is located



## Delete OS policy assignments

When you delete an OS policy assignment, a rollout is created. You can view the progress of the deletion by monitoring the rollout. For more information, see [Getting details for a rollout](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment#viewing-rollouts).

###  Console 

  1. In the Google Cloud console, go to the **OS policies > Assignments** page.

[Go to Google Cloud console](https://console.cloud.google.com/compute/config/assignments/)

  2. For the OS policy assignment that you want to delete, click **Action ( more_vert) > Delete Assignment**.

  3. Click **Delete**.




###  gcloud 

To delete an OS policy assignment, use the [`os-config os-policy-assignments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/os-config/os-policy-assignments/delete).
    
    
    gcloud compute os-config os-policy-assignments delete OS_POLICY_ASSIGNMENT_ID \
        --location=ZONE
    

Replace the following:

  * `OS_POLICY_ASSIGNMENT_ID`: the name of the OS policy assignment that you want to delete
  * `ZONE`: the zone where the OS policy assignment is located



###  REST 

In the API, create a `DELETE` request to the [`projects.locations.osPolicyAssignments.delete` method](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/delete).
    
    
    DELETE https://osconfig.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/osPolicyAssignments/OS_POLICY_ASSIGNMENT_ID
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `OS_POLICY_ASSIGNMENT_ID`: name of the OS policy assignment that you want to delete
  * `ZONE`: the zone where the OS policy assignment is located



## Troubleshooting

To troubleshoot an OS policy assignment, see [Troubleshooting VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager).

## What's next?

  * Learn more about the [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies).
  * [Create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
