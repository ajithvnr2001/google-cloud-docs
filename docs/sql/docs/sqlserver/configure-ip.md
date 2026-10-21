---
url: https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip/
title: Configure public IP \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:28.558885+00:00
---

# Configure public IP  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Configure public IP Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/configure-ip "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/configure-ip "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to configure public IP connectivity for a Cloud SQL instance.

## Introduction

You can configure your Cloud SQL instance to have a public IPv4 address, and to accept connections from specific IP addresses or a range of addresses by adding authorized addresses to your instance.

You can't specify a private network (for example, 10.x.x.x) as an authorized network.

Public IP addresses for SQL Server instances:

  * IPv6: Instances don't support IPv6.
  * IPv4: Instances have a static IPv4 address automatically assigned. There is a small charge for the IP address any time your instance is off (deactivated).



For help with connecting an administration client to your instance over an IP connection, see [Connecting sqlcmd Client using IP addresses](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip).

If you configure your instance to accept connections using its public IP address, also configure it to use SSL to keep your data secure. For more information, see [Configure SSL for Instances](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance).

To configure your instance with an IP address that is not exposed to the public internet, see [Configuring Private IP Connectivity](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip).

## Enable public IP and add an authorized address or address range

When you enable public IP for your instance, Cloud SQL configures the instance with a public, static IPv4 address. After you enable public IP, you must set up authorization for database connections. See the [Authorization options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#authentication_options) for more information.

If you're using either a shared certificate authority (CA) or a customer-managed CA as the `serverCaMode` for your instance, then your instance requires a restart when you enable public IP for your instance. For more information about server CA mode configuration, see [Certificate authority (CA) authorities](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies).

To enable public IP and add an authorized address:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. From the SQL navigation menu, select **Connections**.
  4. Click the **Networking** tab.
  5. Select the **Public IP** checkbox.
  6. Click **Add network**.
  7. Optionally, in the **Name** field, enter a name for this network.
  8. In the **Network** field, enter the IP address or address range from which you want to allow connections. 

Use [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).

  9. Click **Done**.
  10. Click **Save**.



### gcloud

  1. If you haven't already, add an IPv4 address to the instance: 
         
         gcloud sql instances patch INSTANCE_NAME\
         --assign-ip

  2. Show all existing authorized addresses by describing the instance: 
         
         gcloud sql instances describe INSTANCE_NAME

Look for **authorizedNetwork** entries under **ipConfiguration** , and note any authorized addresses you want to keep.

  3. Update the authorized network list, including all addresses you want included. 
         
         gcloud sql instances patch INSTANCE_NAME \
         --authorized-networks=IP_ADDR1,IP_ADDR2...

Use [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).

  4. Confirm your changes: 
         
         gcloud sql instances describe INSTANCE_NAME


When you remove an authorized address, existing connections from that address are _not_ disconnected. If you want to disconnect existing connections, restart your instance. 

To remove all authorized networks, use the following command: 
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-authorized-networks
      

### REST v1

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance, including _all_ addresses you want set on the instance: 

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
    

Use [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    


When you remove an authorized address, existing connections from that address are _not_ disconnected. If you want to disconnect existing connections, restart your instance. 

To remove all authorized networks, use the following command: 
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-authorized-networks
      

### Terraform

To enable public IP and add an authorized address or address range, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance). 
    
    
    resource "google_sql_database_instance" "sqlserver_public_ip_instance_name" {
      name             = "sqlserver-public-ip-instance-name"
      region           = "europe-west4"
      database_version = "SQLSERVER_2019_ENTERPRISE"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        tier              = "db-custom-2-7680"
        availability_type = "ZONAL"
        ip_configuration {
          # Add optional authorized networks
          # Update to match the customer's networks
          authorized_networks {
            name  = "test-net-3"
            value = "203.0.113.0/24"
          }
          # Enable public IP
          ipv4_enabled = true
        }
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
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




### REST v1beta4

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance, including _all_ addresses you want set on the instance: 

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
    

Use [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    


When you remove an authorized address, existing connections from that address are _not_ disconnected. If you want to disconnect existing connections, restart your instance. 

To remove all authorized networks, use the following command: 
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-authorized-networks
      

## Remove an authorized address or address range

To remove an authorized address:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Click the delete icon ![Delete.](https://docs.cloud.google.com/static/sql/images/delete-icon.png) for the address you want to delete.
  5. Click **Save** to update the instance.



### gcloud

  1. Show all existing authorized addresses by describing the instance: 
         
         gcloud sql instances describe INSTANCE_NAME

Look for **authorizedNetwork** entries under **ipConfiguration** , and note any authorized addresses you want to keep.

  2. Update the authorized network list, dropping off any addresses you want to remove. 
         
         gcloud sql instances patch INSTANCE_NAME \
         --authorized-networks=IP_ADDR1,IP_ADDR2...

  3. Confirm your changes: 
         
         gcloud sql instances describe INSTANCE_NAME




### REST v1

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance, by including all the addresses you want to keep and dropping off any addresses you want to remove: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * network_range_1 The authorized IP address or network range to remove

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    {
      "settings":
      {
        "ipConfiguration":
        {
          "authorizedNetworks":
            [{"value": "network_range_1"}]
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
    

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address: The CIDR form of the IP address
     * ip-address-name: The name of the IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address",
              "name": "ip-address-name",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    




### REST v1beta4

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance, by including all the addresses you want to keep and dropping off any addresses you want to remove: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * network_range_1 The authorized IP address or network range to remove

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    {
      "settings":
      {
        "ipConfiguration":
        {
          "authorizedNetworks":
            [{"value": "network_range_1"}]
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
    

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address: The CIDR form of the IP address
     * ip-address-name: The name of the IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address",
              "name": "ip-address-name",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    




When you remove an authorized address, existing connections from that address are _not_ disconnected. If you want to disconnect existing connections, restart your instance. 

To remove all authorized networks, use the following command: 
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-authorized-networks
      

## Configure an instance to refuse all public IP connections

To configure an instance to refuse all public IP connections:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Click the delete icon ![Delete.](https://docs.cloud.google.com/static/sql/images/delete-icon.png) for all authorized addresses.
  5. Click **Save** to update the instance.



### gcloud

  1. Clear the authorized address list: 
         
         gcloud sql instances patch INSTANCE_NAME \
         --clear-authorized-networks

  2. Confirm your changes: 
         
         gcloud sql instances describe INSTANCE_NAME




### REST v1

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance with an empty address list: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

Request JSON body: 
    
    {
      "settings":
      {
        "ipConfiguration":
        {
          "authorizedNetworks": []
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
    

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    




### REST v1beta4

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance with an empty address list: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

Request JSON body: 
    
    {
      "settings":
      {
        "ipConfiguration":
        {
          "authorizedNetworks": []
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
    

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    




When you remove an authorized address, existing connections from that address are _not_ disconnected. If you want to disconnect existing connections, restart your instance. 

To remove all authorized networks, use the following command: 
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-authorized-networks
      

## Disable public IP

You can disable public IP, but only if your instance is also configured to use Private IP. To enable private IP, see [Configuring an existing instance to use private IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip).

If you're using either a shared certificate authority (CA) or a customer-managed CA as the `serverCaMode` for your instance, then your instance requires a restart when you disable public IP for your instance. For more information about server CA mode configuration, see [Certificate authority (CA) authorities](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies).

**Note:** When you disable public IP for an instance, you release its IPv4 address. If you later re-enable public IP for this instance, it gets a different IPv4 address, and all applications that use the public IP address to connect to this instance must be modified.

To disable public IP:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Clear the **Public IP** checkbox.
  5. Click **Save** to update the instance.



### gcloud

  1. Update the instance: 
         
         gcloud sql instances patch INSTANCE_NAME \
         --no-assign-ip

  2. Confirm your changes: 
         
         gcloud sql instances describe INSTANCE_NAME




### REST v1

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * INSTANCE_ID: The instance ID
     * VPC_NETWORK_NAME: Specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
     * RANGE_NAME: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://tools.ietf.org/html/rfc1035) and contain 1-63 characters.
     * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.

For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated-ip).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    {
      "name": "INSTANCE_ID",
      "region": "region",
      "databaseVersion": "database-version",
      "settings": {
        "tier": "machine-type",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "privateNetwork": "projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME",
          "allocatedIpRange": "RANGE_NAME"
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          
        }
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
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

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": false
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    




### REST v1beta4

  1. Show all existing authorized addresses by describing the instance: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * ip-address1: The CIDR form of the first IP address
     * ip-address-name1: The name of the first IP address
     * ip-address2: The CIDR form of the second IP address
     * ip-address-name2: The name of the second IP address
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type4",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks":
          [
            {
              "value": "ip-address1",
              "name": "ip-address-name1",
              "kind": "sql#aclEntry"
            },
            {
              "value": "ip-address2",
              "name": "ip-address-name2",
              "kind": "sql#aclEntry"
            }
          ],
          "ipv4Enabled": true
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    

  2. Update the instance: 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * INSTANCE_ID: The instance ID
     * VPC_NETWORK_NAME: Specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
     * RANGE_NAME: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://tools.ietf.org/html/rfc1035) and contain 1-63 characters.
     * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.

For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated-ip).

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    {
      "name": "INSTANCE_ID",
      "region": "region",
      "databaseVersion": "database-version",
      "settings": {
        "tier": "machine-type",
        "ipConfiguration": {
          "ipv4Enabled": false,
          "privateNetwork": "projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME",
          "allocatedIpRange": "RANGE_NAME"
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          
        }
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  3. Confirm your changes: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * machine-type The instance machine type
     * zone The instance zone

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=settings" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "settings":
      {
        "authorizedGaeApplications": [],
        "tier": "machine-type",
        "kind": "sql#settings",
        "availabilityType": "REGIONAL",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration":
        {
          "privateNetwork": "projects/project-id/global/networks/default",
          "authorizedNetworks": [],
          "ipv4Enabled": false
        },
        "locationPreference":
        {
          "zone": "zone",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "maintenanceWindow":
        {
          "kind": "sql#maintenanceWindow",
          "hour": 0,
          "day": 0
        },
        "backupConfiguration":
        {
          "startTime": "03:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "54",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      }
    }
    




## Troubleshoot

Issue | Troubleshooting | `Aborted connection`. | The issue might be: 

  * Networking instability.
  * No response to TCP keep-alive commands (either the client or the server isn't responsive, possibly overloaded)
  * The database engine connection lifetime was exceeded and the server ends the connection.

Applications must tolerate network failures and follow [best practices](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections) such as connection pooling and retrying. Most connection poolers catch these errors where possible. Otherwise the application must either retry or fail gracefully. For connection retry, we recommend the following methods:

  1. [Exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). Increase the time interval between each retry, exponentially.
  2. Add randomized backoff also.

Combining these methods helps reduce throttling.  
---|---  
Connection timeout or generic connection error when using private IP or VPC Network Peering. | Connection attempts fail with generic timeout or connection errors without diagnostic details. **Troubleshooting steps:**

  1. Run a [Network Intelligence Center Connectivity Test](https://docs.cloud.google.com/sql/docs/sqlserver/debugging-connectivity#diagnose-vpc-connectivity) between the source client and the Cloud SQL private IP on the database port (3306 for MySQL, 5432 for PostgreSQL, or 1433 for SQL Server). The test traces the packet path and identifies whether traffic is dropped by firewall rules, missing routes, or peering misconfigurations.
  2. Verify that the VPC Network Peering connection status is `ACTIVE`.
  3. Verify that firewall rules in the VPC network allow ingress traffic on the database port.
  4. If using non-RFC 1918 address ranges, verify that you updated the peering configuration to export subnet routes with public IP.

For more details and gcloud diagnostic commands, see [Diagnose VPC network and private IP connection failures](https://docs.cloud.google.com/sql/docs/sqlserver/debugging-connectivity#diagnose-vpc-connectivity).  
Error message: `Login failed for user ""` | You might encounter this login error during [Microsoft Entra ID authentication](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id). To resolve this issue, make sure that a SQL Server login exists for this Microsoft Entra ID user.  
Network connectivity issues with private IP instances | You might experience some of the following issues during integration setup: 

  * Slow operations to create Microsoft Entra ID logins
  * Unable to create Microsoft Entra ID logins
  * Unable to connect to the instance using Microsoft Entra ID authentication

For more information on how to help address these issues, see [Troubleshooting Microsoft Entra ID integration](https://docs.cloud.google.com/sql/docs/sqlserver/integration-with-microsoft-entra-id).  
  
## What's next

  * Set up authorization for database connections. Learn more in the [Authorization options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#authentication_options)
  * [Create and manage SSL keys for your instance](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance).
  * [Connect an administration client to your instance](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
