---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/dev-tools/
title: Developer tools overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:35.916555+00:00
---

# Developer tools overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/dev-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Developer tools overview Stay organized with collections  Save and categorize content based on your preferences. 

To interact with your Google Distributed Cloud (GDC) air-gapped universe, you must configure one or more of the following tools:

  * **GDC console** : the primary graphical user interface for GDC air-gapped.
  * **gdcloud CLI** : the primary command-line interface (CLI) for GDC air-gapped.
  * **kubectl CLI** : the Kubernetes CLI used for managing Kubernetes Resource Model (KRM) APIs.
  * **Terraform** : an infrastructure-as-code (IaC) tool that manages KRM APIs using the Terraform Kubernetes provider.



These tools help you deploy and manage applications, manage infrastructure, and view resources in your GDC environment.

This document is for all operators, administrators, and developers who deploy and manage resources in GDC. For more information about audience groups in GDC, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## GDC console

The GDC console is a graphical user interface that lets you manage your GDC projects and resources. From the GDC console, you can perform various tasks such as monitoring your workloads, managing access to resources, and viewing audit logs.

To access the GDC console, open the GDC URL provided by your infrastructure operator group in a web browser. You must authenticate with your identity provider to [sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in).

For more information, see [GDC console access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/console).

## gdcloud CLI

The gdcloud CLI is a GDC air-gapped command-line tool dedicated for managing resources in a disconnected environment. The gdcloud CLI provides capabilities such as the following:

  * Customizable configurations and properties
  * Authentication for clusters, API servers, and zonal and global contexts
  * Autocompletion
  * Accessibility



For more information, see [Use the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/gdcloud).

For reference documentation of all gdcloud CLI commands, see the [gdcloud reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud).

## kubectl CLI

The Kubernetes CLI tool, kubectl, lets you create and manage GDC resources by calling the underlying [Kubernetes Resource Model (KRM) APIs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/apis-overview). For example, you can use the kubectl CLI to deploy virtual machines (VM), inspect and manage cluster resources, and view logs.

The majority of API procedures in GDC documentation require the kubectl CLI.

Before you can use the kubectl CLI to manage resources, you must [install the kubectl CLI tool](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl) and then authenticate with the GDC cluster or API server that hosts your resource with a kubeconfig file. The gdcloud CLI provides the [`get-credentials` command](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) to generate kubeconfig files automatically, or you can [generate a kubeconfig file manually](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#generate-kubeconfig-file).

## Terraform

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage infrastructure resources. In GDC, you can use Terraform to manage your resources by interacting with Kubernetes APIs. GDC uses the [Kubernetes provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) to give Terraform access to the Kubernetes APIs.

For more information about Terraform in GDC, see the [Terraform overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/terraform).

To quickly set up Terraform in your GDC environment, see [Use Terraform](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/terraform).

## What's next

  * [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones)
  * [Design access boundaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/access-boundaries)
  * [Kubernetes concepts for GDC](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/get-started-with-kubernetes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
