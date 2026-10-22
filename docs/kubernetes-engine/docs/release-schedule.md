---
url: https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule/
title: GKE release schedule \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:16.755581+00:00
---

# GKE release schedule  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/resources)



Send feedback 

#  GKE release schedule Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an estimated release schedule for each supported minor version in the [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For [clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel), version milestone dates can be derived from the release channel schedule.

To learn how Google Kubernetes Engine (GKE) upgrades clusters, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades). For more details about GKE version support policies, see [ GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning). To learn about auto-upgrade targets, see [What happens when a version becomes an auto-upgrade target in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target).

This page is for Admins, Architects, and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

### Dates provide a general estimate

The dates in the table are best-effort predictions. Based on qualification and stability of releases, availability and upgrade dates might be delayed. Future dates are updated periodically when new information becomes available, and past dates are updated for accuracy.

To stay up-to-date on version availability and auto-upgrade timing, revisit this page, and subscribe to GKE [upgrade notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications). To get auto-upgrade targets for a specific cluster, see [Get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

#### The timing of automatic upgrades

After a version is announced as an auto-upgrade target, the date of the actual cluster upgrade depends on some of the following factors:

  * The timing of the rollout of the version to the cluster's region. GKE follows a multi-day rollout schedule (typically four or more days) to make new versions available and to auto-upgrade cluster control planes and nodes. Rollouts are paused during weekends and holidays, and include time to observe and monitor for problems.
  * The cluster's configuration of [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).
  * The cluster's exposure to [Kubernetes deprecated features and APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#what_are_kubernetes_deprecations).
  * The cluster's participation in a [rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).



If your business schedule or constraints require different upgrade paths or strategies, you can adjust the scope and timing of the automated upgrades to better align with your business needs. For more information, see [Maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) and [Scope of maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude).

## Estimated schedule for release channels

GKE automatically upgrades clusters in a release channel on or after the dates specified in the _Auto Upgrade_ column of the following schedule. The patches of a minor version remain available in all release channels until the _end of standard support_ (formerly known as _end of life_), except for clusters enrolled in the Extended channel, where the minor version and its patches remain available until the _end of extended support_. You can use [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) to prevent a cluster from being automatically upgraded until its end of support date.

Dates are best-effort predictions and are updated periodically when new information becomes available. Consider the [English language documentation](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule?hl=en) as the source of truth if the dates in other languages differ due to delays in translation.

The following table describes the schedule for clusters enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel). This table doesn't provide estimates for the availability of [alpha patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions), because of the experimental nature of those versions and the restriction to only alpha clusters. For information about the alpha patch versions that are available for alpha clusters, see the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid).

