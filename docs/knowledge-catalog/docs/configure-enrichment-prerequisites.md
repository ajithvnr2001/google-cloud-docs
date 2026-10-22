---
url: https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites/
title: Configure prerequisites for enrichment tasks \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:41.049051+00:00
---

# Configure prerequisites for enrichment tasks  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-prerequisites/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Configure prerequisites for enrichment tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Knowledge Studio gated preview**  
Knowledge Studio is currently available as a gated preview. To view the context graph, create context sets, and run enrichment workflows, you must first request allowance for your organization.   
  
[Request preview access](https://docs.google.com/forms/d/e/1FAIpQLScw1O38BmcLIvqL1ZvpybJsLGO_Dmuq0a5RrCJIqW11iljsKQ/viewform)

Before you can create enrichment tasks in Knowledge Studio, you might need to configure several underlying infrastructure components depending on your security architecture and target data sources.

This guide describes how to configure customer-managed service accounts, third-party authentication providers, and Cloud Storage buckets, and Cloud Logging views.

The following table describes the prerequisite configurations and when you need to configure them:

Configuration feature | When to configure  
---|---  
Google Cloud APIs | Required. You must enable the underlying Google Cloud APIs to run enrichment workflows.  
Customer-managed service account | You want to restrict read and write access on your target datasets.  
User Identity and Access Management (IAM) roles | You need to grant workflow managers and reviewers permissions to generate and approve metadata.  
Third-party auth providers | You're connecting to third-party knowledge sources (such as Microsoft SharePoint, Atlassian Confluence, or GitHub).  
Cloud Storage buckets | You're ingesting unstructured business context (such as PDFs, Markdown, and CSV) and evaluation datasets.  
Evaluation datasets | You want to provide seed queries and benchmark datasets to actively track agent accuracy.  
Agent Traces for self-learning | You want the enrichment agent to automatically analyze downstream Gemini Enterprise agent interactions.  
Data profiling and data insights | Recommended. You want to improve enrichment quality by generating statistical profiles and baseline AI insights on frequently used tables.  
  
## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataplex, Data Lineage, BigQuery, Cloud Storage, and IAM Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,datalineage.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Dataplex, Data Lineage, BigQuery, Cloud Storage, and IAM Credentials APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,datalineage.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required APIs details

To configure and run enrichment tasks, the enabled APIs perform the following functions:

API Name | Service Identifier | Purpose in Enrichment workflows  
---|---|---  
Dataplex API | `dataplex.googleapis.com` | Primary control plane API. Manages `EnrichmentTask`, `EnrichmentRun`, context sets, Change Requests, and the EnrichmentChatService.  
BigQuery API | `bigquery.googleapis.com` | Required for scanning table schemas, ingesting SQL execution history, and querying BigQuery agent analytics trace tables.  
Cloud Storage API | `storage.googleapis.com` | Required for ingesting evaluation sets and managing evaluation dataset samples.  
IAM Service Account Credentials API | `iamcredentials.googleapis.com` | Required for securely authenticating the execution agent and granting Short-Lived Credentials (SLC) during tasks.  
  
## Configure a customer-managed service account

Enrichment tasks use a customer-managed service account to run operations. This lets you restrict read and write access on your target datasets.

  1. Create the service account.

To create a service account, you must be a **Project Owner** (`roles/owner`) or **Editor** (`roles/editor`), or have the **Service Account Admin** role (`roles/iam.serviceAccountAdmin`).

A dedicated service account isolates your enrichment operations, letting you grant only the specific read and write permissions needed for these tasks without affecting other workloads.

To create a service account, follow these steps:

### Google Cloud CLI

To create a service account, use the [`gcloud iam service-accounts create` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
        --description="Service Account for Dataplex Knowledge Catalog enrichment agent execution" \
        --display-name="Knowledge Catalog enrichment agent SA"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME `
        --description="Service Account for Dataplex Knowledge Catalog enrichment agent execution" `
        --display-name="Knowledge Catalog enrichment agent SA"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts create SERVICE_ACCOUNT_NAME ^
        --description="Service Account for Dataplex Knowledge Catalog enrichment agent execution" ^
        --display-name="Knowledge Catalog enrichment agent SA"

### REST

Before using any of the request data, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID

HTTP method and URL: 
    
    POST https://iam.googleapis.com/v1/projects/TARGET_PROJECT_ID/serviceAccounts

Request JSON body: 
    
    {
       "accountId": "SERVICE_ACCOUNT_NAME",
       "serviceAccount": {
        "displayName": "Knowledge Catalog enrichment agent SA",
        "description": "Service Account for Dataplex Knowledge Catalog enrichment agent execution"
       }
      }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/projects/TARGET_PROJECT_ID/serviceAccounts"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v1/projects/TARGET_PROJECT_ID/serviceAccounts" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

  2. Grant the necessary resource-level IAM roles to the execution service account on your target scopes:

     * **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) and **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`): Enables the agent to inspect catalog metadata, create staged working entries, and manually publish approved enrichments.
     * _(Optional)_ **Dataplex Workflow Approver** (`roles/dataplex.workflowApprover`): Required only if you enable **Auto-publish** on your task. Enables the agent to automatically approve and publish its own metadata change requests.
     * **BigQuery Data Viewer** (`roles/bigquery.dataViewer`): Enables the agent to read table schemas, column metadata, and agent analytics trace tables.

**Note** : The following code samples grant these roles at the **project level** for ease of setup. For production systems, we strongly recommend granting these roles securely at the resource level on your specific target datasets.

To grant these standard roles, follow these steps:

To add an IAM policy binding to a project, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/dataplex.catalogEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/bigquery.dataViewer"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/dataplex.catalogEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/bigquery.dataViewer"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/dataplex.catalogEditor"
    
    gcloud projects add-iam-policy-binding TARGET_PROJECT_ID ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/bigquery.dataViewer"

  3. Grant users permission to impersonate the service account by granting them the **Service Account User** role (`roles/iam.serviceAccountUser`):

Users who create the enrichment tasks in the console must have this permission so that they can specify and attach this service account to the task.

To grant users the Service Account User role, follow these steps:

To add an IAM policy binding to a service account, use the [`gcloud iam service-accounts add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID
     * `USER_EMAIL`: the user's email address

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com \
        --member="user:USER_EMAIL@domain.com" \
        --role="roles/iam.serviceAccountUser"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com `
        --member="user:USER_EMAIL@domain.com" `
        --role="roles/iam.serviceAccountUser"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com ^
        --member="user:USER_EMAIL@domain.com" ^
        --role="roles/iam.serviceAccountUser"

  4. Allow the internal Knowledge Catalog service agent to impersonate this service account by granting it the Service Account Token **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`):

This lets the underlying Knowledge Catalog service assume this dedicated service account's identity and its restricted permissions when it runs the background enrichment operations on your behalf.

To authorize the agent to assume the service account identity, follow these steps:

To add an IAM policy binding to a service account, use the [`gcloud iam service-accounts add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID
     * `TARGET_PROJECT_NUMBER`: your Google Cloud project number

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com \
        --member="serviceAccount:service-TARGET_PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
        --role="roles/iam.serviceAccountTokenCreator"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com `
        --member="serviceAccount:service-TARGET_PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" `
        --role="roles/iam.serviceAccountTokenCreator"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com ^
        --member="serviceAccount:service-TARGET_PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" ^
        --role="roles/iam.serviceAccountTokenCreator"




## Grant required IAM roles to users

To ensure that your team can manage enrichment workflows and review AI-generated proposals, grant the appropriate IAM roles to your users. For instructions on how to grant these roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Workflow managers** (such as data stewards) who create, configure, and monitor tasks require the following roles:

  * **Dataplex DataScan Editor** (`roles/dataplex.dataScanEditor`) or **Dataplex Editor** (`roles/dataplex.editor`): allows users to create, modify, trigger, and cancel enrichment tasks.
  * **Service Account User** (`roles/iam.serviceAccountUser`) on the customer-managed service account: required to attach the service account as the task's execution identity.



**Change reviewers** (such as domain owners or subject matter experts) who inspect, approve, and publish AI-generated metadata proposals to the catalog require the following roles:

  * **Dataplex Catalog Editor** (`roles/dataplex.catalogEditor`) and **Dataplex Catalog Viewer** (`roles/dataplex.catalogViewer`): required to open change requests, inspect side-by-side proposal diffs, and edit descriptions inline.
  * **Dataplex Workflow Approver** (`roles/dataplex.workflowApprover`): required to approve and publish change requests to the live catalog.
  * **Dataplex DataScan Viewer** (`roles/dataplex.dataScanViewer`) or **Dataplex Viewer** (`roles/dataplex.viewer`): required to review per-proposal confidence scores, test failure diagnosis, and downstream evaluation scorecards.



## Configure third-party auth providers

When connecting the enrichment agent to third-party knowledge sources (such as Microsoft SharePoint, Atlassian Confluence, or GitHub), you must configure an Auth Provider using Google Cloud's Agent Identity service.

Agent Identity acts as a secure credentials manager that encrypts your third-party tokens inside your project, ensuring that human operators never have to handle raw client secrets during task execution.

For step-by-step instructions on generating the required tokens and configuring the auth provider for specific external platforms, see [Configure external connectors for enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/configure-enrichment-connectors).

### Set up IAM permissions for auth providers

To allow the enrichment agent to securely retrieve your auth provider credentials dynamically during an active run, you must grant the **Agent Identity Admin** (`roles/agentidentity.admin`) role to the managed **Knowledge Catalog Service Agent** (`service-<var>PROJECT_NUMBER</var>@gcp-sa-dataplex.iam.gserviceaccount.com`). You can grant this role at either the auth provider resource level or the project level.

Additionally, the human user who attaches the auth provider to the task in the Google Cloud console must have the `agentidentity.authProviders.get` permission (included in **Agent Identity Viewer** (`roles/agentidentity.viewer`)) on the auth provider.

## Prepare Cloud Storage buckets

Cloud Storage serves as the primary file-based staging, context ingestion, and artifact export layer for knowledge enrichment workflows.

You can configure the agent to ingest files from one or more input buckets to ground its reasoning in your enterprise domain knowledge. Supported context types include:

  * **Domain documentation and data dictionaries** : Markdown, plain text, PDF, HTML, or CSV files containing table definitions, business glossaries, Standard Operating Procedures (SOPs), data pipeline architectures, or column naming guidelines.

  * **Evaluation datasets** : JSONL or CSV files storing seed queries and held-out validation query sets. For more information, see Format evaluation datasets.

  * **Reference SQL and transformation scripts** : Saved SQL scripts, dbt model definitions, or ETL transformation logic that provide contextual signals regarding table join patterns and business calculations.




When configured, the enrichment agent can also export structured bundles and run artifacts to an output bucket. Supported output artifacts include:

  * **Detailed evaluation reports** : Comprehensive scorecards showing per-query accuracy deltas, test failure diagnosis, and confidence distribution metrics.



To ensure the enrichment agent can work out of the bucket, make sure that your execution service account has the necessary permissions.

  * Grant the Object Viewer role (`roles/storage.objectViewer`) on the input buckets so the agent can read stages documents and configuration files.
  * (Optional) Grant the Object Creator role (`roles/storage.objectCreator`) on the output bucket if you want the agent to save execution artifacts and validation logs.



To grant the service account access to the Cloud Storage buckets, follow these steps:

To add an IAM policy binding to a storage bucket, use the [`gcloud storage buckets add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

  * `CUSTOMER_BUCKET`: the name of your Cloud Storage bucket
  * `SERVICE_ACCOUNT_NAME`: the name of your service account
  * `TARGET_PROJECT_ID`: your Google Cloud project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud storage buckets add-iam-policy-binding gs://CUSTOMER_BUCKET \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/storage.objectViewer"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud storage buckets add-iam-policy-binding gs://CUSTOMER_BUCKET `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/storage.objectViewer"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud storage buckets add-iam-policy-binding gs://CUSTOMER_BUCKET ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/storage.objectViewer"

## Format evaluation datasets

Enrichment workflows can automatically extract information without examples. However, providing evaluation datasets lets the agent test itself and improve its accuracy.

You can provide two types of datasets:

  * **Curation set** : A list of sample user questions and the expected SQL queries. The agent uses this list to practice and write better table summaries.

  * **Evaluation set** : A separate list of questions used to grade the agent's performance. If the agent performs poorly, this evaluation set prevents poor updates from being published to your catalog.




Alternatively, you can provide a single consolidated dataset. The enrichment service automatically partitions the data into a curation set and an evaluation set.

### Dataset schema requirements

Evaluation datasets must be formatted as JSONL files and stored in Cloud Storage. Each line in the file must contain a natural language question paired with the expected ground truth SQL query.

Ensure that your file matches the evaluation dataset schema prescribed by the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-dataset). The following table shows the accepted formatting fields:

Field name | Type | Description  
---|---|---  
`display_name` | `STRING` | Optional. An identifier or name for the evaluation request.  
`evaluation_request.prompt.text` | `STRING` | The natural language question or user prompt.  
`evaluation_request.golden_response.candidate` | `STRING` | Identifies the golden response. Set to `golden`.  
`evaluation_request.golden_response.text` | `STRING` | The ground truth, validated SQL query that answers the question. The scorer runs this SQL against the data.  
  
The following snippet shows a valid `.jsonl` evaluation file:
    
    
    {"display_name": "revenue-2026", "evaluation_request": {"prompt": {"text": "What is total revenue for customer C100 in 2026?"}, "golden_response": {"candidate": "golden", "text": "SELECT SUM(amount) FROM `project.dataset.orders` WHERE customer_id = 'C100' AND EXTRACT(YEAR FROM order_date) = 2026;"}}}
    {"display_name": "monthly-subscribers", "evaluation_request": {"prompt": {"text": "List active subscribers on monthly billing"}, "golden_response": {"candidate": "golden", "text": "SELECT user_id, email FROM `project.dataset.subscriptions` WHERE status = 'ACTIVE' AND plan_type = 'MONTHLY';"}}}
    

For detailed guidance on crafting high-quality evaluation datasets, see the [ Gemini Enterprise Agent Platform documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview).

## Configure agent traces for self-learning

To let the enrichment agent automatically analyze downstream Gemini Enterprise agent interactions (or custom Gemini Enterprise Agent Platform applications), you can optionally provide it with read access to your application's interaction traces.

Ingesting these traces enables the agent to perform _trajectory mining_. The agent discovers where downstream agents struggled due to missing context, clusters frequent user questions into high-impact query classes, and automatically curates the exact table summaries, column semantics, and business glossary terms needed to resolve those gaps.

Depending on your enterprise architecture, choose one of the following two setup methods:

  * **Direct Logging using scoped log views** : Create a log view restricted to only the application's telemetry to grant least-privilege read access. Recommended.
  * **BigQuery agent analytics** : Grant read access to an exported BigQuery dataset if your organization natively routes interaction logs to a BigQuery log sink.



### Direct Logging using scoped log views (Recommended)

When interaction logging is enabled for an application, execution logs stream directly into Logging. To follow the principle of least privilege, create a dedicated Log View restricted to the specific application and grant the execution service account read access exclusively on that view.

  1. Create a scoped log view to isolate the logs. This ensures the enrichment service only reads telemetry from specific configured applications (for example, by filtering on `resource.type="aiplatform.googleapis.com/Agent"`), preventing unauthorized access to your broader Cloud logs.

### gcloud CLI

To create a scoped log view, use the [`gcloud logging views create` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/views/create):

Before using any of the command data below, make the following replacements: 

     * `LOG_VIEW_NAME`: the name of your log view
     * `YOUR_GEMINI_ENTERPRISE_APP_ID`: your Gemini Enterprise application ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views create LOG_VIEW_NAME \
        --location=global \
        --bucket=_Default \
        --log-filter='resource.type="aiplatform.googleapis.com/Agent" AND resource.labels.agent_id="YOUR_GEMINI_ENTERPRISE_APP_ID"'

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views create LOG_VIEW_NAME `
        --location=global `
        --bucket=_Default `
        --log-filter='resource.type="aiplatform.googleapis.com/Agent" AND resource.labels.agent_id="YOUR_GEMINI_ENTERPRISE_APP_ID"'

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). **Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    gcloud logging views create LOG_VIEW_NAME ^
        --location=global ^
        --bucket=_Default ^
        --log-filter='resource.type="aiplatform.googleapis.com/Agent" AND resource.labels.agent_id="YOUR_GEMINI_ENTERPRISE_APP_ID"'

### REST

Before using any of the request data, make the following replacements: 

     * `LOG_VIEW_NAME`: the name of your log view
     * `TARGET_PROJECT_ID`: your Google Cloud project ID
     * `YOUR_GEMINI_ENTERPRISE_APP_ID`: your Gemini Enterprise application ID

HTTP method and URL: 
    
    POST https://logging.googleapis.com/v2/projects/TARGET_PROJECT_ID/locations/global/buckets/_Default/views?viewId=LOG_VIEW_NAME

Request JSON body: 
    
    {
     "filter": "resource.type=\"aiplatform.googleapis.com/Agent\" AND resource.labels.agent_id=\"YOUR_GEMINI_ENTERPRISE_APP_ID\""
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://logging.googleapis.com/v2/projects/TARGET_PROJECT_ID/locations/global/buckets/_Default/views?viewId=LOG_VIEW_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://logging.googleapis.com/v2/projects/TARGET_PROJECT_ID/locations/global/buckets/_Default/views?viewId=LOG_VIEW_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

  2. After you create the log view, grant the execution service account read access to it. This authorizes the enrichment job to pull the application telemetry it needs during the self-learning phase.

To add an IAM policy binding to a log view, use the [`gcloud logging views add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/views/add-iam-policy-binding):

