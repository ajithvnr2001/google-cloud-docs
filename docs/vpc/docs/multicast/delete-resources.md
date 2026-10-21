---
url: https://docs.cloud.google.com/vpc/docs/multicast/delete-resources/
title: Delete multicast configurations \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.909741+00:00
---

# Delete multicast configurations  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/delete-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete multicast configurations

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to delete existing multicast configurations for Cloud Multicast.

For more information about the multicast resources described on this page, see [Cloud Multicast resource model](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#resources).

## Before you begin

Set the gcloud CLI to use the project in which you want to delete multicast configurations. Alternatively you can include the `--project=PROJECT_ID` flag for each command in the following procedures.
    
    
        gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project.

## Deletion order

This section describes the required deletion order for multicast configurations:

  * **For multicast consumers:** If you are a multicast consumer network administrator in a multicast domain that uses the Network Connectivity Center (NCC) star topology, see Delete multicast consumer configurations.
  * **For multicast producers:** If you are a multicast producer network administrator in a multicast domain that uses the NCC star topology, see Delete multicast producer configurations.
  * **For multicast administrators:** If you are the multicast administrator for a domain, ensure that you adhere to the following deletion order.



Multicast configurations must be deleted in the following order. If you attempt to delete one of the following resources while it is still in use by another resource, then Google Cloud returns an error.

  1. If the same VPC network has both multicast producer and multicast consumer configurations, then you must first delete multicast consumer configurations, regardless of the topology of the multicast domain.

If you are using the NCC star topology and all multicast consumer configurations are in different networks, then you can skip this step. You can delete the following multicast configurations without deleting the multicast consumer configurations.

  2. Delete multicast producer configurations.

  3. Delete group range activations.

  4. At this step, you can delete both group ranges and domain activations.

  5. Delete domains.

  6. Delete domain groups.




In the NCC star topology, if there are any multicast consumer configurations that depend on a deleted multicast group range or multicast domain, then the associated multicast consumer resources are deactivated and have a status of `OBSOLETE`.

## Delete multicast consumer configurations

This section describes how to delete existing multicast consumer configurations.

To delete a multicast consumer association, you must first delete all of its multicast group consumer activations.

### Delete multicast group consumer activations

###  gcloud 

To delete a multicast group consumer activation, use the [`network-services multicast-group-consumer-activations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-consumer-activations/delete).
    
    
      gcloud network-services multicast-group-consumer-activations delete GROUP_CONSUMER_ACTIVATION_NAME \
          --location=ZONE
    

Replace the following values:

  * `GROUP_CONSUMER_ACTIVATION_NAME`: the name of the multicast group consumer activation
  * `ZONE`: the zone in which the multicast consumer VPC network was activated



###  API 

To delete a multicast group consumer activation, use the [`multicastGroupConsumerActivations.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupConsumerActivations/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupConsumerActivations/GROUP_CONSUMER_ACTIVATION_NAME
    

Replace the following values:

  * `PROJECT_ID`: the ID of the project
  * `GROUP_CONSUMER_ACTIVATION_NAME`: the name of the multicast group consumer activation
  * `ZONE`: the zone in which the multicast consumer VPC network was activated



### Delete multicast consumer associations

###  gcloud 

To delete a multicast consumer association, use the [`network-services multicast-consumer-associations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-consumer-associations/delete).
    
    
      gcloud network-services multicast-consumer-associations delete CONSUMER_ASSOCIATION_NAME \
          --location=ZONE
    

Replace the following values:

  * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association
  * `ZONE`: the zone in which the multicast consumer association was created



###  API 

To delete a multicast consumer association, use the [`multicastConsumerAssociations.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastConsumerAssociations/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastConsumerAssociations/CONSUMER_ASSOCIATION_NAME
    

Replace the following values:

  * `PROJECT_ID`: the ID of the project
  * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association
  * `ZONE`: the zone in which the multicast consumer association was created



## Delete multicast producer configurations

This section describes how to delete existing multicast producer configurations.

To delete a multicast producer association, you must first delete all of its multicast group producer activations.

### Delete multicast group producer activations

###  gcloud 

To delete a multicast group producer activation, use the [`network-services multicast-group-producer-activations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-producer-activations/delete).
    
    
      gcloud network-services multicast-group-producer-activations delete GROUP_PRODUCER_ACTIVATION_NAME \
          --location=ZONE
    

Replace the following values:

  * `GROUP_PRODUCER_ACTIVATION_NAME`: the name of the multicast group producer activation
  * `ZONE`: the zone in which the multicast producer VPC network was activated



###  API 

To delete a multicast group producer activation, use the [`multicastGroupProducerActivations.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupProducerActivations/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupProducerActivations/GROUP_PRODUCER_ACTIVATION_NAME
    

Replace the following values:

  * `PROJECT_ID`: the ID of the project
  * `GROUP_PRODUCER_ACTIVATION_NAME`: the name of the multicast group producer activation
  * `ZONE`: the zone in which the multicast producer VPC network was activated



### Delete multicast producer associations

###  gcloud 

To delete a multicast producer association, use the [`network-services multicast-producer-associations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-producer-associations/delete).
    
    
      gcloud network-services multicast-producer-associations delete PRODUCER_ASSOCIATION_NAME \
          --location=ZONE
    

Replace the following values:

  * `PRODUCER_ASSOCIATION_NAME`: the name of the multicast producer association
  * `ZONE`: the zone in which the multicast producer association was created



###  API 

To delete a multicast producer association, use the [`multicastProducerAssociations.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastProducerAssociations/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastProducerAssociations/PRODUCER_ASSOCIATION_NAME
    

Replace the following values:

  * `PROJECT_ID`: the ID of the project
  * `PRODUCER_ASSOCIATION_NAME`: the name of the multicast producer association
  * `ZONE`: the zone in which the multicast producer association was created



## Delete multicast group ranges and domains

This section describes how to delete existing configurations for multicast group ranges and domains.

Ensure that you follow the required deletion order.

### Delete multicast group range configurations

This section describes how to delete existing configurations for multicast group ranges.

#### Delete group range activations

###  gcloud 

To delete a multicast group range activation, use the [`network-services multicast-group-range-activations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-range-activations/delete).
    
    
      gcloud network-services multicast-group-range-activations delete GROUP_RANGE_ACTIVATION_NAME \
          --location=ZONE
    

Replace the following:

  * `GROUP_RANGE_ACTIVATION_NAME` the name of the group range activation
  * `ZONE` the zone in which the group range was activated



###  API 

To delete a multicast group range activation, use the [`multicastGroupRangeActivations.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRangeActivations/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project
  * `GROUP_RANGE_ACTIVATION_NAME` the name of the group range activation
  * `ZONE` the zone in which the group range was activated



#### Delete group ranges

###  gcloud 

To delete a multicast group range, use the [`network-services multicast-group-ranges delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-ranges/delete).
    
    
      gcloud network-services multicast-group-ranges delete GROUP_RANGE_NAME \
          --location=global
    

Replace `GROUP_RANGE_NAME` with the name of the group range.

###  API 

To delete a multicast group range, use the [`multicastGroupRanges.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastGroupRanges/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastGroupRanges/GROUP_RANGE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project
  * `GROUP_RANGE_NAME`: the name of the group range



### Delete multicast domain configurations

This section describes how to delete existing configurations for multicast domains.

#### Delete domain activations

###  gcloud 

To delete a multicast domain activation, use the [`network-services multicast-domain-activations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-activations/delete).

The following command can take several minutes to complete.
    
    
      gcloud network-services multicast-domain-activations delete DOMAIN_ACTIVATION_NAME \
          --location=ZONE
    

Replace the following values:

  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation
  * `ZONE`: the zone where the domain was activated



###  API 

To delete a multicast domain activation, use the [`multicastDomainActivations.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainActivations/delete).

The following command can take several minutes to complete.
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME
    

Replace the following values:

  * `PROJECT_ID`: the ID of the project
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation
  * `ZONE`: the zone where the domain was activated



#### Delete domains

###  gcloud 

To delete a multicast domain, use the [`network-services multicast-domains delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domains/delete).
    
    
      gcloud network-services multicast-domains delete DOMAIN_NAME \
          --location=global
    

Replace `DOMAIN_NAME` with the name of the domain.

###  API 

To delete a multicast domain, use the [`multicastDomains.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomains/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastDomains/DOMAIN_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project
  * `DOMAIN_NAME`: the name of the domain



#### Delete domain groups

###  gcloud 

To delete a multicast domain group, use the [`network-services multicast-domain-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domain-groups/delete).
    
    
      gcloud network-services multicast-domain-groups delete DOMAIN_GROUP_NAME \
          --location=global
    

Replace `DOMAIN_GROUP_NAME` with the name of the domain group.

###  API 

To delete a multicast domain group, use the [`multicastDomainGroups.delete` method](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1/projects.locations.multicastDomainGroups/delete).
    
    
    DELETE https://networkservices.googleapis.com/v1/projects/PROJECT_ID/locations/global/multicastDomainGroups/DOMAIN_GROUP_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project
  * `DOMAIN_GROUP_NAME`: the name of the domain group



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
