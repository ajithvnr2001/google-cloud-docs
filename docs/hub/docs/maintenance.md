---
url: https://docs.cloud.google.com/hub/docs/maintenance/
title: View maintenance activities \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:21.276784+00:00
---

# View maintenance activities  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  View maintenance activities Stay organized with collections  Save and categorize content based on your preferences. 

The Maintenance page lets you track scheduled, ongoing, completed, and canceled maintenance events across [Google Cloud services](https://docs.cloud.google.com/unified-maintenance/docs/supported-services) that [Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/overview) supports. Monitoring maintenance across your projects or App Hub applications helps keep resources reliable, secure, and current.

Depending on the service, you can configure maintenance windows or defer updates. Other events are fully managed by Google and you can't reschedule them.

## Before you begin

  1. [Set up Cloud Hub](https://docs.cloud.google.com/hub/docs/setup-cloud-hub).

  2. Choose the project where you want to enable the Unified Maintenance API, if the API isn't already enabled. The project must contain or have access to your maintenance logs.

     * If you set up an app-enabled folder to manage applications, enable the APIs on the folder's management project.
     * To view data for a single project, enable the API on that project.
     * If you have multiple projects that are not in an app-enabled folder, you can configure a single project to provide an aggregated view of log data from other projects. You can then enable the Unified Maintenance API on that project.

[Go to project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Enable the API on the project you selected.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=maintenance.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to view maintenance activities, ask your administrator to grant you the [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) IAM role on the project or management project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The Logs Viewer role is included in the Cloud Hub Operator (`roles/cloudhub.operator`).

For information about permissions to perform additional tasks with maintenance logs, such as setting alerts and notifications, see the [Unified Maintenance documentation](https://docs.cloud.google.com/unified-maintenance/docs/access-control).

## View current and scheduled maintenance

To view maintenance activities that are scheduled and started, follow these steps:

  1. In the Google Cloud console, go to the **Maintenance** page:

[Go to Maintenance](https://console.cloud.google.com/cloud-hub/maintenance)

  2. From the project selector, select the project or management project that you want to view.

The Maintenance page displays the total number of scheduled and started activities in the **Maintenance summary** section.

The **Maintenance** table displays scheduled and started activities. If you can control or configure an activity, the more_vert **Settings** menu is available for that activity.

  3. To filter the displayed maintenance activities, select options from the following selectors:

     * **Category** \- Select the types of maintenance that you want to view. **Infrastructure** maintenance is regular maintenance on Google Cloud network equipment and host machines. Service update maintenance is an update to services that include bug fixes, changes, or new features.
     * **Location** \- Select resource locations that you want to view.
     * **Resource Type** \- Select the types of resources you want to view.
  4. To run or reschedule a maintenance activity that you can control, click more_vert **Settings** and then click **Reschedule** or **Run maintenance**. Documentation that explains how to reschedule or run the maintenance activity is displayed.

  5. To view details about a maintenance activity, click the activity name.

The **Maintenance details** page displays the following information:

     * **Description** \- A description of the maintenance activity. It includes links to product-specific information to help you manage the maintenance activity.
     * **Timeline** \- The scheduled start time, scheduled end time, and actual start time (if the activity has started).
     * **Resource progress** \- A summary of the number of resources with scheduled, running, successful, and canceled states.
     * **Locations** \- The locations of impacted resources.
     * **Affected Google Cloud resources** \- A list of resources that are impacted by the maintenance activity with the impacted resource name, location, resource type, maintenance state, and timeline (scheduled start time, actual start time, actual end time, and duration).

If the activity can be rescheduled, the **Reschedule** button links to documentation that explains how to reschedule the activity.




## View maintenance history

To view maintenance activities that are completed or canceled, follow these steps:

  1. In the Google Cloud console, go to the **Maintenance** page:

[Go to Maintenance](https://console.cloud.google.com/cloud-hub/maintenance)

  2. From the project selector, select the project or management project that you want to view.

The Maintenance page displays the total number of completed and canceled activities in the **Maintenance summary** section.

The **Maintenance history** table displays completed and canceled activities in the last 30 days.

  3. To filter the displayed maintenance activities, select options from the following selectors:

     * **Category** \- Select the types of maintenance that you want to view. **Infrastructure** maintenance is regular maintenance on Google Cloud network equipment and host machines. Service update maintenance is an update to services that include bug fixes, changes, or new features.
     * **Location** \- Select resource locations that you want to view.
     * **Resource Type** \- Select the types of resources you want to view.
  4. To view details about a maintenance activity, click the activity name.

The **Maintenance details** page displays the following information:

     * **Description** \- A description of the maintenance activity. It includes links to product-specific information to help you manage the maintenance activity.
     * **Timeline** \- The scheduled start time, scheduled end time, actual start time, actual end time, and duration of the maintenance activity.
     * **Resource progress** \- A summary of the number of resources with scheduled, running, successful, and canceled states.
     * **Locations** \- The locations of impacted resources.
     * **Affected Google Cloud resources** \- A list of resources that are impacted by the maintenance activity with the impacted resource name, location, resource type, maintenance state, and timeline (scheduled start time, actual start time, actual end time, and duration).



## What's next

  * [Learn more about Unified Maintenance](https://docs.cloud.google.com/unified-maintenance/docs/overview).
  * Learn about setting [alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications) for maintenance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
