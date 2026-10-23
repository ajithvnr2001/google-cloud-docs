---
url: https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage/
title: Create and manage log scopes \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:50.966238+00:00
---

# Create and manage log scopes  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/log-scope/create-and-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Create and manage log scopes Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can create and manage log scopes, which you can use to help you efficiently find the log entries that you want to view or analyze. If you only want to view and analyze the log entries that originate in a project, folder, or organization, then this document isn't for you. However, if you rely on [log sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) to route logs to other projects or to user-defined [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries), or if you use [log views](https://docs.cloud.google.com/logging/docs/logs-views), then the information in this document might help you efficiently find specific log entries.

This document doesn't describe how to view your logs. For information about that topic, see [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

## About log scopes

Log scopes are persistent, project-level resources that list a set of resources. These resources can be projects, folders, organizations, and log views. For example, you could define a log scope that lists the projects that contain resources used for production, or one that lists the log views that include log entries for a specific resource type.

When you create a Google Cloud project, folder, or organization resource, Logging creates a log scope named `_Default`. This scope includes the project, folder, or organization that was created. When a searched resource is a Google Cloud project, folder, or organization, the results include the log entries that originate in the resource and then are stored in a log bucket. The log bucket can be in any project. When a project is searched, the results also include log entries that are routed to the project by a sink in another project and then stored in a log bucket.

You can create log scopes. You can also edit and delete the log scopes that you create. However, you can't edit or delete the log scope named `_Default`.

You use a log scope to control which resources the **Logs Explorer** page searches for log data. When you open that page and select a log scope, the page searches the resources listed in that scope and then refreshes the display.

