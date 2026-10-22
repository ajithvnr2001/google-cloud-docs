---
url: https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints/
title: Create and update Outbound Endpoints \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:09.301225+00:00
---

# Create and update Outbound Endpoints  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/create-update-outbound-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create and update Outbound Endpoints Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to create, update, and associate Outbound Endpoints with forwarding zones and DNS server policies to enable direct forwarding of DNS queries using private IP addresses from your VPC network. By using this approach, you gain more granular control over outbound traffic. For more information about Outbound Endpoints, see [Outbound Endpoints overview](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview).

## Before you begin

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.outboundEndpoints.get`
  * `dns.outboundEndpoints.list`
  * `dns.outboundEndpoints.create`
  * `dns.outboundEndpoints.update`
  * `dns.outboundEndpoints.delete`
  * `dns.outboundEndpoints.bindPrivateDNSZone`
  * `dns.outboundEndpoints.bindPrivateDNSPolicy`
  * `compute.networks.get`
  * `compute.subnetworks.get`
  * `compute.subnetworks.use`



**Roles**

  * `roles/compute.networkAdmin`
  * `roles/dns.admin`



  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Cloud DNS, Compute Engine, and Network Services APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dns.googleapis.com,compute.googleapis.com,networkservices.googleapis.com)




Make sure you have a VPC network with connectivity to your on-premises or external DNS name servers. In each region where you plan to deploy an Outbound Endpoint, your VPC network must have a regular and proxy-only subnet in the target region. For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

Also ensure your on-premises network has a return route for the regional proxy-only subnet IP address range and configure on-premises firewall rules to allow inbound DNS queries (UDP and TCP port 53) from the regional proxy-only subnet IP address range.

## Create an Outbound Endpoint

To create an Outbound Endpoint, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Go to the **Outbound endpoints** tab and click **Create outbound endpoint**.

  3. In the **Name** field, enter a unique name for the endpoint.

  4. (Optional) For the **Description** field, enter a description for the endpoint.

  5. For **Region** , select the target region.

  6. In the **Network** list, select your VPC network.

  7. For **Subnet** , select the regular subnet in the selected region.

  8. For **Endpoint IP address** , enter a valid IPv4 address string from the selected subnet range.

**Note:** The endpoint IP address used to place the Outbound Endpoint in the networking stack is _not_ used for DNS query egress. Outbound DNS queries only egress from the proxy-only subnet IP address range.
  9. For **Proxy-only subnet** , the Console automatically detects the regional proxy-only subnet in the selected VPC network and region for outbound query egress. If a proxy-only subnet isn't detected, click **Reserve subnet** to create one before continuing.

  10. Click **Create**.




###  gcloud 

Run the `gcloud beta dns outbound-endpoints create` command:
    
    
    gcloud beta dns outbound-endpoints create ENDPOINT_NAME \
        --project=PROJECT_ID \
        --network=VPC_NETWORK \
        --subnetwork=REGULAR_SUBNET \
        --location=REGION \
        --endpoint-ip=IP_ADDRESS \
        --description=DESCRIPTION
    

Replace the following:

  * `ENDPOINT_NAME`: name of the Outbound Endpoint
  * `PROJECT_ID`: your project ID
  * `VPC_NETWORK`: VPC network associated with the Outbound Endpoint, for example, `projects/PROJECT_ID/global/networks/NETWORK_NAME` or just `NETWORK_NAME`
  * `REGULAR_SUBNET`: the regular subnet from which the endpoint's internal listening IP address is allocated, for example, `projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME` or just `SUBNET_NAME`
  * `REGION`: region where the endpoint is deployed
  * `IP_ADDRESS`: an available internal IPv4 address from the regular subnet's primary IP address range
  * `DESCRIPTION`: an optional description for the endpoint



###  API 

Run the `outboundEndpoints.create` method:
    
    
    POST https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/locations/REGION/outboundEndpoints?outboundEndpointId=ENDPOINT_NAME
    {
        "network": "projects/PROJECT_ID/global/networks/VPC_NETWORK",
        "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/REGULAR_SUBNET",
        "endpointIp": "IP_ADDRESS",
        "description": "DESCRIPTION"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed
  * `ENDPOINT_NAME`: name of the Outbound Endpoint
  * `VPC_NETWORK`: VPC network associated with the Outbound Endpoint
  * `REGULAR_SUBNET`: the regular subnet from which the endpoint's internal listening IP address is allocated
  * `IP_ADDRESS`: an available internal IPv4 address from the regular subnet's primary IP range
  * `DESCRIPTION`: an optional description for the endpoint



## Update an Outbound Endpoint

To update an Outbound Endpoint, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Go to the **Outbound endpoints** tab and click the name of the Outbound Endpoint that you want to update.

  3. Click **Edit** , update the **Description** field, and click **Save**.




###  gcloud 

Run the `gcloud beta dns outbound-endpoints update` command:
    
    
    gcloud beta dns outbound-endpoints update ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --description=UPDATED_DESCRIPTION
    

Replace the following:

  * `ENDPOINT_NAME`: name of the Outbound Endpoint to be updated
  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed
  * `UPDATED_DESCRIPTION`: optional updated description for the endpoint

**Note:** The region, project, network, subnet, and `--endpoint-ip` fields can't be changed on an existing endpoint. You must delete the existing endpoint and create a new one to change these values.

###  API 

Run the `outboundEndpoints.patch` method:
    
    
    PATCH https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/locations/REGION/outboundEndpoints/ENDPOINT_NAME?updateMask=description
    {
        "description": "UPDATED_DESCRIPTION"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed
  * `ENDPOINT_NAME`: name of the Outbound Endpoint to be updated
  * `UPDATED_DESCRIPTION`: updated description of the Outbound Endpoint

**Note:** The `PATCH` method only supports updating the description of an Outbound Endpoint. To change the region, network, subnet, or endpoint IP address, you must delete the existing endpoint and create a new one.

## Associate endpoints with a forwarding zone

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Go to the **Zones** tab and click **Create zone** , or select an existing forwarding zone and click **Edit**.

  3. Configure the zone parameters:

     1. For **Zone type** , select **Private**.
     2. For **Zone name** , enter a unique identifier for the zone.
     3. For **DNS name** , enter the domain suffix you want to forward. For example, `corp.example.com`.
     4. (Optional) For **Description** , enter a description.
     5. For **Options** , select **Forward queries to another server**.
     6. For **Networks** , select the VPC networks authorized to resolve queries against this zone.
  4. Under **Destination DNS servers** , enter the target IPv4 addresses or FQDNs of your external/on-premises name servers.

  5. For **Forwarding path** , select **Outbound Endpoints**.

  6. Under **Outbound Endpoints** , select one or more endpoints to handle query forwarding:

     * **Minimum selection** : select at least one Outbound Endpoint (required when Outbound Endpoints is chosen as the forwarding path).
     * **Single VPC constraint** : all selected endpoints must belong to the same VPC network.
     * **High availability (HA) best practice** : for cross-region disaster recovery and automatic failover, configure and select at least two endpoints in different regions within that VPC network.
  7. Click **Create** (or **Save** for an existing zone).




###  gcloud 

Associate endpoints with a forwarding zone by using the [`gcloud beta dns managed-zones update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/managed-zones/update):
    
    
    gcloud beta dns managed-zones update ZONE_NAME \
        --project=PROJECT_ID \
        --outbound-endpoints=projects/PROJECT_ID/locations/REGION_1/outboundEndpoints/ENDPOINT_NAME_1,projects/PROJECT_ID/locations/REGION_2/outboundEndpoints/ENDPOINT_NAME_2
    

