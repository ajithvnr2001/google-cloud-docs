---
url: https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources/
title: Retain deleted resources in the recycle bin \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:06.186972+00:00
---

# Retain deleted resources in the recycle bin  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Retain deleted resources in the recycle bin Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Recycle bin for Compute Engine snapshots**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Compute Engine protects [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) from permanent accidental or malicious deletion by temporarily retaining deleted standard snapshots for three days. Retaining these snapshots lets you reverse the deletion and recover the data if you need to. Such snapshots are _in the recycle bin_. Retaining deleted standard snapshots can also let you meet certain compliance or regulatory requirements.

This document describes how the recycle bin for standard snapshots works and how to configure the recycle bin to meet your organization's needs.

## Supported Compute Engine resources

The recycle bin supports only standard snapshots.

The following resources **are not supported by the recycle bin and can't be recovered if deleted manually or by an automated process** :

  * Google Cloud Hyperdisk and Persistent Disk volumes
  * Archive snapshots, including archive snapshots that are created by a snapshot schedule
  * Instant snapshots
  * Disk clones
  * Machine images



To protect these resources, implement one of the strategies discussed in [Data protection options for disks and instances](https://docs.cloud.google.com/compute/docs/disks/data-protection).

## How the recycle bin works for standard snapshots

The recycle bin is enabled by default for only standard snapshots, which are retained by default for a three-day _retention period_ , but you can configure custom retention periods. Snapshots that are in the recycle bin are called _recoverable snapshots_. You incur storage costs for recoverable snapshots at the same rate as standard snapshots.

Compute Engine retains deleted standard snapshots in the recycle bin regardless of how the snapshot was deleted—manually or by an automated process.

To reverse a standard snapshot's deletion, you must _recover_ the snapshot from the recycle bin before the retention period expires. After you recover a standard snapshot, you can then use the snapshot to create new disks. If you don't recover the snapshot, Compute Engine permanently deletes the snapshot after the retention period ends.

To disable the recycle bin completely or set custom retention periods for different projects and organizations, configure _the recycle bin retention policy_. To learn more, see [How to configure the snapshot recycle bin](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin).

To prevent data loss, you should check whether the recycle bin is enabled for a standard snapshot before you delete the snapshot. For instructions, see [Check the recycle bin retention period for a specific snapshot](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin#view-retention-period-snapshot).

### Criteria for retaining snapshots in the recycle bin

When you delete a standard snapshot, Compute Engine retains the snapshot in the recycle bin only if at least one of the following conditions is true:

  * The default three-day retention period applies because you haven't configured any custom retention periods.
  * You have set a custom retention period that applies to the standard snapshot, and the retention period is between one and seven days.



Compute Engine permanently erases the snapshot if the applicable retention period is set to zero.

### Outcomes for recoverable snapshots

One of the following outcomes is possible for a recoverable snapshot:

  * **Recovery** : To reverse the deletion, recover the snapshot from the recycle bin before the retention period elapses.
  * **Manual permanent deletion** : To reduce storage costs, you can permanently delete a recoverable snapshot from the recycle bin.
  * **Automatic permanent deletion** : Compute Engine permanently deletes the recoverable snapshot after the applicable retention period elapses.



Recoverable snapshots are read-only; you can't use a recoverable snapshot to create a disk. You must first recover the snapshot; then you can restore the snapshot to a disk.

**Important:** If you or Compute Engine delete a recoverable snapshot, then it is permanently erased.

### Snapshots created by a snapshot schedule

The recycle bin retention policy also applies to standard snapshots that are deleted by a schedule. However, if you later recover such a snapshot from the recycle bin, then Compute Engine retains the snapshot indefinitely until you manually delete it.

Archive snapshots that are created by a snapshot schedule are immediately and permanently deleted because the recycle bin doesn't support archive snapshots.

## How to configure the recycle bin for standard snapshots

The three-day default retention period is called the _system default rule_. To override the system default rule, modify the _recycle bin retention policy_. The recycle bin retention policy is a global set of rules that let you specify which snapshots in your organizations and projects are retained in the recycle bin on deletion, and for how long.

You can specify a retention period of zero to seven days for each rule in the retention policy.

**Caution:** If you set a retention period of zero days for a project or organization, then you disable the recycle bin for that project or organization. For optimal data protection, Google advises against setting the retention period to zero days and recommends maintaining a retention period of at least one day.

To learn more about rules in the recycle bin retention policy, see Use rules to set the recycle bin retention policy.

To learn how to set retention policy rules, see [Configure the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin).

## Use rules to set the recycle bin retention policy

For granular control over how long deleted standard snapshots are retained within your projects and organizations, create rules in the recycle bin retention policy. When you delete a standard snapshot, Compute Engine checks the rules in the retention policy to determine the recycle bin retention period for the standard snapshot, or if the snapshot should be immediately deleted.

By default, the retention policy doesn't contain any rules. When you add a rule to the retention policy, you specify a **target** for the rule and the target's **retention period**.

  * A rule's **target** can be any of the following resources:

    * **A tag** : the rule applies to all standard snapshots that have the tag. Tag-based rules can be scoped to a project or an organization. The tag must already exist.
    * **A project** : the rule applies to all standard snapshots that are in the project if no tag-based rules for the project exist.
    * **An organization** : the rule applies to all projects within the organization if no tag based rules for the organization exist.
  * A rule's **retention period** specifies how long, in days, Compute Engine retains a deleted standard snapshot in the recycle bin. The retention period for a rule must be between zero and seven days, in increments of one day. A value of zero days means that the recycle bin is disabled for the target.




When you delete a standard snapshot, Compute Engine looks for an applicable rule in the retention policy and acts as follows:

  * If an applicable rule exists and the rule's retention period is zero, then the standard snapshot is immediately deleted.
  * If a rule exists, and the retention period is between one and seven days, then Compute Engine retains the standard snapshot in the recycle bin for the duration specified by the rule.
  * If no rule exists, then the default retention period of three days is applied.



To learn how to set retention policy rules, see [Configure the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin).

To understand how Compute Engine applies rules when multiple rules apply to a standard snapshot, see Hierarchy of rules within the recycle bin retention policy.

### Default rules

To reduce costs but still maintain a baseline level of protection for deleted standard snapshots, you can override the default three-day retention period in project or organization.

For example, to keep deleted snapshots in your organization for two days instead of three, set a two-day default retention period for the organization. The default rule you set for a project or organization is called the _project default rule_ and the _organization default rule_ , respectively.

### Combine rules for added flexibility

To balance cost reduction with data protection, combine rules in the retention policy. To do so, set default rules for your projects and organizations, and then create rules that apply to specific tags.

For example, suppose you want to keep deleted snapshots in your organization for one day, but safeguard data within a research project for five days, and then keep snapshots of audit data for seven days.

To configure such a policy for the recycle bin, follow these steps:

  1. Create or choose a tag to identify audit-related standard snapshots.
  2. Create a seven-day tag-based rule for the tag within the organization
  3. Apply the tag to all audit-related standard snapshots.
  4. Set a five-day default rule for the research project
  5. Set a one-day retention rule for the organization



### Use the system default retention period for an organization

To maintain a baseline retention period of three days for all the standard snapshots in your organization, you don't have to take any action. The system default of three days will apply to all standard snapshots.

### Rule conflicts

When multiple rules apply to the same target, Compute Engine applies the most specific rule or the rule with the longest retention period, as discussed in Hierarchy of rules within the recycle bin retention policy.

### Disable the recycle bin for a project or organization by adding a default rule

For projects that don't contain critical data, you can reduce storage costs by disabling the recycle bin for such projects. To do so, set the default retention policy for the project or organization to zero.

### Hierarchy of rules within the recycle bin retention policy

When you delete a standard snapshot, Compute Engine applies the rules that are in the recycle bin retention policy as follows:

  1. **Tag-based rules for the project and organization** : Compute Engine checks if any of the tag-based rules within the retention policy apply to the standard snapshot. If a tag-based rule exists, then Compute Engine applies the rule to the snapshot.

For additional protection from accidental deletion, when multiple tag-based rules apply to the snapshot, Compute Engine applies the rule that has the longest retention period.

For example, suppose that a two-day and a four-day tag-based rule apply to a snapshot. The four-day rule applies in all scenarios, even when the two-day rule is at the project level and the four-day rule is at the organization level. However, a project default rule won't override a tag-based rule even if the former has a longer retention period.

  2. **Project-level default rule** : if there are no tag-based rules at the project or organization level, then Compute Engine applies the default retention rule defined for the project, if one exists.

  3. **Organization-level default rule** : if the project doesn't have a default rule, Compute Engine checks for a default rule for the organization. If one exists, then that rule applies to the deleted snapshot.

  4. **System default rule** : if a rule exists at any of the preceding levels, then the system default rule is ignored. Otherwise, Compute Engine applies the system default rule and retains the deleted standard snapshot for three days.




**Rules with a zero-day retention period** : If a rule is found, and the rule's retention period is zero, then the standard snapshot is immediately deleted. If a rule with a non-zero retention period is found then the standard snapshot is retained in the recycle bin for the duration specified by the rule.

To learn how to view and modify the retention policy, see [Configure the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin).

## Manage the recycle bin

You can also view information about the recoverable snapshots in the recycle bin. To reduce costs you can permanently delete recoverable snapshots from the recycle bin. For more information, see [Manage recoverable snapshots in the recycle bin](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin).

Recoverable snapshots that are in the recycle bin are read-only. To use the snapshot to create a disk, you must first recover the standard snapshot from the recycle bin.

### Recover a snapshot from the recycle bin

When you recover a snapshot from the recycle bin, you can immediately use the snapshot to create disks. However, the following data is not preserved on the snapshot:

  * Tags: You must add any tags back to the snapshot after it is recovered from the recycle bin.
  * Associated snapshot schedules: the snapshot won't be automatically deleted after the duration specified by the snapshot schedule that you used to originally create the snapshot. Instead, Compute Engine retains the snapshot indefinitely until you manually delete it.



To recover a snapshot from the recycle bin, see [Recover a snapshot from the recycle bin](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin#recover-snapshot).

To view the recoverable snapshots within a project, see [View all snapshots in the recycle bin](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin#list-recycle-bin-snapshots).

### Disable the recycle bin

**Warning:** To prevent data loss, Google advises against disabling the recycle bin.

Disabling the recycle bin for standard snapshots means the snapshot's data is permanently erased when the snapshot is deleted. Google cannot recover the data. If you choose to disable the recycle bin, you should do so for only projects that don't contain critical data.

## Limitations

  * **Supported resources** : Only standard snapshots are supported. Archive snapshots, instant snapshots, disks, and images are immediately permanently erased upon deletion. 
  * **Name conflicts** : Recovering a snapshot will fail if a standard snapshot that has the same name already exists and you don't provide a new name for the recovered snapshot. To recover such a snapshot, you must use the Google Cloud CLI or REST to specify a new name. 
  * **Tag persistence** : Tags that are attached to a snapshot before it is deleted are not retained if the snapshot is recovered from the recycle bin. You must [add the tags back](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource) to the snapshot after you recover it from the recycle bin. 
  * **Scheduled snapshots** : If you recover a snapshot that was originally created on a schedule, then the snapshot is no longer part of the schedule and isn't automatically deleted after the duration specified by the schedule. Instead, Compute Engine retains the snapshot indefinitely until you manually delete the snapshot. 
  * **Customer-managed encryption keys (CMEKs)** : If you revoke the CMEK that protects a recoverable snapshot, and you then recover the snapshot, you can't use the recovered snapshot to create a disk until you restore the key. If you don't recover the snapshot before the retention period expires, then Compute Engine permanently erases the snapshot. 
  * **Recovery required before use** : Recoverable snapshots are read-only. To use a recoverable snapshot to create a disk, you must first recover the standard snapshot from the recycle bin. 



## Pricing

**Note:** Storage costs for recoverable snapshots are discounted at 100% while the feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

Storage costs for recoverable snapshots are the same as for standard snapshots.

For example, if a standard snapshot was deleted 30 days after its creation and then stored in the recycle bin for five days, the total storage period is 35 days. Since the recycle bin is in preview, the five-day storage costs are discounted and you incur costs for only 30 days of storage.

Recovering a snapshot from the recycle bin doesn't incur any costs.

For detailed pricing information, see [Disk and image pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk-snapshot-pricing).

## What's next

  * [Configure the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin)
  * [Recover a snapshot from the recycle bin](https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin)
  * [Learn about standard and archive snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
