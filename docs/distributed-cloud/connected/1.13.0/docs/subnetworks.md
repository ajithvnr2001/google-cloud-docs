---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/subnetworks/
title: Create and manage subnetworks \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:03.743711+00:00
---

# Create and manage subnetworks  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/subnetworks/

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
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)



Send feedback 

#  Create and manage subnetworks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud subnetwork resources in a Distributed Cloud connected zone.

For more information about Distributed Cloud subnetworks, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

Keep the following in mind:

  * You can create up to 138 subnetworks per Distributed Cloud zone.
  * The subnetwork is a VLAN within the parent network. As such, each subnetwork must have a globally unique VLAN ID. Distributed Cloud connected does not allow the reuse of VLAN IDs.
  * To have Distributed Cloud connected assign an unused VLAN ID at random, specify `0` as the VLAN ID when you create the subnetwork.
  * The subnetwork is accessible to all nodes in your Distributed Cloud connected zone.



## Create a subnetwork

To create a Distributed Cloud subnetwork, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking subnets create` command:
    
    
    gcloud edge-cloud networking subnets create SUBNETWORK_NAME \
        --network=NETWORK_NAME \
        --ipv4-range=IPV4_RANGE \
        --vlan-id=VLAN_ID \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `SUBNETWORK_NAME`: a descriptive name that uniquely identifies this subnetwork.
  * `NETWORK_NAME`: the network that encapsulates this subnetwork.
  * `IPV4_RANGE`: the IPv4 address range that this subnetwork covers in the IP address/prefix format.
  * `VLAN_ID`: the target VLAN ID for this subnetwork.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `POST` request to the `projects.locations.zones.subnets.create` method:
    
    
     POST /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/subnets?subnetId=SUBNETWORK_ID
     {
      "labels": { LABELS,
       },
      "network": { NETWORK_NAME,
       },
      "ipv4Cidr": { IPV4_RANGE,
       },
      "vlanId": { VLAN_ID,
       },
     }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `SUBNETWORK_ID`: an ID that uniquely identifies this subnetwork.
  * `LABELS`: a list of labels to apply to this subnetwork resource. 
  * `NETWORK_NAME`: the network that encapsulates this subnetwork.
  * `IPV4_RANGE`: the IPv4 address range that this subnetwork covers in the IP address/prefix format.
  * `VLAN_ID`: the target VLAN ID for this subnetwork.



## List subnetworks

To list subnetworks provisioned within a Distributed Cloud connected zone, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking subnets list` command:
    
    
    gcloud edge-cloud networking subnets list \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.subnets.list` method:
    
    
     GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/subnets?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a subnetwork

To get information about a Distributed Cloud subnetwork, complete the steps in this section.

To complete this task, you must have the [Edge Network Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/permissions#edge-network-viewer) (`roles/edgenetwork.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking subnets describe` command:
    
    
    gcloud edge-cloud networking subnets describe SUBNETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `SUBNETWORK_NAME`: the name of the target subnetwork.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `GET` request to the `projects.locations.zones.subnets.get` method:
    
    
     GET /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/subnets/SUBNETWORK_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `SUBNETWORK_NAME`: the name of the target subnetwork.



This operation returns detailed information about the resource, including its provisioning state:

  * `PENDING`: the resource has not yet begun provisioning and has not yet been propagated throughout the zone.
  * `PROVISIONING`: the resource is being provisioned; you must wait until it has been propagated throughout the zone.
  * `RUNNING`: the resource has been successfully provisioned and propagated throughout the zone; it is ready to use.
  * `FAILED`: the provisioning of the resource was not successful; the resource has not been propagated throughout the zone.



## Delete a subnetwork

To delete a Distributed Cloud subnetwork, complete the steps in this section.

To complete this task, you must have the [Edge Network Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/permissions#edge-network-admin) (`roles/edgenetwork.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud networking subnets delete` command:
    
    
    gcloud edge-cloud networking subnets delete SUBNETWORK_NAME \
        --location=REGION \
        --zone=ZONE_NAME
    

Replace the following:

  * `SUBNETWORK_NAME`: the name of the target subnetwork.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.



###  API 

Make a `DELETE` request to the `projects.locations.zones.subnets.delete` method:
    
    
     DELETE /v1/projects/PROJECT_ID/locations/REGION/zones/ZONE_NAME/subnets/SUBNETWORK_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region to which the target Distributed Cloud connected zone belongs.
  * `ZONE_NAME`: the name of the target Distributed Cloud connected zone.
  * `SUBNETWORK_NAME`: the name of the target subnetwork.



## What's next

  * [Deploy workloads on Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/deploy)
  * [Create and manage networks](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/networks)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.13.0/docs/zones)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
