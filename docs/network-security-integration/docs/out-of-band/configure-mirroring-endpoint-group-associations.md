---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations/
title: Create and manage mirroring endpoint group associations \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:35.741254+00:00
---

# Create and manage mirroring endpoint group associations  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage mirroring endpoint group associations Stay organized with collections  Save and categorize content based on your preferences. 

Create a mirroring endpoint group association to attach a mirroring endpoint group to a Virtual Private Cloud (VPC) network. You can create a mirroring endpoint group globally and associate it with one or more VPC networks to monitor workloads.

This page explains how to create and manage mirroring endpoint group associations.

## Before you begin

  * You need a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and a [subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your Google Cloud project.

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in your Google Cloud project.

  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.

  * You must have a [mirroring endpoint group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups).




### Roles

To get the permissions that you need to create, view, or delete mirroring endpoint group associations, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview#iam-roles) on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the following Mirroring Endpoint Admin role (`roles/networksecurity.mirroringEndpointAdmin`) and Mirroring Endpoint User (`roles/networksecurity.mirroringEndpointUser`) role permissions:

  * `networksecurity.mirroringEndpointGroupAssociations.create`
  * `networksecurity.mirroringEndpointGroupAssociations.delete`
  * `networksecurity.mirroringEndpointGroupAssociations.update`
  * `networksecurity.mirroringEndpointGroupAssociations.get`
  * `networksecurity.mirroringEndpointGroupAssociations.list`



### Quotas

To view quotas associated with mirroring endpoint group associations, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## Create mirroring endpoint group associations

You can associate one or more VPC networks to a specific mirroring endpoint group in the same zone.

On the [Create and manage mirroring endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups) page, you created a mirroring endpoint group where the network traffic inspection can happen for the mirrored traffic. However, you still need to specify which VPCs' traffic can be inspected. To do this, you create a project-level mirroring endpoint group association.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointGroupAssociations.create`
  * `networksecurity.mirroringEndpointGroupAssociations.update`
  * `networksecurity.mirroringEndpointGroupAssociations.delete`
  * `networksecurity.mirroringEndpointGroupAssociations.get`
  * `networksecurity.mirroringEndpointGroupAssociations.list`



**Roles**

  * Mirroring Endpoint Admin (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint User (`roles/networksecurity.mirroringEndpointUser`)



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the endpoint group.

  3. In the **Associations** section, click **Create**.

  4. In the **Create associations** pane, click **Add endpoint group association**.

  5. For **Project** and **Network** , select the project and the VPC network that hosts the mirroring endpoint group.

**Note:** Make sure that the VPC network you associate with the endpoint group isn't the same as the deployment group network.
  6. Click **Done**.

  7. Click **Create**.




###  gcloud 

To create a mirroring endpoint group association, use the [`gcloud network-security mirroring-endpoint-group-associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/create):
    
    
     gcloud network-security mirroring-endpoint-group-associations \
         create ENDPOINT_GROUP_ASSOCIATION \
         --location global \
         --project PROJECT_NAME \
         --network NETWORK \
         --mirroring-endpoint-group ENDPOINT_GROUP \
         --no-async
    

Replace the following:

  * `ENDPOINT_GROUP_ASSOCIATION`: the name of the mirroring endpoint group association  The endpoint group association name is visible to producers that the consumer explicitly granted access to. Therefore, don't include sensitive information such as personally identifiable information or security data in the mirroring endpoint group name.

  * `PROJECT_NAME`: the Google Cloud project name of the network

  * `NETWORK`: the name of the network

  * `ENDPOINT_GROUP`: the name of the mirroring endpoint group




### Terraform

To create a mirroring endpoint group association, you can use a [`google_network_security_mirroring_endpoint_group_association` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_mirroring_endpoint_group_association).
    
    
    resource "google_network_security_mirroring_endpoint_group_association" "default" {
      mirroring_endpoint_group_association_id = "mirroring-endpoint-group-association"
      location                                = "global"
      network                                 = google_compute_network.consumer_network.id
      mirroring_endpoint_group                = google_network_security_mirroring_endpoint_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View mirroring endpoint associations

You can view the details of a specific mirroring endpoint group association in a zone.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointgroupAssociations.get`



**Roles**

  * Mirroring Endpoint Admin (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint User (`roles/networksecurity.mirroringEndpointUser`)
  * Mirroring Endpoint Viewer (`roles/networksecurity.mirroringEndpointViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the mirroring endpoint group. The **Associations** section lists the details of the mirroring endpoint associations.




###  gcloud 

To view a mirroring endpoint group association, use the [`gcloud network-security mirroring-endpoint-group-associations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe):
    
    
     gcloud network-security mirroring-endpoint-group-associations \
         describe ENDPOINT_GROUP_ASSOCIATION \
         --location global \
         --project PROJECT_NAME
    

Replace the following:

  * `ENDPOINT_GROUP_ASSOCIATION`: the name of the mirroring endpoint group association

  * `PROJECT_NAME`: the project name of the mirroring endpoint group association




## List mirroring endpoint group associations

You can list the mirroring endpoint group associations for a network, a project, or a mirroring endpoint group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointgroupAssociations.list`



**Roles**

  * Mirroring Endpoint Admin (`roles/networksecurity.mirroringEndpointAdmin`)
  * Mirroring Endpoint User (`roles/networksecurity.mirroringEndpointUser`)
  * Mirroring Endpoint Viewer (`roles/networksecurity.mirroringEndpointViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the mirroring endpoint group. The **Associations** section lists all mirroring endpoint associations of the mirroring endpoint group.




###  gcloud 

To list a mirroring endpoint group association in a project, use the [`gcloud network-security mirroring-endpoint-group-associations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/list):
    
    
     gcloud network-security mirroring-endpoint-group-associations list \
         --project PROJECT_NAME \
         --network NETWORK
    

Replace the following:

  * `PROJECT_NAME`: the project name of the mirroring endpoint group association

  * `NETWORK`: the name of the VPC network




## Delete a mirroring endpoint group association

You can delete a mirroring endpoint group association for a specific VPC network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointgroupAssociations.delete`



**Roles**

  * Mirroring Endpoint Admin (`roles/networksecurity.mirroringEndpointAdmin`)
  * `networksecurity.mirroringEndpointNetworkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **Endpoint groups** page.

[Go to Endpoint groups](https://console.cloud.google.com/net-security/integration/endpoint-groups/list)

  2. Click the name of the mirroring endpoint group.

  3. In the **Associations** section, select the mirroring endpoint association to delete.

  4. Click **Delete**.

  5. Click **Delete** again to confirm.




###  gcloud 

To delete a mirroring endpoint group association, use the [`gcloud network-security mirroring-endpoint-group-associations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/delete):
    
    
     gcloud network-security mirroring-endpoint-group-associations \
         delete ENDPOINT_GROUP_ASSOCIATION \
         --location global \
         --project PROJECT_NAME \
         --no-async
    

Replace the following:

  * `ENDPOINT_GROUP_ASSOCIATION`: the name of the mirroring endpoint group association

  * `PROJECT_NAME`: the project name of the mirroring endpoint group association




## What's next

  * [Mirroring endpoint groups overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview)
  * [Create and manage mirroring endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
