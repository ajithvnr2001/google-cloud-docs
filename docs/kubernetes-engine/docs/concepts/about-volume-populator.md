---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-volume-populator/
title: About GKE Volume Populator \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:54.270710+00:00
---

# About GKE Volume Populator  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-volume-populator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE Volume Populator Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

The Google Kubernetes Engine (GKE) Volume Populator can help you automate and streamline the process of preloading data from [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets) to destination [PersistentVolumeClaims (PVCs)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistentvolumeclaims) during [dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#dynamic_provisioning). 

## How GKE Volume Populator works

GKE Volume Populator leverages the core [Kubernetes Volume Populator](https://kubernetes.io/blog/2022/05/16/volume-populators-beta/) concept. Instead of provisioning an empty volume, the GKE Volume Populator allows a PVC to reference a [`GCPDataSource`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/gcpdatasource) custom resource. This custom resource specifies the source Cloud Storage bucket and the necessary credentials.

When you create a PVC with a `dataSourceRef` pointing to a `GCPDataSource` resource, the GKE Volume Populator initiates the data transfer. It copies data from the specified Cloud Storage bucket URI into the underlying persistent storage volume before making the volume available to your Pods.

This process reduces your need to use manual data transfer scripts or CLI commands, and automates the transfer of large datasets to persistent volumes. GKE Volume Populator supports data transfers between the following source and destination types:

  * Cloud Storage to [Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk#hyperdisk-ml)



GKE Volume Populator is a GKE managed component that's enabled by default on both Autopilot and Standard clusters. You primarily interact with GKE Volume Populator through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and [kubectl](https://kubernetes.io/docs/reference/kubectl/) CLI.

### Architecture

The following diagram shows how data flows from the source storage to the destination storage, and how the [PersistentVolume](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes) for the destination storage is created by using GKE Volume Populator.

  1. You create a PVC that references a [`GCPDataSource`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/gcpdatasource) custom resource.
  2. The GKE Volume Populator detects the PVC and initiates a data transfer Job.
  3. The transfer Job runs on an existing node pool, or a new one is created if node auto-provisioning is enabled.
  4. The transfer Job copies data from the Cloud Storage bucket specified in the `GCPDataSource` resource to the destination storage volume.
  5. After the transfer is complete, the PVC is bound to the destination storage volume, making the data available to the workload Pod.



![Data transfer from source data storage and creation of PV for destination storage by using the GKE Volume Populator](https://docs.cloud.google.com/static/kubernetes-engine/images/volume-populator.svg)

## Key benefits

The GKE Volume Populator offers several benefits:

  * **Automated data population** : automatically populate volumes with data from Cloud Storage during provisioning, which helps reduce operational overhead.
  * **Seamless data portability** : move data from object storage to high-performance block storage (Hyperdisk) systems to help optimize for price or performance based on your workload needs.
  * **Simplified workflows** : reduce the need for separate data loading Jobs, or manual intervention to prepare persistent volumes.
  * **Integration with[Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview)**: use IAM-based authentication through [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) to help ensure secure data transfer with fine-grained access control.
  * **Accelerated AI/ML workloads** : quickly preload large datasets, models, and weights directly into high-performance storage to help speed up training and inference tasks.



## Use cases for GKE Volume Populator

You can use GKE Volume Populator to load large training datasets for AI/ML. Imagine you have a multi-terabyte dataset for training a large language model (LLM) stored in a Cloud Storage bucket. Your training Job runs on GKE and requires high I/O performance. Instead of manually copying the data, you can use the GKE Volume Populator to automatically provision a [Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-populator-hdml) volume, and populate it with the dataset from Cloud Storage when the PVC is created. This automated process helps ensure that your training Pods start with immediate, high-speed access to the data.

Here are some more examples where you can use the GKE Volume Populator:

  * Pre-caching AI/ML model weights and assets from Cloud Storage into Hyperdisk ML volumes to accelerate model loading times for inference serving.
  * Migrating data from Cloud Storage to persistent volumes for stateful applications requiring performant disk access.



## What's next

  * [Automate data transfer to Hyperdisk ML by using GKE Volume Populator](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-populator-hdml).
  * [Troubleshooting GKE Volume Populator data transfer issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/troubleshooting-gke-volume-populator). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
