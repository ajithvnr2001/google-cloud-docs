---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-on-prem-api/
title: Upgrade an admin or user cluster using GKE On-Prem API clients \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:30.670445+00:00
---

# Upgrade an admin or user cluster using GKE On-Prem API clients  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-on-prem-api/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Upgrade an admin or user cluster using GKE On-Prem API clients Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade-on-prem-api)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-on-prem-api)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page explains how to use the Google Cloud console or the Google Cloud CLI to upgrade a Google Distributed Cloud admin or user cluster that is enrolled in the GKE On-Prem API. If you created your user cluster using Terraform, you can use Terraform to upgrade the user cluster. For upgrade requirements, best practices, and additional information about the upgrade process, review [Upgrade best practices](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-best-practices) and [Lifecycle and stages of cluster upgrades](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/upgrade-lifecycle) before proceeding.

## What is the GKE On-Prem API?

The GKE On-Prem API is a Google Cloud-hosted API that lets you manage the lifecycle of your on-premises clusters using Terraform and standard Google Cloud tools. The GKE On-Prem API runs in Google Cloud's infrastructure. Terraform, the Google Cloud console, and the Google Cloud CLI are clients of the API, and they use the API to create, update, upgrade, and delete clusters in your data center. If you created the cluster using a standard client, the cluster is _enrolled_ in the GKE On-Prem API, which means you can use the standard clients to manage the lifecycle of the cluster (with some exceptions). If you created the cluster using `bmctl`, you can [enroll the cluster in the GKE On-Prem API](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/enroll-cluster), which lets you use the standard clients. 

## Before you begin

### Set up the gcloud CLI

To use the gcloud CLI or Terraform to upgrade a cluster:

  1. Ensure that you have [the latest version of the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). Update the gcloud CLI components, if needed:
         
         gcloud components update
         




### IAM requirements

If you aren't a project owner, you must be granted the Identity and Access Management role `roles/gkeonprem.admin` on the Google Cloud project that the cluster was created in. For details on the permissions included in this role, see [GKE on-prem roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem) in the IAM documentation.

To use the console to upgrade the cluster, at a minimum, you need the following:

  * `roles/container.viewer`. This role lets users view the GKE Clusters page and other container resources in the console. For details about the permissions included in this role, or to grant a role with read/write permissions, see [Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/roles-permissions/container) in the IAM documentation.

  * `roles/gkehub.viewer`. This role lets users view clusters in the console. For details about the permissions included in this role, or to grant a role with read/write permissions,see [GKE Hub roles](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub) in the IAM documentation.




## Version requirements

It takes about 7 to 10 days after a Google Distributed Cloud release for the version to be available in the GKE On-Prem API.

You can upgrade directly to a version that is in the same minor release or the next minor release. For example, you can upgrade from 1.16.1 to 1.16.2, or from 1.15.1 to 1.16.2. Upgrading to a version that is more than one minor release later than the installed version isn't allowed.

An admin cluster can manage user clusters that are on the same or previous minor version. Managed user clusters can't be more than one minor version lower than the admin cluster, so before upgrading an admin cluster to a new minor version, make sure that all managed user clusters are at the same minor version as the admin cluster.

## Upgrade an admin cluster

###  Console 

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project, and then select the cluster that you want to upgrade.

  3. In the **Details** panel, click **More details**.

  4. In the **Cluster basics** section, click edit **Upgrade**.

  5. In the **Choose target version** list, select the version that you want to upgrade to. We recommend that you upgrade to the latest patch version.

  6. Click **Upgrade**.




Before the cluster is upgraded, preflight checks run to validate cluster status and node health. If the preflight checks pass, the admin cluster is upgraded. It takes 30 minutes or more for the upgrade to complete, depending on the size of your cluster.

To view the status of the upgrade, click **Show Details** on the **Cluster Details** tab.

###  gcloud CLI 

  1. Optionally, list all enrolled admin clusters in the project to confirm the cluster name and region:
         
         gcloud container bare-metal admin-clusters list \
           --project=PROJECT_ID \
           --location=-
         

     * Replace `PROJECT_ID` with the ID of the fleet host project in which the cluster is a member. If you created the cluster using `bmctl`, this is the project ID in the `gkeConnect.projectID` field in the cluster configuration file.

     * When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to a specific [region](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/supported-regions-on-prem-api).

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the Google Cloud CLI with the account that has access to the project.

  2. Get a list of available versions to upgrade to:
         
         gcloud container bare-metal admin-clusters query-version-config \
           --admin-cluster=ADMIN_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION
         

Replace the following:

     * `ADMIN_CLUSTER_NAME`: The name of the admin cluster.

     * `PROJECT_ID`: The ID of the fleet host project in which the cluster is a member.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores cluster metadata.

  3. Upgrade the admin cluster:
         
         gcloud container bare-metal admin-clusters update ADMIN_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --version=VERSION
         

Replace `VERSION` with the Google Distributed Cloud version that you want to upgrade to. Specify a version from the output of the previous command. We recommend that you upgrade to the latest patch version.

The output from the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
         

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation.

To find out the status of the operation, copy the `OPERATION_ID` from your output into the following command. Open another terminal window and run the command.
         
         gcloud container bare-metal operations describe OPERATION_ID \
           --project=PROJECT_ID \
           --location=REGION
         




