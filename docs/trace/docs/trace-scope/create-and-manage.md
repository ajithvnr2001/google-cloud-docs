---
url: https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage/
title: Create and manage trace scopes \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:43.184949+00:00
---

# Create and manage trace scopes  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-scope/create-and-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Create and manage trace scopes Stay organized with collections  Save and categorize content based on your preferences. 

Trace scopes let you search and analyze Cloud Trace data across multiple projects from the **Trace Explorer** page. If you only want to view and analyze spans that originate in a single Google Cloud project, then you don't need to configure any trace scopes. For information about viewing traces and spans, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## About trace scopes

Trace scopes let you have an aggregated view of trace data that is stored in multiple projects. These scopes are persistent, project-level resources that list views; each view provides access to the trace data stored by a project. Pages like the **Trace Explorer** use trace scopes to determine where to search for data. However, these pages also use your Identity and Access Management (IAM) roles on those resources to determine whether you have permission to see the data that is found.

When you create a trace scope, you provide a name and a list of projects. The system automatically includes each project's default trace view, which has the path `_Trace/Spans/_AllSpans`. The path fields `_Trace`, `Spans`, and `_AllSpans` refer to an observability bucket, the dataset that stores the data, and a view on the dataset. The `_AllSpans` view provides access to all trace data that the project stores.

The **Trace Explorer** page includes an option that lets you select a trace scope. When you make a selection, the page searches the views listed in the trace scope and refreshes the display.

