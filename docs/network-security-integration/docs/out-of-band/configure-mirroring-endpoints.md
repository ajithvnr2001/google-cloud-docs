---
url: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoints/
title: Create and manage mirroring endpoints \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:56.015292+00:00
---

# Create and manage mirroring endpoints  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Create and manage mirroring endpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A mirroring endpoint acts as a Google-managed intermediary or a broker for mirrored network traffic. After receiving the mirrored traffic, the mirroring endpoint enhances the network packets with additional [GENEVE metadata](https://docs.cloud.google.com/network-security-integration/docs/understand-geneve), and mirrors the traffic to multiple producer mirroring deployment groups.

You need a mirroring endpoint only for the broker mode of mirroring, not for the direct mode of mirroring.

## Before you begin

  * You must [enable](https://console.cloud.google.com/apis/library/compute.googleapis.com) the [ Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1) in your Google Cloud project.

  * You must [enable](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) the [Network Security API](https://docs.cloud.google.com/network-security-integration/docs/reference/rest) in the Google Cloud project that you want to use for billing.

  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the `gcloud` command-line examples in this guide.

  * You must have a [mirroring deployment group](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-deployment-groups).




### Roles

To get the permissions that you need to create, view, or delete mirroring endpoints, ask your administrator to grant you the necessary [ Identity and Access Management (IAM) roles](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview#iam-roles) on your Google Cloud project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, make sure that your user role has the Mirroring Endpoint Admin (`roles/networksecurity.mirroringEndpointAdmin`) permission.

### Quotas

To view quotas associated with mirroring endpoints, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## Create a mirroring endpoint

Create a mirroring endpoint in a specific zone.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpoints.create`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`



###  gcloud 

To create a mirroring endpoint, use the [`gcloud network-security mirroring-endpoint create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoints/create):
    
    
    gcloud beta network-security mirroring-endpoint create ENDPOINT \
        --location ZONE \
        --project PROJECT_NAME \
        --mirroring-endpoint-group ENDPOINT_GROUP \
        --no-async
    

Replace the following:

  * `ENDPOINT`: the name of the mirroring endpoint.

  * `ZONE`: the zone of the mirroring endpoint. You can create only one mirroring endpoint in a zone.

  * `PROJECT_NAME`: the project name where you want to create the mirroring endpoint.

  * `ENDPOINT_GROUP`: the name of the mirroring endpoint group.




## View the details of a mirroring endpoint

View the details of a specific mirroring endpoint.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpoints.get`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`
  * `networksecurity.mirroringEndpointViewer`



###  gcloud 

To view details of a mirroring endpoint, use the [`gcloud network-security mirroring-endpoint describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoints/describe):
    
    
    gcloud beta network-security mirroring-endpoint describe ENDPOINT \
        --location ZONE \
        --project PROJECT_NAME
    

Replace the following:

  * `ENDPOINT`: the name of the mirroring endpoint.

  * `ZONE`: the zone where the mirroring endpoint is located.

  * `PROJECT_NAME`: the name of the project where the mirroring endpoint is created.




## List mirroring endpoints

List all mirroring endpoints in a project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpoints.list`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`
  * `networksecurity.mirroringEndpointViewer`
  * `networksecurity.mirroringEndpointUser`



###  gcloud 

To list all mirroring endpoints, use the [`gcloud network-security mirroring-endpoint list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoints/list):
    
    
    gcloud beta network-security mirroring-endpoint list \
        --project PROJECT_NAME \
        --location ZONE
    

Replace the following:

  * `PROJECT_NAME`: the name of the project where the mirroring endpoint is created.

  * `ZONE`: the zone where the mirroring endpoint is located.




## Delete a mirroring endpoint

You can delete a mirroring endpoint by specifying its name, location, and project.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.mirroringEndpoints.delete`



**Roles**

  * `networksecurity.mirroringEndpointAdmin`



###  gcloud 

To delete a mirroring endpoint, use the [`gcloud network-security mirroring-endpoint delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoints/delete):
    
    
    gcloud beta network-security mirroring-endpoint delete ENDPOINT \
        --project PROJECT_NAME \
        --location ZONE \
        --no-async
    

Replace the following:

  * `ENDPOINT`: the name of the mirroring endpoint.

  * `PROJECT_NAME`: the project name where the mirroring endpoint is created.

  * `ZONE`: the zone where the mirroring endpoint is located.




## What's next

  * [Mirroring endpoint groups overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/endpoint-groups-overview)
  * [Out-of-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/out-of-band-integration-overview)
  * [Create and manage mirroring endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/out-of-band/configure-mirroring-endpoint-group-associations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
