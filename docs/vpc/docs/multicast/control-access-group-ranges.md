---
url: https://docs.cloud.google.com/vpc/docs/multicast/control-access-group-ranges/
title: Control access to multicast group ranges \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:45.533997+00:00
---

# Control access to multicast group ranges  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/control-access-group-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control access to multicast group ranges

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to control access to multicast group ranges.

The configuration described on this page determines whether a multicast consumer project can [Activate a multicast consumer VPC network for a group range](https://docs.cloud.google.com/vpc/docs/multicast/enable-consumer-network#activate-consumer).

## Overview

You can update which multicast consumer projects can access a multicast group range as follows:

  * Update the group range to allow all projects.
  * Update the group range to deny all projects by default. You can optionally provide a list of specific projects to allow during this procedure.
  * Configure the multicast consumer accept list: For group ranges that already deny all projects by default, you can specify projects to allow.



### About revoking and restoring access to group ranges

Consider the following before updating access to a multicast group range:

  * If your update revokes access for an existing multicast consumer project that has a multicast group consumer activation, then Google Cloud deactivates the multicast group consumer activation, but the resource still exists in the multicast consumer project with a status of `INACTIVE`.
  * If you grant access to a multicast consumer project for which you previously revoked access, then the multicast consumer network administrator must delete their existing group consumer activation and create a new one. Existing `INACTIVE` resources can't be reused.



## Update the group range to allow all projects

This section describes how to update a multicast group range to allow all projects.

After completing this procedure, any project that has access to the domain can use this group range.

###  gcloud 

To update a multicast group range to allow all projects, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update) and specify the following flags:

  * `--no-require-explicit-accept`
  * If the multicast consumer accept list is not empty, then you must also specify the `--clear-consumer-accept-list` flag.


    
    
      gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
          --location=global \
          --no-require-explicit-accept \
          --clear-consumer-accept-list
    

Replace `GROUP_RANGE_NAME` with the name of the multicast group range.

###  API 

To update a multicast group range to allow all projects, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).

Set the `requireExplicitAccept` field to `false`. If the consumer accept list is not empty, then you must also clear the `consumerAcceptList` field by setting its value to `[]`.
    
    
      PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=requireExplicitAccept,consumerAcceptList
      {
        "requireExplicitAccept": "false",
        "consumerAcceptList": []
      }
    

Replace the following values:

  * `PROJECT_ID`: the ID of the multicast administrator project
  * `GROUP_RANGE_NAME`: the name of the multicast group range



## Update the group range to deny all projects by default

This section describes how to update a multicast group range to deny all projects by default.

In the following procedure, you can optionally provide a list of specific projects that can access the multicast group range. Alternatively, you can specify projects to allow later as described in Configure the multicast consumer accept list.

###  gcloud 

To update a multicast group range to deny all projects by default, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update).
    
    
      gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
          --location=global \
          --require-explicit-accept \
          [--consumer-accept-list=LIST_OF_CONSUMERS]
    

Replace the following values:

  * `GROUP_RANGE_NAME`: the name of the multicast group range.
  * `LIST_OF_CONSUMERS`: a list of consumer projects that can use this multicast group range. You can specify up to 100 projects by their ID or name.

If an existing multicast consumer project is using the multicast group range and you want them to continue to have access, then specify the project in the list. Otherwise, Google Cloud deactivates all existing multicast group consumer activations for the group range. If a project is then added back to the consumer accept list later, the multicast consumer network administrator must create new group consumer activations.

You can optionally omit this flag and specify projects to allow later as described in Configure the consumer accept list.




###  API 

To update a multicast group range to deny all projects by default, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).

Set the `requireExplicitAccept` field to `true`. You can optionally set the `consumerAcceptList` field.
    
    
      PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=requireExplicitAccept,consumerAcceptList
      {
        "requireExplicitAccept": "true",
        "consumerAcceptList": [LIST_OF_CONSUMERS]
      }
    

Replace the following values:

  * `PROJECT_ID`: the ID of the multicast administrator project
  * `GROUP_RANGE_NAME`: the name of the multicast group range
  * `LIST_OF_CONSUMERS`: a list of consumer projects that can use this multicast group range. Use the following format: `"project-1", "project-2"`. You can specify up to 100 projects by their ID or name.

If an existing multicast consumer project is using the multicast group range and you want them to continue to have access, then specify the project in the list. Otherwise, Google Cloud deactivates all existing multicast group consumer activations for the group range. If a project is then added back to the consumer accept list later, the multicast consumer network administrator must create new group consumer activations.

You can optionally omit `consumerAcceptList` from the request body and the update mask, and specify projects to allow later as described in Configure the consumer accept list.




## Configure the multicast consumer accept list

This section describes how to configure the multicast consumer accept list for a multicast group range.

