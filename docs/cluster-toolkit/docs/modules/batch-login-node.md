---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-login-node/
title: Create a Batch login node \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:56.129304+00:00
---

# Create a Batch login node  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-login-node/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Batch login node Stay organized with collections  Save and categorize content based on your preferences. 

The `batch-login-node` module lets you create a Compute Engine instance that acts as a login node. Use this login node to test and submit Google Cloud [Batch](https://docs.cloud.google.com/batch/docs/get-started) jobs. We recommend that you use this module alongside the [`batch-job-template` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-job-template).

To help ensure that your login node exactly matches the environment of your batch workload, the `batch-login-node` module requires a reference to a [`batch-job-template` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-job-template) in your blueprint by using the `use` keyword. By defining the job template first, the login node can automatically inherit the following settings:

  * **Network and VPC:** Connects to the exact same Virtual Private Cloud network and subnetwork as your job template.
  * **Machine configuration:** Replicates the same machine type, base image, and mounted file systems as your job template.
  * **Initialization:** Runs the identical startup script to help ensure that all required software is installed.



The module automatically names your login node compute instance by using the format `<deployment_name>-<group_name>-login-001`. Once the login node is running, you can connect to it to test your environment, modify your job template, and submit your jobs to the fully managed Batch service.

For the complete list of inputs and outputs for this module, see the [`batch-login-node` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/batch-login-node#inputs) page in the Cluster Toolkit GitHub repository.

## Limitations

The `batch-login-node` module has the following limitations:

  * **Cluster provisioning:** The `batch-login-node` module doesn't create an active cluster or execute workloads. The module provisions only a single instance that acts as a login node to test and submit jobs.

  * **Testing scope:** The login node lets you verify your environment and single-node setup. Because the login node is a single compute instance, the node does not support testing for multi-node Message Passing Interface (MPI) communication. Batch provisions compute nodes only when you submit a job.




## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for Batch, see the [`examples/batch.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/batch.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support Batch, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Batch**.



### Required roles

To get the permissions that you need to deploy the login node compute instance, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To ensure that the compute instance service account has the necessary permissions to submit Google Cloud Batch jobs from the login node, ask your administrator to grant the [Batch Job Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsAdmin) (`roles/batch.jobsAdmin`) IAM role to the compute instance service account on your project. **Important:** You must grant this role to the compute instance service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the compute instance service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Alternatively, you can grant this role to the service account by executing a command in the gcloud CLI. The following command grants the Batch Job Administrator role to the service account:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:SERVICE_ACCOUNT_EMAIL \
      --role=roles/batch.jobsAdmin
    

## Create a Batch login node

The following example demonstrates how to configure the `batch-login-node` module. To view the location of the generated file and the instructions for accessing the login node and submitting jobs, refer to the `instructions` output.
    
    
    - id: batch-job
      source: modules/scheduler/batch-job-template
      ...
    
    - id: batch-login
      source: modules/scheduler/batch-login-node
      use: [batch-job]
      outputs: [instructions]
    

If the Google Cloud Batch CLI is not available, the `gcloud components update` command updates the gcloud CLI. Alternatively, you can use an image that contains a more recent version of the gcloud CLI.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`batch-login-node` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/batch-login-node#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
