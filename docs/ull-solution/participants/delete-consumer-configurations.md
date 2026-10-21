---
url: https://docs.cloud.google.com/ull-solution/participants/delete-consumer-configurations/
title: Delete multicast consumer configurations \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:31.407882+00:00
---

# Delete multicast consumer configurations  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/delete-consumer-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Delete multicast consumer configurations

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to delete existing multicast consumer configurations.

## Before you begin

Set the gcloud CLI to use the project in which you want to delete multicast configurations. Alternatively you can include the `--project=PROJECT_ID` flag for each command in the following procedures.
    
    
        gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project.

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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
