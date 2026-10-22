---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview/
title: Modules \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:16.184802+00:00
---

# Modules  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Modules Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of modules for Cluster Toolkit. Modules are reusable, configurable building blocks that define the infrastructure and software resources in your Cluster Toolkit deployment. Modify blueprints by configuring modules for compute, networking, storage, and scheduling in your blueprint file.

## Example module

Modules are declared in YAML format in the [`deployment_groups`](https://docs.cloud.google.com/docs/setup/cluster-blueprint#design-blueprint) section of your blueprint file.

For example, the following code snippet configures a primary deployment group with a Compute Engine instance module:
    
    
    deployment_groups:
    - group: primary
      modules:
      - id: compute_nodes
        source: modules/compute/vm-instance
        settings:
          machine_type: c2-standard-60
    

Use modules to create flexible, repeatable deployments that adhere to infrastructure-as-code best practices.

## Module structure

The following diagram shows the structure of a Cluster Toolkit blueprint. A deployment group within the blueprint acts as a container for your infrastructure modules, grouping together resources such as compute instances, networks, file systems, and schedulers:

![A Cluster Toolkit blueprint structure showing a deployment group containing
compute instance, network, file system, and scheduler
modules.](https://docs.cloud.google.com/static/cluster-toolkit/images/blueprint-example.png)

**Figure 1.** Modules are organized within a deployment group in a cluster blueprint.

## Module categories

Provision and manage your cluster resources efficiently by using different categories of modules. These modules provide the building blocks to define and deploy infrastructure optimized for demanding workloads, such as high performance computing (HPC) or AI/ML training workloads.

Modules let you configure the following aspects of your cluster deployment:

  * **Compute resources:** define compute instances, autoscaling groups, GKE node pools, and specialized Slurm partitions and node sets.
  * **Scheduler deployment:** configure workload managers, including controller and login nodes, to manage job queues.
  * **File systems:** provision shared, high-performance storage solutions for data-intensive applications.
  * **Networking:** establish connectivity, configure firewalls, and integrate your cluster into existing VPC networks.
  * **Observability:** monitor cluster health and performance.
  * **Software and system setup:** customize VM images and automate system configuration tasks.



## What's next

  * To start configuring modules, see [Supported modules](https://docs.cloud.google.com/cluster-toolkit/docs/modules/module-list-overview).
  * To see how these modules work together in practice, view the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog).
  * For a complete list of modules, including experimental and community modules, see the [Cluster Toolkit GitHub repository](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
