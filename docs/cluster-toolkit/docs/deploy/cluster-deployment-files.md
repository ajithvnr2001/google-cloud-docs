---
url: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/cluster-deployment-files/
title: Cluster deployment files \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:43:25.570273+00:00
---

# Cluster deployment files  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/deploy/cluster-deployment-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Cluster deployment files Stay organized with collections  Save and categorize content based on your preferences. 

Cluster deployment files let you reuse your infrastructure blueprints across environments by overriding parameters instead of duplicating code. This document describes the configuration precedence and structure of cluster deployment files.

## About cluster deployment files

[Cluster blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint) define infrastructural patterns that you can deploy repeatedly for different workloads or environments. Deployment files act as an overlay mechanism that modifies a blueprint's configuration without altering the underlying Terraform and Packer modules.

Using deployment files can help you do the following:

  * Ensure unique names for each individual deployment.
  * Specify target environments, such as changing the `project_id`, `region`, or `zone`.
  * Override backend configuration defaults for Terraform state management.



## Supported configuration parameters

You can specify variables and default backend settings in the deployment file by using a YAML structure.

The following example shows the parameters that can be configured in a deployment file:
    
    
    vars:
      project_id: PROJECT_ID
      deployment_name: DEPLOYMENT_NAME
      region: REGION
      zone: ZONE
    
    terraform_backend_defaults:
      type: gcs
      configuration:
        bucket: BUCKET_NAME
    

Replace the following:

  * `PROJECT_ID`: The unique identifier for your target Google Cloud project.
  * `DEPLOYMENT_NAME`: A custom name for your cluster deployment.
  * `REGION`: The Google Cloud region where you want to deploy your cluster resources.
  * `ZONE`: The specific Google Cloud zone within the region for your deployment.
  * `BUCKET_NAME`: The name of the Cloud Storage bucket used to store your remote Terraform state.



## Variable precedence rules

When variables are defined in multiple locations, Cluster Toolkit resolves conflicts using a strict order of precedence.

The following precedence rules apply from highest priority to lowest priority:

  1. **Command-line flags:** Values supplied using the `--vars` flag of the [`gcluster create`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-create) or [`gcluster deploy`](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) commands have the highest precedence.
  2. **Deployment files:** If a variable is specified in the deployment file, then it takes precedence over the blueprint definition.
  3. **Blueprint defaults:** Any variable not supplied by a command-line flag or a deployment file defaults to the value defined in the cluster blueprint.



If `terraform_backend_defaults` is set in a deployment file, then it replaces all backend default settings declared in the blueprint.

## What's next

  * Learn how to deploy clusters in the [Deploy a cluster with blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/deploy-cluster-overview).
  * Review the [Module overview](https://docs.cloud.google.com/cluster-toolkit/docs/modules/overview) to understand how modules extend blueprints.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
