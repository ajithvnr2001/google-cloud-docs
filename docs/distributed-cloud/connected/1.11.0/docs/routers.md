---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers/
title: Create and manage routers \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:13:01.530470+00:00
---

# Create and manage routers  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/routers/

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

#  Create and manage routers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud connected router resources in a Distributed Cloud zone.

This functionality is only available on Distributed Cloud connected racks. Distributed Cloud connected servers don't support router resources.

For more information about Distributed Cloud routers, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

Keep the following in mind:

  * You can create one router per Distributed Cloud network.

  * We recommend that you create a router along with its corresponding interconnect attachment at the same time. For more information about creating an interconnect attachment, see [Create an interconnect attachment](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/attachments#create).




## Create a router

To create a Distributed Cloud router, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers create` command:
    
    
    gcloud edge-cloud networking routers create ROUTER_NAME \
        --network=NETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME \
        --asn=ASN
    

Replace the following:

  * `ROUTER_NAME`: a descriptive name that uniquely identifies this router.
  * `NETWORK_NAME`: the name of the network that this router serves.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `ASN`: the Autonomous System Number (ASN) for this router. You can specify a two-byte or a four-byte value. Supports public and private ASN values.



###  API 

Make a `POST` request to the `projects.locations.zones.routers.create` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/routers?routerId=ROUTER_ID
    {
     "labels": { LABELS,
      },
     "network": { NETWORK_NAME,
      },
     "asn": { ASN,
      },      
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `ROUTER_ID`: an ID that uniquely identifies this router.
  * `LABELS`: a list of labels to apply to this router resource. 
  * `NETWORK_NAME`: the name of the network that this router serves.
  * `ASN`: the Autonomous System Number (ASN) for this router. You can specify a two-byte or a four-byte value. Supports public and private ASN values.



## Establish a BGP peering session on a router

A router allows you to establish the following types of Border Gateway Protocol (BGP) peering sessions:

  * A northbound peering session with an interconnect attachment
  * A southbound peering session with a subnetwork
  * A loopback peering session with a network



A BGP peering session is established by adding an interface to the router for the Distributed Cloud network component that corresponds to the type of peering session.

### Establish a northbound peering session

To establish a northbound peering session on a router with an interconnect attachment, complete the steps in this section. The target interconnect attachment must be associated with the target router.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers add-interface` command:
    
    
    gcloud edge-cloud networking routers add-interface ROUTER_NAME \
        --interface-name=INTERFACE_NAME \
        --interconnect-attachment=ATTACHMENT_NAME \
        --ip-address=INTERCONNECT_ADDRESS \
        --ip-mask-length=IP_MASK_LENGTH \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `INTERFACE_NAME`: a descriptive name for this interface.
  * `ATTACHMENT_NAME`: the name of the target interconnect attachment within the target router.
  * `INTERCONNECT_ADDRESS`: the IP address of the interconnect on which the target interconnect attachment is configured.
  * `IP_MASK_LENGTH`: the length of the mask for the specified interconnect IP address.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



### Establish a southbound peering session

To establish a southbound peering session on a router with a subnetwork, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers add-interface` command:
    
    
    gcloud edge-cloud networking routers add-interface ROUTER_NAME \
        --interface-name=INTERFACE_NAME \
        --subnet=SUBNETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `INTERFACE_NAME`: a descriptive name for this interface.
  * `SUBNETWORK_NAME`: the name of the target subnetwork.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



### Establish a loopback peering session

To establish a loopback peering session on a router with a network, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers add-interface` command:
    
    
    gcloud edge-cloud networking routers add-interface ROUTER_NAME \
        --interface-name=INTERFACE_NAME \
        --loopback-ip-addresses=LOOPBACK_ADDRESSES \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `INTERFACE_NAME`: a descriptive name for this interface.
  * `LOOPBACK_ADDRESSES`: the IPv4 incoming and outgoing addresses for the loopback interface, comma-separated.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



## Terminate a BGP peering session

To terminate a BGP peering session between a router and an interconnect attachment, a subnetwork, or a network, you must delete the interface for that network component from the target router. To delete the interface, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers remove-interface` command:
    
    
    gcloud edge-cloud networking routers remove-interface ROUTER_NAME \
        --interface-name=INTERFACE_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `INTERFACE_NAME`: a descriptive name for this interface.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



## Configure peers in a BGP peering session

You can add and remove BGP peers in a BGP peering session that's established between a router and an interconnect attachment, a subnetwork, or a network. When you add a peer to a BGP peering session, Bidirectional Forwarding Detection (BFD) is automatically enabled on the target router with a 100-ms interval, 100-ms minimum receive window, and a multiplier of 3.

After you add a peer to the target BGP peering session, you can then assign the peer IP address to the Pod that runs your workload. To find the peer IP address, complete the steps in Get information about a router.

### Add a peer to a BGP peering session

To add a peer to a BGP peering session, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers add-bgp-peer` command:
    
    
    gcloud edge-cloud networking routers add-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME> \
        --peer-asn=PEER_ASN \
        --peer-ipv4-range=PEER_IPv4_RANGE \
        --peer-ipv6-range=PEER_IPv6_RANGE \        
        --interface=INTERFACE_NAME \                                                       \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `PEER_NAME`: a descriptive name for this peer.
  * `PEER_ASN`: the Autonomous System Number (ASN) for this peer. You can specify a two-byte or a four-byte value. Supports public and private ASN values.
  * `PEER_IPv4_RANGE`: the IPv4 CIDR range for this peer. This address range must be in the same subnetwork as the IP address or address range for the associated interconnect attachment, subnetwork, or network.
  * `PEER_IPv6_RANGE`: the IPv6 CIDR range for this peer. This address range must be in the same subnetwork as the IP address or address range for the associated interconnect attachment, subnetwork, or network. 
  * `INTERFACE_NAME`: the name of the interface that corresponds to the target BGP session.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



### Remove a peer from a BGP peering session

To remove a peer from a BGP peering session, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers remove-bgp-peer` command:
    
    
    gcloud edge-cloud networking routers remove-bgp-peer ROUTER_NAME \
        --peer-name=PEER_NAME> \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `PEER_NAME`: the name of the target peer.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



## List routers

To list the routers provisioned within a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers list` command:
    
    
    gcloud edge-cloud networking routers list \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.routers.list` method:
    
    
     GET /v1/PROJECT_ID/locations/REGION/zones/ZONE_NAME/routers?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a router

To get information about a Distributed Cloud router, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers describe` command:
    
    
    gcloud edge-cloud networking routers describe ROUTER_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.routers.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/routers/ROUTER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `ROUTER_ID`: the ID of the target router.



This operation returns detailed information about the resource, including its provisioning state:

  * `PENDING`: the resource has not yet begun provisioning and has not yet been propagated throughout the zone.
  * `PROVISIONING`: the resource is being provisioned; you must wait until it has been propagated throughout the zone.
  * `RUNNING`: the resource has been successfully provisioned and propagated throughout the zone; it is ready to use.
  * `FAILED`: the provisioning of the resource was not successful; the resource has not been propagated throughout the zone.



## Check the operational status of a router

To check the operational status of a Distributed Cloud router, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers get-status` command:
    
    
    gcloud edge-cloud networking routers get-status ROUTER_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.routers.diagnose` method:
    
    
     GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/routers/ROUTER_ID:diagnose
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `ROUTER_ID`: the ID of the target router.



## Delete a router

To delete a Distributed Cloud router, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking routers delete` command:
    
    
    gcloud edge-cloud networking routers delete ROUTER_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `ROUTER_NAME`: the name of the target router.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `DELETE` request to the `projects.locations.zones.routers.delete` method:
    
    
     DELETE /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/routers/ROUTER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `ROUTER_ID`: the ID of the target router.



## What's next

  * [Deploy workloads on Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/deploy)
  * [Manage interconnects](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/interconnects)
  * [Create and manage interconnect attachments](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/attachments)
  * [Create and manage networks](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/networks)
  * [Create and manage subnetworks](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/subnetworks)
  * [Create and manage VPN connections](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/vpn-connections)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/zones)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