You can also use a log scope to control which resources a logs panel searches for log data. A _logs panel_ is a custom-dashboard widget that displays log data. Each logs panel has its own configuration, which lets you create a dashboard that contains multiple logs panels where each panel displays different log data. For more information, see [Display logs and errors on a custom dashboard](https://docs.cloud.google.com/monitoring/charts/view-logs).

For projects, the _default log scope_ determines the set of resources that the **Logs Explorer** page searches when it opens. However, your Identity and Access Management (IAM) roles on the searched resources and the time-range setting determine which log entries are fetched from storage. When projects are created, the log scope named `_Default` is designated as the default log scope. You can set which log scope is the default log scope.

### How log scopes differ from centralized log storage

Both centralized log storage and log scopes provide a way for you to view log data that originates in different projects.

When you [centralize your log storage](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks_overview), you configure the sinks in an organization or folder to route log entries to a single storage location. Centralized storage provides a single place to query for log data, which simplifies your queries when you are searching for trends or investigating issues. From a security perspective, you also have one storage location, which simplifies the tasks of your security analysts.

When a query is issued to the resources listed in a log scope, the individual query results are combined. A log scope facilitates read-time aggregation of log data which might be stored in different locations. However, a log scope can also be used to provide read access to a one or more log views on a centralized log bucket.

When the **Logs Explorer** page opens, it issues queries to the resources listed in the default log scope. Therefore, configure the default scope so that the page shows you the data that you usually want to view. For example, you might set the default log scope to list a log view, which when queried, returns the log data for an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application.

### Best practices

Because log scopes provide a way for you to define and save a configuration for future use, we recommend that you create log scopes for complex search configurations.

For example, suppose that you are troubleshooting an issue and want to view the log entries for all virtual machine (VM) instances owned by your team. To accomplish this task, you might do the following:

  1. You determine that the log entries that you want to view are stored in multiple log buckets and in multiple projects. For most log buckets, a log view exists that includes the log entries that you want to analyze. Where a log view doesn't exist, you can create one.

  2. You decide to create a log scope because you expect to have a similar troubleshooting task in the future.

  3. You open the **Logs Explorer** page in the Google Cloud console and then use the **Refine scope** menu to select your new log scope.

  4. You review the log entries and find the information you need to resolve the issue you were investigating.

  5. After you resolve the issue, you share the failure cause with your colleagues. You also share that you expect to see similar failures in the future, so you created a log scope that will let you, or whomever is investigating the failure, quickly find relevant log entries.




### App Hub applications and log scopes

Your [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications might write log data to multiple projects. Your log data might be stored in the project in which it originates, or an organization administrator might have configured centralized storage. To view your application's log data, create a log scope, configure it to list the projects or log views that store your application's log data, and then configure it as the default log scope. When you complete those steps, the **Logs Explorer** page automatically displays the data written by your application, even when that data is stored in different projects or in a centralized log bucket.

Create the custom log scope in the project from which you will view your log data. This project is your App Hub host project or management project. For example, if a folder's display name is `My Folder`, then the display name of the folder's management project is `My Folder-mp`.

### Limitations

  * You can't delete or modify the log scope named `_Default`.
  * Only Google Cloud projects support a default log scope.
  * You can't add folders or organizations to a user-defined log scope.
  * Log scopes are created in the `global` location.



## Before you begin

Configure your project, your IAM roles, and select the interface that you plan to use.

### Configure your project and roles

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

  8. To get the permissions that you need to create and view log scopes, and to set the default log scope, ask your administrator to grant you the following IAM roles on your project: 

     * [Logs Configuration Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.configWriter) (`roles/logging.configWriter`)
     * [Observability Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.editor) (`roles/observability.editor`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and view log scopes, and to set the default log scope. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and view log scopes, and to set the default log scope:

     * To set the default log scope: `observability.scopes.{get, update}`
     * To create and manage log scopes: `logging.logScopes.{create, delete, get, list, update}`

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




### Select the interface you plan to use

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

## List log scopes

###  Console 

To list the log scopes, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your project, folder, or organization. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Log Scopes** tab.

The table lists your log scopes. When you've selected a Google Cloud project, one entry in the table is shown with a "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png), which indicates that this log scope lists the resources that the Logs Explorer searches when that page is opened.




###  gcloud 

**Note:** The Google Cloud CLI commands on this page are configured to query a Google Cloud project. To query a folder, replace the `--project` field with the `--folder` field. Similarly, to query an organization, replace the `--project` field with the `--organization` field.

To list the log scopes in a project, use the [`gcloud logging scopes list`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/list) command:
    
    
    gcloud logging scopes list --project=PROJECT_ID
    

Before running the command, update the following fields:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.



To get the details of a log scope in a project, use the [`gcloud logging scopes describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/describe) command:
    
    
    gcloud logging scopes describe LOG_SCOPE_ID --project=PROJECT_ID
    

Before running the command, update the following fields:

  * PROJECT_ID: The identifier of the project.
  * LOG_SCOPE_ID: The ID of the log scope. For example, `my-scope`.



###  Terraform 

You can use Terraform to create and modify a log scope. However, you can't use Terraform to list log scopes.

###  REST 

The Cloud Logging API contains commands that list the log scopes in a resource, or that report the details of a specific log scope. For a complete list of commands, see the [API reference documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest).

For Google Cloud projects, use the following commands:

  * [`projects.locations.logScopes.list`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/list).
  * [`projects.locations.logScopes.get`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/get).



In the previous commands, the `parent` field has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.



## Create a log scope

You can create 100 log scopes per project. A log scope can include a total of 100 log views and projects; however, it can only include 5 projects. You can't add folders or organizations to a log scope.

###  Console 

To create a log scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your project, folder, or organization. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Log Scopes** tab and then click **Create log scope**.
  4. To add one or more projects, click **Add projects** , and complete the dialog.

After you add a project, your IAM roles on that project determine which log entries that you can view. For example, your IAM role might let you view only those log entries that are accessible by a specific log view on a log bucket. For more information about roles, see [Logging roles](https://docs.cloud.google.com/logging/docs/access-control#considerations).

  5. To add one or more log views, click **Add log views** , and complete the dialog.

The dialog lists all log views that have log entries that originate in the current project, or that were routed to the current project by a sink in another project. For example, if you haven't configured any sinks, then this dialog lists the log views in your current project.

To list log views stored in another Google Cloud project, click _add_circle_ **Import project** , and then select the Google Cloud project.

After you add a log view, your IAM roles on either the log view or the project that stores the log view determine which log entries that you can access. For more information, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views).

  6. In the **Name log scope** section, enter the name and description that you want displayed on the **Log Scopes** tab.

The name of a log scope can't be modified and it must be unique within the project.

  7. Click **Create log scope**.




###  gcloud 

**Note:** The Google Cloud CLI commands on this page are configured to query a Google Cloud project. To query a folder, replace the `--project` field with the `--folder` field. Similarly, to query an organization, replace the `--project` field with the `--organization` field.

To create a log scope in a project, use the [`gcloud logging scopes create`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/create) command:
    
    
    gcloud logging scopes create LOG_SCOPE_ID --project=PROJECT_ID \
      --description=DESCRIPTION \
      --resource-names=RESOURCE_NAMES
    

Before running the command, update the following fields:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOG_SCOPE_ID: The ID of the log scope. For example, `my-scope`.
  * DESCRIPTION: Optional. The description of the log scope. Format the description as a string.

  * RESOURCE_NAMES: A comma-separated list of the fully-qualified names of projects or log views. For example, to include `my-project` in the log scope, specify `projects/my-project`.




###  Terraform 

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To create a log scope in a project, folder, or organization by using Terraform, use the Terraform resource [`google_logging_log_scope`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_log_scope).

In the command, set the following fields:

  * `parent`: The fully-qualified name of your project, folder, or organization. For example, you might set this field to `"projects/PROJECT_ID"`, where PROJECT_ID is the ID of your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * `location`: Set to `"global"`.
  * `name`: Set to the fully-qualified name of the log scope. For projects, the format of this field is:
        
        "projects/PROJECT_ID/locations/global/logScopes/LOG_SCOPE_ID"
        

In the previous expression, LOG_SCOPE_ID is the name of a log scope, such as "production".

  * `resource_names`: An array of projects and log views, where each project and log view is specified by its fully-qualified name.

  * `description`: A brief description. For example, "Scope for production resources".




###  REST 

The Cloud Logging API also supports creating log scopes in a folder or organization. For more information, see the [API reference documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest).

For Google Cloud projects, use the following command:

  * [`projects.locations.logScopes.create`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/create).



In the previous commands, the `parent` field has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.



## Modify or delete a log scope

###  Console 

To modify or delete a log scope that you or a colleague created, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your project, folder, or organization. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Log Scopes** tab.
  4. Find the **Log Scopes** that you want to modify or delete, click _more_vert_ **More** , and then do one of the following:

     * To modify, select **Edit scope** , and then complete the dialog.
     * To delete, select **Delete scope** , and then complete the dialog.



###  gcloud 

**Note:** The Google Cloud CLI commands on this page are configured to query a Google Cloud project. To query a folder, replace the `--project` field with the `--folder` field. Similarly, to query an organization, replace the `--project` field with the `--organization` field.

To modify the description of list of resources in a log scope in a project, use the [`gcloud logging scopes update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/update) command:
    
    
    gcloud logging scopes update LOG_SCOPE_ID --project=PROJECT_ID \
      --description=DESCRIPTION \
      --resource-names=RESOURCE_NAMES
    

Before running the command, update the following fields:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOG_SCOPE_ID: The ID of the log scope. For example, `my-scope`.
  * DESCRIPTION: The description of the log scope. Format the description as a string. Omit this field when you don't want to change the description of the log scope.

  * RESOURCE_NAMES: A comma-separated list of the fully-qualified names of projects or log views. Omit this field when you don't want to change the list of resources.




To delete a log scope in a project, use the [`gcloud logging scopes delete`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/scopes/delete) command:
    
    
    gcloud logging scopes delete LOG_SCOPE_ID --project=PROJECT_ID
    

Before running the command, update the following fields:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOG_SCOPE_ID: The ID of the log scope. For example, `my-scope`.



###  Terraform 

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To modify a log scope in a project, folder, or organization by using Terraform, use the Terraform resource [`google_logging_log_scope`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/logging_log_scope).

###  REST 

The Cloud Logging API contains commands that can modify or delete a log scope. For a complete list of commands, see the [API reference documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest).

For Google Cloud projects, use the following commands:

  * [`projects.locations.logScopes.patch`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/patch).
  * [`projects.locations.logScopes.delete`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.locations.logScopes/delete).



In the previous commands, the `parent` field has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID/logScopes/LOG_SCOPE_ID
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.
  * LOG_SCOPE_ID: The ID of the log scope. For example, `my-scope`.



## Configure the default log scope

This section doesn't apply to folders or organizations. For folders and organizations, when the **Logs Explorer** page opens, it searches for the log entries that originate in the folder or organization.

When a project is created, a log scope named `_Default` is created. This scope lists one resource, which is your project, and it is designated as the default log scope. If you create a project and don't modify the default log scope, then when the **Logs Explorer** page opens, it searches for all log entries that originate in the project.

You can create your own log scope and designate it as the default log scope. This capability lets you configure which resources the **Logs Explorer** page searches for log entries.

###  Console 

To set the default log scope for a project, do the following:

  1. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. . You can only set the default log scope for a project.

  2. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

The **Settings** page contains several tabs. Each tab displays the scope configuration for a particular telemetry type.

  3. Select the **Log Scopes** tab.

The tab displays your existing log scopes and a button to create a custom log scope.

  4. Find the log scope that you want to designate as the default log scope, click _more_vert_ **More** , and then select **Set as default**.

The log scope you selected is shown with a "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png).




###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

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
    




###  Terraform 

You can use Terraform to create and modify a log scope. However, you can't use Terraform to set the default log scope.

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
             




## What's next

  * [View logs by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
  * [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
