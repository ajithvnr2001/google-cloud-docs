---
url: https://docs.cloud.google.com/sql/docs/mysql/edit-instance/
title: Edit instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:15.461989+00:00
---

# Edit instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/edit-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Edit instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/edit-instance "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance "View this page for the SQL Server database engine")

This page describes how to edit an existing Cloud SQL instance.

After you create an instance, you can edit it while it's running to change its settings. For information about instance settings and how changing settings can impact an instance, see [Instance Settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings).

**Note:** This procedure restarts the instance. See [How long are instances shut down during restart?](https://cloud.google.com/sql/docs/mysql/faq.md#shutdown)

## Edit an instance

Most edits can be applied to an instance only when it's running. 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, if the **Show configuration options** menu appears, then click it.
  5. Update any editable settings for your instance.

Learn more about [instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings).

  6. Click **Save**.



### gcloud

This command modifies the backup start time.
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --backup-start-time 16:00

This command allows other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection.
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --enable-google-private-path

If a patch modifies a value that requires a restart, then you see a prompt to proceed with the change or cancel.

To learn more about instance configuration flags, see [gcloud sql instances patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch).

### REST v1

By using this command, you can modify the backup start time and allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID
  * PRIVATE_NETWORK: the network that you're adding or selecting to create a private connection



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "backupConfiguration": {
          "startTime": "16:00",
          "enabled": true,
          "binaryLogEnabled": true
        }
      }
        "ipConfiguration": {
          "privateNetwork": "PRIVATE_NETWORK",
          "authorizedNetworks": [],
          "ipv4Enabled": false,
          "enablePrivatePathForGoogleCloudServices": true
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If a patch modifies a value that requires a restart, you will see a prompt to proceed with the change or cancel.

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch). 

### REST v1beta4

By using this command, you can modify the backup start time and allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over an internal connection.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID
  * PRIVATE_NETWORK: the network that you're adding or selecting to create a private connection



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings": {
        "backupConfiguration": {
          "startTime": "16:00",
          "enabled": true,
          "binaryLogEnabled": true
        }
      }
        "ipConfiguration": {
          "privateNetwork": "PRIVATE_NETWORK",
          "authorizedNetworks": [],
          "ipv4Enabled": false,
          "enablePrivatePathForGoogleCloudServices": true
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

If the patch modifies a value that requires a restart, you will see a prompt to proceed with the change or cancel.

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch). 

## Edit an instance with Private Service Connect enabled

