---
url: https://docs.cloud.google.com/ull-solution/participants/view-consumer-configurations/
title: View multicast consumer configurations \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:13.082488+00:00
---

# View multicast consumer configurations  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/view-consumer-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View multicast consumer configurations

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to list and view the details of multicast consumer configurations.

The commands on this page for listing resources show all multicast configurations, including for Ultra Low Latency (ULL) Multicast and Cloud Multicast.

For more information about the multicast resources mentioned on this page, see [Multicast resource model](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#resources).

## Before you begin

Set the gcloud CLI to use the project for which you want to view multicast resources. Alternatively you can include the `--project=PROJECT_ID` flag for each command in the following procedures.
    
    
        gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project.

## About multicast resource states

The multicast resources that you have configured include a read-only property that describes their current state. When you view multicast configurations by using the procedures on this page, you can view the state of individual resources in the `state` field in the output of the command or request.

The following table describes the possible states:

State | Description  
---|---  
`CREATING` | The resource is being created.  
`ACTIVE` | The resource is in a normal state and ready to use.  
`DELETING` | The resource is being deleted.  
`DELETE_FAILED` | An attempt to delete the resource failed.  
`UPDATING` | The resource is being updated.  
`UPDATE_FAILED` | An attempt to update the resource failed.  
`INACTIVE` | This state applies to multicast consumer configurations. It indicates that the multicast administrator performed an action that deactivated a multicast consumer resource, such as by revoking access to a domain or group range. An existing multicast consumer resource that has an `INACTIVE` state can't be reused. If the multicast administrator restores access to the domain or group range, then the multicast consumer network administrator must delete and recreate the `INACTIVE` resource.  
  
## View multicast consumer configurations

This section describes how to view existing multicast consumer configurations.

### View multicast consumer associations

###  gcloud 

  * To list multicast consumer associations, use the [`network-services multicast-consumer-associations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-consumer-associations/list).
        
        gcloud network-services multicast-consumer-associations list --location=ZONE
        

Replace `ZONE` with the zone for which to list multicast consumer associations.

  * To describe a multicast consumer association, use the [`network-services multicast-consumer-associations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-consumer-associations/describe).
        
        gcloud network-services multicast-consumer-associations describe CONSUMER_ASSOCIATION_NAME \
            --location=ZONE
        

Replace the following values:

    * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association
    * `ZONE`: the zone in which the multicast consumer association was created



###  API 

  * To list multicast consumer associations, use the [`multicastConsumerAssociations.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastConsumerAssociations
        

Replace `ZONE` with the zone for which to list multicast consumer associations.

  * To describe a multicast consumer association, use the [`multicastConsumerAssociations.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastConsumerAssociations/CONSUMER_ASSOCIATION_NAME
        

Replace the following values:

    * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association
    * `ZONE`: the zone in which the multicast consumer association was created



### View multicast group consumer activations

###  gcloud 

  * To list multicast group consumer activations, use the [`network-services multicast-group-consumer-activations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-consumer-activations/list).
        
        gcloud network-services multicast-group-consumer-activations list --location=ZONE
        

Replace `ZONE` with the zone for which to list multicast group consumer activations.

  * To describe a multicast group consumer activation, use the [`network-services multicast-group-consumer-activations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-consumer-activations/describe).
        
        gcloud network-services multicast-group-consumer-activations describe GROUP_CONSUMER_ACTIVATION_NAME \
            --location=ZONE
        

Replace the following values:

    * `GROUP_CONSUMER_ACTIVATION_NAME`: the name of the multicast group consumer activation
    * `ZONE`: the zone in which the multicast consumer network was activated



###  API 

  * To list multicast group consumer activations, use the [`multicastGroupConsumerActivations.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupConsumerActivations
        

Replace `ZONE` with the zone for which to list multicast group consumer activations.

  * To describe a multicast group consumer activation, use the [`multicastGroupConsumerActivations.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupConsumerActivations/GROUP_CONSUMER_ACTIVATION_NAME
        

Replace the following values:

    * `GROUP_CONSUMER_ACTIVATION_NAME`: the name of the multicast group consumer activation
    * `ZONE`: the zone in which the multicast consumer network was activated



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
