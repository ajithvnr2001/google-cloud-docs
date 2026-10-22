---
url: https://docs.cloud.google.com/hub/docs/setup-cloud-hub/
title: Set up Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:25.617137+00:00
---

# Set up Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/setup-cloud-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  Set up Cloud Hub Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Hub aggregates data across Google Cloud so that you can view the data in centralized dashboards in the Google Cloud console. To start using Cloud Hub, you must set up Google Cloud services that provide data to Cloud Hub.

## Overview

The setup process includes the following main tasks:

  1. To create App Hub applications and view data about them in Cloud Hub, set up application management.

If you don't set up application management, you can still view some data by Google Cloud project instead of by application in Cloud Hub. 

  2. Enable APIs for project data. Some pages in Cloud Hub don't support application data. You must enable APIs for these pages separately.

  3. Configure aggregated views of logs, metrics, and traces.

  4. Grant access to Cloud Hub users.




Different people or teams might be responsible for different steps in the Cloud Hub setup process.

## Set up application management

This section describes the steps required to enable application management and create your applications.

### Required roles

To get the permissions that you need to configure an app-enabled folder, ask your administrator to grant you the following IAM roles: 

  * Enable application management: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) on the parent resource for the folder 
  * Enable APIs: [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`) on the target folder (to enable required and recommended APIs) 
  * Link a billing account to the management project: 
    * [Project Billing Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.projectManager) (`roles/billing.projectManager`) on the management project
    * [Billing Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.user) (`roles/billing.user`) on the target billing account
  * Grant application-centric roles to users: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the management project 
  * Configure the observability scope: 
    * [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`) on the management project
    * [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) on the management project
    * [Monitoring Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.admin) (`roles/monitoring.admin`) on the management project and on each project that you want to add to the metrics scope
    * [Cloud Trace User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`) on the management project
    * [App Hub Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.viewer) (`roles/apphub.viewer`) on the management project
  * View application-level and project-level data in Cloud Hub: [Cloud Hub Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`) on the app-enabled folder 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable application management

Application management lets you shift your focus from individual infrastructure components to your application as a whole.

When you enable application management on a folder, the folder is called app-enabled folder and the following occurs:

  * A project is defined as the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) in the folder.
  * The system enables required APIs on the management project.
  * The management project stores application data, including enabled APIs, billing, quotas, and access controls.



To enable application management on a folder, do the following:

