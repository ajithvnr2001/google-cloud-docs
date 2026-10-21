---
url: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview/
title: Overview \u00a0|\u00a0 DeployStack \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:55.260472+00:00
---

# Overview  |  DeployStack  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Shell ](https://docs.cloud.google.com/shell/docs)
  * [ DeployStack ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack)
  * [ Guides ](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/overview)



#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

DeployStack is a series of applications that are prebuilt and architected to demonstrate common application architectures. Each DeployStack includes infrastructure Terraform scripts and starter code. When the Terraform scripts run, they build the architecture and deploy the code into that infrastructure. You can then customize the code to suit your application needs.

If DeployStack doesn't have an app to suit your needs, see the [Cloud Architecture Center](https://cloud.google.com/architecture/) for best practices, implementation recommendations, and more to help you design a Google Cloud deployment that matches your business needs. The DeployStack library is still growing, so check back soon for more applications.

## Architecture

[ ![Architecture](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/deploystack_diagram.svg)](https://docs.cloud.google.com/shell/docs/cloud-shell-tutorials/deploystack/images/deploystack_diagram.svg)

Each DeployStack is open-source. They will always contain the following files:

  * **./main.tf** \- the Terraform script that deploys the architecture
  * **./deploystack.json** \- a configuration file for the collection script. 



These files dictate what information DeployStack will request and what infrastructure will be built. 

## How does it work?

Run your DeployStack by taking the following steps:

  1. Follow the "Open in Cloud Shell" link for the stack. 

  2. When the Cloud Shell terminal loads, DeployStack will start up automatically: 

  3. Enter the required settings as prompted. These settings are then configured in the `deploystack.json` file.

The result of this command is an output a file named `terraform.tfvars`. This file gives Terraform the customized settings used to configure the architecture.

  4. Once the `terraform.tfvars` is created, the install routine calls Terraform to apply the contents of `main.tf` and `terraform.tfvars`. 

  5. Upon completion of the install routine, the architecture is deployed in the designated Google Cloud project. 




## Source Code

All of the stacks are released as Open Source code on GitHub. They are here: 

  * [DeployStack Core Project](https://github.com/googlecloudplatform/deploystack)
  * [Cost Sentry](https://github.com/googlecloudplatform/deploystack-cost-sentry)
  * [ETL Pipeline](https://github.com/googlecloudplatform/deploystack-etl-pipeline)
  * [Load Balanced Vms](https://github.com/googlecloudplatform/deploystack-load-balanced-vms)
  * [NoSQL Client Server](https://github.com/googlecloudplatform/deploystack-nosql-client-server)
  * [Ops Agent](https://github.com/googlecloudplatform/deploystack-ops-agent)
  * [Single VM](https://github.com/googlecloudplatform/deploystack-single-vm)
  * [Static Hosting with Domain](https://github.com/googlecloudplatform/deploystack-static-hosting-with-domain)
  * [Storage Event Function App](https://github.com/googlecloudplatform/deploystack-storage-event-function-app)
  * [Three Tier App](https://github.com/googlecloudplatform/deploystack-three-tier-app)
  * [Serverless End-To-End Photo Sharing Application](https://github.com/googlecloudplatform/deploystack-serverless-e2e-photo-sharing-app)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
