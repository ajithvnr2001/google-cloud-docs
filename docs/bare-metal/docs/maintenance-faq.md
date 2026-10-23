---
url: https://docs.cloud.google.com/bare-metal/docs/maintenance-faq/
title: Bare Metal Solution maintenance FAQ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:47.766099+00:00
---

# Bare Metal Solution maintenance FAQ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/maintenance-faq/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bare Metal Solution maintenance FAQ

## What is a maintenance event?

To collaborate with you on a maintenance activity that requires server downtime, we create a maintenance event. It contains all the details about the maintenance activity and steps you need to take to prepare for the event. It also lets you take an appropriate action, such as approving or rescheduling the maintenance event.

## When do you schedule a maintenance event?

Ideally, we create a maintenance event two to three weeks before your server is due for maintenance. However, if we need to perform an urgent maintenance activity on your server, you might receive less than three weeks notice from us.

We also send you reminders about your upcoming maintenance events seven days, three days, and one day before the maintenance event with preparatory steps for the event to be successful.

## Where can I view the details of my maintenance event?

You can [view your maintenance event and its details](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#view-maintenance-event) in the Google Cloud console.

## What happens if I don't respond to a maintenance event?

If you do not respond by five days before the scheduled start date of the maintenance event, we might need to cancel it or reschedule it. We notify you if this happens.

## What does it mean if the status of my maintenance event is **Pending**?

A **Pending** status means that your maintenance event is pending approval. You can either approve it or reschedule it.

For more information about approving or rescheduling maintenance events, see [Manage maintenance events](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events).

## Why am I unable to interact with my maintenance event?

If you're unable to interact with a maintenance event, it can be because of one of the following reasons:

  * The maintenance event is past its deadline.
  * You've already approved or rescheduled the maintenance event.
  * The maintenance event is not in the **Pending** state.



## Do I need to do something to prepare my server for the maintenance event?

Yes, you must complete the following preparatory steps:

  * All of the steps in [Prepare for a maintenance event](https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance). 

  * Any additional steps explained in the **Required action** field of your maintenance event.




## What if I am unable to complete preparation for the maintenance event?

If you do not complete the preparatory steps before the maintenance event starts, we might cancel the maintenance event. If we cancel the maintenance event, then your server keeps running in a degraded state until its maintenance is done.

## Why am I unable to reschedule a maintenance event?

If you're unable to reschedule a maintenance event, it's likely for one of the following reasons:

  * You're trying to reschedule an approved maintenance event. After you approve a maintenance event, you can't reschedule it. 
  * You've rescheduled a maintenance event three times, which is the maximum number of reschedules allowed per maintenance event.
  * You're trying to reschedule a maintenance event beyond the permissible time period which is seven days earlier or fourteen days later than the latest maintenance window proposal that is either pending, approved, or rescheduled.



## How many times can I reschedule a maintenance event?

You can reschedule a maintenance event up to three times.

## Can I cancel a maintenance event?

We do not recommend canceling a maintenance event unless you have an urgent situation in which the maintenance activity might cause a business or service impact.

## What happens if the maintenance event fails?

If the maintenance does not complete as planned, we reach out to you about the issues and next steps, including options to continue the maintenance event or revert the server to its previous state.

If you are unreachable or unavailable to respond in time, we roll back the changes and return the server to its previous state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