You can update an instance with [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) enabled by using [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API. For example, you can update projects associated with instances for the following purposes:

  * To allow connections from [Private Service Connect endpoints](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#psc-endpoint) to the Cloud SQL instances.
  * For all Cloud SQL instance creations, clones, and Private Service Connect enablements in August 2026 and after, connection reconciliation behavior is enabled by default and cannot be disabled. When you remove a project from the list of allowed projects, all existing Private Service Connect connections from the removed project are immediately closed (reconciled). This means applications using Private Service Connect endpoints in those removed projects cannot continue connecting using those endpoints. For instances created before August 2026, when you remove a project from the list of allowed projects, applications using Private Service Connect endpoints in those removed projects continue to connect until you manually remove those endpoints.

**Note:** There are some limitations to modifying instances with Private Service Connect enabled. For more information, see [Limitations](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect#limitations).

### gcloud

To update projects that can use Private Service Connect, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --project=PROJECT_ID \
    --allowed-psc-projects=ALLOWED_PROJECTS

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance to which Private Service Connect endpoints in VPC networks can connect.
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance to which Private Service Connect endpoints in VPC networks can connect.
  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. These projects override projects that are already configured to use Private Service Connect. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.



The following example lets two projects (`98765` and `87654`) make connections from Private Service Connect endpoints to the `myinstance` Cloud SQL instance that's contained in the `12345` project:
    
    
    gcloud sql instances patch myinstance \
    --project=12345 \
    --allowed-psc-projects='98765','87654'

To remove all allowed projects, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command and the   
`--clear-allowed-psc-projects` flag:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --project=PROJECT_ID \
    --clear-allowed-psc-projects

This flag ensures that no projects are allowed inadvertently.

### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance to which Private Service Connect endpoints in VPC networks can connect.
  * INSTANCE_NAME: the name of the Cloud SQL instance to which Private Service Connect endpoints in VPC networks can connect.
  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. These projects override projects that are already configured to use Private Service Connect. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "kind": "sql#instance",
      "name": "INSTANCE_NAME",
      "project": "PROJECT_ID",
      "settings": {
        "ipConfiguration": {
          "pscConfig": {
            "allowedConsumerProjects": [ALLOWED_PROJECTS]
          }
        },
        "kind": "sql#settings"
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
    

To remove all allowed projects, use the `clear-allowed-psc-projects` flag. This flag ensures that no projects are allowed inadvertently.

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch). 

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance to which Private Service Connect endpoints in VPC networks can connect.
  * INSTANCE_NAME: the name of the Cloud SQL instance to which Private Service Connect endpoints in VPC networks can connect.
  * ALLOWED_PROJECTS: a list of allowed project IDs or numbers, separated by commas. These projects override projects that are already configured to use Private Service Connect. If a project isn't contained in this list, then you can't use it to create an instance and enable Private Service Connect for it.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "kind": "sql#instance",
      "name": "INSTANCE_NAME",
      "project": "PROJECT_ID",
      "settings": {
        "ipConfiguration": {
          "pscConfig": {
            "allowedConsumerProjects": [ALLOWED_PROJECTS]
          }
        },
        "kind": "sql#settings"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To remove all allowed projects, use the `clear-allowed-psc-projects` flag. This flag ensures that no projects are allowed inadvertently.

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch). 

## Edit the server CA mode for an instance

You can change the server certificate authority (CA) mode of an instance to use the either the shared CA (`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CA (`CUSTOMER_MANAGED_CAS_CA`) option.

You can't change an instance to use the per-instance CA (`GOOGLE_MANAGED_INTERNAL_CA`) option, which is the default configuration.

For more information about the different server CA mode options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies).

Before you update an instance to use a shared CA or customer-managed CA, do the following:

  * Review [the list of Google Cloud services that don't support connections](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#service-connection-limitations) to Cloud SQL instances that are configured to use a shared CA or customer-managed CA. If your deployment is required to use the service, then you might need to delay the update.
  * Make sure you're using MySQL 8.0.30 or later. 
  * If you're using the Cloud SQL Auth Proxy or any of the Cloud SQL Language Connectors to connect to the instance, then make sure that they're running the minimum required versions. For shared CA, you must be using the Cloud SQL Auth Proxy version 2.13.0 or later, and for customer-managed CA, you must be using the Cloud SQL Auth Proxy version 2.14.3 or later. For the minimum required versions of the Cloud SQL Language Connectors, see [Cloud SQL Language Connectors requirements](https://docs.cloud.google.com/sql/docs/mysql/language-connectors#requirements).
  * If you're switching to shared CA, then [download the global and regional CA bundles](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#download-root-regional-ca-bundles), copy them to your database clients, and let them trust these CAs. Setting up the certificates before switching server CA mode configuration can help avoid potential interruption for your database clients.
  * If you're switching to customer-managed CA, then do the following: 
    * Make sure that you've already created a [CA pool](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca#ca-pool) and you've [provided the service account with access to the CA pool](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca#update-access).
    * Make sure there's at least one CA in the CA pool.
    * To avoid any interruptions after the update, download the certificates from your customer-managed CA, and set up your database clients to trust your CA.



### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In **Customize your instance** section, expand **Show configuration options**.
  5. Click **Security**.
  6. In the **Server certificate authority mode section** , select **Google managed CAS certificate authority**.
  7. Optional: To [enable the automatic rotation of your server certificates](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#automatic-server-certificate-rotation-cas), select the **Rotate server certificates automatically** checkbox.
  8. Click **Save**.



To update your instance from using a per-instance CA or shared CA to a customer-managed CA, see [Use a customer-managed CA](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca#update-instance-customer-managed-ca).

### gcloud

To update your instance from using a per-instance CA to a shared CA, run the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --server-ca-mode=GOOGLE_MANAGED_CAS_CA

Replace `INSTANCE_NAME`: the name of the Cloud SQL instance you want to patch.

For the `--server-ca-mode` flag, specify `GOOGLE_MANAGED_CAS_CA`.

To update your instance from using a per-instance CA or shared CA to a customer-managed CA, see [Use a customer-managed CA](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca#update-instance-customer-managed-ca).

### REST

To update your instance from using a per-instance CA to a shared CA, use the [`instances.patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID` the ID of the project where your Cloud SQL instance is. 
  * `INSTANCE_ID` the name of the Cloud SQL instance that you want to patch.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":{
         "ipConfiguration":
          {
             "serverCaMode": "GOOGLE_MANAGED_CAS_CA"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To update your instance from using a per-instance CA or shared CA to a customer-managed CA, see [Use a customer-managed CA](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca#update-instance-customer-managed-ca).

## Edit a custom SAN for an instance

If you want to use a custom DNS name to connect to a Cloud SQL instance instead of using an IP address, then configure the custom subject alternative name (SAN) setting while creating the instance. The custom DNS name that you insert into the custom SAN setting is added to the SAN field of the server certificate of the instance. This lets you use the custom DNS name with hostname validation securely.

You can perform the following operations with a custom SAN for a server certificate of an instance:

  * Add DNS names to the instance: add a comma-separated list of up to three custom DNS names to the custom SAN setting. Cloud SQL adds these names to the SAN field of the server certificate. You can secure multiple DNS names with a single certificate.
  * Modify DNS names for the instance: change the custom DNS names that you want to add to the SAN field of the server certificate of the instance.
  * Remove DNS names from the instance: remove all custom DNS names from the SAN field of the server certificate of the instance.



You can edit a custom SAN for an instance by using [](https://docs.cloud.google.com/sdk/gcloud)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API.

**Note:** This feature is available for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) instances only.

### gcloud

To edit a custom SAN for an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --project=PROJECT_ID \
    --custom-subject-alternative-names=DNS_NAMES

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance that has a server certificate to which you're adding, modifying, or removing DNS names
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * DNS_NAMES: a comma-separated list of up to three DNS names that you're adding to the server certificate of your instance **Note:** If you already have DNS names that you added to the certificate, and you use this parameter to specify different DNS names, then Cloud SQL removes the original DNS names from the certificate.



To remove all DNS names from the server certificate of a Cloud SQL instance, use the [ `gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command and the   
`--clear-custom-subject-alternative-names` flag:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --project=PROJECT_ID \
    --clear-custom-subject-alternative-names

This flag ensures that no DNS names are added to the certificate inadvertently.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project. This project contains a Cloud SQL instance that has a server certificate to which you're adding, modifying, or removing DNS names.
  * INSTANCE_NAME: the name of the instance.
  * DNS_NAMES: a comma-separated list of up to three DNS names that you're adding to the server certificate of your instance.

If you already have DNS names that you added to the certificate, and you use this parameter to specify different DNS names, then Cloud SQL removes the original DNS names from the certificate.

If you don't specify any DNS names for the `customSubjectAlternativeNames` parameter, but provide the null `[]` value instead, then Cloud SQL removes all DNS names from the server certificate of the instance. This ensures that no DNS names are added to the certificate inadvertently.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1veta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "kind": "sql#instance",
      "name": "INSTANCE_NAME",
      "project": "PROJECT_ID",
      "settings": {
        "ipConfiguration": {
          "customSubjectAlternativeNames": "DNS_NAMES"
        },
        "kind": "sql#settings"
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
         "https://sqladmin.googleapis.com/sql/v1veta4/projects/PROJECT_ID/instances/INSTANCE_NAME"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1veta4/projects/PROJECT_ID/instances/INSTANCE_NAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch). 

## What's next

  * [About instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
