---
url: https://docs.cloud.google.com/spanner-omni/create-helm-configuration/
title: Create a Helm chart configuration for Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:34.636575+00:00
---

# Create a Helm chart configuration for Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/create-helm-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Create a Helm chart configuration for Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Helm configuration for Spanner Omni on Kubernetes.

## Overview

You configure Helm charts for Spanner Omni deployments on Kubernetes. Review the available configuration options to customize your deployment. The Helm template includes a `global.platform` property, which sets default values for key settings like `StorageClass` and service annotations based on your chosen platform.

Understand how the Helm chart applies platform-specific default values for Google Kubernetes Engine (GKE) and Amazon Elastic Kubernetes Service (Amazon EKS). These defaults cover configurations such as storage classes, data locations, and service annotations. Customize these settings to align with your specific deployment requirements for each platform.

## Before you begin

If you haven't done so already, install [Helm](https://helm.sh/).

## Prepare a Helm chart configuration

To create a Helm chart configuration, do the following:

  1. Use the `helm show values` command to review the configuration options available for creating a deployment:
         
         helm show values oci://us-docker.pkg.dev/spanner-omni/charts/spanner-omni --version 1.0.0
         

The documentation for creating a deployment uses the `--set` flag to specify various options. You can also specify these options in a YAML file and use the `-f` flag in the `helm` command. For ease of deployment, the Helm template includes the `global.platform` property, which determines the default values for the `StorageClass`, service annotations, and other settings based on the platform.

  2. The following table summarizes the platform-specific default values for Google Kubernetes Engine (GKE) and Amazon EKS:


Property | Default | Platform  
---|---|---  
GKE | Amazon EKS  
`storageClasses` | `- name: my_sc`  
`provisioner: kubernetes.io/no-provisioner`  
`volumeBindingMode: WaitForFirstConsumer` | `- name: hyperdisk-balanced-rwo`  
`provisioner: pd.csi.storage.gke.io`  
`parameters:`  
` type: hyperdisk-balanced` | `- name: aws-gp3`  
`provisioner: ebs.csi.aws.com`  
`parameters:`  
` type: gp3`  
`- name: aws-standard`  
`provisioner: ebs.csi.aws.com`  
`parameters:`  
` type: standard`  
`locations` | `- name: us`  
`namespace: ""`  
`zones:`  
`- name: "us-a"`  
`shortName: "a"`  
`replicas: 1`  
`rootServers: 1`  
`singleServer: true`  
`- name: "us-b"`  
`shortName: "b"`  
`- name: "us-c"`  
`shortName: "c"` | `- name: us-east1`  
`zones:`  
`- name: us-east1-b`  
`shortName: a`  
`- name: us-east1-c`  
`shortName: b`  
`- name: us-east1-d`  
`shortName: c` | `- name: us-east-1`  
`zones:`  
`- name: us-east-1a`  
`shortName: a`  
`- name: us-east-1c`  
`shortName: b`  
`- name: us-east-1d`  
`shortName: c`  
`dataStorageClass` | `<default>` | `premium-rwo` | `aws-gp3`  
`logsStorageClass` | `<default>` | `standard-rwo` | `aws-standard`  
`serviceAnnotations` | `null` | `networking.gke.io/load-balancer-type: "Internal"`  
`networking.gke.io/internal-load-balancer-allow-global-access: "true"` | `service.beta.kubernetes.io/aws-load-balancer-internal: "true"`  
`service.beta.kubernetes.io/aws-load-balancer-type: "nlb"`  
`service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: "ip"`  
`service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"`  
  
The number of root servers per zone must be an odd number between one and nine, inclusive, to ensure quorum for consistency. If the number of servers is an even number, deployments might fail. When configuring your zones, designate servers as root servers. We recommend that you use one for development or testing and three for highly available production zones. 

## What's next

  * Learn how to use a Helm chart to [create a multi-cluster deployment on Kubernetes for Spanner Omni](https://docs.cloud.google.com/spanner-omni/deploy-multi-cluster-on-kubernetes).

  * Learn how to use a Helm chart to [create a deployment on Kubernetes for Spanner Omni](https://docs.cloud.google.com/spanner-omni/deploy-on-kubernetes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
