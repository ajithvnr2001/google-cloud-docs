---
url: https://docs.cloud.google.com/tpu/docs/collection-scheduling/
title: TPU collection scheduling for inference workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:24.802248+00:00
---

# TPU collection scheduling for inference workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/collection-scheduling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU collection scheduling for inference workloads

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. We recommend using Google Kubernetes Engine for collection scheduling. For more information, see [Collection scheduling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling) in the GKE documentation.

Trillium (v6e) includes a feature called "collection scheduling" that lets you group a set of TPU slices, single or multi-host, intended to serve replicas of the same model. This feature is available for both Cloud TPU and Google Kubernetes Engine (GKE) configurations.

This document is about using collection scheduling with the Cloud TPU API. See the [GKE documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus#collection-scheduling) for more information about using collection scheduling with GKE.

By creating a collection for your inference workload, Google Cloud limits and streamlines interruptions to the operations of inference workloads. This is useful for inference workloads where high availability is a concern. Google Cloud ensures high availability for the collection to manage incoming traffic. A portion of slices within a collection is always available to handle incoming traffic.

Each TPU slice in a collection will have the same accelerator type and topology.

**Note:** Collection scheduling only applies to v6e.

### Create a collection from the Cloud TPU API

When you request a queued resource using the Cloud TPU API, you use the `--workload-type=AVAILABILITY-OPTIMIZED` flag to create a collection. This flag indicates to the Cloud TPU infrastructure that it is meant to be used for availability-focused workloads.

The following command provisions a collection using the Cloud TPU API:
    
    
    gcloud alpha compute tpus queued-resources create QUEUED_RESOURCE_ID \
       --project=PROJECT_ID \
       --zone=ZONE \
       --accelerator-type=ACCELERATOR_TYPE \
       --runtime-version=RUNTIME_VERSION \
       --node-count=NODE_COUNT \
       --node-prefix=NODE_PREFIX \
       --workload-type=AVAILABILITY-OPTIMIZED

The `--node-count` flag specifies the number of slices you want in your queued resource. This creates a collection of TPU slices.

Optional: The `--node-prefix` flag specifies a prefix for the slice names.

**Note:** The supported accelerator types are described in [v6e supported configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
