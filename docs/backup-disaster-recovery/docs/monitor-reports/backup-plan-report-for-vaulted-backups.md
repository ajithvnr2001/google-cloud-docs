---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-plan-report-for-vaulted-backups/
title: Backup plan reports for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:47.494506+00:00
---

# Backup plan reports for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-plan-report-for-vaulted-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup plan reports for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This report provides comprehensive insights into configured backup plans, detailing their rules, associated backup vaults, and the statistics of the resources they protect.

The report includes the following fields:

  * date: The most recent date on which the backup plan information was updated.
  * backup_plan_name: The designated name of the backup plan.
  * backup_plan_location: The geographical location of the backup plan.
  * backup_rules: A repeated record (array) containing granular details for each backup rule within the plan. Each rule record comprises: 
    * backup_rules.rule_name: The designated name of the backup rule.
    * backup_rules.recurrence: The specified recurrence type for the backup (e.g., "hourly," "daily," "weekly," "monthly," "yearly").
    * backup_rules.recurrence_schedule: The defined recurrence schedule for the backup rule (e.g., "every day at 10:00," "every Monday").
    * backup_rules.backup_window: The defined timeframe (in 24-hour clock format) during which backup jobs are permitted to commence (e.g., "02:00-08:00").
    * backup_rules.backup_window_time_zone: The timezone in which the backups are scheduled (e.g., "UTC," "America/Los_Angeles").
    * backup_rules.retention_days: The specified duration (in days) for which backups are to be retained in accordance with this rule.
  * backup_vault_name: The name of the backup vault intrinsically linked to the backup plan.
  * backup_vault_location: The geographical location of the backup vault associated with the backup plan.
  * resources_protected_count: The quantifiable number of resources protected by this specific backup plan.
  * protected_data_volume_gib: The aggregate data volume (expressed in GiB) of the resources protected by this backup plan.
  * minimum_enforced_retention_days: The minimum mandatory retention period (in days) applicable to backups associated with this backup plan.
  * effective_date_for_enforced_retention_lock: The precise effective date for the enforced retention lock.
  * lock_on_enforced_retention: An indicator of whether the retention is in a locked state. This field is dynamically generated based on the subsequent logic:

    * If the `effective_date_for_enforced_retention_lock` timestamp is present and corresponds to either the current time or a past time, then the value is designated as "locked."
    * If this condition is not met, the value is designated as "unlocked."



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
