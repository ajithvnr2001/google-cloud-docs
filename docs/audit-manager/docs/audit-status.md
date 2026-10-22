---
url: https://docs.cloud.google.com/audit-manager/docs/audit-status/
title: Get the status of an audit \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:41.129326+00:00
---

# Get the status of an audit  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/audit-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Get the status of an audit Stay organized with collections  Save and categorize content based on your preferences. 

You can get the status of an in-progress audit that you started using Audit Manager or Compliance Manager. Audits can take a long time to complete, and tracking this status helps you follow the progress of the audit while it runs.

## Before you begin

  * Ensure that you have one of the following IAM roles:

    * [Audit Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.admin) (`roles/auditmanager.admin`)
    * [Audit Manager Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.auditor) (`roles/auditmanager.auditor`)
    * [Compliance Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.viewer) (`roles/cloudsecuritycompliance.viewer`) (required if you're auditing a framework that you've created using Compliance Manager)
  * Identify the audit for which you want to get the status.




## Get the status of an in-progress audit

### Console

  1. In the Google Cloud console, go to the **View audits** page.

[Go to View audits](https://console.cloud.google.com/compliance/auditmanager/auditreports)

  2. On the **View assessments** page, you can view the current status of an in-progress audit or get more information about a completed audit.

  3. To view more information about the audit, click the link in the **Status** column.

  4. To view more information about the audit, click the name of the audit.




### gcloud

The [`gcloud audit-manager operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe) command describes an audit operation.

Before using any of the command data below, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organization`, `folder`, and `project`.
  * RESOURCE_ID: the resource ID of the organization, project or folder. For example: `8767234`.
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`.
  * AUDIT_OPERATION_ID: The unique ID for the in-progress operation that was included in the response body when you ran the audit. For example: `098234`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager operations describe AUDIT_OPERATION_ID \
        --RESOURCE_TYPE=RESOURCE_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager operations describe AUDIT_OPERATION_ID `
        --RESOURCE_TYPE=RESOURCE_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager operations describe AUDIT_OPERATION_ID ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --location=LOCATION

A successful response includes one of the following execution status types:

Status type | Description  
---|---  
`OPERATION_STATE_UNSPECIFIED` | An invalid state.  
`OPERATION_STATE_NOT_STARTED` | The audit report generation process has not yet started.  
`OPERATION_STATE_EVALUATION_IN_PROGRESS` | Audit Manager is evaluating the resources against compliance controls.  
`OPERATION_STATE_EVALUATION_DONE` | Audit Manager has completed compliance evaluation.  
`OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS` | Audit Manager is creating an audit report from the evaluated data.  
`OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE` | Audit Manager has completed the generation of the audit report.  
`OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS` | Audit Manager is uploading the audit report and evidence to the destination.  
`OPERATION_STATE_DONE` | The audit report generation process is completed.  
`OPERATION_STATE_FAILED` | The audit report generation process has failed.  
  
Each of the execution status types might provide any of the following additional information, when applicable:

Additional status | Description  
---|---  
`failure_reason` | If the audit assessment fails, this field provides the reason for the failure.  
`evaluation_percent_complete` | If evaluation has started, this field provides the percentage of the progress. When the process is yet to start, the field starts at `0`. When the process is concluded, the field is set to `100`.  
`report_generation_percent_complete` | If the report generation has started, this field provides percentage of the progress. When the process is yet to start, the field starts at `0`. When the process is concluded, the field is set to `100`.  
`report_uploading_percent_complete` | If the report uploading has started, this field provides percentage of the progress. When the process is yet to start, the field starts at `0`. When the process is concluded, the field is set to `100`.  
  
A successful gcloud response is similar to the following:
    
    
    done: true
    name: projects/PROJECT_ID/locations/LOCATION/operationDetails/AUDIT_OPERATION_ID
    response:
      '@type': type.googleapis.com/google.cloud.auditmanager.v1.AuditReport
      gcsUri: gs://testbucketauditmanager
    

### REST

Before using any of the request data, make the following replacements: 

  * RESOURCE_TYPE: the type of resource. Valid values are `organizations`, `folders`, and `projects`.
  * RESOURCE_ID: the resource ID of the organization, project or folder. For example: `8767234`.
  * LOCATION: the location of the Audit Manager API endpoint. For a list of available endpoints, see [Audit Manager locations](https://docs.cloud.google.com/audit-manager/docs/locations). For example: `us-central1`.
  * AUDIT_OPERATION_ID: The unique ID for the in-progress operation that was included in the response body when you ran the audit. For example: `098234`. 



HTTP method and URL: 
    
    
    GET https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION//operationDetails/AUDIT_OPERATION_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION//operationDetails/AUDIT_OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/LOCATION//operationDetails/AUDIT_OPERATION_ID" | Select-Object -Expand Content

A successful response includes one of the following execution status types:

Status type | Description  
---|---  
`OPERATION_STATE_UNSPECIFIED` | An invalid state.  
`OPERATION_STATE_NOT_STARTED` | The audit report generation process has not yet started.  
`OPERATION_STATE_EVALUATION_IN_PROGRESS` | Audit Manager is evaluating the resources against compliance controls.  
`OPERATION_STATE_EVALUATION_DONE` | Audit Manager has completed compliance evaluation.  
`OPERATION_STATE_EVIDENCE_REPORT_GENERATION_IN_PROGRESS` | Audit Manager is creating an audit report from the evaluated data.  
`OPERATION_STATE_EVIDENCE_REPORT_GENERATION_DONE` | Audit Manager has completed the generation of the audit report.  
`OPERATION_STATE_EVIDENCE_UPLOAD_IN_PROGRESS` | Audit Manager is uploading the audit report and evidence to the destination.  
`OPERATION_STATE_DONE` | The audit report generation process is completed.  
`OPERATION_STATE_FAILED` | The audit report generation process has failed.  
  
Each of the execution status types might provide any of the following additional information, when applicable:

Additional status | Description  
---|---  
`failure_reason` | If the audit assessment fails, this field provides the reason for the failure.  
`evaluation_percent_complete` | If evaluation has started, this field provides the percentage of the progress. When the process is yet to start, the field starts at `0`. When the process is concluded, the field is set to `100`.  
`report_generation_percent_complete` | If the report generation has started, this field provides percentage of the progress. When the process is yet to start, the field starts at `0`. When the process is concluded, the field is set to `100`.  
`report_uploading_percent_complete` | If the report uploading has started, this field provides percentage of the progress. When the process is yet to start, the field starts at `0`. When the process is concluded, the field is set to `100`.  
  
A successful REST response is similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operationDetails/AUDIT_OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.auditmanager.v1.AuditReport",
        "gcsUri": "gs://testbucketauditmanager"
      }
    }
    

When an audit report is completed and uploaded, a link to the report is returned.

## What's next

  * [View an audit report](https://docs.cloud.google.com/audit-manager/docs/view-audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
