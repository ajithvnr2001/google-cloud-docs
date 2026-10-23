---
url: https://docs.cloud.google.com/storage/docs/terraform-for-cloud-storage/
title: Provision Cloud Storage resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:09.350132+00:00
---

# Provision Cloud Storage resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/terraform-for-cloud-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Provision Cloud Storage resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Cloud Storage.

This page introduces you to using Terraform with Cloud Storage, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Cloud Storage, code examples, and guides for using Terraform to provision Cloud Storage resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Cloud Storage resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Cloud Storage APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Cloud Storage

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Cloud Storage:

Service | Terraform resources | Data sources  
---|---|---  
Cloud Storage Terraform service: `Cloud Storage` | 

  * [`google_storage_anywhere_cache`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache)
  * [`google_storage_bucket`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket)
  * [`google_storage_bucket_access_control`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_access_control)
  * [`google_storage_bucket_acl`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_acl)
  * [`google_storage_bucket_iam`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_iam)
  * [`google_storage_bucket_object`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object)
  * [`google_storage_default_object_access_control`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_default_object_access_control)
  * [`google_storage_default_object_acl`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_default_object_acl)
  * [`google_storage_folder`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_folder)
  * [``google_storage_hmac_key``](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_hmac_key)
  * [`google_storage_managed_folder`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_managed_folder)
  * [`google_storage_managed_folder_iam`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_managed_folder_iam)
  * [`google_storage_notification`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_notification)
  * [`google_storage_object_access_control`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_object_access_control)
  * [`google_storage_object_acl`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_object_acl)

| 

  * [`google_storage_bucket`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_bucket)
  * [`google_storage_bucket_iam_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_bucket_iam_policy)
  * [`google_storage_bucket_object`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_bucket_object)
  * [`google_storage_bucket_object_content`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_bucket_object_content)
  * [`google_storage_bucket_objects`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_bucket_objects)
  * [`google_storage_buckets`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_buckets)
  * [`google_storage_object_signed_url`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_object_signed_url)
  * [`google_storage_project_service_account`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_project_service_account)

  
Storage Intelligence Terraform service: `Cloud Storage Control` | 

  * [`google_storage_control_folder_intelligence_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_control_folder_intelligence_config)
  * [`google_storage_control_organization_intelligence_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_control_organization_intelligence_config)
  * [`google_storage_control_project_intelligence_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_control_project_intelligence_config)

| 

  * [`google_storage_control_folder_intelligence_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_control_folder_intelligence_config)
  * [`google_storage_control_organization_intelligence_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_control_organization_intelligence_config)
  * [`google_storage_control_project_intelligence_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_control_project_intelligence_config)

  
Storage batch operations feature of Storage Intelligence Terraform service: `Cloud Storage Batch Operations` | 

  * [`google_storage_batch_operations_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_batch_operations_job)

| -  
Storage Insights feature of Storage Intelligence Terraform service: `Cloud Storage Insights` | 

  * [`google_storage_insights_dataset_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_insights_dataset_config)
  * [`google_storage_insights_report_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_insights_report_config)

| 

  * [`google_storage_insights_dataset_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/storage_insights_dataset_config)

  
  
## Terraform-based guides for Cloud Storage

The following table lists Terraform-based how-to guides and tutorials for Cloud Storage:

**Guide** | **Details**  
---|---  
[Quickstart: use Terraform to create a bucket and upload an object](https://docs.cloud.google.com/storage/docs/terraform-create-bucket-upload-object) | This quickstart shows how to get started with Terraform by creating a Terraform configuration file that provisions a storage bucket and uploads a sample object to the bucket. |   
[Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#terraform) | This guide explains how to create a bucket.  
[Get bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata#get-bucket-properties-terraform-sample) | This guide explains how to view the metadata of a bucket.  
[Upload objects](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) | This guide explains how to upload objects to a bucket from your local file system.  
[Get object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view) | This guide explains how to view the metadata of an object.  
[Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles#set) | This guide explains how to set the lifecycle configuration for a bucket.  
[Configure Pub/Sub notifications](https://docs.cloud.google.com/storage/docs/reporting-changes#enabling) | This guide explains how to configure your bucket to send notifications about object changes to a Pub/Sub topic.  
[Create HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys#create) | This guide explains how to create hash-based message authentication code (HMAC) keys for service accounts in your project.  
[Make data public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#buckets) | This guide explains how to make all objects in a bucket readable to everyone on the public internet.  
[Host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website) | This guide explains how to configure a bucket to host a static website for a domain that you own.  
  
## Terraform modules and blueprints for Cloud Storage

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to Cloud Storage:

Module or blueprint | Details  
---|---  
[`terraform-google-cloud-storage`](https://github.com/terraform-google-modules/terraform-google-cloud-storage) | This module creates one or more Cloud Storage buckets and assigns basic permissions on them to arbitrary users.  
  
## What's next

  * [Terraform code samples for Cloud Storage](https://docs.cloud.google.com/docs/samples?language=terraform&product=cloudstorage)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
