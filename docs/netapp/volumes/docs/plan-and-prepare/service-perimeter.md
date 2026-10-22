---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/service-perimeter/
title: Secure NetApp Volumes with a service perimeter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:52.016611+00:00
---

# Secure NetApp Volumes with a service perimeter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/service-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Secure NetApp Volumes with a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to protect your Google Cloud NetApp Volumes volumes with a service perimeter using VPC Service Controls.

VPC Service Controls improve the security of Google Cloud services by creating a service perimeter that prevents unauthorized data access. This perimeter protects against accidental or intentional data exfiltration attempts from external or internal entities. To grant access, you need to add entities to your perimeter. For more information about VPC Service Controls, see [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

VPC Service Controls protect access to the NetApp Volumes API, which is used for administrative management of NetApp Volumes resources. You can't access a volume's content with this API.

Data access to the content of a volume is granted using the NFS, SMB, or iSCSI protocol. The security of data access is protected through volume and file access controls specific to these protocols which are independent of VPC Service Controls. To connect to a volume, an NFS, SMB, or iSCSI client needs to be connected to the same network as the volume. For more information, see the following sections:

  * [Volume access controls for NFS protocols](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_access_controls_for_nfs_protocols)

  * [Volume access controls for SMB protocols](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_access_controls_for_smb_protocol)

  * [Volume access controls for iSCSI protocols](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_access_controls_for_iscsi_protocol)

  * [File access control](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#file_access_control)




## Secure your volumes using VPC Service Controls

  1. [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  2. Add the NetApp Volumes API to your service perimeter. For instructions about adding a service to your service perimeter, see [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).




## VPC Service Controls limitations

Some features of NetApp Volumes require access to Google resources within your perimeter. The following features are known to cause issues when you enable VPC Service Controls.

  * **Customer-managed encryption keys (CMEK)** : NetApp Volumes needs access to the KMS key you specified for CMEK. For more information, see [Verify key access](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/verify-key-access).

  * **Volume replication across projects (allow-listed General Availability (GA) feature)** : for Flex Unified, Standard, Premium, and Extreme service levels, replication between projects in different perimeters requires VPC Service Controls egress and ingress rules in both projects to allow NetApp API flows. For more information, see [Considerations for volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#considerations_for_volume_replication).




For more information about products and services that are supported by VPC Service Controls, see [Supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_netapp_volumes).

### VPC Service Controls rules for cross-project volume replication

To enable cross-project volume replication, you must add both an egress and an ingress rule to the VPC Service Controls perimeter for both the source and destination projects.

#### Egress rule

Add the following egress rule to the source and destination projects of the cross-project volume replication.

Before you apply the rule, you must replace SOURCE_PROJECT and DESTINATION_PROJECT with your project IDs. For the identities field, add the Google IDs of the NetApp Volumes administrators who manage the replication.
    
    
       {
           "egressFrom": {
               "identities": [
                   "your_google_id@your_domain.com"
               ],
               "sources": [
                   {
                       "resource": "projects/SOURCE_PROJECT"
                   },
                   {
                       "resource": "projects/DESTINATION_PROJECT"
                   }
               ]
           },
           "egressTo": {
               "operations": [
                   {
                       "methodSelectors": [
                           {
                               "method": "*"
                           }
                       ],
                       "serviceName": "netapp.googleapis.com"
                   }
               ],
               "resources": [
                   "projects/SOURCE_PROJECT",
                   "projects/DESTINATION_PROJECT"
               ]
           },
           "title": "NetApp Volumes cross-project volume replication"
       }
     

#### Ingress rule

Add the following ingress rule to the source and destination projects of the cross-project volume replication.

Before you apply the rule, you must replace SOURCE_PROJECT and DESTINATION_PROJECT with your project IDs. For the identities field, add the Google IDs of the NetApp Volumes administrators who manage the replication.
    
    
       {
           "ingressFrom": {
               "identities": [
                   "your_google_id@your_domain.com"
               ],
               "sources": [
                   {
                       "resource": "projects/SOURCE_PROJECT"
                   },
                   {
                       "resource": "projects/DESTINATION_PROJECT"
                   }
               ]
           },
           "ingressTo": {
               "operations": [
                   {
                       "methodSelectors": [
                           {
                               "method": "*"
                           }
                       ],
                       "serviceName": "netapp.googleapis.com"
                   }
               ],
               "resources": [
                   "projects/SOURCE_PROJECT",
                   "projects/DESTINATION_PROJECT"
               ]
           },
           "title": "NetApp Volumes cross-project volume replication"
       }
     

## What's next

[Configure access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/workflow) to Google Cloud NetApp Volumes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
