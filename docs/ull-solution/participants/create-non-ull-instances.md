---
url: https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances/
title: Create non-ULL Compute Engine instances for auxiliary workloads \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:10.598938+00:00
---

# Create non-ULL Compute Engine instances for auxiliary workloads  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/create-non-ull-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create non-ULL Compute Engine instances for auxiliary workloads

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to create non-Ultra Low Latency (ULL) Compute Engine instances by using U4S machine types from the [U4S machine series](https://docs.cloud.google.com/ull-solution/participants/u4-machines).

You can create non-ULL instances in the private zones supported by ULL Solution for close proximity to ULL instances. You can use non-ULL instances to provide data or services to ULL instances, or to send and receive Cloud Multicast traffic.

## Before you begin

Before you create non-ULL compute instances, see the following sections.

### Create a VPC network

If you haven't already, create a VPC network for your instance as described in [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).

Ensure that the network has a subnet in the region in which you plan to create your instance.

### Set your project

Set the gcloud CLI to use your project. Alternatively you can include the `--project=PROJECT_ID` flag for each command in the following procedures.
    
    
        gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the ID of your project.

### Enable APIs

If you haven't already, enable the following APIs.

###  Console 

Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

###  gcloud 

Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable compute.googleapis.com

## Create a non-ULL instance

This section describes how to create a new non-ULL instance to use for auxiliary workloads.

For general information about creating compute instances, including additional configuration options, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  gcloud 

To create a non-ULL instance, use the [`compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --network=NETWORK \
        --subnet=SUBNET
    

Replace the following values:

  * `ZONE`: the zone in which to create the instance
  * `INSTANCE_NAME`: a name for the instance
  * `MACHINE_TYPE`: the U4S machine type to use for the instance.
  * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info), such as `rhel-cloud`. See [Operating system support for U4 machine types](https://docs.cloud.google.com/ull-solution/participants/u4-machines#u4-os-images).
  * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info), such as `rhel-10-2-eus-oot-gve`. See [Operating system support for U4 machine types](https://docs.cloud.google.com/ull-solution/participants/u4-machines#u4-os-images).

Specifying an image family creates the instance from the most recent, non-deprecated version of the OS image in the image family. Alternatively, you can use the `--image` flag instead and specify an image version.

  * `NETWORK`, `SUBNET`: the general-purpose VPC network and subnet in which to host the instance.




## What's next

  * If you plan to use the non-ULL instance as a multicast consumer for Cloud Multicast, see [Configure an existing instance to be a multicast consumer](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms#update) in the Cloud Multicast documentation.
  * To synchronize your instance system clock to the physical NIC clock of its host server, see [Configure accurate time](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
