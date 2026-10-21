---
url: https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances/
title: Configure new and existing instances for IAM database authentication \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:26.101544+00:00
---

# Configure new and existing instances for IAM database authentication  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/create-edit-iam-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure new and existing instances for IAM database authentication Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-edit-iam-instances "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page has procedures for creating or editing Cloud SQL instances to allow users, service accounts, or groups that are configured to use Cloud SQL IAM database authentication. To learn more about the Cloud SQL IAM integration, see [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication).

A newly-created instance has a `postgres` database.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Make sure you have the Cloud SQL Admin and Compute Viewer roles on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

[Learn more](https://docs.cloud.google.com/sql/docs/postgres/roles-and-permissions) about roles and permissions. 




The maximum number of instances you can have in a single project depends on the [network architecture](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-new-network-architecture#overview) of those instances:

  * New SQL network architecture: You can have up to 1,000 instances per project.
  * Old SQL network architecture: You can have up to 100 instances per project.
  * Using both architectures: Your limit will be somewhere between 100 and 1,000, depending on the distribution of your instances across the two architectures.



[File a support case](https://support.google.com/googlecloud/answer/1041916) to request an increase. Read replicas are counted as instances.

## Configure new instances for IAM database authentication

To configure a new Cloud SQL instance for IAM database authentication, you need to enable the `cloudsql.iam_authentication` flag. After you enable this flag, you can add IAM users, service accounts, or groups to the Cloud SQL instance.

To configure a new Cloud SQL instance to use IAM database authentication:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create Instance**.
  3. Click **Choose PostgreSQL**.
  4. Enter a name for the **Instance ID**.
Don't include sensitive or personally identifiable information in your instance name; it's externally visible. You don't need to include the project ID in the instance name. The project ID is included automatically where appropriate (for example, in the log files). 
  5. Enter a password for the default administrator.
  6. From the **Database version** menu, select a database version.
  7. In the **Choose region and zonal availability** section, select the region and zone for your instance. Place your instance in the same region as the resources that access it. The region you select can't be modified in the future. Usually, you don't need to specify a zone. **Note:** If there's a resource location constraint on your organization policy, then you must select one of the regions that the organization policy allows. If a constraint exists, then a message appears about the constraint. [Learn more](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).
  8. In the **Customize your instance** section, click **Show Configuration Options** , and then expand **Flags**. 
  9. Click **Add Flag**.
  10. From the **Choose a flag** menu, select the `cloudsql.iam_authentication` flag. Make sure that **On** is selected as the value for this flag, and then click **Done**.
  11. Configure other instance settings, as needed. For more information about settings, see [Settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#settings-2ndgen).
  12. Click **Create Instance**.



### gcloud

Run `[gcloud sql instances create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create)` with the `--database-flags` parameter set to `cloudsql.iam_authentication=on`.

Replace the following:

  * INSTANCE_NAME: the name of the new instance.
  * POSTGRES_VERSION: the PostgreSQL version (such as POSTGRES_9_6, POSTGRES_10, POSTGRES_11, or POSTGRES_12).
  * NUMBER_OF_CORES: the number of cores in the machine.
  * AMOUNT_OF_MEMORY: the amount of memory in the machine. A size unit should be provided (such as, 3072MiB or 9GiB).
  * ZONE: preferred Compute Engine zone (such as us-central1-a, or us-central1-b).
  * PASSWORD: create a password for the root user.


    
    
    gcloud sql instances create INSTANCE_NAME \
    --database-version=POSTGRES_VERSION \
    --cpu=NUMBER_OF_CORES \
    --memory=AMOUNT_OF_MEMORY \
    --zone=ZONE_NAME \
    --root-password=PASSWORD \
    --database-flags=cloudsql.iam_authentication=on

### Terraform

To create an instance with IAM database authentication enabled, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "postgres-db-auth-instance-name-test"
      region           = "us-west4"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        database_flags {
          name  = "cloudsql.iam_authentication"
          value = "on"
        }
      }
    }

#### Apply the changes

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

#### Delete the changes

To delete your changes, do the following:

  1. To disable deletion protection, in your Terraform configuration file set the `deletion_protection` argument to `false`. 
         
         deletion_protection =  "false"

  2. Apply the updated Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply



  3. Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform destroy




### REST v1

Don't include sensitive or personally identifiable information (PII) in your instance name; it is externally visible.

You don't need to include the project ID in the instance name. The project ID is included automatically where needed (for example, in the log files).

Before using any of the request data, make the following replacements: 

  * INSTANCE_ID: the desired instance ID
  * REGION: the desired region, such as us-east-1
  * PROJECT_ID: the project ID
  * LOCATION_ID: the location ID
  * DATABASE_VERSION: enum string of the database version. For example: `POSTGRES_12`
  * PASSWORD: the password for the root user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "backupConfiguration": {
          "enabled": true
        },
        "databaseFlags": [
          {
            "name": "cloudsql.iam_authentication",
            "value": "on"
          }
        ]
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert) is constructed for this task, see the [APIs Explorer on the instances:insert page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert). 

### REST v1beta4

Don't include sensitive or personally identifiable information (PII) in your instance name; it is externally visible.

You don't need to include the project ID in the instance name. The project ID is included automatically where needed (for example, in the log files).

Before using any of the request data, make the following replacements: 

  * INSTANCE_ID: the desired instance ID
  * REGION: the desired region, such as us-east-1
  * PROJECT_ID: the project ID
  * LOCATION_ID: the location ID
  * DATABASE_VERSION: enum string of the database version. For example: `POSTGRES_12`
  * PASSWORD: the password for the root user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "backupConfiguration": {
          "enabled": true
        },
        "databaseFlags": [
          {
            "name": "cloudsql.iam_authentication",
            "value": "on"
          }
        ]
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert) is constructed for this task, see the [APIs Explorer on the instances:insert page](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances/insert). 

