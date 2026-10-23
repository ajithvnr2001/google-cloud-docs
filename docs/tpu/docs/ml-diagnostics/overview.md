---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/overview/
title: ML Diagnostics platform \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:20.007721+00:00
---

# ML Diagnostics platform  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ML Diagnostics platform

**Note:** Google Cloud ML Diagnostics only supports JAX on TPUs.

Google Cloud ML Diagnostics is an end-to-end managed platform for optimizing, monitoring, and diagnosing AI and ML workloads on Google Cloud. Use ML Diagnostics to monitor workloads, as well as collect and visualize all workload metrics, configurations, and profiles within a single platform. ML Diagnostics is applicable to both training and inference workloads, and is compatible with all orchestrators on Cloud TPU, including Google Kubernetes Engine (GKE) and custom orchestrators. ML Diagnostics includes the following features:

  * **Workload monitoring** : Automatically monitor and diagnose AI/ML workloads running on GKE TPUs. For each GKE job, ML Diagnostics Workload Monitoring automatically creates a Machine Learning run, monitors TPU duty cycle across the workload, detects events affecting the workload, and analyzes different layers of the workload -- such as infra, orchestrator and framework -- to help determine the potential causes of the event.
  * **Machine learning runs:** Use ML Diagnostics to create and register your machine learning runs through Google Cloud CLI, or integrate the ML Diagnostics SDK with your workload. You can create and register runs automatically with workload monitoring, and deploy managed [XProf](https://openxla.org/xprof) instances with your machine learning runs, and collect and manage workload metrics, configurations, and profile sessions.
  * **gcloud CLI experience:** Use the ML Diagnostics APIs through gcloud CLI to register and manage runs, deploy managed XProf resources, visualize profile sessions in storage buckets, and trigger profile captures from the CLI. You can also list all events detected by workload monitoring and obtain analyzer details for these events through the CLI or API.
  * **Python SDK** : Use the open-source [ML Diagnostics SDK](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics) integrated with ML workloads for a complete ML workload diagnostics experience. Monitor workloads and collect and manage workload metrics, configurations, and profiles on Google Cloud.
  * **Managed profiling** : ML Diagnostics deploys a managed instance of [XProf](https://openxla.org/xprof) with a scalable backend into associated accounts, enabling the fast loading of large profiles. It supports multiple users simultaneously accessing profiles, and contains built-in features like multi-host profiling and on-demand profiling.
  * **Workload metrics** : Track workload metrics, including model quality, model performance, and system metrics. With workload monitoring, you can get system metrics associated with the workload without integrating the SDK.
  * **Workload configuration management** : Track workload configurations, including software configurations, system configurations, and user-defined configurations.
  * **Visualizations in Cluster Director and GKE** : Visualize metrics, configurations, and profiles in [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) and [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) in the Google Cloud console.
  * **Link sharing** : Collaborate using shareable links with information on machine learning runs, workload monitoring, metrics, and profiles.



## User paths

You can use the ML Diagnostics platform automatically with workload monitoring for all GKE jobs, or integrate the SDK with your workload for the complete ML workload diagnostics experience. You can interact with the ML diagnostics system through Google Cloud console or the CLI. Workload monitoring is automatically available for all workloads deployed with GKE on TPUs.

With the CLI, you can use ML Diagnostics gcloud CLI to create or modify a machine learning run, and deploy the managed XProf resources. With the ML Diagnostics SDK, the SDK needs to be integrated into your ML workload to collect and manage workload metrics and configurations, and deploy managed XProf resources.

To get started, use one of the following guides:

  * [Monitor workloads](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/workload-monitoring)
  * [Get started with SDK](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/sdk)
  * [Get started with CLI](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/cli)



## Managed profiling with XProf

You can get a managed profiling experience with [XProf](https://openxla.org/xprof) when you use either the CLI or SDK. XProf is an open-source profiling and performance analysis tool for machine learning workloads and part of the [OpenXLA](https://openxla.org/) ecosystem.

The benefits of a managed profiling experience compared to a self-hosted profiling experience include:

  * No required setup of XProf or other dependencies.
  * Better security and protection from vulnerabilities.
  * Shareable links for collaboration.
  * Faster loading of large profiles.
  * Support for multiple users simultaneously accessing profiles with automatic scaling of resources based on link access load.
  * Built-in features like multi-host profiling and on-demand profiling.
  * Load multiple profile sessions across multiple runs with the same managed XProf instance.
  * There is no charge for the managed XProf resources deployed by the ML Diagnostics platform, making managed XProf more cost effective than self-hosting XProf.



## Prerequisites

Before using ML Diagnostics, enable the Cluster Director API and add the required IAM permissions. If you are using GKE, workload monitoring is already enabled. However, the ML Diagnostics SDK and on-demand profiling, requires additional GKE artifacts and configuration of your GKE cluster. For more information, see [Set up GKE](https://docs.cloud.google.com/tpu/docs/ml-diagnostics/gke).

### Enable Cluster Director API

**Note:** The Cluster Director API is not related to [TPU Cluster Director](https://docs.cloud.google.com/tpu/docs/all-capacity-overview). Google Cloud ML Diagnostics relies on the [Cluster Director API](https://docs.cloud.google.com/cluster-director/docs/overview) for accessing gcloud CLI commands; for collecting metrics, configurations, and profiles in the platform; and for accessing the Google Cloud console.

You don't need to use Cluster Director for deploying and managing your clusters in order to use the ML Diagnostics product. ML Diagnostics works with clusters managed by GKE, Cluster Director, or custom orchestrators. ML Diagnostics is part of the Cluster Director family of APIs, but doesn't depend on users using the Cluster Director product itself.

For more information about enabling Cluster Director API, see [Enabling an API in your Google Cloud project](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).

### IAM permissions

The Google Cloud service account used by your workload requires the following IAM roles assigned on the project:

  * `roles/hypercomputecluster.editor`: For full access to create and manage `MLRun` resources and view the user interface.
  * `roles/logging.logWriter`: To write logs and metrics to Cloud Logging.
  * `roles/storage.objectUser`: To save profiles to the Cloud Storage bucket specified in `machinelearning_run`.



You can also create [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that assign users a subset of APIs needed for ML Diagnostics. Since users don't need to use Cluster Director for managing clusters, you only need to assign the following permissions:

  * `hypercomputecluster.locations.get`
  * `hypercomputecluster.locations.list`
  * `hypercomputecluster.machineLearningRuns.create`
  * `hypercomputecluster.machineLearningRuns.delete`
  * `hypercomputecluster.machineLearningRuns.get`
  * `hypercomputecluster.machineLearningRuns.list`
  * `hypercomputecluster.machineLearningRuns.update`
  * `hypercomputecluster.operations.cancel`
  * `hypercomputecluster.operations.delete`
  * `hypercomputecluster.operations.get`
  * `hypercomputecluster.operations.list`
  * `resourcemanager.projects.get`
  * `Resourcemanager.projects.list`



For workloads on Google Kubernetes Engine, use [Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to associate a Kubernetes Service Account with a Google Cloud service account that has been granted the required roles. Pods running on the [host network](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#hosts-namespaces) (`hostNetwork: true`) don't use Workload Identity Federation for GKE. For these cases, see [Alternatives to Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#alternatives_to).

## Pricing

You are charged for the storage of metrics through Cloud Logging, and the storage of profiles through Cloud Storage. There is no need to enable any extra billing for these services when using ML Diagnostics platform. There is no charge for the managed XProf resources deployed by ML Diagnostics platform.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
