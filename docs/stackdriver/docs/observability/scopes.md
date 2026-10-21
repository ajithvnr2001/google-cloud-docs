---
url: https://docs.cloud.google.com/stackdriver/docs/observability/scopes/
title: Configure observability scopes for multi-project queries \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:17.863066+00:00
---

# Configure observability scopes for multi-project queries  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/scopes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Configure observability scopes for multi-project queries Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can create charts or view log data when that data is stored in multiple projects. By default, only the data that originates in a project is available to the visualization tools. However, if you configure a scope, then visualization and analysis tools can query data that is stored in multiple projects.

If you only want to monitor or view data that is stored in one Google Cloud project, then you don't need to perform any configuration.

## Scopes provide read-time aggregation

Scopes let visualization and analysis tools perform read-time aggregation of data that is stored in multiple locations. Scopes don't control where data is stored. Instead, query engines rely on scopes to determine where to search for data.

Metric and trace data is always stored in the Google Cloud project where the data originates. To view metric data that is stored in multiple projects on a single chart, configure a metrics scope to list those projects. After you configure this scope, when you create a chart or alerting policy, the query issued by these services automatically returns metric data from the listed projects. The behavior is similar for trace data.

By default, log data is stored in the Google Cloud project, billing account, folder, or organization where the data originates. However, you can configure Logging to route log data from the resource where it originates to another location, like another project or a centralized log bucket. In all cases, configure a custom log scope. We recommend that your log scope lists [log views](https://docs.cloud.google.com/logging/docs/logs-views) instead of projects; a _log view_ provides read-access to a subset of log entries in a log bucket. For example, if you have log data stored in three projects, then you might configure the log view to include the `_Default/_AllLogs` view for each of those projects.

## How scopes are used by Google Cloud Observability

Google Cloud Observability analysis and visualization tools rely on data-type specific scopes to determine what resources to query for the data that the tool is to display or analyze.

Examples:

  * When the **Logs Explorer** page opens, the system queries the resources listed in the default log scope for log data. After this page is open, you can use a toolbar option to query the resources in a different scope.
  * When the **Trace Explorer** page opens, the system queries the projects listed in the default trace scope for trace data. After this page is open, you can use a toolbar option to query the resources in a different scope.
  * When you create an alerting policy, Monitoring queries the projects listed in the metrics scope for metric data. It then analyzes the query response and determines whether to create an alert.
  * When you create a chart by using the **Metrics Explorer** page, you specify a metric to chart. Monitoring queries the projects listed in the metrics scope for metric data, and then displays the query results.



Logging and Trace verify your Identity and Access Management (IAM) roles on a resource before a query returns data. For example, if a log scope specifies a project for which you haven't been given the permissions to read log data, then a query to that project doesn't return data.

Monitoring verifies your IAM role on the project from which the query is issued. Suppose the metrics scope for a project named `AllEnv` lists the following projects: `AllEnv`, `Prod`, and `Staging`. Also, assume that you've been granted the Monitoring Viewer role on the `AllEnv` project. Charts you create with the **Metrics Explorer** page when using the `AllEnv` project automatically display metric data for the three projects.

## Google Cloud Observability scopes

This section describes the scopes used by Google Cloud Observability.

### Observability scope

The observability scope specifies the default log scope and the default trace scope. Pages like the **Logs Explorer** and **Trace Explorer** use the default scopes to determine what resources to query, when the page opens. For example, suppose you have an application that generates trace data in three projects. You can configure the **Trace Explorer** page to automatically query those three projects by setting the default trace scope.

If you don't configure the observability scope, then the following occur:

  * The **Logs Explorer** page queries your project for log data.
  * The **Trace Explorer** page queries your project for trace data.



The observability scope doesn't apply to metric data.

#### When to configure the observability scope

Configure the observability scope in the following scenarios:

  * You create a custom log scope and you want the resources listed in that scope queried by default.

  * You create a custom trace scope and you want the projects listed in that scope queried by default.




#### Limits associated with observability scopes

Description | Maximum value  
---|---  
Number of observability scopes per project | 1  
  
### Log scopes

Log scopes are used by the **Logs Explorer** page and by dashboards that display log data:

  * When the **Logs Explorer** page opens, the system automatically queries the resources listed in the default log scope for log data. This page also provides controls that let you switch between scopes.

  * For dashboards, the implementation determines whether the system queries the project or the resources listed in the default log scope.




A log scope can list [log views](https://docs.cloud.google.com/logging/docs/logs-views), projects, folders, and organizations.

If you don't configure a custom log scope, then the **Logs Explorer** page queries your project for log data.

#### When to create custom log scopes

Create custom log scopes for the following configurations:

  * You route log data to a [centralized log bucket](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview).
  * You store log data in multiple projects.
  * You are using [Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring), which is a service that generates dashboards for your [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications.



In all cases, configure your custom log scopes to list one or more log views. Those log views might be on a centralized log bucket, or they might be log views on different log buckets. If you use a centralized log bucket, then you might create multiple custom log scopes, each with their own set of log views.

If you create a custom log scopes, then consider updating the default log scope.

#### Best practices when configuring log scopes

  * Include only log views.
  * Don't configure a scope that lists both projects and log views.



#### Limits associated with log scopes

Description | Maximum value  
---|---  
Number of log scopes per project | 100  
Number of projects per log scope | 5  
Number of log views or projects per log scope | 100  
  
For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

### Metrics scope

The metrics scope is used by all queries issued by Cloud Monitoring. For example, alerting policies and charting tools like the Metrics Explorer issue queries to the projects listed in the metrics scope.

If you don't configure the metrics scope, then Monitoring services query your project for metric data.

#### When to configure the metrics scopes

Configure the metrics scope when any of the following are true:

  * You want to chart data stored in different projects.
  * You want an alerting policy to monitor data stored in different projects.
  * You register applications with [App Hub](https://docs.cloud.google.com/app-hub/docs/overview). For information about this scenario, see [App Hub applications and metrics scopes](https://docs.cloud.google.com/monitoring/settings#mgmt-project-scopes).



#### Limits associated with metrics scopes

Description | Maximum value  
---|---  
Number of metrics scopes per project | 1  
Number of projects per metrics scopes | 375  
  
For more information, see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).

### Trace scopes

The **Trace Explorer** page uses Trace scopes. When this page opens, the system automatically queries the views listed in the default trace scope for trace data. This page also provides controls that let you switch between scopes.

If you don't configure a custom trace scope, then the **Trace Explorer** page queries the project's `_AllSpans` view on the default dataset for your trace data.

A trace scope lists views, not Google Cloud projects. Although you select projects when you configure a trace scope, the system adds to the scope those projects' default trace view. A project's _default trace view_ corresponds to the view with the path `_Trace/Spans/_AllSpans`, where the fields `_Trace`, `Spans`, and `_AllSpans` refer to an observability bucket, dataset, and view. The dataset `Spans` stores your trace data.

#### When to create custom trace scopes

Create custom trace scopes when you have applications that rely on resources in different Google Cloud projects.

#### Best practices when configuring trace scopes

**Warning:** Make sure that all projects listed in a trace scope store their trace data in the same location. Your trace data is stored in an observability bucket named `_Trace`. To learn how to display the location where your trace data is stored, see [List observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage#list-buckets).

#### Limits associated with trace scopes

Description | Maximum value  
---|---  
Number of trace scopes per project | 100  
Number of views per trace scope | 20  
  
For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

## Configure the observability scope

This section doesn't apply to folders or organizations.

For log and trace data, your Identity and Access Management (IAM) roles on the project you are viewing, and any searched projects and log views, affect what data is returned by the query. If you issue a query to view log data that you don't have permission to view, then the query doesn't return any log data.

For metric data, when a project's metrics scope is configured, the project is granted read-access to the metric data stored by the projects listed in its metrics scope. When a user is granted an Identity and Access Management role that lets them view metric data in a project, they can view metric data available to the project.

To configure the observability scope, you set the default log scope and the default trace scope. The remainder of this section describes how to complete these actions.

### Before you begin

Configure your project, your IAM roles, and select the interface that you plan to use.

#### Configure your project and roles

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  8. To get the permissions that you need to create and view scopes, ask your administrator to grant you the following IAM roles: 

     * To create and view log scopes and to get the default log scope: [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`) on your project 
     * To modify a metrics scope: [Monitoring Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.admin) (`roles/monitoring.admin`) on your project and on each project you want to add to the metrics scope 
     * To create and view trace scopes, and to get and set default scopes: [Observability Scopes Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`) on your project 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and view scopes. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and view scopes:

     * `logging.logScopes.{create, delete, get, list, update}`
     * `monitoring.metricsscopes.{link, get, list}`
     * `observability.traceScopes.{create, delete, get, list, update}`
     * `observability.scopes.{get, update}`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Select the interface you plan to use

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### View and set the default scope

###  Console 

To configure the observability scope, you configure its components, which are the default log scope, the metrics scope, and the default trace scope:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Configure the default log scope:

     1. Select the **Log Scopes** tab.

Existing log scopes are listed. The entry with the "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png), is the default log scope. If you want to create a log scope, click **Create log scope** and then complete the dialog. For more information, see [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).

     2. Find the entry that you want to designate as the default, click _more_vert_ **More** , and then select **Set as default**.

  4. Configure the metrics scope:

     1. Select the **Metrics scope** tab.
     2. In the **Google Cloud Projects** pane, click **Add Projects** , and then complete the dialog. For more information, see [Configure metrics scopes](https://docs.cloud.google.com/monitoring/settings/multiple-projects).
  5. Configure the default trace scope:

     1. Select the **Trace Scopes** tab and then do the following:

Existing trace scopes are listed. The entry with the "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png), is the default trace scope. If you want to create a trace scope, click **Create log scope** and then complete the dialog. For more information, see [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).

     2. Find the entry that you want to designate as the default, click _more_vert_ **More** , and then select **Set as default**.




###  gcloud 

To view and update the observability scope, do the following:

  1. To view the settings for the observability scope, run the `gcloud observability scopes describe` command.

Before using any of the command data below, make the following replacements: 

     * OBSERVABILITY_SCOPE_ID: The name of a `Scope` object. This value must be set to `_Default`.
     * LOCATION: The location field must be set to `global`.
     * PROJECT_ID: The identifier of the project.

Execute the [`gcloud observability scopes describe`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/scopes/describe) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud observability scopes describe OBSERVABILITY_SCOPE_ID \
       --location=LOCATION\
       --project=PROJECT_ID

#### Windows (PowerShell)
    
    gcloud observability scopes describe OBSERVABILITY_SCOPE_ID `
       --location=LOCATION`
       --project=PROJECT_ID

#### Windows (cmd.exe)
    
    gcloud observability scopes describe OBSERVABILITY_SCOPE_ID ^
       --location=LOCATION^
       --project=PROJECT_ID

The response to the command is similar to the following: 
    
    logScope: logging.googleapis.com/projects/my-project/locations/global/logScopes/_Default
    traceScope: projects/my-project/locations/global/traceScopes/_Default
    name: projects/my-project/locations/global/scopes/_Default
    

  2. To update the observability scope, run the `gcloud observability scopes update` command. In the `update` command, you can include the `--log-scope` flag, the `--trace-scope` flag, or both flags.

Before using any of the command data below, make the following replacements: 

     * OBSERVABILITY_SCOPE_ID: The name of a `Scope` object. This value must be set to `_Default`.
     * LOG_SCOPE_FQN_ID: The fully-qualified resource name of the log scope. This field has the following format: 
           
           logging.googleapis.com/projects/PROJECT_ID/locations/LOCATION/logScopes/LOG_SCOPE_ID

In the previous expression, LOG_SCOPE_ID is the ID of the log scope. For example, `my-scope`.

     * TRACE_SCOPE_FQN_ID: The fully-qualified resource name of the trace scope. This field has the following format: 
           
           projects/PROJECT_ID/locations/LOCATION/traceScopes/TRACE_SCOPE_NAME

In the previous expression, TRACE_SCOPE_NAME is the name of the trace scope. For example, `my-trace-scope`.

     * LOCATION: The location field must be set to `global`.
     * PROJECT_ID: The identifier of the project.

Execute the [`gcloud observability scopes update`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/scopes/update) command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud observability scopes update OBSERVABILITY_SCOPE_ID \
       --log-scope=LOG_SCOPE_FQN_ID\
       --trace-scope=TRACE_SCOPE_FQN_ID\
       --location=LOCATION\
       --project=PROJECT_ID

#### Windows (PowerShell)
    
    gcloud observability scopes update OBSERVABILITY_SCOPE_ID `
       --log-scope=LOG_SCOPE_FQN_ID`
       --trace-scope=TRACE_SCOPE_FQN_ID`
       --location=LOCATION`
       --project=PROJECT_ID

#### Windows (cmd.exe)
    
    gcloud observability scopes update OBSERVABILITY_SCOPE_ID ^
       --log-scope=LOG_SCOPE_FQN_ID^
       --trace-scope=TRACE_SCOPE_FQN_ID^
       --location=LOCATION^
       --project=PROJECT_ID

For example, if the value of the LOG_SCOPE_ID is `my-log-scope`, and the value of TRACE_SCOPE_NAME is `my-trace-scope`, then the response is similar to the following: 
    
    Updated scope [_Default].
    logScope: logging.googleapis.com/projects/my-project/locations/global/logScopes/my-log-scope
    traceScope: projects/my-project/locations/global/traceScopes/my-trace-scope
    name: projects/my-project/locations/global/scopes/_Default
    




###  REST 

To get and set the default log scope or the default trace scope by using an API call, you configure the observability scope. The observability scope lists the default log scope and the default trace scope:

  * To get the default observability scope for a project, send a request to the [`projects.locations.scopes.get`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.scopes/get) endpoint. You must specify a path parameter. The response is a [`Scope`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.scopes#Scope) object, which lists the default log scope and the default trace scope.
  * To update the default observability scope for a project, send a request to the [`projects.locations.scopes.patch`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.scopes/patch) endpoint. You must specify a path parameter, query parameters, and provide a [`Scope`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.scopes#Scope) object. The query parameters identify which fields are changed. The response is a `Scope` object.



The path parameter for both endpoints has the following form:
    
    
    projects/PROJECT_ID/locations/LOCATION/scopes/OBSERVABILITY_SCOPE_ID
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION: The location field must be set to `global`.
  * OBSERVABILITY_SCOPE_ID: The name of a `Scope` object. This field must be set to `_Default`. The `Scope` object with the name `_Default`, which is created automatically, stores information about the default log scope and the default trace scope.



To send a command to an API endpoint, you can use the APIs Explorer, which lets you issue a command from a reference page. For example, to get the current default scope, you can do the following:

  1. Click [`projects.locations.scopes.get`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.scopes/get).
  2. In the **Try this method** widget, enter the following in the **name** field: 
         
         projects/PROJECT_ID/locations/global/scopes/_Default
             

Before you copy the previous field, replace PROJECT_ID with the name of your project.

  3. Select **Execute**.
  4. In the authorization dialog, complete the required steps. 

The response is similar to the following:
         
         {
             "name": "projects/my-project/locations/global/scopes/_Default",
             "logScope": "logging.googleapis.com/projects/my-project/locations/global/logScopes/_Default"
             "traceScope": "projects/my-project/locations/global/traceScopes/_Default"
             }
             




## Learn more about scopes

For more information about scopes, see the following documents:

  * [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage).
  * [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings).
  * [Create and manage trace scopes](https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
