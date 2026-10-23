---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings/
title: Mute findings in Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:35.163345+00:00
---

# Mute findings in Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Mute findings in Security Command Center Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to reduce the volume of findings that you receive in Security Command Center by _muting_ findings.

Muting a finding hides it from the default view of your findings in the Google Cloud console. You can manually or programmatically mute findings and create filters to automatically silence existing and future findings based on criteria you specify.

The Security Command Center detection services provide broad security assessments of your Google Cloud deployment, but you might find that certain findings are not appropriate or relevant for your organization or projects. A high volume of findings also can make it difficult for your security analysts to effectively identify and remediate the most critical risks. Muting findings saves you time from reviewing or responding to security findings for assets that are isolated or fall within acceptable business parameters.

Muting findings has several advantages over [disabling detectors](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/settings/services/modules/disable):

  * You can create custom filters to fine-tune which findings are muted.
  * You can use mute rules to temporarily or indefinitely mute findings.
  * Muting findings doesn't stop underlying assets from being scanned. Findings are still generated but remain hidden until you decide to view them.



## Permissions

To perform specific mute tasks, you need appropriate Identity and Access Management (IAM) roles. For detailed permissions required for each task, see the following:

  * [Manage mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#roles-mute-rules)
  * [Mute individual findings](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings#roles-mute-findings)



## Create and manage mute rules

Mute rules are Security Command Center configurations that use filters you create to automatically mute future and existing findings based on criteria you specify. You can create filters with _static_ or _dynamic_ mute rules.

Static mute rules mute _future_ findings indefinitely. Dynamic mute rules mute _future and existing_ findings temporarily until a specified date or indefinitely until a finding no longer matches the configuration.

### Static and dynamic mute rules

Security Command Center supports static and dynamic mute rule configurations. Although you can use static and dynamic mute rules simultaneously, we don't recommend it. Static mute rules override dynamic mute rules when they are applied to the same finding. As a result, dynamic mute rules won't work as intended, which can create confusion when managing your findings. Therefore, we recommend that you use one mute rule type exclusively.

Unless you are already using static mute rules, we recommend using dynamic mute rules exclusively because they offer more flexibility.

The following table provides a high-level comparison of the two mute rule types. For more details, see Static mute rules and Dynamic mute rules.

Static mute rules | Dynamic mute rules  
---|---  
Indefinitely act on findings. | Can act on a finding either temporarily with an expiration time or indefinitely if no expiration time is set.  
Don't apply to existing findings. | Apply to existing and new findings.  
Take precedence over dynamic mute rules. | Are a lower priority and are overridden by static mute rules when both types apply to a finding.  
  
#### Static mute rules

  * Static mute rules act indefinitely. When a finding matches your static mute configuration, Security Command Center automatically sets the `mute` property of the finding to `MUTED` until you manually change it.
  * Static mute rules have no effect on existing findings unless they are created using the Google Cloud console, in which case the rule will retroactively mute existing findings. Otherwise, they only apply to findings that are newly created or updated after the rule is defined. If you also want to mute similar _existing_ findings without using the Google Cloud console, use the same filters to [bulk mute findings](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings#bulk_mute_findings).
  * Static mute rules take precedence over dynamic mute rules. Therefore, all new findings that match a defined static mute rule are considered muted even if they also match a defined dynamic mute rule.



#### Dynamic mute rules

  * Dynamic mute rules can act on a finding either temporarily with an expiration time or indefinitely if no expiration time is set. When an existing or newly created finding matches your dynamic mute configuration, Security Command Center automatically sets the `mute` property of the finding to `MUTED` until the specified expiration date or until there are changes in the finding or the configuration itself. When a dynamic mute rule expires, Security Command Center removes the rule from the finding. If the finding does not match any other dynamic mute rules, the `mute` property is automatically reset to `UNDEFINED`.
  * Dynamic mute rules automatically apply to existing findings that match your configuration, as well as to findings that are newly created or updated.
  * Dynamic mute rules are a lower priority and are overridden by static mute rules when both types apply to a finding.



We recommend using dynamic mute rules exclusively. The ability to temporarily mute and automatically unmute findings makes dynamic mute rules a more flexible option than static mute rules.

If you are using static mute rules to reduce the number of findings that you review manually, and you want to migrate to dynamic mute rules, see [Migrate from static to dynamic mute rules](https://docs.cloud.google.com/security-command-center/docs/dynamic-mute-migrate).

### Scope of mute rules

Consider the scope of a mute rule when creating filters.

For example, if a filter is written to mute findings in `Project A`, but the filter itself is created under `Project B`, the filter might not match any findings.

Similarly, if [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled, the scope of a mute rule is limited to the Security Command Center location in which the mute rule is created. For example, if you create a mute rule in the **United States** (`us`) location, then the mute rule does not mute findings that are stored in the **European Union** (`eu`) location.

For more information on creating filters, see [Filtering notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications).

### Mute rule restrictions

Mute rules don't support all finding properties. For a list of properties that mute rules don't support, see [Unsupported finding properties for mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#mute_rule_unsupported_properties).

**Note:** Findings belonging to the finding class `SCC errors` report issues that prevent Security Command Center from working as expected. For this reason, error findings can't be muted. For more information, see [Overview of Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

You can create, view, update, and delete mute rules based on the scope of your IAM roles. With organization-level roles, you see mute rules for all folders and projects within the organization. If you have folder-level roles, you can access and manage mute rules for specific folders and all subfolders and projects within those folders. Project-level roles let you manage mute rules in specific projects.

Security Command Center Premium supports granting roles at the organization, folder, and project levels. Security Command Center Standard only supports granting roles at the organization level. For more information, see [Access control](https://docs.cloud.google.com/security-command-center/docs/access-control).

Security Command Center uses active and muted findings to calculate the percentages for compliance controls on the **Compliance** page and in compliance reports. Muting a finding doesn't exclude it from the **Compliance** page or from compliance reports.

### Data residency and mute rules

If [data residency](https://docs.cloud.google.com/security-command-center/docs/data-residency-support) is enabled, the configurations that define mute rules—`muteConfig` resources—are subject to data residency controls and are stored in a [Security Command Center location](https://docs.cloud.google.com/security-command-center/docs/data-residency-support#supported_data_locations) that you select.

To apply a mute rule to the findings in a Security Command Center location, you must create the mute rule in the same location as the findings to which it applies.

Because the filters that are used in mute rules can contain data that is subject to residency controls, make sure you specify the correct location before you create them. Security Command Center does not restrict which location you create mute rules or streaming exports in.

Mute rules are stored only in the location in which they are created and cannot be viewed or edited in other locations.

After you create a mute rule, you can't change its location. To change the location, you need to delete the mute rule and recreate it in the new location.

To learn how to use Security Command Center when data residency is enabled, see [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints). 

## Mute tasks

For instructions on how to perform specific mute tasks, see the following pages:

  * [Manage mute rules](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules)
  * [Mute individual findings](https://docs.cloud.google.com/security-command-center/docs/mute-individual-findings)
  * [Migrate from static to dynamic mute rules](https://docs.cloud.google.com/security-command-center/docs/dynamic-mute-migrate)



## Finding properties related to muting

This section lists finding properties that are related to the mute state of a finding, and describes how they are impacted by mute operations:

  * `mute`: set to `UNDEFINED` when findings are created and changes in the following scenarios: 
    * `MUTED`: a finding is muted manually or by a mute rule.
    * `UNMUTED`: a user unmutes a finding.
  * `muteUpdateTime`: the time that a finding gets muted or unmuted.
  * `muteInitiator`: the identifier for the principal or mute rule that muted a finding.
  * `muteInfo`: mute information about the finding, such as mute rule type (static or dynamic) and which mute rules the finding matched.
  * `muteInfo.staticMute`: a static mute state overrides any dynamic mute rules that apply to this finding. 
    * `state`: a static mute state that can be set by muting the finding directly or a static mute rule.
    * `applyTime`: time when the static mute state was applied to the finding.
  * `muteInfo.dynamicMuteRecords`: The record of a dynamic mute rule that matches the finding. 
    * `muteConfig:` the relative resource name of the mute rule, represented by the mute configuration that created the record. For example, `organizations/123/muteConfigs/examplemuteconfig`.
    * `matchTime`: time when a dynamic mute rule matched the finding.



## What's next

Learn more about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications).

Look through more [examples of filters](https://docs.cloud.google.com/security-command-center/docs/how-to-api-list-findings) you can use.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
