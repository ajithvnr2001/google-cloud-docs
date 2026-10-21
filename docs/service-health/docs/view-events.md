---
url: https://docs.cloud.google.com/service-health/docs/view-events/
title: Quickstart: View service health events in the Google Cloud console \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:58:21.334533+00:00
---

# Quickstart: View service health events in the Google Cloud console  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/view-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Quickstart: View service health events in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how to use the Service Health dashboard to view active and past service health events.

You can access your Google Cloud project's service health events by opening the Service Health dashboard in the Google Cloud console. Only events within the selected project scope appear.

## Before you begin

  1. Enable the Service Health API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicehealth.googleapis.com)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions.



### Required roles

To get the permissions that you need to access the Service Health dashboard, ask your administrator to grant you the [Personalized Service Health Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/servicehealth#servicehealth.viewer) (`roles/servicehealth.viewer`) IAM role on the project that you want to view events for. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Find the Service Health dashboard in the Google Cloud console

To access the Service Health dashboard:

  1. [Go to Google Cloud console](https://console.cloud.google.com/).
  2. Select a Google Cloud project.
  3. Select the navigation menu.
  4. Go to **Tools** , and select **Service Health**.



If you see an error message that says "You do not have sufficient permissions to view this page", set [permissions to access the Service Health dashboard](https://docs.cloud.google.com/service-health/docs/manage-access#access-service-health-api-dashboard).

## Find the Service Health dashboard on a mobile device

To view Google Cloud incidents on your mobile device:

  1. Install the [Google Cloud mobile application](https://cloud.google.com/app).
  2. Open the Google Cloud mobile application. The **Dashboard** tab appears.
  3. Select the **Operations** tab.
  4. Select **Personalized Service Health**.



## View Google Cloud incidents

**Note:** If Personalized Service Health itself is experiencing an issue, go to [Google Cloud Service Health](https://status.cloud.google.com/) for status and updates.

The Service Health dashboard lets you view active and closed Google Cloud incidents relevant to the selected Google Cloud project. A list of Google Cloud incidents related to your project appears.

The incident list fields are:

  * **Event State** : Indicates the overall state of the event. It can be one of the following:

    * **Active** : Event is actively affecting Google Cloud and continues to receive updates.
    * **Closed** : Event is no longer affecting any Google Cloud product, or has been merged with another event.

The event also has a **detailed state** enclosed in parentheses. It can be one of the following:

    * **Emerging** : Google engineers are actively investigating the event to determine the impact.
    * **Confirmed** : The incident is confirmed as affecting at least one Google Cloud product. Ongoing status updates are provided until it is resolved.
    * **Merged** : The incident was merged into a parent incident. All further updates are published to the parent only.
    * **Resolved** : The incident is no longer affecting any Google Cloud product after action was taken. There are no further updates.
    * **False positive** : Upon investigation, Google engineers concluded that the incident is not affecting a Google Cloud product. This state can change if the incident is reviewed again.
    * **Auto-closed** : The incident was automatically closed for the following reasons:

      * The impact of the incident could not be confirmed.
      * The incident was intermittent or resolved itself.

The incident does not have a resolution because no action or investigation happened. If it is intermittent, the incident might reopen.

  * **Title** : Brief description of the incident.

  * **Relevance** : Describes how an incident affects your project. The relevance might change as the incident progresses.

    * **Impacted** : The incident is verified to be affecting your project. Available for some Google Cloud products only, including Compute Engine and Persistent Disk.
    * **Related** : The incident has a direct connection with your project and affects a Google Cloud product in a location your project uses.
    * **Partially Related** : The incident is associated with a Google Cloud product your project uses, but the incident might not be affecting your project. For example, the incident might be affecting a Google Cloud product that your project uses, but in a location that your project does not use.
    * **Not Impacted** : The incident is not affecting your project.
    * **Unknown** : The impact on your project is not known at this point.
**Note:** Google might determine that an earlier reported incident did not affect your project, or did not have customer impact on any projects. Personalized Service Health informs you by setting the relevance of the incident as **Not Impacted**. You might also see an update published from Google Cloud Support.
  * **Impacted products** : The Google Cloud products known to be affected by the incident. If the incident is affecting multiple Google Cloud products, you can see the list of products by doing one of the following:

    * Expand the **Impacted products** entry in the list.
    * Go to the incident.

In the expanded list or table, each product includes a status chip or badge indicating its granular disruption status: **Affected** (currently disrupted) or **Resolved** (recovered, even if the overall incident is still active).

During multi-product incidents, the dashboard can show a mixed status combination (for example, Cloud SQL is **Resolved** while Google Kubernetes Engine remains **Affected**). If an active incident expands to impact additional products, newly added services appear as **Affected**.

  * **Impacted locations** : The locations known to be affected by the incident. If the incident is affecting multiple Google Cloud locations, you can see the list of locations by doing one of the following:

    * Expand the **Impacted locations** entry in the list.
    * Go to the incident.

In the expanded list or table, each location includes a status chip or badge indicating its granular disruption status (**Affected** or **Resolved**). Individual locations can be marked as **Resolved** as regional mitigations complete, while other locations remain **Affected**.

  * **Incident start time** : The time Personalized Service Health detected the incident.

  * **Last update** : The latest update from Google Cloud Support.




You can filter the information shown in the Service Health dashboard by doing any of the following:

  * Enter a query in the filter bar. You can filter by fields such as title, impacted products, and date ranges. Personalized Service Health lets you query for information within the past year. If you delete a project, information about it is no longer available in Personalized Service Health.
  * Select a button for the date range.



To view the details of a single Google Cloud incident, select the title of an incident from the incident list. In the incident details page, you can navigate between tabs showing an overview of the incident and full history.

The fields in the **Overview** tab are:

  * **Event State** : The overall state of the event.
  * **Title** : A brief description of the incident.
  * **Event timeline** : A detailed timeline of the incident so far. The timeline is not specific to your project.
  * **Impacted products and locations** : A list of all Google Cloud products and locations known to be affected by the incident, including products and locations you might not be using. 
    * **Relevance** : Describes how an incident affects your project.
    * **Granular disruption status** : A badge (**Affected** or **Resolved**) indicating whether an individual product or location is disrupted or has recovered.
    * **Start time and recovery timestamp** : Displays the disruption start time and, when recovered, the recovery timestamp for each individual product or location pair.
  * **Most recent update** : The latest update from Google Cloud Support.
  * **Diagnosis** : The cause of the incident.
  * **Workaround** : Steps to mitigate the impact of the incident on your project.

**Note:** Alerts configured in Cloud Logging apply to overall event revisions and state changes, not to isolated granular status transitions for individual products or locations.

The **Full Incident History** tab contains a complete list of updates from Google Cloud Support for the history of the incident.

The **Incident Report** tab, if available, shows a summary that includes the factors that contributed to the incident, and the steps Google Cloud plans to take to prevent similar incidents from reoccurring.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
