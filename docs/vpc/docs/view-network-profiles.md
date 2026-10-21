---
url: https://docs.cloud.google.com/vpc/docs/view-network-profiles/
title: View network profiles \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:42.680771+00:00
---

# View network profiles  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/view-network-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View network profiles

This page describes how to view network profiles in Google Cloud.

## Required roles

To get the permissions that you need to view network profiles, ask your administrator to grant you the [Compute Network Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view network profiles. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view network profiles:

  * `compute.networkProfiles.get`
  * `compute.networkProfiles.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List network profiles

This section describes how to list network profiles by using the Google Cloud CLI and the API. There is a unique instance of a given network profile for each location in which it is available.

If you are using the Google Cloud console, you can view the list of network profiles by location as part of the network profile configuration when you create a VPC network. For more information, see [Create a VPC network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma).

###  gcloud 

To list all network profiles in Google Cloud, use the [`gcloud compute network-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-profiles/list).
    
    
    gcloud compute network-profiles list
    

To list the network profiles that are available in a specific zone, use the `location.name` filter.
    
    
    gcloud compute network-profiles list --filter='location.name=ZONE'
    

Replace `ZONE` with the zone for which you want to view network profiles, such as `europe-west1-b`.

To list all instances of a specific network profile, use the `--filter` flag.
    
    
    gcloud compute network-profiles list --filter=NAME
    

Replace `NAME` with the relevant part of the network profile resource name, such as `falcon`, `roce`, or `roce-metal`.

###  API 

To list all network profiles in Google Cloud, use the [`networkProfiles.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkProfiles/list).
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/global/networkProfiles
    

Replace `PROJECT_ID` with your project ID.

## View the details of a network profile

This section describes how to view the details of a network profile by using the Google Cloud CLI or the API.

If you are using the Google Cloud console, you can view the details of a network profile as part of the network profile configuration when you [create a VPC network](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma), or when [viewing an existing network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#viewing-networks) that has a network profile configured.

###  gcloud 

To view the details of a network profile, use the [`gcloud compute network-profiles describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-profiles/describe).
    
    
    gcloud compute network-profiles describe NETWORK_PROFILE
    

Replace `NETWORK_PROFILE` with the name of the network profile.

###  API 

To view the details of a network profile, use the [`networkProfiles.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkProfiles/get).
    
    
    GET https://compute.googleapis.com/compute/projects/PROJECT_ID/global/networkProfiles/NETWORK_PROFILE
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `NETWORK_PROFILE`: the name of the network profile.



## What's next

  * Get an overview of [network profiles for specific use cases](https://docs.cloud.google.com/vpc/docs/network-profiles).
  * Learn about [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).
  * Create a [VPC network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
