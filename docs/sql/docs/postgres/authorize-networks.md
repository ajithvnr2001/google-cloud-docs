---
url: https://docs.cloud.google.com/sql/docs/postgres/authorize-networks/
title: Authorize with authorized networks \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:08.039403+00:00
---

# Authorize with authorized networks  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/authorize-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Authorize with authorized networks Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-networks "View this page for the SQL Server database engine")

This page describes how to use the authorized networks settings for connecting to Cloud SQL instances that use IP addresses.

## Configure authorized networks

Your client application's IP address or address range must be configured as `authorized networks` for the following conditions: 

  * Your client application is connecting directly to a Cloud SQL instance on its public IP address.
  * Your client application is connecting directly to a Cloud SQL instance on its private IP address, and your client's IP address is a [non-RFC 1918 address](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges)



The IP address can be either a single endpoint or consist of a range in [ CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. From the SQL navigation menu, select **Connections**.
  4. Click the **Networking** tab.
  5. Select the **Public IP** checkbox.
  6. In the **Authorized networks** section, expand **New IP range**.
  7. In the **Name** field, enter a name for the **New IP range**.
  8. In the **IP range** field, enter the public IPv4 address or address range from which you want to allow connections.  
Alternatively, click **Use My IP** to let Cloud SQL populate the IPv4 address of the client machine from which you are accessing Google Cloud.  
The **Use my IP** option isn't available for clients that use IPv6 addresses. 

For the address range, you must use a valid [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation) (for example, 10.10.10.0/24).

  9. Click **Done**.
  10. Click **Save**.



### gcloud

Configuring authorized networks replaces the existing authorized networks list.
    
    
    gcloud sql instances patch INSTANCE_ID \
    --authorized-networks=NETWORK_RANGE_1,NETWORK_RANGE_2...
        

### Terraform

To configure authorized networks, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "postgres-instance-with-authorized-network"
      region           = "us-central1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        ip_configuration {
          authorized_networks {
            name            = "Network Name"
            value           = "192.0.2.0/24"
            expiration_time = "3021-11-15T16:19:00.094Z"
          }
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

Configuring authorized networks replaces the existing authorized networks list.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * network_range_1 An authorized ip address or range
  * network_range_2 Another authorized ip address or range



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "ipConfiguration":
        {
          "authorizedNetworks":
            [{"value": "network_range_1"}, {"value": "network_range_2"}]
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

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

### REST v1beta4

Configuring authorized networks replaces the existing authorized networks list.

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID
  * network_range_1 An authorized ip address or range
  * network_range_2 Another authorized ip address or range



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    
    {
      "settings":
      {
        "ipConfiguration":
        {
          "authorizedNetworks":
            [{"value": "network_range_1"}, {"value": "network_range_2"}]
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

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

## Limitations

  * Some IP address ranges can't be added as authorized networks. Address range | Notes  
---|---  
10.0.0.0/8 | RFC 1918 address range. These are automatically and implicitly included in the authorized networks by Cloud SQL  
172.16.0.0/12 | RFC 1918 address range. These are automatically and implicitly included in the authorized networks by Cloud SQL  
192.168.0.0/16 | RFC 1918 address range. These are automatically and implicitly included in the authorized networks by Cloud SQL  
**Note:** The authorized networks list is implemented on the Cloud SQL instance VM by a local firewall. Learn more about [managing connections](https://docs.cloud.google.com/sql/docs/postgres/manage-connections).
  * Cloud SQL doesn't support IPv6 authorized networks. If your client machine uses the IPv6 protocol, then the optional **Use my IP** button isn't available in the **Networking** tab of the Google Cloud console.
  * If you're using a VPN or proxy server, then the **Use my IP** option doesn't display the client machine's actual IP address. This is by design.



## What's next

  * Learn more about [instance access control](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control).

  * [Configure your instance](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance) to use SSL/TLS.

  * [Connect to your instance](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect-ssl) with the psql client using SSL/TLS.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