Minor version ([release date](https://kubernetes.io/releases/)) | Rapid | Regular | Stable | Extended | End of standard support (formerly _end of life_)3 | End of extended support3  
---|---|---|---|---|---|---  
Available1 | Auto Upgrade2 | Available1 | Auto Upgrade2 | Available1 | Auto Upgrade2 | Available1 | Auto Upgrade2  
1.30 | 2024-04-30 | 2024-07-30 | 2024-07-30 | 2024-09-17 | 2024-08-13 | 2024-09-24 | 2024-07-30 | 2025-12-03 | 2025-09-30 | 2026-07-30  
1.31 | 2024-08-20 | 2024-09-17 | 2024-10-22 | 2025-03-11 | 2025-01-28 | 2025-04-30 | 2024-10-22 | 2026-06-09 | 2026-01-16 | 2026-10-22  
1.32 | 2024-12-17 | 2025-03-11 | 2025-02-11 | 2025-05-13 | 2025-03-04 | 2025-07-22 | 2025-02-11 | 2026-08-25 | 2026-04-27 | 2027-02-11  
1.33 | 2025-05-07 | 2025-06-10 | 2025-06-04 | 2025-09-09 | 2025-07-22 | 2025-10-14 | 2025-06-04 | _2026-12_4 | 2026-08-12 | 2027-06-12  
1.34 | 2025-09-02 | 2025-10-28 | 2025-11-26 | 2026-03-10 | 2026-02-18 | 2026-06-09 | 2025-12-03 | _2027-Q2_4 | 2027-01-25 | 2027-11-25  
1.35 | 2025-12-24 | 2026-02-11 | 2026-02-11 | 2026-04-28 | 2026-04-07 | 2026-09-15 | 2026-02-11 | _2027-Q3_4 | 2027-04-11 | 2028-02-11  
1.36 | 2026-04-28 | 2026-06-19 | 2026-06-09 | _2026-11_4 | _2026-10-21_5 | _2027-01_4 | 2026-06-09 | _2027-Q4_4 | 2027-08-09 | 2028-06-09  
1.37 | 2026-09-02 | _2026-10-28_5 | _2026-10-21_5 | _2027-Q1_4 | _2027-01_4 | _2027-Q1_4 | _2026-10-21_5 | _2028-Q2_4 | _2027-Q4_4 | _2028-Q4_4  
**Caution:** GKE version 1.29 and earlier have reached [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle) and are no longer supported.

### Stages of release schedule predictions

The dates in the release schedule generally progress through the following stages, which offer increasing levels of granularity and certainty:

  * **TBD** : when an entry is marked as "TBD", the date is to be determined.
  * **Month or quarter year prediction** : dates with only a month (for example, 2025-03) or [quarter year](https://en.wikipedia.org/wiki/Calendar_year#Quarter_year) (for example, 2025-Q3) are approximations that will be updated with a date when it is known. Dates are updated from a quarter year to month prediction when the approximated date is less than three months away.
  * **Day-level prediction** : italicized dates with day-level granularity are provided when the month prediction is less than 14 days from the most recent update to the release schedule table, but the specific date is not yet known. These italicized dates are approximations that will be updated with a specific date when it is known.
  * **Specific date** : non-italicized dates are the best-effort prediction which represent the highest degree of certainty in the release schedule. For more information about the certainty of this information, see Dates provide a general estimate.



## Estimated schedule for clusters with no channel (formerly _static_)

**Warning:** Not enrolling your cluster in a release channel (known as _No channel_ , and formerly as _Static_) is a deprecated configuration option, only allowed for existing customers, and will be removed on June 14, 2027. New customers can't create or update their cluster to use this configuration option. For any clusters not enrolled in a release channel, we recommend that you [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) before this date. After the removal date, GKE enrolls all remaining clusters in the Stable channel. For more information about this deprecation and how you can achieve the same functionality with release channels, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).**Key Point:** GKE automatically upgrades clusters not enrolled in a release channel using automatic upgrade targets from the _Stable_ and _Regular_ channels. Clusters not enrolled in a channel aren't static, as they are upgraded like clusters enrolled in a channel.

GKE automatically upgrades clusters not in a release channel to newer minor versions on or after the dates specified in the _Auto Upgrade_ column of the Stable release channel schedule. You can use [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) to prevent a cluster from being automatically upgraded for [up to 30 days](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) when your cluster isn't enrolled in a release channel.

[Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel) follow this availability and support schedule:

  * Available date: The same available date for the Kubernetes minor version on the _Regular_ Channel, and the same available patch versions as the _Rapid_ channel for those minor versions available in the _Regular_ channel
  * Auto upgrade date: The same auto upgrade date for the Kubernetes minor version on the _Stable_ Channel, and the same auto upgrade date for patch versions as the _Regular_ channel
  * End of standard support (formerly known as _end of life_): The same end of support date for the Kubernetes minor version on release channels other than the _Extended_ channel



#### Notes

**Note:** Dates are updated monthly and subject to change. Dates with only a month (for example, 2025-03) or [quarter year](https://en.wikipedia.org/wiki/Calendar_year#Quarter_year) (for example, 2025-Q3) are approximations that will be updated with a date when it is known. Dates are formatted numerically as YYYY-MM-DD following the [ISO 8601 international standard](https://wikipedia.org/wiki/ISO_8601) for numeric dates. When an entry is marked as "TBD", the date is to be determined.

**Note:** Security patches will continue to be made available and may be applied to existing resources until a version reaches [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning).

  1. The [_Available date_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel) is the approximate date when the Kubernetes version first reaches production, and it takes about one week for it to become available in all regions. ↩

  2. Kubernetes versions are generally available on each release channel a few weeks before auto upgrades start so that you can [test the new version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel). On/after the auto upgrades start date, clusters subscribed to release channels will be auto upgraded to the referenced minor version. ↩

  3. [_End of support_](https://docs.cloud.google.com/kubernetes-engine/versioning#version_support): For clusters in the Rapid, Regular, Stable channels, or no channel ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)), new features, security patches, or bug fixes will be made available for this minor version until its end of standard support (formerly known as _end of life_) date. For clusters in the [ Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended), GKE continues to support the minor version until its end of extended support date. If a cluster is running a patch version of a minor version that has reached its end of support date, GKE auto-upgrades the cluster to help ensure cluster operability and compliance. To learn more, see the [GKE minor version lifecycle](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle). ↩

  4. Dates with only a month (for example, 2025-03) or [quarter year](https://en.wikipedia.org/wiki/Calendar_year#Quarter_year) (for example, 2025-Q3) are approximations that will be updated with a date when it is known. Dates are updated from a quarter year to month prediction when the approximated date is less than three months away. ↩

  5. Italicized dates with day-level granularity are provided when the prediction is less than 14 days from the latest update to the release schedule. These italicized dates are approximations that will be updated with a specific date when it is known. ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
