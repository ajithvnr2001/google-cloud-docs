---
url: https://docs.cloud.google.com/app-optimize/create-read-report/
title: Quickstart: Create and read a report \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:45.975402+00:00
---

# Quickstart: Create and read a report  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/create-read-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Guides ](https://docs.cloud.google.com/app-optimize/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and read a report

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Optimize API lets you generate reports on your Google Cloud costs and resource usage to help you optimize spending. In this quickstart, you create a report, monitor its generation, and read the report's data using the Google Cloud CLI, Python client library, or REST API.

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

To get the permissions that you need to create and read a report using this quickstart, ask your administrator to grant you the following IAM roles on your project with active resources: 

  * [App Optimize Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/appoptimize#appoptimize.admin) (`roles/appoptimize.admin`)
  * Viewer (`roles/viewer`) (or another role granting `billing.resourceCosts.get`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about permissions and roles required for App Optimize API, see [Access control with IAM](https://docs.cloud.google.com/app-optimize/access-control).

## Create a report

This example creates a report of the total spending within your chosen PROJECT_ID. The report breaks down the costs by each Google Cloud product used, such as Compute Engine and Cloud Storage, and by the specific SKU and location. The report covers the last three days of data.

To create the report resource, follow the instructions for your preferred method:

### gcloud

Use the `gcloud beta app-optimize reports create` command to create the report.
    
    
    gcloud beta app-optimize reports create REPORT_ID \
      --project=PROJECT_ID \
      --location=global \
      --dimensions=location,product_display_name,project,sku \
      --metrics=cost \
      --report-filter='hour >= now - duration("72h")' \
      --scopes=project=projects/PROJECT_ID
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REPORT_ID`: a unique ID for your new report—for example, `my-first-report`



The command waits for the report creation operation to complete and then returns the created report resource.

### Python

The following Python code uses `AppOptimizeClient.create_report()` to create a report.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    report_id = "REPORT_ID"
    
    # Create the App Optimize client and prepare a request for a new report
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    report = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[Report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.Report.html)(
        dimensions=['location', 'product_display_name', 'project', 'sku'],
        metrics=['cost'],
        filter='hour >= now - duration("72h")',
        scopes=[
            [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[Scope](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.Scope.html)(project=f"projects/{project_id}"),
        ],
    )
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[CreateReportRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.CreateReportRequest.html)(
        parent=f"projects/{project_id}/locations/global",
        report=report,
        report_id=report_id,
    )
    
    # Request the creation of the report and wait until the process is done
    operation = client.[create_report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_create_report)(request=request)
    print("Waiting for report creation operation to complete...")
    response = operation.result()
    print(response)
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REPORT_ID`: a unique ID for your new report—for example, `my-first-report`.



The `operation.result()` method waits for the report creation operation to complete.

### REST

Send an HTTP `POST` request to the REST API's `projects.locations.reports` resource path.

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
               "sku"
             ],
             "metrics": [
               "cost"
             ],
             "filter": "hour >= now - duration(\"72h\")"
           }' \
           "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports?report_id=REPORT_ID"
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `REPORT_ID`: a unique ID for your new report—for example, `my-first-report`

The API returns a Long-Running Operation (LRO) object, which represents the report generation process. Here is an example response:
    
    {
      "name": "projects/PROJECT_ID/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.appoptimize.v1beta.OperationMetadata"
      },
      "done": false
    }
    

The `"done": false` status indicates that the report is still being generated. Note the `OPERATION_ID` as you will use this in the next step.

  2. Because report generation can take time, you need to poll the LRO until it indicates that the generation process is complete and the report's data is ready for download.

To check the status of the generation process, send an HTTP `GET` request to the operation's resource name:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/operations/OPERATION_ID"
         

Examine the response. If `"done"` is `false`, wait 5 to 15 seconds and repeat this step. If `"done"` is `true`, then the report is ready.

The following is an example of a response when the operation is complete:
         
         {
           "name": "projects/PROJECT_ID/locations/global/operations/OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.appoptimize.v1beta.OperationMetadata"
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.appoptimize.v1beta.Report",
             "name": "projects/PROJECT_ID/locations/global/reports/REPORT_ID",
             "scopes": [
               {
                 "project": "projects/PROJECT_ID"
               }
             ],
             "dimensions": [
               "location",
               "product_display_name",
               "project",
               "sku"
             ],
             "metrics": [
               "cost"
             ],
             "filter": "hour >= now - duration(\"72h\")",
             "expireTime": "2026-02-04T22:05:05Z"
           }
         }
         




## Read the report data

To retrieve the report data, follow the instructions for your preferred method:

### gcloud

