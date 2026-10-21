---
url: https://docs.cloud.google.com/looker/docs/enabling-looker-reports/
title: Enabling and disabling Looker reports \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:24:12.862724+00:00
---

# Enabling and disabling Looker reports  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/enabling-looker-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Enabling and disabling Looker reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Important:**

As of December 4, 2025, new instances or instances that have not already enabled Looker reports won't be able to enable Looker reports. In addition, if you disable Looker reports, you won't be able to re-enable Looker reports

As of June 15, 2026, the Looker reports preview is no longer supported. If you have enabled the preview for Looker reports, be aware of the following:

  * You will no longer have the option to create new reports.
  * You will lose the ability to view or edit reports that were created during the preview period.



Access to the rest of your Looker content in your instance will remain unaffected and you will continue to have access to Looker as a data source from Data Studio and Data Studio Pro.

You can create ad hoc Explores using Looker's [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) feature, which lets you upload CSV, XLS, and XLSX files to Looker and then query and visualize the data in a Looker Explore without needing to configure a LookML model or set up Git version control.

This document provides guidance for enabling Looker reports on your Looker (original) or Looker (Google Cloud core) instance.

**Important:** By enabling Looker reports, you agree to the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms). Use of Looker reports are subject to the agreement under which you use Google Cloud, not your Looker agreement.**Important:** Don't enable Looker reports on a Looker instance that requires your data to reside in one specific location. Looker reports use globally distributed storage to support high availability.

## Requirements and limitations

Before you enable Looker reports, verify that your Looker (original) or Looker (Google Cloud core) instance meets the following requirements:

  * Your Looker instance must be running Looker 24.18 or later and be Looker-hosted.
  * If your Looker instance uses Google OAuth for authentication, your instance must be running Looker 25.4 or later.

  * You must have the [Admin Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) within your Looker instance.


**Note:** Looker reports are in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`studio-in-looker-feedback@google.com`](mailto:studio-in-looker-feedback@google.com) with the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



### Limitations

Looker reports are in preview, and the following limitations apply:

  * Looker reports aren't supported for Looker (Google Cloud core) instances that are configured to use CMEK, VPC-SC, or [FIPS 140-3 level 1 validated encryption](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode).
  * Looker (Google Cloud core) users who are granted the [Admin via IAM](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin_via_iam) role, but not the [Looker Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) role, won't be able to create or view reports. To enable report usage, assign the Looker Admin role to these users on the Looker **Roles** page in the Admin panel.
  * Users won't be able to use Looker reports if they log in to their Looker instance by using secondary authentication.
  * Looker reports are not accessible using the [Looker mobile application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app).



## Enabling Looker reports

To enable Looker reports, follow the instructions for Looker (original) or Looker (Google Cloud core):

  * Looker (original)
  * Looker (Google Cloud core)



### Looker (original)

To enable Looker reports for a Looker (original) instance, follow these steps:

  1. In Looker, navigate to **Admin** > **Preview** , and enable the **Access Studio in Looker** [preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features).
  2. In Looker, navigate to **Admin** > **Reports** > **Reports setup**.
  3. On the **Reports** page, enable the **Enable Reports** option.



### Looker (Google Cloud core)

**Note:** Looker reports are supported only on Looker (Google Cloud core) instances that are _not_ using [FIPS 140-3 level 1 validated encryption](https://docs.cloud.google.com/looker/docs/looker-core-fips-mode).

To enable Looker reports for a Looker (Google Cloud core) instance, follow these steps:

  1. In Looker, navigate to **Admin** > **Reports** > **Reports setup**.
  2. On the **Reports** page, enable the **Enable Reports** option.



## Using Looker reports with Gemini in Looker

When Looker reports and [Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) are enabled for a Looker instance, Looker users who have the appropriate permissions can query Looker Explore data in natural language by accessing [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview).

  * For Looker (original), the instance must be running Looker 25.2 or later, and the instance must be enabled for Gemini in Looker in the Admin settings. For detailed enablement instructions, see the [Admin settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
  * For Looker (Google Cloud core), the instance must be enabled for Gemini in Looker in the Google Cloud console. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.



## Disabling Looker reports

**Important:**

As of December 4, 2025, if you disable Looker reports, you won't be able to re-enable Looker reports, as new enablements are no longer supported.

**Warning:** If you disable Looker reports, Looker permanently deletes all reports after 30 days. To avoid permanent report deletion, and to restore access to reports, re-enable Looker reports within 30 days of disabling the feature. In addition, only reports created with Looker version 25.4 or later can be recovered. Any reports created with a Looker version prior to Looker 25.4 will be permanently deleted.

To disable Looker reports, follow these steps:

  1. Navigate to **Admin** > **Reports** > **Reports setup**.
  2. Disable the **Enable Reports** option.
  3. Confirm that you understand that you will lose all your report data after 30 days if you disable Looker reports by selecting the box.
  4. Click **Disable**.



## Restoring access to Looker reports

**Important:**

As of December 4, 2025, if you disable Looker reports, you won't be able to re-enable Looker reports, as new enablements are no longer supported.

**Important:** When you disable Looker reports for your Looker instance, users can't access the saved reports on that instance. Per [Cloud Data Processing Addendum (Customers)](https://cloud.google.com/terms/data-processing-addendum), Looker permanently deletes your reports and their associated data 30 days after you disable Looker reports.

To restore access to existing Looker reports on your Looker instance, follow the steps to re-enable Looker reports within 30 days of disabling the feature.

**Important:** Only reports that are created with Looker 25.4 or later can be recovered after disabling Looker reports. Any reports that were created with a Looker version prior to Looker 25.4 will be permanently deleted.

After you re-enable Looker reports, some reports might appear in the **Recovered reports** folder. This typically occurs if the report's original folder was deleted or if the folder's permissions were changed. Admins can [move these reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports#move_reports) from the **Recovered reports** folder to another folder or [delete the reports](https://docs.cloud.google.com/looker/docs/move-share-copy-reports#delete_reports).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
