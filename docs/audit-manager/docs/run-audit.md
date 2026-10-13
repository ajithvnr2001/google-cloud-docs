---
url: https://docs.cloud.google.com/audit-manager/docs/run-audit/
title: Run a compliance audit in Google Cloud \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:38.969316+00:00
---

# Run a compliance audit in Google Cloud  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/run-audit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Run a compliance audit in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Schedule and perform audits to collect the evidence that you require to assess your Google Cloud organization against [supported frameworks](https://docs.cloud.google.com/audit-manager/docs/overview#supported_compliance).

An audit is a long-running operation that might take a few hours. The duration depends on the number of resources within the audit scope, which is the organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), project, or folder you have previously enrolled.

You can schedule audits ([Preview](https://cloud.google.com/products/#product-launch-stages)) to run at a regular interval and specify a timeframe for a scheduled audit. You can only create a schedule for a specific framework and resource if an active or paused schedule doesn't already exist for the framework and resource combination.

## Before you begin

  * Ensure that you have one of the following IAM roles:

    * Audit Manager Admin (`roles/auditmanager.admin`)
    * Audit Manager Auditor (`roles/auditmanager.auditor`)
  * Ensure that your organization, project, or folder has been enrolled for auditing.




## Run an audit

### Console

  1. In the Google Cloud console, go to the **Run assessment** page in Audit Manager.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager/auditreports/create)

  2. In the **Choose resource and region** section, do the following:

     1. Select your organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), folder, or project that needs to be audited.

     2. Select the framework that you want to audit your resource against. For information about supported frameworks, see [Supported frameworks](https://docs.cloud.google.com/audit-manager/docs/overview#supported_compliance).

     3. Select the location where the audit assessment must be processed. For the list of supported locations, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations).

     4. Click **Next**.

  3. Select the framework that you want to audit your resource against and click **Next**. For information about supported frameworks, see [Supported frameworks](https://docs.cloud.google.com/audit-manager/docs/overview#supported_compliance).

  4. Optional: In the **View Assessment Plan** section, you can download an ODS file that contains information about the audit scope based on the framework that you selected. To download the file, click the link, and click **Next**.

  5. In the **Choose storage bucket** section, select a storage bucket where the audit report and evidence must be saved, and click **Done**. If your bucket is not listed, ask your administrator to [enroll your resource](https://docs.cloud.google.com/audit-manager/docs/enroll-resource) with your storage bucket.

  6. ([Preview](https://cloud.google.com/products/#product-launch-stages)) Optional: In the **Schedule** section, set any of the following:

     * How often to repeat the audit (daily, monthly, quarterly, or annually).

     * The time period to include in the audit. If you choose **Never ending** , the audit continues to run from the start date that you specify, until you manually stop it.

  7. To start the audit, click **Run Audit** or **Run Scheduled Audit**.

You can view the audit status on the **View assessments** page.




### gcloud

#### Optional: Generate an audit assessment

Before running an actual audit, you can generate an audit assessment (or scope) that includes a detailed task breakdown for the audit based on the compliance framework you chose.

The [`gcloud audit-manager audit-scopes generate`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-scopes/generate) command generates an audit scope.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource, which can be an organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), folder, or project. For example: `folders` or `projects`.
  * RESOURCE_ID: the resource ID of the organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), project or folder. For example: `8767234`.
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`.
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in Audit Manager.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.
  * OUTPUT_DIRECTORY: the directory where the output must be stored. For example: `reports`.
  * OUTPUT_FILENAME: the name of the output file. Don't include the file extension in the filename. For example:`scopeReport`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-scopes generate \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION \
        --compliance-framework=FRAMEWORK \
        --report-format=AUDIT_REPORT_FORMAT \
        --output-directory=OUTPUT_DIRECTORY \
        --output-file-name=OUTPUT_FILENAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-scopes generate `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION `
        --compliance-framework=FRAMEWORK `
        --report-format=AUDIT_REPORT_FORMAT `
        --output-directory=OUTPUT_DIRECTORY `
        --output-file-name=OUTPUT_FILENAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-scopes generate ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION ^
        --compliance-framework=FRAMEWORK ^
        --report-format=AUDIT_REPORT_FORMAT ^
        --output-directory=OUTPUT_DIRECTORY ^
        --output-file-name=OUTPUT_FILENAME

#### Run an on-demand audit

You can't schedule an audit ([Preview](https://cloud.google.com/products/#product-launch-stages)) or run organization-level reports ([Preview](https://cloud.google.com/products/#product-launch-stages)) using gcloud CLI.

The [`gcloud audit-manager audit-reports generate`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/audit-reports/generate) command runs an audit.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource, which can be an organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), folder, or project. For example: `folders` or `projects`.
  * RESOURCE_ID: the resource ID of the organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), project or folder. For example: `8767234`.
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`.
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in Audit Manager.
  * BUCKET_URI: the URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-reports generate \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION \
        --compliance-framework=FRAMEWORK \
        --report-format=AUDIT_REPORT_FORMAT \
        --gcs-uri=BUCKET_URI

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-reports generate `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION `
        --compliance-framework=FRAMEWORK `
        --report-format=AUDIT_REPORT_FORMAT `
        --gcs-uri=BUCKET_URI

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager audit-reports generate ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION ^
        --compliance-framework=FRAMEWORK ^
        --report-format=AUDIT_REPORT_FORMAT ^
        --gcs-uri=BUCKET_URI

You should receive a response similar to the following:
    
    
    done: false
    name: projects/10398413/locations/987234/operations/operation-1726842525305-6228ddb4dca96-78a6db59-f9dd9a24
    
    

### REST

#### Optional: Generate an audit assessment

Before running an actual audit, you can generate an audit assessment (or scope) that includes a detailed task breakdown for the audit based on the compliance framework you chose.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource, which can be an organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), folder, or project. For example: `folders` or `projects`.
  * RESOURCE_ID: the resource ID of the organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), project or folder. For example: `8767234`.
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`.
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in Audit Manager.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.



