---
url: https://docs.cloud.google.com/security-command-center/docs/determine-ownership-posture-findings/
title: Determine ownership for posture findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:11.966403+00:00
---

# Determine ownership for posture findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/determine-ownership-posture-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Determine ownership for posture findings Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains the concept of ownership for posture findings and the flow of determining the resource owner for a finding in Security Command Center Enterprise.

## Overview

Security Command Center requires a valid resource owner value to know what case to ingest the finding into, define whom to automatically assign a ticket to, and ensure that all findings grouped into a case belong to the same owner even if you customize the grouping settings.

For more information about findings grouping mechanism, refer to [Group findings in cases](https://docs.cloud.google.com/security-command-center/docs/group-findings-in-cases).

## Determine the ownership for posture findings

The flow of determining the resource owner for posture findings is as follows:

  1. Cloud tags. For more information, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

Upon receiving a finding, the **SCC Enterprise - Urgent Posture Findings Connector** analyzes it for the cloud tag value inherited from the finding resource and contained in the **Owner Tag Name** parameter.

If a finding possesses a cloud tag with the email of a resource owner, the connector ingests the finding and assigns it to the resource owner defined in a cloud tag.

  2. Essential Contacts. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) in the Resource Manager documentation.

If a finding hasn't inherited any cloud tags, then the connector attempts to define the resource owner using Essential Contacts.

If a finding has any contacts inherited from its resource, the connector ingests the finding and assigns it to the owner stated in contacts.

If there are several values (emails) in the contacts, the first value in the list defines the resource owner.

  3. The **Fallback Owner** parameter in the **SCC Enterprise - Urgent Posture Findings Connector**.

If a finding hasn't inherited any cloud tags or Essential Contacts, the connector ingests the finding and assigns it to the owner defined in the connector's **Fallback Owner** parameter.

To configure the **Fallback Owner** parameter, follow these steps:

     1. In the Google Cloud console, go to **Settings > SOAR settings** to open the **SOAR settings** page.
     2. In the Security Operations console **Settings** navigation, go to **Ingestion > Connectors**.

     3. Select the **SCC Enterprise - Urgent Posture Findings Connector**. The connector parameter configuration page opens.

     4. In the **Fallback Owner** parameter field, enter the email of the default assignee to remediate findings. The email should be assignable in your ticketing system.


**Note:** We recommend using cloud tags for all your Google Cloud resources to make sure that every finding automatically inherits correct tags with defined owners and is assigned to a correct person. Using cloud tags is the most accurate method to determine the resource owner while ensuring that the hierarchy of your Google Cloud resources is correct.

## What's next?

  * Learn how to [assign tickets in cases](https://docs.cloud.google.com/security-command-center/docs/assign-itsm-tickets).
  * Learn the concepts of cases in [Cases overview](https://docs.cloud.google.com/security-command-center/docs/cases-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
