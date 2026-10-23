---
url: https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration/
title: Upload a Terraform configuration to a storage bucket \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:42.607965+00:00
---

# Upload a Terraform configuration to a storage bucket  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/upload-terraform-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Upload a Terraform configuration to a storage bucket Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upload a Terraform configuration to a Cloud Storage bucket.

A storage bucket allows you to control access to the configuration. If you are working with a configuration that doesn't need access controls, you can use a public Git repo.

For details about Terraform configurations and Infra Manager, see [Terraform and Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform).

## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Identify the Terraform configuration to upload to a storage bucket.



## Create a storage bucket

Create or identify an existing Cloud Storage bucket to store the Terraform configuration. You can use any storage bucket, but it's common to use a bucket in the same project where you will run Infra Manager.

The storage bucket can be in any project and location. It's common to create this bucket in the same project and location as where you run the Infra Manager service.

To create the storage bucket, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

## Grant read permission for the bucket

If the storage bucket is in a different project from the project where you are running Infra Manager, then you need to ensure that Infra Manager's service account has read permission for the bucket. See [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account) for more details.

If the storage bucket is in the same project as Infra Manager, read permission to the bucket is already enabled.

## Enable Object Versioning for the bucket

We recommend versioning the Terraform configuration so that you can track changes and manage your infrastructure as code.

To version the configuration when it's stored in a Cloud Storage bucket, see [Use Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning).

For more details, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).

## Upload the Terraform configuration

Upload the Terraform configuration to the storage bucket. To choose an upload method, see [Object uploads](https://docs.cloud.google.com/storage/docs/uploads).

## What's next

  * Deploy the Terraform configuration by [Creating a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * Learn more about [Terraform and Google Cloud](https://docs.cloud.google.com/docs/terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
