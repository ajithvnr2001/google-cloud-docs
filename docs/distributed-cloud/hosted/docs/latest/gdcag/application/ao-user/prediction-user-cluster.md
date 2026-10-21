---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/prediction-user-cluster/
title: Create the prediction cluster \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:01:22.358032+00:00
---

# Create the prediction cluster  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/prediction-user-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create the prediction cluster Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

You must deploy your prediction custom resources in the prediction cluster that the Infrastructure Operator (IO) creates for you. The operator creates prediction workloads in this same cluster.

To create the prediction cluster, work with the IO to associate your prediction project and allocate the node pools needed for online predictions in Google Distributed Cloud (GDC) air-gapped.

**Important:** Only one prediction cluster can exist in each organization. However, the IO can attach and associate multiple projects to the cluster to separate and organize the endpoints.

## Before you begin

To set up a project and deploy prediction resources in the prediction cluster, you must have the necessary permissions.

### Request IAM organization roles

Contact your Organization IAM Admin to request the following role:

  * **Project Creator** (`project-creator`): create a new project in your organization.



### Request IAM project roles

Contact your Project IAM Admin to request the following role in your project namespace:

  * **Vertex AI Prediction Admin** (`vertex-ai-prediction-admin`): manage resources used to deploy models with Online Prediction.



For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

## Request a prediction cluster

To create a prediction cluster, perform the following steps:

  1. Identify the project in your organization that you want to associate with the new cluster for online predictions.

To create a project, see [Set up a project for Vertex AI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-set-up-project). You need your project ID when making API calls.

  2. From [the list of available machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#available-machine-types) in Distributed Cloud, choose the machine type for the nodes that your workloads need in the cluster.

The machine type you choose depends on your prediction model size and complexity and determines the compute and graphic processing unit (GPU) resources your IO provides to the cluster. Follow node selection recommendations when selecting the machine type for your nodes.

  3. Email the IO using the prediction cluster case template to open a case and address your request to create the cluster.

  4. If necessary, communicate with the IO until they finish creating the prediction cluster associated with your project and assigning the appropriate node pools within the cluster.




After completing cluster provisioning, the prediction cluster is ready for online predictions.

## Node selection recommendations

When the IO creates node pools in a cluster, they assign one of the [available machine types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines#available-machine-types) in Distributed Cloud to provide a predefined set of resources for the worker nodes. Depending on the model size and complexity, you require different computing performances and, consequently, a specific amount of CPU, memory, and GPU. You must provide these details in your communication with the IO when you want to create a prediction cluster.

**Important:** Distributed Cloud uses virtualized GPUs in the cluster, which means you get a one-seventh slice of the GPU you have for each requested accelerator count. For example, if you ask for an accelerator count of three in the [resource pool](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model#resource-pool), you get three-sevenths of a GPU.

When you determine with the IO the machine type for node pools that you require in the prediction cluster, you must adhere to the following practices:

  * Distributed Cloud adds computing overhead to the nodes for mandatory system components. Therefore, you must choose a larger machine type for your node pools than the one you intend to use in the [resource pool](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model#resource-pool) for your models.
  * Choose the solution that provides the minimum memory and computing resources necessary for your requirements. For example, if your model requires eight vCPUs, choose the `n2-highcpu-8-gdc` machine type, the smallest solution with eight vCPUs and 8 GB of memory in Distributed Cloud.
  * As you progress, consider higher performance solutions only if smaller solutions are not adequate for your needs and the size and complexity of the model. It's crucial to adhere to the principle of least privilege, using only the resources you need to execute your specific workflow. This responsible approach ensures considerate use of resources in the Distributed Cloud environment.
  * Only choose solutions that have GPUs if you require them for your model.
  * If your model requires GPUs, consider the `a2-highgpu-1g-gdc` machine type, the smallest solution providing GPUs.



## Prediction cluster case template

Use the following template to send an email to your IO. The email opens a case to create the prediction cluster that you need for online predictions.
    
    
    Good day,
    
    I need to create a prediction cluster and associate it with a project in my organization to use online predictions.
    
    Please use the following information for the creation of the cluster:
    
    - **Cluster name:** vtx-ai-prediction
    - **Name of the organization:** [Specify your organization's name.]
    - **Project name:** [Specify the name of your project to associate with the prediction cluster.]
    - **Machine type for the node pool:** [Specify the machine type you chose from the list of available machine types for the cluster nodes based on node selection recommendations. Please note that the IO can respond with a different suggestion based on your needs.]
    - **Compute resources:** [Optionally, if you know how many compute resources your workloads need, describe them in this field.]
    - **Memory resources:** [Optionally, if you know how many memory resources your workloads need, describe them in this field.]
    - **GPU resources:** [Optionally, if you know how many GPU resources your workloads need, describe them in this field.]
    
    **Note for IO:** Review the instructions to create the prediction cluster in the following section of the documentation: Operator > Configure the deployment > Create the Prediction cluster
    
    Thank you,
    [Your name]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
