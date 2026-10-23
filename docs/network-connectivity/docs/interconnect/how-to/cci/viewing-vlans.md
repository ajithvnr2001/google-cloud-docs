---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/viewing-vlans/
title: View VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:44.391105+00:00
---

# View VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/viewing-vlans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

You can view a list of all the VLAN attachments in your project and details about each one. For example, you can view the name of an attachment, the name of its associated Cloud Router, and whether it's an attachment for Cross-Cloud Interconnect or another Cloud Interconnect variant. You can also check the Dataplane version of the attachment.

## View VLAN attachments and their details

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

VLAN attachments for Cross-Cloud Interconnect are listed as attachments of type **Dedicated (Cross-Cloud)**.

  2. Select a VLAN attachment to view its details.




###  gcloud 

  1. To list all VLAN attachments in your project, use the [`gcloud compute interconnects attachments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/list):
         
         gcloud compute interconnects attachments list
         

You should see output similar to the following. VLAN attachments for Cross-Cloud Interconnect connections are listed as attachments of type `DEDICATED`:
         
         NAME: my-vlan-attachment
         REGION: us-east4
         TYPE: DEDICATED
         INTERCONNECT: my-connection
         ROUTER: my-router
         
         NAME: my-vlan-attachment-2
         REGION: us-east4
         TYPE: DEDICATED
         INTERCONNECT: my-connection
         ROUTER: my-router
         ...
         

  2. To view more information about an attachment, use the [`gcloud compute interconnects attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/describe):
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME \
             --region= REGION
         

Replace the following:

     * `ATTACHMENT_NAME`: the name of your VLAN attachment
     * `REGION`: the region where the attachment is located

You should see output similar to the following:
    
    adminEnabled: true
    bandwidth: BPS_1G
    cloudRouterIpAddress: 169.254.245.153/29
    creationTimestamp: '2023-03-17T23:32:27.087-07:00'
    customerRouterIpAddress: 169.254.245.154/29
    dataplaneVersion: 2
    encryption: NONE
    id: '4461230117430551572'
    interconnect: https://www.googleapis.com/compute/v1/projects...my-connection
    kind: compute#interconnectAttachment
    mtu: 1500
    name: my-vlan-attachment
    operationalStatus: OS_ACTIVE
    privateInterconnectInfo:
    tag8021q: 246
    region: https://www.googleapis.com/compute/v1/projects...us-east4
    router: https://www.googleapis.com/compute/v1/projects...my-router
    selfLink: https://www.googleapis.com/compute/v1/projects...my-vlan-attachment
    stackType: IPV4_ONLY
    state: ACTIVE
    type: DEDICATED
    vlanTag8021q: 246




## Check the Dataplane version of an attachment

After you create a VLAN attachment, you can check the Dataplane version for the attachment.

To check the Dataplane version of a VLAN attachment, use the Google Cloud CLI or the Compute Engine API. The Dataplane version of an attachment does not appear in the Google Cloud console.

### gcloud

To check the Dataplane version of the attachment, run the following command:
    
    
    gcloud compute interconnects attachment describe ATTACHMENT_NAME \
        --region= NAME
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the attachment
  * `REGION`: the region where the attachment is located



In the output, look for the `dataplaneVersion` field.

If the `dataplaneVersion` field does not appear in the output, the VLAN attachment is using version 2.

The following example output shows a VLAN attachment that uses Dataplane v2.
    
    
    adminEnabled: true
    bandwidth: BPS_10G
    cloudRouterIpAddress: 169.254.132.105/29
    creationTimestamp: '2022-03-04T10:08:11.526-08:00'
    customerRouterIpAddress: 169.254.132.106/29
    **dataplaneVersion: 2**
    id: '8542849272424426340'
    interconnect: https://www.googleapis.com/compute/v1/projects/customer-project/global/interconnects/my-interconnect
    kind: compute#interconnectAttachment
    mtu: 1440
    name: my-attachment
    operationalStatus: OS_ACTIVE
    privateInterconnectInfo:
      tag8021q: 1100
    region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-west1
    router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-west1/routers/ipv6-cf-test-1
    selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-west1/interconnectAttachments/my-attachment
    state: ACTIVE
    type: DEDICATED
    vlanTag8021q: 1100
    

### API

Use the [`interconnectAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) to obtain the value of the `dataplaneVersion` field.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/interconnectAttachments/ATTACHMENT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project that contains the VLAN attachment
  * `REGION`: the region where the VLAN attachment is located
  * `ATTACHMENT_NAME`: the name of the VLAN attachment



In the output, look for the `dataplaneVersion` field with a value of 2.

If the `dataplaneVersion` field does not appear in the output, the VLAN attachment is using version 2.

## What's next

  * To learn more about Cross-Cloud Interconnect, see the [Cross-Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview).

  * To learn about common issues that you might encounter when using Cross-Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#cci).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