###  Console 

  1. Select or create the Google Cloud folder that you want to configure as an app-enabled folder. To create a new folder, see [Creating folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#creating-folders).

  2. In the Google Cloud console, open the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  3. From the list of projects and folders, locate the folder that you want to configure.

If a folder has the ![](https://docs.cloud.google.com/static/app-hub/images/app-folder.png) app-enabled folder icon, application management is already enabled.

  4. In the folder row, open the more_vert **Actions** menu and click **Settings**.

If application management has not been enabled on the folder, the **Application management** setting displays _Not enabled_.

  5. In the **Enable application management** area, click **Create project**.

The **Create management project and enable required APIs** panel opens.

  6. Review the list of [required APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis). These APIs manage your application lifecycle. For APIs that have associated costs, click the API name to learn more about pricing.

  7. To enable application management, click **Create project and enable APIs**.

The system creates the management project in the folder.

**Warning:** If API enablement fails, you must restart the application management enablement process. The error is displayed in notifications_none **Notifications**.
  8. Make note of the project name and ID of the management project. You'll use these values to grant access.

Alternatively, to get the management project ID, you can use the following Google Cloud CLI command:
         
         gcloud resource-manager folders describe FOLDER_ID
             --format="value(managementProject.split('/').slice(-1))"
         

Replace `FOLDER_ID` with the ID of the app-enabled folder.

For more information, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that the most recent version of Google Cloud CLI is installed:
         
         gcloud components update
         

  3. To enable application management on a specific folder, use the `gcloud resource-manager capabilities update` command with the `--enable` flag.
         
         gcloud resource-manager capabilities update folders/FOLDER_ID/capabilities/app-management \
            --enable
         

Replace `FOLDER_ID` with the ID of the folder.

This command enables the application management capability on the specified folder and automatically provisions a new Google Cloud project within that folder to serve as the management project.

  4. Optionally, to enable [recommended APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis) on the management project, follow the instructions to [enable Google Cloud services on a project](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable).




###  Terraform 

To enable application management on a folder using Terraform, use [the `google_resource_manager_capability` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/resource_manager_capability), for example:
    
    
    resource "google_folder" "folder" {
      display_name     = "my-folder"
      parent           = "organizations/123456789"
      deletion_protection = false
    }
    resource "time_sleep" "wait_60s" {
      depends_on = [google_folder.folder]
      create_duration = "60s"
    }
    resource "google_resource_manager_capability" "capability" {
      value            = true
      parent           = "${google_folder.folder.name}"
      capability_name  = "app-management"
      depends_on = [time_sleep.wait_60s]
    }
    

This command enables the application management capability on the specified folder and automatically provisions a new Google Cloud project within that folder to serve as the management project. To enable the list of [recommended APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis) on the management project, follow the instructions to [enable an API service on a Google Cloud project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service).

**Important:** When you create an app-enabled folder, it is important to understand the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) in the folder. If a descendant project or subfolder that contains services and workloads is moved out of an app-enabled folder after an application is created, the application remains in the app-enabled folder. However, the [registration status of services and workloads](https://docs.cloud.google.com/app-hub/docs/overview#registration-status) changes to _detached_.

### Link a billing account to the management project

To use advanced Application-centric Google Cloud features, you must link an active billing account to the management project. For example, a linked billing account helps you do the following:

  * Manage workloads that exceed App Hub resource quotas.
  * Use Application Design Center to create templates and deploy applications.



For an overview of potential costs associated with application management and the enabled APIs, see [Understanding costs](https://docs.cloud.google.com/app-hub/docs/enabled-apis#costs).

**Note:** If you don't link a billing account, you can still use App Hub and Application Monitoring. You can model your applications with underlying services and workloads at no cost and use the [free data usage allotments](https://docs.cloud.google.com/stackdriver/pricing) for Google Cloud Observability usage in the management project.

Follow these steps to link an active billing account to your management project:

###  Console 

  1. Verify the billing account that you want to use for application management exists. To create a billing account, see [Create a new self-serve Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account).

  2. In the Google Cloud console, open the **Billing** page.

[Go to Billing](https://console.cloud.google.com/billing)

  3. In the **My projects** tab, locate the management project.

  4. In the project row, open the more_vert **Actions** menu, select **Change billing** , and then choose the Cloud Billing account.




For more information about enabling billing for a project, see [Enabling billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).

###  gcloud 
    
    
    gcloud billing projects link PROJECT_ID \
        --billing-account ACCOUNT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the management project.
  * `ACCOUNT_ID`: the ID of the billing account. Billing account IDs are in the format `0X0X0X-0X0X0X-0X0X0X`.



### Configure observability scopes

The [observability scope](https://docs.cloud.google.com/stackdriver/docs/observability/scopes#about-obs-scope) determines where the Google Cloud console searches for telemetry data to display. Each Google Cloud project has a single observability scope, which identifies the default log and trace scopes. For metric data, the project's metrics scope determines where the Google Cloud console searches for data.

To view or analyze all of your application's telemetry data, configure the observability scope and the metrics scope for the management project. By configuring these scopes, Cloud Hub and other services can find and display your application's log, metric, and trace data, even when that data is stored in multiple projects.

This section summarizes the required configuration. For detailed instructions, see [Set up application monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/setup-application-monitoring). The following table shows the required configuration scopes.

Scope component | Configuration scenario | Key actions and considerations  
---|---|---  
**Log scope** | You use an [ aggregated sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview) to route all logs in the organization to a central log bucket. | 

  1. Create a log view that only includes application logs stored in the bucket.
  2. Configure the default log scope on the management project to include the log view.

  
You don't have an organization-level aggregated sink, and the app-enabled folder doesn't have nested folders. | 

  1. Configure an aggregated sink to route application logs to the `_Default` log bucket of the management project.
  2. Make sure that the log scope named `_Default` is the default log scope.

  
You don't want to use an aggregated sink. | Configure the default log scope on the management project to list the storage locations of your application's log data.  
**Metrics scope** | You configured an app-enabled folder containing all the projects that store the metric data you want to view. | Google Cloud Observability attempts to synchronize the list of projects in your app-enabled folder with the list of projects on the scope of the metrics.  
  
As long as the number of projects in the app-enabled folder doesn't exceed your metric scope quota, Google Cloud Observability can keep the list of projects on the scope of the metrics updated when you add or remove projects in the app-enabled folder.  
**Trace scope** | You want to monitor application trace data across multiple projects. | 

  1. Create a custom trace scope on the management project that lists the projects that store your application's trace data.
  2. Set your custom trace scope as the default trace scope.

  
  
### Create applications

After you have enabled application management, you can create your applications. You have the following options to create your applications:

  * Use [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) to create applications from existing Google Cloud resources. See [Create an application from existing resources](https://docs.cloud.google.com/app-hub/docs/quickstart-create-application).
  * Use [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) to design and deploy new Google Cloud resources, which automatically provision App Hub applications. You use _application templates_ to define the design and then deploy _application instances_ based on the templates.



## Enable APIs for Cloud Hub

Cloud Hub does not have its own API. Instead, it calls other APIs that provide data to Cloud Hub.

The following table lists APIs that Cloud Hub uses. Some of these APIs have associated costs or have dependencies with costs. Review the pricing links for more information.

API | Usage in Cloud Hub | Pricing  
---|---|---  
App Hub API  
(`apphub.googleapis.com`) Stores metadata for all registered applications. Lets you organize existing resources into applications.  | Required to display application data in Cloud Hub. [Learn about App Hub.](https://docs.cloud.google.com/app-hub/docs) | [App Hub pricing](https://cloud.google.com/app-hub/pricing)  
App Topology API  
(`apptopology.googleapis.com`) View visualizations of relationships between application resources. | Required to view App Topology visualizations.  |   
App Design Center API  
(`designcenter.googleapis.com`) Design, deploy, and update applications | Required to [view application deployments](https://docs.cloud.google.com/hub/docs/deployments) in Cloud Hub. | [Pricing](https://cloud.google.com/products/application-design-center/pricing)  
App Optimize API  
(`appoptimize.googleapis.com`) Get cost and utilization data to help you optimize costs. | Required for viewing data on the [Optimization page](https://docs.cloud.google.com/hub/docs/optimize) in Cloud Hub.  | The are no additional charges for this API. The API retrieves data from [Cloud Billing](https://cloud.google.com/billing/v1/pricing) and [Cloud Monitoring ](https://cloud.google.com/stackdriver/pricing)  
Capacity Planner API  
(`capacityplanner.googleapis.com`) View usage and forecast data to help plan capacity needs. | Required to [view usage and forecast data](https://docs.cloud.google.com/hub/docs/quotas-reservations#view-usage) in Cloud Hub. | [ Capacity Planner pricing](https://docs.cloud.google.com/capacity-planner/docs/overview#pricing)  
Compute Engine API  
(`compute.googleapis.com`) Provision self-managed virtual machine (VM) instances and bare metal instances. | Required to [view reservation data ](https://docs.cloud.google.com/hub/docs/quotas-reservations#reservations) in Cloud Hub. | [ Billing information for future reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#billing)  
Cloud Logging API  
(`logging.googleapis.com`) Real-time log-management. | Provides logging for Google Cloud services. Required for the [Health & Troubleshooting page](https://docs.cloud.google.com/hub/docs/health) in Cloud Hub.  | [ Observability pricing](https://cloud.google.com/stackdriver/pricing)  
Cloud Monitoring API  
(`monitoring.googleapis.com`) | Provides metrics and alerting for Google Cloud services. Required for alert and telemetry data on the [Health & Troubleshooting page](https://docs.cloud.google.com/hub/docs/health) in Cloud Hub.  | [ Observability pricing](https://cloud.google.com/stackdriver/pricing)  
Service Health API  
(`servicehealth.googleapis.com`) Identify Google Cloud service disruptions relevant to your applications | Required to view Google Cloud incidents on the [Health & Troubleshooting](https://docs.cloud.google.com/hub/docs/health) and [Support](https://docs.cloud.google.com/hub/docs/support) pages in Cloud Hub.  | [ Personalized Service Health pricing](https://cloud.google.com/service-health#pricing)  
Recommender API  
(`recommender.googleapis.com`) Generate Active Assist recommendations and insights to help you optimize your Google Cloud resources | Required to view [ cost optimization recommendations](https://docs.cloud.google.com/hub/docs/optimize#recommendations) in Cloud Hub  | [ Recommender pricing](https://cloud.google.com/recommender/pricing)  
Gemini Cloud Assist API  
(`geminicloudassist.googleapis.com`) A product of the [ Gemini for Google Cloud](https://cloud.google.com/products/gemini) portfolio that offers AI-powered assistance to simplify the application lifecycle in Google Cloud.  | Required use Gemini Cloud Assist for assistance with tasks such as [cost optimization](https://docs.cloud.google.com/hub/docs/optimize-gemini) and [troubleshooting](https://docs.cloud.google.com/hub/docs/health#gemini).  | [ Gemini Cloud Assist pricing](https://cloud.google.com/products/gemini/pricing#gemini-cloud-assist-pricing)  
Cloud Quotas API  
(`cloudquotas.googleapis.com`) View and manage quotas. | Required to [view quotas and system limits](https://docs.cloud.google.com/hub/docs/quotas-reservations#view-quotas) in Cloud Hub. | [ Cloud Quotas pricing](https://cloud.google.com/quotas/pricing)  
Unified Maintenance API  
(`maintenance.googleapis.com`) Manage planned maintenance across Google Cloud services. | Required to [view maintennance acitivities](https://docs.cloud.google.com/unified-maintenance/docs) in Cloud Hub | [ Unified Maintenance pricing](https://cloud.google.com/products/unified-maintenance/pricing)  
Service Usage API  
(`serviceusage.googleapis.com`) List and manage APIs and services in your Google Cloud projects.  | Required to [view quotas and system limits](https://docs.cloud.google.com/hub/docs/quotas-reservations#view-quotas) in Cloud Hub. | [Service Usage pricing](https://docs.cloud.google.com/service-usage/pricing)  
  
After you set up application management, many of the APIs that provide data to Cloud Hub are enabled on the management project as [required APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis#apis).

However, some APIs that Cloud Hub uses only provide data for projects or are not automatically enabled as required APIs on a management project.

Use the instructions in this section to enable missing APIs for Cloud Hub.

  * If you set up an app-enabled folder, enable the APIs on the folder's management project.
  * To view data for a single project, enable APIs on that project.
  * For the Maintenance page: If your projects aren't in an app-enabled folder, configure a project to aggregate logs from the other projects, and then enable the Unified Maintenance API on that project.

    * [Route logs](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) using an aggregated sink to a single project.
    * [Configure the default log scope](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage) on a project so that it can view logs that are stored in other projects or in a centralized log storage bucket.



### Required roles

To get the permissions that you need to enable APIs, ask your administrator to grant you the Service Usage Admin (roles/serviceusage.serviceUsageAdmin) IAM role on the project where you want to enable APIs. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

For information about APIs that Cloud Hub uses, see Enable APIs for Cloud Hub.

###  Console 

From the Cloud Hub Home page, you can view a list of APIs that are not enabled for Cloud Hub and enable those APIs.

  1. In the Google Cloud console, go to the **Home** page:

[Go to Home](https://console.cloud.google.com/cloud-hub/home)

  2. From the project picker, select the project that you want to view.

  3. Next to **Enable Recommended APIs** , click **Enable APIs**. A panel opens and displays APIs that are not yet enabled.

  4. Select the APIs that you want to enable, and then click **Enable**.




###  gcloud 

  1. Set the default project to the project where you want to enable the API.
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your project ID.

  2. Get a list of services that you can enable in your project:
         
         gcloud services list --available
         

If you don't see the API listed, that means you haven't been granted access to enable the API.

  3. Enable the services that you want to use in the project. You can enable more than one API by providing a list of service names.
         
         gcloud services enable SERVICE_NAME1 SERVICE_NAME2
         




## Grant access to Cloud Hub users

The [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) role includes permissions for viewing most data in Cloud Hub.

Depending on the specific responsibilities of your users, you might need to grant other roles so that they can use Gemini Cloud Assist features or take action on data that they view in Cloud Hub. For more information, see [Access control with IAM](https://docs.cloud.google.com/hub/docs/access-control).

### Required roles

To get the permissions that you need to manage access to a project or folder, ask your administrator to grant you the following IAM roles on the resource that you want to manage access for (project or folder): 

  * To manage access to a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * To manage access to a folder: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Grant access to users

### Console

  1. Go to the Home page in Cloud Hub.

[Go to Home](https://console.cloud.google.com/cloud-hub/home)

  2. In the project selector, choose the app-enabled folder or project where you want to grant access.

  3. Click **Grant access**. The **Grant access to Cloud Hub** panel opens.

  4. In the **New principals** field, enter a [principal](https://docs.cloud.google.com/iam/docs/principal-identifiers) who requires access to Cloud Hub.

  5. Click **Grant roles**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that the most recent version of Google Cloud CLI is installed. Run the following command from the Cloud Shell:
         
         gcloud components update

  3. To grant the Cloud Hub Operator role, run the appropriate command:

For an app-enabled folder:
         
         gcloud resource-manager folders add-iam-policy-binding FOLDER_ID \
             --member='user:PRINCIPAL' \
             --role='roles/cloudhub.operator'
         

For a single project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member='user:PRINCIPAL' \
             --role='roles/cloudhub.operator'
         

Replace the following variables:

     * `FOLDER_ID`: the ID of the app-enabled folder. In the Google Cloud console, you can find the folder ID on the [**Home**](https://console.cloud.google.com/cloud-hub/home) page in Cloud Hub. The **Folder type** field has the value `App-enabled folder` if the folder is configured for application management.
     * `PROJECT_ID`: the ID of the project. In the Google Cloud console, you can find the project ID on the [**Home**](https://console.cloud.google.com/cloud-hub/home) page in Cloud Hub.
     * `PRINCIPAL`: the identity that you are granting access to.



## What's next

  * View the [Home](https://docs.cloud.google.com/hub/docs/home) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
