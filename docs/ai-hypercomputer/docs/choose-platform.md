---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/choose-platform/
title: Choose an orchestrator and deployment option \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:33.220723+00:00
---

# Choose an orchestrator and deployment option  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/choose-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Choose an orchestrator and deployment option Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

To efficiently run artificial intelligence (AI) or machine learning (ML) workloads, you must select both a workload orchestrator and a deployment platform. These components function as follows:

  * An orchestrator schedules and runs your jobs.

  * A deployment option manages an orchestrator.




After you identify which GPU infrastructure ( clustered GPUs or general GPUs) to use to run your workloads, follow the guidance in this document to identify the orchestrator and deployment that best fits your workload and level of management.

To review the GPU machine types that you can use to run your workloads, see [GPU machines](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu).

## Compare orchestrators and deployment options

AI Hypercomputer offers several orchestrators and deployment options for your compute instances. These options range from fully managed clusters that let you focus on your workloads, to self-managed environments that offer granular control over how you maintain and update your compute instances.

The following table compares the orchestrators and deployment options that you can use when running AI workloads:

Product | Orchestrator | Technical complexity | Recommended for | Key benefit  
---|---|---|---|---  
Cluster Director | Slurm | Low | AI researchers, Data scientists | Managed lifecycle for Slurm clusters  
Google Kubernetes Engine (GKE) | Kubernetes | Medium to high | ML engineers, Platform engineers | Container orchestration and scaling  
Cluster Toolkit | Slurm, Kubernetes | Medium | ML DevOps, Platform engineers | Validated infrastructure-as-code blueprints  
Compute Engine | Custom / None | High | Infrastructure architects | Granular control over OS and networking  
  
## Choose an orchestrator and deployment option

To choose an orchestrator and deployment option, use the following flowchart:

[ ![Decision tree for selecting an orchestrator and deployment option.](https://docs.cloud.google.com/static/ai-hypercomputer/images/choose-orchestrator.png)](https://docs.cloud.google.com/static/ai-hypercomputer/images/choose-orchestrator.png)

The preceding flowchart asks the following questions:

  1. Do you want cluster orchestration for your workloads?

     * **Yes** : go to question 2.
     * **No** : use Compute Engine.
  2. Do you want to run standard containerized apps?

     * **Yes** : use GKE.
     * **No** : go to question 3.
  3. Do you want Google to manage the cluster lifecycle?

     * **Yes** : use Cluster Director.
     * **No** : use Cluster Toolkit.



## Supported orchestrators

An orchestrator automates cluster management, and eliminates the need to manage each compute instance individually. Orchestrators like Slurm or Kubernetes handle job queueing, resource allocation, and autoscaling.

  * **Slurm** : an open source orchestrator commonly used for AI, ML, and HPC workloads. You can use Slurm with Cluster Toolkit or Cluster Director.

  * **Kubernetes** : an open source container orchestration platform. You can deploy Kubernetes by using GKE directly or through Cluster Toolkit.

  * **Custom or none** : use Compute Engine if you prefer a different orchestrator or want to manage your compute instances without one. This option provides the highest level of control, but requires you to manually set up, maintain, and update your compute instances.




## Supported deployment platforms

After you identify the recommended orchestrator and deployment option for your use case, review their descriptions below to verify that their management levels and features meet your workload requirements.

### Managed and automated platforms

If you want to avoid the overhead of managing a cluster and instead focus on running your workloads, then use one of the following managed platforms:

  * **Cluster Director** : a fully managed service that automates the lifecycle of Slurm clusters. Use Cluster Director to simplify the setup and configuration of your Slurm clusters. Cluster Director automates the lifecycle of your clusters so that you can focus on running your AI, ML, or HPC workloads. For more information, see [ Cluster Director overview](https://docs.cloud.google.com/cluster-director/docs/overview).

  * **GKE** : a managed Kubernetes environment optimized for AI and ML workloads. Use GKE to orchestrate containerized workloads, integrate with specialized Compute Engine hardware, and leverage GKE-specific features like Topology Aware Scheduling (TAS). For more information, see [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).




### Semi-managed and self-managed platforms

If you require granular control over the operating system, kernel configurations, or driver versions, then use a semi-managed or self-managed platform:

  * **Cluster Toolkit** : an open source toolkit that provides validated, customizable blueprints for deploying reproducible AI and ML environments. It offers high flexibility and control using infrastructure-as-code (IaC) principles. For more information, see [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

  * **Compute Engine** : a customizable compute service that provides maximum control for building custom environments from the ground up. While not a standalone orchestrator, Compute Engine serves as the foundation for users who prefer to build and manage their own specialized custom stacks. For more information, see [Compute Engine overview](https://docs.cloud.google.com/compute/docs/overview).




## What's next

  * To obtain capacity, see [Consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  * To deploy your cluster, see [Cluster creation overview](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
