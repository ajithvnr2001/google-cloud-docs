---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-attachment-group/
title: Create an attachment group \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:07.917222+00:00
---

# Create an attachment group  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-attachment-group/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create an attachment group Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create or update attachment group resources in Google Distributed Cloud (GDC) air-gapped.

An attachment group represents a collection of VLAN attachments that share access to a set of organizations. An `AttachmentGroup` resource lists the organizations allowed to use virtual routing and forwarding (VRF) on the `InterconnectAttachment` resource.

Attachment groups are a required resource in setting up a secure air-gapped connection with high bandwidth and low latency.

This page is for developers within the application operator group who are looking to establish connectivity with interconnects. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To create or update an attachment group, you must have the following:

  * The necessary identity and access roles. For more information, see [Prepare predefined roles and permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview#prepare-roles).



## Create or update an attachment group

To create or update an attachment group, follow these steps:

  1. Create a YAML file named `attachmentgroup.yaml`.
  2. Add the following content to the file:
         
         apiVersion: system.private.gdc.goog/v1alpha1
         kind: AttachmentGroup
         metadata:
           name: attachment-group-IDENTIFIER
           namespace: gpc-system
         spec:
           identifier: IDENTIFIER
           entities:
             - orgName: ORG_NAME
               domainType: DOMAIN_TYPE
         

  3. Replace the following:

     * `IDENTIFIER`: a unique identifier string for the attachment group. Because VLAN attachments that you create use the `DirectConnect` type, you can choose any unique identifier. For more information, see [Interconnect types](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/interconnect-overview#interconnect-types).
     * `ORG_NAME`: the name of the tenant organization that all VLAN attachments in the attachment group can connect to. This must be your organization's name.
     * `DOMAIN_TYPE`: the specific domain of the tenant organization in the entry that all VLAN attachments can connect to. You must provide one of the following valid values:

       * `OrgAdmin`: Connect to the Org Management-plane infrastructure.
       * `OrgData`: Connect to the Org Data-plane infrastructure.
       * `OrgMixed:` Use the `OrgMixed` type to connect to both the Org Management-plane and Org Data-plane infrastructure.
  4. Create the attachment group:
         
         kubectl apply -f attachmentgroup.yaml -n gpc-system
         --kubeconfig=MANAGEMENT_API_SERVER
         

Replace `MANAGEMENT_API_SERVER` with the path to the kubeconfig file for the Management API server.

  5. Check that the creation of attachment group is successful:
         
         kubectl get attachmentgroup -n gpc-system
         --kubeconfig=MANAGEMENT_API_SERVER
         

The output returns the attachment group and shows `True` in the `Ready` column:
         
         NAME                     IDENTIFIER       READY
         attachment-group-mixed   mixed            True
         




## What's next

  * [Create a VLAN attachment](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/interconnects/create-vlan-attachment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
