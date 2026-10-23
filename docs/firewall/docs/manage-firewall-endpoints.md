---
url: https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints/
title: Manage firewall endpoints and endpoint associations \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:13.262763+00:00
---

# Manage firewall endpoints and endpoint associations  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage firewall endpoints and endpoint associations Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to manage firewall endpoints and their associations with a Virtual Private Cloud (VPC) network by using the Google Cloud console or the Google Cloud CLI. Associating a firewall endpoint with your VPC networks lets you help protect your VM instances and inspect traffic across multiple networks in the same zone without deploying separate inspection appliances.

A [firewall endpoint](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints) is a zonal resource that provides Layer 7 inspection for your traffic. A [firewall endpoint association](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#endpoint-association) lets you associate the endpoint with one or more VPC networks in that zone to inspect traffic.

## Before you begin

Before you manage firewall endpoints and associations, complete the following:

  1. Ensure that you have a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and a [subnet](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#specifications).
  2. Enable the required APIs: 
     * [Compute Engine API (Compute Engine API)](https://console.cloud.google.com/apis/library/compute.googleapis.com) in your Google Cloud project.
     * [Network Security API](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) in the Google Cloud project that you want to use for billing.
     * [Certificate Authority Service API](https://console.cloud.google.com/apis/library/privateca.googleapis.com) in your Google Cloud project.
  3. Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run `gcloud` command-line examples.



### Roles and permissions

To get the permissions that you need to view, update, or delete firewall endpoints and associations, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#iam-roles) on your organization or project. For more information, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, ensure that your user account has the [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role, which includes the following permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



### Quotas

To view quotas for firewall endpoints and associations, see [Quotas and limits](https://docs.cloud.google.com/firewall/docs/quotas).

## Manage firewall endpoints

In this section, learn to manage firewall endpoints.

### List and view details of a firewall endpoint

To list all firewall endpoints, use the Google Cloud console or the gcloud CLI.

You can view the endpoint details such as:

  * The zone where the endpoint is deployed
  * The current state of the endpoint
  * The jumbo frames support status
  * The billing project (for organization-level endpoints only)
  * The endpoint associations



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your organization or the project where the endpoint exists.

If you select an organization, the **Firewall endpoints** page lists the firewall endpoints in the organization.

If you select a project, the **Firewall endpoints located in this project** section lists the project's firewall endpoints.

  3. Click the name of the firewall endpoint to view its details.




###  gcloud 

To list all firewall endpoints, use the [`gcloud network-security firewall-endpoints list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/list):
    
    
    gcloud network-security firewall-endpoints list \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location LOCATION \
        [--billing-project QUOTA_PROJECT_ID]
    

To view details of a firewall endpoint, use the [`gcloud network-security firewall-endpoints describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/describe):
    
    
    gcloud network-security firewall-endpoints describe NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the firewall endpoint.

  * `ORGANIZATION_ID`: the organization ID where the firewall endpoint exists. Use this flag for an organization-level endpoint.

  * `PROJECT_ID`: the project ID where the firewall endpoint exists. Use this flag for a project-level endpoint.

  * `LOCATION`: the zone where the endpoint exists.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level endpoints.




### Update a firewall endpoint

To update a firewall endpoint, use the Google Cloud console or the gcloud CLI.

You can update the following key details of an endpoint:

  * The billing project (available for organization-level endpoints only)
  * The labels of the endpoint
  * The description of the endpoint



You can't change any of the following details:

  * The status of jumbo frames support
  * The name of the endpoint
  * The zone of the endpoint
  * The organization or project of the endpoint



To change the previous details, delete the endpoint and create another.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your organization or the project where the endpoint exists.

If you select an organization, the **Firewall endpoints** page lists all the configured firewall endpoints in the organization.

If you select a project, the **Firewall endpoints located in this project** section of the **Firewall endpoints** page lists all firewall endpoints of the project.

  3. Click the name of the firewall endpoint to view its details.

  4. Click **Edit**.

  5. To update the billing project, select the **Billing project**

  6. In the **Advanced configuration** section, select the **Enable Advanced malware sandbox (WildFire)** checkbox ([Preview](https://cloud.google.com/products#product-launch-stages)).

  7. To update the additional Advanced malware sandbox configuration, click **Additional Advanced malware sandbox configuration** and update the fields.

  8. Click **Save**.




###  gcloud 

To update a firewall endpoint, use the [`gcloud network-security firewall-endpoints update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/update):
    
    
    gcloud network-security firewall-endpoints update NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location LOCATION \
        [--update-billing-project QUOTA_PROJECT_ID]
    

Replace the following:

  * `NAME`: the name of the firewall endpoint.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level endpoint.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level endpoint.

  * `LOCATION`: the zone where the endpoint exists.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level endpoints.


**Note:** You can't reconfigure an existing endpoint to add or remove support for jumbo frames. To add or remove jumbo frame support, delete the endpoint and recreate it. For more information, see Delete a firewall endpoint and [Create a firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints#create-firewall-endpoint).

To update a firewall endpoint for Advanced malware sandbox, use the [`gcloud beta network-security firewall-endpoints update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/update) ([Preview](https://cloud.google.com/products#product-launch-stages)):
    
    
    gcloud beta network-security firewall-endpoints \
       update NAME \
       --organization ORGANIZATION_ID \
       --zone ZONE \
       --[no-]enable-wildfire \
       --wildfire-region=WILDFIRE_REGION \
       --content-cloud-region=CONTENT_CLOUD_REGION \
       --hold-for-wildfire-realtime-signature-lookup-timeout-ms=TIMEOUT_MS \
       --hold-for-wildfire-realtime-signature-lookup-timeout-action=ACTION \
       --wildfire-inline-cloud-analysis-timeout-ms=TIMEOUT_MS \
       --wildfire-inline-cloud-analysis-timeout-action=ACTION \
       --[no-]enable-wildfire-analysis-logging \
       --[no-]block-partial-http \
       --billing-project BILLING_PROJECT_ID
    

Replace the following:

  * `WILDFIRE_REGION`: geographical region where the endpoint sends unknown files.
  * `CONTENT_CLOUD_REGION`: content cloud region that the endpoint uses.
  * `TIMEOUT_MS`: timeout thresholds in milliseconds for signature lookup or inline analysis.
  * `ACTION`: the timeout action, which must be `Allow` or `Deny`.
  * `--[no-]enable-wildfire-analysis-logging`: whether to enable logging for timeout events.
  * `--[no-]block-partial-http`: select to block the resuming of blocked malicious HTTP file downloads.



For information about the packet sizes supported by firewall endpoints, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

### Delete a firewall endpoint

To delete a firewall endpoint, use the Google Cloud console or the gcloud CLI.

Before you delete a firewall endpoint, consider the following:

  * You can delete a firewall endpoint only if it is not associated with any VPC network.
  * If firewall policy rules direct traffic to this endpoint, deleting the endpoint stops traffic inspection. All Layer 7 inspection services that the endpoint provides for associated networks in that zone also stop.
  * Deleting an endpoint in one zone affects only traffic and associations within that specific zone.



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.delete`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your organization or the project where the endpoint exists.

If you select an organization, the **Firewall endpoints** page lists all configured firewall endpoints in the organization.

If you select a project, the **Firewall endpoints located in this project** section of the **Firewall endpoints** page lists all firewall endpoints of the project.

  3. Select the firewall endpoint, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a firewall endpoint, use the [`gcloud network-security firewall-endpoints delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/delete):
    
    
    gcloud network-security firewall-endpoints delete NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the firewall endpoint.

  * `ORGANIZATION_ID`: the organization ID. Use this flag for an organization-level endpoint.

  * `PROJECT_ID`: the project ID. Use this flag for a project-level endpoint.

  * `LOCATION`: the zone where the endpoint exists.




## Manage firewall endpoint associations

A firewall endpoint association connects a firewall endpoint to a VPC network in a specific zone.

Ensure that you have a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints) before you manage its associations. To create an association, see [Create firewall endpoints and associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints).

### Association requirements

When you configure endpoint associations, follow these requirements:

  * **Zone constraints:** You must create the association in the same zone as the firewall endpoint. For effective traffic inspection, create associations in zones where your compute instances are deployed.
  * **One endpoint per zone:** In a single zone, you can associate a VPC network with only one firewall endpoint (either project-level or organization-level). However, you can associate a single VPC network with different firewall endpoints across multiple, different zones.
  * **Cross-project associations:** You can associate a VPC network with a firewall endpoint in a separate project. If you use a project-level endpoint, the endpoint's project must reside in the same organization as the VPC network.
  * **Resource mapping:** An association is a project-level resource. You create the association within the specific project where your compute instances are deployed, even if the association points to an organization-level firewall endpoint.



A firewall endpoint with jumbo frame support can accept packets only up to 8,500 bytes. Alternatively, a firewall endpoint without jumbo frame support can accept packets only up to 1,460 bytes. If you need intrusion detection and prevention service, Advanced malware sandbox, or URL filtering service, we recommend that you configure the associated VPC networks to use the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) limits of 8,500 bytes and 1,460 bytes. For more information, see [ Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

**Caution:** A firewall endpoint doesn't perform intrusion detection and prevention service, Advanced malware sandbox, or URL filtering service for a VPC network if the network is configured with an MTU that's greater than the firewall endpoint's limit.

### List and view a firewall endpoint association

To list and view firewall endpoint associations, use the Google Cloud console or the gcloud CLI.

You can view the following details for an endpoint association:

  * The lifecycle status
  * The active status
  * The TLS inspection status
  * The ID of the firewall endpoint



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.firewallEndpointAssociations.get`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Compute Network User (`roles/compute.networkUser`)
  * Compute Network Viewer (`roles/compute.networkViewer`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your Google Cloud project.

In the **Firewall endpoint associations** section, the table lists all firewall endpoint associations of organization-level and project-level endpoints.




###  gcloud 

To list firewall endpoint associations for a specific network, use the [`gcloud network-security firewall-endpoint-associations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/list) with the `--filter` flag.
    
    
    gcloud network-security firewall-endpoint-associations list \
        --filter network:NETWORK_NAME \
        [--project PROJECT_ID]
    

To view a firewall endpoint association, use the [`gcloud network-security firewall-endpoint-associations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/describe):
    
    
    gcloud network-security firewall-endpoint-associations describe NAME \
        --filter network:NETWORK_NAME \
        [--project PROJECT_ID]
    

Replace the following:

  * `NAME`: the name of the firewall endpoint association.

  * `PROJECT_ID`: the project ID where the association exists.

  * `NETWORK_NAME`: the name of the VPC network.




### Update a firewall endpoint association

To update a firewall endpoint association, use the Google Cloud console or the gcloud CLI.

You can update the following details:

  * The activation state
  * The associated TLS inspection policy
  * The labels and description



You can't update the following details:

  * The firewall endpoint and the VPC network connected by this association
  * The name, project, or zone of the association



To change these details, delete the association and create another.

**Caution:** If you use the explicit Private Service Connect data path to inspect traffic targeting load balancers, such as cross-region internal Application Load Balancers, remove the Service Extension (the `LBTCPExtension` resource) from your load balancer before you disable the firewall endpoint association. For more information, see [Disable application layer inspection for a load balancer](https://docs.cloud.google.com/firewall/docs/global-network-app-lb#disable-application-layer-inspection). 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.firewallEndpointAssociations.update`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your Google Cloud project.

In the **Firewall endpoint associations** section, the table lists all the configured firewall endpoint associations for this project.

  3. Next to the firewall endpoint association that you want to update, click **Edit**.

  4. To disable the firewall endpoint association, clear the **Enable association** checkbox.

  5. To update the TLS inspection policy, select a new policy from the **TLS inspection policy** list.

  6. Click **Save**.




###  gcloud 

To update a firewall endpoint association, use the [`gcloud network-security firewall-endpoint-associations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/update).
    
    
    gcloud network-security firewall-endpoint-associations update NAME \
      --project PROJECT_ID \
        [ --disabled ] \
        [ --tls-inspection-policy projects/TLS_PROJECT_NAME/locations/REGION_NAME/tlsInspectionPolicies/TLS_POLICY_NAME ] \
      --location LOCATION
    

Replace the following:

  * `NAME`: the name of the firewall endpoint association.

  * `PROJECT_ID`: the project ID where the association is created.

  * `TLS_PROJECT_NAME`: the project name of the TLS inspection policy.

  * `REGION_NAME`: the region name of the TLS inspection policy.

  * `TLS_POLICY_NAME`: the name of the TLS inspection policy.

  * `LOCATION`: the location of the firewall endpoint association.




### Delete a firewall endpoint association

To delete a firewall endpoint association, use the Google Cloud console or the gcloud CLI.

When a Google Cloud project is deleted, its associated firewall endpoint associations are automatically removed. This deletion is irreversible, even if the project is later restored.

However, the deletion process for these associations might sometimes fail. If this happens and the project is restored, the associated firewall endpoints appear in `ORPHAN` state within the restored project. This indicates the broken link between the project and its resources due to the unsuccessful deletion.

You can view these orphaned associations in the Google Cloud console, but you can't edit them. Cloud Next Generation Firewall periodically runs a background process that deletes these orphaned resources.

**Caution:** If you use the explicit Private Service Connect data path to inspect traffic targeting load balancers, such as cross-region internal Application Load Balancers, remove the Service Extension (the `LBTCPExtension` resource) from your load balancer before you delete the firewall endpoint association. For more information, see [Disable application layer inspection for a load balancer](https://docs.cloud.google.com/firewall/docs/global-network-app-lb#disable-application-layer-inspection). 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your project.

**Permissions**

  * `networksecurity.firewallEndpointAssociations.delete`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your Google Cloud project.

In the **Firewall endpoint associations** section, the table lists all the configured firewall endpoint associations for this project.

  3. Select the firewall endpoint association, and then click **Delete**.

  4. Click **Delete** again to confirm.




###  gcloud 

To delete a firewall endpoint association, use the [`gcloud network-security firewall-endpoint-associations delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/delete).
    
    
    gcloud network-security firewall-endpoint-associations delete NAME \
        --project PROJECT_ID \
        --location LOCATION
    

Replace the following:

  * `NAME`: the name of the firewall endpoint association.

  * `PROJECT_ID`: the project ID where the association exists.

  * `LOCATION`: the location of the firewall endpoint association.




## What's next

  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Use hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies)
  * [Use global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
