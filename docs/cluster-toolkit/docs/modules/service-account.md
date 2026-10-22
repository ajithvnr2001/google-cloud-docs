---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/service-account/
title: Create a service account \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:15.769962+00:00
---

# Create a service account  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a service account Stay organized with collections  Save and categorize content based on your preferences. 

The `service-account` module lets you create service accounts for your Google Cloud projects. By using this module, you can automate the creation of service identities and securely assign Identity and Access Management (IAM) roles. This automation ensures that your cluster resources have the exact permissions that they require to operate securely.

For the complete list of inputs and outputs for this module, see the [`service-account` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/project/service-account#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).



### Required roles

To get the permissions that you need to create service accounts and assign roles, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a service account with project roles

The following example demonstrates how to create a service account named `instance_acct` and grant it specific roles across all resources within the project.
    
    
    - id: service_acct
      source: modules/project/service-account
      settings:
        project_id: $(vars.project_id)
        name: instance_acct
        project_roles:
        - logging.logWriter
        - monitoring.metricWriter
        - storage.objectViewer
    

## Use a service account with the startup-script module

When you use the `service-account` module alongside the [`startup-script` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/startup-script), the service account must have read access to the Cloud Storage bucket that contains the scripts. You can provide this access in one of the following ways:

  * **Grant a project-wide role** : Assign a role to the service account that grants read access to Cloud Storage buckets project-wide.
  * **Assign access in`startup-script` module**: Specify the service account as a bucket viewer in the `startup-script` module settings.



The following example demonstrates how to specify the service account as a bucket viewer:
    
    
    - id: service_acct
      source: modules/project/service-account
      settings:
        project_id: $(vars.project_id)
        name: instance_acct
        project_roles:
        - logging.logWriter
        - monitoring.metricWriter
    
    - id: script
      source: modules/scripts/startup-script
      settings:
        bucket_viewers:
        - $(service_acct.service_account_iam_email)
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`service-account` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/project/service-account#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
