---
url: https://docs.cloud.google.com/app-optimize/create-report/
title: Create a report \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:11.670771+00:00
---

# Create a report  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/create-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

#  Create a report Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Optimize API lets you analyze cost and resource utilization data for a single project or App Hub application by generating reports.

## Overview

You create a report by sending an API request that defines the scope of the data, how it should be aggregated or grouped, and any filters to apply. The API request creates a long-running operation (LRO) that generates your report.

When the report is ready, you can then read the data.

For information on available scopes, dimensions, metrics, and filters, and valid combinations of these settings, see [About reports](https://docs.cloud.google.com/app-optimize/about-reports).

## Before you begin

  * The examples in this guide require a Google Cloud project with active resources to analyze. App Optimize API needs billing and utilization data to produce meaningful results; reports run against new or empty projects will be empty.

In this guide, the project identified as `PROJECT_ID` provides the data [scope](https://docs.cloud.google.com/app-optimize/about-reports#scopes) and hosts the report resource.

App Optimize API does support creating reports in one project that analyzes data from another project or from applications in [single-project or folder-level boundaries](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub). To generate a report on an App Hub application, which can be made up of multiple projects, you must have the required monitoring and billing permissions on all of the application's associated projects to create the report.

  * Ensure that the [App Optimize API is enabled](https://docs.cloud.google.com/app-optimize/enable-api) for the project you will use to create and manage the report resource.



  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

Verify that you have the permissions required to complete this guide. 

Verify that you have the permissions required to complete this guide. 

  * Select the tab for how you plan to use the samples in this document:




### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account) in the Google Cloud authentication documentation. 

### Python

  1. Install the [Python client library](https://docs.cloud.google.com/app-optimize/reference/libraries) for App Optimize API.
  2. To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

For information about setting up authentication for a production environment, see [ Set up Application Default Credentials for code running on Google Cloud ](https://docs.cloud.google.com/docs/authentication/set-up-adc-attached-service-account) in the Google Cloud authentication documentation. 

### Required roles

To get the permissions that you need to create a report using this guide, ask your administrator to grant you the following IAM roles on your project with active resources: 

  * [App Optimize Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/appoptimize#appoptimize.admin) (`roles/appoptimize.admin`)
  * [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * Cloud Hub Operator (`roles//cloudhub.operator`) (or another role granting `billing.resourceCosts.get`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about permissions and roles required for App Optimize API, see [Access control with IAM](https://docs.cloud.google.com/app-optimize/access-control).

## Create a report

The following steps describe how to initiate report creation. This example creates a report to help you understand your chosen project's costs and average CPU usage over the last week. The report breaks down this information by each individual resource, including what type of resource it is, the Google Cloud product it's part of, and its location.

To create the report resource, follow the instructions for your preferred method:

### gcloud

Use the following `gcloud beta app-optimize reports create` command to create your report.
    
    
    gcloud beta app-optimize reports create REPORT_ID \
      --project=PROJECT_ID \
      --location=global \
      --dimensions=location,product_display_name,project,resource,resource_type \
      --metrics=cost,cpu_mean_utilization \
      --report-filter='hour >= now - duration("168h")' \
      --scopes=project=projects/PROJECT_ID
    

Replace the following:

  * `REPORT_ID`: a unique ID for your new report—for example, `my-resource-cost-report-1`.
  * `PROJECT_ID`: your Google Cloud project ID.



The command to create a report automatically waits for the operation to complete.

### Python

The following Python code uses `AppOptimizeClient.create_report()` to create a report.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    report_id = "REPORT_ID"
    
    # Create the App Optimize client
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    
    # Initialize the report request
    report = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[Report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.Report.html)(
        dimensions=['location', 'product_display_name', 'project', 'resource', 'resource_type'],
        metrics=['cost', 'cpu_mean_utilization'],
        filter='hour >= now - duration("168h")',
        scopes=[
            [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[Scope](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.Scope.html)(project=f"projects/{project_id}"),
        ],
    )
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[CreateReportRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.CreateReportRequest.html)(
        parent=f"projects/{project_id}/locations/global",
        report=report,
        report_id=report_id,
    )
    
    # Send the request and wait for completion
    operation = client.[create_report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_create_report)(request=request)
    print("Waiting for operation to complete...")
    response = operation.result()
    print(response)
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REPORT_ID`: a unique ID for your new report—for example, `my-first-report`.



The `operation.result()` method in the client library automatically waits for the operation to complete. No manual polling loop is required.

### REST

Send an HTTP `POST` request to the REST API's `projects.locations.reports` resource path

  1. To send the request, use the following [`curl`](https://curl.se) command:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{
             "scopes": [
               {
                 "project": "projects/PROJECT_ID"
               }
             ],
             "dimensions": [
               "location",
               "product_display_name",
               "project",
               "resource",
               "resource_type"
             ],
             "metrics": [
               "cost",
               "cpu_mean_utilization"
             ],
             "filter": "hour >= now - duration(\"168h\")"
           }' \
           "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports?report_id=REPORT_ID"
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REPORT_ID`: a unique ID for your new report—for example, `my-resource-cost-report-1`.

The API returns a long-running operation (LRO) object. Note the `name` field in the response, which you'll use to check the operation's status:
    
    {
      "name": "projects/PROJECT_ID/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.appoptimize.v1beta.OperationMetadata"
      },
      "done": false
    }
    

In the response, the `done` field is `false`, indicating that the report generation is in progress.

  2. To check if the report is ready, send a `GET` HTTP request to the operation `name` returned in the previous step:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/operations/OPERATION_ID"
         

Replace `PROJECT_ID` and `OPERATION_ID` with the values from the LRO response.

Examine the response to determine the operation's status:

     * If the report is still being generated, the response will look similar to the initial LRO response, with `done` set to `false`. You should wait a short period, such as 5 to 15 seconds, and poll again by repeating this step.
     * When the report generation is complete, the response will have `"done": true` and include the report resource in the `response` field:
           
           {
               "name": "projects/PROJECT_ID/locations/global/operations/OPERATION_ID",
               "metadata": {
                 "@type": "type.googleapis.com/google.cloud.appoptimize.v1beta.OperationMetadata"
               },
               "done": true,
               "response": {
                 "@type": "type.googleapis.com/google.cloud.appoptimize.v1beta.Report",
                 "name": "projects/PROJECT_ID/locations/global/reports/REPORT_ID",
                 "dimensions": [
                   "location",
                   "product_display_name",
                   "project",
                   "resource",
                   "resource_type"
                 ],
                 "scopes": [
                   {
                     "project": "projects/PROJECT_ID"
                   }
                 ],
                 "filter": "hour >= now - duration(\"168h\")",
                 "expireTime": "2026-02-05T18:50:25.273833857Z",
                 "metrics": [
                   "cost",
                   "cpu_mean_utilization"
                 ]
               }
             }
             ```
           

     * If the LRO encounters an error, the response will contain an `error` field instead of the `response` field, providing details about the failure.




Once the operation is successfully complete, you can [read the report's data](https://docs.cloud.google.com/app-optimize/read-report).

## Concurrency limits

When you create a report, App Optimize API gets cost data from Cloud Billing and utilization data from Cloud Monitoring for each target_project of the report.

  * For a report scoped to a single project, that project is the target project.
  * For an App Hub application, each project that contains a service or workload in the application is a target project.



App Optimize API enforces a concurrency quota called **Concurrent CreateReport operations** , which allows a maximum of 10 concurrent requests for report data per target project. When you create a report, App Optimize API calculates the number of target projects in the report and locks the required number of quota units until the LRO for creating the report is finished.

Reports that complete in less than a few minutes might not be counted against your concurrency limit due to system-level measurement timing.

You can view your current API activity and manage these limits on the [Quotas & System Limits](https://console.cloud.google.com/apis/api/appoptimize.googleapis.com/quotas) page in the Google Cloud console.

If you plan to create multiple reports concurrently, consider when your teams run reports and how your App Hub applications are structured:

  * If multiple teams run reports that include the same target projects, you can stagger the start times for report creation for each team.
  * Applications can include resources from multiple projects, and more than one application might use resources from a single project. Creating reports concurrently for these types of applications results in multiple requests to target projects.



For example, consider a team that works on a suite of applications for learning creative arts, with standard and premium variants. The following table shows the list of applications in the first column. In the remaining columns, the check mark icon () indicates that a project contains services or workloads for a listed application.

Application | common-project | dance-project | draw-project | animate-project | **music-project**  
---|---|---|---|---|---  
dance-app |  |  |  |  |   
draw-app |  |  |  |  |   
music-app |  |  |  |  |   
animate-app |  |  |  |  |   
choreograph-app |  |  |  |  |   
storyteller-app |  |  |  |  |   
dance-premium-app |  |  |  |  |   
draw-premium-app |  |  |  |  |   
music-premium-app |  |  |  |  |   
animate-premium-app |  |  |  |  |   
choreograph-premium-app |  |  |  |  |   
storyteller-premium-app |  |  |  |  |   
  
If you create reports for cost and utilization data for all listed applications at the same time, App Optimize API uses more than one unit of your concurrency limit in some projects. In particular, the shared project `common-project` receives 12 requests for cost and utilization data. Since this number exceeds the concurrency limit, 2 of data requests will fail.

To prevent this issue, the team could run reports for the standard versions of the applications first and then run reports for the premium version.

## What's next

  * To understand dimensions, metrics, and filters, see [About reports](https://docs.cloud.google.com/app-optimize/about-reports).
  * Explore other ways to manage reports: 
    * [Read a report's data](https://docs.cloud.google.com/app-optimize/read-report)
    * [List reports](https://docs.cloud.google.com/app-optimize/list-reports)
    * [Delete a report](https://docs.cloud.google.com/app-optimize/delete-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
