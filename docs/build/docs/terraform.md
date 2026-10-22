---
url: https://docs.cloud.google.com/build/docs/terraform/
title: Provision Cloud Build resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:06.583596+00:00
---

# Provision Cloud Build resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Provision Cloud Build resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Cloud Build.

This page introduces you to using Terraform with Cloud Build, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Cloud Build, code examples, and guides for using Terraform to provision Cloud Build resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Cloud Build resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Cloud Build APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Cloud Build

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Cloud Build:

Cloud Build service | Terraform Resources | Data sources  
---|---|---  
Cloud Build v1 | 

  * `[google_cloudbuild_bitbucket_server_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuild_bitbucket_server_config)`
  * `[google_cloudbuild_trigger](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloudbuild_trigger)`
  * `[google_cloudbuild_worker_pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuild_worker_pool)`

| `[google_cloudbuild_trigger](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloudbuild_trigger)`  
Cloud Build v2 | 

  * `[google_cloudbuildv2_connection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuildv2_connection)`
  * `[IAM policy for Cloud Build v2 Connection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuildv2_connection_iam)`
  * `[google_cloudbuildv2_repository](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuildv2_repository)`

| `[google_cloudbuildv2_connection_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloudbuildv2_connection_iam_policy)`  
  
## Terraform-based guides for Cloud Build

The following table lists Terraform-based how-to guides and tutorials for Cloud Build:

**Guide** | **Details**  
---|---  
[Connect to a GitHub repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github?generation=2nd-gen#terraform) | This guide explains how to connect a GitHub repository to Cloud Build using Terraform.  
[Connect to a GitHub Enterprise host](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-host-github-enterprise?generation=2nd-gen#terraform) | This guide explains how to connect a GitHub Enterprise host to Cloud Build using Terraform.  
[Connect to a GitHub Enterprise repository](https://docs.cloud.google.com/build/docs/automating-builds/github/connect-repo-github-enterprise?generation=2nd-gen#terraform) | This guide explains how to connect a GitHub Enterprise repository to Cloud Build using Terraform.  
[Connect to a GitLab Enterprise Edition host](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-host-gitlab-enterprise-edition#terraform) | This guide explains how to connect a GitLab Enterprise Edition host to Cloud Build using Terraform.  
[Connect to a GitLab Enterprise Edition repository](https://docs.cloud.google.com/build/docs/automating-builds/gitlab/connect-repo-gitlab-enterprise-edition#terraform) | This guide explains how to connect a GitLab Enterprise Edition repository to Cloud Build using Terraform.  
[Connect to a Bitbucket Data Center host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-data-center?generation=2nd-gen#terraform) | This guide explains how to connect a Bitbucket Data Center host to Cloud Build using Terraform.  
[Connect to a Bitbucket Data Center repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-data-center?generation=2nd-gen#terraform) | This guide explains how to connect a Bitbucket Data Center repository to Cloud Build using Terraform.  
[Connect to a Bitbucket Cloud host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-cloud#terraform) | This guide explains how to connect a Bitbucket Cloud host to Cloud Build using Terraform.  
[Connect to a Bitbucket Cloud repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-cloud#terraform) | This guide explains how to connect a Bitbucket Cloud repository to Cloud Build using Terraform.  
[Deploy to Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine) | This guide explains how to perform zero-downtime blue-green deployments on Compute Engine Managed Instance Groups (MIGs) using Cloud Build and Terraform.  
[Create a Developer Connect push trigger](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuild_trigger#example-usage---cloudbuild-trigger-developer-connect-push) | This code sample shows how to create a Developer Connect push trigger using Terraform.  
[Create a Developer Connect pull trigger](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudbuild_trigger#example-usage---cloudbuild-trigger-developer-connect-pull) | This code sample shows how to create a Developer Connect pull trigger using Terraform.  
  
## Terraform modules and blueprints for Cloud Build

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to Cloud Build:

Module or blueprint | Details  
---|---  
[Secure CI/CD pipeline](https://github.com/GoogleCloudPlatform/terraform-google-secure-cicd) | This module enables Google Cloud customers to quickly deploy a secure CI/CD pipeline, implementing many of the functions outlined in [Shifting left on security](https://docs.cloud.google.com/solutions/shifting-left-on-security).   
[`terraform-google-bootstrap`](https://github.com/terraform-google-modules/terraform-google-bootstrap) | This module helps bootstrap a Google Cloud organization, creating all the required resources and permissions to start using the Cloud Foundation Toolkit (CFT). For users who want to use Cloud Build and Cloud Source Repositories for foundations code, this module contains a submodule that bootstraps all the required resources.  
  
## What's next

  * [Terraform code samples for Cloud Build](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
