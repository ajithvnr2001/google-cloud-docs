---
url: https://docs.cloud.google.com/vpc/docs/multicast/view-resources/
title: View multicast configurations \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:43.919413+00:00
---

# View multicast configurations  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/view-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View multicast configurations

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to list and view the details of multicast configurations for Cloud Multicast.

For more information about the multicast resources mentioned on this page, see [Cloud Multicast resource model](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#resources).

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
  
## View multicast domain configurations

This section describes how to view existing configurations for multicast domains.

### View multicast domain groups

###  gcloud 

  * To list multicast domain groups, use the [`network-services multicast-domain-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-groups/list).
        
        gcloud network-services multicast-domain-groups list --location=global 
        

  * To describe a multicast domain group, use the [`network-services multicast-domain-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-groups/describe).
        
        gcloud network-services multicast-domain-groups describe DOMAIN_GROUP_NAME \
            --location=global
        

Replace `DOMAIN_GROUP_NAME` with the name of the domain group.




###  API 

  * To list multicast domain groups, use the [`multicastDomainGroups.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastDomainGroups
        

  * To describe a multicast domain group, use the [`multicastDomainGroups.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastDomainGroups/DOMAIN_GROUP_NAME
        

Replace `DOMAIN_GROUP_NAME` with the name of the domain group.




### View multicast domains

###  gcloud 

  * To list multicast domains, use the [`network-services multicast-domains list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domains/list).
        
        gcloud network-services multicast-domains list --location=global
        

  * To describe a multicast domain, use the [`network-services multicast-domains describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domains/describe).
        
        gcloud network-services multicast-domains describe DOMAIN_NAME \
            --location=global
        

Replace `DOMAIN_NAME` with the name of the domain.




###  API 

  * To list multicast domains, use the [`multicastDomains.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastDomains
        

  * To describe a multicast domain, use the [`multicastDomains.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastDomains/DOMAIN_NAME
        

Replace `DOMAIN_NAME` with the name of the domain.




### View multicast domain activations

###  gcloud 

  * To list multicast domain activations, use the [`network-services multicast-domain-activations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-activations/list).
        
        gcloud network-services multicast-domain-activations list --location=ZONE
        

Replace `ZONE` with the zone for which to list domain activations.

  * To describe a multicast domain activation, use the [`network-services multicast-domain-activations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-activations/describe).
        
        gcloud network-services multicast-domain-activations describe DOMAIN_ACTIVATION_NAME \
            --location=ZONE
        

Replace the following values:

    * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation
    * `ZONE`: the zone where the domain was activated



###  API 

  * To list multicast domain activations, use the [`multicastDomainActivations.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastDomainActivations
        

Replace `ZONE` with the zone for which to list domain activations.

  * To describe a multicast domain activation, use the [`multicastDomainActivations.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME
        

Replace the following values:

    * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation
    * `ZONE`: the zone where the domain was activated



## View multicast group range configurations

This section describes how to view existing configurations for multicast groups.

### View multicast group ranges

###  gcloud 

  * To list multicast group ranges, use the [`network-services multicast-group-ranges list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/list).
        
        gcloud network-services multicast-group-ranges list --location=global
        

  * To describe a multicast group range, use the [`network-services multicast-group-ranges describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/describe).
        
        gcloud network-services multicast-group-ranges describe GROUP_RANGE_NAME \
            --location=global
        

Replace `GROUP_RANGE_NAME` with the name of the group range.




###  API 

  * To list multicast group ranges, use the [`multicastGroupRanges.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges
        

  * To describe a multicast group range, use the [`multicastGroupRanges.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME
        

Replace `GROUP_RANGE_NAME` with the name of the group range.




### View multicast group range activations

###  gcloud 

  * To list multicast group range activations, use the [`network-services multicast-group-range-activations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-range-activations/list).
        
        gcloud network-services multicast-group-range-activations list --location=ZONE
        

Replace `ZONE` with the zone for which to list group range activations.

  * To describe a multicast group range activation, use the [`network-services multicast-group-range-activations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-range-activations/describe).
        
        gcloud network-services multicast-group-range-activations describe GROUP_RANGE_ACTIVATION_NAME \
            --location=ZONE
        

Replace the following values:

    * `GROUP_RANGE_ACTIVATION_NAME`: the name of the group range activation
    * `ZONE`: the zone where the group range was activated



###  API 

  * To list multicast group range activations, use the [`multicastGroupRangeActivations.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupRangeActivations
        

Replace `ZONE` with the zone for which to list group range activations.

  * To describe a multicast group range activation, use the [`multicastGroupRangeActivations.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME
        

Replace the following values:

    * `GROUP_RANGE_ACTIVATION_NAME`: the name of the group range activation
    * `ZONE`: the zone where the group range was activated



## View multicast producer configurations

This section describes how to view existing multicast producer configurations.

### View multicast producer associations

###  gcloud 

  * To list multicast producer associations, use the [`network-services multicast-producer-associations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-producer-associations/list).
        
        gcloud network-services multicast-producer-associations list --location=ZONE
        

Replace `ZONE` with the zone for which to list multicast producer associations.

  * To describe a multicast producer association, use the [`network-services multicast-producer-associations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-producer-associations/describe).
        
        gcloud network-services multicast-producer-associations describe PRODUCER_ASSOCIATION_NAME \
            --location=ZONE
        

Replace the following values:

    * `PRODUCER_ASSOCIATION_NAME`: the name of the multicast producer association
    * `ZONE`: the zone in which the multicast producer association was created



###  API 

  * To list multicast producer associations, use the [`multicastProducerAssociations.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastProducerAssociations
        

Replace `ZONE` with the zone for which to list multicast producer associations.

  * To describe a multicast producer association, use the [`multicastProducerAssociations.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastProducerAssociations/PRODUCER_ASSOCIATION_NAME
        

Replace the following values:

    * `PRODUCER_ASSOCIATION_NAME`: the name of the multicast producer association
    * `ZONE`: the zone in which the multicast producer association was created



### View multicast group producer activations

###  gcloud 

  * To list multicast group producer activations, use the [`network-services multicast-group-producer-activations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-producer-activations/list).
        
        gcloud network-services multicast-group-producer-activations list --location=ZONE
        

Replace `ZONE` with the zone for which to list multicast group producer activations.

  * To describe a multicast group producer activation, use the [`network-services multicast-group-producer-activations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-producer-activations/describe).
        
        gcloud network-services multicast-group-producer-activations describe GROUP_PRODUCER_ACTIVATION_NAME \
            --location=ZONE
        

Replace the following values:

    * `GROUP_PRODUCER_ACTIVATION_NAME`: the name of the multicast group producer activation
    * `ZONE`: the zone in which the multicast producer network was activated



###  API 

  * To list multicast group producer activations, use the [`multicastGroupProducerActivations.list` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/list).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupProducerActivations
        

Replace `ZONE` with the zone for which to list multicast group producer activations.

  * To describe a multicast group producer activation, use the [`multicastGroupProducerActivations.get` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/get).
        
        GET https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupProducerActivations/GROUP_PRODUCER_ACTIVATION_NAME
        

Replace the following values:

    * `GROUP_PRODUCER_ACTIVATION_NAME`: the name of the multicast group producer activation
    * `ZONE`: the zone in which the multicast producer network was activated



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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
