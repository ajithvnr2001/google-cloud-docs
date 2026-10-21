---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/
title: gcloud alpha container ai profiles \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:11.297606+00:00
---

# gcloud alpha container ai profiles  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container ai profiles Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container ai profiles - quickstart engine for GKE AI workloads 
SYNOPSIS
    

`gcloud alpha container ai profiles` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The GKE Inference Quickstart helps simplify deploying AI inference on Google Kubernetes Engine (GKE). It provides tailored profiles based on Google's internal benchmarks. Provide inputs like your preferred open-source model (e.g. Llama, Gemma, or Mistral) and your application's performance target. Based on these inputs, the quickstart generates accelerator choices with performance metrics, and detailed, ready-to-deploy profiles for compute, load balancing, and autoscaling. These profiles are provided as standard Kubernetes YAML manifests, which you can deploy or modify. 

To visualize the benchmarking data that support these estimates, see the accompanying Colab notebook: <https://colab.research.google.com/github/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/notebooks/giq_visualizations.ipynb>

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[accelerators](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/accelerators)`
     `(ALPHA)` Manage supported accelerators for GKE Inference Quickstart. 
`[manifests](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/manifests)`
     `(ALPHA)` Generate optimized Kubernetes manifests. 
`[model-and-server-combinations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/model-and-server-combinations)`
     `(ALPHA)` Manage supported model and model servers for GKE Inference Quickstart. 
`[model-server-versions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/model-server-versions)`
     `(ALPHA)` Manage supported model server versions for GKE Inference Quickstart. 
`[model-servers](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/model-servers)`
     `(ALPHA)` Manage supported model servers for GKE Inference Quickstart. 
`[models](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/models)`
     `(ALPHA)` Manage supported models for GKE Inference Quickstart. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud container ai profiles](https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
