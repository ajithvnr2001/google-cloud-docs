---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/terraform/
title: Provision Agent Platform Workbench resources with Terraform \u00a0|\u00a0 Gemini Enterprise Agent Platform Workbench \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:50.890991+00:00
---

# Provision Agent Platform Workbench resources with Terraform  |  Gemini Enterprise Agent Platform Workbench  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Gemini Enterprise Agent Platform Workbench ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances)
  * [ Notebooks ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/overview)



Send feedback 

#  Provision Agent Platform Workbench resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Agent Platform Workbench.

This page introduces you to using Terraform with Agent Platform Workbench, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Agent Platform Workbench, code examples, and guides for using Terraform to provision Agent Platform Workbench resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Agent Platform Workbench resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Agent Platform Workbench APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Agent Platform Workbench

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Agent Platform Workbench:

Service | Terraform resources | Data sources  
---|---|---  
Agent Platform Workbench | 

  * [`google_workbench_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workbench_instance)
  * [`google_workbench_instance_iam`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workbench_instance_iam)

| [`google_workbench_instance_iam_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/workbench_instance_iam_policy)  
  
## Terraform-based guides for Agent Platform Workbench

The following table lists Terraform-based how-to guides and tutorials for Agent Platform Workbench:

**Guide** | **Details**  
---|---  
[Create a Agent Platform Workbench instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create#terraform) | Create a Agent Platform Workbench instance with a basic configuration.   
[Manage idle shutdown on Terraform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/idle-shutdown#terraform) | Configure the idle shutdown settings on a Agent Platform Workbench instance.   
[Upgrade a custom container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/create-custom-container#upgrade-container) | Change the `container_image` field in the Terraform configuration to update the container payload.   
[Create an instance with specific metadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/instances/manage-metadata#terraform) | Create a Agent Platform Workbench instance with specific metadata.   
  
## Terraform modules and blueprints for Agent Platform Workbench

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to Agent Platform Workbench:

Module or blueprint | Details  
---|---  
[`ai-notebook`](https://github.com/GoogleCloudPlatform/notebooks-blueprint-security) | This module demonstrates how to protect confidential data in a Agent Platform Workbench instance.   
  
## What's next

  * [Terraform code samples for Agent Platform Workbench](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
