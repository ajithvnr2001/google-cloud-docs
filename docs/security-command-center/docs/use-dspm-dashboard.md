---
url: https://docs.cloud.google.com/security-command-center/docs/use-dspm-dashboard/
title: Monitor your data security posture \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:00.404186+00:00
---

# Monitor your data security posture  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/use-dspm-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Monitor your data security posture Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions.  Data Security Posture Management will be shut down on February 1, 2027. Learn more about the controls and [ alternative detection capabilities](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework). 

This document describes the data security dashboard and how you can use it to monitor and analyze your data security posture.

If you're on the Security Command Center Standard tier, [limited DSPM features](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security-standard) are available.

The data security dashboard in the Google Cloud console lets you see how your organization's data aligns with your data security and compliance requirements.

The data map explorer on the data security dashboard shows the geographic locations where your data is stored and lets you filter information about your data by geographic location, how sensitive the data is, the associated project, and which Google Cloud services store the data. The circles on the data map represent the relative count of data resources and data resources with alerts in the region.

You can view data security findings, which occur when a data resource violates a data security cloud control. When a new finding is generated, it can take up to two hours for the finding to appear on the data map explorer.

You can also review information about the data security frameworks that are deployed, the number of open findings associated with each framework, and the percentage of resources in your environment covered by at least one framework.

([Preview](https://cloud.google.com/products/#product-launch-stages)) The dashboard also displays data security insights that you can use to proactively identify potential data risks. The insights are available only for resources that contain highly sensitive data. The resources must be scanned by Sensitive Data Protection, and the scan must be configured to publish results to Security Command Center.

The dashboard shows the following:

  * Users that most frequently access highly sensitive data. A table that highlights which users and service accounts most often access sensitive data. It features an AI-centric view that lets you filter for AI agents. By default, the table displays only AI agent activity if present. Otherwise, the table shows all principals. You can toggle the filter to view all access. The data shown is limited to Cloud Storage buckets, BigQuery tables, and Gemini Enterprise Agent Platform resources.
  * Instances of cross-border access (limited to Cloud Storage buckets, BigQuery tables, and Gemini Enterprise Agent Platform resources only).
  * Instances where country-specific sensitive data is stored outside its associated region (applies to all [Google Cloud resources](https://cloud.google.com/products)).



The dashboard doesn't include security insights for the following:

  * [Assets encrypted by CMEK](https://docs.cloud.google.com/security-command-center/docs/cmek)
  * Resources in `me-central2` region



## Use the DSPM dashboard

Dashboard content and features depend on the Security Command Center tier. If you are on the Standard tier, see [Data Security Posture Management in the Standard tier overview](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security-standard) for what capabilities are available to you in the dashboard.

See [All risk dashboard](https://docs.cloud.google.com/security-command-center/docs/assess-risk#premium-and-enterprise) for more information about the dashboard in the Security Command Center Premium and Enterprise tiers.

Complete the following actions to use the dashboard to analyze your data security posture.

  1. To get the permissions that you need to use the [DSPM dashboard](https://docs.cloud.google.com/security-command-center/docs/use-dspm-dashboard), ask your administrator to grant you the following IAM roles on your organization: 

     * [Data Security Posture Management Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.admin) (`roles/dspm.admin`)
     * [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`)
     * For read-only access: 
       * [Data Security Posture Management Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dspm#dspm.viewer) (`roles/dspm.viewer`)
       * [Security Center Admin Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.adminViewer) (`roles/securitycenter.adminViewer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  2. Use the DSPM dashboard for data discovery and risk analysis. When you enable DSPM, you can immediately assess how your environment aligns with the [Data security and privacy essentials framework](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework). 

In the Google Cloud console, go to the **Data Security & Compliance** page, and then select your Google Cloud organization. After you select an organization, you are redirected to the **Data** tab in the **Risk overview** dashboard.

[Go to the Risk Overview Dashboard](https://console.cloud.google.com/security/command-center/overview/data-security)

Use this information to review and remediate findings so that your environment better aligns with your security and compliance requirements.

When you view the dashboard from an organization level and you deploy applications in a [folder configured for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications), you can select an application to filter the dashboard to show only the findings and insights that apply to the application. Consider the following [scan latencies](https://docs.cloud.google.com/security-command-center/docs/concepts-scan-latency-overview#scan_latency) when reviewing the data:

     * The top findings panel might show outdated resource configuration data. For example, a finding's primary resource might be associated with an outdated application.

     * The application selector might not show the applications and resource registrations that were created within the last 24 hours.

The data map explorer might take 24 hours after you activate Security Command Center to populate all the data from Security Command Center and Cloud Asset Inventory.




## What's next

  * [Review findings related to data security](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#dspm-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
