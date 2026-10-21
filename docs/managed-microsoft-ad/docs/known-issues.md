---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/known-issues/
title: Known issues for Managed Microsoft AD \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:21:12.703743+00:00
---

# Known issues for Managed Microsoft AD  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)



Send feedback 

#  Known issues for Managed Microsoft AD Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the known issues for Managed Service for Microsoft Active Directory.

## Trust status is stale

Currently, when the trust between a Managed Microsoft AD domain and an on-premises Active Directory domain is broken, the status in the Google Cloud console may not be correctly updated.

To view the latest status of a trust, in the Google Cloud console, [go to the details for the Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/list-describe-delete-domains#getting_domain_info) and in the **Trust relationships** table, click **Validate Trust**.

## No access to event logs for domain controllers

Currently, it is not possible to access the event logs of domain controllers in managed Active Directory domains.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
