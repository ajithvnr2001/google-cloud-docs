---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/networks/
title: Create and manage networks \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:39.785130+00:00
---

# Create and manage networks  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/networks/

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
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/overview)



Send feedback 

#  Create and manage networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud network resources in a Distributed Cloud connected zone.

Distributed Cloud connected servers ship with a single pre-configured network, the default Distributed Cloud network. Distributed Cloud connected servers don't support configuring additional networks.

For more information about Distributed Cloud networks, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/how-it-works#networking).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

Keep the following in mind:

  * You can create up to 100 networks per Distributed Cloud zone.
  * A network is a virtual private network instantiated within the target zone.
  * The network is instantiated as a Virtual Routing Function (VRF).
  * Packets are routed independently inside a network.
  * If your zone Google Cloud project and cluster Google Cloud project are different, you must grant the cluster Google Cloud project permission in the zone Google Cloud project to allow access to the Edge Network API. For instructions, see [Authorize actions in clusters using role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control).



## Create a network

To create a Distributed Cloud network, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking networks create` command:
    
    
    gcloud edge-cloud networking networks create NETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME \
        --mtu=MTU_SIZE
    

Replace the following:

  * `NETWORK_NAME`: a descriptive name that uniquely identifies this network.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `MTU_SIZE`: the maximum transmission unit (MTU) size for this network. Valid values are 1500 and 9000. This value must match the MTU size of the `default` network and be the same for all networks.



###  API 

Make a `POST` request to the `projects.locations.zones.networks.create` method:
    
    
    POST /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/networks?networkId=NETWORK_ID
    {
     "labels": { LABELS,
      },
     "mtu": { MTU_SIZE,
      },
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `NETWORK_ID`: a unique ID that identifies this network.
  * `LABELS`: a list of labels to apply to this network resource. 
  * `MTU_SIZE`: the maximum transmission unit (MTU) size for this network. Valid values are 1500 and 9000.



## List networks

To list Distributed Cloud networks provisioned within a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking networks list` command:
    
    
    gcloud edge-cloud networking networks list \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.networks.list` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/networks?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud zone.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a network

To get information about a Distributed Cloud network, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking networks describe` command:
    
    
    gcloud edge-cloud networking networks describe NETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `NETWORK_NAME`: the name of the target network.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.networks.get` method:
    
    
    GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/networks/NETWORK_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `NETWORK_ID`: the ID of the target network.



## Check the operational status of a network

To check the operational status of a Distributed Cloud network, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking networks get-status` command:
    
    
    gcloud edge-cloud networking networks get-status NETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `NETWORK_NAME`: the name of the target network.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.networks.diagnose` method:
    
    
     GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/networks/NETWORK_ID:diagnose
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `NETWORK_ID`: the ID of the target network.



## Delete a network

To delete a Distributed Cloud network, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking networks delete` command:
    
    
    gcloud edge-cloud networking networks delete NETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `NETWORK_NAME`: the name of the target network.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `DELETE` request to the `projects.locations.zones.networks.delete` method:
    
    
     DELETE /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/networks/NETWORK_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `NETWORK_ID`: the ID of the target network.



## What's next

  * [Deploy workloads on Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/deploy)
  * [Manage interconnects](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/interconnects)
  * [Create and manage interconnect attachments](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/attachments)
  * [Create and manage routers](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/routers)
  * [Create and manage subnetworks](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/subnetworks)
  * [Create and manage VPN connections](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/vpn-connections)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/zones)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
