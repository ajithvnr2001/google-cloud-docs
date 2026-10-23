---
url: https://docs.cloud.google.com/ull-solution/participants/enable-consumer-network/
title: Enable a ULL VPC network to consume multicast traffic \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:49.363578+00:00
---

# Enable a ULL VPC network to consume multicast traffic  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/enable-consumer-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable a ULL VPC network to consume multicast traffic

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes the steps required to configure resources in Google Cloud so that multicast consumers in an Ultra Low Latency (ULL) VPC network can receive multicast traffic from a given ULL Multicast domain and one or more group ranges.

## Before you begin

Before you begin the procedures on this page, you must complete the prerequisites that are described in this section.

### Confirm that the multicast domain, group range, and producer configurations are complete

Confirm that the multicast domain, multicast group range, and multicast producer configurations for which you want to consume multicast traffic are complete as described in [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview). If necessary, contact the multicast administrator of the domain.

### Create a ULL VPC network and add it to a hub

The procedures on this page require a ULL VPC network to use as a _multicast consumer network_. If you haven't created one already, see [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).

### Set your project

Set the gcloud CLI to use the project of the multicast consumer network. Alternatively you can pass in the `--project=MULTICAST_CONSUMER_PROJECT` flag for each command in the following procedures.
    
    
    gcloud config set project MULTICAST_CONSUMER_PROJECT
    

Replace `MULTICAST_CONSUMER_PROJECT` with the ID of your project.

### Enable APIs

If you haven't already, enable the following APIs.

###  Console 

Enable the Network Services API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=networkservices.googleapis.com)

###  gcloud 

Enable the Network Services API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable networkservices.googleapis.com

### Required roles

To get the permissions that you need to configure multicast consumer resources, ask your administrator to grant you the following IAM roles: 

  * To create multicast resources: Multicast Admin (`networkservices.multicastAdmin`) on your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable a ULL VPC network to consume multicast traffic

This section describes the steps required to enable multicast consumers in a ULL VPC network to receive multicast traffic from a given ULL Multicast domain and one or more group ranges.

### Add the multicast consumer network to a domain

This section describes how to add a multicast consumer network to a domain by creating a multicast consumer association between the network and the domain.

Complete the following steps for each domain for which you want to consume multicast traffic.

###  gcloud 

To add a multicast consumer network to a domain, use the [`network-services multicast-consumer-associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-consumer-associations/create).
    
    
    gcloud network-services multicast-consumer-associations create CONSUMER_ASSOCIATION_NAME \
        --multicast-domain-activation="projects/MULTICAST_ADMIN_PROJECT/locations/ZONE/multicastDomainActivations/DOMAIN_ACTIVATION_NAME" \
        --network="projects/MULTICAST_CONSUMER_PROJECT/locations/global/networks/MULTICAST_CONSUMER_NETWORK" \
        --location=ZONE
    

Replace the following values:

  * `CONSUMER_ASSOCIATION_NAME`: a name for the multicast consumer association
  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project
  * `ZONE`: a zone in which the administrator activated the multicast domain and in which you need to host multicast consumers
  * `DOMAIN_ACTIVATION_NAME`: the name of the domain activation that was created by the multicast administrator
  * `MULTICAST_CONSUMER_PROJECT` and `MULTICAST_CONSUMER_NETWORK`: the project and ULL VPC network that consumes multicast traffic.



### Activate the multicast consumer network for a group range

This section describes how to activate a multicast consumer network for a group range.

Complete the following steps for each multicast group range for which you want to consume multicast traffic.

###  gcloud 

To activate a multicast consumer network for a multicast group range, use the [`network-services multicast-group-consumer-activations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-group-consumer-activations/create).

**Note:** If you can't run the following command successfully, your project might not be part of the consumer accept list for the group range. If necessary, contact the multicast administrator.
    
    
    gcloud network-services multicast-group-consumer-activations create GROUP_CONSUMER_ACTIVATION_NAME \
        --multicast-consumer-association="projects/MULTICAST_CONSUMER_PROJECT/locations/ZONE/multicastConsumerAssociations/CONSUMER_ASSOCIATION_NAME" \
        --multicast-group-range-activation="projects/MULTICAST_ADMIN_PROJECT/locations/ZONE/multicastGroupRangeActivations/GROUP_RANGE_ACTIVATION_NAME" \
        --location=ZONE \
        [--enable-logging | --no-enable-logging]
    

Replace the following values:

  * `GROUP_CONSUMER_ACTIVATION_NAME`: a name for the multicast group consumer activation
  * `MULTICAST_CONSUMER_PROJECT`: the ID of your project

  * `ZONE`: the zone in which to activate the multicast consumer network. Must also be a zone in which the administrator activated the multicast group range.

  * `CONSUMER_ASSOCIATION_NAME`: the name of the multicast consumer association that you created previously

  * `MULTICAST_ADMIN_PROJECT`: the ID of the multicast administrator project

  * `GROUP_RANGE_ACTIVATION_NAME`: the name of the group range activation that was created by the multicast administrator.

  * `--[no-]enable-logging`: optional, determines whether [group membership event logging](https://docs.cloud.google.com/ull-solution/view-membership-logs) is enabled.

    * To enable logging, use `--enable-logging`.
    * (Default) To disable logging, use `--no-enable-logging`.



## What's next

  * To create multicast consumer instances, see [Create ULL Compute Engine instances](https://docs.cloud.google.com/ull-solution/participants/create-ull-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
