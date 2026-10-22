---
url: https://docs.cloud.google.com/chronicle/docs/reports/migrate-legacy-dashboards/
title: Migrate legacy dashboards \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:45.492053+00:00
---

# Migrate legacy dashboards  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/migrate-legacy-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate legacy dashboards

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

This guide is for administrators who want to transition legacy Looker dashboards to the modern Google SecOps dashboards using the AI-powered Dashboard Migration tools. The guide explains how to initiate migration jobs, monitor progress, and provide feedback on generated visualizations. By following this process, you can seamlessly standardize on the modern dashboard interface, ensuring operational continuity while retiring deprecated infrastructure.

## Common use cases

### Migrate legacy dashboards

  * **Objective** : Convert Looker-based dashboards and visualizations into the modern dashboard.
  * **Value** : Standardizes operational reporting on the modern dashboard.



### Validate migration results

  * **Objective** : Review migrated dashboards and submit feedback on mapping accuracy.
  * **Value** : Ensures visual and query accuracy through continuous engineering feedback loops.



## Key terminology

  * **Legacy dashboard** : The original Looker-based SIEM dashboard and visualization structure within Google SecOps, scheduled for deprecation.
  * **Dashboard or modern dashboard** : The updated, primary dashboard interface and target architecture in Google SecOps.



## Before you begin

Before starting the migration process, review the following required roles and scope limits:

  * **Permissions** : You must have the `chronicle.admin` role in Google SecOps to access the Dashboard Migration tool.
  * **Limitations** : You can only migrate dashboards saved in shared folders. Personal dashboards located in personal folders and scheduled report deliveries are not supported.



## Migrate legacy dashboards

Follow these steps to initiate a migration job:

  1. In Google SecOps, open the navigation panel and select **Dashboard Migration**. ![Dashboard Migration](https://docs.cloud.google.com/static/chronicle/images/reports/DashboardMigration.png)
  2. In the **Dashboard Overview** tab, click **Start New Migration**.
  3. Select the shared legacy dashboards you want to convert. Then click **Next**.
  4. Confirm your selection and start the conversion job.



## Monitor migration jobs

Track the status of active and historical migration executions:

  1. In Google SecOps, open the navigation panel and select **Dashboard Migration**.
  2. Go to the **Migration Jobs** tab.
  3. Look for your job entry in the list to view the job's summary, such as `JOB_MIGRATION_STATE_SUCCESS` or `FAILURE`.
  4. In the **View Details** column, click the job you want to see more details for. This can include dashboard statuses, error messages, and direct links to generated dashboards.



## Provide dashboard feedback

Because AI translation can produce non-deterministic results, you should submit feedback about mapping inaccuracies to Google SecOps:

  1. In Google SecOps, open the navigation panel and select **Dashboard Migration**.
  2. In the **Recent Migration Jobs** table or detailed job view, locate the generated dashboard link.
  3. Click thumb up thumb_up if the visual layout and query mappings are accurate. Click thumb down  thumb_down if there are any inaccuracies.
  4. If you click thumb down thumb_down to report an issue, select the feedback reasons, such as **Inaccurate content** or **Bug encountered**. In the field, describe the issue and click **Send Feedback**.



## Troubleshooting

  * **Automated error retries** : When a migration job encounters an error, backend systems automatically investigate and retry the job. This happens typically within hours to a few days. You don't need to manually retry the migration job.
  * **Sync boundaries** : The original Looker dashboard remains editable post-migration, but changes made to the legacy dashboard do not automatically copy over or sync to the dashboard version.



### Error remediation

Use this table to resolve common issues during dashboard migration:

**Issue** | **Description** | **Fix**  
---|---|---  
**Migration Error State** | Migration run failed due to query or schema translation errors.  | Allow background automated retries to resolve the issue. If uncorrected, click thumb down thumb_down to send details to Google SecOps.   
**Dashboard Not Visible** | Dashboard missing from the selection list during wizard setup.  | Make sure the dashboard is located in a shared folder not a personal folder.   
  
### Validation and testing

After triggering a migration job, check back in the **Migration Jobs** tab to confirm the status has transitioned to success. You can then validate the resulting Google SecOps dashboard widgets against the source Looker dashboard.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
