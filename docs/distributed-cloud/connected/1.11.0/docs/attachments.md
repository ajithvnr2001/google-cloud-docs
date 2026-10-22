---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/attachments/
title: Create and manage interconnect attachments \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:29.998980+00:00
---

# Create and manage interconnect attachments  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/attachments/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/overview)



Send feedback 

#  Create and manage interconnect attachments Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud interconnect attachment resources in a Distributed Cloud connected zone.

This functionality is only available on Distributed Cloud connected racks. Distributed Cloud connected servers don't support interconnect attachment resources.

For more information about Distributed Cloud interconnect attachments, see [How Distributed Cloud works](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/how-it-works#networking).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

Keep the following in mind:

  * We recommend that you create an interconnect attachment along with its corresponding router at the same time. For more information, see [Create a router](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers#create).
  * You can optionally specify a VLAN ID to use to tag the packets that pass through the interconnect attachment.
  * The VLAN ID that you specify for packet tagging is local to the interconnect attachment. In other words, a given interconnect attachment is not part of the same Layer 2 domain as the interconnect attachments associated with other interconnects, or subnetworks that are not associated with any interconnect attachments. Therefore, while the VLAN ID specified for packet tagging must be unique across all interconnect attachments created on the target interconnect, it can be reused on other interconnects and on subnetworks not associated with an interconnect attachment.



## Create an interconnect attachment

To create a Distributed Cloud interconnect attachment, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects attachments dedicated create` command:
    
    
    gcloud edge-cloud networking interconnects attachments dedicated create ATTACHMENT_NAME \
        --interconnect=INTERCONNECT_NAME \
        --network=NETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME \
        --vlan-id=VLAN_ID \
        --mtu=MTU_SIZE
    

Replace the following:

  * `ATTACHMENT_NAME`: a descriptive name that uniquely identifies this interconnect attachment.
  * `INTERCONNECT_NAME`: the name of the interconnect to which this interconnect attachment connects.
  * `NETWORK_NAME`: the name of the Distributed Cloud network that this interconnect attachment resource serves.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `VLAN_ID` (optional): the VLAN ID with which packets that pass through this interconnect attachment are tagged. Valid values are between 2 and 4095. If you omit this value or set it to 0, the packets are untagged.
  * `MTU_SIZE`: the maximum transmission unit (MTU) size for the subnetwork that this interconnect attachment instantiates. Valid values are 1500 and 9000.



###  API 

Make a `POST` request to the `projects.locations.zones.interconnectAttachments.create` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/interconnectAttachments?interconnectAttachmentId=ATTACHMENT_ID
     {
      "labels": { LABELS,
       },
      "interconnect": { INTERCONNECT_NAME,
       },
      "network": { NETWORK_NAME,
       },
      "vlanId": { VLAN_ID,
       },
      "mtu": { MTU_SIZE,
       },       
     }   
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `ATTACHMENT_ID`: an ID that uniquely identifies this interconnect attachment.
  * `LABELS`: a list of labels to apply to this interconnect attachment resource.
  * `INTERCONNECT_NAME`: the name of the interconnect to which this interconnect attachment connects.
  * `NETWORK_NAME`: the network that this interconnect attachment resource serves. 
  * `VLAN_ID`: the VLAN ID for the subnetwork that this interconnect attachment instantiates on the router. Valid values are between 2 and 4095. A value of 0 configures the subnetwork as untagged.
  * `MTU_SIZE`: the maximum transmission unit (MTU) size for the subnetwork that this interconnect attachment instantiates. Valid values are 1500 and 9000.



## List interconnect attachments

To list the Distributed Cloud interconnect attachments in a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects attachments list` command:
    
    
    gcloud edge-cloud networking interconnects attachments list \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



###  API 

Make a `GET` request to the `projects.locations.zones.interconnectAttachments.list` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/interconnectAttachments?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive the following page of results.



## Get information about an interconnect attachment

To get information about a Distributed Cloud interconnect attachment, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects attachments describe` command:
    
    
    gcloud edge-cloud networking interconnects attachments describe ATTACHMENT_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the target interconnect attachment.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



###  API 

Make a `GET` request to the `projects.locations.zones.interconnectAttachments.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/interconnectAttachments/ATTACHMENT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `ATTACHMENT_ID`: the name of the target interconnect attachment.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



This operation returns detailed information about the resource, including its provisioning state as follows:

  * `PENDING`: the resource has not yet begun provisioning and has not yet been propagated throughout the zone.
  * `PROVISIONING`: the resource is being provisioned; you must wait until it has been propagated throughout the zone.
  * `RUNNING`: the resource has been successfully provisioned and propagated throughout the zone; it is ready to use.
  * `FAILED`: the provisioning of the resource was not successful; the resource has not been propagated throughout the zone.



## Delete an interconnect attachment

To delete a Distributed Cloud interconnect attachment, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking interconnects attachments delete` command:
    
    
    gcloud edge-cloud networking interconnects attachments delete ATTACHMENT_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the target interconnect attachment.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.



###  API 

Make a `DELETE` request to the `projects.locations.zones.interconnectAttachments.delete` method:
    
    
    DELETE /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/subnets/SUBNETWORK_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `ATTACHMENT_NAME`: the name of the target interconnect attachment.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/deploy)
  * [Manage interconnects](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/interconnects)
  * [Create and manage networks](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networks)
  * [Create and manage routers](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers)
  * [Create and manage subnetworks](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/subnetworks)
  * [Create and manage VPN connections](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/vpn-connections)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/zones)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
