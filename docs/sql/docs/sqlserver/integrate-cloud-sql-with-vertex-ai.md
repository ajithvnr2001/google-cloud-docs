---
url: https://docs.cloud.google.com/sql/docs/sqlserver/integrate-cloud-sql-with-vertex-ai/
title: Integrate Cloud SQL with Vertex AI \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:24.318302+00:00
---

# Integrate Cloud SQL with Vertex AI  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/integrate-cloud-sql-with-vertex-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Integrate Cloud SQL with Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai "View this page for the PostgreSQL database engine") | SQL Server

**Preview — Vertex AI integration with Cloud SQL for SQL Server**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to integrate Cloud SQL with [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs).

This integration lets you apply large language models (LLMs), which are hosted in Vertex AI, to a Cloud SQL for SQL Server 2025 database.

By integrating Cloud SQL with Vertex AI, you can apply the semantic and predictive power of machine learning (ML) models to your data. This integration extends the SQL syntax with the generate embeddings function for querying your models.

You use the generate embeddings function so that the embedding model can translate text prompts into numerical vectors. You can then apply these vector embeddings as inputs to vector data types. For more information, see the Microsoft documentation on [Vector search and vector indexes in the SQL Database Engine](https://learn.microsoft.com/en-us/sql/sql-server/ai/vectors?view=sql-server-ver17).

For more information about Vertex AI, see [Introduction to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).

## Supported editions and database versions

Vertex AI integration is supported for both [Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro) and for all [database versions of SQL Server 2025](https://docs.cloud.google.com/sql/docs/db-versions).

## Supported model types

Vertex AI integration with Cloud SQL supports model endpoints from the following sources:

  * Vertex AI
  * Hugging Face
  * OpenAI



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
        * Optional: If using a third-party model, then the Secret Manager API is required.

**Note:** If you need help finding these APIs, then use the search field.

     5. After selecting each API, click **Enable**.

### gcloud

     1. Open [Cloud Shell](https://docs.cloud.google.com/shell/docs/run-gcloud-commands), which provides command-line access to your Google Cloud resources directly from the browser.
     2. To enable the required APIs, use the `[gcloud services enable](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable)` command: 
            
            gcloud services enable sqladmin.googleapis.com \
              aiplatform.googleapis.com \
              compute.googleapis.com \
              secretmanager.googleapis.com
            

This command enables the following APIs: 
        * Cloud SQL Admin API
        * Vertex AI API
        * Compute Engine API
        * Optional: If using a third-party model, then the Secret Manager API is required.

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

  8. Make sure the Cloud SQL user who is working with the embedding models is granted the following database permissions: 
     * To let a database user create or modify models, you need to grant the Cloud SQL user the `EXECUTE` permission on the following stored procedures: 
       * `[msdb].gcloudsql_ml_create_external_model`: creates an external model object that contains the location, authentication method, and purpose of an AI model inference endpoint.
       * `[msdb].gcloudsql_ml_alter_external_model`: lets you modify the external model object.
       * `[msdb].gcloudsql_ml_drop_external_model`: removes the external model object from the database.
     * To call the stored procedures previously listed, you need the following permissions in the target database: 
       * `CREATE EXTERNAL MODEL`
       * `ALTER EXTERNAL MODEL`

To see how to grant these permissions, see Microsoft documentation on the [Create external model](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-model-transact-sql?view=sql-server-ver17#permissions) command and nomenclature.

For information about Cloud SQL superuser permissions, see [About SQL Server users and stored procedures](https://docs.cloud.google.com/sql/docs/sqlserver/users).

  9. If you want to use a third-party external model, then you must have a valid API Key for the model stored in a Secret Manager location accessible to the Cloud SQL instance.
  10. If using a third-party external model, then the Cloud SQL instance must use a public IP address. Private IP instances can't access third-party external models. Private services access and Private Service Connect are only supported with Vertex AI integration. 




## Enable database integration with Vertex AI

**Caution:** If you enable Vertex AI integration on an existing Cloud SQL instance, then the SQL Server database restarts.**Caution:** If you enable Vertex AI integration on a Cloud SQL instance, then the `external rest endpoint enabled` setting on the database instance is enabled. As a result, you might need to take additional security measures. For more information, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-invoke-external-rest-endpoint-transact-sql?view=sql-server-ver17&tabs=request-headers).

To enable database integration with Vertex AI, complete the following steps:

  1. Create or update a Cloud SQL instance so that the instance can integrate with Vertex AI. 

### gcloud

#### Create the instance

To create the Cloud SQL instance, use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command.
         
         gcloud sql instances create INSTANCE_NAME \
         --database-version=DATABASE_VERSION \
         --tier=MACHINE_TYPE \
         --region=REGION_NAME \
         --enable-google-ml-integration

Make the following replacements:

     * INSTANCE_NAME: the name of the instance.
     * DATABASE_VERSION: the database version for the instance, such as `SQLSERVER_2025_ENTERPRISE`.
     * MACHINE_TYPE: the machine type for the instance, such as `db-perf-optimized-N-8.`.
     * REGION_NAME: the region for the instance, such as `us-central1`.
**Note:** For more information about these parameters, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

#### Update the instance

To update the instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command.
    
    gcloud sql instances patch INSTANCE_NAME \
    --enable-google-ml-integration

**Note:** For more information about updating an instance, see [Edit instances](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance).

### REST v1

#### Create the instance

Use this example to create the instance. For a complete list of parameters for this call, see the [instances:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/insert) page. For information about instance settings, including valid values for a region, see [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#settings-2ndgen). 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
     * INSTANCE_NAME: the name of the instance.
     * REGION_NAME: the region name for the instance.
     * DATABASE_VERSION: enum string of the database version, such as `SQLSERVER_2025_ENTERPRISE`.
     * PASSWORD: the password for the database `root` user.
     * MACHINE_TYPE: enum string of the machine (tier) type, such as `db-custom-[CPUS]-[MEMORY_MBS]`. For more information, see [Machine tiers](https://docs.cloud.google.com/sdk/gcloud/reference/sql/tiers/list).
     * EDITION_TYPE: your Cloud SQL edition, such as `ENTERPRISE`.
**Note:** For more information about these parameters, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

You must also include the [enableGoogleMlIntegration](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances) object in the request. Set the following parameters, as required:

     * `enableGoogleMlIntegration`: when this parameter is set to `true`, Cloud SQL instances can connect to Vertex AI to pass requests for [real-time predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) and insights to the AI.

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

Use this example to update the instance. For a complete list of parameters for this call, see the [instances.patch](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/patch) page.

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
    

**Note:** For more information about updating an instance, see [Edit instances](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance).

### REST v1beta4

#### Create the instance

Use this example to create the instance. For a complete list of parameters for this call, see the [instances:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/insert) page. For information about instance settings, including valid values for a region, see [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#settings-2ndgen). 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance.
     * INSTANCE_NAME: the name of the instance.
     * REGION_NAME: the region name for the instance.
     * DATABASE_VERSION: enum string of the database version, such as `SQLSERVER_2025_ENTERPRISE`.
     * PASSWORD: the password for the database `root` user.
     * MACHINE_TYPE: enum string of the machine (tier) type, such as `db-custom-[CPUS]-[MEMORY_MBS]`. For more information, see [Machine tiers](https://docs.cloud.google.com/sdk/gcloud/reference/sql/tiers/list).
     * EDITION_TYPE: your Cloud SQL edition, such as `ENTERPRISE`.
**Note:** For more information about these parameters, see [Create instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

You must also include the [enableGoogleMlIntegration](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances) object in the request. Set the following parameters, as required:

     * `enableGoogleMlIntegration`: when this parameter is set to `true`, Cloud SQL instances can connect to Vertex AI to pass requests for [real-time predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) and insights to the AI.

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

Use this example to update the instance. For a complete list of parameters for this call, see the [instances.patch](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) page.

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
    

**Note:** For more information about updating an instance, see [Edit instances](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance).




## Add Secret Manager permissions

If you want to use a model from an external source, such as OpenAI or Hugging Face, then you must store the model source's API key in Secret Manager.

Then, you need to give the Cloud SQL instance access to the model source's API key in Secret Manager. To gain access, run the following command:
    
    
    
    SA_NAME=$(gcloud sql instances describe INSTANCE_NAME --format="value(serviceAccountEmailAddress)");
    
    gcloud secrets add-iam-policy-binding SECRET_NAME \
        --member="serviceAccount:${SA_NAME}" \
        --role="roles/secretmanager.secretAccessor"
    

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL instance.
  * SECRET_NAME: the secret's name as used in Secret Manager.



## External model objects

To access a model from an external source, you need to create a model object for SQL Server to use. Cloud SQL provides three stored procedures that let you create, alter, and drop an external model object:

  * `gcloudsql_ml_create_external_model`
  * `gcloudsql_ml_alter_external_model`
  * `gcloudsql_ml_drop_external_model`



### Create an external model

To create a model, run the `gcloudsql_ml_create_external_model` stored procedure found in the `msdb` database:
    
    
    EXECUTE [msdb].[dbo].[gcloudsql_ml_create_external_model]
    @db = [DB_NAME],
    @model_name = MODEL_NAME,
    @model_provider = 'MODEL_PROVIDER',
    @model = 'MODEL',
    @model_url = MODEL_URL,
    @secret_url = SECRET_URL
    

Replace the following:

  * DB_NAME: the target database where you want the external model to be created.
  * MODEL_NAME: the name of the new external model.
  * MODEL_PROVIDER: the name of the model provider, such as one of the following: 
    * Vertex AI
    * OpenAI
    * Hugging Face
  * MODEL_URL: the URL of the model endpoint. 

An example uses the following format:
        
        https://region-aiplatform.googleapis.com/v1/projects/project-id/locations/region/publishers/google/models/model:predict
            

Replace the following:

    * REGION: the region where the model endpoint is located.
    * PROJECT_ID: the project ID where the model endpoint is located.
    * MODEL: the name of the model.
  * MODEL: the AI model being invoked. For example, `text-embedding-005`.
  * SECRET_URL: if Vertex AI is the model provider, this parameter must be empty. If using an external model, this value must reference the Secret Manager location of the API Key. 

An example URL uses the following format:
        
        https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION
            

Replace the following:

    * PROJECT_ID: the project ID where the secret is located.
    * SECRET_NAME: the name of the secret as used in Secret Manager.
    * VERSION: the version number of the secret.



### Alter an external model

To alter an external model object, run the `gcloudsql_ml_alter_external_model` stored procedure found in the `msdb` database:
    
    
    EXECUTE [msdb].[dbo].[gcloudsql_ml_alter_external_model]
    @db = [DB_NAME],
    @model_name = MODEL_NAME,
    @model_provider = 'MODEL_PROVIDER',
    @model = 'MODEL',
    @model_url = MODEL_URL,
    @secret_url = SECRET_URL
    

Replace the following:

  * DB_NAME: the target database where the model you want to modify exists.
  * MODEL_NAME: the name of the existing model.
  * MODEL_PROVIDER: the name of the model provider, such as one of the following: 
    * Vertex AI
    * OpenAI
    * Hugging Face
  * MODEL_URL: the URL of the model endpoint. 

An example uses the following format:
        
        https://region-aiplatform.googleapis.com/v1/projects/project-id/locations/region/publishers/google/models/model:predict
            

Replace the following:

    * REGION: the region where the model endpoint is located.
    * PROJECT_ID: the project ID where the model endpoint is located.
    * MODEL: the name of the model.
  * MODEL: the AI model being invoked. For example, `gemini-embedding-001`.
  * SECRET_URL: if Vertex AI is the model provider, this parameter must be empty. If using an external model, this value must reference the Secret Manager location of the API Key. 

An example URL uses the following format:
        
        https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION
            

Replace the following:

    * PROJECT_ID: the project ID where the secret is located.
    * SECRET_NAME: the name of the secret as used in Secret Manager.
    * VERSION: the version number of the secret.



### Disable Vertex AI integration

To disable Vertex AI integration on a Cloud SQL instance, run the following:
    
    
    gcloud sql instances patch [instance-name] --no-enable-google-ml-integration
    

Replace INSTANCE_NAME with the name of the Cloud SQL instance.

## Drop an external model in SQL Server

To drop an external model from SQL Server, run the `gcloudsql_ml_drop_external_model` stored procedure found in the `msdb` database:
    
    
    EXECUTE [msdb].[dbo].[gcloudsql_ml_drop_external_model]
    @db = [DB_NAME],
    @model_name = MODEL_NAME
    

Replace the following:

  * DB_NAME: the target database where the external model you want to drop exists.
  * MODEL_NAME: the name of the external model to drop.

**Note:** When Vertex AI integration is disabled, external models aren't removed. You must drop the models manually in SQL Server using `DROP EXTERNAL MODEL`.

## Invoke an external model

After Vertex AI integration is enabled on the Cloud SQL instance, and a model object is created for SQL Server to use, you can invoke the SQL Server `AI_GENERATE_EMBEDDINGS` function to create vector embeddings for your data.

To create vector embeddings using the external model, run the following command:
    
    
    SELECT AI_GENERATE_EMBEDDINGS(N'Test Text' USE MODEL MODEL_NAME)
    

Replace MODEL_NAME with the name of the model you want to use.

The executing principal user must have been granted `EXECUTE ON EXTERNAL MODEL` permissions using an appropriate role or grant.

For more information, see the Microsoft documentation on [External model grants](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-model-transact-sql?view=sql-server-ver17#external-model-grants).

## Model size restrictions

Some models, such as `gemini-embedding-01`, have higher default output dimensions than SQL Server can support for `float32` vectors, which have a maximum of 1,998 dimensions. When necessary, you must either use [`float16` (a Microsoft preview feature)](https://learn.microsoft.com/en-us/sql/sql-server/preview-features-faq?view=sql-server-ver17#how-do-i-enable-the-preview_features-option-) for the vector base type, which offers a maximum of 3,996 vector dimensions, or the dimensions parameter must be provided in the `AI_GENERATE_EMBEDDINGS` request to reduce the dimensionality.

For more information, see [Half-precision float support in vector data type](https://learn.microsoft.com/en-us/sql/t-sql/data-types/vector-data-type-half-precision-float?view=sql-server-ver17).

For an example, see the following:
    
    
    DECLARE @params JSON = N'{"dimensions": "DIMENSIONS"}';
    SELECT AI_GENERATE_EMBEDDINGS('This article introduces AI concepts.' USE MODEL MODEL_NAME PARAMETERS @params)
    

Replace the following:

  * DIMENSIONS: the dimensions you want to use for your model, such as `1536`. This value is accepted as a string.
  * MODEL_NAME: the name of the model you want to use.



## Troubleshoot

The following are potential error messages you might receive:

Context | Error or message received | Possible cause  
---|---|---  
`CREATE/ALTER` procedure | "The specified model provider is not valid." | An unsupported model provider was given.  
`CREATE/ALTER` procedure | "The specified secret URL is not valid for this model provider." | For Vertex AI, the secret URL must be empty. For other model providers, the secret URL must not be empty.  
`CREATE/ALTER/DROP` procedure | "The specified model name is not valid." | Model name is a required field.  
`CREATE/ALTER` procedure | "The specified model URL is not valid." | Model URL is a required field.  
`CREATE/ALTER/DROP` procedure | "The specified DB name is not valid." | A valid DB name is a required field.  
`AI_GENERATE_EMBEDDINGS` call | Various error codes, including `400`, `403`, `404`, `405`, `500`. | If running into issues when attempting to run the `AI_GENERATE_EMBEDDINGS` function, only error codes are returned. This is a known Microsoft limitation.  
`AI_GENERATE_EMBEDDINGS` call | "The HTTP response does not contain valid JSON." | An error code that asks you to try again, such as `429` or `500`, was returned from the machine learning agent. However, the client receives this text message instead. This is a known Microsoft limitation.  
  
### Error codes

The `AI_GENERATE_EMBEDDINGS` function only provides error codes, not messages. The following table lists possible causes for some error codes:

Error code | Possible cause  
---|---  
`400 Bad Request` | 

  * Unsupported model type.
  * Incorrectly-formed JSON payload.
  * Invalid URL for the model type.

  
`401 Unauthorized` | The third-party model lacks a valid API key.  
`403 Forbidden` | 

  * The Cloud SQL instance lacks appropriate permissions to access Vertex AI.
  * The Cloud SQL instance lacks appropriate permissions to access Secret Manager.
  * The API key does not grant permission to the specified third-party model.
  * Vertex AI is not enabled on the project.

  
`404 Not Found` | 

  * The specified `secret_url` does not exist.
  * The specified `model_url` does not exist.

  
`405 Method Not Allowed` | A method other than `POST` was provided.  
`413 Request Body Too Large` | The request size is larger than the 1MB limit.  
`429 Too Many Requests` | Exhausted error from the model provider.  
`500 Internal Server Error` | 

  * Unspecified errors from the model provider.
  * Unexpected reply from the model provider.

  
  
## What's next

  * [Work with vector embeddings](https://docs.cloud.google.com/sql/docs/sqlserver/generate-manage-vector-embeddings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
