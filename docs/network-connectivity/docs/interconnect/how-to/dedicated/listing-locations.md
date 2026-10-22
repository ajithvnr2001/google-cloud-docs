---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/listing-locations/
title: List locations \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:51.197403+00:00
---

# List locations  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/listing-locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  List locations Stay organized with collections  Save and categorize content based on your preferences. 

When you order a Dedicated Interconnect connection, you must specify a colocation facility where your network meets Google's network. In most cases, select a facility that's geographically close to your on-premises network.

To view a list of these facilities in the documentation, see [All colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities).

To use the Google Cloud console or Google Cloud CLI to view a list of facilities, see the following steps.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnectLocations.list`
  * `compute.interconnectLocations.get`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

You can view a list of the colocation facilities when you order a Dedicated Interconnect connection. You can filter the locations by city or facility name.

For more information, see [Ordering a Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect).

###  gcloud 

List all the colocation facilities:
    
    
     gcloud compute interconnects locations list
     

Output: 
    
    
     NAME             DESCRIPTION                    FACILITY_PROVIDER
     lhr-zone1-832    Equinix London Slough (LD5)    Equinix
     nrt-zone1-599    ComSpace I                     Marubeni Access Solutions Inc.
     nrt-zone2-452    Equinix Tokyo (TY2)            Equinix
      ...
     

Describe a location by providing a name to view the details of a facility, such as their physical address. The following example describes the `lhr-zone1-832` location:
    
    
     gcloud compute interconnects locations describe lhr-zone1-832
     

Output: 
    
    
      address: |-
        Equinix
        8 Buckingham Avenue
        SLOUGH
        SL1 4AX
        United Kingdom
      availabilityZone: zone1
      availableFeatures:
      − IF_MACSEC
      availableLinkTypes:
      − LINK_TYPE_ETHERNET_10G_LR
      − LINK_TYPE_ETHERNET_100G_LR
      city: London
      continent: EUROPE
      creationTimestamp: '1969-12-31T16:00:00.000-08:00'
      description: Equinix London Slough (LD5)
      facilityProvider: Equinix
      facilityProviderFacilityId: LD5
      id: '1024'
      kind: compute#interconnectLocation
      name: lhr-zone1-832
      peeringdbFacilityId: '832'
      regionInfos:
        region: https://www.googleapis.com/compute/projects/test-project/regions/europe-west1
      selfLink: https://www.googleapis.com/compute/projects/test-project/global/interconnectLocations/lhr-zone1-832
      status: AVAILABLE
     

## What's next

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
