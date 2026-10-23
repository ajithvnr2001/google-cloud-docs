---
url: https://docs.cloud.google.com/vpc/docs/disable-hybrid-subnet-routing/
title: Disable hybrid subnet routing \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:51.203111+00:00
---

# Disable hybrid subnet routing  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/disable-hybrid-subnet-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Disable hybrid subnet routing

This page describes how to disable hybrid subnet routing when you have completed a migration supported by Hybrid Subnets.

If you no longer need Hybrid Subnets functionality—for example, because all workloads in the on-premises network have either migrated to Google Cloud or been decommissioned—you can disable hybrid subnet routing. Disabling hybrid subnet routing restores standard routing behavior for the subnet that uses hybrid subnet routing and lets you remove temporary migration configuration.

While you can keep hybrid subnet routing enabled indefinitely, Google recommends disabling it to avoid unnecessary charges, simplify your network architecture, and remove complexity such as managing custom advertised routes.

## Required roles

To get the permissions that you need to disable hybrid subnet routing, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Update Cloud Router route advertisements

If you want to disable hybrid subnet routing while maintaining connectivity between your migrated workloads and the on-premises network, you must update your custom route advertisements.

To update Cloud Router custom route advertisements, do the following:

  1. [Remove the custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-removing-routes) that you configured for migrated workloads.

  2. Ensure that you continue to advertise the subnet range of the subnet that had hybrid subnet routing enabled. You can do this in one of the following ways:

     * Configure the relevant BGP sessions to use subnet range advertisement.

     * Configure the relevant BGP sessions to use custom advertisement, but continue to advertise subnet ranges.

     * Configure the relevant BGP sessions to use custom advertisement without advertising subnet ranges, but use custom advertised routes that include the subnet range.

For information about configuring your BGP session to use one of these advertisement methods, see [Advertise custom address ranges](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip).




### Disable hybrid subnet routing

To disable hybrid subnet routing for a subnet, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network that contains the subnet that you want to update.

  3. Click the **Subnets** tab.

  4. Click the subnet that you want to update.

  5. Click **Edit**.

  6. In the **Hybrid subnet** section, select **Off**.

  7. Click **Save**.




###  gcloud 

Use the [`gcloud compute networks subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --region=REGION \
        --no-allow-cidr-routes-overlap
    

Replace the following:

  * `SUBNET`: the name of the subnet.
  * `REGION`: the region of the subnet.



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
    

  2. Disable `allowSubnetCidrRoutesOverlap`.

Before using any of the request data, replace `SUBNET_FINGERPRINT` with the fingerprint ID of your subnet that you found in the previous request—for example, `YiItidAFRsA5`.

HTTP method and URL: 
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME

Request JSON body: 
         
         {
           "allowSubnetCidrRoutesOverlap": false,
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
           "targetLink": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/subnetworks/subnet-name-abceefg",
           "targetId": "5514771331600183201",
           "status": "RUNNING",
           "user": "user@gmail.com",
           "progress": 0,
           "insertTime": "2023-03-31T11:40:03.882-07:00",
           "startTime": "2023-03-31T11:40:03.893-07:00",
           "selfLink": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1/operations/operation-1680288003494-5f8368991917a-59bf1c92-1897c7c6",
           "region": "https://www.googleapis.com/compute/v1/projects/test-project/regions/us-central1"
         }
         

  3. To verify that `allowSubnetCidrRoutesOverlap` is disabled for your subnet, make another `GET` request and ensure that the response includes the following:

     * `"allowSubnetCidrRoutesOverlap": false`



## Remove unnecessary configuration

Consider the following:

  * If you don't need proxy ARP for another purpose, you can disable proxy ARP. For information about disabling proxy ARP, see the documentation of your proxy ARP solution.
  * If you no longer need connectivity between your on-premises and VPC networks, you can disconnect the two networks. To disconnect the networks, complete the following steps.

    1. Do one of the following, depending on how you've configured connectivity:

       * [Delete the HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway#delete-ha-gw)
       * [Delete the VLAN attachment for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/delete-vlan-attachments)
       * [Delete the Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/deleting-interconnects)
    2. If you no longer need Cloud Routers that you configured for Hybrid Subnets, you can [delete them](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers#delete_routers).

    3. If you no longer need the firewall configuration that you added to support Hybrid Subnets, you can remove it.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