Replace the following:

  * `ZONE_NAME`: name of the forwarding zone to be updated
  * `PROJECT_ID`: your project ID
  * `REGION_1` and `REGION_2`: regions where the endpoints are deployed
  * `ENDPOINT_NAME_1`: name of the first endpoint to be associated with the forwarding zone
  * `ENDPOINT_NAME_2`: name of the second endpoint to be associated with the forwarding zone



###  API 

Run the [`managedZones.patch`](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/patch) method:
    
    
    PATCH https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/managedZones/ZONE_NAME
    {
        "name": "ZONE_NAME",
        "dnsName": "DNS_NAME",
        "description": "DESCRIPTION",
        "visibility": "private",
        "forwardingConfig": {
            "outboundEndpoints": [
                  {
                     "name": "projects/PROJECT_ID/locations/REGION_1/outboundEndpoints/ENDPOINT_NAME_1"
                  },
                  {
                     "name": "projects/PROJECT_ID/locations/REGION_2/outboundEndpoints/ENDPOINT_NAME_2"
                  }
            ]
        }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE_NAME`: name of the forwarding zone to be updated
  * `DNS_NAME`: DNS name for the forwarding zone
  * `DESCRIPTION`: (optional) updated description of the forwarding zone
  * `REGION_1` and `REGION_2`: regions where the endpoints are deployed (all listed Outbound Endpoints in `forwardingConfig` must belong to the same VPC network)
  * `ENDPOINT_NAME_1`: name of the first endpoint to be associated with the forwarding zone
  * `ENDPOINT_NAME_2`: name of the second endpoint to be associated with the forwarding zone



## Associate endpoints with a DNS server policy

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Go to the **DNS server policies** tab and click **Create Policy** (or select an existing DNS server policy and click **Edit**).

  3. Configure the following:

     1. For **Policy name** , enter a unique name for the server policy.
     2. (Optional) For **Description** , enter a description.
     3. For **Inbound query forwarding** , specify whether external clients will query VPC workloads using inbound endpoints.
     4. For **DNS64** , enable or disable IPv6 synthesis as needed.
     5. For **Logs** , enable or disable DNS logging as needed.
     6. For **VPC networks** , select the VPC networks to which the server policy applies.
  4. Under **Alternative DNS servers** , enter the target IPv4 addresses of your external or on-premises name servers.

  5. For **Forwarding path** , select **Outbound Endpoints**.

  6. Under **Outbound Endpoints** , select one or more endpoints to route all non-private VPC queries:

     * **Minimum selection** : select at least one Outbound Endpoint.
     * **Single VPC constraint** : all selected endpoints must belong to the same VPC network.
     * **High availability (HA) best practice** : for cross-region disaster recovery and automatic failover, configure and select at least two endpoints in different regions within that VPC network.
  7. Click **Create** (or **Save** for an existing policy).




###  gcloud 

Associate endpoints with a DNS server policy by using the [`gcloud beta dns policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/policies/update):
    
    
    gcloud beta dns policies update POLICY_NAME \
        --project=PROJECT_ID \
        --outbound-endpoints=projects/PROJECT_ID/locations/REGION_1/outboundEndpoints/ENDPOINT_NAME_1,projects/PROJECT_ID/locations/REGION_2/outboundEndpoints/ENDPOINT_NAME_2
    

