---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-private-cloud-management-dns/
title: Configure Management DNS for private clouds \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:58.478830+00:00
---

# Configure Management DNS for private clouds  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-private-cloud-management-dns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Management DNS for private clouds

This document describes how to manage a private cloud's management DNS zone bindings. Use this document if you want to list, create, delete, update, or review DNS zone bindings. For more information on Cloud DNS, see [Configuring DNS for management appliance access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises).

## List management DNS zone bindings

You can list all the networks that are bound to the private cloud's management DNS zone. The private cloud VMware Engine network is automatically bound to the management DNS zone as part of private cloud creation. Any networks that are peered to the private cloud VMware Engine network are also automatically bound to the management DNS zone. The management DNS zone bindings that are created automatically have resource names of the type `auto-bind-xxxxxx`.

To list management DNS zone bindings using the Google Cloud CLI or VMware Engine API, do the following:

###  gcloud 

To list management DNS zone bindings using the Google Cloud CLI, use the [`gcloud vmware private-clouds management-dns-zone-bindings list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/list):
    
    
    gcloud vmware private-clouds management-dns-zone-bindings list \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `ZONE`: the zone for this request.



### API

To list management DNS zone bindings using the VMware Engine API, make a `GET` request:
    
    
      GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/managementDnsZoneBindings"
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.



## Create a management DNS zone binding

A VPC or a VMware Engine network can be bound to the management DNS zone. To create a new private cloud management DNS zone binding by binding a VPC or a VMware Engine network using the Google Cloud CLI or VMware Engine API, do the following:

###  gcloud 

To bind a VPC using the Google Cloud CLI, use the [`gcloud vmware private-clouds management-dns-zone-bindings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/create):
    
    
    gcloud vmware private-clouds management-dns-zone-bindings create DNS_ZONE_BINDING_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE \
      --vpc-network=projects/VPC_PROJECT_ID/global/networks/VPC_NETWORK
    

To bind a VMware Engine network, use the [`gcloud vmware private-clouds management-dns-zone-bindings create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/create):
    
    
    gcloud vmware private-clouds management-dns-zone-bindings create DNS_ZONE_BINDING_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE \
      --vmware-engine-network=projects/PROJECT_ID/locations/global/vmwareEngineNetworks/NETWORK_ID
    

Replace the following:

  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID.
  * `PRIVATE_CLOUD_ID`: your private cloud name.
  * `ZONE`: the zone for your private cloud.
  * `VPC_PROJECT_ID`: the project for your VPC network.
  * `PROJECT_ID`: the project for your private cloud.
  * `NETWORK_ID`: the name for your VMware Engine network.
  * `VPC_NETWORK`: the name for your VPC network.



### API

To bind a VPC using the VMware Engine API, make a `POST` request:
    
    
    POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/managementDnsZoneBindings?management_dns_zone_binding_id=DNS_ZONE_BINDING_ID" -d '{
         "vpc_network": "projects/VPC_PROJECT_ID/global/networks/VPC_NETWORK"
    }'
    

To bind a VMware Engine network using the VMware Engine API, make a `POST` request:
    
    
    POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/managementDnsZoneBindings?management_dns_zone_binding_id=DNS_ZONE_BINDING_ID" -d '{
      "vmware_engine_network" : "NETWORK_ID"
    }'
    

Replace the following:

  * `PROJECT_ID`: the project for your private cloud.
  * `ZONE`: the zone for your private cloud.
  * `PRIVATE_CLOUD_ID`: your private cloud name.
  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID.
  * `VPC_PROJECT_ID`: the project for your VPC network.
  * `VPC_NETWORK`: the name for your VPC network.
  * `NETWORK_ID`: the name for your VMware Engine network.



## Delete management DNS zone bindings

You can delete a DNS zone binding that was created. Refer to the list of management DNS zone bindings and find the `DNS_ZONE_BINDING_ID` corresponding to the VPC or VMware Engine network with that you want to remove the binding from. To delete a management DNS zone binding using the Google Cloud CLI or VMware Engine API, do the following:

###  gcloud 

If you want to delete a management DNS zone binding using the Google Cloud CLI, use the [`gcloud vmware private-clouds management-dns-zone-bindings delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/delete):
    
    
    gcloud vmware private-clouds management-dns-zone-bindings delete DNS_ZONE_BINDING_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE
    

Replace the following:

  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `ZONE`: the zone for this request.



### API

If you want to delete a management DNS zone binding using the VMware Engine API, make a `DELETE` request:
    
    
    DELETE "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/managementDnsZoneBindings/DNS_ZONE_BINDING_ID"
    

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID for this request.



## Edit management DNS zone binding

You can edit a management DNS zone binding description using the Google Cloud CLI or VMware Engine API by doing the following:

###  gcloud 

If you want to edit the description of a management DNS zone binding using the Google Cloud CLI, use the [`gcloud vmware private-clouds management-dns-zone-bindings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/update):
    
    
    gcloud vmware private-clouds management-dns-zone-bindings update DNS_ZONE_BINDING_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE \
      --description="DESCRIPTION"

Replace the following:

  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `ZONE`: the zone for this request.
  * `DESCRIPTION`: a new description for this request.



### API

If you want to edit the description of a management DNS zone binding using the VMware Engine API, make a `PATCH` request:
    
    
         PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/managementDnsZoneBindings/DNS_ZONE_BINDING_ID?update_mask_description" -d '{
            "description": "DESCRIPTION"
         }'
      

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID for this request.
  * `DESCRIPTION`: a new description for this request.



## Describe management DNS zone binding

You can get the description of a management DNS zone binding to verify updates using the Google Cloud CLI or VMware Engine API by doing the following:

###  gcloud 

If you want to get the description of a management DNS zone binding using the Google Cloud CLI, use the [`gcloud vmware private-clouds management-dns-zone-bindings describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/management-dns-zone-bindings/describe):
    
    
    gcloud vmware private-clouds management-dns-zone-bindings describe DNS_ZONE_BINDING_ID \
      --private-cloud=PRIVATE_CLOUD_ID \
      --location=ZONE

Replace the following:

  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `ZONE`: the zone for this request.



### API

If you want to get the description of a management DNS zone binding using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/privateClouds/PRIVATE_CLOUD_ID/managementDnsZoneBindings/DNS_ZONE_BINDING_ID"
    

Replace the following:

  * `PROJECT_ID`: the project for this request.
  * `ZONE`: the zone for this request.
  * `PRIVATE_CLOUD_ID`: the private cloud name for this request.
  * `DNS_ZONE_BINDING_ID`: the DNS zone binding ID for this request.



## What's next

  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
