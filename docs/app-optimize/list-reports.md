---
url: https://docs.cloud.google.com/app-optimize/list-reports/
title: List reports \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:41.552347+00:00
---

# List reports  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/list-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

#  List reports Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can list reports in your Google Cloud project to identify ones that you want to read, or ones that you want to delete before the expiry date.

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

To get the permissions that you need to list a project's report resources, ask your administrator to grant you the [App Optimize Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/appoptimize#appoptimize.viewer) (`roles/appoptimize.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List reports

The list operation returns the report metadata, including the resource name, scope, dimensions, metrics, and expiration time for each report. To download the requested cost and usage information, you need to [read the report's data](https://docs.cloud.google.com/app-optimize/read-report).

To list reports in a project, follow the instructions for your preferred method:

### gcloud

Use the `gcloud beta app-optimize reports list` command to list the reports in a project.
    
    
    gcloud beta app-optimize reports list \
      --project=PROJECT_ID \
      --location=global
    

Replace `PROJECT_ID` with the ID of the Google Cloud project that owns the report resources that you want to list.

The `gcloud` command handles pagination automatically, returning all requested resources.

### Python

The following Python code uses `AppOptimizeClient.list_reports()` to display a list of reports in a project.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    
    # Create the App Optimize client and request the project's reports
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[ListReportsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.ListReportsRequest.html)(
        parent=f"projects/{project_id}/locations/global"
    )
    page_result = client.[list_reports](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_list_reports)(request=request)
    
    # Iterate over the list of reports and display each one
    for response in page_result:
        print(response)
    

Replace `PROJECT_ID` with the ID of the Google Cloud project that owns the report resources that you want to list.

The client library handles pagination automatically, yielding results from the iterator.

### REST

Use the following [`curl`](https://curl.se) command to list the reports for a project:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports?pageSize=PAGE_SIZE"
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resources that you want to list.
  * `PAGE_SIZE`: the maximum number of reports to return per page. If omitted, the API uses a default value. The server might return fewer reports than requested.



If the request is successful, the API returns a JSON response containing a list of report resources. Here is an example successful call response:
    
    
    {
      "reports": [
        {
          "name": "projects/PROJECT_ID/locations/global/reports/my-first-report",
          "dimensions": [
            "location",
            "product_display_name",
            "project",
            "sku"
          ],
          "scopes": [
            {
              "project": "projects/PROJECT_ID"
            }
          ],
          "filter": "hour \u003e= now - duration(\"168h\")",
          "expireTime": "2026-02-05T18:30:39.907639266Z",
          "metrics": [
            "cost"
          ]
        },
        {
          "name": "projects/PROJECT_ID/locations/global/reports/my-second-report",
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
          "filter": "hour \u003e= now - duration(\"168h\")",
          "expireTime": "2026-02-05T18:50:25.273833857Z",
          "metrics": [
            "cost",
            "cpu_mean_utilization"
          ]
        }
      ]
    }
    

The `reports` array contains the metadata for each report. If the request is unsuccessful, review the error message returned by the API.

If the response includes a `nextPageToken` string, it means there are more reports to retrieve.

Check the response for a `nextPageToken` field. If the token exists, run the following `curl` command to retrieve the next page, including the `pageToken` query parameter. You can continue to use the `pageSize` parameter.
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports?pageToken=NEXT_PAGE_TOKEN&pageSize=PAGE_SIZE"
    

Replace the following:

  * `NEXT_PAGE_TOKEN`: the value of the `nextPageToken` received in the previous response.
  * `PAGE_SIZE`: the page size you want for this request.



Repeat this process until the response no longer contains a `nextPageToken`, which indicates that you have retrieved all reports.

## What's next

  * [Get a report's metadata](https://docs.cloud.google.com/app-optimize/get-report-metadata)
  * [Read a report's data](https://docs.cloud.google.com/app-optimize/read-report)
  * [Delete a report](https://docs.cloud.google.com/app-optimize/delete-report)
  * [App Optimize API overview](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
