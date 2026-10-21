---
url: https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip/
title: Configure private IP \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:34.750756+00:00
---

# Configure private IP  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Configure private IP Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/configure-private-ip "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip "View this page for the SQL Server database engine")

This page describes how to configure a Cloud SQL instance to use private IP.

For information about how private IP works, as well as environment and management requirements, see [Private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Service Networking API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Service Networking API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=servicenetworking.googleapis.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles and permissions

To get the permissions that you need to create and manage a private services access connection, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on on the project where you plan to host your Cloud SQL instance. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage a private services access connection. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage a private services access connection:

  * `compute.addresses.create`
  * `compute.addresses.list`
  * `compute.globalAddresses.create`
  * `compute.globalAddresses.createInternal`
  * `compute.globalAddresses.list`
  * `compute.networks.list`
  * `compute.networks.use`
  * `servicenetworking.services.addPeering`
  * `serviceusage.services.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Important:** If you're using a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc), then you need to enable the same APIs, add the same user, and provide the same permissions to the user in the host project.

### Private services access

When you [create a new Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) in your project, you need to [configure private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#configure-access) to allocate an IP address range and create a private services access connection. This allows resources in the VPC network to connect to Cloud SQL instances. The Google Cloud console provides a wizard to help you set up this configuration.

Assigning different VPC networks to Cloud SQL for MySQL instances with private IP addresses provides better isolation than attaching all of them to the `default` VPC network. 

## Configure an instance to use private IP

You can configure a Cloud SQL instance to use private IP when you create the instance, or for an existing instance.

After you configure an instance to use private IP, you cannot disable private IP connectivity for that instance.   


If you choose to let Cloud SQL allocate your private IP for an instance, the addresses for all instances you later configure in that VPC network are automatically allocated in the same IP address range.

For each project, there's an internal limit for the number of different network-region combinations in which Cloud SQL instances can be setup with Private Services Access. To avoid reaching this limit, we recommend reusing existing available networks. 

### Configure private IP for a new instance

To configure a Cloud SQL instance to use private IP when creating an instance:

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. Expand **Show configuration options**.
  4. Expand **Connections**.
  5. Select **Private IP**. 

A drop-down list shows the available VPC networks in your project. If your project is the service project of a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), then VPC networks from the host project are also shown. 

  6. Select the VPC network you want to use.

If you see a message indicating that you need to set up a private service connection, do the following:

     1. Click **Set up connection**.
     2. In the **Allocate an IP range** section, select one of the following options: 
        * Select one or more existing IP ranges or create a new one from the dropdown. The dropdown includes previously allocated ranges, if there are any, or you can select **Allocate a new IP range** and enter a new range and name.
        * **Use an automatically allocated IP range in your network**.
**Note:** You can specify an address range only for a primary instance, not for a read replica or clone.
     3. Click **Continue**.
     4. Click **Create connection**.
     5. Verify that you see the message: `Private service connection for network VPC_NETWORK_NAME has been successfully created`.
  7. Optionally, you can specify an allocated IP range for your instances to use for connections. 
     1. Expand **Show allocated IP range option**.
     2. Select an IP range from the drop-down menu.
  8. Optional. If you want to allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private IP connection, then select **Enable private path**.
  9. Finish configuring your instance.
  10. Click **Create instance**.



### gcloud

Before you create an instance using a private IP address, ensure that your project is configured for [ private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access).

**Prerequisites for Private IP using private services access on new projects:**

If you are creating a private IP instance in a new or empty project, you must first enable the Service Networking API and then you establish VPC Network Peering with Google services. Otherwise, instance creation will fail with `SERVICE_NETWORKING_NOT_ENABLED` or `NETWORK_NOT_PEERED`.

Run the following [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands to set up private services access networking for Cloud SQL:

  1. **Enable the required APIs:**
         
         gcloud services enable \
             sqladmin.googleapis.com \
             compute.googleapis.com \
             servicenetworking.googleapis.com \
             --project=PROJECT_ID
             

  2. **Allocate an IP address range for VPC Network Peering:**
         
         gcloud compute addresses create google-managed-services-VPC_NETWORK_NAME \
             --global \
             --purpose=VPC_PEERING \
             --prefix-length=16 \
             --network=projects/NETWORK_PROJECT_ID/global/networks/VPC_NETWORK_NAME \
             --project=PROJECT_ID
             

  3. **Establish the VPC Network Peering connection:**
         
         gcloud services vpc-peerings connect \
             --service=servicenetworking.googleapis.com \
             --ranges=google-managed-services-VPC_NETWORK_NAME \
             --network=VPC_NETWORK_NAME \
             --project=PROJECT_ID
             




Before using any of the request data, make the following replacements:

  * `INSTANCE_ID`: The instance ID
  * `PROJECT_ID`: The project ID
  * `NETWORK_PROJECT_ID`: The project ID of the VPC network

**Note:** If the VPC network is a Shared VPC, then `PROJECT_ID` must be the ID of the Shared VPC service project, and `NETWORK_PROJECT_ID` must be the ID of the Shared VPC host project.

  * `VPC_NETWORK_NAME`: The name of the VPC network 
  * `RANGE_NAME`: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://datatracker.ietf.org/doc/html/rfc1035) and contain 1-63 characters.
  * `REGION_NAME`: The region name

To specify the name of your VPC network, use the `--network` parameter. To disable public IP, use the `--no-assign-ip` flag. 

Also, optionally, use the `--enable-google-private-path` parameter to allow other Google Cloud services such as BigQuery to access data in Cloud SQL and make queries against this data over a private IP connection. This parameter is valid only if: 

  * You use the `--no-assign-ip` parameter.
  * You use the `--network` parameter to specify the name of the VPC network that you want to use to create a private connection.

To enforce the use of the new network architecture for the instance, use the [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create#--enforce-new-sql-network-architecture) flag. Make sure that you have allocated enough IP addresses. When you use new network architecture enforcement before a project is fully upgraded, you might experience instance creation failure if sufficient IP address space isn't available. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip). 

**Note:** After you create an instance, you can't assign an allocated range name for that instance. After you assign a range to an instance, you can't modify the range.
    
    
    gcloud beta sql instances create INSTANCE_ID \
    --project=PROJECT_ID \
    --network=projects/NETWORK_PROJECT_ID/global/networks/VPC_NETWORK_NAME \
    --no-assign-ip \
    --allocated-ip-range-name=RANGE_NAME \
    --enable-google-private-path \
    --enforce-new-sql-network-architecture

### Terraform

To configure private IP for a new instance, use the following Terraform resources:

  * [`google_compute_network`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network)
  * [`google_compute_global_address`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_address)
  * [`google_service_networking_connection`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/service_networking_connection)
  * [`google_sql_database_instance`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance)


    
    
    resource "google_compute_network" "peering_network" {
      name                    = "private-network"
      auto_create_subnetworks = "false"
    }
    
    resource "google_compute_global_address" "private_ip_address" {
      name          = "private-ip-address"
      purpose       = "VPC_PEERING"
      address_type  = "INTERNAL"
      prefix_length = 16
      network       = google_compute_network.peering_network.id
    }
    
    resource "google_service_networking_connection" "default" {
      network                 = google_compute_network.peering_network.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
    }
    
    resource "google_sql_database_instance" "instance" {
      name             = "private-ip-sql-instance"
      region           = "us-central1"
      database_version = "MYSQL_8_0"
    
      depends_on = [google_service_networking_connection.default]
    
      settings {
        tier = "db-f1-micro"
        ip_configuration {
          ipv4_enabled    = "false"
          private_network = google_compute_network.peering_network.id
        }
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }
    
    resource "google_compute_network_peering_routes_config" "peering_routes" {
      peering              = google_service_networking_connection.default.peering
      network              = google_compute_network.peering_network.name
      import_custom_routes = true
      export_custom_routes = true
    }
    
    
    ## Uncomment this block after adding a valid DNS suffix
    
    # resource "google_service_networking_peered_dns_domain" "default" {
    #   name       = "example-com"
    #   network    = google_compute_network.peering_network.name
    #   dns_suffix = "example.com."
    #   service    = "servicenetworking.googleapis.com"
    # }
    
    

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

Create a new instance with a private IP address:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * VPC_NETWORK_NAME: Specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * RANGE_NAME: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://tools.ietf.org/html/rfc1035) and contain 1-63 characters.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.



For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

If you set the `enablePrivatePathForGoogleCloudServices` parameter to `true`, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private IP connection. By setting this parameter to `false`, other Google Cloud services can't access data in Cloud SQL over a private IP connection.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

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
          
          "enablePrivatePathForGoogleCloudServices": true
          
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
    

### REST v1beta4

Create a new instance with a private IP address:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * VPC_NETWORK_NAME: Specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * RANGE_NAME: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://tools.ietf.org/html/rfc1035) and contain 1-63 characters.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.



For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

If you set the `enablePrivatePathForGoogleCloudServices` parameter to `true`, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private IP connection. By setting this parameter to `false`, other Google Cloud services can't access data in Cloud SQL over a private IP connection.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances

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
          
          "enablePrivatePathForGoogleCloudServices": true
          
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
    

### Configure private IP for an existing instance

Configuring an existing Cloud SQL instance to use private IP causes the instance to restart, resulting in downtime.

**Note:** You can't assign a private IP address for an existing Cloud SQL instance in a Shared VPC network. You also can't assign an allocated range name for an existing instance.

To configure an existing instance to use private IP:

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the Cloud SQL navigation menu.
  4. On the **Networking** tab, select the **Private IP** checkbox. 

A drop-down list shows the available networks in your project. 

  5. Select the VPC network you want to use:

If you see **Private service connection required** :

     1. Click **Set up connection**.
     2. In the **Allocate an IP range** section, choose one of the following options: 
        * Select one or more existing IP ranges or create a new one from the dropdown. The drop down includes previously allocated ranges, if there are any, or you can select **Allocate a new IP range** and enter a new range and name.
        * Use an automatically allocated IP range in your network.
**Note:** You can specify an address range only for a primary instance, not for a read replica or clone.
     3. Click **Continue**.
     4. Click **Create connection**.
     5. Verify that you see the **Private service connection for network` VPC_NETWORK_NAME` has been successfully created** status. 
  6. Optional. If you want to allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private IP connection, then select the **Enable private path** check box.
  7. Click **Save**.



### gcloud

Ensure your project is configured for [ private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access).

Update your Cloud SQL instance by using the `--network` parameter to specify the name of your selected VPC network.

To enforce the use of the new network architecture for the instance when you add a private IP network configuration, use the [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/patch#--enforce-new-sql-network-architecture) flag. Make sure that you have allocated enough IP address space in your IP range. When you use new network architecture enforcement before a project is fully upgraded, you might experience instance creation failure if sufficient IP address space isn't available.

For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).
    
    
    gcloud beta sql instances patch INSTANCE_ID \
    --project=PROJECT_ID \
    --network=projects/NETWORK_PROJECT_ID/global/networks/VPC_NETWORK_NAME \
    --no-assign-ip \
    --enable-google-private-path \
    --enforce-new-sql-network-architecture

### REST v1

Create a new instance with a private IP address:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * VPC_NETWORK_NAME: Specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * RANGE_NAME: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://tools.ietf.org/html/rfc1035) and contain 1-63 characters.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.



For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

If you set the `enablePrivatePathForGoogleCloudServices` parameter to `true`, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private IP connection. By setting this parameter to `false`, other Google Cloud services can't access data in Cloud SQL over a private IP connection.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":
      {
        "ipConfiguration": {
          "ipv4Enabled": false,
          "privateNetwork": "projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME",
          "allocatedIpRange": "RANGE_NAME"
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          
          "enablePrivatePathForGoogleCloudServices": true
          
        }
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

Create a new instance with a private IP address:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The project ID
  * INSTANCE_ID: The instance ID
  * VPC_NETWORK_NAME: Specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * RANGE_NAME: _Optional._ If specified, sets a range name for which an IP range is allocated. The range name must comply with [`RFC-1035`](https://tools.ietf.org/html/rfc1035) and contain 1-63 characters.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.



For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

If you set the `enablePrivatePathForGoogleCloudServices` parameter to `true`, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private IP connection. By setting this parameter to `false`, other Google Cloud services can't access data in Cloud SQL over a private IP connection.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":
      {
        "ipConfiguration": {
          "ipv4Enabled": false,
          "privateNetwork": "projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME",
          "allocatedIpRange": "RANGE_NAME"
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          
          "enablePrivatePathForGoogleCloudServices": true
          
        }
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
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

#### Response
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-21T22:43:37.981Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Connect to an instance using its Private IP

You use [private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access) to connect to Cloud SQL instances from Compute Engine or Google Kubernetes Engine instances in the same VPC network (defined here as _internal_ sources) or from outside of that network (an _external_ source).

### Connect from an internal source

To connect from a source in the same Google Cloud project as your Cloud SQL instance, such as the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) running on a Compute Engine resource, that resource must be in the same VPC network where private services access has been established for the Cloud SQL instance.

To connect from a serverless source, such as [App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard#connecting_to), [Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run#connecting_to), or [Cloud Run functions](https://docs.cloud.google.com/sql/docs/mysql/connect-functions#connecting_to), your application or function connects directly to your instance through Serverless VPC Access without the Cloud SQL Auth Proxy. 

### Connect from an external source

If an external network (for example, an on-premises network or a VPC network), is connected to the VPC network to which your Cloud SQL instance is connected, then you can use [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) to connect to the instance from a client in the external network.

To permit connections from an external network, do the following:

  1. Ensure your VPC network is connected to the external network using a [ Cloud VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or a VLAN attachment for [ Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview) or [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview). 
  2. Ensure the Border Gateway Protocol (BGP) sessions on the Cloud Routers managing your Cloud VPN tunnels and Cloud Interconnect attachments (VLANs) have received specific prefixes (destinations) from your on-premises network. 

Default routes (destination 0.0.0.0/0) cannot be imported into the Cloud SQL VPC network because that network has its own local default route. Local routes for a destination are used even though the Cloud SQL peering is configured to import custom routes from your VPC network.

  3. [ Identify the peering connections](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing-connections) produced by the private services connection. Depending on the service, the private services connection might create one or more of the following peering connections, but not necessarily all of them: 
     * `cloudsql-mysql-googleapis-com`
     * `cloudsql-postgres-googleapis-com`
     * `servicenetworking-googleapis-com`
  4. [ Update **all** of the peering connections ](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection) to enable **Export custom routes**.
  5. [ Identify the allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing_allocated_ip_address_ranges) used by the private services connection.
  6. [ Configure Cloud Router custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for the allocated range on the Cloud Routers managing BGP sessions for your Cloud VPN tunnels or Cloud Interconnect attachments (VLANs). 

**Note:** If you're using a [non-RFC 1918 IP address range](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for your application, then to allow access from this range, [configure the authorized network](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) for your instance.




### Connect from Cloud Shell

[Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) uses a Compute Engine virtual machine that's managed by Google Cloud and is outside of your VPC network. Therefore, a connectivity path doesn't exist between Cloud Shell and the private IP address space of the your VPC network.

As a result, Cloud Shell doesn't support connecting to a Cloud SQL instance that has only a private IP address.

To connect to Cloud SQL instances from an external network using Private IP connectivity, see [ Connect to a Cloud SQL instance from outside its VPC](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-from-outside-vpc).

### Connect from non-RFC 1918 IP addresses

[RFC 1918](https://tools.ietf.org/html/rfc1918) specifies IP addresses that are assigned to be used internally (that is, within an organization) and will not route on the Internet. Specifically, these are:

  * 10.0.0.0/8
  * 172.16.0.0/12
  * 192.168.0.0/16



Connections to a Cloud SQL instance using a private IP address are automatically authorized for [RFC 1918 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). This way, all private clients can access the database without going through the proxy.

**Note:** You must configure all the non-RFC 1918 IP address ranges as [authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks) of the Cloud SQL for MySQL instances. Alternatively, you can connect to your instance using the [Cloud SQL Auth Proxy client](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).

To connect from a non-RFC 1918 IP address, you must set per-instance IP authorization to allow traffic from non-RFC 1918 IP address ranges.

For example, use a `gcloud` command like the following:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --authorized-networks=192.88.99.0/24,11.0.0.0/24

**Note:** This command overwrites all existing authorized networks, so you must include all desired authorized networks.

Cloud SQL doesn't learn non-RFC 1918 subnet routes from your VPC network by default. You need to update the network peering to Cloud SQL to export any non-RFC 1918 routes.
    
    
    gcloud compute networks peerings update PEERING_CONNECTION \
    --network=VPC_NETWORK_NAME \
    --export-subnet-routes-with-public-ip \
    --project=PROJECT_ID

Replace the following:

  * `PEERING_CONNECTION` is the [name of the peering connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#listing-connections) produced by the private services connection between your VPC network and the service producer network. 
  * `VPC_NETWORK_NAME` is the name of your VPC network.
  * `PROJECT_ID` is the ID of the project of the VPC network. If you're using Shared VPC, then use the host project ID.



To mitigate IP address exhaustion, you can use [privately used public IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#pupi-addresses).

#### Connect from privately used public IP addresses

If you want to configure your instance in a privately used public IP address range, then enable `export-subnet-routes-with-public-ip` on the network peering between your network and the Cloud SQL network.
    
    
    gcloud compute networks peerings update PEERING_CONNECTION \
    --network=VPC_NETWORK_NAME \
    --export-subnet-routes-with-public-ip \
    --project=PROJECT_ID

Replace the following:

  * `PEERING_CONNECTION` is the name of the peering connection produced by the private services connection between your VPC network and the service producer network. To know the name of the peering connection, go to the [VPC network peering](https://console.cloud.google.com/networking/peering/) page. 
  * `VPC_NETWORK_NAME` is the name of your VPC network.
  * `PROJECT_ID` is the ID of the project of the VPC network. If you're using Shared VPC, then use the host project ID.



#### Connect to an instance configured with privately used public IP addresses

If your instance is configured in a privately used public IP address range and you want to connect to it, then enable `import-subnet-routes-with-public-ip` on the network peering between your network and the Cloud SQL network.
    
    
    gcloud compute networks peerings update PEERING_CONNECTION \
    --network=VPC_NETWORK_NAME \
    --import-subnet-routes-with-public-ip \
    --project=PROJECT_ID

Replace the following:

  * `PEERING_CONNECTION` is the name of the peering connection produced by the private services connection between your VPC network and the service producer network. To know the name of the peering connection, go to the [VPC network peering](https://console.cloud.google.com/networking/peering/) page.
  * `VPC_NETWORK_NAME` is the name of your VPC network.
  * `PROJECT_ID` is the ID of the project of the VPC network. Use the host project ID if you're using Shared VPC.



### Connect by using a write endpoint

In addition to a private IP address, you can use a write endpoint in a SQL connection string. A write endpoint is a global domain name service (DNS) name that resolves to the IP address of the current primary instance automatically. By using a write endpoint, you can avoid having to make application connection changes when a region failure occurs.

If a replica [failover or switchover](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas) occurs, then the write endpoint can help manage private IP addresses of instances. When this happens, use the write endpoint to connect to the instance that acts as the primary instance.

**Note** : A write endpoint is available only for Cloud SQL Enterprise Plus edition instances that have private IP addresses and associated networks. For more information on creating instances that meet this criteria, see [Create instances](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

#### How Cloud SQL creates a write endpoint

If you enable the Cloud DNS API for your Google Cloud project, and then you [create a primary Cloud SQL Enterprise Plus edition instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance), [promote the replica for the instance](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#promote-replica), or [upgrade the instance from Cloud SQL Enterprise edition](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place), Cloud SQL generates a write endpoint automatically and assigns it to the instance.

If the primary instance changes during the switchover or failover processes, then Cloud SQL assigns the write endpoint to the failover replica because this replica is the new primary instance. 

For more information, see [View the write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint#view_the_write_endpoint).

#### Assign a write endpoint to an instance

If you don't enable the Cloud DNS API for your Google Cloud project, and then you create, promote, or upgrade your instance, Cloud SQL doesn't assign the write endpoint to the instance automatically.

To have Cloud SQL generate a write endpoint and assign it to the instance, see [Generate the write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint).

## Troubleshoot

See [ troubleshooting](https://docs.cloud.google.com/sql/docs/mysql/troubleshooting#connectivity) for known connectivity issues, and also [ debugging connection issues](https://docs.cloud.google.com/sql/docs/mysql/debugging-connectivity) for help with self-diagnostics.

## What's next

  * Learn more about [private IP](https://docs.cloud.google.com/sql/docs/mysql/private-ip).
  * Learn more about [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access).
  * See how to use [VPC Service Controls](https://docs.cloud.google.com/sql/docs/mysql/admin-api/configure-service-controls) to add a service perimeter.
  * Learn more about [configuring private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).
  * Learn more about [configuring private services access for Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#configure-access).
  * Learn more about [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * Learn more about [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).
  * Learn more about [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).
  * Learn more about [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
