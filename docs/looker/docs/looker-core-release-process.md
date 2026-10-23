---
url: https://docs.cloud.google.com/looker/docs/looker-core-release-process/
title: Looker (Google Cloud core) release overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:51.806891+00:00
---

# Looker (Google Cloud core) release overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-release-process/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker (Google Cloud core) release overview Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains the standard release and update processes for Looker (Google Cloud core), along with best practices and variations that may better fit your needs.

## Development and release cycle

A new minor version of Looker (Google Cloud core) is deployed over the course of roughly a couple of weeks. No new releases nor deployments happen in the month of December.

At times, small update patches will be released for fixes that shouldn't wait for the next release. These are nearly always fixes for critical product or security issues. Ideally, no new features would ever be included in a patch release. The application of patch updates follows the same process as upgrading during a standard release.

### Release numbers

The release numbering scheme for Looker (Google Cloud core) uses the same release numbering as for Looker (original) instances, which is a three-number sequence: X.Y.Z, where X is the last two digits of the year of the release, Y is the monthly version (starting with 0 in January, and using even numbers for each subsequent month), and Z is the patch release version. For example, Looker (Google Cloud core) 26.10.1 would be the first patch of the Looker (Google Cloud core) release from June of 2026.

### Release notes

Stay current with any new features and issue fixes by checking out the release notes. See the [Looker releases](https://docs.cloud.google.com/looker/docs/release-notes) page for links to the release notes and changelog for the latest release.

## Release channels

**Preview:**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms. Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions.

Provide feedback or report issues with this preview feature by sending a detailed email to [LookeReleaseChannelFeedback@google.com](mailto:LookeReleaseChannelFeedback@google.com).

Release channels offer greater control and predictability over when new features and updates are applied to your Looker (Google Cloud core) instances. By choosing a release channel, you can balance your organization's needs for early access to the latest capabilities against the need for operational stability in production environments.

During the preview launch, **Rapid** and **Regular** release channels are available. There is also a **No channel** option. The following sections describe each one.

### Rapid release channel

The Rapid release channel provides the earliest access to new features and improvements. The Rapid channel is ideal for non-production, staging, or testing instances, allowing you to validate internal workflows and test new capabilities. When a Looker (Google Cloud core) instance uses the Rapid release channel, [maintenance windows](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) and [deny maintenance periods](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#configure_a_deny_maintenance_period) can't be set for that instance.

If a Looker instance doesn't have a release channel selected, and you enroll that instance in the Rapid channel, there is no change to the release cadence for that instance. The Rapid channel receives new Looker versions once a month and receives security updates as soon as they're available.

If you [opt in to maintenance notifications](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#upcoming_maintenance_notifications), you'll receive an email notification of upcoming instance upgrades for every patch version rollout. The email will be sent to the email address that's associated with your Google Account at least 72 hours before an upgrade is scheduled.

**Caution:** Because the Rapid channel provides the newest Looker (Google Cloud core) versions, these versions are excluded from the [Looker (Google Cloud core) Service Level Agreement](https://cloud.google.com/terms/looker-core/sla).

### Regular release channel

The Regular release channel offers balanced stability, with updates applied on a monthly basis. The Regular channel is the recommended channel for production instances, providing a predictable update cadence while still delivering new features and issue fixes in a timely manner. The Regular channel receives Looker versions one month after the Rapid channel receives Looker versions.

If a Looker (Google Cloud core) instance doesn't have a release channel selected, and you enroll that instance in the Regular channel, there is a one-time delay where that instance may remain on its current Looker version for up to two months, to move the instance from the previous release cadence onto the Regular release cadence.

#### The Accelerated Security Patching (ASP) flag

The Regular release channel offers an Accelerated Security Patching (ASP) configuration, which can be enabled through the `--accelerated-security-patch-enabled` gcloud CLI flag. This flag allows Looker (Google Cloud core) instances to receive updates in the following manner:

  * **Critical security fixes** : Fixes will be applied as soon as they're available. Fixes may not respect set maintenance windows or deny maintenance periods.
  * **Non-critical security updates** : Updates will be applied as part of the next patch or binary release. Updates respect set maintenance windows or deny maintenance periods.
  * **Non-security updates** : Updates are rolled out as part of the next patch or binary release. Updates respect set maintenance windows or deny maintenance periods.



If you [opt in to maintenance notifications](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#upcoming_maintenance_notifications), you'll receive an email notification of upcoming instance upgrades for the monthly version rollout that's scheduled for this channel. The email will be sent to the email address that's associated with your Google Account at least 72 hours before an upgrade is scheduled. However, for critical security patches, notifications of upgrades may be sent less than 72 hours in advance.

### No channel option

If you have an existing Looker (Google Cloud core) instance and you don't edit your instance to enroll in a release channel, or if you select the **No channel** option (in the Google Cloud console) or use the `--release-channel=no-channel` flag when creating a Looker (Google Cloud core) instance, that instance isn't enrolled in a release channel. No channel is the default during the release channels preview.

### Summary of release channels

The following table summarizes the features of each release channel.

Feature | Rapid release channel | Regular release channel | No channel option  
---|---|---|---  
Primary focus | Earliest access to new features and improvements. | Balanced operational stability with predictable updates. | Traditional Looker (Google Cloud core) release process.  
Recommended environment | Non-production, staging, or testing instances (default for trials). | Production environments (default recommendation). | Not applicable.  
Version timing | Receives new Looker versions once a month in binary and patch rollouts | Received **one month after** the Rapid channel. | Receives new Looker versions once a month in binary and patch rollouts.  
Deny maintenance period | **Cannot** be configured. | Allowed by default. | Allowed by default.  
Maintenance windows | **Cannot** be configured. | Allowed by default. | Allowed by default.  
Service Level Agreement (SLA) | **Excluded** from the Looker (Google Cloud core) SLA. | Covered by the standard SLA. | Covered by the standard SLA.  
Accelerated Security Patching (ASP) | Not applicable (already receives security updates as soon as available). | **Available as an optional flag** (`--accelerated-security-patch-enabled`) to receive security fixes as soon as possible. | Not available.  
Upgrade notifications | Email sent at least 72 hours before every patch version rollout. | Email sent at least 72 hours before the monthly rollout. _(Note: For critical ASP patches, notifications may be less than 72 hours)._ | Email sent at least 72 hours before every patch version rollout.  
Enrollment behavior (from No channel) | No change to the existing release cadence.If you have a maintenance window or deny maintenance period set, it will be removed upon enrollment in the Rapid channel. | Possible one-time delay of up to two months to transition onto the Regular cadence. | No change to the release process for the instance.  
  
### Enrolling in release channels

You can choose a release channel for a new Looker (Google Cloud core) instance by using the configuration options section when you're creating an instance. You can also [edit](https://docs.cloud.google.com/looker/docs/looker-core-view-console#config_edit) release channel enrollment in the Google Cloud console or using the `--release-channel=` Google Cloud CLI flag.

If you have an existing Looker (Google Cloud core) instance, and you don't enroll that instance in a release channel, there will be no change to the release process for the instance.

If you enroll an instance in a release channel that updates **more quickly** than its current release cadence, the instance will update to the version of Looker that the new channel is on immediately. For example, if you switch an instance from the Regular channel to the Rapid channel, that instance will update to the Looker version that the Rapid channel is on immediately.

If you enroll an instance in a release channel that updates **more slowly** than its current release cadence, the instance maintains its current Looker version until it is aligned with the Looker version that the new, slower release channel is on. For example, if you switch an instance from the Rapid channel or the No channel option to the Regular channel, there is a one-time delay where that instance may stay on the same version for up to two months.

### Viewing an instance's release channel and Looker version

To view the release channel that your Looker (Google Cloud core) instance is enrolled in, complete the following steps:

### console

  1. Navigate to the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the instance's configuration page.
  2. The release channel is shown in the **Release Channel** field. Options during the preview launch are:

     * **No channel** : Not enrolled in a release channel
     * **Rapid** : Enrolled in the Rapid channel
     * **Regular** : Enrolled in the Regular channel
  3. The Looker version that the instance is using is shown in the **Looker Version** field.

  4. To view the status of the ASP flag, use gcloud CLI.




###  gcloud 
    
    
    gcloud looker instances describe INSTANCE_NAME --region=REGION --format config
    

Replace the following:

  * `INSTANCE_NAME`: a name for your Looker (Google Cloud core) instance; it isn't associated with the instance URL
  * REGION: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in



This command should return a `RELEASE_CHANNEL` field and a `VERSION` field to indicate which channel and version the instance is using. `describe` will also return confirmation if the `--accelerated-security-patch-enabled` flag is enabled.

In addition, non-admin users can see the Looker release that their instance is using by navigating to the **Help** menu within Looker (Google Cloud core) and finding the Looker version next to the **Release Notes** link.

## Update process

Looker (Google Cloud core) applies updates on a rolling basis over the course of a couple of weeks. If you have [defined a preferred window for maintenance](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) of your Looker (Google Cloud core) instance, the Looker (Google Cloud core) Release and Ops teams will apply updates during the maintenance window. If you have not set a maintenance window, you will receive the update within two weeks of the version rollout.

If you have [set a maintenance window](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#set_a_preferred_window_for_maintenance) for your Looker (Google Cloud core) instance, you can [opt in to receive notifications](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#opt_in_to_maintenance_notifications) ahead of upcoming maintenance. Updates generally take around an hour within the maintenance window and may result in downtime.

**Important:** Security upgrades may be applied outside of a preferred maintenance window or during a deny maintenance period. Such upgrades may take place without notifications.

### What if I need to skip a new release version?

You can defer scheduled maintenance of your Looker (Google Cloud core) instance by defining a [deny maintenance period](https://docs.cloud.google.com/looker/docs/looker-core-maintenance#configure_a_deny_maintenance_period) of up to 60 days in length. Instances that are enrolled in the Rapid release channel can't set deny maintenance periods.

**Note:** You must allow at least 14 days of maintenance availability between any 2 deny maintenance periods.

### Does maintenance downtime count toward the SLA?

Downtime associated with maintenance doesn't apply towards the Looker (Google Cloud core) Service Level Agreement.

### Update your Looker (Google Cloud core) version following a deny maintenance period

Following a deny maintenance period, your Looker (Google Cloud core) instance will usually be updated during the first release that occurs after your deny maintenance period ends.

## Extended support release program

Looker (Google Cloud core) doesn't provide an [extended support release (ESR)](https://docs.cloud.google.com/looker/docs/standard-extended-support-release-program-overview) program.

## Getting support

If you have questions, see the [Getting support for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-support) page for information on troubleshooting and contacting Google Cloud support.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