You can also share your configured view by copying the browser URL. The URL encodes your selected trace scope and other page settings, overriding default scope selections for anyone who opens the link. For more information, see [Share traces and spans](https://docs.cloud.google.com/trace/docs/share-trace-or-span).

You can designate one trace scope as "default". When you make this designation, the following occur:

  * The system updates the observability scope. This scope contains pointers to the default log scope and default trace scope, which helps the system to correlate log and trace data when that data is stored in multiple projects. For more information, see [Configure observability scopes for multi-project queries](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

  * The system updates which trace scope the **Trace Explorer** page automatically uses to search for trace data. If the page can't access the default trace scope, then it searches your project for trace data.




You can modify and delete any trace scopes that you create.

## App Hub applications and trace scopes

Your [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) applications might write trace data to multiple projects. To get an aggregate view of this data, create a trace scope, configure it to list the default trace view of all projects that store trace data, and then configure it as the default trace scope. When you complete those steps, the **Trace Explorer** page automatically displays the data written by your application, even when that data is stored in different projects.

Create the custom trace scope in the project from which you view your trace data. This project is your App Hub host project or management project. For example, if a folder's display name is `My Folder`, then the display name of the folder's management project is `My Folder-mp`.

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

  8. To get the permissions that you need to create and view trace scopes, ask your administrator to grant you the [Observability Scopes Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.scopesEditor) (`roles/observability.scopesEditor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and view trace scopes. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and view trace scopes:

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

## List trace scopes

###  Console 

To list the trace scopes, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Trace Scopes** tab.

The window displays a list of your trace scopes. The entry that includes a "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png), is the default trace scope.

  4. To view the details of a trace scope, expand it.

If you expand a trace scope, then you can see the list of views that the scope includes. Each row lists a project ID along with an entry like `_Trace/Spans/_AllSpans`, which identifies the default storage location for your trace data. The fields `_Trace`, `Spans`, and `_AllSpans` refer to the observability bucket, dataset, and view for your trace data. The `_AllSpans` view corresponds to every entry in the bucket:

Name | Description | Type | Resources  
---|---|---|---  
_arrow_right_`_Default` |  | `Trace scope` | `1`  
_arrow_drop_down_`myscope` | `My description` | `Trace scope` | `2`  
` _Trace/Spans/_AllSpans` | `myproject` | `Trace view` |   
` _Trace/Spans/_AllSpans` | `project-b` | `Trace view` |   



###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * LOCATION: The location of the trace scope. This field must have a value of `global`.
  * PROJECT_ID: The identifier of the project..



Execute the [`gcloud observability trace-scopes list`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/trace-scopes/list) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability trace-scopes list \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability trace-scopes list `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability trace-scopes list ^
     --location=LOCATION --project=PROJECT_ID

The response data is a list of trace scopes. For each scope, the name and relevant information is shown. For example, the following illustrates the result of the `list` command for a project that has two trace scopes: 
    
    
    name: projects/my-project/locations/global/traceScopes/_Default
    resourceNames:
    - projects/my-project
    ---
    createTime: '2026-03-26T13:43:54.772326947Z'
    description: a test
    name: projects/my-project/locations/global/traceScopes/my-test-scope
    resourceNames:
    - projects/another-project
    - projects/my-project
    updateTime: '2026-03-26T13:43:54.772326947Z'
    

###  Terraform 

You can use Terraform to create and modify a trace scope. However, you can't use Terraform to list trace scopes.

###  REST 

To list all trace scopes in a Google Cloud project, use the [`projects.locations.traceScopes.list`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes/list) command. You must specify a path parameter.

The path parameter for this endpoint has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID/traceScopes
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.



The response is an array of [`TraceScope`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes#TraceScope) objects. Each object includes a name and a list of resources.

To get information about a specific trace scope, use the [`projects.locations.traceScopes.get`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes/get) command.

## Create a trace scope

The spans displayed by the **Trace Explorer** page depend on the searched views, your IAM roles on those views, the time-range setting, and the filters you apply.

**Warning:** Make sure that all views listed in a trace scope store their trace data in the same location. The system stores your trace data in an observability bucket named `_Trace`. For information about how to display the location where your trace data is stored, see [List observability buckets](https://docs.cloud.google.com/trace/docs/storage-manage#list-buckets).

You can create 100 trace scopes per project. A trace scope can include a total of 20 views.

###  Console 

To create a trace scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Trace Scopes** tab and then click **Create trace scope**.
  4. Click **Add projects** and complete the dialog.

**Note:** When you select a project, the system adds the project's default trace view to the scope.
  5. In the **Name trace scope** section, enter the name and description that you want displayed on the **Trace Scopes** tab.

The name of a trace scope can't be modified, and it must be unique within the project.

  6. Click **Create trace scope**.

By default, the **Trace scopes** table lists your trace scopes in a collapsed form. For each scope, the table lists a name, description, type, and number of resources.

If you expand a trace scope, then you can see the list of views that the scope includes. Each row lists a project ID along with an entry like `_Trace/Spans/_AllSpans`, which identifies the default storage location for your trace data. The fields `_Trace`, `Spans`, and `_AllSpans` refer to the observability bucket, dataset, and view for your trace data. The `_AllSpans` view corresponds to every entry in the bucket:

Name | Description | Type | Resources  
---|---|---|---  
_arrow_right_`_Default` |  | `Trace scope` | `1`  
_arrow_drop_down_`myscope` | `My description` | `Trace scope` | `2`  
` _Trace/Spans/_AllSpans` | `myproject` | `Trace view` |   
` _Trace/Spans/_AllSpans` | `project-b` | `Trace view` |   



###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * TRACE_SCOPE_NAME: The name of a trace scope. For example, `my-trace-scope`.
  * DESCRIPTION: Optional. The description of the trace scope. Format the description as a string.
  * RESOURCE_NAMES: A comma-separated list of the fully-qualified names of projects. For example, `projects/my-project`.
  * LOCATION: The location of the trace scope. This field must have a value of `global`.
  * PROJECT_ID: The identifier of the project..



Execute the [`gcloud observability trace-scopes create`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/trace-scopes/create) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability trace-scopes create TRACE_SCOPE_NAME \
     --description=DESCRIPTION \
     --resource-names=RESOURCE_NAMES \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability trace-scopes create TRACE_SCOPE_NAME `
     --description=DESCRIPTION `
     --resource-names=RESOURCE_NAMES `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability trace-scopes create TRACE_SCOPE_NAME ^
     --description=DESCRIPTION ^
     --resource-names=RESOURCE_NAMES ^
     --location=LOCATION --project=PROJECT_ID

When successful, the response of the `create` command includes the name of the new trace scope: 
    
    
    Created traceScope [my-test-scope].
    

###  Terraform 

For information about how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To create a trace scope in a project by using Terraform, use the Terraform resource [`google_observability_trace_scope`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_trace_scope).

In the command, set the following fields:

  * `project`: The name of your project, folder, or organization. For example, `my-project`. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

**Note:** The system doesn't add the project to the scope. Instead, it adds the project's `_AllSpans` view on the `Spans` dataset.
  * `trace_scope_id`: Set to a scope ID. For example, `my-trace-scope`.

  * `location`: Set to `"global"`.

  * `resource_names`: An array of projects, where each project is specified by using its fully-qualified name.

  * `description`: A brief description. For example, "Scope for production resources".




###  REST 

To create a trace scope, use the [`projects.locations.traceScopes.create`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes/create) command. You must specify a path parameter and provide a [`TraceScope`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes#TraceScope) object. The response is a `TraceScope` object.

The path parameter for this endpoint has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID/traceScopes
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.



## Modify a trace scope

You can't modify the trace scope named `_Default`. You can modify all other trace scopes.

###  Console 

To modify a trace scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Trace Scopes** tab.
  4. Find the trace scope that you want to modify, click _more_vert_ **More** , select **Edit scope** , and then complete the dialog.



###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * TRACE_SCOPE_NAME: The name of a trace scope. For example, `my-trace-scope`.
  * DESCRIPTION: Optional. The description of the trace scope. Format the description as a string.
  * RESOURCE_NAMES: A comma-separated list of the fully-qualified names of projects. For example, projects/my-project.
  * LOCATION: The location of the trace scope. This field must have a value of `global`.
  * PROJECT_ID: The identifier of the project..



Execute the [`gcloud observability trace-scopes update`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/trace-scopes/update) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability trace-scopes update TRACE_SCOPE_NAME \
     --description=DESCRIPTION \
     --resource-names=RESOURCE_NAMES \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability trace-scopes update TRACE_SCOPE_NAME `
     --description=DESCRIPTION `
     --resource-names=RESOURCE_NAMES `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability trace-scopes update TRACE_SCOPE_NAME ^
     --description=DESCRIPTION ^
     --resource-names=RESOURCE_NAMES ^
     --location=LOCATION --project=PROJECT_ID

When successful, the response data of an `update` command displays the updated trace scope: 
    
    
    Updated traceScope [my-test-scope].
    createTime: '2026-03-26T13:43:54.772326947Z'
    description: A scope for testing
    name: projects/my-project/locations/global/traceScopes/my-test-scope
    resourceNames:
    - projects/another-project
    - projects/my-project
    updateTime: '2026-03-26T13:48:05.262142872Z'
    

###  Terraform 

For information about how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To modify a trace scope in a project by using Terraform, use the Terraform resource [`google_observability_trace_scope`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_trace_scope).

###  REST 

To modify a trace scope, use the [`projects.locations.traceScopes.patch`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes/patch) command. You must specify a path parameter, query parameters, and provide a [`TraceScope`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes#TraceScope) object. The query parameters identify which fields are changed. The response is a `TraceScope` object.

The path parameter for this endpoint has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID/traceScopes/TRACE_SCOPE_NAME
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.
  * TRACE_SCOPE_NAME: The name of a trace scope. For example, `my-trace-scope`.



## Delete a trace scope

You can't delete the trace scope named `_Default`. You can delete all other trace scopes.

###  Console 

To delete a trace scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Trace Scopes** tab.
  4. Find the trace scope that you want to delete, click _more_vert_ **More** , select **Delete scope** , and then complete the dialog.



###  gcloud 

**Note** : You must use gcloud CLI version 586.0.0 or later.

Before using any of the command data below, make the following replacements: 

  * TRACE_SCOPE_NAME: The name of a trace scope. For example, `my-trace-scope`.
  * LOCATION: The location of the trace scope. This field must have a value of `global`.
  * PROJECT_ID: The identifier of the project..



Execute the [`gcloud observability trace-scopes delete`](https://docs.cloud.google.com/sdk/gcloud/reference/observability/trace-scopes/delete) command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud observability trace-scopes delete TRACE_SCOPE_NAME \
     --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud observability trace-scopes delete TRACE_SCOPE_NAME `
     --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud observability trace-scopes delete TRACE_SCOPE_NAME ^
     --location=LOCATION --project=PROJECT_ID

If you issue a `delete` command, then you are prompted to confirm the action. The following shows an example execution: 
    
    
    You are about to delete traceScope [my-test-scope]
    
    Do you want to continue (Y/n)?  Y
    
    Deleted traceScope [my-test-scope].
    

###  Terraform 

For information about how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To delete a trace scope in a project by using Terraform, use the Terraform resource [`google_observability_trace_scope`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/observability_trace_scope).

###  REST 

To delete a trace scope, use the [`projects.locations.traceScopes.delete`](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/projects.locations.traceScopes/delete) command. You must specify a path parameter.

The path parameter for this endpoint has the following syntax:
    
    
    projects/PROJECT_ID/locations/LOCATION_ID/traceScopes/TRACE_SCOPE_NAME
    

The fields in the previous expression have the following meaning:

  * PROJECT_ID: The identifier of the project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.
  * LOCATION_ID must be set to `global`.
  * TRACE_SCOPE_NAME: The name of a trace scope. For example, `my-trace-scope`.



## Configure the default trace scope

When the **Trace Explorer** page opens, it searches the views listed in the default trace scope for trace data. If the default scope isn't accessible, then the page searches your project for trace data. This search is equivalent to querying your project's `_AllSpans` view on the default dataset.

When projects are created, the trace scope named `_Default` is created and is designated as the default trace scope. However, you can create your own trace scope and designate it as the default trace scope.

###  Console 

To set the default trace scope, do the following:

  1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 
  3. Select the **Trace Scopes** tab.

The tab displays your trace scopes, and it includes a button to create a custom trace scope. The trace scope that is shown with a "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png), is the current default trace scope.

  4. To change the default trace scope, find the trace scope that you want to designate as the default trace scope, click its _more_vert_ **More** , and then select **Set as default**.

The trace scope you selected is shown with a "Default" icon, ![](https://docs.cloud.google.com/static/stackdriver/images/default_scope_icon.png).




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

You can use Terraform to create and modify a trace scope. However, you can't use Terraform to set the default trace scope.

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
             




## Limits on trace scopes

Limits on trace scopes | Value  
---|---  
Maximum number of trace scopes per project | 100  
Maximum number of views per trace scope | 20  
  
## What's next

  * [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces)

  * Cloud Logging and Cloud Monitoring contain similar constructs that let you control the log data or metric data that you can view or monitor. For information about those scopes, see the following documents:

    * [Observability scopes overview](https://docs.cloud.google.com/stackdriver/docs/observability/scopes)
    * [Create and manage log scopes](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface)
    * [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
