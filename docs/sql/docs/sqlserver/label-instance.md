---
url: https://docs.cloud.google.com/sql/docs/sqlserver/label-instance/
title: Label instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:05.869381+00:00
---

# Label instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/label-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Label instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/label-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/label-instance "View this page for the PostgreSQL database engine") | SQL Server

This page explains labels. It describes how to create an instance with labels; how to add, update, and remove labels; and how to use labels in searches.

Labels are a lightweight way to group together instances that are related or associated with each other. For example, you could label your instances according to whether you are using them as test or production, or you could add your own billing code to an instance. You can use the labels to search for instances or to track instance charges.

You always add labels as key/value pairs:
    
    
    {
     "userLabels": {
        "track": "production",
        "location": "western-division"
        "billing-code": "34802",...
     }
    

Modifying labels has no impact on Cloud SQL instance performance.

For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#what-are-labels) and [Requirements for labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).

## Restrictions

  * You can assign up to 50 user-defined labels to each instance. Although Google Cloud resources support up to 64 total labels, Cloud SQL reserves up to 14 labels for internal system and billing metadata on underlying backup snapshots.
  * If an existing instance already has more than 50 user-defined labels, then you can't add new labels, and automated or on-demand backups might fail if the combined user and system labels exceed 64. To prevent backup failures, reduce user-defined labels to 50 or fewer per instance.
  * Label keys and values must conform to the following restrictions:

    * Keys and values cannot be longer than 63 characters each.
    * Keys and values can only contain lowercase letters, numeric characters, underscores, and dashes. International characters are allowed.
    * Label keys must start with a lowercase letter.
    * Label keys cannot be empty.



## Create instances with labels

When creating a new instance using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) or the API, you can apply labels to the instance.

### gcloud

When creating your instance, include the `--labels` flag, followed by a comma-separated list of key value pairs of labels. You must use the beta version of the create command to include labels.

For example:
    
    
    gcloud beta sql instances create ... --labels track=production,billing-code=34802

### Terraform

When creating an instance with a label, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance): 
    
    
    resource "google_sql_database_instance" "default" {
      name             = "sqlserver-instance-labels"
      region           = "us-central1"
      database_version = "SQLSERVER_2019_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        tier = "db-custom-2-7680"
        user_labels = {
          track        = "production"
          billing-code = 34802
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




### curl

In the API, during the `POST` request to add a new instance, add the `userLabels` property in the request body to apply labels to the new instance. For example, your request body for creating an instance has the following labels:
    
    
              "settings": {"tier":"db-custom-2-7680",
                           "userLabels": {"track": "production",
                                          "location": "western-division",
                                          "billing-code": "34802"},
              

## Add or update labels on an existing instance

###  console 

  1. Go to the Cloud SQL Instances page in the Google Cloud console. 

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances)

  2. Select the checkboxes next to the resources you want to label.

  3. Click **Show Info Panel** in the upper righthand corner to expand the labels column.

  4. Update or add new labels as desired.

  5. Save your changes.




###  gcloud 

Use the `patch` subcommand (beta version) to update or add labels on an existing instance:
    
    
    gcloud beta sql instances patch [INSTANCE_NAME] --update-labels [KEY1]=[VALUE1]...
    

For example:
    
    
    gcloud beta sql instances patch my-instance --update-labels track=production,billing-code=34802
    

If you provide a label key that already exists, the tool updates the existing key with the new label value. If you provide a new key, the tool adds the new key to the list of labels. Only the labels you specify are affected; existing labels not included in the command remain unchanged.

###  rest v1 

To add or update labels, use the `PATCH` method:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * label-name-1: A label name
  * value-1: The value of label-name-1
  * label-name-2: A label name
  * value-2: The value of label-name-2



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings" :
        {
            "userLabels" :
             {
                "label-name-1" : "value-1",
                "label-name-2" : "value-2"
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

If you provide a label key that already exists, the tool updates the existing key with the new label value. If you provide a new key, the tool adds the new key to the list of labels. Only the labels you specify are affected; existing labels not included in the request remain unchanged.

###  rest v1beta4 

To add or update labels, use the `PATCH` method:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * label-name-1: A label name
  * value-1: The value of label-name-1
  * label-name-2: A label name
  * value-2: The value of label-name-2



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings" :
        {
            "userLabels" :
             {
                "label-name-1" : "value-1",
                "label-name-2" : "value-2"
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

If you provide a label key that already exists, the tool updates the existing key with the new label value. If you provide a new key, the tool adds the new key to the list of labels. Only the labels you specify are affected; existing labels not included in the request remain unchanged.

## Remove a label

###  console 

  1. Go to the Cloud SQL Instances page in the Google Cloud console. 

[Go to the Cloud SQL Instances page](https://console.cloud.google.com/sql/instances)

  2. Select the checkboxes next to the resources for which you want to remove labels.

  3. Click **Show info panel** to expand the labels column.

  4. Click the `X` next to all the labels you want to remove.

  5. Save your changes.




###  gcloud 

Using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), run the `patch` subcommand (beta version) with the `--remove-labels` flag:
    
    
    gcloud beta sql instances patch [INSTANCE_NAME] --remove-labels [LABEL1],[LABEL2]
    

If you provide a label name that does not exist, no error is returned.

###  rest v1 

You remove a label using the API by setting its value to `null`:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * label-name: The label name



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings" :
        {
            "userLabels" :
             {
                "label-name" : null,
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
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

###  rest v1beta4 

You remove a label using the API by setting its value to `null`:

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * label-name: The label name



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings" :
        {
            "userLabels" :
             {
                "label-name" : null,
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
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Filter instance searches using labels

You can filter your instance list results by labels using the gcloud CLI or the API.

###  gcloud 

In `gcloud`, make a `list` request and use the `--filter` flag. To filter on labels, use the syntax `labels.[KEY]:[VALUE]`. For example, if you wanted to filter on a label `billing-code` with a value of `34802`, you can run this command:
    
    
    gcloud beta sql instances list --filter='labels.billing-code:34802'
    

If you want to filter on whether a label exists, regardless of its value:
    
    
    gcloud beta sql instances list --filter='labels:billing-code'
    

For complete documentation about the filter syntax in the gcloud CLI, see the [`gcloud topic filters` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

###  curl 

In the API, make a list request with a URL encoded `filter` query parameter:
    
    
    gcloud auth login
    ACCESS_TOKEN="$(gcloud auth print-access-token)"
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         -X GET \
         https://www.googleapis.com/sql/v1beta4/projects/[PROJECT_ID]/instances/list?filter=userLabels.[KEY1_NAME]:[KEY1_VALUE]%20userLabels.[KEY2_NAME]:[KEY2_VALUE]
    

For example:
    
    
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         -X GET \
         https://www.googleapis.com/sql/v1beta4/projects/[PROJECT_ID]/instances/list?filter=userLabels.track:production%20userLabels.billing-code:34802
    

When two label values are included with an (encoded) space between them, they both must be true for an instance to be returned (an `AND` operation). You can also explicitly provide `AND`, `OR`, and `NOT` operators. For example:
    
    
    curl --header "Authorization: Bearer ${ACCESS_TOKEN}" \
         -X GET \
         https://www.googleapis.com/sql/v1beta4/projects/[PROJECT_ID]/instances/list?filter=userLabels.track:production%20OR%20userLabels.billing-code:34802
    

## What's next

  * Learn about [exporting billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).
  * Learn about [filtering using the gcloud tool](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
