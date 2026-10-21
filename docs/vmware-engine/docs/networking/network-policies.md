---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/network-policies/
title: Create and manage network policies \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:20.477826+00:00
---

# Create and manage network policies  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/network-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage network policies

This document describes how to use network policies to control whether your VMware workloads can access or be accessed from the internet.

Each network policy is associated with a VMware Engine network, and VMware Engine networks can be either regional or global. _Standard VMware Engine Networks_ are global resources, while _Legacy VMware Engine Networks_ are regional.

A network policy applies to all private clouds associated with the VMware Engine network. For legacy networks, if you have private clouds deployed in more than one region and you want to enable internet access or the external IP address service, you must create a network policy in each region.

## Create a network policy

Create a network policy using the console, `gcloud`, or the API.

###  Console 

To create a new network policy using the Google Cloud console:

  1. In the Google Cloud console, go to the **Network policies** page.

[Go to Network policies](https://console.cloud.google.com/vmwareengine/network-policies)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to associate the network policy with.

  3. Click **Create**.

  4. Provide information about the new network policy:

     * **Network policy name:** a name to identify the network policy
     * **Network policy description:** a description of the network policy
     * **VMware Engine network:** the VMware Engine network to associate the policy with
     * **Region:** the region where you want the network policy to apply
  5. In the **Policy details** section, enable or disable network services:

     * **Internet access service:** When enabled, VMware Engine allows outbound traffic from internal IP addresses to the internet.
     * **External IP address service:** When enabled, VMware Engine lets you [reserve external IP addresses](https://docs.cloud.google.com/vmware-engine/docs/preview/networking/howto-allocate-external-ip) for internal IP addresses in the associated private cloud. External IP addresses provide inbound traffic access to internal IP addresses from the internet.

This service can only be enabled when the internet access service is also enabled.

**Note:** If you enable internet access and leave the external IP address service disabled, you won't be able to reserve external IP addresses for internal IP addresses covered by this network policy.
  6. In the **Edge services address range** field, enter the IP address range to use when addressing the VMware Engine public IP gateway (_/26_ address range).

  7. Click **Create**. VMware Engine begins creating your new network policy.




###  gcloud 

In `gcloud`, run the [`network-policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/create) command:
    
    
    gcloud vmware network-policies create NETWORK_POLICY_ID \
      --location LOCATION --vmware-engine-network NETWORK_ID \
      --edge-services-cidr=EDGE_SERVICES_CIDR [--external-ip-access] \
      [--internet-access]

Replace the following:

  * `NETWORK_POLICY_ID`: a name for this network policy
  * `LOCATION`: the location of this network policy; this must match the VMware Engine network
  * `NETWORK_ID`: the VMware Engine network name
  * `EDGE_SERVICES_CIDR`: the IP address range to use when addressing the VMware Engine public IP gateway (_/26_ address range)
  * `--external-ip-access`: whether to enable external IP addresses to be assigned to VMware workloads. Must also have `--internet-access` enabled.
  * `--internet-access`: whether VMWare workloads can access the internet



###  API 

In the API, make a `POST` request:
    
    
    POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/networkPolicies?networkPolicyId=NETWORK_POLICY_ID
    
    '{
      "internetAccess": INTERNET_ACCESS,
      "externalIp": EXTERNAL_IP,
      "vmwareEngineNetwork": "projects/PROJECT_ID/locations/LOCATION/vmwareEngineNetworks/NETWORK_ID"
      "edgeServicesCidr": "EDGE_SERVICES_CIDR"
    }'

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `LOCATION`: the location of this network policy; this must match the VMware Engine network
  * `NETWORK_POLICY_ID`: a name for this network policy
  * `INTERNET_ACCESS`: whether VMWare workloads can access the internet; set this to `true` or `false`
  * `EXTERNAL_IP`: whether to enable external IP addresses to be assigned to VMware workloads. Must also have `internetAccess` enabled; set this to `true` or `false`.
  * `NETWORK_ID`: the VMware Engine network name
  * `EDGE_SERVICES_CIDR`: the IP address range to use when addressing the VMware Engine public IP gateway (_/26_ address range)



## Edit a network policy

###  Console 

To edit an existing network policy using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Network policies** page.

[Go to Network policies](https://console.cloud.google.com/vmwareengine/network-policies)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to edit the network policy for.

  3. In the list of network policies, find the network policy that you want to edit.

  4. Click the **More** more_vert icon at the end of a row and select **Edit**.

  5. On the page that appears, adjust the network policy as you need.

  6. Click **Save**.




###  gcloud 

To update a network policy, use the [`network-policies update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/update):
    
    
    gcloud vmware network-policies update NETWORK_POLICY_ID \
      --location LOCATION \
      --edge-services-cidr=EDGE_SERVICES_CIDR [--external-ip-access] \
      [--internet-access]

Replace the following:

  * `NETWORK_POLICY_ID`: the name of the network policy
  * `LOCATION`: the location of this network policy
  * `EDGE_SERVICES_CIDR`: the IP address range to use when addressing the VMware Engine public IP gateway (_/26_ address range)
  * `--external-ip-access`: whether to enable external IP addresses to be assigned to VMware workloads. Must also have `--internet-access` enabled.
  * `--internet-access`: whether VMWare workloads can access the internet



###  API 

In the API, make a `PATCH` request:
    
    
    POST https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/networkPolicies?networkPolicyId=NETWORK_POLICY_ID
    
    '{
      "internetAccess": INTERNET_ACCESS,
      "externalIp": EXTERNAL_IP,
      "edgeServicesCidr": "EDGE_SERVICES_CIDR"
    }'

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `LOCATION`: the location of this network policy
  * `NETWORK_POLICY_ID`: the name of this network policy
  * `INTERNET_ACCESS`: whether VMWare workloads can access the internet; set this to `true` or `false`
  * `EXTERNAL_IP`: whether to enable external IP addresses to be assigned to VMware workloads. Must also have `internetAccess` enabled; set this to `true` or `false`.
  * `EDGE_SERVICES_CIDR`: the IP address range to use when addressing the VMware Engine public IP gateway (_/26_ address range)



## Delete a network policy

To delete an existing network policy, take the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Network policies** page.

[Go to Network policies](https://console.cloud.google.com/vmwareengine/network-policies)

  2. Click **Select a project** and then select the organization, folder, or project that contains the VMware Engine network you want to delete the network policy for.

  3. In the list of network policies, find the network policy that you want to delete.

  4. Click the **More** more_vert icon at the end of a row and select **Delete**.




###  gcloud 

In `gcloud`, use the [`network-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/network-policies/delete):
    
    
    gcloud vmware network-policies delete NETWORK_POLICY_ID

Replace `NETWORK_POLICY_ID` with the name of the network policy to delete.

###  API 

Make a `DELETE` request to the network policy resource:
    
    
    DELETE https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/networkPolicies/NETWORK_POLICY_ID
    

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `LOCATION`: the location of this network policy
  * `NETWORK_POLICY_ID`: the name of this network policy



## What's next

  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
