---
url: https://docs.cloud.google.com/assured-workloads/docs/restrict-customer-personnel-access/
title: Supporting compliance by restricting customer personnel data access \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:08.780950+00:00
---

# Supporting compliance by restricting customer personnel data access  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/restrict-customer-personnel-access/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supporting compliance by restricting customer personnel data access

This page provides information about supporting compliance with customer personnel restrictions using Identity and Access Management (IAM) in combination with Assured Workloads.

## Overview

Restricting access to data personnel is fundamental to supporting regulatory compliance of Google Cloud resources. Assured Workloads supports compliance by controlling access to your resources by Google personnel. You are still responsible for controlling access to your resources by your organization's personnel.

### Restricting customer personnel access strategies

**Note:** Assured Workloads only provides support for personnel data access controls for Google Cloud if it is supported by the control package you choose.

IAM allows you to create roles and groups that restrict personnel access to data and Google Cloud resources. It is your responsibility to determine the eligibility of staff, based on compliance requirements. We recommend that you determine eligibility before providing access to data. After you have confirmed adjudication, you can use IAM to create a group for the personnel who successfully meet the compliance criteria. You use this group to limit access to Google Cloud resources and data within the Assured Workloads folder to support compliance.

Remaining compliant requires ongoing management of these IAM groups to ensure that:

  * Personnel continue to meet the requirements of the control package.
  * Personnel are properly removed from IAM groups when they don't meet the requirements of the program.



## What's next

  * Learn more about [personnel access controls](https://docs.cloud.google.com/assured-workloads/docs/personnel-access-data-controls).
  * Learn how to [create an IAM group](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console#creating).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
