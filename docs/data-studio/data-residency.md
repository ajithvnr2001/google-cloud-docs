---
url: https://docs.cloud.google.com/data-studio/data-residency/
title: Set up data residency \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:25.593502+00:00
---

# Set up data residency  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/data-residency/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Set up data residency Stay organized with collections  Save and categorize content based on your preferences. 

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

Data residency lets you keep your data physically within a geographical area during different operations on the data. For many organizations, this is a critical aspect of data governance and helps ensure compliance with regulations.

## Before you begin

To enable data residency settings, you must meet the following prerequisites:

  * You must create a new Data Studio Pro subscription.
  * You must have the [necessary permissions](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription#requirements) to create a new Pro subscription.
  * **Grant authorization if prompted** : When you sign in to Data Studio for the first time, you may be prompted with an OAuth consent dialog requesting access to your Google Account. This authorizes the `datastudio.firstparty` scope to use the Data Studio API. Click **Continue** (or **Allow**) to grant consent. This is a one-time setup and does not need to be done again unless you explicitly [revoke access](https://docs.cloud.google.com/data-studio/remove-or-reconnect-access-to-your-google-account).



## Set a region for data residency

You can enable data residency for your Data Studio Pro assets in Data Studio Pro only while [creating a new subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription). To set up data residency, you can optionally select a single data region from the available regions in the drop-down menu. Multi-region and dual-region locations are not supported.

Your organization might use [organization policies](https://docs.cloud.google.com/organization-policy/overview) to restrict which locations can be used for data residency. If such a policy is in effect, it limits the regions available for you to choose from in the drop-down menu. If no region is available when setting up Data Studio Pro, or if your preferred region is not available, contact your Google Cloud administrator to adjust the organization policy. For more information, see Troubleshoot organization policy restrictions.

**Note:** You can skip this step if you don't want to select a region. In this case, the default region 'global' will be used. However, if your organization policy restricts locations, you can only skip region selection if 'global' is not restricted by the policy.

### Available regions

Data Studio offers data residency in the following regions:

Region | Region description | Location  
---|---|---  
`asia-east1` | Taiwan | Asia Pacific  
`europe-west4` | Netherlands | Europe  
`southamerica-west1` | Santiago | Americas  
`us-central1` | Iowa | Americas  
`us-east4` | Northern Virginia | Americas  
  
### Troubleshoot organization policy restrictions

When setting up your Data Studio Pro subscription, you might see the following error:

`There are no available locations that satisfy your organization policy`

This issue occurs if your Google Cloud organization has configured a location organization policy (`constraints/gcp.resourceLocations`) that restricts all regions supported by Data Studio.

To resolve this issue, follow one of the following options. Note that the steps require you to be a Google Cloud organization administrator.

#### Option 1: Modify the organization policy (recommended)

Update the [resource locations](https://docs.cloud.google.com/organization-policy/restrict-locations) policy (`constraints/gcp.resourceLocations`) on the Google Cloud project or parent folder. Either allow the region you want to use, or remove the policy.

Alternatively, create a separate project or folder that has a more permissive location organization policy that allows the necessary location, and set up your subscription in that project.

#### Option 2: Use Resource Manager tags for conditional exception

If you prefer not to directly modify the location organization policy, you can use Resource Manager tags to conditionally apply the restrictions. Follow these steps:

  1. [Create and attach a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) (for example, `lop_enforcement: exempt`) to the specific projects or folders where you are setting up Data Studio Pro.
  2. Add a conditional rule in the organization policy for `constraints/gcp.resourceLocations` to bypass the location restriction when that specific tag is present.



## Limitations of data residency

Data residency has the following limitations:

  * You can only select one region. Multi-region and dual-region locations are not supported.
  * You can enable data residency only when you create a new subscription.
  * You cannot change the region after the subscription is created, and cross-regional migration of assets isn't supported.
  * You cannot move or copy assets in or out of projects with data residency enabled.
  * If you downgrade from Data Studio Pro to the no-cost version of Data Studio, data residency features are disabled, and regionalized assets will be deleted after a 30-day grace period. You can prevent assets from being deleted by [upgrading to Data Studio Pro](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription) again during the grace period.
  * You cannot use data residency with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). The workaround is to use [Private Service Connect](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints) instead.



### Unavailable or modified features

When data residency is enabled, some features are unavailable or have modified functionality:

  * **Geocoding** : Geocoding is not supported for data from location-restricted regional endpoints. This affects Google Maps and Geo chart visualizations with unstructured geographical data—such as country names, addresses, and city names—that require geocoding to find corresponding latitude and longitude to plot on a map.
  * **Scheduled delivery** : 
    * Delivery to Google Chat and Slack is unavailable.
    * For email delivery, PDF reports are not embedded in scheduled emails. Instead, the email will contain a link to a PDF which will be available for 30 days.
  * **Themes** : The **Extract theme from image** feature is unavailable.
  * **Alerts** : Alerts are unavailable.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
