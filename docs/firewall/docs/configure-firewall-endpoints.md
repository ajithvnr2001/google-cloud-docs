---
url: https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints/
title: Create firewall endpoints and endpoint associations \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:45:38.126778+00:00
---

# Create firewall endpoints and endpoint associations  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create firewall endpoints and endpoint associations Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to create firewall endpoints and associate them with your Virtual Private Cloud (VPC) networks by using the Google Cloud console, the Google Cloud CLI, or Terraform.

To control network traffic and protect your virtual machine (VM) instances, you configure firewall endpoints and endpoint associations. After you create a firewall endpoint, you create a [zonal association](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#endpoint-association) to link the endpoint with one or more VPC networks in the same zone.

This document is intended for network administrators, security engineers, and security architects who configure network security and firewall endpoints.

## Before you begin

Before you configure firewall endpoints and associations, complete the following:

  * Review the concepts in the [Firewall endpoint overview](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints).
  * Ensure that you have a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) and a [subnet](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#specifications).
  * Enable the required APIs: 
    * [Compute Engine API (Compute Engine API)](https://console.cloud.google.com/apis/library/compute.googleapis.com) in your Google Cloud project.
    * [Network Security API](https://console.cloud.google.com/apis/library/networksecurity.googleapis.com) in the Google Cloud project that you want to use for billing.
    * [Certificate Authority Service API](https://console.cloud.google.com/apis/library/privateca.googleapis.com) in your Google Cloud project.
  * Install the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run `gcloud` command-line examples.



### Roles and permissions

To get the permissions that you need to create firewall endpoints, ask your administrator to grant you the necessary [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#iam-roles) on your organization or project. For more information, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To check the progress of the operations listed on this page, ensure that your user account has the [Compute Network User](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role, which includes the following permissions:

  * `networksecurity.operations.get`
  * `networksecurity.operations.list`



### Quotas

To view quotas for firewall endpoints and associations, see [Quotas and limits](https://docs.cloud.google.com/firewall/docs/quotas).

## Create a firewall endpoint

You create a firewall endpoint in a specific zone. To ensure proper traffic inspection and avoid routing failures, create the firewall endpoint in the same zone as the workloads you want to inspect.

You can create a firewall endpoint at the organization level or project level. Organization level endpoints support only organization-level security profile groups. Project-level endpoints support both organization-level and project-level security profile groups.

You can create a firewall endpoint with or without jumbo frame support. For information about the packet sizes supported by firewall endpoints, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

**Note:** Cloud NGFW can take up to 20 minutes to create a firewall endpoint.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.firewallEndpoints.create`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. Click **Open project picker** and select your organization or the project.

  3. If you selected the organization, click **Create organization-level endpoint**.

If you selected a project, in the **Firewall endpoints located in this project** section, click **Create project-level endpoint**.

  4. In the **Region** list, select the region where you want to create the firewall endpoint.

  5. In the **Zone** list, select the zone where you want to create the firewall endpoint.

  6. In the **Name** field, enter a name for the firewall endpoint.

Avoid sensitive information, such as personally identifiable information (PII) or security data, in the firewall endpoint name.
  7. If you're creating an organization-level endpoint, in the **Billing project** list, select the Google Cloud project that you want to use for billing the firewall endpoint.

  8. Click **Continue**. The **Advanced configuration** section opens.

  9. To enable Advanced malware sandbox support for the endpoint, select the **Enable Advanced malware sandbox (WildFire)** ([Preview](https://cloud.google.com/products#product-launch-stages)) checkbox.

     1. If the end-user license agreement (EULA) is not accepted for the selected project, click **Agree and continue** to accept the Advanced malware sandbox-specific EULA.

     2. Optional: Click the **Additional Advanced malware sandbox configurations** list and perform the following actions:

        * In the **Advanced malware sandbox region** list, select the region.
        * In the **Content cloud region** list, select the region.
        * In the **Signature lookup timeout** field, enter the timeout duration.
        * In the **Signature lookup timeout action** list, select `Allow` or `Deny`.
        * To block HTTP partial responses, select the **Block HTTP partial responses** checkbox.
        * In the **Inline cloud analysis max duration** field, enter the duration.
        * In the **Inline cloud analysis timeout action** list, select `Allow` or `Deny`.
        * To enable log generation for files that time out during Advanced malware sandbox inline cloud analysis, select the **Enable submission timeout logging** checkbox.
  10. If you want the endpoint to support jumbo frames, select the **Enable jumbo frames support** checkbox; otherwise, clear this checkbox.

  11. Click **Continue**.

  12. If you want to add a firewall endpoint association, click **Add endpoint association** ; otherwise, skip this step.

     1. In the **Project** list, select the Google Cloud project where you want to create the firewall endpoint association.
     2. If the Compute Engine API or Network Security API are not enabled for the Google Cloud project, click **Enable**.
     3. In the **Network** list, select the network that you want to associate with the firewall endpoint.
     4. In the **TLS inspection policy** list, select the TLS inspection policy that you want to add to this association.
     5. To add another association, click **Add endpoint association**.
  13. Click **Create**.




###  gcloud 

To create a firewall endpoint, use the [`gcloud network-security firewall-endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoints/create):
    
    
    gcloud network-security firewall-endpoints create NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --location LOCATION \
        [--billing-project QUOTA_PROJECT_ID] \
        [--enable-jumbo-frames]
    

Replace the following:

  * `NAME`: the name of the firewall endpoint.

Don't include sensitive information such as personally identifiable information or security data in the firewall endpoint name.

  * `ORGANIZATION_ID`: the organization ID. Use this flag to create an organization-level firewall endpoint.

  * `PROJECT_ID`: the project ID. Use this flag to create a project-level firewall endpoint.

  * `LOCATION`: the zone to create the endpoint.

  * `QUOTA_PROJECT_ID`: the quota project ID. Use this flag only for organization-level firewall endpoints.




To create a firewall endpoint that supports jumbo frames up to 8,500 bytes in size, use the optional `--enable-jumbo-frames` flag. Skip this flag to create an endpoint without jumbo frame support. For information about the packet sizes supported by firewall endpoints, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

To create a firewall endpoint that supports Advanced malware sandbox, use the [`gcloud beta network-security firewall-endpoints create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/create) ([Preview](https://cloud.google.com/products#product-launch-stages)):
    
    
    gcloud beta network-security firewall-endpoints create NAME \
        --organization ORGANIZATION_ID | --project PROJECT_ID \
        --zone ZONE \
        --enable-jumbo-frames \
        --enable-wildfire \
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



To associate the firewall endpoint to a VPC network, see [Create firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations#create-endpoint-association).

###  Terraform 

Use the [`google_network_security_firewall_endpoint` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_security_firewall_endpoint).
    
    
    resource "google_network_security_firewall_endpoint" "default" {
      name               = "my-firewall-endpoint"
      parent             = "organizations/123456789"
      location           = "us-central1-a"
      billing_project_id = "my-project-name"
      enable_jumbo_frames = true
    }
    

To create a firewall endpoint that supports jumbo frames up to 8,500 bytes in size, set the field `enable_jumbo_frames` to `true`. To create a firewall endpoint that doesn't support jumbo frames, set this field to `false`. For information about the packet sizes supported by firewall endpoints, see [Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size). To create a firewall endpoint that supports Advanced malware sandbox, set the field `enable_wildfire` to `True`.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Create a firewall endpoint association

A firewall endpoint association connects a firewall endpoint to a VPC network in a specific zone. This association ensures that traffic matching an interception rule for the associated network in that zone is inspected by the firewall endpoint.

Ensure that you have a [firewall endpoint](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints) before you create an association.

**Note:** Cloud NGFW can take up to 15 minutes to create a firewall endpoint associations.

### Association requirements

When you configure endpoint associations, follow these requirements:

  * **Zone constraints:** You must create the association in the same zone as the firewall endpoint. For effective traffic inspection, create associations in zones where your compute instances are deployed.
  * **One endpoint per zone:** In a single zone, you can associate a VPC network with only one firewall endpoint (either project-level or organization-level). However, you can associate a single VPC network with different firewall endpoints across multiple, different zones.
  * **Cross-project associations:** You can associate a VPC network with a firewall endpoint in a separate project. If you use a project-level endpoint, the endpoint's project must reside in the same organization as the VPC network.
  * **Resource mapping:** An association is a project-level resource. You create the association within the specific project where your compute instances are deployed, even if the association points to an organization-level firewall endpoint.

**Note:** When inspecting traffic targeting cross-region internal Application Load Balancers, the firewall endpoint association ignores any attached TLS inspection policy because the load balancer terminates TLS natively. For more information, see [TLS inspection with internal load balancers](https://docs.cloud.google.com/firewall/docs/about-tls-inspection#tls-inspection-lb).

A firewall endpoint with jumbo frame support can accept packets only up to 8,500 bytes. Alternatively, a firewall endpoint without jumbo frame support can accept packets only up to 1,460 bytes. If you need intrusion detection and prevention service, Advanced malware sandbox, or URL filtering service, we recommend that you configure the associated VPC networks to use the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) limits of 8,500 bytes and 1,460 bytes. For more information, see [ Supported packet size](https://docs.cloud.google.com/firewall/docs/about-firewall-endpoints#supported-packet-size).

**Caution:** A firewall endpoint doesn't perform intrusion detection and prevention service, Advanced malware sandbox, or URL filtering service for a VPC network if the network is configured with an MTU that's greater than the firewall endpoint's limit.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization or project.

**Permissions**

  * `networksecurity.firewallEndpointAssociations.create`
  * `networksecurity.firewallEndpoints.use` on the organization or the project where the firewall endpoint is created.



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`)
  * Firewall Endpoint Admin (`roles/networksecurity.firewallEndpointAdmin`) granted at the organization level for organization-level firewall endpoints, and at either the project level or the organization level for project-level firewall endpoints 



###  Console 

  1. In the Google Cloud console, go to the **Firewall endpoints** page.

[Go to Firewall endpoints](https://console.cloud.google.com/net-security/firewall-endpoints/list)

  2. In the project selector menu, select your Google Cloud project.

  3. Click **Create endpoint association**.

  4. In the **Region** list, select the region where you want to create the firewall endpoint association.

  5. In the **Zone** list, select the zone where you want to create the firewall endpoint association.

  6. In the **Firewall endpoint** list, select the firewall endpoint that you want to add to the association.

  7. In the **Network** list, select the network that you want to add to the association.

  8. In the **TLS inspection policy** list, select the TLS inspection policy that you want to add to this association.

  9. Click **Create**.


**Note:** You can also create firewall endpoint associations from the **Firewall endpoints** tab on the [VPC networks page](https://console.cloud.google.com/networking/networks/list).

###  gcloud 

To create a firewall endpoint association, use the [`gcloud network-security firewall-endpoint-associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/firewall-endpoint-associations/create).

**Organization-level firewall endpoint**
    
    
    gcloud network-security firewall-endpoint-associations \
        create NAME \
        --endpoint organizations/ORGANIZATION_ID/locations/LOCATION/firewallEndpoints/FIREWALL_ENDPOINT_NAME \
        --network projects/PROJECT_NAME/global/networks/NETWORK_NAME \
        --location LOCATION \
        --project PROJECT_ID \
        [ --tls-inspection-policy projects/TLS_PROJECT_NAME/locations/REGION_NAME/tlsInspectionPolicies/TLS_POLICY_NAME ]
    

**Project-level firewall endpoint**
    
    
    gcloud network-security firewall-endpoint-associations \
        create NAME \
        --endpoint projects/ENDPOINT_PROJECT_ID/locations/LOCATION/firewallEndpoints/FIREWALL_ENDPOINT_NAME \
        --network projects/PROJECT_NAME/global/networks/NETWORK_NAME \
        --location LOCATION \
        --project PROJECT_ID \
        [ --tls-inspection-policy projects/TLS_PROJECT_NAME/locations/REGION_NAME/tlsInspectionPolicies/TLS_POLICY_NAME ]
    

Replace the following:

  * `NAME`: the name of the firewall endpoint association.

Don't include sensitive information such as personally identifiable information or security data in the firewall endpoint association name.

  * `ORGANIZATION_ID`: the organization ID where the firewall endpoint exists. Use this flag only for an organization-level firewall endpoint.

  * `ENDPOINT_PROJECT_ID`: the project ID where the firewall endpoint exists. Use this flag only for a project-level firewall endpoint.

  * `LOCATION`: the zone where firewall endpoint exists.

  * `FIREWALL_ENDPOINT_NAME`: the name of the firewall endpoint.

  * `PROJECT_NAME`: the Google Cloud project name of the network.

  * `NETWORK_NAME`: the name of the network.

  * `PROJECT_ID`: the Google Cloud project ID where the association is created. This should be the project where you want to intercept traffic.

  * `TLS_PROJECT_NAME`: the Google Cloud project name of the TLS inspection policy.

  * `REGION_NAME`: the region name of the TLS inspection policy.

  * `TLS_POLICY_NAME`: the name of the TLS inspection policy.

This policy is used for the TLS inspection of the encrypted traffic on the specified network. This is an optional argument.




## What's next

  * [Create hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/using-firewall-policies)
  * [Manage hierarchical firewall policies and rules](https://docs.cloud.google.com/firewall/docs/manage-hierarchical-firewall-policies)
  * [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies)
  * [Manage global network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