Before using any of the command data below, make the following replacements: 

     * `LOG_VIEW_NAME`: the name of your log view
     * `SERVICE_ACCOUNT_NAME`: the name of your service account
     * `TARGET_PROJECT_ID`: your Google Cloud project ID

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views add-iam-policy-binding LOG_VIEW_NAME \
        --location=global \
        --bucket=_Default \
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" \
        --role="roles/logging.viewAccessor"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views add-iam-policy-binding LOG_VIEW_NAME `
        --location=global `
        --bucket=_Default `
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" `
        --role="roles/logging.viewAccessor"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud logging views add-iam-policy-binding LOG_VIEW_NAME ^
        --location=global ^
        --bucket=_Default ^
        --member="serviceAccount:SERVICE_ACCOUNT_NAME@TARGET_PROJECT_ID.iam.gserviceaccount.com" ^
        --role="roles/logging.viewAccessor"


**Note:** If your organization does not use custom log views, you can alternatively grant the broader Logs Viewer role (`roles/logging.viewer`) to the service account on the consumer project.

For more information, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views).

### BigQuery agent analytics

If your organization streams interaction logs into BigQuery using a Logging log sink or writes directly to BigQuery agent analytics tables, you can grant access to the dataset instead.

Ensure the interaction logs are configured to stream to a designated BigQuery dataset, and verify that the execution service account is granted the BigQuery Data Viewer role (`roles/bigquery.dataViewer`) on that specific dataset. This lets the agent read the exported telemetry directly from BigQuery.

For more information on exporting logs, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export).

## Enable data profiling and data insights

Before running an enrichment task, we recommend enabling data profiling and AI data insights on your frequently used target tables. Data profiling provides statistical characteristics—such as common values, data distributions, and null counts—while data insights generate baseline table descriptions and sample queries. Providing these signals helps the enrichment agent generate more accurate metadata proposals.

  * For more information about configuring data profile scans, see [Create and use data profile scans](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).
  * For more information about generating AI data insights, see [Use data insights for structured data](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-insights-structured-data).



## What's next

  * Learn how to [create enrichment tasks](https://docs.cloud.google.com/knowledge-catalog/docs/create-enrichment-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
