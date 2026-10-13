---
url: https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage/
title: Manage preview features \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:47.660499+00:00
---

# Manage preview features  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage preview features

Supported in:

Google SecOps 

This guide is for SOC managers who want to manage access to _public preview_ features and for security engineers who want to view and learn about the _public preview_ features in their Google Security Operations environment. The guide explains how administrators enable or disable individual public preview features.

## Common use cases

This section describes the top use cases that this feature addresses.

### View and learn about public preview features

The ability to view the list of all the public preview features, their status (on or off), along with their expected GA dates and documentation provides Google SecOps users with visibility into features in the GA pipeline that include potentially important and beneficial functionality. Users without the administrator role can reach out to an administrator and enquire about plans for the feature within their specific Google Security Operations tenant.

### Turn on a public preview feature and test it

A user with the administrator role can turn on a public preview feature in their Google SecOps tenant—without needing to go through support channels. The administrator can then monitor the feature's benefit and impact in the environment. If a problem with the feature is identified, the administrator can turn the feature off immediately and provide feedback.

## Before you begin

To turn preview features on or off, you must have the **Administrator** role within Google SecOps.

**Note:** All Google SecOps users can view the list of public preview features.

## Key terminology

  * Outside the context of this guide, a _public preview_ feature may also be referred to as a _preview_ feature or _a feature in preview_.

  * **Public preview feature** : a feature that is available for customers to test and provide feedback on before its general availability. Public preview features—that is, pre-GA features, are covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).


**Note:** _Private preview_ features are outside the scope of this document. For matters regarding private preview features, [contact Google SecOps support](https://console.cloud.google.com/support).

## Manage public preview features

This section describes how to view and manage access to public preview features.

## View details about public preview features

Use the **Public Preview Features** page to view details about public preview features. All Google SecOps users can view the **Public Preview Features** page, but only administrators can enable and disable individual features.

  * To open the **Public Preview Features** page, select **SIEM Settings** > **Public Preview**. 



The **Public Preview Features** page displays the following:

  * The number of public preview features that are _enabled_ out of the total number public preview features that are _available_ —for example **Features enabled for public preview (27 of 35)**.
  * A table with one row for every preview feature and the following columns: 
    * **Preview Status** : an On/Off toggle that specifies whether the feature is enabled in the tenant.
    * **Feature Name**
    * **Expected GA Date** : the date that the feature is expected to become generally available. If there is no date specified, the table cell displays a dash (-).
    * **Documentation** : a link to the public document. If there is no relevant document, the table cell displays a dash (-).



### Enable a public preview feature

To enable a public preview feature, do the following:

  1. Select **Settings** > **Public Preview**. 
  2. In the row with the relevant feature, click the **Preview Status** toggle to the on position. 
  3. In the confirmation dialog, click **Enable**.

**Note:** If the functionality of a preview feature depends on some other feature, Google SecOps notifies the administrator to enable both features to ensure proper functionality. 

### Disable a public preview feature

To disable a public preview feature, do the following:

  1. Select **Settings** > **Public Preview**. 
  2. In the row with the relevant feature, click the **Preview Status** toggle to the off position. 
  3. In the dialog that appears, select or describe the reason for disabling the feature.
  4. Click **Confirm**.



### Public preview features in compliance-controlled tenants

In Google SecOps tenants with special compliance controls (for example, FedRAMP or HIPAA): 

  * Using the **Public Preview Features** page to turn features on and off isn't available. 

  * Contact Google SecOps support to get public preview features enabled. 




For more information, see [Set up an Assured Workloads folder](https://docs.cloud.google.com/chronicle/docs/onboard#set-up-assured-workloads-folder).

## Troubleshooting

If you encounter issues, verify that you have the correct administrator permissions. 

For persistent problems, [contact Google SecOps support](https://console.cloud.google.com/support) or your Google representative.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
