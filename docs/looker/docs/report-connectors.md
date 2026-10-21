---
url: https://docs.cloud.google.com/looker/docs/report-connectors/
title: Managing report connectors \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:52:14.045817+00:00
---

# Managing report connectors  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/report-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Managing report connectors Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports.

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

Looker admins can manage which connectors can be used to create data sources for Looker reports. [_Connectors_](https://docs.cloud.google.com/looker/docs/studio/connector) are the mechanism by which Looker reports access data from a specific data platform, system, or product. When a Looker report connector is enabled on a Looker instance, users can create [_data sources_](https://docs.cloud.google.com/looker/docs/studio/about-data-sources) to add data from the data source's underlying dataset into their Looker reports.

Looker admins can enable all available report connectors or individual connectors. Google-authored connectors are enabled by default.

## Before you begin

To manage the connectors that are available to use to create data sources on Looker reports, note the following requirements:

  * The Looker instance must meet all [requirements](https://docs.cloud.google.com/looker/docs/enabling-studio-in-looker#requirements_and_limitations) to support Studio in Looker.
  * A Looker admin must [enable Studio in Looker](https://docs.cloud.google.com/looker/docs/enabling-studio-in-looker#enabling_studio_in_looker).
  * Users must have the [Looker Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) to enable or disable report connectors.



## Enabling report connectors

To enable one or more report connectors, follow these steps:

  1. In your Looker instance's **Admin** panel, navigate to the **Reports (Studio in Looker)** section, and then open the **Report connectors** page: **Admin** > **Reports (Studio in Looker)** > **Report connectors**.
  2. To enable all of the connectors that are available for use in Studio in Looker, turn on **Select all**. Alternatively, to enable individual connectors, turn on each connector's corresponding toggle.

**Note:** If you don't see the **Report connectors** admin page, confirm that the **Enable reports** setting is turned on from the **Reports setup** admin page. You may need to use that setting to [enable Studio in Looker](https://docs.cloud.google.com/looker/docs/enabling-studio-in-looker) and then click **Manage report connectors** to load the **Report connectors** admin page.

## Disabling report connectors

To disable one or more report connectors, follow these steps:

  1. In your Looker instance's **Admin** panel, navigate to the **Reports (Studio in Looker)** section, and then open the **Report connectors** page: **Admin** > **Reports (Studio in Looker)** > **Report connectors**.
  2. To disable all of the connectors that are available for use in Studio in Looker, turn off **Select all**. Alternatively, to disable individual connectors, turn off each connector's corresponding toggle.



### Effects of disabling report connectors

If a Looker admin disables a connector, the following changes take effect:

  * Users can no longer create Looker reports in the Studio in Looker environment using that connector.
  * Any existing reports that were built with that connector are still accessible from the Looker instance, but report editors can no longer [edit the data source](https://docs.cloud.google.com/looker/docs/studio/edit-a-data-source-article).
  * Any existing reports that were built with the disabled connector can no longer be copied.



Looker admins can still [remove a data source](https://docs.cloud.google.com/looker/docs/studio/delete-a-data-source) from an existing report built with a disabled connector.

## Effects of disabling Studio in Looker

If a Looker admin disables Studio in Looker for a Looker instance, all report connectors are disabled automatically.

Re-enabling Studio in Looker restores the default report connector settings.

## Related resources

  * [About Data Studio data sources](https://docs.cloud.google.com/looker/docs/studio/about-data-sources)
  * [Feature availability in Studio in Looker](https://docs.cloud.google.com/looker/docs/studio-in-looker-feature-availability)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
