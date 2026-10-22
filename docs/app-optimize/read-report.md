---
url: https://docs.cloud.google.com/app-optimize/read-report/
title: Read a report's data \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:40.887236+00:00
---

# Read a report's data  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/read-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

#  Read a report's data Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After App Optimize API creates a report, you fetch the report's cost and utilization data. This operation downloads this information as columns and rows, structured according to the dimensions and metrics you specified when you requested your report.

This API request is different from getting [a report's metadata](https://docs.cloud.google.com/app-optimize/get-report-metadata), which only returns the report's configuration settings.

## Before you begin

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

To get the permissions that you need to read a report's data, ask your administrator to grant you the [App Optimize Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/appoptimize#appoptimize.viewer) (`roles/appoptimize.viewer`) IAM role on the project that owns the report resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Read report data

To read data from a completed report, follow the instructions for your preferred method:

### gcloud

Use the `gcloud beta app-optimize reports read` command to fetch a report's data.
    
    
    gcloud beta app-optimize reports read REPORT_ID \
      --project=PROJECT_ID \
      --location=global
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resource that you want to read.
  * `REPORT_ID`: the ID of the report to read. This ID was specified when the report was created, and can be obtained by [listing reports](https://docs.cloud.google.com/app-optimize/list-reports).



The `gcloud` command handles pagination automatically, returning all requested resources.

To understand the values in the `cost` field, see [Interpreting cost metrics](https://docs.cloud.google.com/app-optimize/about-reports#interpreting_cost_metrics). For more information on the data and to understand its limitations, see [Understanding the data](https://docs.cloud.google.com/app-optimize/overview#understand-data).

### Python

The following Python code uses `AppOptimizeClient.read_report()` to read a report's data.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    report_id = "REPORT_ID"
    
    # Create the App Optimize client and read a report's data
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[ReadReportRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.ReadReportRequest.html)(
        name=f"projects/{project_id}/locations/global/reports/{report_id}"
    )
    result = client.[read_report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_read_report)(request=request)
    
    # Display the report data
    print(result)
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resource that you want to read.
  * `REPORT_ID`: the ID of the report to read. This ID was specified when the report was created, and can be obtained by [listing reports](https://docs.cloud.google.com/app-optimize/list-reports).



The client library handles pagination automatically, yielding results from the iterator.

To understand the values in the `cost` field, see [Interpreting cost metrics](https://docs.cloud.google.com/app-optimize/about-reports#interpreting_cost_metrics). For more information on the data and to understand its limitations, see [Understanding the data](https://docs.cloud.google.com/app-optimize/overview#understand-data).

### REST

Send an HTTP `POST` request to the REST API's `:read` custom method.

  1. Use the following [`curl`](https://curl.se) command to send that request to read the first page of report data:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{"pageSize": PAGE_SIZE}' \
           "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports/REPORT_ID:read"
         

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resource that you want to read.
     * `REPORT_ID`: the ID of the report to read. This ID was specified when the report was created, and can be obtained by [listing reports](https://docs.cloud.google.com/app-optimize/list-reports).
     * `PAGE_SIZE`: the maximum number of rows to return per page. The server returns a maximum of 1,000 rows per page, even if you specify a larger value. Responses are also subject to a 10 MB size limit, so fewer rows might be returned to stay within that limit. If `pageSize` is omitted, a default size is used.
  2. If the request is successful, the API returns a JSON response containing the report schema and rows. Here's an example successful response:
         
         {
           "rows": [
             [
               "//apphub.googleapis.com/projects/123456789/locations/us-central1/applications/my-app-1",
               {
                 "currency_code": "USD",
                 "units": "106",
                 "nanos": 321590000
               }
             ],
             [
               "//apphub.googleapis.com/projects/123456789/locations/us-central1/applications/my-app-2",
               {
                 "currency_code": "USD",
                 "units": "797",
                 "nanos": 641691000
               }
             ]
           ],
           "columns": [
             {
               "name": "application",
               "type": "STRING"
             },
             {
               "name": "cost",
               "type": "RECORD",
               "columns": [
                 {
                   "name": "currency_code",
                   "type": "STRING"
                 },
                 {
                   "name": "units",
                   "type": "INT64"
                 },
                 {
                   "name": "nanos",
                   "type": "INT64"
                 }
               ]
             }
           ],
           "nextPageToken": "AABBCCddeeffGGHHiiJJkkLL"
         }
         

To understand the values in the `cost` field, see [Interpreting cost metrics](https://docs.cloud.google.com/app-optimize/about-reports#interpreting_cost_metrics). For more information on the data and to understand its limitations, see [Understanding the data](https://docs.cloud.google.com/app-optimize/overview#understand-data).

  3. If the response includes a `nextPageToken` field, the report contains additional rows. To retrieve the next page of results, make another `POST` request that includes this token in the `pageToken` field of the JSON body:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{"pageToken": "NEXT_PAGE_TOKEN", "pageSize": PAGE_SIZE}' \
           "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports/REPORT_ID:read"
         

Replace the following:

     * `NEXT_PAGE_TOKEN`: the value of the `nextPageToken` received in the previous response.
     * `PAGE_SIZE`: the maximum number of rows to return per page. While you can change this value between page requests, the server-side limits still apply.

Repeat this process until the response no longer contains a `nextPageToken`, indicating that you have retrieved all report data.




## What's next

  * [Get a report's metadata](https://docs.cloud.google.com/app-optimize/get-report-metadata)
  * [List reports](https://docs.cloud.google.com/app-optimize/list-reports)
  * [Delete a report](https://docs.cloud.google.com/app-optimize/delete-report)
  * [App Optimize API overview](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
