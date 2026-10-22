---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-job-template/
title: Create a Batch job template \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:19.658270+00:00
---

# Create a Batch job template  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-job-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a Batch job template Stay organized with collections  Save and categorize content based on your preferences. 

The `batch-job-template` module lets you create and configure job templates for [Batch](https://docs.cloud.google.com/batch/docs/get-started) in your Cluster Toolkit deployments.

By using this module, you can automate the configuration of Compute Engine resources for your Batch workloads. This module generates a local job template file and a Compute Engine instance template. The instance template defines the specific compute settings for your Batch job, such as the network, machine type, image, and startup script. The job template automatically references this instance template. By separating the job definition from the compute environment, you can deploy complex workloads and customize the generated template before you submit it to the Batch API.

When you use this module with the [`batch-login-node` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-login-node), the cluster places the generated job template directly on the login node.

For the complete list of inputs and outputs for this module, see the [`batch-job-template` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/batch-job-template#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `batch-job-template` module, see the [`examples/batch.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/batch.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints that support the `batch-job-template` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select scheduler** menu and then select **Batch**.



### Required roles

To get the permissions that you need to create the Batch job template and instance template, ask your administrator to grant you the following IAM roles on your project: 

  * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Batch job template

The following example demonstrates how to configure a basic Batch job. This configuration defines an `echo` command and assigns a standard machine type. To view the location of the generated file and the instructions for submitting the job, refer to the `instructions` output.
    
    
    - id: batch-job
      source: modules/scheduler/batch-job-template
      use: [network1]
      settings:
        runnable: "echo 'hello world'"
        machine_type: n2-standard-4
      outputs: [instructions]
    
    

For more complex implementations, such as integrating the `batch-job-template` module with the [`filestore` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/filestore-instance) and the [`startup-script` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/startup-script), see the [`examples/batch.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/batch.yaml) example on GitHub.

### Configure network settings

This module supports newly created Virtual Private Cloud (VPC) networks, pre-existing networks, and Shared VPC networks. To define the network for your Batch jobs, include a network module, such as the [`pre-existing-vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-vpc) or the [`vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc) for new Virtual Private Cloud networks, in your blueprint. Then, instruct the `batch-job-template` module to use that network resource by specifying it in the `use` keyword.
    
    
      - id: shared_network
        source: modules/network/pre-existing-vpc
        settings:
          project_id: host-project-id
          network_name: my-shared-vpc
          subnetwork_name: my-shared-subnet
    
      - id: batch-job
        source: modules/scheduler/batch-job-template
        use: [shared_network]
        settings:
          runnable: "echo 'hello from a shared vpc'"
          machine_type: n2-standard-4
        outputs: [instructions]
    

### Configure instance templates

Batch jobs rely on instance templates to define settings like the network, machine type, image, and startup script. By default, the `batch-job-template` module creates an internal instance template that uses a Rocky Linux 9 OS image and supplies it to the Batch job.

Alternatively, you can supply your own instance template to the module by using the `instance_template` setting. You can generate this custom instance template outside of Cluster Toolkit, or you can define it within your blueprint by using a separate module. Supplying a custom instance template is useful when you need to configure a property that the `batch-job-template` module does not natively support.

### Generate a custom instance template

The following example demonstrates how to generate a custom instance template by using a Cloud Foundation Toolkit module. The blueprint supplies this custom template to the Batch job.
    
    
    deployment_groups:
    - group: primary
      modules:
      - id: network1
        source: modules/network/pre-existing-vpc
    
      - id: appfs
        source: modules/file-system/filestore
        use: [network1]
    
      - id: batch-startup-script
        source: modules/scripts/startup-script
        settings:
          runners: ...
    
      - id: batch-compute-template
        source: github.com/terraform-google-modules/terraform-google-vm//modules/instance_template?ref=v7.8.0
        use: [batch-startup-script]
        settings:
          # Boiler plate to work with Cloud Foundation Toolkit
          network: $(network1.network_self_link)
          service_account: {email: null, scopes: ["https://www.googleapis.com/auth/cloud-platform"]}
          access_config: [{nat_ip: null, network_tier: null}]
          # Batch customization
          machine_type: n2-standard-4
          metadata:
            network_storage: ((jsonencode([module.appfs.network_storage])))
          source_image_family: hpc-rocky-linux-9
          source_image_project: cloud-hpc-image-public
    
      - id: batch-job
        source: modules/scheduler/batch-job-template
        settings:
          instance_template: $(batch-compute-template.self_link)
        outputs: [instructions]
    

### Configure MPI

Workloads for tightly coupled high performance computing (HPC) often use the Message Passing Interface (MPI) to communicate between processes and nodes.

When you run MPI workloads by setting the `mpi_mode` variable to `true`, the `batch-job-template` module sets the `task_count_per_node` parameter to `1` by default. In this configuration, the `task_count` variable determines the number of compute nodes that the module provisions.

If the `mpi_mode` variable is not enabled, then the `task_count_per_node` parameter is not forced to `1`. In standard Batch jobs, to maximize resource utilization, you can assign multiple tasks to a single compute instance. The number of compute instances provisioned is calculated by dividing the total task count by the number of tasks per node.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`batch-job-template` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/scheduler/batch-job-template#inputs) page in the Cluster Toolkit GitHub repository.
  * Learn how to create a login node to test and submit your jobs by using the [`batch-login-node` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/batch-login-node).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
