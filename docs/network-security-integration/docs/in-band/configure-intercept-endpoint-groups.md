---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups/
title: Create and manage intercept endpoint groups \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:11.119736+00:00
---

# Create and manage intercept endpoint groups  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage intercept endpoint groups Stay organized with collections  Save and categorize content based on your preferences. 

An [intercept endpoint group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-group-overview) is a global resource that you can use with multiple VPC networks across different projects in your organization. You create an intercept endpoint group to allow consumers to access a producer's [intercept deployment group](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview). Each intercept endpoint group is associated with a single intercept deployment group.

This page describes how to create and manage intercept endpoint groups.

## Before you begin

  * [Enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [ Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your Google Cloud project.

  * [Enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in the Google Cloud project that you want to use for billing.

  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs).

  * Create an [intercept deployment group](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployment-groups).




### Roles

To create, view, or delete intercept endpoint groups, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview#iam-roles) on your Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the Intercept Endpoint Admin (`roles/networksecurity.interceptEndpointAdmin`) and Intercept Deployment User (`roles/networksecurity.interceptDeploymentUser`) roles and permissions.

The Intercept Deployment User role (`roles/networksecurity.interceptDeploymentUser`) is required on the producer project so that you can connect the consumer's intercept endpoint group to the producer's intercept deployment group.

## Create an intercept endpoint group

Create an intercept endpoint group and link it with the producer's intercept deployment group.

We recommend that you create the intercept endpoint group in a project owned by your security administrator.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointGroups.create`
  * `networksecurity.interceptDeploymentGroups.use`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 
  * [Intercept Deployment User role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentUser) (`networksecurity.interceptDeploymentUser`), or [Intercept Deployment External User role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptDeploymentExternalUser) (`networksecurity.interceptDeploymentExternalUser`) if the user is in another organization 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click **Create endpoint group**.

  3. For **Name** , enter a name for the intercept endpoint group.

  4. For **Deployment group** , select any one of the following:

     * **Select project** : Select if you know the project name where the intercept deployment group is available.

     * **Select current project** : Select if the intercept deployment group exists in the same project.

If you select this option, specify the name of the intercept deployment group.

     * **Manually enter deployment group** : Select if the intercept deployment group exists in a different project.

If you select this option, specify the project ID and the name of the intercept deployment group.

  5. Click **Continue**.

  6. Optional: Click **Add endpoint group association**.

Specify the name of the project and the name of the VPC network that hosts the intercept deployment group, and click **Done**.

**Note:** Make sure that the VPC network you associate with the endpoint group is not the same as the deployment group network.
  7. Click **Create**.




###  gcloud 

To create an intercept endpoint group, use the [`gcloud network-security intercept-endpoint-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/create):
    
    
    gcloud network-security intercept-endpoint-groups create ENDPOINT_GROUP_ID \
        --location global \
        --no-async \
        --intercept-deployment-group \
            projects/DEPLOYMENT_GROUP_PROJECT_ID/locations/global/interceptDeploymentGroups/DEPLOYMENT_GROUP_ID
    

Replace the following:

  * `ENDPOINT_GROUP_ID`: the ID of the intercept endpoint group.
  * `DEPLOYMENT_GROUP_PROJECT_ID`: the ID of the Google Cloud project where you created the intercept deployment group.
  * `DEPLOYMENT_GROUP_ID`: the ID of the intercept deployment group.



To associate the intercept endpoint group to a VPC network, see [Create and manage intercept endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/pm/configure-endpoint-group-associations).

###  Terraform 

To create an intercept endpoint group, you can use a [`google_network_security_intercept_endpoint_group` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_intercept_endpoint_group).
    
    
    resource "google_network_security_intercept_endpoint_group" "default" {
      intercept_endpoint_group_id = "intercept-endpoint-group"
      location                    = "global"
      intercept_deployment_group  = google_network_security_intercept_deployment_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View details of an intercept endpoint group

You can view the details of an intercept endpoint group, such as its name and intercept deployment group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointgroups.get`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 
  * [Intercept Endpoint Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointViewer) (`networksecurity.interceptEndpointViewer`) 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the intercept endpoint group.




###  gcloud 

To view details of an intercept endpoint group, use the [`gcloud network-security intercept-endpoint-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/describe):
    
    
    gcloud network-security intercept-endpoint-groups describe ENDPOINT_GROUP_ID \
        --location global
    

Replace `ENDPOINT_GROUP_ID` with the ID of the intercept endpoint group.

In the output, the name of the intercept endpoint group is displayed in the `projects/PROJECT_ID/locations/global/interceptEndpointGroups/ENDPOINT_GROUP_ID` format.

## List intercept endpoint groups

You can list all intercept endpoint groups in a project, including their IDs.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointGroups.list`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 
  * [Intercept Endpoint Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointViewer) (`networksecurity.interceptEndpointViewer`) 
  * [Intercept Endpoint User role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointUser) (`networksecurity.interceptEndpointUser`) 



###  Console 

To see all intercept endpoint groups of the project, in the Google Cloud console, go to the [**Endpoint groups**](https://console.cloud.google.com/net-security/integration/endpoint-groups/list) page.

###  gcloud 

To list all intercept endpoint groups, use the [`gcloud network-security intercept-endpoint-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/list):
    
    
    gcloud network-security intercept-endpoint-groups list \
        --location global
    

## Delete an intercept endpoint group

Before you delete an intercept endpoint group, remove its [intercept endpoint group association from any VPC networks](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-endpoint-group-associations#delete-intercept-endpoint-association).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.interceptEndpointGroups.delete`



**Roles**

  * [Intercept Endpoint Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/networksecurity#networksecurity.interceptEndpointAdmin) (`networksecurity.interceptEndpointAdmin`) 



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Select the checkbox of the intercept endpoint group and click **Delete**.

  3. Click **Delete** again to confirm.




###  gcloud 

To delete an intercept endpoint group, use the [`gcloud network-security intercept-endpoint-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/intercept-endpoint-groups/delete):
    
    
    gcloud network-security intercept-endpoint-groups delete ENDPOINT_GROUP_ID
        --no-async \
        --location global
    

Replace the following `ENDPOINT_GROUP_ID` with the ID of the intercept endpoint group.

## What's next

  * [Create and manage intercept endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-endpoint-group-associations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
