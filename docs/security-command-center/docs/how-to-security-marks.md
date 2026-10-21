---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks/
title: Annotate findings with security marks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:59:30.424693+00:00
---

# Annotate findings with security marks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Annotate findings with security marks Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security marks are unique to Security Command Center and let you add business context to findings, such as priority, access level, or sensitivity classifications.

After you annotate findings with a security marks, you can search, select, or filter findings using the security marks. You can view marks in the Security Command Center API and the Google Cloud console.

Security marks are processed during batch scans—which run twice daily for Security Command Center Premium and Enterprise and once every other day for Security Command Center Standard—and not in real time. There may be a delay of 12 to 24 hours before security marks are processed and enforcement policies that resolve or reopen findings are applied. 

Security marks on assets are separate from security marks on findings. If you add a security mark to an asset, Security Command Center doesn't automatically add the mark to findings for that asset.

To set security marks on assets, see [Annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).

## Required roles

To get the permissions that you need to add or change security marks on findings, ask your administrator to grant you the Finding Security Marks Writer (`securitycenter.findingSecurityMarksWriter`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Add security marks in the console

You can add security marks to findings by using the console. After adding security marks, you can filter findings in the **Query editor** panel.

To add security marks using the console, do the following:

  1. Go to the Security Command Center **Findings** page in the console.

[Go to the Findings page](https://console.cloud.google.com/security/command-center/findings)

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled for your organization, you must access the page using the jurisdictional console. For more information, see [Use the console with data residency enabled](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-command-center#console-jconsole).

  2. Select the project or organization you want to review.

  3. In the **Findings query results** panel, select one or more findings to add a security mark to by selecting their checkboxes.

  4. Click **Set security marks**.

  5. In the **Security Marks** dialog that appears, click **Add mark**.

  6. Specify the security mark **Key** and **Value**.

For example, if you want to mark findings that are part of the same incident, add a key of `incident-number` and a value of `1234`. Each finding then has the new `mark.incident-number: 1234`.

  7. To edit an existing mark, update text in the **Value** field.

  8. To delete marks, click the trash icon next to the mark: _delete_.

  9. When you're finished adding marks, click **Save**.


**Note:** A mark added to a finding applies only to that specific finding. The mark isn't applied to subsequent findings of the same type.

## Filter findings by security mark

To filter findings by security mark on the **Findings** page, add the `security_marks.marks` attribute to the query statement in the **Query editor**. For example, if the security mark key is `stage` and the value is `dev`, add the following clause to the **Query editor** :

`AND security_marks.marks.stage="dev"`

For more information, see [Query findings in the console](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).

## Manage policies

To suppress findings, you can mute individual findings or create mute rules that automatically mute current and future findings based on filters you define. For more information, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

Muting findings is the recommended method when you don't want to review findings for projects that are isolated or fall within acceptable business parameters.

Alternatively, you can set marks on assets to explicitly include or exclude monitored resources from specific detection policies. For instructions to use dedicated security marks for Security Health Analytics detectors, see [Manage policies in Annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets#managing-policies).

## What's next

  * Learn how to [query findings in the console](https://docs.cloud.google.com/security-command-center/docs/how-to-build-findings-query-console).
  * Learn how to [manage security marks using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks).
  * Learn how to [annotate assets with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