## Configure existing instances for IAM database authentication

To configure an existing Cloud SQL instance for IAM database authentication, you need to enable the `cloudsql.iam_authentication` flag. After you enable this flag, you can add IAM users, service accounts, or groups to the Cloud SQL instance.

To configure an existing Cloud SQL instance to use IAM database authentication:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, expand **Flags**. 
  5. Click **Add Flag**.
  6. From the **Choose a flag** menu, select the `cloudsql.iam_authentication` flag. Make sure that **On** is selected as the value for this flag, and then click **Done**.
  7. Configure other instance settings, as needed. For more information about settings, see [Settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#settings-2ndgen).
  8. Click **Save**.



### gcloud

For information about installing and getting started with the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see [Use Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell). 

For this procedure, use ` [gcloud sql instances patch](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch)`.

Replace the following:

  * INSTANCE_NAME: the name of the new instance.


    
    
    gcloud sql instances patch INSTANCE_NAME \
    --database-flags=cloudsql.iam_authentication=on

This resets all other existing database flag settings. For further guidance on setting database flags, see [Set a database flag](https://docs.cloud.google.com/sql/docs/postgres/flags#set_a_database_flag).

  


### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * LOCATION_ID: the location ID
  * INSTANCE_ID: the desired instance ID
  * REGION: the desired region
  * DATABASE_VERSION: enum string of the database version. For example: `POSTGRES_12`
  * PASSWORD: the password for the root user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "backupConfiguration": {
          "enabled": true
        }
        "databaseFlags":
        [
          {
            "name": "cloudsql.iam_authentication",
            "value": "on"
          }
        ]
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * LOCATION_ID: the location ID
  * INSTANCE_ID: the desired instance ID
  * REGION: the desired region
  * DATABASE_VERSION: enum string of the database version. For example: `POSTGRES_12`
  * PASSWORD: the password for the root user
  * MACHINE_TYPE: enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "backupConfiguration": {
          "enabled": true
        }
        "databaseFlags":
        [
          {
            "name": "cloudsql.iam_authentication",
            "value": "on"
          }
        ]
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/locations/LOCATION_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## What's next

  * Learn more about [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/authentication).
  * Learn how to [configure read replica logins for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/replication/create-replica#configure_iam_replicas).
  * Learn how to [create users and service accounts that use Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#creating-a-database-user). 
  * Learn how to [log in to a Cloud SQL database using IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-logins).
  * Learn how to [manage users and service accounts for IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