Replace the following:

  * `POLICY_NAME`: name of the DNS server policy to be updated
  * `PROJECT_ID`: your project ID
  * `REGION_1` and `REGION_2`: regions where the endpoints are deployed
  * `ENDPOINT_NAME_1`: name of the first endpoint to be associated with the DNS server policy
  * `ENDPOINT_NAME_2`: name of the second endpoint to be associated with the DNS server policy



###  API 

Run the [`policies.patch`](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/patch) method:
    
    
    PATCH https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/policies/POLICY_NAME
    {
        "alternativeNameServerConfig": {
            "outboundEndpoints": [
                {"name": "projects/PROJECT_ID/locations/REGION_1/outboundEndpoints/ENDPOINT_NAME_1"},
                {"name": "projects/PROJECT_ID/locations/REGION_2/outboundEndpoints/ENDPOINT_NAME_2"}
            ]
        }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `POLICY_NAME`: name of the DNS server policy to be updated
  * `REGION_1` and `REGION_2`: regions where the endpoints are deployed
  * `ENDPOINT_NAME_1`: name of the first endpoint to be associated with the DNS server policy
  * `ENDPOINT_NAME_2`: name of the second endpoint to be associated with the DNS server policy



## View Outbound Endpoints

To list or describe Outbound Endpoints in a region, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Go to the **Outbound endpoints** tab to view all Outbound Endpoints in your project, their regions, networks, subnets, IP addresses, and health status.




###  gcloud 

To list all Outbound Endpoints in a region, run the `gcloud beta dns outbound-endpoints list` command:
    
    
    gcloud beta dns outbound-endpoints list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed



To view details of a specific Outbound Endpoint, run the `gcloud beta dns outbound-endpoints describe` command:
    
    
    gcloud beta dns outbound-endpoints describe ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: name of the Outbound Endpoint
  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed



###  API 

To list all Outbound Endpoints in a region, send a `GET` request:
    
    
    GET https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/locations/REGION/outboundEndpoints
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed



To view details of a specific Outbound Endpoint, send a `GET` request:
    
    
    GET https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/locations/REGION/outboundEndpoints/ENDPOINT_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed
  * `ENDPOINT_NAME`: name of the Outbound Endpoint



## Delete an Outbound Endpoint

Before you can delete an Outbound Endpoint, you must disassociate it from any forwarding zones or DNS server policies that reference it. For more information, see [Manage network resources associated with Outbound Endpoints](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview#manage-network-resources).

After disassociating the Outbound Endpoint from all forwarding zones and DNS server policies, follow these steps to delete the endpoint:

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/)

  2. Go to the **Outbound endpoints** tab.

  3. Select the Outbound Endpoint that you want to delete and click **Delete**.




###  gcloud 

Run the `gcloud beta dns outbound-endpoints delete` command:
    
    
    gcloud beta dns outbound-endpoints delete ENDPOINT_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `ENDPOINT_NAME`: name of the Outbound Endpoint to be deleted
  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed



###  API 

Use the `outboundEndpoints.delete` method:
    
    
    DELETE https://dns.googleapis.com/dns/v1beta2/projects/PROJECT_ID/locations/REGION/outboundEndpoints/ENDPOINT_NAME
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: region where the endpoint is deployed
  * `ENDPOINT_NAME`: name of the Outbound Endpoint to be deleted



## Troubleshoot

To find methods for diagnosing and resolving errors related to Outbound Endpoints, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting#outbound-endpoints).

## What's next

  * Learn more about [Outbound Endpoints](https://docs.cloud.google.com/dns/docs/outbound-endpoints-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