It takes 30 minutes or more for the upgrade to complete, depending on the size of your cluster. As the cluster is being upgraded, you can run the previous command every so often to get the current status.

When the upgrade is complete, you see something similar to the following in the terminal window where you ran the `gcloud ... update` command:
    
    
    Updated Anthos on bare metal Admin Cluster [https://gkeonprem.googleapis.com/v1/projects/example-project-1234/locations/us-central1/bareMetalAdminClusters/abm-admin-cluster].
    NAME               LOCATION     VERSION     MEMBERSHIP         STATE
    abm-admin-cluster  us-central1  1.16.8      abm-admin-cluster  RUNNING
    

For additional information on the fields and flags, see [gcloud container bare-metal admin-clusters reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters).

## Upgrade a user cluster

###  Console 

  1. In the console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project, and then select the cluster that you want to upgrade.

  3. In the **Details** panel, click **More details**.

  4. In the **Cluster basics** section, click edit **Upgrade**.

  5. In the **Choose target version** list, select the version that you want to upgrade to.

  6. Click **Upgrade**.




Before the cluster is upgraded, preflight checks run to validate cluster status and node health. If the preflight checks pass, the user cluster is upgraded. It takes 30 minutes or more for the upgrade to complete, depending on the size of your cluster.

To view the status of the upgrade, click **Show Details** on the **Cluster Details** tab.

###  gcloud CLI 

  1. Optionally, list all enrolled user clusters in the project to confirm the cluster name and region:
         
         gcloud container bare-metal clusters list \
           --project=PROJECT_ID \
           --location=-
         

     * Replace `PROJECT_ID` with the ID of the fleet host project in which the cluster is a member. If you created the cluster using `bmctl`, this is the project ID in the `gkeConnect.projectID` field in the cluster configuration file.

     * When you set `--location=-`, that means to list all clusters in all regions. If you need to scope down the list, set `--location` to a specific [region](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/supported-regions-on-prem-api).

The output of the command is similar to the following:
    
    NAME              LOCATION     VERSION  ADMIN_CLUSTER      STATE
    abm-user-cluster  us-central1  1.16.8   abm-admin-cluster  RUNNING
    

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the Google Cloud CLI with the account that has access to the project.

  2. Get a list of available versions to upgrade to:
         
         gcloud container bare-metal clusters query-version-config \
           --cluster=USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to upgrade.

     * `PROJECT_ID`: The ID of the fleet host project in which the cluster is a member.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores cluster metadata.

The output of the command is similar to the following
    
    versions:
    - hasDependencies: true
    version: 1.15.2
    - hasDependencies: true
    version: 1.15.1
    - hasDependencies: true
    version: 1.15.0
    - version: 1.14.6
    

Choose a version that _isn't_ listed under `- hasDependencies: true`. In this example, the only available version that you can upgrade the user cluster to is `1.14.6`.

  3. Upgrade the user cluster:
         
         gcloud container bare-metal clusters update USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION \
           --version=VERSION
         

Replace `VERSION` with the Google Distributed Cloud version that you want to upgrade to. Specify a version from the output of the previous command. We recommend that you upgrade to the latest patch version.

The output from the command is similar to the following:
         
         Waiting for operation [projects/example-project-12345/locations/us-west1/operations/operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179] to complete.
         

In the example output, the string `operation-1679543737105-5f7893fd5bae9-942b3f97-75e59179` is the `OPERATION_ID` of the long-running operation.

To find out the status of the operation, copy the `OPERATION_ID` from your output into the following command. Open another terminal window and run the command.
         
         gcloud container bare-metal operations describe OPERATION_ID \
           --project=PROJECT_ID \
           --location=REGION
         




It takes 30 minutes or more for the upgrade to complete, depending on the size of your cluster. As the cluster is being upgraded, you can run the previous command every so often to get the current status.

For additional information on the fields and flags, see [gcloud container bare-metal clusters reference](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters).

### Terraform

To upgrade a cluster using Terraform, you use the same Terraform configuration that you used to create the cluster.

  1. Change to the directory in which the Terraform configuration file is located.

  2. Get a list of available versions to upgrade to:
         
         gcloud container bare-metal clusters query-version-config \
           --cluster=USER_CLUSTER_NAME \
           --project=PROJECT_ID \
           --location=REGION
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster to upgrade.

     * `PROJECT_ID`: The ID of the fleet host project in which that user cluster is a member.

     * `REGION`: The Google Cloud region in which the GKE On-Prem API runs and stores its metadata.

If you get a `PERMISSION_DENIED` error, double check the project ID that you entered. If the project ID is correct, run `gcloud auth login` to sign in to the Google Cloud CLI with the account that has access to the project.

  3. In your Terraform configuration, change `bare_metal_version` to the Google Distributed Cloud version that you want to upgrade to. Specify a version from the output of the previous command. We recommend that you upgrade to the most recent patch version.

  4. Initialize and create the Terraform plan:
         
         terraform init
         

Terraform installs any needed libraries, such as the Google Cloud provider.

  5. Review the configuration and make changes if needed:
         
         terraform plan
         

  6. Apply the Terraform plan to create the user cluster:
         
         terraform apply
         




For information on the `google_gkeonprem_bare_metal_cluster` resource, see the [reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gkeonprem_bare_metal_cluster).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
