---
url: https://docs.cloud.google.com/security-command-center/docs/terraform/
title: Provision Security Command Center resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:40.133927+00:00
---

# Provision Security Command Center resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Provision Security Command Center resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Security Command Center.

This page introduces you to using Terraform with Security Command Center, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Security Command Center, code examples, and guides for using Terraform to provision Security Command Center resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Security Command Center resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Security Command Center APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Security Command Center

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Security Command Center:

Service | Terraform resources | Data sources  
---|---|---  
Security Command Center (SCC) v2 API | 

  * [`google_scc_v2_folder_mute_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_folder_mute_config)
  * [`google_scc_v2_folder_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_folder_notification_config)
  * [`google_scc_v2_folder_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_folder_scc_big_query_export)
  * [`google_scc_v2_organization_mute_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_mute_config)
  * [`google_scc_v2_organization_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_notification_config)
  * [`google_scc_v2_organization_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_scc_big_query_export)
  * [`google_scc_v2_organization_scc_big_query_exports`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_scc_big_query_exports)
  * [`google_scc_v2_organization_source`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_source)
  * [`google_scc_v2_organization_source_iam`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_organization_source_iam)
  * [`google_scc_v2_project_mute_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_project_mute_config)
  * [`google_scc_v2_project_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_project_notification_config)
  * [`google_scc_v2_project_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_v2_project_scc_big_query_export)

| 

  * [`google_scc_v2_organization_source_iam_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/scc_v2_organization_source_iam_policy)

  
Security Command Center (SCC) [v1 API] | 

  * [`google_scc_event_threat_detection_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_event_threat_detection_custom_module)
  * [`google_scc_folder_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_custom_module)
  * [`google_scc_folder_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_notification_config)
  * [`google_scc_folder_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_folder_scc_big_query_export)
  * [`google_scc_mute_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_mute_config)
  * [`google_scc_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_notification_config)
  * [`google_scc_organization_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_organization_custom_module)
  * [`google_scc_organization_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_organization_scc_big_query_export)
  * [`google_scc_project_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_custom_module)
  * [`google_scc_project_notification_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_notification_config)
  * [`google_scc_project_scc_big_query_export`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_project_scc_big_query_export)
  * [`google_scc_source`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_source)
  * [`google_scc_source_iam`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_source_iam)

| 

  * [`google_scc_source_iam_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/scc_source_iam_policy)

  
Security Command Center Management (SCC) | 

  * [`google_scc_management_folder_security_health_analytics_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_management_folder_security_health_analytics_custom_module)
  * [`google_scc_management_organization_event_threat_detection_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_management_organization_event_threat_detection_custom_module)
  * [`google_scc_management_organization_security_health_analytics_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_management_organization_security_health_analytics_custom_module)
  * [`google_scc_management_project_security_health_analytics_custom_module`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/scc_management_project_security_health_analytics_custom_module)

|   
Compliance Manager | 

  * [`google_cloud_security_compliance_cloud_control`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_security_compliance_cloud_control)
  * [`google_cloud_security_compliance_framework`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_security_compliance_framework)
  * [`google_cloud_security_compliance_framework_deployment`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_security_compliance_framework_deployment)

|   
Cloud Security Scanner [Web Security Scanner] | 

  * [`google_security_scanner_scan_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/security_scanner_scan_config)

|   
Model Armor | 

  * [`google_model_armor_floorsetting`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/model_armor_floorsetting)
  * [`google_model_armor_template`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/model_armor_template)

|   
Security Posture | 

  * [`google_securityposture_posture`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/securityposture_posture)
  * [`google_securityposture_posture_deployment`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/securityposture_posture_deployment)

|   
  
## Terraform-based guides for Security Command Center

The following table lists Terraform-based how-to guides and tutorials for Security Command Center:

**Guide** | **Details**  
---|---  
[Create and manage custom modules for Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-custom-modules-etd) |  This guide explains how to manage custom modules for Event Threat Detection. Custom modules help you detect threats based on parameters that you specify.   
[Enable finding notifications for Pub/Sub](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) |  This guide explains how to send notifications for new and updated Security Command Center findings to a Pub/Sub topic.   
[Create a custom cloud control](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-manage-cloud-controls#create-custom-cloud-control) |  This guide explains how to create custom cloud controls for Compliance Manager. Custom cloud controls let you create your own rules that let you detect possible violations to your security or compliance intent in your Google Cloud environment.   
[Create and deploy frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) |  This guide explains how to create custom frameworks for Compliance Manager and deploy frameworks in your environment. Frameworks are a collection of cloud controls that you want to deploy to your Google Cloud environment to detect possible violations to your security or compliance intent.   
[Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings) |  This guide explains how to reduce the volume of Security Command Center findings that you receive by muting findings.   
[Stream findings to BigQuery for analysis](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query) |  This guide explains how to stream new and updated Security Command Center findings to a BigQuery dataset.   
[Using custom modules with Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/custom-modules-sha-create) |  This guide explains how to manage custom modules for Security Health Analytics. Custom modules help you detect threats based on parameters that you specify.   
[Manage a security posture](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-posture) |  This guide describes how to manage security postures and monitor for changes that are made outside of security postures, which causes drift.   
  
## Terraform modules and blueprints for Security Command Center

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to Security Command Center:

Module or blueprint | Details  
---|---  
[`iam`](https://github.com/terraform-google-modules/terraform-google-iam) |  Manages multiple IAM roles for resources on Google Cloud   
[`org-policy`](https://github.com/terraform-google-modules/terraform-google-org-policy) | Manages Google Cloud organization policies  
  
## What's next

  * [Terraform code samples for Security Command Center](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
