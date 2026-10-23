---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets/
title: Configure and manage subnets \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:58.144817+00:00
---

# Configure and manage subnets  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure and manage subnets

This document describes how to create and manage different subnets in VMware Engine.

There are three types of subnets: workload subnets, service subnets, and management workload subnets.

## Workload subnets

For workload virtual machines (VMs), you must create network segments on NSX Manager for your private cloud. Network segments created in NSX Manager aren't visible in VMware Engine.

### Access NSX Manager

The process of creating a subnet happens in NSX, which you access through VMware Engine:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud you want to create a subnet for.

  3. Click the private cloud name where you want to create the subnet.

  4. Under **Management appliances** , copy the **URL** corresponding to NSX Manager.

  5. Paste that URL in a VM that has access to the VMware Engine management network and can solve the DNS for the NSX Manager. NSX Manager can only be accessed from a VM on the management network, and can't be accessed directly from the Google Cloud console.

  6. When prompted, enter your sign-in credentials. As a reminder, you can [retrieve generated credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client#sign-in) from the private cloud details page.




If you've set up NSX to use an identity source, such as Active Directory, use your identity source credentials instead.

### Create a workload network segment

For workload VMs, create subnets as NSX network segments for your private cloud:

  1. In NSX, go to **Networking > Segments**.
  2. Click **Add Segment**.
  3. In the **Segment Name** field, enter a name for your segment.
  4. In the **Connected Gateway** list, select **Tier1** to connect to the tier-1 gateway.
  5. In the **Transport zone** list, select **TZ-OVERLAY | Overlay**.
  6. In the **Subnets** column, enter the subnet range. Specify the subnet range with `.1` as the last octet. For example, `10.12.2.1/24`.
  7. Click **Set DHCP Config** , and provide values for the **DHCP Ranges** field.
  8. Click **Apply** to save your DHCP configuration.
  9. Click **Save**. You can now select this network segment in vCenter when creating a VM.



In a given region, you can advertise at most **100** unique routes from VMware Engine to your VPC network using private services access. For example, those unique routes include private cloud management IP address ranges, NSX workload network segments, and HCX internal IP address ranges. This route limit includes all private clouds in the region and corresponds to the Cloud Router learned route limit.

For information about routing limits, see [Cloud Router Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

## Service subnets

Service subnets are `userDefined` subnets that VMware Engine automatically created when your Private Cloud is created. You can target using service subnets for appliance or service deployment scenarios, such as storage, backup, disaster recovery (DR), media streaming, and providing high scale linear throughput and packet processing for even the largest scaled private clouds. The available service subnet names are:

  * `service-1`
  * `service-2`
  * `service-3`
  * `service-4`
  * `service-5`



Virtual Machine communication across a service subnet exits the VMware ESXi host directly into the Google Cloud networking infrastructure, enabling high speed communication.

**Note:** NSX gateway and distributed firewall rules don't apply to any service subnets.

### Configuring service subnets

When VMware Engine creates a service subnet, it doesn't allocate a CIDR range or prefix. You must specify a non-overlapping CIDR range and prefix. The first usable address will become the gateway address. To allocate a CIDR range and prefix, edit one of the service subnets.

Service subnets can be updated if CIDR requirements change. Modification of an existing service subnet CIDR may cause network availability disruption for VMs attached to that service subnet.

### Configuring vSphere distributed port groups

Additionally, to connect a VM to a service subnet, you need to create a new Distributed Port Group. This port group maps the service subnet ID to a network name within a vCenter private cloud. To do this:

  1. Connect to the VMware vCenter Interface, see Accessing management appliances.
  2. Navigate to the network configuration section of the vCenter interface.
  3. Select Datacenter-dvs, Select New Distributed Port Group.



After the distributed port group has been created, you can attach VMs by selecting the corresponding name in the network configuration of the VM properties. The following are Distributed Port Group critical configuration values:

  * **Port binding** : static binding
  * **Port allocation** : elastic
  * **Number of ports** : 120
  * **VLAN type** : VLAN
  * **VLAN ID:** the corresponding subnet ID within the subnets section of the Google Cloud VMware Engine interface.



#### Google Cloud CLI and API requirements

To use the `gcloud` command line tool or the API to manage your VMware Engine resources, we recommend configuring the tools as described below.

###  gcloud 

  1. Set your default project ID:
         
         gcloud config set project PROJECT_ID
         

  2. Set a default region and zone:
         
         gcloud config set compute/region REGION
         
         
         gcloud config set compute/zone ZONE
         




For more information on the `gcloud vmware` tool, [see the Cloud SDK reference docs](https://docs.cloud.google.com/sdk/gcloud/reference/vmware).

###  API 

API examples in this documentation set use the `cURL` command-line tool to query the API. A valid access token is required as part of the `cURL` request. There are many ways to get a valid access token; the following steps use the `gcloud` tool to generate a access token:

  1. Login to Google Cloud:
         
         gcloud auth login
         

  2. Generate access token and export to TOKEN:
         
         export TOKEN=`gcloud auth print-access-token`
         

  3. Verify that TOKEN is set properly:
         
         echo $TOKEN
         




Now, use the authorization token in your requests to the API. For example:
    
    
    curl -X GET -H "Authorization: Bearer \"$TOKEN\"" -H "Content-Type: application/json; charset=utf-8" https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations
    

### Python

Python code samples in this documentation use the [VMware Engine library](https://cloud.google.com/python/docs/reference/vmwareengine/latest) to communicate with the API. To be able to use this approach, the library needs to be installed and the [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) should be configured.

  1. Download and install the Python library:
         
         pip install google-cloud-vmwareengine
         

  2. Configure the ADC information by executing those command in your shell:
         
         gcloud auth application-default login
         

Or, use a Service Account key file:
         
         export GOOGLE_APPLICATION_CREDENTIALS="FILE_PATH"
         




For more information about the library, visit the [reference page](https://docs.cloud.google.com/python/docs/reference/vmwareengine/latest) or view [code samples on GitHub](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/vmwareengine/cloud-client).

You can configure a `userDefined` subnet using the Google Cloud console, Google Cloud CLI or VMware Engine API. You will need to know the name of the subnet and private cloud.

###  Console 

  1. In the Google Cloud console, go to the **Subnets** page.

[Go to Subnets](https://console.cloud.google.com/vmwareengine/subnets)

  2. Click **Select a project** and then select the organization, folder, or project that contains the private cloud and subnet details.

  3. Look for the `userDefined` subnet you want to edit and click the pencil icon to edit the subnet.




###  gcloud 

Edit a subnet using the Google Cloud CLI using the [`gcloud vmware private-clouds subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/update):
    
    
    gcloud vmware private-clouds subnets update SUBNET_NAME \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE \
      --ip-cidr-range=`IP_ADDRESS`

Replace the following:

  * `SUBNET_NAME`: the name of the subnet to update in this private cloud
  * `PRIVATE_CLOUD_ID`: the name for the private cloud
  * `ZONE`: the zone for the private cloud
  * `IP_ADDRESS`: the IP address and range, for the example `10.0.0.0/24`



###  API 

To edit a subnet using the VMware Engine API, make a `PATCH` request:
    
    
     curl -sSL -XPATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json; charset=utf-8"
     "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/subnets/SUBNET_NAME?update_mask=ip_cidr_range" -d '{
        "ip_cidr_range": "IP_ADDRESS"
     }'

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_ID`: the name for the private cloud
  * `SUBNET_NAME`: the name of the subnet to update in this private cloud
  * `IP_ADDRESS`: the IP address and range, for the example `10.0.0.0/24`



## Management subnets

Management subnets are read-only subnets that you can view using the Google Cloud CLI or VMware Engine API.

## List all subnets

View a list of subnets in the Google Cloud console, Google Cloud CLI, or the API.

###  Console 

View a list of subnets by going to the **Subnets** page, clicking **Select a project** , and then selecting the organization, folder, or project that contains the private cloud and subnet details.

[Go to Subnets](https://console.cloud.google.com/vmwareengine/subnets)

###  gcloud 

List a subnet using the Google Cloud CLI by entering the [`gcloud vmware private-clouds subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/list):
    
    
    gcloud vmware private-clouds subnets list \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `PRIVATE_CLOUD_ID`: the name for the private cloud
  * `ZONE`: the zone for the private cloud



###  API 

To list a subnet using the VMware Engine API, make a `GET` request:
    
    
     curl -sSL -XGET -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json; charset=utf-8"
     "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/subnets"

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `ZONE`: the zone for the private cloud
  * `PRIVATE_CLOUD_ID`: the name for the private cloud



### Describe a subnet

Get a description of any subnet using the Google Cloud CLI or VMware Engine API.

###  Console 

Get the description of a subnet by going to the **Subnets** page, clicking **Select a project** , and then selecting the organization, folder, or project that contains the private cloud and subnet details.

[Go to Subnets](https://console.cloud.google.com/vmwareengine/subnets)

###  gcloud 

Get the description of a subnet using the [`gcloud vmware private-clouds subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/subnets/describe):
    
    
    gcloud vmware private-clouds subnets describe SUBNET_NAME \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `SUBNET_NAME`: the name of the subnet to update in this private cloud
  * `PRIVATE_CLOUD_ID`: the name for the private cloud
  * `ZONE`: the zone for the private cloud



###  API 

To get the description of a subnet using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateClouds/PRIVATE_CLOUD_ID/subnets/SUBNET_NAME"
    

Replace the following:

  * `PROJECT_ID`: the project name for this request
  * `REGION`: the region of the network
  * `PRIVATE_CLOUD_ID`: the name for the private cloud
  * `SUBNET_NAME`: the name for the subnet to update in this private cloud



## What's next

  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
