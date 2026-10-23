---
url: https://docs.cloud.google.com/vpc/docs/migrate-with-hybrid-subnets/
title: Migrate workloads to Google Cloud with Hybrid Subnets \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:39.215849+00:00
---

# Migrate workloads to Google Cloud with Hybrid Subnets  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/migrate-with-hybrid-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate workloads to Google Cloud with Hybrid Subnets

Hybrid Subnets helps you migrate workloads from an on-premises network to a Virtual Private Cloud (VPC) network without needing to change any IP addresses. This document describes the steps to configure hybrid subnet routing, test connectivity across the CIDR block that is shared by the on-premises and VPC networks, and migrate workloads from the on-premises network.

## Before you begin

Make sure that you have completed the steps in [Prepare for Hybrid Subnets connectivity](https://docs.cloud.google.com/vpc/docs/prepare-for-hybrid-subnet-connectivity).

## Enable hybrid subnet routing

To support internal connectivity between on-premises and VPC networks that share a CIDR block, you need at least one subnet that has [hybrid subnet routing](https://docs.cloud.google.com/vpc/docs/hybrid-subnets#routing) enabled.

The subnet that uses hybrid subnet routing must fulfill the following requirements:

  * It must be in the same region as the Cloud Router and the HA VPN tunnels or VLAN attachments that provide hybrid connectivity.
  * The IPv4 address range of the subnet must match the IP address range of the on-premises network that hosts the workloads you want to migrate.



You can enable hybrid subnet routing when you create a new subnet, or you can update an existing subnet to enable the feature.

### Create a new subnet with hybrid subnet routing enabled

To create a new subnet that has hybrid subnet routing enabled, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network where you want to configure hybrid subnet routing.

  3. Click the **Subnets** tab.

  4. Click **Add subnet**. In the panel that appears:

     1. Provide a name.
     2. Select a region.
     3. In the **Purpose** section, select **None**.
     4. In the **Stack type** section, select **IPv4 (single-stack)**.
     5. In the **IPv4 range** field, enter the CIDR block that is shared between this subnet and the workloads that you want to migrate.
     6. In the **Hybrid subnets** section, select **On**.
     7. Click **Add**.



###  gcloud 

Use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create SUBNET \
        --network=NETWORK \
        --region=REGION \
        --range=RANGE \
        --allow-cidr-routes-overlap
    

Replace the following:

  * `SUBNET`: the name of the subnet
  * `NETWORK`: the name of the subnet's VPC network
  * `RANGE`: the CIDR block that is shared between this subnet and the workloads that you want to migrate.
  * `REGION`: the region of the subnet



###  API 

  1. Create a new subnet with hybrid subnet routing enabled.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your project
     * REGION: the region of your subnet
     * SUBNET: the name of your subnet
     * NETWORK_NAME: the name of the subnet's VPC network
     * RANGE: the CIDR block that is shared between this subnet and the workloads that you want to migrate.

HTTP method and URL: 
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks

Request JSON body: 
    
    {
      "name": "SUBNET",
      "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
      "ipCidrRange": "RANGE",
      "allowSubnetCidrRoutesOverlap": true
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#operation",
      "id": "5973660558170953708",
      "name": "operation-1680288003494-5f8368991917a-59bf1c92-1897c7c6",
      "operationType": "insert",
      "targetLink": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/subnetworks/subnet-name",
      "targetId": "5514771331600183201",
      "status": "RUNNING",
      "user": "user@gmail.com",
      "progress": 0,
      "insertTime": "2023-03-31T11:40:03.882-07:00",
      "startTime": "2023-03-31T11:40:03.893-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/operations/operation-1680288003494-5f8368991917a-59bf1c92-1897c7c6",
      "region": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1"
    }
    




### Enable hybrid subnet routing for an existing subnet

To enable hybrid subnet routing for an existing subnet, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network that contains the subnet that you want to update.

  3. Click the **Subnets** tab.

  4. Click the subnet that you want to update.

  5. Click **Edit**.

  6. In the **Hybrid subnets** section, select **On**.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute networks subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --region=REGION \
        --allow-cidr-routes-overlap
    

Replace the following:

  * `SUBNET`: the name of the subnet
  * `REGION`: the region of the subnet



###  API 

  1. Find the `fingerprint` ID of your subnet.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your project
     * REGION: the region of your subnet
     * SUBNET_NAME: the name of your subnet

HTTP method and URL: 
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "compute#subnetwork",
      "id": "5514771331600183201",
      "creationTimestamp": "2022-09-16T12:41:02.010-07:00",
      "name": "subnet-name",
      "network": "https://www.googleapis.com/compute/v1/projects/project-name/global/networks/network-name",
      "ipCidrRange": "10.6.0.0/16",
      "gatewayAddress": "10.6.0.1",
      "region": "https://www.googleapis.com/compute/v1/projects/project-name/regions/us-central1",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/project-name/regions/us-central1/subnetworks/subnet-name",
      "privateIpGoogleAccess": true,
      "fingerprint": "YiItidAFRsA5",
      "allowSubnetCidrRoutesOverlap": false,
      "enableFlowLogs": true,
      "privateIpv6GoogleAccess": "DISABLE_GOOGLE_ACCESS",
      "purpose": "PRIVATE",
      "stackType": "IPV4_ONLY"
    }
    

  2. Enable hybrid subnet routing.

Before using any of the request data, replace SUBNET_FINGERPRINT with the fingerprint ID of your subnet that you found in the previous request—for example, `YiItidAFRsA5`.

HTTP method and URL: 
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME

Request JSON body: 
         
         {
           "allowSubnetCidrRoutesOverlap": true,
           "fingerprint": "SUBNET_FINGERPRINT"
         }
         

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         curl -X PATCH \  
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
              -H "Content-Type: application/json; charset=utf-8" \  
              -d @request.json \  
              "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
         
         $cred = gcloud auth print-access-token  
         $headers = @{ "Authorization" = "Bearer $cred" }  
           
         Invoke-WebRequest `  
             -Method PATCH `  
             -Headers $headers `  
             -ContentType: "application/json; charset=utf-8" `  
             -InFile request.json `  
             -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
         
         {
           "kind": "compute#operation",
           "id": "5973660558170953708",
           "name": "operation-1680288003494-5f8368991917a-59bf1c92-1897c7c6",
           "operationType": "compute.subnetworks.patch",
           "targetLink": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/subnetworks/subnet-name",
           "targetId": "5514771331600183201",
           "status": "RUNNING",
           "user": "user@gmail.com",
           "progress": 0,
           "insertTime": "2023-03-31T11:40:03.882-07:00",
           "startTime": "2023-03-31T11:40:03.893-07:00",
           "selfLink": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/operations/operation-1680288003494-5f8368991917a-59bf1c92-1897c7c6",
           "region": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1"
         }
         

  3. To verify that `allowSubnetCidrRoutesOverlap` is enabled for your subnet, make another `GET` request and ensure that the response includes the following:

     * `"allowSubnetCidrRoutesOverlap": true`



## Test network connectivity from your VPC network to your on-premises network

To test connectivity between your VPC network and the on-premises network across the shared CIDR block, you can do the following:

  1. [Create a test VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) in the subnet that uses hybrid subnet routing.
  2. [Note the primary internal IPv4 address](https://docs.cloud.google.com/compute/docs/instances/view-network-properties#view_ip_addresses) of the test VM.
  3. In the VPC network that contains your test VM, configure custom advertisement on the relevant Cloud Router BGP sessions, including a specific `/32` custom route advertisement that matches the primary internal IPv4 address of the test VM. For more information, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) and [Advertise custom address ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) in the Cloud Router documentation.
  4. Ensure that firewall rules in your on-premises network and in your VPC network allow connectivity (TCP and ICMP) from an on-premises system to the test VM.
  5. [Use SSH to connect to the VM](https://docs.cloud.google.com/compute/docs/instances/ssh).
  6. At the operating system prompt, use the `ping` command to test connectivity to a system in the on-premises network.



## Move workloads and update routing

Each time you migrate a workload or group of workloads, complete the following steps together.

### Migrate workloads

Migrate workloads and VMs from your on-premises network to your VPC network by using your preferred method.

For information about migration options, see [Migration options](https://docs.cloud.google.com/vpc/docs/hybrid-subnets#migrate-to-vms).

### Update custom advertised route

As you migrate VMs to Google Cloud, [update the custom advertised routes of your Cloud Router's BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-subnets#bgp-session) to include the primary internal IPv4 address of each migrated VM.

For contiguous IP address blocks, consolidate addresses into as few custom advertisements as possible. The advertisements must remain more specific (have longer subnet masks) than the IPv4 address range of the subnet that has hybrid subnet routing enabled.

## Test connectivity to a migrated VM from your on-premises network

To test connectivity to a VM that you migrated to Google Cloud, you can do the following:

  1. Make sure that you updated the custom advertisements for the BGP sessions that manage hybrid connectivity. The route advertisements must include the internal IP address of the migrated VM.
  2. Use the `ping` command to test connectivity from a system in your on-premises network to the IP address of the migrated VM.



## What's next

  * [Disable hybrid subnet routing](https://docs.cloud.google.com/vpc/docs/disable-hybrid-subnet-routing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
