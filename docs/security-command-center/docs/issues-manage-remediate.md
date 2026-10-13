---
url: https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate/
title: Manage and remediate issues \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:48.721936+00:00
---

# Manage and remediate issues  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/issues-manage-remediate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Manage and remediate issues Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

## Required roles

To get the permissions that you need to work with issues, ask your administrator to grant you the following IAM roles on the organization: 

  * To view issues, one of the following roles: 
    * [Security Center Findings Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.findingsViewer) (`roles/securitycenter.findingsViewer`)
    * [Security Center Issues Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesViewer) (`roles/securitycenter.issuesViewer`)
  * To view, mute, and unmute issues: [Security Center Issues Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.issuesEditor) (`roles/securitycenter.issuesEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to work with issues. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to work with issues:

  * To view issues: 
    * `securitycenter.issues.get`
    * `securitycenter.issues.list`
    * `securitycenter.issues.group`
    * `securitycenter.issues.listFilterValues`
  * To mute and unmute issues: `securitycenter.issues.mute`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View issues

You can find issues in Security Command Center on the following pages:

  * The **Overview** page shows an at-a-glance view of the top risks found in your cloud environments, including issues and Correlated Threats.
  * The **Issues** page lists all issues that were found in your cloud environments and provides details on each of the issues, including how to remediate them.



To view all issues, go to **Issues**.

To view individual issues, expand a detection group, and then click one of the issues in the group. The issue's details panel opens, which contains the following elements:

  * A summary of the issue.
  * An interactive attack path or evidence diagram.
  * Findings related to the issue.
  * For Correlated Threats, the **MITRE ATT &CK tactics** section, which provides details about the nature of the attack that's tied to the issue.
  * A **How to fix** tab, which provides remediation steps.
  * For toxic combinations and chokepoints, an **Exposed valued resources** tab, which lists the high-value resources that are affected by the issue.
  * For security graph insights, an **Impacted Resources** tab, which lists the resources that contribute to the issue. This tab displays if more than six resources contribute to an issue.
  * A **JSON** tab, which provides the issue data in JSON format.



To step between issues in the queue, click the arrow icons next to **Take Actions**.

## Remediate issues

To remediate an issue, complete the following instructions:

### View all issues

  1. To view all issues, go to the Security Command Center **Issues** page. 

[Go to Issues](https://console.cloud.google.com/security/command-center/issues)

  2. Select your Google Cloud organization.



### Sort by attack exposure score

  1. By default, grouped issues are ranked by severity. Within the group, the issues are ranked by attack exposure score. To sort all issues by attack exposure score instead, disable **Group by detections**.

**Note:** Correlated threats are also tagged with a risk type of **Active Threat** and a **Critical** severity level. These threats always appear at the top of the issues list.
  2. Select an issue.

  3. Review the issue's description and evidence.




### Access findings details and take action

You can view details for any active finding to help identify the root cause of an issue. Depending on the issue, you can also filter results by resource, explore full attack paths, or view remediation guidance.

  1. To access more information for any finding, click **View details**. If multiple critical issues are found on a primary resource in a toxic combination or chokepoint, a message displays after the **Evidence** diagram.
  2. To optimize your remediation efforts on findings, follow these steps as needed:

     * Filter issues for the resource: To focus on resolving issues for that specific resource, click **Filter issues for this primary resource** in the displayed message. If you want to remove the filter, click the back arrow next to ![Open filter panel](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Add filter**.

     * Explore full attack paths: For a more in-depth understanding of the issue and how the attack paths expose high-value resources, Click **Explore full attack paths** within the **Evidence** diagram.

     * Get mitigation guidance: to help mitigate the risk, click **How to fix** and follow the provided instructions.




## Mute issues

If the risk that's posed by an issue is acceptable to your business or you can't remediate it, you can choose to mute it. This tags the issue as muted, and records who muted the issue and when. You can only mute individual issues, not entire detections.

To mute an issue, complete the following steps:

  1. Open an issue's details panel.
  2. Click **Take Actions**.
  3. Click **Mute**.
  4. Enter the reason why you are muting the issue, and then click **Mute**.



After you've muted an issue, it can take a few minutes for this to be reflected in the issues list. After this, the issue won't show in the list with the default filters applied.

## View muted issues

To view muted issues, click ![Add filter](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Add filter** , and then add a **Show muted issues** filter with a value of **Yes**. Click **Apply** to apply the filter.

## Unmute issues

To unmute an issue, complete the following steps:

  1. Filter the view by muted issues.
  2. Open the issue's details panel.
  3. Click **Take Actions**.
  4. Click **Unmute**.
  5. Enter the reason why you are unmuting the issue, and then click **Unmute**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
