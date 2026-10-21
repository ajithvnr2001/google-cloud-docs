---
url: https://docs.cloud.google.com/monitoring/settings/manage-api/
title: Configure a metrics scope by using the API \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:21.702005+00:00
---

# Configure a metrics scope by using the API  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/settings/manage-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Configure a metrics scope by using the API Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Google Cloud CLI or the Cloud Monitoring API to configure the metrics scope of a Google Cloud project. This page is intended for developers and system administrators.

You can also use Terraform to configure a metrics scope. For more information, see the [Terraform registry for `google_monitoring_monitored_project`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/monitoring_monitored_project).

## App Hub applications and metrics scopes

You manage the metrics scope for [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) host projects and management projects for single-project boundaries. You can manage the metrics scope either by using the [Google Cloud console](https://docs.cloud.google.com/monitoring/settings/multiple-projects) or the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/settings/manage-api).

Google Cloud manages the metrics scope for app-enabled folders, unless adding a project to the metrics scope fails due to exhaustion of the metrics scope quota. In that case, you can request a quota increase and then manually add projects to the metrics scope of the management project for your app-enabled folder. To learn more, see [Metrics scopes for app-enabled folders](https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders).

## Before you begin

  * If you aren't familiar with the terms _metrics scope_ and _scoping project_ , then see [Metrics scopes](https://docs.cloud.google.com/monitoring/settings).

  * Ensure that your Identity and Access Management (IAM) roles on the [scoping project](https://docs.cloud.google.com/monitoring/settings) and on each project that you want to add to, or remove from, a metrics scope, include all permissions in the Monitoring Admin (`roles/monitoring.admin`) role. For more information, see [Metrics scope configurations](https://docs.cloud.google.com/monitoring/access-control#workspace_roles_desc).

  * The metrics scope methods of the Cloud Monitoring API that retrieve information are synchronous; however, those APIs that change state are asynchronous. The Google Cloud CLI commands block until the asynchronous operation completes. For information about how to determine when an asynchronous API method is complete and how to determine its status, see Asynchronous API methods.

  * If you plan to invoke the Cloud Monitoring API by using `curl` or if you want to use the samples on this page, then complete the `curl` command setup steps.




## Add a project to a metrics scope

###  gcloud 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To add a Google Cloud project to a metrics scope, run the [`gcloud beta monitoring metrics-scopes create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/metrics-scopes/create) command:
    
    
    gcloud beta monitoring metrics-scopes create MONITORED_PROJECT_ID_OR_NUMBER --project=SCOPING_PROJECT_ID_OR_NUMBER
    

Before you run the previous command, do the following:

  * Enter the name or ID of the Google Cloud project whose metrics scope is to be modified into the variable SCOPING_PROJECT_ID_OR_NUMBER. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  * Enter the identifier of your monitored project into the variable MONITORED_PROJECT_ID_OR_NUMBER. The format is `projects/PROJECT_ID_OR_NUMBER`.




For example, the following command adds the project `my-monitored-project` to the metrics scope of the project named `my-staging-projects`:
    
    
    gcloud beta monitoring metrics-scopes create projects/my-monitored-project --project=my-staging-projects
    

The response to the previous command provides confirmation that the command completed successfully:
    
    
    Created monitored project [locations/global/metricsScopes/my-staging-projects/projects/my-monitored-project].
    

###  curl 

To add a Google Cloud project to a metrics scope, send a `POST` request to the [`locations.global.metricsScopes.projects.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects/create) endpoint:
    
    
    curl -H "Authorization: Bearer ${TOKEN}" \
    -H "Content-Type: application/json" -X POST \
    -d "{'name': 'locations/global/metricsScopes/${SCOPING_PROJECT_ID_OR_NUMBER}/projects/${MONITORED_PROJECT_ID_OR_NUMBER}'}" \
    https://monitoring.googleapis.com/v1/locations/global/metricsScopes/${SCOPING_PROJECT_ID_OR_NUMBER}/projects

In the previous example, the environment variables are defined as follows:

  * `MONITORED_PROJECT_ID_OR_NUMBER` stores the ID of the project to be added to the metrics scope.
  * `SCOPING_PROJECT_ID_OR_NUMBER` stores the ID of the project whose metrics scope is being updated.



The response of this asynchronous method is an [`Operation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations#Operation) object.

Applications calling this method should poll the [`operation.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations/get) endpoint until the value of the `Operation.done` field is `true`. When the `Operation.done` field is set to `false`, that indicates the operation is in progress. For more information, see Asynchronous API commands.

The following is an example of the response when adding a monitored project is successful:
    
    
    {
      "name": "operations/6915efde-1915-400a-ad49-7b62041d9bd2",
      "metadata": {
        "@type": "type.googleapis.com/google.monitoring.metricsscope.v1.OperationMetadata",
        "state": "DONE",
        ...
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.monitoring.metricsscope.v1.MonitoredProject",
        "name": "locations/global/metricsScopes/012012012012/projects/678678678678",
        "provider": "G​C​P",
        "providerAccountId": "...",
        ...
      }
    }
    

In the previous response, the `Operation.done` field is set to `true`. This value indicates that the command is complete. Because the command completed successfully, the `Operation.response` field is set and its value is a [`MonitoredProject`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects#MonitoredProject) object. The `response.name` field includes the identifier of the scoping project and the monitored project. The `providerAccountId` field lists the name of the monitored project.

Invoking this method results in an entry in the audit logs of the scoping project. The Google Cloud console doesn't invoke this API method. Therefore, modifications made to a metrics scope when using the Google Cloud console aren't recorded in the audit logs.

## Remove a project from a metrics scope

###  gcloud 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To remove a Google Cloud project, from a metrics scope, run the [`gcloud beta monitoring metrics-scopes delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/metrics-scopes/delete) command:
    
    
    gcloud beta monitoring metrics-scopes delete MONITORED_PROJECT_ID_OR_NUMBER --project=SCOPING_PROJECT_ID_OR_NUMBER
    

Before you run the previous command, do the following:

  * Enter the name or ID of the Google Cloud project whose metrics scope is to be modified into the variable SCOPING_PROJECT_ID_OR_NUMBER. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

  * Enter the identifier of your monitored project into the variable MONITORED_PROJECT_ID_OR_NUMBER. The format is `projects/PROJECT_ID_OR_NUMBER`.




For example, the following command removes the project `my-monitored-project` from the metrics scope of the project named `my-staging-projects`:
    
    
    gcloud beta monitoring metrics-scopes delete projects/my-monitored-project --project=my-staging-projects
    

The response to the previous command provides confirmation that the command completed successfully:
    
    
    Deleted monitored project [locations/global/metricsScopes/my-staging-projects/projects/my-monitored-project].
    

The following error is reported when the scoping project isn't monitoring the project specified by the MONITORED_PROJECT_ID_OR_NUMBER variable:
    
    
    NOT_FOUND: Requested entity was not found.
    

###  curl 

To remove a Google Cloud project from a metrics scope, send a `DELETE` request to the [`locations.global.metricsScopes.projects.delete`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes.projects/delete) endpoint:
    
    
    curl -H "Authorization: Bearer ${TOKEN}" -X DELETE \
    https://monitoring.googleapis.com/v1/locations/global/metricsScopes/${SCOPING_PROJECT_ID_OR_NUMBER}/projects/${MONITORED_PROJECT_ID_OR_NUMBER}

In the previous example, the environment variables are defined as follows:

  * `MONITORED_PROJECT_ID_OR_NUMBER` stores the ID of the project to be removed from the metrics scope.
  * `SCOPING_PROJECT_ID_OR_NUMBER` stores the ID of the project whose metrics scope is being updated.



The response to this asynchronous method is an [`Operation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations#Operation) object.

Applications calling this method should poll the [`operation.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations/get) endpoint until the value of the `Operation.done` field is `true`. When the `Operation.done` field is set to `false`, that indicates the operation is in progress. For more information, see Asynchronous API commands.

The following is an example of the response when removal of a monitored project is successful:
    
    
    {
      "name": "operations/4367ff34-0ff0-4767-b8d3-0638e30f077c",
      "metadata": {
        "@type": "type.googleapis.com/google.monitoring.metricsscope.v1.OperationMetadata",
        "state": "DONE",
        ...
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

In the previous response, the `Operation.done` field is set to `true`. This value indicates that the command is complete. Because the command completed successfully, the `Operation.response` field is set and contains an `@type` field.

Invoking this method results in an entry in the audit logs of the scoping project. The Google Cloud console doesn't invoke this API method. Therefore, modifications made to a metrics scope when using the Google Cloud console aren't recorded in the audit logs.

## List all metrics scopes that include a project

If you want to know which resources can view the data stored by a Google Cloud project, then you can list all metrics scopes that include the project and then find details about those scopes. This section provides information about how to list the metrics scope that include a specific Google Cloud project.

###  gcloud 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To get a list of metrics scopes that can view the metrics for a Google Cloud project, run the [`gcloud beta monitoring metrics-scopes list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/metrics-scopes/list) command:
    
    
    gcloud beta monitoring metrics-scopes list MONITORED_PROJECT_ID_OR_NUMBER
    

Before you run the command, enter the identifier of the your monitored project into the variable MONITORED_PROJECT_ID_OR_NUMBER. The format is `projects/PROJECT_ID_OR_NUMBER`..

For example, to list the metrics scopes that include the project `my-project`, run the following command:
    
    
    gcloud beta monitoring metrics-scopes list projects/my-project
    

The following response indicates that the project `my-project` is included in two metrics scopes:
    
    
    metricsScopes:
    - createTime: '2018-08-06T17:13:42Z'
      name: locations/global/metricsScopes/012345012345
      updateTime: '2018-08-18T16:20:37.032928Z'
    - createTime: '2021-04-13T15:37:26.869Z'
      name: locations/global/metricsScopes/9876543210
      updateTime: '2021-04-13T15:37:27.284239Z'
    

To get detailed information about a metrics scope, run the `gcloud beta monitoring metrics-scopes describe` command.

###  curl 

To get a list of metrics scopes that can view the metrics for a project, send a `GET` request to the [`locations.global.metricsScopes.listMetricsScopesByMonitoredProject`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes/listMetricsScopesByMonitoredProject) endpoint and include the query parameter that specifies the project.
    
    
    curl -H "Authorization: Bearer ${TOKEN}" \
    https://monitoring.googleapis.com/v1/locations/global/metricsScopes:listMetricsScopesByMonitoredProject?monitored_resource_container=projects/${PROJECT_ID_OR_NUMBER}

In the previous example, the environment variable `PROJECT_ID_OR_NUMBER` stores the ID of the project whose inclusion in metrics scope is being queried.

When successful, the response is an array of [`MetricsScope`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes#MetricsScope) objects.

This method doesn't result in an entry being written to the audit logs of the scoping project. To have these actions recorded in the audit log, enable **Data Read** for the **Cloud Resource Manager API**. For more information, see [Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Get details about a metrics scope

This section shows you how to find details about a specific metrics scope.

###  gcloud 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To get detailed information about a metrics scope, run the [`gcloud beta monitoring metrics-scopes describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/monitoring/metrics-scopes/describe) command:
    
    
    gcloud beta monitoring metrics-scopes describe METRICS_SCOPE_ID
    

Before you run the command, enter the name of the fully qualified name of a metrics scope into the variable METRICS_SCOPE_ID. The following is an example of a fully qualified name:
    
    
    locations/global/metricsScopes/012345012345
    

The following is an example of response. In this example, the metrics scope contains one project, and the ID of the metrics scope and project are the same:
    
    
    createTime: '2018-08-06T17:13:42Z'
    monitoredProjects:
    - createTime: '2018-08-06T17:13:42Z'
      name: locations/global/metricsScopes/012345012345/projects/012345012345
    name: locations/global/metricsScopes/012345012345
    updateTime: '2018-08-18T16:20:37.032928Z'
    

To identify the Google Cloud project from its ID, run the `gcloud projects list` command and filter by the project ID. For example, to get the name for the project `012345012345`, run the following command:
    
    
    gcloud projects list --filter="012345012345" --format="value(NAME)"
    

###  curl 

To get information about a metrics scope, send a `GET` request to the [`locations.global.metricsScopes.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes/get) endpoint:
    
    
    curl -H "Authorization: Bearer ${TOKEN}" \
    https://monitoring.googleapis.com/v1/locations/global/metricsScopes/${SCOPING_PROJECT_ID_OR_NUMBER}

In the previous example, the environment variable `SCOPING_PROJECT_ID_OR_NUMBER` stores the ID of the project whose metrics scope is being queried.

When successful, the response is a [`MetricsScope`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes#MetricsScope) object.

This method doesn't result in an entry being written to the audit logs of the scoping project. To have these actions recorded in the audit log, enable **Data Read** for the **Cloud Resource Manager API**. For more information, see [Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

## Asynchronous API methods

**Note:** The Google Cloud CLI commands block until asynchronous API method they invoke complete.

All metrics scope methods of the Cloud Monitoring API that change the state of the system, for example, the command to add a monitored project a metrics scope, are asynchronous. For these commands, the command response is an [`Operation`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations#Operation) object.

Applications that call an asynchronous API method should poll the [`operation.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations/get) endpoint until the value of the `Operation.done` field is `true`:

  * When `done` is `false`, the operation is in progress.

To refresh the status information, send a `GET` request to the [`operation.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/operations/get) endpoint:
        
        curl -H "Authorization: Bearer ${TOKEN}" \
        https://monitoring.googleapis.com/v1/${OPERATION_NAME}

In the previous command, `OPERATION_NAME` is an environment variable that stores the value of the `Operation.name` field.

  * When `done` is `true`, the operation is complete and either the `error` or `response` field is set:

    * `error`: When set, the asynchronous operation failed. The value of this field is a [`Status`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status) object that contains a gRPC error code and an error message.
    * `response`: When set, the asynchronous operation completed successfully, and the value reflects the result.



## `curl` command setup

This section describes the setup used to create the curl commands in this document. Each `curl` command on this page includes a set of arguments followed by the URL of an API resource:
    
    
    curl -H "Authorization: Bearer ${TOKEN}" <other_args> \
    https://monitoring.googleapis.com/v1/locations/global/metricsScopes/<resource>
    

Set these environment variables to simplify creation of the `curl` commands:

  1. Create the environment variable to store the scoping project ID or number. If you are using App Hub, then set this variable to the ID of your App Hub host project or to the ID the management project of your app-enabled folder:
         
         SCOPING_PROJECT_ID_OR_NUMBER=SCOPING_PROJECT_ID_OR_NUMBER
         

  2. Optional. If you plan to add or remove monitored projects, then configure the environment variable with the monitored project ID or number:
         
         MONITORED_PROJECT_ID_OR_NUMBER=MONITORED_PROJECT_ID_OR_NUMBER
         

  3. Authenticate to the Google Cloud CLI:
         
         gcloud auth login
         

  4. Optional. To avoid having to specify your project ID with each `gcloud` command, set your project ID as the default by using gcloud CLI:
         
         gcloud config set project ${SCOPING_PROJECT_ID_OR_NUMBER}
         

  5. Create an authorization token and capture it in an environment variable:
         
         TOKEN=`gcloud auth print-access-token`
         

Tokens are valid for a limited time. If commands that worked suddenly report that you are unauthenticated, then reissue this command.

  6. To verify that you got an access token, echo the `TOKEN` variable:
         
         echo ${TOKEN}
         ya29.GluiBj8o....
         




You might also have to specify other arguments, for example, to specify the type of the HTTP request (for example, `-X DELETE`). The default request is `GET`, so the examples don't specify it.

## What's next

For information about using Google Cloud with Terraform, see the following resources:

  * [Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform)
  * [Terraform registry for `google_monitoring_monitored_project`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/monitoring_monitored_project)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
