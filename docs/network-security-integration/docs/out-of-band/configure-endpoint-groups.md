---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups/
title: Create and manage mirroring endpoint groups \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:17.418169+00:00
---

# Create and manage mirroring endpoint groups  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-endpoint-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage mirroring endpoint groups Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure and manage the mirroring endpoint groups in the consumer's account to represent the producer's mirroring deployment groups.

We recommend that you create the [mirroring endpoint group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview) in a project owned by your security administrator. To create the [mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations), the security administrator must assign the Mirroring Endpoint Admin (`roles/networksecurity.mirroringAdmin`) and Mirroring Endpoint Network Admin (`roles/networksecurity.mirroringEndpointNetworkAdmin`) roles to the project or to the network administrator.

If you have enabled the mirroring rule action as `MIRROR` in the firewall policy associated with your Virtual Private Cloud (VPC) network, and created the mirroring endpoint group associations, the mirrored traffic is forwarded to the mirroring endpoint group.

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your Google Cloud project.

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in the Google Cloud project that you want to use for billing.

  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.

  * You must have a [mirroring deployment group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups).




### Roles

To get the permissions that you need to create, view, or delete mirroring endpoint groups, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview#iam-roles) on your Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the Mirroring Endpoint Admin (`roles/networksecurity.mirroringEndpointAdmin`) and Mirroring Deployment User (`roles/networksecurity.mirroringDeploymentUser`) roles and permissions.

The Mirroring Deployment User role (`roles/networksecurity.mirroringDeploymentUser`) is required on the producer project so that you can connect the consumer's mirroring endpoint group to the producer's mirroring deployment group.

### Quotas

To view quotas associated with mirroring endpoint groups, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## Create a mirroring endpoint group

This section describes how to create a mirroring endpoint group to mirror packets in a specific zone. To mirror traffic to only one deployment group, create a mirroring endpoint group in the direct mode. To mirror traffic to multiple deployment groups, create a mirroring endpoint group in the broker mode ([Preview](https://cloud.google.com/products#product-launch-stages)).

### Direct mode of mirroring

Create a mirroring endpoint group for the direct mode of mirroring.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointGroups.create`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`



###  gcloud 

To create a mirroring endpoint group for the direct mirroring mode, use the [`gcloud network-security mirroring-endpoint-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/create):
    
    
     gcloud network-security mirroring-endpoint-groups create ENDPOINT_GROUP \
         --location global \
         --project PROJECT_NAME \
         --mirroring-deployment-group DEPLOYMENT_GROUP \
         --no-async
    

Replace the following:

  * `ENDPOINT_GROUP`: the name of the mirroring endpoint group.  The endpoint group name is visible to producers that the consumer explicitly granted access to. Therefore, don't include sensitive information such as personally identifiable information or security data in the mirroring endpoint group name. 

  * `PROJECT_NAME`: the project name where you want to create the mirroring endpoint group.

  * `DEPLOYMENT_GROUP`: the name of the target mirroring deployment group.




To associate the mirroring endpoint group to a VPC network, see [Create and manage mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations).

### Terraform

To create a mirroring endpoint group, you can use a [`google_network_security_mirroring_endpoint_group` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_mirroring_endpoint_group).
    
    
    resource "google_network_security_mirroring_endpoint_group" "default" {
      mirroring_endpoint_group_id = "mirroring-endpoint-group"
      location                    = "global"
      mirroring_deployment_group  = google_network_security_mirroring_deployment_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Broker mode of mirroring

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Create a mirroring endpoint group for the broker mode of packet mirroring.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointGroups.create`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`



###  gcloud 

To create a mirroring endpoint group for the broker mode, use the [`gcloud network-security mirroring-endpoint-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/create):
    
    
    gcloud beta network-security mirroring-endpoint-groups create ENDPOINT_GROUP \
        --location global \
        --project PROJECT_NAME \
         --type broker \
        --mirroring-deployment-groups DEPLOYMENT_GROUP_1,DEPLOYMENT_GROUP_2 \
        --no-async
    

Replace the following:

  * `ENDPOINT_GROUP`: the name of the mirroring endpoint group.  The endpoint group name is visible to producers that the consumer explicitly granted access to. Therefore, don't include sensitive information such as personally identifiable information or security data in the mirroring endpoint group name. 

  * `PROJECT_NAME`: the project name where you want to create the mirroring endpoint group.

  * `TYPE`: specify `broker` as the type of the mirroring endpoint group. The default value is `direct`.

  * `DEPLOYMENT_GROUP`: a comma-separated list of mirroring deployment groups.




To associate the mirroring endpoint group to a VPC network, see [Create and manage mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations).

### Terraform

To create a mirroring endpoint group, you can use a [`google_network_security_mirroring_endpoint_group` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_mirroring_endpoint_group).
    
    
    resource "google_network_security_mirroring_endpoint_group" "default" {
      mirroring_endpoint_group_id = "mirroring-endpoint-group"
      location                    = "global"
      mirroring_deployment_group  = google_network_security_mirroring_deployment_group.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## View a mirroring endpoint group

You can view the details of a specific mirroring endpoint group.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointgroups.get`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`
  * `networksecurity.mirroringEndpointViewer`



###  gcloud 

To view details of a mirroring endpoint group, use the [`gcloud network-security mirroring-endpoint-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/describe):
    
    
     gcloud network-security mirroring-endpoint-groups \
         describe ENDPOINT_GROUP \
         --location global
    

Replace `ENDPOINT_GROUP`with the name of the mirroring endpoint group.

## List mirroring endpoint groups

You can list all the mirroring endpoint groups in a project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointGroups.list`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`
  * `networksecurity.mirroringEndpointViewer`
  * `networksecurity.mirroringEndpointUser`



###  gcloud 

To list all mirroring endpoint groups, use the [`gcloud network-security mirroring-endpoint-groups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/list):
    
    
     gcloud network-security mirroring-endpoint-groups list \
         --project PROJECT_NAME \
         --location global
    

Replace `PROJECT_NAME`with the name of the project where the mirroring endpoint group was created.

## Delete a mirroring endpoint group

You can delete a mirroring endpoint group by specifying its name, location, and project.

**Note:** You can delete a mirroring endpoint group only if it is not associated with any VPC network.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpointGroups.delete`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`



###  gcloud 

To delete a mirroring endpoint group, use the [`gcloud network-security mirroring-endpoint-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-groups/delete):
    
    
     gcloud network-security mirroring-endpoint-groups delete ENDPOINT_GROUP
         --project PROJECT_NAME \
         --location global \
         --no-async
    

Replace the following:

  * `ENDPOINT_GROUP`: the name of the mirroring endpoint group.

  * `PROJECT_NAME`: the project name where the mirroring endpoint group was created.




## What's next

  * [Mirroring endpoint groups overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)
  * [Create and manage mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