HTTP method and URL: 
    
    
    POST https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditScopesReport:generate

Request JSON body: 
    
    
    
    {
      "compliance_framework" : "FRAMEWORK"
      "report_format" : "AUDIT_REPORT_FORMAT"
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditScopesReport:generate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditScopesReport:generate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    
      "scope_report_contents" : "980u43nrf090834uhbkfehf......"
      "name" : "folders/8767234/locations/us-west"
    }
    
    

The response has the following information:

The `scope_reports_contents` field is the byte format of the contents, which must be converted to ODF format before review.

  * `name`: A unique string identifier of the applicable resource.



#### Run an on-demand audit

You can't schedule an audit run ([Preview](https://cloud.google.com/products/#product-launch-stages)) using REST APIs.

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource, which can be an organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), folder, or project. For example: `folders` or `projects`.
  * RESOURCE_ID: the resource ID of the organization ([Preview](https://cloud.google.com/products/#product-launch-stages)), project or folder. For example: `8767234`.
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`.
  * FRAMEWORK: the ID of the framework to audit against. For example: `builtin-cis-v8`. To find the ID of a framework, see the **View assessments** page in Audit Manager.
  * BUCKET_URI: the URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`.
  * AUDIT_REPORT_FORMAT: the format of the output audit report. Only ODF format is supported: `AUDIT_REPORT_FORMAT_ODF`.



HTTP method and URL: 
    
    
    POST https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditReport:generate

Request JSON body: 
    
    
    
    {
      "destination" : {
        "gcs_uri" : "BUCKET_URI"
      },
      "compliance_framework" : "FRAMEWORK"
      "report_format" : "AUDIT_REPORT_FORMAT"
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditReport:generate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION/auditReport:generate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "organizations/834/projects/10398413/locations/987234/operations/098234",
      "done": false
    }
    
    

The response has the following information:

  * `name`: A unique string identifier of the audit assessment operation request. This identifier is used to track the progress of the audit assessment process. For example: `operation/098234`.
  * `done`: A boolean flag that is set to `false` that indicates that the process has been triggered. This is set to `true` when the audit assessment is completed.



## Update scheduled audits

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can pause, resume, and stop recurring audits. If you want to change the schedule, you must delete the existing scheduled audit, and then create a new scheduled audit.

### Console

  1. In the Google Cloud console, go to the **Audit management** page in Audit Manager.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager/manageaudits)

  2. In the **Schedules** tab, find the scheduled audit that you want to update.

  3. Do one of the following:

     * To pause an audit schedule, click pause **Pause schedule**.

     * To restart an audit that you paused, click play_circle_filled **Resume schedule**.

     * To delete a scheduled audit, click stop **Stop schedule**.




## What's next

  * [Get the status of an audit](https://docs.cloud.google.com/audit-manager/docs/audit-status).
  * [Troubleshoot run audit issues](https://docs.cloud.google.com/audit-manager/docs/troubleshoot-run-audit-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
