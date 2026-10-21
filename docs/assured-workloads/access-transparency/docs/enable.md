---
url: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable/
title: Enabling Access Transparency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:56.015306+00:00
---

# Enabling Access Transparency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-transparency/docs/enable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Transparency ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enabling Access Transparency

## Requirements for enabling Access Transparency

Access Transparency is a default security control for every Google Cloud organization. 

## Configuring Access Transparency using the Google Cloud console

To verify that Access Transparency is enabled for audit purposes on any resource level within your organization:

  1. 1\. Verify that you have the IAM role Access Approval Viewer (`roles/accessapproval.viewer`) or **Access Transparency Admin** (`roles/axt.admin`). 
  2. Go to **Security** > **Access Approval** in the Google Cloud console.
  3. Confirm that Access Transparency is enabled on the **Home** tab.

**Note:** If Access Transparency is disabled, the **Access Approval** UI may be inaccessible until Access Transparency is re-enabled.

or

  1. Check the Organization-Level Access Transparency IAM Settings Page. 

     1. Go to the **Identity and Access Management** page on the Google Cloud console.

     2. Verify that you have the IAM role **Access Transparency Admin** (`roles/axt.admin`) listed in the **Role** column for your **Principal** listing under the organization.

  2. Select any Google Cloud organization or project within the organization using the selector menu.

  3. Go to the **IAM** > **Settings** page.

     1. Verify that Access Transparency is enabled.



## What's next

For information about the pricing of Access Transparency, see [Pricing](https://cloud.google.com/assured-workloads/access-transparency/pricing). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
