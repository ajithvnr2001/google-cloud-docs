---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/vertex-ai/
title: Using Vertex AI \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:37.416459+00:00
---

# Using Vertex AI  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/vertex-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Using Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the different ways to use Vertex AI in the GDC Sandbox environment, and how to set up to use it.

## Usage models for Vertex AI in GDC Sandbox

Vertex AI is a machine learning (ML) platform that lets you train and deploy ML models and AI applications. You can use API on GDC Sandbox in two different ways:

  1. CPU-based: run your workload in your GDC Sandbox user cluster, without using GPUs. This option is slower due to running only on CPUs.
  2. GPU-based: take advantage of the GPU support included in the GDC Sandbox AI Optimized SKU, by configuring the workload to use the GPUs associated with the `sandbox-gpu-project` project. This project is only present in GDC Sandbox instances provisioned with the GDC Sandbox AI Optimized SKU.



[Deploy GPU container workloads](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/services/gpu) describes how to configure a workload to use GPUs.

## Set up to use Vertex AI

The use of Vertex AI on GDC Sandbox is not the same as Google Distributed Cloud (GDC) air-gapped. Rather than using the specialized Vertex AI APIs that are part of the Google Distributed Cloud air-gapped platform, you use the regular Google Cloud version of this API. You need a Google Cloud billing account to use this API.

  1. Visit the [Vertex AI environment setup page](https://docs.cloud.google.com/vertex-ai/docs/start/cloud-environment) and: 
     1. Create or identify a Google Cloud project, 
     2. Make sure that billing is enabled for your project, and
     3. Enable the Vertex AI API.
  2. Authenticate to Vertex AI API. Authentication for APIs can be achieved through various methods tailored to specific requirements - see [Authentication methods at Google](https://docs.cloud.google.com/docs/authentication). 
     * To authenticate to Vertex AI API using an API key, generate an [API key](https://docs.cloud.google.com/docs/authentication/api-keys).
     * To authenticate to Vertex AI API using a service account, create a service account key json file by following the instructions at [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating).



After this, you can install the Vertex AI client library for the language you plan to use. Libraries are [available](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries#client_libraries) for many languages, including Python, Java, and Go. The example applications on the following pages include instructions for installing the appropriate library.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
