---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups/
title: Create and manage mirroring deployment groups \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:53.082367+00:00
---

# Create and manage mirroring deployment groups  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage mirroring deployment groups Stay organized with collections  Save and categorize content based on your preferences. 

Create a mirroring deployment group to represent the producer services across different zones within a project.

This page explains how to configure the [mirroring deployment groups](https://docs.cloud.google.com/network-security-integration/docs/deployment-groups-overview).

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.



### Roles

To get the permissions that you need to create, view, or delete mirroring deployment groups, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview#iam-roles) on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following [Mirroring Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.mirroringDeploymentAdmin) (`roles/networksecurity.mirroringDeploymentAdmin`) permissions:

  * `networksecurity.mirroringDeployments.create`
  * `networksecurity.mirroringDeployments.delete`
  * `networksecurity.mirroringDeployments.get`
  * `networksecurity.mirroringDeployments.list`



## Create a mirroring deployment group

The mirroring deployment group is a collection of mirroring deployments. You create a mirroring deployment group across different locations within a project. The deployment group references the network in which all deployments are created.

When you create a mirroring deployment group, you can specify the name of the mirroring deployment group as a string or as a unique URL identifier. The unique URL for a project-scoped mirroring deployment group can be constructed in the following format:
    
    
    projects/PROJECT_ID/locations/global/mirroringDeploymentGroups/DEPLOYMENT_GROUP_ID
    

Replace the following:

  * `PROJECT_ID`: ID of the project.

  * `DEPLOYMENT_GROUP_ID`: ID of the mirroring deployment group.




If you use a unique URL identifier for the mirroring deployment group name, the project and location of the mirroring deployment group is already included in the URL identifier. However, if you use only the mirroring deployment group name, you must specify the project and location separately. For more information about unique URL identifiers, see [mirroring deployment group specifications](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview#deployment-group-specification).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringDeploymentGroups.create`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click **Create deployment group**.

  3. For **Name** , enter a unique name of the deployment group.

  4. For **Network** , select a VPC network. All mirroring deployments must reference internal passthrough Network Load Balancers that use this network.

  5. For **Purpose** , select **NSI out-of-band**.

  6. Click **Create**.




###  gcloud 

To create a mirroring deployment group, use the [`gcloud beta network-security mirroring-deployment-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/mirroring-deployment-groups/create):
    
    
     gcloud beta network-security mirroring-deployment-groups \
         create DEPLOYMENT_GROUP \
         --location global \
         --project PROJECT \
         --network NETWORK \
         --no-async
    

Replace the following:

  * `DEPLOYMENT_GROUP`: the name of the mirroring deployment group; you can specify the name as a string or as a unique URL identifier.

The deployment group name is visible to consumers that the producer explicitly granted access to. Therefore, don't include sensitive information such as personally identifiable information or security data in the mirroring deployment group name.

  * `PROJECT`: the project name of the mirroring deployment group.

  * `NETWORK`: the name of your network.




### Terraform

To create a mirroring deployment group, you can use a [`google_network_security_mirroring_deployment_group` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_mirroring_deployment_group).
    
    
    resource "google_network_security_mirroring_deployment_group" "default" {
      mirroring_deployment_group_id = "mirroring-deployment-group"
      location                      = "global"
      network                       = google_compute_network.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View a mirroring deployment group

You can view the details of a specific mirroring deployment group in a project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringDeploymentGroups.get`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer (`roles/networksecurity.mirroringDeploymentViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the deployment group.




###  gcloud 

To view details of a mirroring deployment group, use the [`gcloud network-security mirroring-deployment-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/describe):
    
    
    gcloud network-security mirroring-deployment-groups \
        describe DEPLOYMENT_GROUP \
        --project PROJECT \
        --location global
    

Replace the following:

  * `DEPLOYMENT_GROUP`: the name of the mirroring deployment group.

  * `PROJECT`: the project name of the mirroring deployment group.




## List mirroring deployments

You can list all the mirroring deployment groups in your project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.mirroringDeploymentGroups.list`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)
  * Mirroring Deployment Viewer (`roles/networksecurity.mirroringDeploymentViewer`)



###  Console 

To see all the mirroring deployment groups of the project, complete the following step:

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. To list the mirroring deployment groups, click filter_list**Filter**.

  3. From the **Properties** list, select **Purpose** and then for **Value** , select **NSI out-of-band**.




###  gcloud 

To list mirroring deployment groups, use the [`gcloud network-security mirroring-deployment-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/list):
    
    
     gcloud network-security mirroring-deployment-groups list \
         --project PROJECT
    

Replace `PROJECT`with the name of the project where the mirroring deployment groups is created.

## Delete a mirroring deployment group

You can delete a mirroring deployment by specifying its name, location, and project. However, if a mirroring deployment group is referenced by a mirroring deployment then it cannot be deleted.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.mirroringDeploymentGroups.delete`



**Roles**

  * Mirroring Deployment Admin (`roles/networksecurity.mirroringDeploymentAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Select the checkbox of the deployment group and click **Delete**.

  3. Click **Delete** again to confirm.




###  gcloud 

To delete a mirroring deployment group, use the [`gcloud network-security mirroring-deployment-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/delete):
    
    
     gcloud network-security mirroring-deployment-groups \
         delete DEPLOYMENT_GROUP \
         --location global \
         --project PROJECT \
         --no-async
    

Replace the following:

  * `DEPLOYMENT_GROUP`: the name of the mirroring deployment group that you want to delete.

  * `PROJECT`: the project name of the mirroring deployment group.




## What's next

  * [Create and manage mirroring deployments](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployments)
  * [Mirroring deployment groups overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/deployment-groups-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
