---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-vlans/
title: View VLAN attachments and groups \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:16.010858+00:00
---

# View VLAN attachments and groups  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-vlans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  View VLAN attachments and groups Stay organized with collections  Save and categorize content based on your preferences. 

You can view a list of all the VLAN attachments in your project and the details about each one. For example, you can view the name of an attachment, whether it's an attachment for Dedicated Interconnect or Partner Interconnect, and its associated Cloud Router. You can also check its Dataplane version.

## View VLAN attachments and their details

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select a VLAN attachment to view its details.




###  gcloud 

  1. List all VLAN attachments that are in your project:
         
         gcloud compute interconnects attachments list
         

The output is similar to the following:
         
         NAME: my-attachment
         REGION: us-east1
         TYPE: PARTNER
         INTERCONNECT: example-partner-interconnect
         ROUTER: my-router
         ATTACHMENT_GROUP: example-attachment-group
         
         NAME: my-second-attachment
         REGION: us-west1
         TYPE: DEDICATED
         INTERCONNECT: example-dedicated-interconnect
         ROUTER: my-second-router
         ATTACHMENT_GROUP: example-attachment-group
         ...
         

  2. Describe the VLAN attachment to view more information about it:
         
         gcloud compute interconnects attachments describe my-attachment
         

The output is similar to the following:
         
         adminEnabled: true
         attachmentGroup: https://www.googleapis.com/compute/v1/projects/customer-project/global/interconnectAttachmentGroups/example-attachment-group
         bandwidth: BPS_10G
         cloudRouterIpAddress: 169.254.194.169/29
         creationTimestamp: '2022-03-04T10:08:51.610-08:00'
         customerRouterIpAddress: 169.254.194.170/29
         dataplaneVersion: 2
         id: '8652605636960316252'
         interconnect: https://www.googleapis.com/compute/v1/projects/customer-project/global/interconnects/example-dedicated-interconnect
         kind: compute#interconnectAttachment
         mtu: 1460
         name: my-second-attachment
         operationalStatus: OS_ACTIVE
         privateInterconnectInfo:
           tag8021q: 1101
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-west1
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-west1/routers/my-second-router
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-west1/interconnectAttachments/my-second-attachment
         state: ACTIVE
         type: DEDICATED
         vlanTag8021q: 1101
         




## View VLAN attachment groups and their details

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. In the **Attachment groups** field, click the name of an attachment group to see more information about that group's details.




###  gcloud 

  1. Use the following command to list all VLAN attachment groups that are in your project:
         
         gcloud compute interconnects attachments groups list
         

The output is similar to the following:
         
         NAME                ATTACHMENTS             INTENDED_SLA             CONFIGURED_SLA
         attachment-group-1                          PRODUCTION_NON_CRITICAL  NO_SLA
         attachment-group-2  us-east4/attachment-1   PRODUCTION_NON_CRITICAL  PRODUCTION_NON_CRITICAL
                             us-east4/attachment-2
         attachment-group-3  us-east4/attachment-3   PRODUCTION_CRITICAL      PRODUCTION_CRITICAL
                             us-east4/attachment-4
                             us-west2/attachment-5
                             us-west2/attachment-6
         

  2. To see more information about a specific VLAN attachment group, use the following command, replacing `GROUP_NAME` with the name of the attachment group.
         
         gcloud compute interconnects attachments groups describe GROUP_NAME
         

The output is similar to the following:
         
         attachments:
           us-east4/attachment-1:
             attachment: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-east4/interconnectAttachments/attachment-1
           us-east4/attachment-2:
             attachment: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-east4/interconnectAttachments/attachment-2
         configured:
           availabilitySla:
             effectiveSla: PRODUCTION_NON_CRITICAL
         description: my attachment group
         intent:
           availabilitySla: PRODUCTION_NON_CRITICAL
         kind: compute#interconnectAttachmentGroup
         logicalStructure:
           regions:
           - metros:
             - facilities:
               - facility: '1'
                 zones:
                 - attachments:
                   - https://www.googleapis.com/compute/v1/projects/my-project/regions/us-east4/interconnectAttachments/attachment-1
                   zone: zone1
                 - attachments:
                   - https://www.googleapis.com/compute/v1/projects/my-project/regions/us-east4/interconnectAttachments/attachment-2
                   zone: zone2
               metro: IAD
             region: us-east4
         name: attachment-group-2
         selfLink: https://www.googleapis.com/compute/v1/projects/my-project/global/interconnectAttachmentGroups/attachment-group-2
         




## What's next

  * To create a Dedicated Interconnect connection, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Dedicated Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#dedicated).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
