---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/terraform/
title: Terraform overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:11.097898+00:00
---

# Terraform overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Terraform overview Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. For Google Distributed Cloud (GDC) air-gapped, you must use the [Kubernetes Provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) to provision resources since there is no specific GDC air-gapped provider for Terraform.

GDC resources can be managed by the Kubernetes Provider with the full lifecycle management of Kubernetes resources.

Operation | Terraform Provider  
---|---  
Create |   
  
Kubernetes Provider  
Read  
Update  
Delete | N/A, use `terraform destroy`  
  
## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your GDC project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your GDC resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.

  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.

  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding GDC air-gapped APIs in the background.

     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.

     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.

        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.

        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.




## Terraform resources for GDC air-gapped

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects.

GDC air-gapped is built on top of Kubernetes. Besides the core Kubernetes APIs like `Node`, `PersistentVolume`, and `Service`, it also supports the `CustomResourceDefinition` API. By using custom resource definitions, GDC-specific APIs are built for representing the GDC air-gapped infrastructure. 

The following table lists the Terraform resources available for GDC air-gapped:

Terraform Resources | Data sources  
---|---  
`[kubernetes_manifest](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/manifest)` | 

  * `[kubernetes_resource](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/data-sources/resource)`
  * `[kubernetes_resources](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/data-sources/resources)`

  
  
## What's next

  * [Configure Terraform](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform)

  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)

  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)

  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
