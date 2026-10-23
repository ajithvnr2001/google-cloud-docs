---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-allocate-external-ip/
title: Reserve an external IP address \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:47.354489+00:00
---

# Reserve an external IP address  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-allocate-external-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reserve an external IP address

External IP addresses allow inbound connections from the internet to a workload virtual machine (VM) instance, an appliance, or a load balancer running in your private cloud. For example, if you run a web server on your workload VM, you can serve web traffic using an external IP address through the internet.

Traffic to and from your external IP addresses follows your [external access firewall rules](https://docs.cloud.google.com/vmware-engine/docs/preview/networking/external-access-rules).

**Note:** If two VMs that are in a single private cloud or in a single region that belongs to the same VMware Engine network have external IP addresses, the communication between the VMs occurs over private IP addresses.

Allocating an external IP address to a resource also provides the following benefits:

  * Distributed denial-of-service (DDoS) attack prevention. This protection is automatically enabled for the external IP address.
  * Always-on traffic monitoring and real-time mitigation of common network-level attacks.
  * Protection and mitigation of attacks across the entire scale of the global network. The network can be used to distribute and mitigate attack traffic across regions.



## Behavior

An external IP address can only be assigned to one internal IP address, and the external IP address is dedicated to that internal IP address until you unassign it. A resource associated with an external IP address always uses the external IP address for internet access. You can reserve up to 100 external IP addresses for the primary VPC network connected to VMware Engine.

By default, incoming traffic on an external IP address is denied, and only outbound internet access is allowed. To allow inbound traffic, [create an external access rule](https://docs.cloud.google.com/vmware-engine/docs/networking/external-access-rules#create-external-access-rule) for the external IP address to the specific port.

**Note:** VMware Engine doesn't support allocation of external IP addresses imported by [Bring your own IP (BYOIP)](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip).**Caution:** If you assign an external IP address to vCenter, NSX, or HCX Manager, keep in mind the following:

  * You can only assign rules to port 443 for vCenter and NSX.
  * Although not required, we strongly recommend opening port 443 for HCX as well.



## Before you begin

Before you can allocate an external IP address to a workload VM, you must create a [network policy](https://docs.cloud.google.com/vmware-engine/docs/preview/networking/network-policies) in the region that applies to your private cloud and enable the internet access service and the external IP address service.

## Reserve an external IP address

To reserve an external IP address for an internal workload VM or management appliance using the Google Cloud console, Google Cloud CLI or VMware Engine API, do the following:

###  Console 

To reserve an external IP address for an internal workload VM or management appliance using the Google Cloud console, complete these steps:

  1. In the Google Cloud console, go to the **External IP addresses** page.

[Go to External IP addresses](https://console.cloud.google.com/vmwareengine/externalips)

  2. Click **Select a project** and then select the organization, folder, or project where you want to reserve the external IP address.

  3. Click **Reserve**.

  4. In the **Name** field, enter a name to identify the external IP address.

  5. In the **Private cloud** list, select the private cloud that contains the workload VM or management appliance.

  6. In the **Target workload or appliance VM** field, enter the itnernal IP address that you want to assign this external IP address.

  7. Click **Reserve**. The newly reserved external IP address appears in the list of external IP addresses.




###  gcloud 

To reserve an external IP address for an internal workload VM or management appliance, use the [`gcloud vmware private-clouds external-addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/create):
    
    
    gcloud vmware private-clouds external-addresses create EXTERNAL_ADDRESS_NAME \
      --internal-ip=IP_ADDRESS \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `EXTERNAL_ADDRESS_NAME`: the name for this external IP address
  * `IP_ADDRESS`: the internal IP address that this corresponds to, for example `192.168.1.11`, for this request
  * `PRIVATE_CLOUD_ID`: the name for this private cloud
  * `ZONE`: the zone for this request



###  API 

To reserve an external IP address for an internal workload VM or management appliance using the VMware Engine API, make a `POST` request:
    
    
      POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/externalAddresses?EXTERNAL_ADDRESS_NAME=EXTERNAL_ADDRESS_NAME"
    
    
    
    '{
         "internal_ip": "IP_ADDRESS"
      }'

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone for this request
  * `PRIVATE_CLOUD_ID`: the name for this private cloud
  * `EXTERNAL_ADDRESS_NAME`: the name for this external IP address
  * `IP_ADDRESS`: the internal IP address that this corresponds to, for example `192.168.1.11`, for this request



**Note:** The external IP address doesn't need to exist when you allocate the external IP address. For example, you can create a VM with the external IP address later. However, the subnet that the external IP address belongs to must exist on the selected private cloud.

## List an external IP address

To see a list of all external IP addresses using the Google Cloud console, Google Cloud CLI or VMware Engine API, do the following:

###  Console 

View a list of all external IP addresses by going to the **External IP addresses** page, clicking **Select a project** , and then selecting the organization, folder, or project where you want to list the external IP addresses.

[Go to External IP addresses](https://console.cloud.google.com/vmwareengine/externalips)

###  gcloud 

If you want to list all external IP addresses, use the [`gcloud vmware private-clouds external-addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/list):
    
    
    gcloud vmware private-clouds external-addresses list \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `PRIVATE_CLOUD_ID`: the name for this private cloud
  * `ZONE`: the zone for this request



###  API 

If you want to list all external IP addresses using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/externalAddresses"

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone for this request
  * `PRIVATE_CLOUD_ID`: the name for this private cloud



## Edit an external address

You can only edit the description and the internal IP attached to an existing external IP resource. You cannot change any other properties.

###  Console 

To edit an IP address:

  1. In the Google Cloud console, go to the **External IP addresses** page.

[Go to External IP addresses](https://console.cloud.google.com/vmwareengine/externalips)

  2. Click **Select a project** and then select the organization, folder, or project that contains the external IP address you want to edit.

  3. Click the **More** more_vert icon at the end of a row and select **Edit**.




###  gcloud 

If you want to edit an external IP addresses, use the [`gcloud vmware private-clouds external-addresses update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/update):
    
    
    gcloud vmware private-clouds external-addresses update EXTERNAL_ADDRESS_NAME \
      --internal-ip=IP_ADDRESS

###  API 

If you want to edit an external address using the VMware Engine API, make a `PATCH` request:
    
    
    PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/externalAddresses/EXTERNAL_ADDRESS_NAME?update_mask=internal_ip"
    
    '{
      "internal_ip": "IP_ADDRESS"
    }'

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone for this request
  * `PRIVATE_CLOUD_ID`: the name for this private cloud
  * `EXTERNAL_ADDRESS_NAME`: the name of the external IP for this request
  * `IP_ADDRESS`: the IP address, for example `192.168.1.11`, for this request



## Delete an external address

To delete an external address using the Google Cloud console, Google Cloud CLI or VMware Engine API, do the following:

###  Console 

To delete an external address using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **External IP addresses** page.

[Go to External IP addresses](https://console.cloud.google.com/vmwareengine/externalips)

  2. Click **Select a project** and then select the organization, folder, or project that contains the external IP address you want to delete.

  3. Click the **Delete** delete icon at the end of a row and select **Delete**.




###  gcloud 

To delete an external address using the Google Cloud console, use the [`gcloud vmware private-clouds external-addresses delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/external-addresses/delete):
    
    
    gcloud vmware private-clouds external-addresses delete EXTERNAL_ADDRESS_NAME \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `EXTERNAL_ADDRESS_NAME`: the external IP address ID for this request
  * `PRIVATE_CLOUD_ID`: the name for this private cloud
  * `ZONE`: the zone for this request



###  API 

To delete an external addresses using the VMware Engine API, make a `DELETE` request:
    
    
      DELETE "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/externalAddresses/EXTERNAL_IP_ADDRESS"

Replace the following:

  * `PROJECT_ID`: the project for this request
  * `ZONE`: the zone for this request
  * `PRIVATE_CLOUD_ID`: the name for this private cloud
  * `EXTERNAL_ADDRESS_NAME`: the name of the external IP for this request



## Outbound traffic configuration

Outbound traffic from the external IP address is allowed. Set up rules to control this traffic in NSX Manager.

## What's next

  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
