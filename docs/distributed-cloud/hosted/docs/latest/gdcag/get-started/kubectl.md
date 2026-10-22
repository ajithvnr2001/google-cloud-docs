---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl/
title: Install the kubectl CLI \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:11.060587+00:00
---

# Install the kubectl CLI  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/kubectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Install the kubectl CLI Stay organized with collections  Save and categorize content based on your preferences. 

The Kubernetes command-line tool, _kubectl_ , lets you call the underlying Kubernetes Resource Model (KRM) APIs provided by Google Distributed Cloud (GDC) air-gapped. You can deploy Kubernetes custom resource definitions with the kubectl CLI to create and manage GDC service resources.

This document is for all audience groups that work on GDC that must make API calls to manage their air-gapped hardware and software workflows. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you install the kubectl CLI, you must install and configure the gdcloud CLI. For more information, see [Use the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/get-started/gdcloud).

## Install the kubectl CLI

Complete the following steps to install the kubectl CLI in your GDC environment:

  1. Install the `kubectl` component with the gdcloud CLI:
         
         gdcloud components install kubectl
         

  2. Verify that the kubectl CLI is installed:
         
         kubectl version
         

The output is similar to the following:
         
         Client Version: v1.30.2-gke.1100
         Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
         Server Version: v1.30.12-gke.300
         

**Important:** The kubectl CLI version bundled with the gdcloud CLI is sometimes not the latest version available. If you prefer a different version of the kubectl CLI, you must connect to the internet and download the version you prefer.
  3. Install the `gdcloud-k8s-auth-plugin` component with the gdcloud CLI:
         
         gdcloud components install gdcloud-k8s-auth-plugin
         




After the kubectl CLI is installed, you must use the gdcloud CLI to [generate the kubeconfig file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-auth#get-kubeconfig) for the cluster or API server that hosts your resources to give you access to the APIs.

## What's next

  * [Access zones with your tools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/access-zones)
  * [Sign in to projects](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in)
  * [GDC air-gapped APIs overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/apis-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
