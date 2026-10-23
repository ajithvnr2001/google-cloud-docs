---
url: https://docs.cloud.google.com/security-command-center/docs/group-findings-in-cases/
title: Group findings in cases \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:43.070936+00:00
---

# Group findings in cases  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/group-findings-in-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Group findings in cases Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how you can group findings into cases.

These steps are performed using Security Operations console pages. To open these pages from the Google Cloud console, go to **Settings > SOAR settings**.

## Overview

The findings grouping mechanism automatically groups ingested findings into cases. By default, this grouping mechanism ensures that all findings in a case belong to the same:

  * Resource owner
  * Google Cloud project
  * AWS account
  * Asset type
  * Category
  * Severity level



## Configure grouping settings

To configure the default grouping settings applicable to all ingested findings, follow these steps:

  1. In the Security Operations console, go to **Settings > Ingestion > Connectors**.

  2. Select **SCC Enterprise - Urgent Posture Findings Connector**.

  3. To customize the grouping mechanism and disable specific grouping options, clear the checkboxes for one or more of the following parameters:

     * `Group by AWS Account`
     * `Group by GCP Project`
     * `Group by Severity`
     * `Group by Asset Type`

**Important:** When customizing the grouping mechanism, we recommend to always select the **Group by GCP Project** and **Group by Asset Type** checkboxes and the **Group by AWS Account** , if the latter applies.

By default, the following grouping settings apply to ingested findings:

  * **Group by AWS Account** : Findings are grouped according to the AWS accounts they belong to.

  * **Group by GCP Project** : Findings are grouped according to the Google Cloud projects they belong to.

  * **Group by Severity** : Findings are grouped according to their `severity` [level](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications), such as `HIGH` or `MEDIUM`.

  * **Group by Asset Type** : Findings are grouped according to their asset type (Google Cloud [resource type](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy)), such as Compute Engine instance or IAM service account.




All findings that are grouped into a case belong to the same owner. To ensure that findings are grouped correctly, including findings with no inherited Google Cloud tags or Essential Contacts, always configure the connector `Fallback Owner` parameter.

### Example: How the grouping mechanism works

In this example, only findings from Google Cloud are used.

The connector ingests four findings with different severities and different values inherited from their respective Google Cloud resources:

  * Finding 1: Severity: `Critical`, Asset Type: `Compute`, Project: `Project_1`

  * Finding 2: Severity: `Critical`, Asset Type: `IAM`, Project: `Project_2`

  * Finding 3: Severity: `High`, Asset Type: `Compute`, Project: `Project_1`

  * Finding 4: Severity: `High`, Asset Type: `Compute`, Project: `Project_2`




#### Default grouping mechanism

Default settings mean that the findings are grouped according to their respective projects, asset types, and severity property.

In this example, every finding is included in a different case.

  * Case 1:

    * Finding 1: Severity: **`Critical`** , Asset Type: **`Compute`** , Project: **`Project_1`**
  * Case 2:

    * Finding 2: Severity: **`Critical`** , Asset Type: **`IAM`** , Project: **`Project_2`**
  * Case 3:

    * Finding 3: Severity: **`High`** , Asset Type: **`Compute`** , Project: **`Project_1`**
  * Case 4:

    * Finding 4: Severity: **`High`** , Asset Type: **`Compute`** , Project: **`Project_2`**



#### Custom grouping mechanism

Selecting only the **Group by GCP Project** checkbox automatically groups findings according to their Google Cloud projects so that a case only contains findings belonging to the same project:

  * Case 1:

    * Finding 1: Severity `Critical`, Asset Type: `Compute`, Project: **`Project_1`**
    * Finding 3: Severity `High`, Asset Type: `Compute`, Project: **`Project_1`**
  * Case 2:

    * Finding 2: Severity `Critical`, Asset Type: `IAM`, Project: **`Project_2`**
    * Finding 4: Severity `High`, Asset Type: `Compute`, Project: **`Project_2`**



Selecting only the **Group by Severity** checkbox automatically groups findings according to their severities so that a case only contains findings with the same severity level:

  * Case 1:

    * Finding 1: Severity: **`Critical`** , Asset Type: `Compute`, Project: `Project_1`
    * Finding 2: Severity: **`Critical`** , Asset Type: `IAM`, Project: `Project_2`
  * Case 2:

    * Finding 3: Severity: **`High`** , Asset Type: `Compute`, Project: `Project_1`
    * Finding 4: Severity: **`High`** , Asset Type: `Compute`, Project: `Project_2`



Selecting only the **Group by Asset Type** checkbox automatically groups findings according to their asset types (resource types in Google Cloud) so that a case only contains findings belonging to the same resource:

  * Case 1:

    * Finding 1: Severity: `Critical`, Asset Type: **`Compute`** , Project: `Project_1`
    * Finding 3: Severity: `High`, Asset Type: **`Compute`** , Project: `Project_1`
    * Finding 4: Severity: `High`, Asset Type: **`Compute`** , Project: `Project_2`
  * Case 2:

    * Finding 2: Severity: `Critical`, Asset Type: **`IAM`** , Project: `Project_2`



Selecting both **Group by GCP Project** and **Group by Severity** checkboxes automatically groups findings according to their respective projects and severity levels so that a case only contains findings belonging to the same project _and_ possessing the same severity. In this example, the connector creates four following cases:

  * Case 1:

    * Finding 1: Severity: **`Critical`** , Asset Type: `Compute`, Project: **`Project_1`**
  * Case 2:

    * Finding 2: Severity: **`Critical`** , Resource Type: `IAM`, Project: **`Project_2`**
  * Case 3:

    * Finding 3: Severity: **`High`** , Resource Type: `Compute`, Project: **`Project_1`**
  * Case 4:

    * Finding 4: Severity: **`High`** , Resource Type: `Compute`, Project: **`Project_2`**



## What's next?

  * Learn more about [alerts](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/whats-on-the-alert-overview-tab) in the Google SecOps documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
