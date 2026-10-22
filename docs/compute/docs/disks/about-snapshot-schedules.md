---
url: https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules/
title: About snapshot schedules for disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:20.488928+00:00
---

# About snapshot schedules for disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About snapshot schedules for disks Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

A snapshot schedule creates standard snapshots, which are geo-redundant disk backups, at specified intervals. Use snapshot schedules as a best practice to backup your Compute Engine disks. You can use snapshot schedules to regularly and automatically back up zonal and regional Persistent Disk volumes and Google Cloud Hyperdisk volumes.

## Snapshot schedule properties

A snapshot schedule includes the following properties:

  * Schedule name
  * Schedule description
  * Snapshot frequency (hourly, daily, weekly)
  * Snapshot start time
  * Region where the snapshot schedule is available
  * Source disk deletion policy for handling auto-generated snapshots if the source disk is deleted
  * Retention policy to define how long to keep snapshots that are generated from the snapshot schedule



## Snapshot schedule frequency

**Note:** You can't combine snapshot frequency options. For example, you can't create a snapshot schedule with both an hourly and a weekly schedule.

Before creating a snapshot schedule, choose a start time and a snapshot frequency. The start time is when you want the snapshot schedule to begin. The frequency is defined as hourly, daily, or weekly.

A snapshot schedule begins within the hour of the specified start time. For example, if the scheduled start time is at 12:00, snapshotting starts anytime between 12:00 and 12:59. The schedule uses the UTC time standard.

Snapshot schedules are impacted by daylight savings time (DST) shifts. At the beginning and end of DST in the US, you might see the start times of your snapshot schedule jobs move forward or backward by an hour, respectively, regardless of whether your local timezone uses DST.

  * **Setting an hourly schedule:** To set up an hourly schedule, choose the start time and choose a snapshot interval using an integer between 1 and 23. A snapshot interval defines how often the snapshot is taken. When setting the interval, choose a number that evenly divides 24 (1, 2, 3, 4, 6, 8, or 12) so that the snapshot starts at the same time interval every day. For example, setting a start time of 9:00 with an interval of 6 indicates the snapshot schedule starts between 9:00 and 10:00 with a snapshot interval of every 6 hours.

  * **Setting a daily schedule:** Set the frequency to daily for the snapshot to occur once a day. For example, you can set a snapshot schedule so that a snapshot is generated every day at 9:00.

  * **Setting a weekly schedule:** Set the frequency to weekly for snapshotting on one or more days every week. For example, a start time of 9:00 PM with a weekly schedule set to Monday indicates the snapshot schedule occurs at 9:00 PM on Monday every week. You can also set a weekly schedule that generates snapshots on different days of the week. For example, you might create a schedule for every week on Monday at 14:00 (2:00 PM) and Thursday at 10:00 AM.




## Names for scheduled snapshots

Snapshots captured as a part of your snapshot schedule have automatically generated names. The snapshot names are generated according to the following pattern:
    
    
    [disk-name-prefix]-[scope-name]-[timestamp]-[random-chars]
    

  * `disk-name-prefix`: The name of the source disk. This field can be up to 20 characters.
  * `scope-name`: The name of the zone or region of the source disk.
  * `timestamp`: The UTC creation timestamp in `YYYYMMDDHHMMSS` format.
  * `random-chars`: Randomly generated alphanumeric characters to avoid naming conflicts with other snapshots.



## Snapshot retention policy

You can specify how long Compute Engine retains the automatically created snapshots by setting a snapshot retention policy.

As a best practice, set up a retention policy to minimize snapshot storage costs. If you don't set a retention policy, Compute Engine retains the snapshots indefinitely. You incur storage costs for those snapshots until you manually delete them.

If you choose to set up a snapshot retention policy, you must do so when you create the snapshot schedule.

If you don't set a retention policy, all your auto-generated snapshots will be retained indefinitely. You will incur storage costs for these snapshots until you delete them manually.

### Automatic snapshot deletion

You can specify a maximum retention time period for your snapshot. The maximum retention time period specifies the maximum number of days for which Compute Engine retains your disk's snapshot after its creation. After the maximum retention time period is over, Compute Engine attempts to automatically delete that disk snapshot. Note that Compute Engine completes the auto-deletion of that snapshot only if you have a newer snapshot of the disk available. If you don't have a newer snapshot available, then Compute Engine continues to retain that snapshot until you create a newer snapshot.

