---
url: https://docs.cloud.google.com/app-optimize/get-report-metadata/
title: Get a report's metadata \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:14:41.245328+00:00
---

# Get a report's metadata  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/get-report-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

#  Get a report's metadata Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To inspect a report's settings, such as its scope and metrics, or to check its expiry time, use App Optimize API to get the report's metadata.

This API request does not return the actual data rows within the report. To download this information, you need to [read the report's data](https://docs.cloud.google.com/app-optimize/read-report).

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

To get the permissions that you need to read a report's metadata, ask your administrator to grant you the [App Optimize Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/appoptimize#appoptimize.viewer) (`roles/appoptimize.viewer`) IAM role on the project that owns the report resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Get report metadata

To retrieve the metadata for a report, follow the instructions for your preferred method:

### gcloud

Use the `gcloud beta app-optimize reports describe` command to get a report's metadata.
    
    
    gcloud beta app-optimize reports describe REPORT_ID \
      --project=PROJECT_ID \
      --location=global
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resource that you want to retrieve.
  * `REPORT_ID`: the ID of the report to retrieve. This ID was specified when the report was created, and can be obtained by [listing reports](https://docs.cloud.google.com/app-optimize/list-reports).



### Python

The following Python code uses `AppOptimizeClient.get_report()` to get a report's metadata.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    report_id = "REPORT_ID"
    name = f"projects/{project_id}/locations/global/reports/{report_id}"
    
    # Create the App Optimize client and request the report's metadata
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[GetReportRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.GetReportRequest.html)(name=name)
    response = client.[get_report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_get_report)(request=request)
    
    # Display the metadata
    print(response)
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resource that you want to retrieve.
  * `REPORT_ID`: the ID of the report to retrieve. This ID was specified when the report was created, and can be obtained by [listing reports](https://docs.cloud.google.com/app-optimize/list-reports).



### REST

Use the following [`curl`](https://curl.se) command to get the report metadata:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports/REPORT_ID"
    

Replace the following:

  * `PROJECT_ID`: the ID of the Google Cloud project that owns the report resource that you want to retrieve.
  * `REPORT_ID`: the ID of the report to retrieve. This ID was specified when the report was created, and can be obtained by [listing reports](https://docs.cloud.google.com/app-optimize/list-reports).



If the request is successful, the API returns a JSON response containing the report metadata. Here is an example successful response, including the dimension and metric selected, the project scope, and when the report is scheduled to expire:
    
    
    {
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
    

## What's next

  * [Read a report's data](https://docs.cloud.google.com/app-optimize/read-report)
  * [List reports](https://docs.cloud.google.com/app-optimize/list-reports)
  * [Delete a report](https://docs.cloud.google.com/app-optimize/delete-report)
  * [App Optimize API overview](https://docs.cloud.google.com/app-optimize/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
