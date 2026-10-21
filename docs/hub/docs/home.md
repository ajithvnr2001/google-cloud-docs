---
url: https://docs.cloud.google.com/hub/docs/home/
title: View top items on the Home page \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:22:06.387712+00:00
---

# View top items on the Home page  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/home/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  View top items on the Home page Stay organized with collections  Save and categorize content based on your preferences. 

The Home page of Cloud Hub lets you view key information about your Google Cloud resources and [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications on a single page. From the Home page you can explore details on other pages in Cloud Hub or on the pages of the Google Cloud services that provide the data.

The types of information that appear on the Home page depend on whether you selected a project or an application. The following example shows Home page information for an application.

![ ](https://docs.cloud.google.com/static/hub/images/home.png)

## Before you begin

To view data for App Hub applications, ensure that the following steps are complete:

  1. [Set up App Hub for a folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) and create your applications.

  2. [Set up aggregation of logs, metrics, and traces](https://docs.cloud.google.com/stackdriver/docs/observability/setup-application-monitoring) for your applications.




To use investigations, [set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).

**Note:** Cloud Hub doesn't support applications in a [host project](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

### Required roles

To get the permissions that you need to view data in Cloud Hub, ask your administrator to grant you the following IAM roles on the project ([project view](https://docs.cloud.google.com/hub/docs/app-project-views#project-view)) or management project for a folder ([application view](https://docs.cloud.google.com/hub/docs/app-project-views#app-view)): 

  * View most application and project data: [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) 
  * Use Gemini Cloud Assist: [Gemini Cloud Assist User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.user) (`roles/geminicloudassist.user`) 
  * Create and view investigations: [Investigations Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationCreator) (`roles/geminicloudassist.investigationCreator`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Open the Home page

  1. In the Google Cloud console, go to the Home page:

[Go to Home](https://console.cloud.google.com/cloud-hub/home)

  2. Select the [project or application](https://docs.cloud.google.com/hub/docs/app-project-views) that you want to view:

     * To view data for applications, choose the folder that is configured for application management. Folders configured for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for the folder also has a special icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)) and the project name is in the format `FOLDER-NAME-mp`. If you choose the management project instead of the folder, then the project picker automatically changes the selection to the folder.

     * To view data for an individual project, choose the project that contains the resources you want to view.

  3. If you selected an app-enabled folder, select the application that you want to view data for.




The following table describes each information card and indicates if the data is visible for project resources, applications, or both.

Card | Description | Applications | Project resources | Open alerts | This card displays the total number of open alerts for alert policies that are configured in Cloud Monitoring. To view your open alerts in Cloud Monitoring, click **View alerts**. [Learn about alerts in Monitoring](https://docs.cloud.google.com/monitoring/alerts). You can also view summary information for open alerts on the [Health & troubleshooting page](https://docs.cloud.google.com/hub/docs/health). | Yes | Yes  
---|---|---|---  
Google Cloud incidents | This card displays the total number of Google Cloud outages and degradations that affect the selected project or application. To view incident details in Personalized Service Health, click **View incidents**. [ Learn about viewing incidents](https://docs.cloud.google.com/service-health/docs/view-events#view-service-health-incidents). You can also view summary information for open incidents on the [Health & troubleshooting page](https://docs.cloud.google.com/hub/docs/health). | Yes | Yes  
Cost summary | This card displays the gross cost and cost change in the last 7 days. Costs are based on your contract prices, before any [committed-use discounts (CUDs)](https://docs.cloud.google.com/docs/cuds) or other credits are applied. For an application, costs include all resources that are fully used by the application and don't include costs for resources that are shared across applications. To view details, click **View Optimization board**. [Learn about viewing cost optimization data](https://docs.cloud.google.com/hub/docs/optimize). | Yes | Yes  
My recent investigations | This card displays the status of your Gemini Cloud Assist [investigations][gca-investigate]. To create a new investigation, click **Investigate**. To view more information, click **View Health & Troubleshooting board**. [Learn about viewing investigations in Cloud Hub](https://docs.cloud.google.com/hub/docs/health#gemini). | Yes | Yes  
Security & compliance | This card displays Security Command Center data related to your **Top findings** and **Frameworks requiring attention**. To view more information, click **View Security & compliance board**. [Learn about assessing your security and compliance status](https://docs.cloud.google.com/hub/docs/security).  | Yes | Yes  
Top queries ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) | This card suggests App Topology queries that you can run to correlate data. You can customize queries to meet your needs and view the query results in a topology graph. [Learn about viewing topology graphs](https://docs.cloud.google.com/hub/docs/app-topology).  | Yes | Yes  
ADC application infrastructure deployment notifications | This card lists issues with Application Design Center deployments for applications in the selected folder. To view details for a deployment, click the application name. To view the list of deployments on the Deployments page, click **View Deployments board**. [Learn about viewing deployment issues](https://docs.cloud.google.com/hub/docs/deployments). | Yes | No  
Maintenance summary | This card displays the total number of scheduled, running, succeeded and canceled maintenance activities. To view maintenance details, click **View maintenance board**. [Learn about viewing maintenance](https://docs.cloud.google.com/hub/docs/maintenance). | Yes | Yes  
Quotas & System Limits at risk | This card displays quotas and system limits with over 90% usage in the selected project. To view a quota or system limit, click its name in the list. To view all quotas and system limits with over 90% usage, click **View all at risk**. [ Learn about viewing quotas and system limits](https://docs.cloud.google.com/hub/docs/quotas-reservations). | No | Yes  
All recommendations | This card displays recommendations from Active Assist for resources in the selected project. To view details about the recommendations in [ Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist), click **View all recommendations**.  | No | Yes  
Technical cases information | This card displays open support cases and cases that need input. To view details, click **View support board**. [Learn about viewing support information](https://docs.cloud.google.com/hub/docs/support). | No | Yes  
Folder info | This card displays information about the selected folder and the associated management project, including the folder name, folder ID, folder type, management project name, and management project ID. | Yes | No  
Project info | This card displays information about the selected Google Cloud project, including the project name, project number, and project ID. | No | Yes  
News | This card displays recent Google Cloud news. For more news, click **Read all news**. To view Google Cloud release notes, click **Read all release notes**. | No | Yes  
Getting started with Google Cloud | This card displays links to tutorials to help you get started with Google Cloud. To view more tutorials, click **View all tutorials**. | No | Yes  
  
## What's next

  * [Learn about application and project views](https://docs.cloud.google.com/hub/docs/app-project-views).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
