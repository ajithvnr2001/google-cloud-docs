---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployment-groups/
title: Create and manage intercept deployment groups \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:55.470012+00:00
---

# Create and manage intercept deployment groups  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployment-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage intercept deployment groups Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage intercept deployment groups.

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).



### Roles

To create, view, or delete intercept deployment groups, your Identity and Access Management (IAM) principal must have the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview#iam-roles) on your project. For more information, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, your Identity and Access Management (IAM) principal must have the following [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`roles/networksecurity.interceptDeploymentAdmin`) permissions:

  * `networksecurity.interceptDeploymentGroups.create`
  * `networksecurity.interceptDeploymentGroups.delete`
  * `networksecurity.interceptDeploymentGroups.get`
  * `networksecurity.interceptDeploymentGroups.list`



## Create an intercept deployment group

An intercept deployment group is a global resource that holds a collection of zonal intercept deployments.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptDeploymentGroups.create`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click **Create deployment group**.

  3. For **Name** , enter a unique name of the deployment group.

  4. For **Network** , select a VPC network. All intercept deployments must reference internal passthrough Network Load Balancers that use this network.

  5. Click **Create**.




###  gcloud 

To create an intercept deployment group, use the [`gcloud network-security intercept-deployment-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/create):
    
    
    gcloud network-security intercept-deployment-groups create DEPLOYMENT_GROUP_ID \
        --location global \
        --no-async \
        --network NETWORK
    

Replace the following:

  * `DEPLOYMENT_GROUP_ID`: the ID of the intercept deployment group.

Don't include sensitive information, such as personally identifiable information or security data, in the intercept deployment group name. The intercept deployment group name is visible to consumers that the producer explicitly granted access to.
  * `NETWORK`: the name of a VPC network. All intercept deployments must reference internal passthrough Network Load Balancers that use this network.




###  Terraform 

To create an intercept deployment group, you can use a [`google_network_security_intercept_deployment_group` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_intercept_deployment_group).
    
    
    resource "google_network_security_intercept_deployment_group" "default" {
      intercept_deployment_group_id = "intercept-deployment-group"
      location                      = "global"
      network                       = google_compute_network.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View details of an intercept deployment group

You can view the details of an intercept deployment group, such as its name and the network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptDeploymentGroups.get`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 
  * [Intercept Deployment Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentViewer) (`networksecurity.interceptDeploymentViewer`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Click the deployment group.




###  gcloud 

To view the details of an intercept deployment group, use the [`gcloud network-security intercept-deployment-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/describe):
    
    
    gcloud network-security intercept-deployment-groups describe DEPLOYMENT_GROUP_ID \
        --location global
    

Replace `DEPLOYMENT_GROUP_ID` with the ID of the intercept deployment group.

In the output, the name of the intercept deployment group is displayed in the `projects/PROJECT_ID/locations/global/interceptDeploymentGroups/DEPLOYMENT_GROUP_ID` format.

## List intercept deployment groups

You can list all intercept deployment groups in a project, including their IDs.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.interceptDeploymentGroups.list`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 
  * [Intercept Deployment Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentViewer) (`networksecurity.interceptDeploymentViewer`) 



###  Console 

To see all the intercept deployment groups of the project, complete the following step:

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. To list the intercept deployment groups, click filter_list **Filter**.

  3. From the **Properties** list, select **Purpose** and then for **Value** , select **NSI In-band**.




###  gcloud 

To list all intercept deployment groups of the project, use the [`gcloud network-security intercept-deployment-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/list):
    
    
    gcloud network-security intercept-deployment-groups list
    

## Delete an intercept deployment group

Before you delete an intercept deployment group, [delete intercept deployments](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployments#delete-intercept-deployment) that reference the intercept deployment group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.interceptDeploymentGroups.delete`



**Roles**

  * [Intercept Deployment Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentAdmin) (`networksecurity.interceptDeploymentAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Deployment groups** page.

[Go to Deployment groups](https://console.cloud.google.com/net-security/integration/deployment-groups/list)

  2. Select the checkbox of the deployment group and click **Delete**.

  3. Click **Delete** again to confirm.




###  gcloud 

To delete an intercept deployment group, use the [`gcloud network-security intercept-deployment-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-deployment-groups/delete):
    
    
    gcloud network-security intercept-deployment-groups delete DEPLOYMENT_GROUP_ID \
        --no-async \
        --location global
    

Replace `DEPLOYMENT_GROUP_ID` with the ID of the intercept deployment group.

## What's next

  * [Intercept deployments overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployments-overview)
  * [Create and manage intercept deployments](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
