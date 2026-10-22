---
url: https://docs.cloud.google.com/compute/docs/containers/prepare-for-container-agent-shutdown/
title: Prepare for the shutdown of the container startup agent \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:12.725523+00:00
---

# Prepare for the shutdown of the container startup agent  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/containers/prepare-for-container-agent-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Prepare for the shutdown of the container startup agent Stay organized with collections  Save and categorize content based on your preferences. 

The _container startup agent_ (konlet) that deploys containers on Compute Engine instances during VM creation is deprecated.

This document describes how to plan the migration of containers that you created during VM creation to other Google Cloud services.

## General information

What is a container startup agent in Compute Engine?
    The container startup agent lets you [deploy and configure containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers/deploying-containers) instances or on instances in a managed instance group (MIG) during VM creation and launches a Docker container.
Why is the container startup agent deprecated?
    

Based on customer feedback, Google Cloud enhances container deployment options. We have deprecated the container startup agent to enable us to provide you with more flexible options for deploying your containers.

For more information about the options that are deprecated, see [Deprecated options for configuring containers on VMs](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#deprecated-options).

What are the key milestones for this deprecation and what happens if I fail to take action by the deadline?
    

As of **July 31, 2026** , any workflows that rely on the container startup agent or the `gce-container-declaration` instance metadata no longer work.

Starting **July 31, 2027** , Google will discontinue support for the container startup agent and no further updates will be provided for any running VMs that use the `gce-container-declaration` metadata. You will be running the workloads at your own risk and it can affect your workflow.

We recommend that you [migrate containers to alternative solutions](https://docs.cloud.google.com/compute/docs/containers/migrate-containers) well before these dates to ensure a smooth transition.

When will I no longer be able to create new VMs or MIGs with containers deployed directly using the `gce-container-declaration` metadata?
    

12 months from the initial deprecation notification, which is **July 31, 2026**.

When will I no longer be able to run container deployments on VMs or MIGs that use the `gce-container-declaration` metadata?
    

We will stop supporting any workloads deployed using the container startup agent 24 months from the initial deprecation notification, which is **July 31, 2027**.

How does this deprecation impact my Terraform configuration?
    

If you use Terraform or similar automation to create or update VMs or MIGs by explicitly setting the `gce-container-declaration` metadata key, your workflow stops working on **July 31, 2026**. To avoid disruption, update your Terraform configuration to use a startup script for container deployment and remove the dependency on the `gce-container-declaration` metadata key. For detailed instructions, see the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

Does this deprecation mean that Container-Optimized OS images will be deprecated?
    

No, Container-Optimized OS images are not being deprecated. The change is about how containers are deployed on VMs that use Container-Optimized OS. Newer versions of Container-Optimized OS will no longer support [konlet](https://github.com/GoogleCloudPlatform/konlet), the container startup agent that uses the `gce-container-declaration` metadata key to deploy containers. Container-Optimized OS images continue to be available and supported. However, you must update your VM configuration to use a startup script or `cloud-init` to deploy containers instead of relying on the `gce-container-declaration` metadata key.

I use `cloud-init` to run containers on VMs. Am I impacted by this change?
    

No. This deprecation does not impact VMs that are configured using `cloud-init`. You can continue to use `cloud-init` for configuring instances. For more information, see [Using cloud-init with Cloud config](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init_with_the_cloud_config_format).

How do I know if I am impacted by this change?
    

If you are deploying a container on a VM during VM creation using the _container startup agent_ or by specifying the `gce-container-declaration`, you are impacted by this deprecation. To validate if there are any instances impacted in **your project,** run the following gcloud CLI command:
    
    
    gcloud compute instances list --filter="metadata.items.key:gce-container-declaration"
    

This command provides a list of all VM instances in your project that contain the `gce-container-declaration` metadata key. The metadata key uniquely identifies VMs that are in scope of the deprecation. If you are using multiple projects, then run the command across all of the active projects.

For more information about viewing project metadata, see [metadata documentation](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#view-custom-project-wide-metadata).

If you have a _specific instance_ that you want to check, then run the following gcloud CLI command:
    
    
    gcloud compute instances describe VM_NAME
    

Replace VM_NAME with the name of the VM instance. This command provides all the information for a given instance, including the metadata. If you see the `gce-container-declaration` metadata key in the command output, then your VM is impacted by this change.

**Note:** Ensure that you validate and select the right zone when running the command.
Is there a way to prevent the creation of VMs that use the container startup agent?
    

Yes. Organization administrators can enforce the `compute.managed.disableVmsWithContainerStartupAgent` organization policy constraint to disable the creation of resources that use the container startup agent and the `gce-container-declaration` metadata key. You can also enforce this policy in dry-run mode to monitor usage before blocking resource creation. For more information, see [Prevent the creation of VMs that use the deprecated container metadata](https://docs.cloud.google.com/compute/docs/containers/prevent-konlet-vms).

Is there any risk to project security or privacy during the migration?
    

No. Security and privacy are foundational to everything we do at Google. When using our scripts or managed solutions, you have the flexibility to configure specific security and privacy settings to meet your requirements. For more information, see the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

## Alternative solutions

What are the recommended alternative solutions to containers on Compute Engine, and how do I choose the right one for my requirements?
    

You can choose one of the following options to migrate your container:

  * If you want to continue deploying containers on VMs or MIGs, or run containers for testing and development, or run a workload that consists of a single VM, then use [startup scripts](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#startup-scripts) or [cloud-init](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#cloud-init).
  * If you have stateless container applications and small to medium jobs, consider Cloud Run. You can also use [startup scripts](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#startup-scripts).
  * If your container is a batch job that has a definite end state and requires additional computing resources, consider Batch. You can also use [startup scripts](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#startup-scripts).
  * If you need advanced control and scalability or you cannot meet your requirements with the other options, consider [GKE](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#gke).



For detailed guidance and recommendations on migration options, read the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

Why should I consider migrating to a managed service such as Cloud Run, GKE or Batch versus using a startup script?
    

We recommend that you consider migrating to container solutions such as Google Kubernetes Engine, Cloud Run, and Batch. These managed services offer significant advantages over conventional VM-based deployments, including enhanced scalability, flexibility, and advanced management capabilities.

Key benefits include the following:

  * **Reduce management overhead** : As fully managed services,Google Cloud handles the underlying infrastructure (VMs, patching, scaling). This approach frees up valuable staff time and reduces your operational burden.
  * **Automatically scale and ensure elasticity** : These services automatically adjust resources based on demand. This leads to better resource utilization and potential cost savings compared to over-provisioning VMs.
  * **Achieve cost efficiency for idle loads** : Unlike VMs, which incur costs even when idle, managed services can be more cost-effective for applications with fluctuating or low traffic.
  * **Utilize free tier availability** : GKE, Cloud Run, and Batch offer a free tier, allowing you to run smaller workloads or conduct testing at potentially no cost.



For detailed guidance on migration, see the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

What are the cost considerations for each alternative solution, and how do they compare to the current setup?
    

**Container deployment startup scripts or cloud-init** : Using startup scripts or `cloud-init` as a direct replacement does not inherently change your Compute Engine costs. You still pay for the underlying VM resources.

**Managed services** : Moving to services such as Cloud Run or Batch can offer cost savings, especially for applications with variable usage. Unlike VMs that charge even when idle, these managed services can be more efficient. Additionally, free tiers can further reduce costs for smaller, temporary workloads.

For more information, see [Compare the container deployment options](https://docs.cloud.google.com/compute/docs/containers/migrate-containers#compare-container-options). Pricing varies based on the chosen service and your specific configuration. Use the [pricing calculator](https://cloud.google.com/products/calculator) for an accurate estimate.

Does this deprecation mean that Container-Optimized OS images will be deprecated and so if we want to run Dockers on Compute Engine VMs, we'll need to configure our own VM template?
    

**No,** Container-Optimized OS images themselves are not being deprecated. The change is about how containers start on VMs using Container-Optimized OS. Newer Container-Optimized OS versions will no longer support [konlet](https://github.com/GoogleCloudPlatform/konlet), which is the container startup agent that starts containers using the `gce-container-declaration` metadata key. This means Container-Optimized OS images will still be available and supported. However, you must update your VM to use a startup script or `cloud-init` configuration to deploy containers instead of using the `gce-container-declaration` metadata key.

## Migration Process

What is the recommended approach for migrating containers to the alternative solutions?
    

We recommend that you take the following steps toward your migration:

  * Understand your options: Review the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers) to explore alternative ways to run your containers.
  * Plan your migration early: To ensure a smooth transition, start planning the migration of your current container deployments well before **July 31, 2026**.
  * Prepare for new workloads: Ensure that your new container workloads are ready to run on alternative solutions by **July 31, 2026** , as direct deployment of containers to VMs or MIGs is no longer possible.
  * Final migration deadline: Ensure that all your existing container workloads are migrated to alternative solutions by **July 31, 2027** , when the direct deployment method will be fully retired.


Am I required to migrate to one of the recommended solutions or are there alternatives that I can use?
    

We support your flexibility to adopt any solution that aligns with your business needs and is actively supported. Resources such as the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers) are available to help you choose the most suitable option.

Is data backup or export required as part of the migration process?
    

While performing a data backup or export is always a critical best practice for data safety and business continuity, it is not a necessary step for this migration process.

How much time will it take me to migrate to one of the alternatives, and are there factors that could affect my time commitment?
    

**Container deployment startup script** : Initial setup and testing using startup scripts should take around 1-2 hours. Subsequent deployments should only take a few minutes each.

**Managed services** : Opting for Google Cloud solutions such as Cloud Run, Batch, or GKE, which are serverless and fully managed PaaS offerings, might involve a greater upfront investment of time and effort. This is due to the fundamental change from a VM-centric (IaaS) approach where you manage the infrastructure, to a PaaS model where the platform handles much of this. This adaptation may necessitate changes to your application, such as ensuring it's stateless, but the long-term benefits can include substantial gains in operational efficiency, scalability, and cost-effectiveness.

For guidance on this transition, see the [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

If I choose to migrate to an alternative, does it involve any interruptions or downtime for Google Cloud projects, VMs, services, and apps?
    

Generally, the transition to the recommended alternative solution is designed to be a zero-downtime process.

For migration of long-running containers on Compute Engine VMs, in order to avoid disruptions, we recommend setting up new VMs with the alternative configuration and switching over the traffic once they are tested.

How does this migration impact my Terraform configuration?
    

If you are using Terraform or similar automation to create or update VMs or MIGs with containers by explicitly setting the `gce-container-declaration` metadata key, your workflow stops working on **July 31, 2026**. To avoid disruption, you must update your configuration to include a startup script for container deployment and remove the dependency on the `gce-container-declaration` metadata key. For detailed instructions on how to implement this change, see [Migrate containers that were deployed on VMs during VM creation](https://docs.cloud.google.com/compute/docs/containers/migrate-containers).

## Getting support

Who should I reach out to in Compute Engine if I have questions about the migration process?
    If you have any questions or require assistance, contact [Google Cloud Support](https://support.google.com/).
What resources are available to support me with the migration and provide technical guidance?
    This FAQ, a [migration guide](https://docs.cloud.google.com/compute/docs/containers/migrate-containers) and [Google Cloud Support](https://support.google.com/) are available to support you with the migration process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
