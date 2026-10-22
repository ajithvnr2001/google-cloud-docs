---
url: https://docs.cloud.google.com/hub/docs/health/
title: View application and resource health \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:26.773436+00:00
---

# View application and resource health  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  View application and resource health Stay organized with collections  Save and categorize content based on your preferences. 

The **Health & troubleshooting** page lets you review the health of your services and applications.

  * View open alerts based on [alerting policies](https://docs.cloud.google.com/monitoring/alerts) that you set up in Cloud Monitoring.
  * View active Google Cloud incidents. These incidents are for Google Cloud service outages or degradations.
  * View metrics about the health and performance of Google Cloud resources such as utilization, latency, or errors.



You can view health data for projects and [supported infrastructure](https://docs.cloud.google.com/stackdriver/docs/observability/application-monitoring-services) in App Hub applications.

  * In the project view, you can view health data for active Google Cloud products in the selected project.
  * In the application view, you can view health data for services and workloads in the selected application.



You can also use [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) to help you troubleshoot an issue.

## Before you begin

To view data for App Hub applications, ensure that the following steps are complete:

  1. [Set up App Hub for a folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) and create your applications.

  2. [Set up aggregation of logs, metrics, and traces](https://docs.cloud.google.com/stackdriver/docs/observability/setup-application-monitoring) for your applications.




To use investigations, [set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

**Note:** Cloud Hub only supports applications in a folder configured for application management. It doesn't support applications in a [host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

### Required roles

To get the permissions that you need to view health data for applications and resources, ask your administrator to grant you the following IAM roles on the project ([project view](https://docs.cloud.google.com/hub/docs/app-project-views#project-view)) or management project for a folder ([application view](https://docs.cloud.google.com/hub/docs/app-project-views#app-view)): 

  * View application and project data: [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) 
  * Create and view investigations: [Investigations Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationCreator) (`roles/geminicloudassist.investigationCreator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you want to make changes based on your analysis, you might need additional permissions or you might need to coordinate with a member of your organization who has the required permissions. For example, changing the configuration of a GKE cluster requires the appropriate GKE permissions.

## View health and troubleshooting information

  1. In the Google Cloud console, go to the **Health & troubleshooting** page:

[Go to Health & troubleshooting](https://console.cloud.google.com/cloud-hub/health-and-troubleshooting)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

  3. From the time range selector, choose a time range to view. By default, the page displays alerts, Google Cloud incidents, and health data for the last hour.

The page displays the following information for the selected time range:

     * **Open alerts** : displays the total number of open alerts for alert policies in a selected project or associated with a selected application. To view the alerts in Monitoring, click **View alerts**. For details about viewing alerts, see [Alerts for metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events).
     * **Google Cloud incidents** : displays the total number of Google Cloud incidents for the selected project or application. To view the incidents in Personalized Service Health, click **View incidents**. [Learn more about viewing incidents](https://docs.cloud.google.com/service-health/docs/view-events) in Service Health.
     * **Google Cloud products** (project view): displays open alerts and Service Health events, including incidents, for each active Google Cloud product in the selected project. Charts with key health data for the selected product are displayed below the product list.
     * **Services and workloads** (application view): displays open alerts and Service Health events, including incidents, for each active Google Cloud service or workload in the application. Charts with key health data for the selected service or workload are displayed below the list of services and workloads.
  4. To view details for a listed product, service, or workload, click its name in the list. You can use the following options to help you understand events that occurred or troubleshoot issues.

     * Review the charts for the selected product, service or workload. Each chart shows health metrics during the selected time period.

Charts also display relevant events. There are several [event types](https://docs.cloud.google.com/monitoring/dashboards/event-types):

       * Cloud Monitoring alert events.
       * Service Health events.
       * Product-specific events

By default, charts show _recommended events_ , but you can select the events you want to view by using the **Annotations** selector at the top of the page. To learn more about showing and hiding events on a chart, see [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

You can interact with the charts the same way you interact with other Monitoring charts. [Learn about exploring chart data](https://docs.cloud.google.com/monitoring/charts/working-with-charts).

     * To view open alerts for a product, service, or workload, click the link in the **Alerts** column.

     * To view Google Cloud relevant incidents for a product, service, or workload, click the link in the **Google Cloud Incidents** column.

     * To review additional details for a product in the project view, click **View details**. Each product provides additional observability data, logs, and other information to help you diagnose and troubleshoot issues.

     * To open details for an application workload or service in Monitoring, click **View dashboard**. The **Application monitoring** page displays the dashboard for the workload or service.




## Troubleshoot with Gemini Cloud Assist

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) are a root-cause analysis (RCA) tool for troubleshooting your Google Cloud infrastructure and applications. Investigations can help you to diagnose and resolve issues more quickly.

In Cloud Hub, you can view your recent investigations or open a new investigation.

**Note:** As of April 10, 2026, creating, running, and editing investigations are only available to users with a Premium Support contract or who have requested access through their account team.

To create or view investigations, do the following:

  1. In the Google Cloud console, go to the **Health & troubleshooting** page:

[Go to Health & troubleshooting](https://console.cloud.google.com/cloud-hub/health-and-troubleshooting)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

The **Recent Cloud Assist Investigations** section displays recent investigations that you created or have access to view.

     * To create an investigation, click **Investigate**. On the **Create new investigation** page, follow the instructions to [create an investigation](https://docs.cloud.google.com/cloud-assist/create-investigation#create).

     * To view details for a recent investigation, click the name of the investigation. You can then [review the investigation](https://docs.cloud.google.com/cloud-assist/create-investigation#review).

     * To see all investigations that you have access to view, click **View all**.




## What's next

  * Learn more about [Monitoring alerts](https://docs.cloud.google.com/monitoring/alerts).
  * Learn more about [Service Health](https://docs.cloud.google.com/service-health/docs/overview) and Google Cloud incidents.
  * Learn about [Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards).
  * Learn about [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
