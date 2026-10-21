---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets/
title: Annotate assets with security marks \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:20.985113+00:00
---

# Annotate assets with security marks  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-assets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Annotate assets with security marks Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security marks are unique to Security Command Center and let you add business context to assets to identify additional information, such as priority, access level, sensitivity classifications, policy application, or integration with your workflow.

After you annotate assets with security marks, you can search, select, or filter assets using these security marks. You can view marks in the Security Command Center API and the Google Cloud console.

Security marks on assets are separate from security marks on findings. If you add a mark to an asset, Security Command Center doesn't automatically add the mark to findings for that asset.

Add or update security marks only on assets that are supported by Security Command Center. For a list of supported assets, see [Supported asset types in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).

To set security marks on findings, see [Annotate findings with security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings).

Security marks are processed during batch scans—which run twice daily for Security Command Center Premium and Enterprise and once every other day for Security Command Center Standard—and not in real time. There may be a delay of 12 to 24 hours before security marks are processed and enforcement policies that resolve or reopen findings are applied. 

## Security marks are different than labels and tags

Labels and tags are similar kinds of metadata that you can use with Security Command Center, but they have a slightly different use and permissions model than security marks.

[Labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) are user-level annotations that are applied to specific resources and are supported across multiple Google Cloud products. Labels are primarily used for billing accounting and attribution.

There are two types of tags in Google Cloud:

  * [Network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) are user-level annotations, specific to Compute Engine resources. Network tags are primarily used to define security groups, network segmentation, and firewall rules.

  * [Resource tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) are key-value pairs that can be attached to an organization, folder, or project. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag.




To read or update labels and tags, you need permissions on the underlying resource. Security Command Center ingests labels and tags as part of the resource attributes. When you post-process `list` API results, you can search for specific labels, tags, keys, and values.

You can add security marks to all resources that are supported by Security Command Center, including all [asset types](https://docs.cloud.google.com/security-command-center/docs/supported-asset-types).

## Required roles

To get the permissions that you need to add or change security marks on assets, ask your administrator to grant you the Asset Security Marks Writer (`securitycenter.assetSecurityMarksWriter`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

This role doesn't include permissions to access the underlying resource.

The IAM roles for Security Command Center can be granted at the organization, folder, or project level. Your ability to view, edit, create, or update findings, assets, and security sources depends on the level that you're granted access for. To learn more about Security Command Center roles, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control). 

## Add security marks to assets in the console

To add security marks to assets in the console, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. From the project selector, select the project, folder, or organization that contains the assets you need to mark.

  3. On the assets display that appears, select the checkbox for each asset that you want to mark.

  4. Click **Set Security Marks**.

  5. In the **Security Marks** dialog that appears, click **Add mark**.

  6. Specify one or more security marks by adding **Key** and **Value** items.

For example, if you want to mark projects that are in a production stage, add a key of "stage" and a value of "prod". All selected projects then have the new `mark.stage: prod`, which you can use to filter them.

  7. To edit an existing mark, update text in the **Value** field. You can delete marks by clicking the trash icon next to the mark: _delete_.

  8. When you're finished adding marks, click **Save**.




The mark now applies to the asset you selected. By default, the **Assets** table shows marks in a column.

For information about dedicated asset marks for Security Health Analytics detectors, see the following section **Manage policies**.

## Filter assets by security mark

To filter assets by security mark on the **Assets** page, use the filter_list**Filter** field. For example, if the security mark key is `stage` and value is `dev`, add the following statement to the **Filter** field:

`Security marks`:`stage`=`dev`

For more information, see [Filter assets](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console#filter-assets).

## Manage policies

**Allowlists with security marks deprecated** : Security Command Center deprecated this feature, and it becomes unavailable for all users on or after April 15, 2025. Until then, this feature is available only in instances of Security Command Center that you activated before June 26, 2023. If you activated Security Command Center on or after June 26, 2023, use the mute feature to suppress findings for certain assets.

For more information, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

You can set marks on assets to explicitly include or exclude those resources from specific policies. To exclude an asset from a Security Health Analytics detection policy, add the security mark `allow_finding-type`. For example, to exclude an asset from the `SSL_NOT_ENFORCED` detector, use the security mark `allow_ssl_not_enforced:true`. This security mark gives you granular control over each resource and detector.

For more information about using security marks in Security Health Analytics, see [Marking assets with marks](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics#security-marks).

To suppress findings directly instead of marking underlying assets, you can manually or programmatically mute individual findings or create mute rules that automatically mute current and future findings based on filters you define. For more information, see [Mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

## What's next

  * Learn how to [inspect assets that are monitored by Security Command Center](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console).
  * Learn how to [manage security marks using the Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/how-to-api-add-manage-security-marks).
  * Learn how to [annotate findings with marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
