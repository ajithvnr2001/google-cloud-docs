---
url: https://docs.cloud.google.com/security-command-center/docs/issues-overview/
title: Issues overview \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:48.656439+00:00
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

_Issues_ are notable security risks that Security Command Center helps identify in your cloud environments.

You can find and respond to these security risks on the following pages within the Google Cloud console:

  * The **Overview** page: Provides an at-a-glance view of your top risks.
  * The **Issues** page: Lists all identified issues with detailed remediation steps.



For more information, see [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate).

Issues can originate from both runtime detections and design-time assessments in the Application Design Center.

Issues are discovered through virtual red teaming and rule-based _detections_. For example, a detection with the name **High Risk CVE on GCE with direct access to a high value resource** covers the following situation:

  * A high-risk, common vulnerability or exposure (CVE) has been identified on a Compute Engine VM in your cloud environment.
  * That compromised VM has access to a [high value resource](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set) through a service account.



A detection can discover multiple instances of an issue. By default, in the Google Cloud console, issues with the same severity and detection are grouped together.

## Issue sources

Issues are classified as medium, high, or critical severity, and come from the following sources:

  * [Toxic combinations and chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview)
  * [Predefined detection rules](https://docs.cloud.google.com/security-command-center/docs/predefined-detection-rules)
  * [Correlated Threats](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages))
  * **Design-time findings** from Application Design Center assessments that are integrated into Security Command Center.



## Issue lifecycle

Issues remain active until they are resolved. You can resolve issues by fixing the findings referenced in the issues or by deleting the affected resources.

Inactive issues have a retention period of 90 days, after which they are deleted. For [Correlated Threats issues](https://docs.cloud.google.com/security-command-center/docs/correlated-threats-overview#issue-lifecycle) ([Preview](https://cloud.google.com/products/#product-launch-stages)), the retention period is 14 days. 

## View application-related information on the Issues page

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

When viewing the **Issues** page for an organization, you can see information about the [App Hub application](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#apphub-integration) if the primary resource in the issue is registered as a [service or workload](https://docs.cloud.google.com/app-hub/docs/key-concepts#service) in an application.

The **Select app** menu lets you display only issues where the primary resource is registered in the application that you selected as a service or workload. If **None** is selected, the list isn't filtered by application and displays issues for all resources, including those that are related to an application, and those that aren't related.

When you select a resource in an issue group, the **Overview** panel displays the application name.

## What's next

  * [Manage and remediate issues](https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate)
  * [Explore the security graph](https://docs.cloud.google.com/security-command-center/docs/graph-search) ([Preview](https://cloud.google.com/products/#product-launch-stages))



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
