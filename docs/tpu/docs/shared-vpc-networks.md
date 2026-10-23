---
url: https://docs.cloud.google.com/tpu/docs/shared-vpc-networks/
title: Connect a TPU to a Shared VPC network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.881982+00:00
---

# Connect a TPU to a Shared VPC network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/shared-vpc-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect a TPU to a Shared VPC network

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This guide explains how to set up Cloud TPUs that use a centrally managed [Shared VPC network](https://docs.cloud.google.com/vpc/docs/overview). This document assumes you are familiar with VPCs and have created a Shared VPC. For more information on how to create and manage Shared VPC networks, see [Create and modify Shared VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

## Configure a VPC host project

You need to grant the TPU Service Account in your [service project](https://docs.cloud.google.com/vpc/docs/shared-vpc#concepts_and_terminology) permissions to manage resources in the [host project](https://docs.cloud.google.com/vpc/docs/shared-vpc#concepts_and_terminology). You do this using the "TPU Shared VPC Agent" (`roles/tpu.xpnAgent`) role. Run the following `gcloud` commands to grant this role binding.
    
    
    gcloud projects add-iam-policy-binding host-project-id \
    --member=serviceAccount:service-your-service-project-number@gcp-sa-tpu.iam.gserviceaccount.com \
    --role=roles/tpu.xpnAgent

**Note:** You can find your service project number in the project info section of the [Google Cloud console](https://console.cloud.google.com/) dashboard.

## Create a TPU VM connected to a Shared VPC Network

First determine which accelerator types and versions are available in the zone
    
    
    gcloud compute tpus accelerator-types list --zone zone
    
    
    gcloud compute tpus versions list --zone zone

You connect a TPU VM to a Shared VPC network when you create your TPU. Specify your Shared VPC using the `--network` tag:
    
    
    gcloud compute tpus tpu-vm create tpu-name \
       --zone zone \
       --accelerator-type accelerator-type \
       --network projects/host-project-id/global/networks/host-network \
       --version tpu-image-version \
       --project your-service-project-id

**Note:** The `--network` tag must be set to the fully qualified network name. For example, `projects/my-host-project-id/global/networks/my-network`.

You can verify your TPU VM is connected to your Shared VPC using the `gcloud describe` command:
    
    
    $ gcloud compute tpus tpu-vm describe tpu-name --zone zone

The response includes the network to which your TPU VM is attached:
    
    
    acceleratorType: v3-8
    apiVersion: V2
    cidrBlock: 10.128.0.0/20
    createTime: '2022-06-17T21:32:13.859274143Z'
    health: HEALTHY
    id: '0000000000000000000'
    name: projects/my-project/locations/us-central1-b/nodes/my-tpu
    networkConfig:
      enableExternalIps: true
      network: projects/my-project/global/networks/default
      subnetwork: projects/my-project/regions/us-central1/subnetworks/default
    networkEndpoints:
    - accessConfig:
        externalIp: 000.000.000.000
      ipAddress: 10.128.0.104
      port: 8470
    runtimeVersion: tpu-vm-tf-2.8.0
    schedulingConfig: {}
    serviceAccount:
      email: 00000000000-compute@developer.gserviceaccount.com
      scope:
      - https://www.googleapis.com/auth/devstorage.read_write
      - https://www.googleapis.com/auth/logging.write
      - https://www.googleapis.com/auth/service.management
      - https://www.googleapis.com/auth/servicecontrol
      - https://www.googleapis.com/auth/cloud-platform
      - https://www.googleapis.com/auth/pubsub
    shieldedInstanceConfig: {}
    state: READY
    

## Delete the TPU VM

When you are done with the TPU VM, make sure to delete it.
    
    
    gcloud compute tpus tpu-vm delete tpu-name --zone zone

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