Use the following `gcloud beta app-optimize reports read` command to fetch the report's data.
    
    
    gcloud beta app-optimize reports read REPORT_ID \
      --project=PROJECT_ID \
      --location=global
    

### Python

The following Python code uses `AppOptimizeClient.read_report()` to fetch the report's data.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    report_id = "REPORT_ID"
    name = f"projects/{project_id}/locations/global/reports/{report_id}"
    
    # Create the App Optimize client and read your report's data
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[ReadReportRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.ReadReportRequest.html)(
            name=name,
    )
    result = client.[read_report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_read_report)(request=request)
    
    # Display the report's data
    print(result)
    

### REST

Once the LRO is complete, use the REST API's `:read` custom method:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{}' \
      "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports/REPORT_ID:read"
    

The response from the API contains the report data rows and column definitions. The following is an example of a successful response:
    
    
    {
      "rows": [
        [
          "us-central1",
          "Compute Engine",
          "projects/PROJECT_ID",
          "6EC2-384A-47D9",
          {
            "currency_code": "USD",
            "units": "25",
            "nanos": 750000000
          }
        ],
        [
          "us-central1",
          "Cloud Storage",
          "projects/PROJECT_ID",
          "9ADA-9ADC-2FBE",
          {
            "currency_code": "USD",
            "units": "5",
            "nanos": 100000000
          }
        ],
        [
          "europe-west1",
          "Compute Engine",
          "projects/PROJECT_ID",
          "6EC2-384A-47D9",
          {
            "currency_code": "USD",
            "units": "18",
            "nanos": 500000000
          }
        ],
        [
          "us-central1",
          "Compute Engine",
          "projects/PROJECT_ID",
          "F61D-4D51-AAFC",
          {
            "currency_code": "USD",
            "units": "12",
            "nanos": 200000000
          }
        ]
      ],
      "columns": [
        {
          "name": "location",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "product_display_name",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "project",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "sku",
          "type": "STRING",
          "mode": "NULLABLE"
        },
        {
          "name": "cost",
          "type": "RECORD",
          "mode": "NULLABLE",
          "columns": [
            {
              "name": "currency_code",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "name": "units",
              "type": "INT64",
              "mode": "NULLABLE"
            },
            {
              "name": "nanos",
              "type": "INT64",
              "mode": "NULLABLE"
            }
          ]
        }
      ],
      "next_page_token": ""
    }
    

Reports with many rows are paginated. To handle multiple pages, see [Read a report's data](https://docs.cloud.google.com/app-optimize/read-report).

To understand the values in the `cost` field, see [Interpreting cost metrics](https://docs.cloud.google.com/app-optimize/about-reports#interpreting_cost_metrics). For more information on the data and to understand its limitations, see [Understanding the data](https://docs.cloud.google.com/app-optimize/overview#understand-data).

## Clean up

App Optimize API automatically deletes your report 24 hours after it is created. To delete the report sooner, follow the instructions for your preferred method:

### gcloud

Use the `gcloud beta app-optimize reports delete` command to remove the report.
    
    
    gcloud beta app-optimize reports delete REPORT_ID \
      --project=PROJECT_ID \
      --location=global
    

### Python

The following code uses `AppOptimizeClient.delete_report()` to remove the report.
    
    
    from google.cloud import [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest)
    
    project_id = "PROJECT_ID"
    report_id = "REPORT_ID"
    
    name = f"projects/{project_id}/locations/global/reports/{report_id}"
    client = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[AppOptimizeClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html)()
    request = [appoptimize_v1beta](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest).[DeleteReportRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.types.DeleteReportRequest.html)(name=name)
    client.[delete_report](https://docs.cloud.google.com/python/docs/reference/google-cloud-appoptimize/latest/google.cloud.appoptimize_v1beta.services.app_optimize.AppOptimizeClient.html#google_cloud_appoptimize_v1beta_services_app_optimize_AppOptimizeClient_delete_report)(request=request)
    print(f"Deleted report: {name}")
    

### REST

Send an HTTP `DELETE` request to the report's resource endpoint:
    
    
    curl -X DELETE \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://appoptimize.googleapis.com/v1beta/projects/PROJECT_ID/locations/global/reports/REPORT_ID"
    

## What's next

  * Learn more [about reports](https://docs.cloud.google.com/app-optimize/about-reports).
  * Explore other ways to manage reports: 
    * [List reports](https://docs.cloud.google.com/app-optimize/list-reports).
    * [Get a report's metadata](https://docs.cloud.google.com/app-optimize/get-report-metadata).
    * [Delete a report](https://docs.cloud.google.com/app-optimize/delete-report).
  * See the [App Optimize API overview](https://docs.cloud.google.com/app-optimize/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
