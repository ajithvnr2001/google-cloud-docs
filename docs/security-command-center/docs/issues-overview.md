---
url: https://docs.cloud.google.com/security-command-center/docs/issues-overview/
title: Issues overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:38.762063+00:00
---

# Issues overview  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/issues-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Issues overview Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

_Issues_ are notable security concerns that Security Command Center helps identify in your cloud environments. Security Command Center scans and detects issues across your organization.

Issues are discovered through virtual red teaming and rule-based _detections_. For example, a detection with the name **High Risk CVE on GCE with direct access to a high value resource** covers the following situation:

  * A high-risk common vulnerability or exposure (CVE) has been identified on a Compute Engine VM in your cloud environment.
  * That compromised VM has access to a [high value resource](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set) through a service account.



A detection can discover multiple instances of an issue. By default, in the Google Cloud console, issues with the same severity and detection are grouped together.

## Issue sources

Issues are classified as medium, high, or critical severity, and come from the following sources:

  * [Toxic combinations and chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview)
  * [Predefined detection rules](https://docs.cloud.google.com/security-command-center/docs/predefined-detection-rules)
  * [Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * **Design-time findings** from Application Design Center assessments that are integrated into Security Command Center.
  * **Runtime detections** in the Application Design Center.



## Investigate issues

You can find and respond to these security risks on the following the Google Cloud console pages at the organization, folder, project level, or by filtering based on an application:

  * The **Overview** page: Provides an at-a-glance view of your top risks.
  * The **Issues** page: Lists all identified issues with detailed remediation steps for your selected purview.



## Viewing issues at different scopes

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

During an investigation, you can filter by the following:

  * **Organization** : Displays all issues affecting all resources in the organization.
  * **Folder** : Displays issues affecting resources contained in a specific folder or its subfolder when the issue is created by a security graph rule or Correlated Threats rule.
  * **Project** : Displays issues affecting resources contained in a specific project when the issue is created by a security graph rule or Correlated Threats rule.



Security Command Center only generates issues when it is activated at the organization level.

The source of an issue determines whether you can view the issue at the organization, folder, or project level.

  * Issues created by security graph rules and Correlated Threats rules can be viewed at the organization, folder, or project level.
  * Issues created by Risk Engine for toxic combinations and chokepoints must be viewed at the organization level.



### Viewing resource information in a selected resource level

An issue is attributed to a specific folder or project if the primary resource resides in the selected scope. Each security graph rule and Correlated Threats rule identifies the primary resource for the issue.

Scope attribution rules ensure that the issue is attributed to the correct folder and project, even when the security condition is on a primary resource outside of the selected folder or project.

### Access control when viewing issues in a selected purview

To view issues and information about related resources in a selected scope, you must have the required [IAM role](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate#required-roles) at the organization, folder, or project level.

If you don't have the required permissions to view the resources that reside outside of the your selected scope, Security Command Center displays only the issue category, for example, **VM with high-risk CVE with access to sensitive data**.

If a secondary resource is in a different project or folder where you don't have the required IAM permissions, details about the resource are hidden.

## Issue lifecycle

Issues remain active until they are resolved. You can resolve issues by fixing the findings referenced in the issues or by deleting the affected resources.

Inactive issues have a retention period of 90 days, after which they are deleted. For [Correlated Threats issues](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview#issue-lifecycle) ([Preview](https://cloud.google.com/products/#product-launch-stages)), the retention period is 14 days. 

## View application-related information on the Issues page

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When viewing the **Issues** page for an organization, folder, or project, you can see information about the [App Hub application](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration) if the primary resource in the issue is registered as a [service or workload](https://docs.cloud.google.com/app-hub/docs/key-concepts#service) in an application.

Use the **Select app** menu to display only issues where the primary resource is registered in the application that you selected as a service or workload. If **None** is selected, the list isn't filtered by application and displays issues for all resources, including those that are related to an application, and those that aren't related.

When you select a resource in an issue group, the **Overview** panel displays the application name.

## What's next

  * [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate)
  * [Explore the security graph](https://docs.cloud.google.com/security-command-center/docs/graph-search) ([Preview](https://cloud.google.com/products/#product-launch-stages))



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
