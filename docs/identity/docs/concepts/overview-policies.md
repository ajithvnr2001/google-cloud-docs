---
url: https://docs.cloud.google.com/identity/docs/concepts/overview-policies/
title: Policy API overview \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:31:58.076915+00:00
---

# Policy API overview  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/overview-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Policy API overview

The Cloud Identity Policy API lets you programmatically view or modify the settings that administrators configure for a Google Workspace domain in the Google Admin console.

**Note:** To verify that a setting is supported in mutate endpoints, check the **Mutate supported** column in [Policy API supported settings](https://docs.cloud.google.com/identity/docs/concepts/supported-policy-api-settings).

The Cloud Identity Policy API provides a different view of policies than the Google Admin console. For a given setting, the Admin console displays a [reduced setting value](https://docs.cloud.google.com/identity/docs/concepts/policy-api-concepts#terminology) for an organization unit or group, whereas the Cloud Identity Policy API provides the underlying source of truth policies where a value has been explicitly set.

Only a super administrator can use the Cloud Identity Policy API.

## What's next

  * To set up Cloud Identity, see [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).
  * To set up the Policy API, see [Setting up the Policy API](https://docs.cloud.google.com/identity/docs/how-to/setup-policies).
  * To list and get policies, see [Listing and getting policies](https://docs.cloud.google.com/identity/docs/how-to/list-get-policies).
  * To create, patch and delete policies, see [Creating, patching, and deleting policies](https://docs.cloud.google.com/identity/docs/how-to/create-patch-delete-policies).
  * To learn more about which settings are readable or modifiable by the Policy API, see [Policy API supported settings](https://docs.cloud.google.com/identity/docs/concepts/supported-policy-api-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
