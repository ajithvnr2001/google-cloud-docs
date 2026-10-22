---
url: https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details/
title: Looker Support details \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:37.091749+00:00
---

# Looker Support details  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Resources ](https://docs.cloud.google.com/looker/docs/release-notes)



Send feedback 

#  Looker Support details Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page provides information for Looker (original) instances only. For information on Google Cloud Customer Care Support for Looker (Google Cloud core), see the [Getting support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-support) documentation page. 

You can reach Looker Support by using the [Google Cloud console. ](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-integrations-with-google-cloud)

Find details on service level agreements (SLAs) and overall support programs on the [Looker Technical Support Services Guidelines](https://cloud.google.com/terms/tssg/looker) page. 

## Hours of coverage and supported languages

For details about hours of coverage and supported languages, see section "3. Language Support" on the [Looker Technical Support Services Guidelines](https://cloud.google.com/terms/tssg/looker) page. 

## Looker Support regional holidays

For the list of Looker Support regional holidays, refer to the Google Cloud [Language support and working hours](https://docs.cloud.google.com/support/docs/language-working-hours#regional-holidays) document. 

## Who can access Looker Support?

To access Looker support, the following requirements must be met:

  * **Looker support is available only on Looker instances that are running an[officially supported Looker version](https://docs.cloud.google.com/looker/docs/officially-supported-releases).** Instances that are hosted by Looker automatically update to supported releases. If your Looker instance is customer-hosted and is running an unsupported Looker version, [update your Looker instance](https://docs.cloud.google.com/looker/docs/updating-looker-instance) to a supported Looker version. 

  * **For Looker (original) instances, Looker support is available only if the[Google Cloud Project number](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#google_cloud_project_number) is filled in on the Admin General Settings page.** The project number connects your Looker instance to your Google Cloud support plan and determines your level of support. 

  * **Looker support is available only to users with the Tech Support Editor[IAM role](https://docs.cloud.google.com/iam/docs/grant-role-console).** This allows us to focus on your most involved users, who may need in-depth help with the Looker product. You should develop your own internal process for helping your users, especially because you'll know the ins and outs of your data better than anyone. 

    * If your Looker instance is using Legacy Support, then support is available only to administrators and developers on your instance.



## Issue submission best practices

To ensure a timely and effective resolution when you [submit a support case](https://console.cloud.google.com/support/cases), include the following information:

  * The Looker version number of the running application.
  * Environment details, such as OS version, database type and version, and architecture details (for example, whether the instance is containerized or running on a VM).
  * A detailed description of the problem, including the expected behavior and the actual behavior.
  * Steps to reproduce the issue.
  * Any relevant, sanitized log snippets that show errors or other relevant activity. Don't include sensitive information in logs. See the Finding logs section for more information on retrieving logs from customer-hosted Looker instances.



See the [Best practices for working with Cloud Customer Care](https://docs.cloud.google.com/support/docs/best-practices) page for more information.

## Finding logs

For customer-hosted instances, you can find the Looker logs in the `log` subdirectory under the Looker user's home directory (usually `/home/looker`).

The current day's log file is named `looker.log` and is actively being written to. Log files from previous days have dates in their filenames.

**Important:** If you need to download today's log file while Looker is running, make a copy of `looker.log`. Don't attempt to move or rename `looker.log` while the application is writing to it; if you tamper with `looker.log` in any way, Looker will stop writing to log files.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
