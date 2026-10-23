---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/compare-parameter-versions/
title: Compare parameter versions \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:43.526169+00:00
---

# Compare parameter versions  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/compare-parameter-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Compare parameter versions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to compare two different versions of a parameter to identify changes in their payload. The compare functionality lets you audit modifications over time and debug issues related to specific parameter updates.

## Required roles

To get the permissions that you need to compare parameter versions, ask your administrator to grant you the [Parameter Manager Parameter Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Compare parameter versions

To compare parameter versions, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Click the parameter name to view its versions.

The parameter details page opens, displaying all of the versions of the selected parameter on the **Versions** tab.

  3. Select the checkboxes for the two versions that you want to compare, and then click swap_horiz**Compare**.

**Note:** The swap_horiz**Compare** button is enabled only when you select exactly two versions.
  4. Review the differences between the versions.

**Note:** If a parameter version references a secret, the system compares the secret reference string (the resource path), not the rendered secret value. To see a version's secret values, see [Render secrets referenced within a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version).



Alternatively, click the more_vert**Actions** menu associated with a version, and select **Compare**. On the **Compare versions** page, choose another version from the drop-down menu.

## What's next

  * Roll back to a previous version by [creating a new version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version) with the payload you want to use.
  * [View parameter version details](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/view-parameter-version-details)
  * [Render secrets referenced within a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
