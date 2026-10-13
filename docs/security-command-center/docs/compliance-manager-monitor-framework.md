---
url: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework/
title: Monitor your frameworks for compliance \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:53.080973+00:00
---

# Monitor your frameworks for compliance  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/compliance-manager-monitor-framework/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Monitor your frameworks for compliance Stay organized with collections  Save and categorize content based on your preferences. 

Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

After you [apply a framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) to your resources, you can view monitoring dashboards that show the status of your environment's compliance with the framework. The monitoring dashboards also provide guidance on how to further align your environment with relevant industry standards and regulatory requirements. You can use the monitoring dashboards to assess your workloads' compliance with multiple frameworks over time. Compliance specialists and privacy teams can use the dashboard to monitor, track, and consult on issues.

The summary monitoring dashboard for Compliance Manager provides an overview of the following:

  * Whether your environment is in compliance with applied frameworks.
  * The list of current findings, with the frameworks that generated them.
  * Filtered views for resources in a specific [App Hub application](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration). Available for Standard-legacy, Standard, Premium, and Enterprise (Deprecated) service tiers.
  * Compliance scores that incorporate both runtime violations and design-time findings detected in application templates. Available for Standard, Premium, and Enterprise (Deprecated) service tiers.



The detailed framework monitoring dashboard provides the following details, related to a specific deployed framework:

  * Whether your environment is in compliance with the applied controls. The compliance scoring is based only on the regulatory controls that are part of the framework. If your framework doesn't include regulatory controls (for example, the [Data security and privacy essentials framework](https://docs.cloud.google.com/security-command-center/docs/dspm-data-security#data-security-framework)), then scoring is based on the cloud controls.
  * Information about how to remediate any violations.
  * Mapping information between cloud controls and regulatory controls.
  * [Shared responsibilities](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) status for cloud controls.
  * Current compliance status, as well as compliance status trends over time.
  * The ability to download a report, in CSV format.
  * The list of top findings related to the framework.



For the steps to remediate each finding, see [Cloud controls reference](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls).

## Before you begin

  * To get the permissions that you need to monitor frameworks, ask your administrator to grant you the [Compliance Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.viewer) (`roles/cloudsecuritycompliance.viewer`) IAM role on your organization or project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 



  * [Apply the frameworks](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) that you want to monitor to the appropriate organization, folders, and projects.



## Monitor your framework

  1. In the console, go to the **Compliance** page.

[Go to Compliance](https://console.cloud.google.com/security/command-center/compliance/monitor)

  2. Select your organization or project.

  3. Click **Monitor (New)**.

The summary dashboard appears. This dashboard provides a summary of applied frameworks and the percentage of cloud controls and regulatory controls that don't have any associated findings. These percentages factor in both runtime and design-time findings.

  4. Standard, Premium, and Enterprise (Deprecated) service tiers and Standard-legacy, Standard, Premium, and Enterprise (Deprecated) service tiers: To display only data related to resources in a specific [App Hub application](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration), use the **Select app** menu. Select **None** to display data for all resources.

You can use the application search and filter options to view compliance for specific applications.

  5. For details about a framework, click the framework.

In the **Framework details** page, the following details are available:

     * The time when the framework was applied, in your time zone.
     * The releases of the framework that's applied. For more information about how Compliance Manager evaluates scoring when multiple versions of a framework are applied, see Monitoring across multiple releases of a deployed framework
     * The organization, folders, or projects that the framework is applied to.
     * A timeline that shows the trends of passing controls.
     * An overview of the controls that are in the framework, including the mapping between regulatory controls and cloud controls. The **Overview by Controls** table displays regulatory controls in the **Control** toggle and cloud controls in the **Cloud Control** toggle. For frameworks that don't have cloud control groups or regulatory controls, cloud control IDs are treated as groups.
     * The findings that are associated with the cloud controls.

This page might take some time to update the findings. For the latest information about findings, use the [**Findings** page](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings). The **Summary** tab for findings shows the applied frameworks and cloud controls that are related to the finding.

  6. To view information from an earlier date, use the date picker.

  7. Standard-legacy, Standard, Premium, and Enterprise (Deprecated) service tiers only: To display only data related to resources in a specific [App Hub application](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration), use the **Select app** menu. Select **None** to display data for all resources.

  8. To download a report about the framework, click **Download report**. The report is downloaded in CSV format. The filename is `framework-name_yyyy-mm-dd.csv`.




## Monitoring across multiple releases of a deployed framework

In some scenarios, your organization or project might have multiple releases of a framework deployed to different projects and folders in your environment. For example, you might deploy release 5 of a framework to a test project, and leave release 4 of the framework applied to a production project.

In this scenario, Compliance Manager aggregates the passing scores for your regulatory controls to create the summary view of passing controls and passing controls over time. If your framework doesn't include any regulatory controls, then the compliance scoring is based on cloud controls. The aggregation logic is as follows:

  * If a control is passing across all assigned releases of the framework, the control is counted as passing.
  * If a control is failing in one or more of the assigned releases of the framework, the control is counted as failing.



The score is calculated as follows:

`TOTAL_UNIQUE_PASSING_CONTROLS` / `TOTAL_UNIQUE_CONTROLS` = `FRAMEWORK_SCORE`

The monitoring summary dashboard shows only the aggregated framework score. The detailed framework monitoring dashboard also includes the following information:

  * The applied releases of the framework
  * In the **Controls Overview** table, the following:

    * The framework releases that a control is included in
    * The cloud control releases that are applied
    * The ability to review findings related to different releases of a control
    * A list of all unique control groups for all applied releases
    * For each control group, a list of all cloud controls and applied releases



## What's next

  * Review the [cloud controls](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-cloud-controls), including the steps to remediate each finding.
  * [Create a custom framework](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-apply-framework) that better matches your organization's security and compliance objectives.
  * [Create an audit report](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit) for your environment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
