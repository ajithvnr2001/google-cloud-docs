---
url: https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai/
title: Integrate Cloud SQL with Vertex AI \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:09.774579+00:00
---

# Integrate Cloud SQL with Vertex AI  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Integrate Cloud SQL with Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/integrate-cloud-sql-with-vertex-ai "View this page for the SQL Server database engine")

This page describes how to integrate Cloud SQL with [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs).

This integration lets you apply large language models (LLMs), which are hosted in Vertex AI, to a Cloud SQL for MySQL database, version 8.0.36 and later.

By integrating Cloud SQL with Vertex AI, you can apply the semantic and predictive power of machine learning (ML) models to your data. This integration extends the SQL syntax with two functions for querying models:

  * [Invoke predictions](https://docs.cloud.google.com/sql/docs/mysql/invoke-online-predictions) to call a model using SQL within a transaction.

  * [Generate embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings) to have an embedding model translate text prompts into numerical vectors. You can then apply these vector embeddings as inputs to `vector` functions. This includes methods to compare and sort samples of text according to their relative semantic distance.




As a result, you can make real-time predictions and gain valuable insights directly within the database, streamlining your workflows and enhancing your decision-making capabilities.

For more information about Vertex AI, see [Introduction to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).

## Before you begin

**Note:** The name that you use for your project must be between 4 and 30 characters. When you type the name, the form suggests a project ID, which you can edit. The project ID must be between 6 and 30 characters, with a lowercase letter as the first character. You can use a dash, lowercase letter, or digit for the remaining characters, but the last character can't be a dash. 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the necessary Google Cloud APIs. 

### Console

     1. Go to the [**APIs & Services** page](https://console.developers.google.com).
     2. From the projects list, select your project.
     3. If the **API Library** isn't open, then from the navigation menu, select **Library**.
     4. Click the APIs that you want to enable. For this procedure, enable the following:

        * Cloud SQL Admin API
        * Vertex AI API
        * Compute Engine API

**Note:** If you need help finding these APIs, then use the search field.

     5. After selecting each API, click **Enable**.

### gcloud

     1. Open [Cloud Shell](https://docs.cloud.google.com/shell/docs/run-gcloud-commands), which provides command-line access to your Google Cloud resources directly from the browser.
     2. To enable the required APIs, use the `[gcloud services enable](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable)` command: 
            
            gcloud services enable sqladmin.googleapis.com \
              aiplatform.googleapis.com \
              compute.googleapis.com
            

This command enables the following APIs: 
        * Cloud SQL Admin API
        * Vertex AI API
        * Compute Engine API

  7. Grant the Cloud SQL service account Identity and Access Management (IAM) permissions to access Vertex AI.

### gcloud

**Note** : If you're creating an instance with Vertex AI enabled, then create the instance before you complete this step.

To add the Vertex AI permissions to the Cloud SQL service account for the project where the Cloud SQL instance is located, create a custom IAM role with the minimum required permissions, and then grant that role to the service account. 

     1. To create a custom role with the `aiplatform.endpoints.predict` permission, use the [`gcloud iam roles create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/create) command: 
            
            gcloud iam roles create ROLE_NAME \
              --project=PROJECT_ID \
              --title="Cloud SQL Vertex AI Predictor" \
              --description="Allows Cloud SQL to invoke Vertex AI predictions" \
              --permissions="aiplatform.endpoints.predict"
            

     2. To grant the custom role to the Cloud SQL service account, use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
              --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
              --role="projects/PROJECT_ID/roles/ROLE_NAME"
            

Make the following replacements: 
     * ROLE_NAME: the name of the custom IAM role to create, for example `CloudSQLMLPredictor`.
     * PROJECT_ID: the ID of the project that has the Vertex AI endpoint. Cloud SQL uses this endpoint to access the LLM that's hosted in Vertex AI. 
     * SERVICE_ACCOUNT_EMAIL: the email address of the Cloud SQL service account.

To find this email address, use the `[gcloud sql instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe)` command: 
           
           gcloud sql instances describe INSTANCE_NAME | grep EmailAddress
           

Replace INSTANCE_NAME with the name of the Cloud SQL instance. 

**Note:** In general, the policy change takes effect within 2 minutes. However, under certain circumstances, it can take up to 7 minutes for such changes to propagate fully across the system. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation). 
  8. Grant the following privileges to any MySQL database user who needs to make Vertex AI requests: 
     * `SELECT ON mysql.*`
     * `EXECUTE ON mysql.*`

By default, any user with the `cloudsqlsuperuser` role has these privileges or can create a user and grant the required privileges. For more information about the `cloudsqlsuperuser` role in Cloud SQL, see [MySQL 8.0 user privileges](https://docs.cloud.google.com/sql/docs/mysql/users#cloudsqlsuperuser) and [MySQL 8.4 user privileges](https://docs.cloud.google.com/sql/docs/mysql/users#cloudsqlsuperuser-84).




## Enable database integration with Vertex AI

To enable database integration with Vertex AI, complete the following steps:

  1. Create or update a Cloud SQL instance so that the instance can integrate with Vertex AI. 

### gcloud

#### Create the instance

To create the Cloud SQL instance, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command.
         
         gcloud sql instances create INSTANCE_NAME \
         --database-version=DATABASE_VERSION \
         --tier=MACHINE_TYPE \
         --region=REGION_NAME \
         --edition=EDITION_NAME \
         --enable-google-ml-integration

Make the following replacements:

     * INSTANCE_NAME: the name of the instance
     * DATABASE_VERSION: the database version for the instance
     * MACHINE_TYPE: the machine type for the instance
     * REGION_NAME: the region name for the instance
     * EDITION_NAME: the Cloud SQL edition for the instance
**Note:** For more information about these parameters, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

#### Update the instance

To update the instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command.
    
    gcloud sql instances patch INSTANCE_NAME \
    --enable-google-ml-integration

If this update modifies a value that requires a restart, then you see a prompt to proceed with the change or cancel.

**Note:** For more information about updating an instance, see [Edit instances](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).

### REST v1

#### Create the instance

Use this example to create the instance. For a complete list of parameters for this call, see the [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert) page. For information about instance settings, including valid values for a region, see [Instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen). 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
     * INSTANCE_NAME: the name of the instance.
     * REGION_NAME: the region name for the instance.
     * DATABASE_VERSION: enum string of the database version.
     * PASSWORD: the password for the `root` user.
     * MACHINE_TYPE: enum string of the machine (tier) type, such as `db-custom-[CPUS]-[MEMORY_MBS]`. For more information, see [Machine tiers](https://docs.cloud.google.com/sdk/gcloud/reference/sql/tiers/list).
     * EDITION_TYPE: your Cloud SQL edition, such as `ENTERPRISE`.
**Note:** For more information about these parameters, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

You must also include the [enableGoogleMlIntegration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances) object in the request. Set the following parameters, as required:

     * `enableGoogleMlIntegration`: when this parameter is set to `true`, Cloud SQL instances can connect to Vertex AI to pass requests for [real-time predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) and insights to the AI.
     * `cloudsql.enable_google_ml_integration`: when this parameter is set to `on`, Cloud SQL can integrate with Vertex AI.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    {
      "name": "INSTANCE_NAME",
      "region": "REGION_NAME",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "enableGoogleMlIntegration": "true" | "false"
        
        "databaseFlags":
          {
            "name": "cloudsql.enable_google_ml_integration",
            "value": "on" | "off"
          }
        
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2019-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

#### Update the instance

Use this example to update the instance. For a complete list of parameters for this call, see the [instances.patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) page.

If this update modifies a value that requires a restart, then you see a prompt to proceed with the change or cancel.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings": {
        "enableGoogleMlIntegration": true,
        
        "databaseFlags":
          {
            "name": "cloudsql.enable_google_ml_integration",
            "value": "on"
          }
        
       }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

**Note:** For more information about updating an instance, see [Edit instances](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).

### REST v1beta4

#### Create the instance

Use this example to create the instance. For a complete list of parameters for this call, see the [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) page. For information about instance settings, including valid values for a region, see [Instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen). 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
     * INSTANCE_NAME: the name of the instance.
     * REGION_NAME: the region name for the instance.
     * DATABASE_VERSION: enum string of the database version.
     * PASSWORD: the password for the `root` user.
     * MACHINE_TYPE: enum string of the machine (tier) type, such as `db-custom-[CPUS]-[MEMORY_MBS]`. For more information, see [Machine tiers](https://docs.cloud.google.com/sdk/gcloud/reference/sql/tiers/list).
     * EDITION_TYPE: your Cloud SQL edition, such as `ENTERPRISE`.
**Note:** For more information about these parameters, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

You must also include the [enableGoogleMlIntegration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances) object in the request. Set the following parameters, as required:

     * `enableGoogleMlIntegration`: when this parameter is set to `true`, Cloud SQL instances can connect to Vertex AI to pass requests for [real-time predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) and insights to the AI.
     * `cloudsql.enable_google_ml_integration`: when this parameter is set to `on`, Cloud SQL can integrate with Vertex AI.

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    {
      "name": "INSTANCE_NAME",
      "region": "REGION_NAME",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "enableGoogleMlIntegration": "true" | "false"
        
        "databaseFlags":
          {
            "name": "cloudsql.enable_google_ml_integration",
            "value": "on" | "off"
          }
        
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2019-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

#### Update the instance

Use this example to update the instance. For a complete list of parameters for this call, see the [instances.patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) page.

If this update modifies a value that requires a restart, then you see a prompt to proceed with the change or cancel.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     * INSTANCE_NAME: the name of the instance

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    {
      "settings": {
        "enableGoogleMlIntegration": true,
        
        "databaseFlags":
          {
            "name": "cloudsql.enable_google_ml_integration",
            "value": "on"
          }
        
       }
    }

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

**Note:** For more information about updating an instance, see [Edit instances](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).




## Troubleshoot

This section contains information about issues associated with integrating Cloud SQL with Vertex AI along with steps for troubleshooting the issues.

Issue | Troubleshooting  
---|---  
Error message: `Google ML integration API is supported only on MySQL version 8.0.36 or above.` | To enable the Vertex AI integration in Cloud SQL, you must have a Cloud SQL for MySQL database, version 8.0.36 or later. To upgrade your database to this version, see [Upgrade the database minor version](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version).  
Error message: `Google ML Integration API is not supported on shared core instance. Please upsize your machine type.` | If you selected a shared core for the machine type of your instance, then you can't enable the Vertex AI integration in Cloud SQL. Upgrade your machine type to dedicated core. For more information, see [Machine Type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#machine-type-2ndgen).  
Error message: `Google ML Integration is unsupported for this maintenance version. Please follow https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance to update the maintenance version of the instance.` | To enable the Vertex AI integration in Cloud SQL, the maintenance version of your instance must be `R20240130` or later. To upgrade your instance to this version, see [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).  
Error message: `**Cannot invoke ml_predict_row if 'cloudsql.enable_google_ml_integration' is off.**` | The `cloudsql.enable_google_ml_integration `database flag is turned off. Cloud SQL can't integrate with Vertex AI.  
  
To turn this flag on, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:  
  
`gcloud sql instances patch INSTANCE_NAME --database-flags cloudsql.enable_google_ml_integration=on`  
  
Replace INSTANCE_NAME with the name of the primary Cloud SQL instance.  
Error message: `**Failed to connect to remote host: Connection refused.**` | The integration between Cloud SQL and Vertex AI isn't enabled. To enable this integration, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:  
  
`gcloud sql instances patch INSTANCE_NAME   
--enable-google-ml-integration `  
  
Replace INSTANCE_NAME with the name of the primary Cloud SQL instance.  
Error message: `**Vertex AI API has not been used in project PROJECT_ID before or it is disabled. Enable it by visiting /apis/api/aiplatform.googleapis.com/overview?project=PROJECT_ID then retry.**` | The Vertex AI API isn't enabled. For more information on enabling this API, see [Enable database integration with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#enable-database-integration-with-vertex-ai).  
Error message: `**Permission 'aiplatform.endpoints.predict' denied on resource.**` | Vertex AI permissions aren't added to the Cloud SQL service account for the project where the Cloud SQL instance is located. For more information on adding these permissions to the service account, see [Grant the Cloud SQL service account Identity and Access Management (IAM) permissions to access Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#grant-service-account).  
Error message: `**Publisher Model `projects/ PROJECT_ID/locations/REGION_NAME/publishers/google/models/MODEL_NAME` not found.**` | The machine learning model or the LLM doesn't exist in Vertex AI.   
Error message: `**Resource exhausted: grpc: received message larger than max.**` | The size of the request that Cloud SQL passes to Vertex AI exceeds the [gRPC](https://grpc.io/) limit of 4 MB per request.  
Error message: `**Cloud SQL attempts to send a request to Vertex AI. However, the instance is in the %s region, but the Vertex AI endpoint is in the %s region. Make sure the instance and endpoint are in the same region.**` | Cloud SQL attempts to send a request to Vertex AI. However, the instance is in one region, but the Vertex AI endpoint is in a different region. To resolve this issue, both the instance and endpoint must be in the same region.  
Error message: `**The Vertex AI endpoint isn't formatted properly.**` | The Vertex AI endpoint isn't formatted properly. For more information, see [Use private endpoints for online prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints).   
Error message: `**Quota exceeded for aiplatform.googleapis.com/online_prediction_requests_per_base_model with base model: textembedding-gecko.**` | The number of requests that Cloud SQL passes to Vertex AI exceeds the limit of 1,500 requests per minute per region per model per project.  
Error message: `**execute command denied to user DB_USER for routine 'mysql.ml_embedding'.**` | The MySQL database user doesn't have the necessary privileges to call the `mysql.ml_embedding` function. See [the required grants](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#before-you-begin).  
  
## What's next

  * [Work with vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings)


  * [Invoke online predictions from Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/invoke-online-predictions)

  * [Understand an example of an embedding workflow](https://docs.cloud.google.com/sql/docs/mysql/understand-example-embedding-workflow)

  * [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/sql/docs/mysql/langchain)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
