---
url: https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events/
title: Manage maintenance events \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:42.824203+00:00
---

# Manage maintenance events  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage maintenance events

Bare Metal Solution lets you manage your maintenance events in the following ways:

  * View maintenance events
  * Approve a maintenance event
  * Reschedule a maintenance event
  * Cancel a maintenance event



You can't interact with a maintenance event if it's past its deadline, you've already approved or rescheduled it, or it's not in the **Pending** state.

## View maintenance events

  1. In the Google Cloud console, go to the **Maintenance events** page.

[Go to Maintenance events](https://console.cloud.google.com/compute/bareMetalSolution/maintenanceEvents)

The **Maintenance events** page shows the following details for the maintenance events:

Field | Description  
---|---  
**Name** | Name of the maintenance event.  
**Start date** | Scheduled start date of the event. The start date is based on the latest maintenance window proposal that is either pending, approved, or rescheduled.  
**End date** | Scheduled end date of the event. The end date is based on the latest maintenance window proposal that is either pending, approved, or rescheduled.   
**State** | State of the maintenance event. A maintenance event can be in one of the following states:
     * **Pending:** The maintenance event is pending approval.
     * **Scheduled:** The maintenance event is scheduled to take place in the specified window.
     * **Running:** The maintenance event is underway.
     * **Complete:** The maintenance event is complete.
     * **Failed:** The maintenance event has failed.
     * **Closed:** The maintenance event is closed and did not take place or is not going to take place.  
  2. Click the name of the maintenance event.

The **Maintenance event details** page displays the following information for the selected maintenance event:

Field | Description  
---|---  
**Name** | Name of the maintenance event.  
**State** | State of the maintenance event. A maintenance event can be in one of the following states:
     * **Pending:** The maintenance event is pending approval.
     * **Scheduled:** The maintenance event is scheduled to take place in the specified window.
     * **Running:** The maintenance event is underway.
     * **Complete:** The maintenance event is complete.
     * **Failed:** The maintenance event has failed.
     * **Closed:** The maintenance event is closed and did not take place or is not going to take place.  
**Impact** | Impact that the maintenance event might have on your servers.  
**Description** | Description of the activities to be performed in the maintenance event.  
**Start date** | Scheduled start date of the event. The start date is based on the latest maintenance window proposal that is either pending, approved, or rescheduled.  
**End date** | Scheduled end date of the event. The end date is based on the latest maintenance window proposal that is either pending, approved, or rescheduled.  
**Action required by** | Date and time by which you need to take an appropriate action on the maintenance event, that is, either approve it or reschedule it.  
**Outage required** | Whether the maintenance event requires server downtime.  
**Required action** | Specific steps that you need to complete to be ready for the maintenance event. Apart from these specific steps, you must also complete the mandatory basic steps that are explained in [ Prepare for a maintenance event](https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance). **Important:** You must complete the steps specified in this field before the start of the maintenance event.   



The page also displays the following information:

  * **Affected resources:** Lists the name and type of the resources impacted by the maintenance event.
  * **Proposals:** Lists all the maintenance window proposals related to the maintenance event with the following details: 
    * **Create date:** The date of creation of the proposal.
    * **State:** A proposal can be in one of the following states:
    * **Pending:** The proposal is pending approval.
    * **Approved:** The proposal is approved.
    * **Rescheduled:** The proposal is rescheduled.
    * **Proposed start date:** The proposed start date for the maintenance event.
    * **Proposed end date:** The proposed end date for the maintenance event. 



## Approve a maintenance event

If you accept the proposed maintenance window, you can approve the maintenance event.

**Caution:** A maintenance event once approved cannot be rescheduled.

To approve a maintenance event, follow these steps:

  1. In the Google Cloud console, go to the **Maintenance events** page.

[Go to Maintenance events](https://console.cloud.google.com/compute/bareMetalSolution/maintenanceEvents)

  2. Click the maintenance event ID.

  3. On the **Maintenance event details** page, click **Approve maintenance window**.

  4. In the **Approve maintenance window** , read about the preparatory steps that you need to complete before the maintenance event starts.

  5. Click **Approve**. 




## Reschedule a maintenance event

If the proposed maintenance window does not work for you, reschedule the event. 

Consider the following points while rescheduling a maintenance event:

  * A maintenance event once approved cannot be rescheduled. It can only be canceled. See [Cancel a maintenance event](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#cancel-maintenance-event).
  * You can reschedule a maintenance event seven days earlier or fourteen days later than the latest maintenance window proposal that is either pending, approved, or rescheduled.
  * You can reschedule a maintenance event up to three times.
  * We treat the new date and time that you provide while rescheduling as an approved maintenance window from your end.
  * Allow us up to five business days to confirm your request and schedule the new maintenance event.
  * If we cannot schedule your maintenance event for the window you requested, we provide alternate windows for your consideration.



To reschedule a maintenance event, follow these steps: 

  1. In the Google Cloud console, go to the **Maintenance events** page.

[Go to Maintenance events](https://console.cloud.google.com/compute/bareMetalSolution/maintenanceEvents)

  2. Click the maintenance event ID.

  3. On the **Maintenance event details** page, click **Propose new date**.

  4. In the **Propose maintenance window** , do the following:

     1. Select start date and time. The end date and time are set automatically based on the start date and time that you enter.
     2. Click **Send proposal**. 



## Cancel a maintenance event

**Caution:** We do not recommend canceling a maintenance event unless you have an urgent situation in which the maintenance activity might cause a business or service impact.

To cancel a scheduled maintenance event, open a support case with [Customer Care](https://cloud.google.com/support-hub) with the following information:

  * Set the title as `[URGENT] Cancel maintenance`.
  * Set the priority to `P1` (high priority).
  * Include your server ID.
  * Provide the date and start time of when you would like the maintenance event to resume.



## What's next

  * [Prepare for a maintenance event](https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
