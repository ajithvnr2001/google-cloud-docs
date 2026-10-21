---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance/
title: Maintenance overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:39:16.805743+00:00
---

# Maintenance overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Maintenance overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section provides an overview of maintenance for Apigee.

For instructions on scheduling maintenance windows, see [Manage Apigee instance maintenance windows](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/maintenance-windows).

## Overview

Apigee routinely performs updates to ensure that the service is reliable, performant, secure, and up-to-date. Most of these updates are performed with no noticeable impact. These updates are called maintenance.

Maintenance typically falls into the following categories:

  * **Apigee features** : To launch some features, Apigee requires a maintenance update.
  * **Improved performance:** Delivering the best possible performance and reliability.
  * **Security patches and updates** : We continuously monitor for newly identified security vulnerabilities in our software stack. Upon discovery, we patch the system to protect you from new risks.



## Impact of maintenance

Usually, Apigee maintenance is entirely seamless. However, during Apigee maintenance you will be unable to perform certain activities, such as:

  * Creating new instances
  * Attaching an environment to an instance
  * Creating an endpoint attachment
  * Certain scaling activity



## Maintenance settings

Apigee offers you the ability to configure maintenance to occur at the most opportune time for your application. You can do this by configuring maintenance windows.

You can configure the following options for Apigee instances:

  * **Maintenance window** : The day of the week and the hour in which Apigee schedules maintenance to start.
  * **Order of update** : Sets the order in which the instances are updated relative to other instances in the same region. Order of update can be set to Week 1 or Week 2. Week 2 instances are updated one week after Week 1 instances with the same maintenance window in the same region. You set the order of update when you configure a maintenance window. 

**Note:** "Week 1" and "Week 2" refer to the rollout phases and notification lead times (1 week versus 2 weeks). They do **not** refer to the first or second calendar week of the month. For example, a "Week 2" rollout does not necessarily happen in the second week of a calendar month. It happens one week after the "Week 1" rollout for that specific release.




Apigee will schedule the maintenance to start at the specified start time you have configured. Due to differing customer configurations Apigee cannot estimate exactly how long maintenance will take; however, it typically takes several hours.

If a maintenance window is configured for a resource, future automatic maintenance is scheduled to respect these preferences. If a maintenance window is not specified for your resource, maintenance can begin at any time.

Apigee will make a best effort to respect maintenance windows. However, to maintain compatibility and security across our fleet we may sometimes need to update your instance outside of your preferred times.

## Rollout frequency and stability

Apigee does not roll out every runtime version to instances with maintenance windows. Updates are typically bundled and rolled out only when a release has been determined to be highly stable across the fleet. Consequently, your instances might skip several version numbers between updates. New maintenance window rollouts are announced in the [Apigee Release Notes](https://docs.cloud.google.com/apigee/docs/release-notes).

## Freeze and exclusion windows

Apigee currently does not support customer-defined maintenance freeze or exclusion windows. Once a rollout is scheduled, it will proceed according to the configured window and order of update settings. Modifying or clearing your maintenance settings after a maintenance event has been scheduled will not cancel or postpone the scheduled event.

## Maintenance window best practices

We recommend that you set maintenance windows on your production instances, and not set maintenance windows on your non-production instances. This is because of the following broad order of events around a maintenance update:

  1. First, Apigee updates all of your instances that don't have maintenance windows.
  2. Next, Apigee schedules updates for all of your instances that do have maintenance windows. These updates have at least one week (for Week 1 update order) or two weeks (for Week 2 update order) of lead time.
  3. If you have opted in to receive communication about upcoming Apigee maintenance events, then Apigee emails you with notification about the scheduled maintenance.
  4. Apigee performs the maintenance updates at the scheduled times.



Therefore, a notification of upcoming maintenance also means that the same updates have already been applied to all of your instances with no maintenance windows set. If you leave your non-production instances without maintenance windows, you can then guarantee that they receive system updates first, and you can use upcoming-maintenance notifications as a prompt to test or preview the updates in a non-production environment.

### Maintenance example

Assume you are a developer at a retailer managing a shopping cart service, and you have one Apigee instance for a production environment. You want maintenance to start at the time when your instance handles the lowest amount of traffic, which is around midnight on Sundays.

In this case, you set both your production instance maintenance settings to:

  * **Maintenance window** : Sundays starting at 12:00AM UTC
  * **Order of update** : Week 2



The maintenance settings for an instance in your staging environment would be similar, except the order of update would be set to Week 1. Finally, any instances in your development environment would have no maintenance window configured. This ensures you can run operational acceptance tests for a maintenance release in your development and staging environment before maintenance rolls out to production. If something goes wrong in the development or staging environment, you have time to diagnose and fix the issue so that your production environment is unaffected.

**Note:** Apigee will attempt to perform the update in the order specified. However, sometimes maintenance on a resource is unsuccessful. This can result in the Week 2 resource receiving the maintenance while the Week 1 resource is left on the previous release.

## Upcoming maintenance notifications

You can have a notification about upcoming maintenance sent to your email at least one week (for Week 1) or two weeks (for Week 2) before the scheduled maintenance is set to begin. If you want to set an email filter for notifications, the email title is "Upcoming maintenance for your Apigee resource [your-resource-name]".

Maintenance notifications are not sent out by default. If you want to get a notification for an upcoming maintenance you must do all of the following:

  1. Set a maintenance window.
  2. Opt in to maintenance notifications.
  3. Do both of these at least 7 days (for Week 1) or 14 days (for Week 2) before the scheduled maintenance event starts. Otherwise, you have not signed up for notifications in enough time for the system to send you a notification of upcoming maintenance.



Notifications are sent to the email address associated with your Google account. It is not possible to configure a custom email alias (for instance, a team email alias), nor is it possible to subscribe another email address other than your own.

When subscribing, you opt-in to maintenance notifications for all Apigee resources that have maintenance windows in a given project. You receive one notification per resource.

## FAQ

The following are some frequently asked questions about the maintenance policy for Apigee:

### What best practices should I follow for a smooth maintenance update experience?

We recommend you take the following actions to ensure a smooth maintenance update experience:

  * Set your maintenance window to a time ensuring maintenance is not applied in your peak hours of Apigee use.
  * Opt-in to maintenance notifications to be alerted by email at least 7 days (for Week 1) or 14 days (for Week 2) before the scheduled maintenance update begins.
  * Use different non-overlapping maintenance windows for each resource. This means that if there is disruption during the maintenance period you are still able to use the product with the unaffected resources.



### Why were my maintenance settings ignored?

Apigee will make a best effort to respect maintenance windows and the order of update. However, to maintain compatibility and security across our fleet we may sometimes need to update your instance outside of your preferred times. You will not be notified in advance if this occurs, but instance update logs will still be generated for the instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
