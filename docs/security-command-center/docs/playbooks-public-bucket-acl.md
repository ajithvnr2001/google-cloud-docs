---
url: https://docs.cloud.google.com/security-command-center/docs/playbooks-public-bucket-acl/
title: Enable public bucket remediation \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:16.909235+00:00
---

# Enable public bucket remediation  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/playbooks-public-bucket-acl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Enable public bucket remediation Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document provides a step-by-step guide to enable the public bucket remediation for the posture findings playbooks in the Enterprise tier of Security Command Center.

## Overview

Security Command Center supports additional remediation for the vulnerabilities in the following playbooks:

  * **Posture Findings – Generic**
  * **Posture Findings With Jira**
  * **Posture Findings With ServiceNow**



These posture findings playbooks include a block that remediates the `OPEN PORT`, `PUBLIC IP ADDRESS`, and `PUBLIC BUCKET ACL` findings. For more information about these finding types, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

Playbooks are preconfigured to process the `OPEN PORT` and `PUBLIC IP ADDRESS` findings. Remediating the `PUBLIC_BUCKET_ACL` findings requires that you enable the public bucket remediation for playbooks.

## Enable public bucket remediation for playbooks

After the Security Health Analytics (SHA) detector identifies the Cloud Storage buckets that are publicly accessible and generates the `PUBLIC_BUCKET_ACL` findings, Security Command Center Enterprise ingests the findings and attaches playbooks to them. To enable the public bucket remediation for posture findings playbooks, you need to create a custom IAM role, configure a specific permission for it, and grant the custom role that you've created to an existing principal.

### Before you begin

A configured and running instance of the Cloud Storage integration is required to remediate the public bucket access. To validate the integration configuration, see [Update the Enterprise use case](https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update#storage-integration-config).

### Create a custom IAM role

To create a custom IAM role and configure a specific permission for it, complete the following steps:

  1. In the Google Cloud console, go to the IAM **Roles** page.

[Go to IAM Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **Create role** to create a custom role with permissions required for the integration.

  3. For a new custom role, provide the **Title** , **Description** , and a unique **ID**.

  4. Set the **Role Launch Stage** to **General Availability**.

  5. Add the following permission to the created role:
         
         resourcemanager.organizations.setIamPolicy
         

  6. Click **Create**.




### Grant a custom role to an existing principal

After you grant your new custom role to a selected principal, they can change permissions for any user in your organization.

To grant the custom role to an existing principal, complete the following steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the **Filter** field, paste the **Workload Identity Email** value that you use for the Cloud Storage integration and search for the existing principal.

  3. Click edit **Edit principal**. The **Edit access to " PROJECT"** dialog opens.

  4. Under **Assign roles** , click add **Add another role**.

  5. Select the custom role that you've created and click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