If the multicast group range denies all projects by default, then you can configure the consumer accept list as follows:

  * Set a new accept list
  * Add a project to the accept list
  * Remove a project from the accept list
  * Clear the accept list



### Set a new accept list

This section describes how to set a new multicast consumer accept list for a multicast group range.

Follow the steps in this section if you are configuring the multicast consumer accept list for the first time or if you want to replace the existing consumer accept list. If you want to keep the existing list and add or remove a multicast consumer project, see Add a project to the accept list or Remove a project from the accept list.

###  gcloud 

To set the accept list for a multicast group range, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update).
    
    
      gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
          --location=global \
          --consumer-accept-list=LIST_OF_CONSUMERS
    

Replace the following values:

  * `GROUP_RANGE_NAME`: the name of the multicast group range
  * `LIST_OF_CONSUMERS`: one or more consumer projects that can use this multicast group range. You can specify up to 100 projects by their ID or name.



###  API 

To set the accept list for a multicast group range, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).
    
    
      PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=consumerAcceptList
      {
        "consumerAcceptList": [LIST_OF_CONSUMERS]
      }
    

Replace the following values:

  * `PROJECT_ID`: the ID of the multicast administrator project
  * `GROUP_RANGE_NAME`: the name of the multicast group range
  * `LIST_OF_CONSUMERS`: one or more consumer projects that can use this multicast group range. Use the following format: `"project-1", "project-2"`. You can specify up to 100 projects by their ID or name.



### Add a project to the accept list

This section describes how to add a multicast consumer project to the accept list for a multicast group range.

###  gcloud 

To add a multicast consumer project to the accept list, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update).
    
    
      gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
          --location=global \
          --add-consumer-accept-list=LIST_OF_CONSUMERS
    

Replace the following values:

  * `GROUP_RANGE_NAME`: the name of the multicast group range
  * `LIST_OF_CONSUMERS`: one or more multicast consumer projects to add to the accept list so that they can use this multicast group range.



###  API 

To add a multicast consumer project to the accept list, get the current accept list and then make an API request to update the list:

  1. To get the current accept list for the group range, follow the instructions in [View multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-group-ranges). Copy the accept list so that you can use it in the next step.

  2. To update the accept list, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).
         
         PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=consumerAcceptList
         {
           "consumerAcceptList": [UPDATED_LIST_OF_CONSUMERS]
         }
         

Replace the following values:

     * `PROJECT_ID`: the ID of the multicast administrator project
     * `GROUP_RANGE_NAME`: the name of the multicast group range
     * `UPDATED_LIST_OF_CONSUMERS`: the updated list of projects that includes the existing projects to keep and any new projects to add. Use the following format: `"project-1", "project-2"`. The API replaces the entire consumer accept list with list that you provide.



### Remove a project from the accept list

This section describes how to remove a multicast consumer project from the accept list for a multicast group range.

###  gcloud 

To remove a multicast consumer project from the accept list, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update).
    
    
      gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
          --location=global \
          --remove-consumer-accept-list=LIST_OF_CONSUMERS
    

Replace the following values:

  * `GROUP_RANGE_NAME`: the name of the multicast group range
  * `LIST_OF_CONSUMERS`: one or more multicast consumer projects to remove from the consumer accept list so that they can't use this multicast group range.



###  API 

To remove a multicast consumer project from the accept list, get the current accept list and then make an API request to update the list:

  1. To get the current accept list for the group range, follow the instructions in [View multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-group-ranges). Copy the accept list so that you can use it in the next step.

  2. To update the accept list, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).
         
         PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=consumerAcceptList
         {
           "consumerAcceptList": [UPDATED_LIST_OF_CONSUMERS]
         }
         

Replace the following values:

     * `PROJECT_ID`: the ID of the multicast administrator project
     * `GROUP_RANGE_NAME`: the name of the multicast group range
     * `UPDATED_LIST_OF_CONSUMERS`: the updated list of projects that includes the existing projects to keep and excludes any projects that you want to remove. Use the following format: `"project-1", "project-2"`. The API replaces the entire consumer accept list with the list that you provide.



### Clear the accept list

This section describes how to clear the accept list for a multicast group range.

###  gcloud 

To clear the consumer accept list for a multicast group range, use the [`network-services multicast-group-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/update).
    
    
      gcloud network-services multicast-group-ranges update GROUP_RANGE_NAME \
          --location=global \
          --clear-consumer-accept-list
    

Replace `GROUP_RANGE_NAME` with the name of the multicast group range.

###  API 

To clear the consumer accept list for a multicast group range, use the [`multicastGroupRanges.patch` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/patch).
    
    
      PATCH https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME?updateMask=consumerAcceptList
      {
        "consumerAcceptList": []
      }
    

Replace the following values:

  * `PROJECT_ID`: the ID of the multicast administrator project
  * `GROUP_RANGE_NAME`: the name of the multicast group range



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