For example, if you set its value as `3`, Compute Engine retains the snapshot for a maximum of three days before attempting to delete it. After three days, Compute Engine checks if there is a newer snapshot created for your disk. If such a snapshot is available, Compute Engine automatically deletes your snapshot.

  * The snapshot retention policy applies only to automatic snapshots, not to those you created manually.
  * You cannot apply a retention policy retroactively. If you create a snapshot schedule without a retention policy and then switch to a snapshot schedule with a retention policy, the retention policy will only apply to the new snapshots.
  * Regardless of the retention policy, you can always manually delete automatically generated and manual snapshots.
  * If you want Compute Engine to automatically delete your disk snapshot after a specified maximum retention period, then you must have a newer snapshot created for that disk before the auto-deletion time.
  * If you set a maximum retention time for your disk snapshot, ensure that you use a minimum value of 1 day.



## Source disk deletion rule

When you create a snapshot schedule, you can also set a source disk deletion rule. The source disk deletion rule controls what happens to your snapshots if the source disk is deleted. By default, if your source disk is deleted, snapshots automatically generated from your snapshot schedule are retained permanently unless you delete them manually, regardless of the original retention policy you set, unless you specify otherwise.

Alternatively, you can set the rule so that your snapshot retention policy is applied to your snapshots if the source disk is deleted. For example, you might apply a retention policy that keeps your snapshots for one week after the source disk is deleted.

For example, assume you created a snapshot schedule with a retention policy of 3 days but choose not to apply the retention policy on source disk deletion. After you apply the policy to your Persistent Disk or Hyperdisk, Compute Engine automatically generates snapshots but will also automatically delete snapshots after 3 days, per the retention policy. However, if you then delete the source disk, the retention policy no longer applies and all existing snapshots that were created by this schedule are retained indefinitely.

**Note:** If you detach a snapshot schedule from the source disk and then delete the source disk, the original source disk deletion rule still applies to any snapshots that were generated from that schedule. A snapshot retention policy that specifies **automatic deletion** is applied to your scheduled snapshots even after you detach the snapshot schedule from the source disk.

## Scheduling snapshots for Windows instances

If you are applying a snapshot schedule to disks that are attached to Windows VM instances, use the `guest-flush` option to enable VSS to generate shadow copies of your snapshots. For more information about snapshots for Windows, see [Create a Windows application consistent disk snapshot](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

## Snapshot locality rules and snapshot labels

Similar to manually generated snapshots, you can also apply [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources) and [select the storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location) for auto-generated snapshots. If you set these in your snapshot schedule, any auto-generated snapshots from this schedule will have these properties applied to it. For example, if you set a snapshot locality as `US`, all snapshots generated from this schedule will be stored in the United States of America. See [Create a snapshot schedule](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots#create_snapshot_schedule) for examples on how to set these options.

## Limitations for snapshot schedules

Snapshot schedules have the following limitations:

  * Snapshot schedules apply only in the project that they were created in. Snapshot schedules can't be used in other projects or organizations.
  * You can't create [archive snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots#archive) or [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) using a snapshot schedule.
  * After you create a snapshot schedule, you can make changes to the description, schedule, retention policy, and labels. To update other values for a snapshot schedule, you must delete the snapshot schedule and create a new one.
  * For disks that use a [customer-supplied encryption key (CSEK)](https://docs.cloud.google.com/security/encryption/customer-supplied-encryption-keys), you can't create snapshot schedules.
  * For disks that use a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/kms/docs/cmek), all snapshots created with a snapshot schedule are automatically encrypted with the same key.
  * You can attach a maximum of 10 snapshot schedules at a time to a Persistent Disk volume using the Google Cloud CLI or REST. On the Google Cloud console, you can attach only one snapshot schedule to a disk.
  * You can attach a snapshot schedule to a maximum of 1000 disks.
  * You can create a maximum of 1000 in-use snapshot schedules per region.



## What's next

  * Learn more about [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).
  * Learn how to [create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).
  * Learn how to [manage snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/manage-snapshot-schedules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
