---
url: https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users/
title: Manage users with IAM database authentication \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:13.063601+00:00
---

# Manage users with IAM database authentication  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage users with IAM database authentication Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to add and manage users, service accounts, and groups to a Cloud SQL instance that uses IAM database authentication.

For more information about the IAM integration, see [IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication).

**Note:** When managing access for users in [external identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation), replace instances of Google Account principal identifiers—like `user:kiran@example.com`, `group:support@example.com`, and `domain:example.com`—with appropriate [Workforce Identity Federation principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 

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

  12. Make sure you have the Cloud SQL Admin role on your user account. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  13. [Enable IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/create-edit-iam-instances#configuring_existing_instances_for) on your Cloud SQL instance.
  14. Assign the necessary `cloudsql.instanceUser` IAM role to IAM principals such as [IAM users](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_identities), [service accounts](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#service_account), or [groups](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#group) to log in to the Cloud SQL instance.
     * If you are adding an individual user or individual service account to the Cloud SQL instance, then you need to assign the IAM role individually to each user and service account.
     * If you are adding a group, then you need to assign the IAM role to the group as the members of the group automatically inherit the IAM permissions associated with the IAM role. For more information about creating groups in Cloud Identity, see [Create and manage Google groups in the Google Cloud console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console). 
     * You can grant the role on a project that contains Cloud SQL instances by using the IAM page of Google Cloud console, the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the Cloud SQL Admin API. For more information, see Add an Add an IAM policy binding to a user, service account, or group.
  15. If you are using a service account, then make sure you have added a [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for each service that requires access to databases in the project.

For more information about creating service accounts, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create). 




### Add an IAM policy binding to a user, service account, or group

This procedure adds a policy binding to the IAM policy of a specific project, given a project ID and the binding. The binding command consists of a member, a role, and an optional condition.

The database username must be the IAM user's email address, for example `example-user@example.com`. It must be all lowercase and use quotes because it contains special characters (`@` and `.`).

### Console

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Add**.
  3. In **New members** , enter an email address. You can add individual users, service accounts, or groups as members, but every project must have at least one principal as a member.
  4. In **Role** , navigate to **Cloud SQL** and select **Cloud SQL Instance User**.
  5. Optional: If you want to connect using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors, then also select **Cloud SQL Client**.
  6. Click **Save**.



### gcloud

Run `[gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` with the `--role=roles/cloudsql.instanceUser` flag.

**Add a policy binding to a user account**

Replace the following:

  * PROJECT_ID: the ID for the project you want to authorize the user to use.
  * USERNAME: the email address for the user.


    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=user:USERNAME \
        --role=roles/cloudsql.instanceUser
      

If you want to connect using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors, then run `[gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` again with the `--role=roles/cloudsql.client` flag.

**Add a policy binding to a service account**

Replace the following:

  * PROJECT_ID: the ID for the project you want to authorize the user to use.
  * SERVICE_ACCT: the email address for the service account.


    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=serviceAccount:SERVICE_ACCT \
        --role=roles/cloudsql.instanceUser
      

If you want to connect using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors, then run `[gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` again with the `--role=roles/cloudsql.client` flag.

**Add a policy binding to a Cloud Identity group**

Replace the following:

  * PROJECT_ID: The ID for the project that you want to authorize members of the group to use.
  * GROUP_EMAIL_ADDRESS: The email address for the group. For example, `example-group@example.com`.


    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=group:GROUP_EMAIL_ADDRESS \
        --role=roles/cloudsql.instanceUser
       

All members of the specified group are granted the Cloud SQL Instance User role and can log in to instances in this project.

If you want to connect using the Cloud SQL Auth Proxy or Cloud SQL Language Connectors, then run `[gcloud projects add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` again with the `--role=roles/cloudsql.client` flag.

### Terraform

To add the required policy-binding to the IAM user and service accounts, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    data "google_project" "project" {
    }
    
    resource "google_project_iam_binding" "cloud_sql_user" {
      project = data.google_project.project.project_id
      role    = "roles/cloudsql.instanceUser"
      members = [
        "user:test-user@example.com",
        "serviceAccount:${google_service_account.default.email}"
      ]
    }
    
    resource "google_project_iam_binding" "cloud_sql_client" {
      project = data.google_project.project.project_id
      role    = "roles/cloudsql.client"
      members = [
        "user:test-user@example.com",
        "serviceAccount:${google_service_account.default.email}"
      ]
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




### Terraform

To add the required policy-binding to the IAM user and service accounts, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    data "google_project" "project" {
    }
    
    resource "google_project_iam_binding" "cloud_sql_user" {
      project = data.google_project.project.project_id
      role    = "roles/cloudsql.instanceUser"
      members = [
        "group:example-group@example.com"
      ]
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




### REST

Grant the `cloudsql.instanceUser` and `cloudsql.client` roles to both types of accounts by editing the JSON or YAML binding policy returned by the `[get-iam-policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#getting-policy)` command. Note that this policy change does not take effect until you [set the updated policy](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#setting-policy).
    
    
        {
          "role": "roles/cloudsql.instanceUser",
          "members": [
                       "user:example-user@example.com"
                       "serviceAccount:service1@sql.iam.gserviceaccount.com"
                       "group:example-group@example.com"
          ]
        }
        {
          "role": "roles/cloudsql.client",
          "members": [
                       "user:example-user@example.com"
                       "serviceAccount:service1@sql.iam.gserviceaccount.com"
          ]
        }

## Add an individual IAM user or service account to a Cloud SQL instance

You must create a new user account for each individual IAM user or service account that you are adding to the Cloud SQL instance in order to access databases. If you are adding an IAM group, then you don't need to create a user account for each member of that group.

The database username must be the IAM user's email address and all lowercase. For example, `example-user@example.com`.

**Note** : When Cloud SQL for MySQL stores a username, it truncates the `@` and the domain name from the user or service account's email address. For example, `example-user@example.com` becomes `example-user`. For this reason, you can't add two IAM users or service accounts with the same username but different domain names to the same Cloud SQL instance.

When using REST commands, the username must use quotes because it contains special characters (`@` and `.`). Service accounts use the format `service-account-name@project-id.iam.gserviceaccount.com`.

To add an individual IAM user or service account, you add a new user account and select IAM as the authentication method:

### Console

**Note:** When you use the Google Cloud console to add a new IAM user or service account to a Cloud SQL instance, Cloud SQL automatically assigns the `cloudsql.instanceUser` IAM role to the user or service account for all instances in the project. The IAM policy binding is automatically added for the user or service account at the project level. You can view the assignment details for this IAM role in the [IAM roles](https://console.cloud.google.com/iam-admin/iam) section of the Google Cloud console.

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click **Add user account**. The **Add a user account to instance _instance_name_** tab opens.
  5. Click the **Cloud IAM** radio button.
  6. Add the email address for the user or service account you want to add in the **Principal** field. 
  7. Click **Add**. The user or service account is now in the user account list.
  8. If the user doesn't have the `cloudsql.instanceUser` IAM role assigned after user account creation, then a ![triangle](https://docs.cloud.google.com/static/sql/images/triangle.png) icon appears next to the username.

To give the user login permissions, click the icon, and then select **Add IAM role**. If the icon no longer appears, then the user account is assigned the IAM role that gives the login permission.




### gcloud

**Create a user account**

Use the email, such as `example-user@example.com`, to identify the user.

Replace the following:

  * USERNAME: the email address for the user.
  * INSTANCE_NAME: the name of the instance you want to authorize the user to access.


    
    
    gcloud sql users create USERNAME \
    --instance=INSTANCE_NAME \
    --type=cloud_iam_user

You can assign one or more database roles to provide the user with database privileges when you create the user account.

**Create a service account**

Replace the following:

  * SERVICE_ACCT: the email address of the service account. 
  * INSTANCE_NAME: the name of the instance you want to authorize the service account to access.


    
    
    gcloud sql users create SERVICE_ACCT \
    --instance=INSTANCE_NAME \
    --type=cloud_iam_service_account

You can assign one or more database roles to provide the account with database privileges when you create the service account.

### Terraform

To add IAM user and service accounts on an instance with IAM database authentication enabled, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "mysql-db-auth-instance-name-test"
      region           = "us-west4"
      database_version = "MYSQL_8_0"
      settings {
        tier = "db-f1-micro"
        database_flags {
          name  = "cloudsql_iam_authentication"
          value = "on"
        }
      }
    }
    
    # Specify the email address of the IAM user to add to the instance
    # This resource does not create a new IAM user account; this account must
    # already exist
    
    resource "google_sql_user" "iam_user" {
      name     = "test-user@example.com"
      instance = google_sql_database_instance.default.name
      type     = "CLOUD_IAM_USER"
    }
    
    # Create a new IAM service account
    
    resource "google_service_account" "default" {
      account_id   = "cloud-sql-mysql-sa"
      display_name = "Cloud SQL for MySQL Service Account"
    }
    
    # Specify the email address of the IAM service account to add to the instance
    
    resource "google_sql_user" "iam_service_account_user" {
      name     = google_service_account.default.email
      instance = google_sql_database_instance.default.name
      type     = "CLOUD_IAM_SERVICE_ACCOUNT"
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

**Create a user account**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "CLOUD_IAM_USER"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:44:16.656Z",
      "startTime": "2020-02-07T22:44:16.686Z",
      "endTime": "2020-02-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

**Create a service account**

Before using any of the request data, make the following replacements: 

  * SERVICE_ACCT: the service account email 
  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the service account to



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
        "name": "SERVICE_ACCT",
        "type": "CLOUD_IAM_SERVICE_ACCOUNT"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-11-20T04:08:00.211Z",
      "startTime": "2020-11-20T04:08:00.240Z",
      "endTime": "2020-11-20T04:08:02.003Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

**Create a user account**

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "CLOUD_IAM_USER"
      }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:44:16.656Z",
      "startTime": "2020-02-07T22:44:16.686Z",
      "endTime": "2020-02-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

**Create a service account**

Before using any of the request data, make the following replacements: 

  * SERVICE_ACCT: the service account email 
  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the service account to



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
        "name": "SERVICE_ACCT",
        "type": "CLOUD_IAM_SERVICE_ACCOUNT"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
    "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-11-20T04:08:00.211Z",
      "startTime": "2020-11-20T04:08:00.240Z",
      "endTime": "2020-11-20T04:08:02.003Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Add an IAM group to a Cloud SQL instance

To use [IAM group authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-group-auth) and add an IAM group to a Cloud SQL instance, use one of the procedures in this section. After you add the IAM group, you don't need to add the individual group members to the instance. For more information, see Add members of a group to a Cloud SQL instance automatically.

A maximum of 200 IAM groups can exist on a Cloud SQL instance at any time. Inactive groups count towards this limit.

IAM group names have the same length limitations as [MySQL usernames](https://dev.mysql.com/doc/refman/8.4/en/user-names.html) and can only be 32 characters long. 

If you have an IAM group with a name that exceeds a database engine's username length limitation, then you can still use it for IAM group authentication by nesting it under a parent IAM group that has a name that complies with the length limitation. The parent IAM group must be added to the instance before the nested group can be used.

### Console

**Note** : When you use the Google Cloud console to add a new IAM group to a Cloud SQL instance, Cloud SQL automatically assigns the `cloudsql.instanceUser` IAM role to the group for all instances in the project. The IAM policy binding is automatically added for the group at the project level. You can see view the IAM role assignment details in the [IAM roles](https://console.cloud.google.com/iam-admin/iam) of the Google Cloud console.

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click **Add user account**. The **Add a user account to instance _instance_name_** tab opens.
  5. Click the **Cloud IAM** radio button.
  6. Add the email address for the group you want to add in the **Principal** field.
  7. Click **Add**. The group is now in the user list.
  8. If the group doesn't have the `cloudsql.instanceUser` IAM role assigned after user account creation, then a ![triangle](https://docs.cloud.google.com/static/sql/images/triangle.png) icon appears next to the group.

To give the group members login permissions, click the icon, and then select **Add IAM role**. If the icon no longer appears, then all members of the group are assigned the role that gives the login permission.




### gcloud

Replace the following:

  * GROUP_EMAIL_ADDRESS: the email address of the Cloud Identity group that you want to add to the instance. For example, **example-group@example.com**.
  * INSTANCE_NAME: the name of the instance where you want to add the group.



Run the following command:
    
    
    gcloud sql users create GROUP_EMAIL_ADDRESS \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_group

You can assign one or more database roles to provide members of the group with database privileges when you create the group.

### Terraform

To add IAM user and service accounts on an instance with IAM database authentication enabled, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "mysql-iam-group-auth-instance-name"
      region           = "us-west4"
      database_version = "MYSQL_8_0"
      settings {
        tier = "db-f1-micro"
        database_flags {
          name  = "cloudsql_iam_authentication"
          value = "on"
        }
      }
    }
    
    # Specify the email address of the Cloud Identity group to add to the instance
    # This resource does not create a Cloud Identity group; the group must
    # already exist
    
    resource "google_sql_user" "iam_group" {
      name     = "example-group@example.com"
      instance = google_sql_database_instance.default.name
      type     = "CLOUD_IAM_GROUP"
    }
    
    data "google_project" "project" {
    }
    
    resource "google_project_iam_binding" "cloud_sql_user" {
      project = data.google_project.project.project_id
      role    = "roles/cloudsql.instanceUser"
      members = [
        "group:example-group@example.com"
      ]
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

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the Cloud Identity group to
  * GROUP_EMAIL: the email address for the Cloud Identity group



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "GROUP_EMAIL",
      "type": "CLOUD_IAM_GROUP"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "example-group@example.com",
      "insertTime": "2023-12-07T22:44:16.656Z",
      "startTime": "2023-12-07T22:44:16.686Z",
      "endTime": "2023-12-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the Cloud Identity group to
  * GROUP_EMAIL: the email address for the Cloud Identity group



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "GROUP_EMAIL",
      "type": "CLOUD_IAM_GROUP"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "example-group@example.com",
      "insertTime": "2023-12-07T22:44:16.656Z",
      "startTime": "2023-12-07T22:44:16.686Z",
      "endTime": "2023-12-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

**Note** : An IAM group deleted from IAM and immediately recreated might not be usable right away. The deletion and recreation takes time to propagate before the IAM group is usable again for IAM group authentication.

## Add members of a group to a Cloud SQL instance automatically

When you add an IAM group to a Cloud SQL instance, all members (users and service accounts) of that group inherit the IAM permissions to authenticate to the instance. You don't need to add the group member individually to the Cloud SQL instance. After a group member logs in and authenticates successfully to the instance for the first time, Cloud SQL creates a group user account or group service account for that group member. You can view the group member listed on the instance after their first successful login.

For more information about login, see [Log in using IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-logins).

## Migrate existing IAM users to use IAM group authentication

Existing IAM users of type `CLOUD_IAM_USER` or `CLOUD_IAM_SERVICE_ACCOUNT` don't use IAM group authentication.

You can migrate these users to use IAM group authentication.

  1. Add these users to a group.

  2. Add the group to your instance.

  3. Assign the group sufficient IAM permissions to let group members connect to your instances. These changes might take time to propagate. For more information about propagation times, see [ Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

  4. Assign database privileges assigned to the IAM users you are migrating to the group.

  5. After group membership changes and IAM permissions are applied, delete the existing IAM user from your instance. The next time that the IAM user logs in successfully, the user is recreated as an IAM group user which can use IAM group authentication.




## Manage group members on a Cloud SQL instance

When you add an IAM group to a Cloud SQL instance, all members (user or service accounts) of that group inherit the IAM permission to authenticate to the instance. You can control access to an instance by managing the group in Cloud Identity. For example, if you want to give a new user access to an instance, then add the user as a group member in Cloud Identity. You don't need to remove or add group members separately at the Cloud SQL instance level because changes to group membership are propagated from to the Cloud SQL instance automatically. Changes to group membership, such as the addition or removal of a member, take about 15 minutes to propagate. The 15 minute propagation delay from Cloud SQL happens in parallel with the [time required for IAM changes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

Granting or revoking database privileges for an IAM group in MySQL takes effect immediately. For example, if you revoke access to a table, members of that IAM group lose access to that table instantly.

It's possible for a user or service account to be a member of multiple IAM groups. If a user or service account belongs to multiple IAM groups on an instance, then they have all the IAM permissions and database privileges combined from each of those IAM groups.

When you add a new member (user or service account) to the IAM group in Cloud Identity and they log in to the instance successfully for the first time, then they inherit the database privileges granted to the group automatically. To use the newly acquired database privileges within the same login session, use the following statement.
    
    
    SET ROLE ALL;
    

For more information, see [`SET ROLE`](https://dev.mysql.com/doc/refman/8.4/en/set-role.html) in the MySQL Documentation. 

## Grant database privileges to an individual IAM user or service account

When an individual IAM user or service is added to a Cloud SQL instance, that new account is granted no privileges on any databases, by default. You can assign individual database privileges to the account, or you can create a database role and then assign the database role to the IAM user or service account. 

To give individual database privileges to an account, use the `GRANT` statement. See the [`GRANT`](https://dev.mysql.com/doc/refman/8.4/en/grant.html) reference page for a complete list of privileges you can grant to users and service accounts. Run `GRANT` from the `mysql` command line.

Replace the following:

* USERNAME: for a user account, this is the email address of the IAM user with the `@` and domain string truncated. For example, if the IAM user's email address is `example-user@example.com`, the username would be `example-user`. for a service account, this is the email address of the service account without the `@project-id.iam.gserviceaccount.com` domain. 
* DATABASE_NAME: the name of the database that hosts the table. 
* TABLE_NAME: the name of the table that you want to give the user access to.
    
    
    grant select on DATABASE_NAME.TABLE_NAME to "USERNAME";

## Grant database privileges to an IAM group

When you use IAM group authentication, you grant database privileges to IAM groups instead of granting privileges to individual users or service accounts. By default, when you add an IAM group to a Cloud SQL instance, the group has no database privileges. You can assign individual database privileges to the group, or you can create a database role and then assign the database role to the IAM group.

To give individual database privileges to an IAM group, use the `GRANT` statement. After they log in to the Cloud SQL instance for the first time, each group member (including users and service accounts) inherit the database privileges granted to the group automatically.

Replace the following:

* GROUP_NAME: the first part of the email address of the Cloud Identity group with the `@` and domain name truncated. For example, if the IAM group's email address is `example-group@example.com`, then the group name is `example-group`.
* DATABASE_NAME: the name of the database that hosts the table.
* TABLE_NAME: the name of the table that you want to give the user access to.

Run GRANT from the `mysql` command line.
    
    
    grant select on DATABASE_NAME.TABLE_NAME to "GROUP_NAME"@"HOSTNAME";

Replace HOSTNAME with the domain name of the IAM group email address.

For more information about granting privileges, see the [GRANT](https://dev.mysql.com/doc/refman/8.4/en/grant.html) reference page in the MySQL documentation.

The database privileges that you grant to the IAM group take effect immediately.

## Assign database roles while adding an IAM account to an instance

To create a custom database role in MySQL, see [Using roles](https://dev.mysql.com/doc/refman/8.4/en/roles.html). 

### gcloud

**Create a user account**

Use the email, such as `example-user@example.com`, to identify the user.
    
    
    gcloud sql users create USERNAME \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_user \
      --database-roles=ROLE_1, ROLE_2

Replace the following:

  * USERNAME: the email address for the user.
  * INSTANCE_NAME: the name of the instance you want to authorize the user to access.
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the user.



**Create a service account**
    
    
    gcloud sql users create SERVICE_ACCOUNT \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_service_account \
      --database-roles=ROLE_1, ROLE_2

Replace the following:

  * SERVICE_ACCOUNT: the email address of the service account. 
  * INSTANCE_NAME: the name of the instance you want to authorize the service account to access.
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the service account.



**Create a group**
    
    
    gcloud sql users create GROUP_EMAIL_ADDRESS \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_group \
      --database-roles=ROLE_1, ROLE_2

Replace the following:

  * GROUP_EMAIL_ADDRESS: the email address of the Cloud Identity group that you want to add to the instance. For example, **example-group@example.com**.
  * INSTANCE_NAME: the name of the instance where you want to add the group.
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the service account.



### Terraform

To add IAM user and service accounts on an instance with IAM database authentication enabled, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_user" "iam_user" {
      name     = "test-user@example.com"
      instance = google_sql_database_instance.default.name
      type     = "CLOUD_IAM_USER"
      # Specify the list of database roles to be granted to the user
      # The database roles must exist in the database.
      database_roles = ["cloudsqlsuperuser"]
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

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user
  * USER_TYPE: the Cloud SQL user type, which is one of the following IAM user types: 
    * `CLOUD_IAM_USER`
    * `CLOUD_IAM_SERVICE_ACCOUNT`
    * `CLOUD_IAM_GROUP`
  * ROLE_1, ROLE_2 ..., ROLE__N_ : the database role or roles to assign to the IAM user, service account, or group



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "USER_TYPE",
      "databaseRoles": [
        "ROLE_1",
        "ROLE_2"
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2025-10-07T22:44:16.656Z",
      "startTime": "2025-10-07T22:44:16.686Z",
      "endTime": "2025-10-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user
  * USER_TYPE: the Cloud SQL user type, which is one of the following IAM user types: 
    * `CLOUD_IAM_USER`
    * `CLOUD_IAM_SERVICE_ACCOUNT`
    * `CLOUD_IAM_GROUP`
  * ROLE_1, ROLE_2 ..., ROLE__N_ : the database role or roles to assign to the IAM user, service account, or group



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "CLOUD_IAM_USER",
      "databaseRoles": [
        "ROLE_1",
        "ROLE_2"
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2025-10-07T22:44:16.656Z",
      "startTime": "2025-10-07T22:44:16.686Z",
      "endTime": "2025-10-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Assign or revoke database roles while updating an IAM account on an instance

After you add an individual IAM user, service account, or IAM group to a Cloud SQL instance, you can modify the database roles that are assigned to it. You can assign database roles that you've defined for your database. The database roles that you assign are added to any roles that are already assigned to the account. If you want to replace database roles, then you must revoke the database roles with the `--revoke-existing-roles` flag.

Before you can assign a role to the principal in Cloud SQL for MySQL, the role must already exist. If you're using a custom role, then create the role in the MySQL database first.

To create a role in MySQL, see [Using roles](https://dev.mysql.com/doc/refman/8.4/en/roles.html).

### gcloud

**Update a user account**

Use the email, such as `example-user@example.com`, to identify the user.

To add database roles for a user account, use the following command:
    
    
    gcloud sql users assign-roles USERNAME \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_user \
      --database-roles=ROLE_1, ROLE_2

To replace the database roles for a user account, use the following command:
    
    
    gcloud sql users assign-roles USERNAME \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_user \
      --database-roles=ROLE_1, ROLE_2
      --revoke-existing-roles

Replace the following:

  * USERNAME: the email address for the user.
  * INSTANCE_NAME: the name of the instance you want to authorize the user to access.
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the user.



**Update a service account**

To add database roles for a service account, use the following command:
    
    
    gcloud sql users assign-roles SERVICE_ACCT \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_service_account \
      --database-roles=ROLE_1, ROLE_2

To replace database roles for a service account, use the following command:
    
    
    gcloud sql users assign-roles SERVICE_ACCT \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_service_account \
      --database-roles=ROLE_1, ROLE_2
      --revoke-existing-roles

Replace the following:

  * SERVICE_ACCT: the email address of the service account. 
  * INSTANCE_NAME: the name of the instance you want to authorize the service account to access.
  * ROLE_1, ROLE_2, ..., ROLE__N_ : the database role or roles to assign to the service account.



**Update a group**

To add database roles for a group, use the following command: 
    
    
    gcloud sql users assign-roles GROUP_EMAIL_ADDRESS \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_group \
      --database-roles=ROLE_1, ROLE_2

To replace database roles for a group, use the following command:
    
    
    gcloud sql users assign-roles GROUP_EMAIL_ADDRESS \
      --instance=INSTANCE_NAME \
      --type=cloud_iam_group \
      --database-roles=ROLE_1, ROLE_2
      --revoke-existing-roles

Replace the following:

  * GROUP_EMAIL_ADDRESS: the email address of the Cloud Identity group that you want to add to the instance. For example, **example-group@example.com**.
  * INSTANCE_NAME: the name of the instance where you want to add the group.
  * ROLE_1, ROLE_2, ...ROLE__N_ : the database role or roles to assign to the group.



### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user
  * USER_TYPE: the Cloud SQL user type, which is one of the following IAM user types: 
    * `CLOUD_IAM_USER`
    * `CLOUD_IAM_SERVICE_ACCOUNT`
    * `CLOUD_IAM_GROUP`
  * ROLE_1, ROLE_2 ..., ROLE__N_ : the database role or roles to assign to the IAM user, service account, or group
  * REVOKE_EXISTING_ROLES: set to `true` to revoke the user's existing roles, set to `false` to keep the user's existing roles



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "USER_TYPE",
      "databaseRoles": [
        "ROLE_1",
        "ROLE_2"
      ],
      "revokeExistingRoles": REVOKE_EXISTING_ROLES
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2025-10-07T22:44:16.656Z",
      "startTime": "2025-10-07T22:44:16.686Z",
      "endTime": "2025-10-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID for the instance you are adding the user to
  * USERNAME: the email address for the user
  * USER_TYPE: the Cloud SQL user type, which can be one of the following IAM user types: 
    * `CLOUD_IAM_USER`
    * `CLOUD_IAM_SERVICE_ACCOUNT`
    * `CLOUD_IAM_GROUP`
  * ROLE_1, ROLE_2 ..., ROLE__N_ : the database role or roles to assign to the IAM user, service account, or group
  * REVOKE_EXISTING_ROLES: set to `true` to revoke the user's existing roles, set to `false` to keep the user's existing roles



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users

Request JSON body: 
    
    
    {
      "name": "USERNAME",
      "type": "USER_TYPE",
      "databaseRoles": [
        "ROLE_1",
        "ROLE_2"
      ],
      "revokeExistingRoles": REVOKE_EXISTING_ROLES
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2025-10-07T22:44:16.656Z",
      "startTime": "2025-10-07T22:44:16.686Z",
      "endTime": "2025-10-07T22:44:20.437Z",
      "operationType": "CREATE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## View IAM users, service accounts, and groups added to a Cloud SQL instance

To view the IAM users, service accounts, and groups that have been added to your Cloud SQL instance, run the following commands.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu. The page displays a list of IAM users, service accounts, and Cloud Identity groups that have been added to your instance.
  4. Optional: To view a list of IAM users or service accounts that have already logged in to the instance, click **Authenticated IAM group members**.



### gcloud

Replace INSTANCE_NAME with the name of the instance that has the groups you want to view.
    
    
      gcloud sql users list --instance=INSTANCE_NAME
      

Groups have a user type of `CLOUD_IAM_GROUP`.

Groups display whether they are active or inactive with the `IAM_STATUS` column. An `ACTIVE` IAM group can be used for IAM group authentication. An `INACTIVE` IAM group can't be used for IAM group authentication.

The output also lists user and service accounts on your Cloud SQL instance.

  * User accounts that are members of a group have the type of `CLOUD_IAM_GROUP_USER`.
  * Service accounts that are members of a group have the type `CLOUD_IAM_GROUP_SERVICE_ACCOUNT`.
  * User accounts that are individual IAM database authentication user accounts have the type of `CLOUD_IAM_USER`.
  * Service accounts that are individual IAM database authentication service accounts have the type of `CLOUD_IAM_SERVICE_ACCOUNT`.



### REST v1

The following request uses the [ users.list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/list) method to list the users who have accounts on the Cloud SQL instance.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users/list

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users/list"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users/list" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "kind": "sql#usersList",
      "items": [
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "example-service-acct",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_SERVICE_ACCOUNT",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "another-example-service-acct",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_GROUP_SERVICE_ACCOUNT",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "root",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "passwordPolicy": {
            "status": {}
          },
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "example-user",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_USER",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "another-example-user",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_GROUP_USER",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "example-group",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_GROUP",
          "iamStatus": "ACTIVE"
        }
      ]
    }
    
    

Groups have a user type of `CLOUD_IAM_GROUP`.

Groups display whether they are active or inactive through the `iamStatus` field. An `ACTIVE` IAM group can be used for IAM group authentication. An `INACTIVE` IAM group is not used for IAM group authentication.

The value `IAM_STATUS_UNSPECIFIED` for the `iamStatus` field means that IAM status isn't relevant for that particular user type.

The output also lists user and service accounts on your Cloud SQL instance.

  * User accounts that are members of a group have the type of `CLOUD_IAM_GROUP_USER`.
  * Service accounts that are members of a group have the type `CLOUD_IAM_GROUP_SERVICE_ACCOUNT`.
  * User accounts that are individual IAM database authentication user accounts have the type of `CLOUD_IAM_USER`.
  * Service accounts that are individual IAM database authentication service accounts have the type of `CLOUD_IAM_SERVICE_ACCOUNT`.



### REST v1beta4

The following request uses the [ users.list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/list) method to list the users who have accounts on the Cloud SQL instance.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the project ID
  * INSTANCE_ID: the instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users/list

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users/list"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users/list" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "kind": "sql#usersList",
      "items": [
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "example-service-acct",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_SERVICE_ACCOUNT",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "another-example-service-acct",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_GROUP_SERVICE_ACCOUNT",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "root",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "passwordPolicy": {
            "status": {}
          },
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "example-user",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_USER",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "another-example-user",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_GROUP_USER",
          "iamStatus": "IAM_STATUS_UNSPECIFIED"
        },
        {
          "kind": "sql#user",
          "etag": "--redacted--",
          "name": "example-group",
          "host": "%",
          "instance": "INSTANCE_ID",
          "project": "PROJECT_ID",
          "type": "CLOUD_IAM_GROUP",
          "iamStatus": "ACTIVE"
        }
      ]
    }
    
    

Groups have a user type of `CLOUD_IAM_GROUP`.

Groups display whether they are active or inactive through the `iamStatus` field. An `ACTIVE` IAM group can be used for IAM group authentication. An `INACTIVE` IAM group can't be used for IAM group authentication.

The value `IAM_STATUS_UNSPECIFIED` for the `iamStatus` field means that IAM status isn't relevant for that particular user type.

The output also lists user and service accounts on your Cloud SQL instance.

  * User accounts that are members of a group have the type of `CLOUD_IAM_GROUP_USER`.
  * Service accounts that are members of a group have the type `CLOUD_IAM_GROUP_SERVICE_ACCOUNT`.
  * User accounts that are individual IAM database authentication user accounts have the type of `CLOUD_IAM_USER`.
  * Service accounts that are individual IAM database authentication service accounts have the type of `CLOUD_IAM_SERVICE_ACCOUNT`.



## Remove an individual IAM user or service account from a Cloud SQL instance

To remove an individual user or service account that is not a member of a group from the Cloud SQL instance, you delete that account by using the following command:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click more_vert for the user you want to remove.
  5. Select **Remove**. This revokes access to this instance only.



### gcloud

**Revoke a user**

Use the email, such as `example-user@example.com`, to identify the user.

Replace the following:

  * USERNAME: the email address without the @domain name.
  * INSTANCE_NAME: the name of the instance you want to remove the user from.


    
    
    gcloud sql users delete USERNAME \
    --instance=INSTANCE_NAME

**Delete the individual service account**

Replace the following:

  * SERVICE_ACCT: the email address of the service account. 
  * INSTANCE_NAME: the name of the instance you want to remove the user from.


    
    
    gcloud sql users delete SERVICE_ACCT \
    --instance=INSTANCE_NAME

### REST v1

The following request uses the [ users.delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/delete) method to delete the specified user account.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * INSTANCE_ID: The desired instance ID
  * USERNAME: The email address for the user or service account



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "DELETE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

The following request uses the [ users.delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/delete) method to delete the specified user account.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID
  * INSTANCE_ID: The desired instance ID
  * USERNAME: The email address for the user or service account



HTTP method and URL: 
    
    
    DELETE https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/users?host=&name=USERNAME" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2020-02-07T22:38:41.217Z",
      "startTime": "2020-02-07T22:38:41.217Z",
      "endTime": "2020-02-07T22:38:44.801Z",
      "operationType": "DELETE_USER",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Remove IAM group members from a Cloud SQL instance

There are two ways to remove IAM group members from a Cloud SQL instance:

  * Automatic removal
  * Manual removal



### Automatic removal

To remove an IAM group member, you need to remove their membership from the applicable IAM groups in Cloud Identity. After the IAM group users have lost membership to all the applicable groups in Cloud Identity, Cloud SQL removes those group users from the instance automatically. 

Changes to group membership, such as the addition or removal of a member, take about 15 minutes to propagate. The 15 minute propagation delay from Cloud SQL happens in parallel with the [time required for IAM changes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

**Note** : IAM users that exist solely on MySQL replicas and have lost all group memberships lose their database privileges and ability to login but don't get removed from the replica. These IAM users remain visible in lists of users.

### Manual removal

In cases where an IAM group user can't be removed automatically, you can manually remove them. You can't manually remove an IAM group user from a Cloud SQL instance by using gcloud CLI, Google Cloud console, Terraform, or the Cloud SQL Admin API. Instead, database users with superuser privileges can manually delete IAM group users from the Cloud SQL instance by using a [DROP USER](https://dev.mysql.com/doc/refman/8.4/en/drop-user.html) statement from a MySQL client. 

After you manually remove an IAM group user from the Cloud SQL instance, make sure that you also remove them from the IAM group in Cloud Identity to prevent further logins to the Cloud SQL instance.

## Change the domain name for existing IAM group members on a Cloud SQL instance

If you change the domain name of an organization in Cloud Identity, then the changes aren't applied automatically to IAM group members on the Cloud SQL instance.

For example, if you change `user@example.com` to `user@new-example.com` in Cloud Identity, then `user@example.com` remains on the Cloud SQL instance despite the domain name being changed in Cloud Identity.

To change the domain name of the IAM group members, do the following:

  1. Use the [IAM group member automatic removal procedure](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#automatic-removal-iam-group-account) to remove any users using the old domain name from the instance.

  2. Re-create the account by logging in to the Cloud SQL instance as each IAM group member and using the account with the new domain name. For more information, see [Add members of a group to a Cloud SQL instance automatically](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-iam-group-auth-users).




To change the domain name of IAM groups, do the following:

  1. Use the [IAM group removal procedure](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#delete-group-instance) to remove any groups using the old domain name from the instance.

  2. Use the [IAM group creation procedure](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-iam-group-db) to add the group with the new domain to the instance.

  3. Re-grant database privileges for the IAM group.




## Delete an IAM group from a Cloud SQL instance

You can delete the added IAM groups from the Cloud SQL instance. After you delete an IAM group from the instance, all users and service accounts that belong to the IAM group lose any database privileges that were granted to the IAM group. In addition, the following conditions apply:

  * The users and service accounts that belong to the IAM group are still able to log in until the `cloudsql.instances.login` IAM permission is removed from the group.
  * If the deletion of a group results in the IAM group user or service accounts belonging to no other groups on the instance, then Cloud SQLremoves the IAM group user or service accounts from the instance. 



If you delete all IAM groups from a Cloud SQL instance, then all the IAM group users and service accounts lose all their database privileges. In addition, the following conditions apply:

  * All IAM group users and service accounts are unable to login to the instance.
  * Cloud SQL also removes all IAM group users and service accounts from the instance automatically.



### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Users** from the SQL navigation menu.
  4. Click more_vert for the group you want to remove.
  5. Select **Remove**. This revokes access to this instance only.



### gcloud

To delete a Cloud Identity group from an instance, use the [`gcloud sql users delete`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete) command.

Replace the following:

  * GROUP_NAME: the first part of the email address of the Cloud Identity group. For example, using the email address `example-group@example.com`, the Cloud Identity group name is `example-group`.
  * HOSTNAME: The second part of the email address represents the hostname of the Cloud Identity group. For example, using the email address `example-group@example.com`, the hostname is `example.com`.
  * INSTANCE_NAME: the name of the Cloud SQL instance with the Cloud Identity group you want to delete.


    
    
    gcloud sql users delete GROUP_NAME \
       --host=HOSTNAME \
       --instance=INSTANCE_NAME

## Delete an IAM group from IAM or Cloud Identity

If you delete an IAM group from IAM or Cloud Identity but don't delete the IAM group from the Cloud SQL instance, then the IAM group is marked as `INACTIVE` and remains on the instance until you [remove the group manually](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#delete-group-instance).

Inactive IAM groups can't be used for IAM group authentication. Database privileges granted to inactive groups don't get passed on to their members. Inactive groups don't count as valid IAM group memberships. IAM group users that don't belong to an active IAM won't be able to authenticate using IAM group authentication.

If an IAM group is inactive, then the group remains inactive on the Cloud SQL instance even if you recreate the group in IAM and Cloud Identity. To recreate the IAM group name, do the following:

  1. Recreate the group in IAM and Cloud Identity.

  2. Use the [IAM group removal procedure](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#delete-group-instance) to remove the inactive group.

  3. Use the [procedure for adding an IAM group](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#add-iam-group-db) to add the group back to the Cloud SQL instance.

  4. Grant database privileges to the newly created IAM group.




## Remove IAM login permissions from an IAM group

If you revoke the `cloudsql.instanceUser` role from an IAM group, then all members of the group lose the ability to log in to any Cloud SQL instance in the project. The users or service accounts can only log into instances if they are members of another IAM group that still has login permissions.

To revoke a role from a Cloud Identity group, see [Revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-other-resources#revoke-single-role).

**Note:** Changes to group **login** permissions can take 15 minutes to propagate.

## Remove users from an IAM group

IAM group members such as users or service accounts can be removed from the IAM group in Cloud Identity.

After the removal has propagated through IAM, the user can no longer log in to the database unless they have received login permissions from another group or are directly granted login privileges. In addition, users removed from a group lose the database privileges of the group.

If an IAM group user doesn't belong to any groups on the instance, then Cloud SQL automatically removes the user from the instance. 

## View login information in audit logs

You can enable audit logs to capture IAM logins to the database. When there are login issues, you can use the audit logs to diagnose the problem.

**Note:** Audit Logging incurs extra costs. For more information, see [Pricing for logging data](https://docs.cloud.google.com/logging#pricing).

Once configured, you can [view Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit#data-access) of successful logins using the **Logs Explorer**.

For IAM group authentication, audit logs display the activity and logins for individual user and service accounts.

For example, a log might have information similar to the following:
    
    
    {
     insertId: "..."
     logName: "projects/.../logs/cloudaudit.googleapis.com%2Fdata_access"
     protoPayload: {
      @type: "type.googleapis.com/google.cloud.audit.AuditLog"
      authenticationInfo: {
       principalEmail: "..."
      }
      authorizationInfo: [
       0: {
        granted: true
        permission: "cloudsql.instances.login"
        resource: "instances/..."
        resourceAttributes: {
        }
       }
      ]
      methodName: "cloudsql.instances.login"
      request: {
       @type: "type.googleapis.com/google.cloud.sql.authorization.v1.InstancesLoginRequest"
       clientIpAddress: "..."
       database: "..."
       databaseSessionId: ...
       instance: "projects/.../locations/us-central1/instances/..."
       user: "..."
      }
      requestMetadata: {
       callerIp: "..."
       destinationAttributes: {
       }
       requestAttributes: {
        auth: {
        }
        time: "..."
       }
      }
      resourceName: "instances/..."
      serviceName: "cloudsql.googleapis.com"
      status: {
      }
     }
     receiveTimestamp: "..."
     resource: {
      labels: {
       database_id: "...:..."
       project_id: "..."
       region: "us-central"
      }
      type: "cloudsql_database"
     }
     severity: "INFO"
     timestamp: "..."
    }
    

## Troubleshoot a login failure

When an attempt to log in fails, MySQL returns a minimal error message for security reasons. For example:
    
    
    $MYSQL_PWD=`gcloud-access-token mysql` --enable-cleartext-plugin --ssl-ca=server-ca.pem
    --ssl-cert=client-cert.pem --ssl-key=client-key.pem   --host=ip_address --user=testuser
    Access denied for user 'testuser'@'...' (using password: NO)
    

You can review the MySQL error logs for more details about the error. For more information, see [Viewing Logs](https://docs.cloud.google.com/sql/docs/mysql/logging).

For example, for the previous error, the following log entry explains the action you can take to resolve the problem.
    
    
    F ... [152172]: [1-1] db=...,user=... FATAL:  Cloud SQL IAM user authentication failed for user "..."
    I ... [152172]: [2-1] db=...,user=... DETAIL:  Request is missing required authentication credential. Expected OAuth 2 access token, log in cookie or other valid authentication credential. See https://developers.google.com/identity/sign-in/web/devconsole-project.
    

Check the error message you receive. If the message does not indicate that you used "Cloud SQL IAM user authentication" or "Cloud SQL IAM service account authentication," verify that the database user type used to log in is either `CLOUD_IAM_USER` or `CLOUD_IAM_SERVICE_ACCOUNT`. For an IAM user, verify that the database username is the IAM user's email address without the `@` and domain. For a service account, verify that it is the service account's email without the `@project-id.iam.gserviceaccount.com`. 

If you used IAM database authentication, check the details of the error message. You can find the error message in the database error log. If it indicates the access token (OAuth 2.0) you sent as a password was invalid, you can use the [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) `gcloud` command to find details of the token, as follows:
    
    
    curl -H "Content-Type: application/x-www-form-urlencoded" \
    -d "access_token=$(gcloud auth application-default print-access-token)" \
    https://www.googleapis.com/oauth2/v1/tokeninfo

Verify that the token is for the intended IAM user or service account and has not expired.

If the details indicate a lack of permission, then verify the IAM user or service account is granted the `cloudsql.instances.login` permission using the predefined `Cloud SQL Instance User` role or custom role in the IAM policy of the instance's project. Use the IAM [Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access) for additional help.

If a login fails due to IAM database authentication unavailability, the user can log in using the default MySQL user and password. This method of logging in still gives the user access to the entire database. Verify that the connection is a secured connection.

## Troubleshoot user accounts that use IAM group authentication

This section lists troubleshooting scenarios for IAM group authentication.

### Failure to add a group to a database

When you attempt to add a group to an instance, you receive the following error:
    
    
    (gcloud.sql.users.create) HTTPError 400: Invalid request: Provided CLOUD_IAM_GROUP: EMAIL, does not exist.
    

Make sure the email address that you provided is a valid group.

If the group doesn't exist yet, then create the group. For more information about creating groups, see [Create and manage Google groups in the Google Cloud console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console).

If you receive the following error:
    
    
    (gcloud.sql.users.create) HTTPError 400: Invalid request: IAM Group Authentication is disabled.
    

Then before you can use IAM group authentication, your Cloud SQL instance requires the following maintenance update:

`R20240514.00_04` or later

You can apply the maintenance update to your instance by using self-service maintenance. For more information, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance).

### An existing IAM user or service account isn't inheriting the database privileges granted to their IAM group

If an existing IAM user or service account isn't inheriting the correct database privileges of their group, then complete the following steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

Verify that the account is a member of the group added to the Cloud SQL instance.

  2. List the users and service accounts on the instance.
         
         gcloud sql users list --instance=INSTANCE_NAME

In the output, check whether the user or service account is listed as a `CLOUD_IAM_USER` or a `CLOUD_IAM_SERVICE_ACCOUNT`.

  3. If the user or service account is listed as a `CLOUD_IAM_USER` or a `CLOUD_IAM_SERVICE_ACCOUNT`, then remove the account from the instance. The account you are removing is an individual IAM account which doesn't inherit database privileges of the group.

  4. Log in again to the instance with the user or service account.

Logging in again to the instance re-creates the account with the correct account type of `CLOUD_IAM_GROUP_USER` or `CLOUD_IAM_GROUP_SERVICE_ACCOUNT`.




## What's next

  * Learn more about [IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/authentication).
  * Learn how to [log in to a Cloud SQL database](https://docs.cloud.google.com/sql/docs/mysql/iam-logins).
  * Learn how to [configure instances for IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/create-edit-iam-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
