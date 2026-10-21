---
url: https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmad/
title: Use customer-managed Microsoft Active Directory (CMAD) \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:20.057701+00:00
---

# Use customer-managed Microsoft Active Directory (CMAD)  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/configure-cmad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use customer-managed Microsoft Active Directory (CMAD) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to use customer-managed Microsoft Active Directory (also referred to as customer-managed AD (CMAD)):

  * Integrate Cloud SQL for SQL Server with CMAD.
  * Connect to an instance with an Active Directory (AD) user.



A Cloud SQL instance that is integrated with CMAD supports [Windows Authentication](https://docs.microsoft.com/windows-server/security/windows-authentication/windows-authentication-overview) in addition to SQL Authentication.

**Note:** Before integrating, review the [Customer-managed AD overview](https://docs.cloud.google.com/sql/docs/sqlserver/cmad) page, including the section on [Limitations and alternatives](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#limitations-and-alternatives).

## Before you begin

  * In the Google Cloud console, select your [project name](https://docs.cloud.google.com/projectselector2/home/dashboard).
  * Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).
  * Install and initialize the [](https://docs.cloud.google.com/sdk/docs)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).
  * Make sure that you have the Cloud SQL Admin role on your user account. [Go to the Identity and Access Management (IAM) page](https://console.cloud.google.com/iam-admin/iam).
  * Review the [prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration).
  * Verify that [Active Directory replication](https://learn.microsoft.com/en-us/troubleshoot/windows-server/active-directory/diagnose-replication-failures) is working correctly. If not properly implemented, you might experience issues with CMAD integration.



## Create an instance with Windows Authentication

You can integrate with CMAD during [instance creation](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance), by enabling Windows Authentication for the instance. To integrate, you choose a domain for the instance to join. If joining a domain fails, instance creation fails.

In preparation for creating an instance with Windows Authentication, review the [tips](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#tips) and the [limitations and alternatives](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#limitations-and-alternatives).

While you can choose to use a public IP, the Cloud SQL instance must also have access to a private IP.

**Note:** After you create an instance with Windows Authentication, an additional Cloud SQL for SQL Server login is created for internal service use. The login is in the format `[domain]\sql_[letters-and-digits]`. For example, Cloud SQL might create a login named `AD\sql_1a1a6145bc1aaaa`. Don't remove it. If you disable Windows Authentication on the instance, then the login is automatically deleted.

Use any of the following options to create an instance that is integrated with CMAD and, as a result, enabled for Windows Authentication. For information about the basic command to create an instance, see [Creating instances](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).

### gcloud

To create an instance with CMAD, run the following:
    
    
      gcloud sql instances create INSTANCE_NAME \
      --database-version=DATABASE_VERSION \
      --root-password=PASSWORD \
      --active-directory-domain=DOMAIN \
      --active-directory-mode=CUSTOMER_MANAGED_ACTIVE_DIRECTORY \
      --active-directory-organizational-unit="OU=CLOUD_OU,DC=DC1,DC=DC2" \
      --active-directory-secret-manager-key=projects/PROJECT_ID/secrets/SECRET_NAME \
      --active-directory-dns-servers=IP1,IP2 \
      --cpu=CPU \
      --memory=MEMORY  \
      --network=NETWORK

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL for SQL Server instance you want to create.
  * DATABASE_VERSION: the database version you want to use, such as `SQLSERVER_2019_STANDARD`.
  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance will reside.
  * SECRET_NAME: is the secret you want to use.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.
  * CPU: is the amount of CPU you want to assign to the instance.
  * MEMORY: is the amount of memory you want to assign to the instance.
  * NETWORK: is the name of the network to which your instance will be connected, such as `projects/my-gcp-project-123/global/networks/my-production-vpc`.



### REST v1

To create an instance with CMAD, use a POST request with the [ users:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/users/insert) method.

Before using any of the request data, make the following replacements: 

Replace the following:

  * DATABASE_VERSION: the database version you want to use, such as `SQLSERVER_2019_STANDARD`.
  * INSTANCE_NAME: the name of the Cloud SQL for SQL Server instance you want to create.
  * REGION: the region where you want the instance to reside, such as `us-central1`.
  * PASSWORD: the password for the instance.
  * MACHINE_TYPE: the machine type you want to use for the instance, such as `db-n1-standard-8`.
  * NETWORK: is the name of the network to which your instance will be connected, such as `projects/my-gcp-project-123/global/networks/my-production-vpc`.
  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance will reside.
  * SECRET_NAME: is the secret you want to use.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
       "databaseVersion":"DATABASE_VERSION",
       "name":"INSTANCE_NAME",
       "region":"REGION",
       "rootPassword":"PASSWORD",
       "settings":{
          "tier":"MACHINE-TYPE",
          "ipConfiguration":{
             "privateNetwork":"NETWORK"
          },
          "activeDirectoryConfig":{
             "domain":"DOMAIN"
             "mode": "CUSTOMER_MANAGED_ACTIVE_DIRECTORY",
             "organizational_unit":"OU=CLOUDOU,DC=DC1,DC=DC2"
             "admin_credential_secret_name":"projects/PROJECT_ID/secrets/SECRET_NAME"
             "dns_servers":"IP1,IP2"
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
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To create an instance with CMAD, use a POST request with the [ users:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/users/insert) method.

Before using any of the request data, make the following replacements: 

Replace the following:

  * DATABASE_VERSION: the database version you want to use, such as `SQLSERVER_2019_STANDARD`.
  * INSTANCE_NAME: the name of the Cloud SQL for SQL Server instance you want to create.
  * REGION: the region where you want the instance to reside, such as `us-central1`.
  * PASSWORD: the password for the instance.
  * MACHINE_TYPE: the machine type you want to use for the instance, such as `db-n1-standard-8`.
  * NETWORK: is the name of the network to which your instance will be connected, such as `projects/my-gcp-project-123/global/networks/my-production-vpc`.
  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance will reside.
  * SECRET_NAME: is the secret you want to use.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
       "databaseVersion":"DATABASE_VERSION",
       "name":"INSTANCE_NAME",
       "region":"REGION",
       "rootPassword":"PASSWORD",
       "settings":{
          "tier":"MACHINE-TYPE",
          "ipConfiguration":{
             "privateNetwork":"NETWORK"
          },
          "activeDirectoryConfig":{
             "domain":"DOMAIN"
             "mode": "CUSTOMER_MANAGED_ACTIVE_DIRECTORY",
             "organizational_unit":"OU=CLOUDOU,DC=DC1,DC=DC2"
             "admin_credential_secret_name":"projects/PROJECT_ID/secrets/SECRET_NAME"
             "dns_servers":"IP1,IP2"
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
         "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

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
        -Uri "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME",
      "status": "RUNNING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "startTime": "2023-06-14T18:48:35.499Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Update an instance with Windows Authentication

You can update the domain of an existing instance, such as changing or adding a domain.

**Caution:** Removing Windows Authentication or changing any other parameter causes an instance to [restart](https://docs.cloud.google.com/sql/docs/sqlserver/start-stop-restart-instance#restart).

For general information about updating an instance, see [Editing instances](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance).

**Note:** Before starting the steps in this section, review the [prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#prerequisites-for-integration) and the [best practices](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#best-practices).

If an instance is currently joined with a CMAD domain, the instance is initially unjoined from that domain, before it is joined to the new domain. If the update fails, the instance might no longer be joined to any domain.

**Note:** An instance with a public IP is supported, as long as it has a private IP as well. A private IP must be enabled for the instance. Then you can choose to use public IP or private IP to connect to the instance, as long as both are available.

### gcloud

The following is an example command to update an existing instance. The command either adds or replaces a domain. Pass `--active-directory-domain=DOMAIN` to the command, as follows:
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --active-directory-domain=DOMAIN \
      --active-directory-mode=CUSTOMER_MANAGED_ACTIVE_DIRECTORY \
      --active-directory-organizational-unit="OU=CLOUDOU,DC=DOMAIN,DC=COM" \
      --active-directory-secret-manager-key=projects/PROJECT_ID/secrets/SECRET_NAME \
      --active-directory-dns-servers=IP1,IP2

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL for SQL Server instance you want to update.
  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance resides.
  * SECRET_NAME: is the secret associated with the instance.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.



### REST v1

To update a CMAD instance, use a PATCH request with the [ users:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/users/insert) method.

Before using any of the request data, make the following replacements: 

  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance resides.
  * SECRET_NAME: is the secret associated with the instance.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
        "settings":{
            "activeDirectoryConfig":{
              "domain":"DOMAIN"
              "mode": "CUSTOMER_MANAGED_ACTIVE_DIRECTORY",
              "organizational_unit":"OU=CLOUDOU,DC=DC1,DC=DC2"
              "admin_credential_secret_name":"projects/PROJECT_ID/secrets/SECRET_NAME"
              "dns_servers":"IP1,IP2"
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### REST v1beta4

To update a CMAD instance, use a PATCH request with the [ users:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/users/insert) method.

Before using any of the request data, make the following replacements: 

  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance resides.
  * SECRET_NAME: is the secret associated with the instance.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
        "settings":{
            "activeDirectoryConfig":{
              "domain":"DOMAIN"
              "mode": "CUSTOMER_MANAGED_ACTIVE_DIRECTORY",
              "organizational_unit":"OU=CLOUDOU,DC=DC1,DC=DC2"
              "admin_credential_secret_name":"projects/PROJECT_ID/secrets/SECRET_NAME"
              "dns_servers":"IP1,IP2"
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
    

## Migration between Managed Service for Microsoft Active Directory and CMAD

To migrate an instance from integration with Managed Microsoft AD to integration with CMAD, use the following [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) command:
    
    
      gcloud sql instances patch INSTANCE_NAME \
      --active-directory-domain=DOMAIN \
      --active-directory-mode=CUSTOMER_MANAGED_ACTIVE_DIRECTORY \
      --active-directory-organizational-unit="OU=CLOUDOU,DC=DOMAIN,DC=COM" \
      --active-directory-secret-manager-key=projects/PROJECT_ID/secrets/SECRET_NAME \
      --active-directory-dns-servers=IP1,IP2

Replace the following:

  * INSTANCE_NAME: the name of the Cloud SQL for SQL Server instance you want to modify.
  * DOMAIN: the domain name you want to use, such as `myaddomain.com`.
  * CUSTOMER_MANAGED_ACTIVE_DIRECTORY: indicates the mode of the domain. If the domain is created and owned by Google, then enter `MANAGED_ACTIVE_DIRECTORY`. If the domain is created and owned by the user, then enter `CUSTOMER_MANAGED_ACTIVE_DIRECTORY`.
  * CLOUD_OU: is the name of the organizational unit you want to use. For example, `CLOUDOU`. You can enter as many organizational units as needed.
  * DC1: is the first domain component used for the distinguished name of the organizational unit. For example, `DOMAIN`. You can enter as many domain components as needed.
  * DC2: is the second domain component used for the distinguished name of the organizational unit. For example, `COM`. A complete value for the `--active-directory-organizational-unit` flag might look like the following: `"OU=CLOUDOU,DC=DOMAIN,DC=COM"`. You can enter as many domain components as needed.
  * PROJECT_ID: is the project ID where the instance resides.
  * SECRET_NAME: is the secret associated with the instance.
  * IP1: is the IP address of the first DNS server you want to use, such as `10.20.30.40`. You can enter as many IP addresses as needed.
  * IP2: is the IP address of the second DNS server you want to use, such as `20.30.40.50`. You can enter as many IP addresses as needed.

**Note:** If you need to migrate back to Managed Microsoft AD from CMAD, you must first disable CMAD using a command similar to the previous example. Then, you can update the instance using a `patch` command: 
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-active-directory
      

Replace the following:

INSTANCE_NAME: the name of the instance you want to migrate.

## Connect to an instance with a user

For Cloud SQL for SQL Server, the default [user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) is `sqlserver`.

After you integrate an instance with CMAD, you can connect to the instance with the `sqlserver` user, as follows:

  1. Create a SQL Server login based on a Windows user or group, as follows: 
         
         CREATE LOGIN [domain\user_or_group] FROM WINDOWS
             

  2. Sign in to the instance, using Windows Authentication, with the instance DNS name. Examples of instance DNS names to specify include the following: 
     * Shows an example connecting through a private IP: 
           
           private.myinstance.us-central1.myproject.cloudsql.mydomain.com
                 

     * Shows an example connecting through a public IP: 
           
           public.myinstance.us-central1.myproject.cloudsql.mydomain.com
                   

     * Shows an example connecting through the Cloud SQL Auth Proxy: 
           
           proxy.myinstance.us-central1.myproject.cloudsql.mydomain.com
                   

For more information, see Use the Cloud SQL Auth Proxy with Windows Authentication.




If you use the instance IP address, you must [configure](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip) the Kerberos clients to support IP hostnames. Cloud SQL doesn't support signing in using IP addresses from domains connected through a trust relationship. 

## Use the Cloud SQL Auth Proxy with Windows Authentication

You can use the Cloud SQL Auth Proxy with your CMAD integration.

Before you begin, review the following:

  * [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/sql-proxy)
  * [Connecting using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy)



### Steps for Windows Authentication

For background on starting the Cloud SQL Auth Proxy, see [Start the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy#start-proxy).

For Windows Authentication, you must run the Cloud SQL Auth Proxy on port 1433. To map a predefined Service Principal Name (SPN) entry to a Cloud SQL Auth Proxy address, use the following command:
    
    
    Proxy.[instance].[location].[project].cloudsql.[domain]

**Note:** Cloud SQL supports connection with [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/ssms/sql-server-management-studio-ssms).

### Run the Cloud SQL Auth Proxy locally

If you run the Cloud SQL Auth Proxy locally, use your hosts file to map the following to `127.0.0.1`:
    
    
    Proxy.[instance].[location].[project].cloudsql.[domain]

As an example, you could add the following to the hosts file (for example, to `c:\windows\system32\drivers\etc\hosts`):
    
    
    127.0.0.1 proxy.[instance].[location].[project].cloudsql.[domain]

In that example, you could run the Cloud SQL Auth Proxy using this command, and make it available on `127.0.0.1:1433`:
    
    
    cloud-sql-proxy.exe --credentials-file credential.json project:name

## Run the Cloud SQL Auth Proxy non-locally

To run the Cloud SQL Auth Proxy externally, follow the instructions in Running the Cloud SQL Auth Proxy locally, but use a different entry in the hosts file.

Specifically, if a non-local host is, for example, MyOtherHost, you could add the following to the hosts file:
    
    
    127.0.0.1 MyOtherHost proxy.[instance].[location].[project].cloudsql.[domain]

### Troubleshoot for NTLM fallback in clients

If you use Windows Authentication and an instance IP address to sign in to an instance, you must [configure](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip) a Kerberos client to support IP hostnames.

Cloud SQL doesn't support NTLM authentication, but some Kerberos clients might try to fall back to it. As discussed in this section, if you try to connect with SQL Server Management Studio (SSMS), and the following error message occurs, a likely cause is NTLM fallback:
    
    
    Login failed. The login is from an untrusted domain and cannot be used with
    Integrated authentication. (Microsoft SQL Server, Error: 18452)
    

NTLM is a set of Microsoft security protocols for authentication. For more information, see Reasons for NTLM fallback.

### Verification of an NTLM fallback for a Windows client

From a Windows terminal, to verify that an NTLM fallback caused an error, complete the following:

  1. Sign in with the on-premises credentials you want to use. Don't use `"Run as..."` commands.
  2. Open a command prompt.
  3. Run `klist purge`.
  4. From SSMS, try to connect to SQL Server with Windows Authentication.
  5. Run `klist` and check if there's a ticket issued for the returned error, 
         
         MSSQLSvc/:1433 @ domain.

  6. If there's no such ticket, NTLM fallback is the likely cause for the error.
  7. If there is such a ticket, check that your SQL Server driver doesn't enforce NTLM authentication. Also, check if NTLM authentication is enforced through a Group Policy.



### Verify the NTLM fallback for a Linux client

From Ubuntu 16.04, to verify that an NTLM fallback caused an error, use the steps in this section. The steps are similar to those for other Linux distributions.

#### Set up Kerberos authentication

  1. Set up a Kerberos client: 
         
         sudo apt-get install krb5-user
             

  2. When you are prompted for the default realm, type an on-premises domain name, using uppercase letters.
  3. Run the following command to install SQL Server command-line tools: 
         
         curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
               curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list
               sudo apt-get update
               sudo apt-get install mssql-tools unixodbc-dev
             




#### Connect with Windows Authentication

  1. Run the kinit tool as follows: 
         
         kinit     

  2. To connect with Windows Authentication, run the following: 
         
         /opt/mssql-tools/bin/sqlcmd -S 
             

  3. Run the klist command and check whether a ticket was issued specifically for the following returned message: 
         
         MSSQLSvc/:1433 @ domain
             

  4. If the ticket wasn't issued, the previous error likely indicates an issue that causes NTLM fallback.



#### Reasons for NTLM fallback

Fallback to NTLM is a client misconfiguration that can be associated with the following conditions:

  * By default, Windows doesn't attempt Kerberos authentication for a host if the hostname is an IP address. To enable Kerberos authentication for IP addresses, try the method described in [Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip).
  * Kerberos authentication over external trusts doesn't work. [Use forest trusts instead](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-trust).
  * Kerberos authentication requires name suffix routing to enable the finding of services in another forest. Try the method described in [Set up a trust relationship between two domains](https://learn.microsoft.com/en-us/archive/msdn-technet-forums/9e501d72-5457-421a-b81b-3a1f83ac7b0e).
  * Kerberos authentication doesn't work if there's no SPN registered for the service. Use only FQDNs or IP addresses you obtain from the Google Cloud console to connect with Windows Authentication.



## Create a Windows login for on-premises AD users

Follow the [`CREATE LOGIN` instructions](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-login-transact-sql?view=sql-server-ver15) for creating a Windows login for an on-premises user. For example, specify a command similar to the following:
    
    
    CREATE LOGIN [DOMAIN_NAME\USER_NAME] FROM WINDOWS

## Tips for using CMAD with Cloud SQL

**Note:** In addition to reviewing the tips in this section, see [Limitations and alternatives](https://docs.cloud.google.com/sql/docs/sqlserver/cmad#limitations-and-alternatives).

  * An instance with public IP is supported, as long as it has private IP as well. Private IP must be enabled for the instance. Then, you can choose to use a public IP or a private IP to connect to the instance, as long as both are available.
  * Before creating an instance, including as a replacement instance, review the following: 
    * [Learn about using private IP](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip)
    * [Configure public IP](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip)
  * If Windows Authentication fails from a domain that is connected through a trust relationship, verify that Windows Authentication works for a user from a customer-managed domain. If it does, then complete the following: 
    1. Verify that you used a DNS name. IP addresses aren't supported from domains connected using a trust relationship.
    2. Make sure you completed the steps in [Setup a trust relationship between two domains](https://learn.microsoft.com/en-us/archive/msdn-technet-forums/9e501d72-5457-421a-b81b-3a1f83ac7b0e), including the opening of all firewall ports.
    3. Validate the trust.
    4. Verify that the direction of the trust allows users from the domain (connected through a trust relationship) to authenticate.
    5. Follow the steps described in [Prepare a nonroutable domain for directory synchronization](https://learn.microsoft.com/en-us/microsoft-365/enterprise/prepare-a-non-routable-domain-for-directory-synchronization?view=o365-worldwide).
    6. Verify that the trust works without using Cloud SQL for SQL Server: 
       1. Create a Windows VM.
       2. Join it to the CMAD domain.
       3. Try to run, for example, Notepad as a user from the domain that is connected through a trust relationship.
    7. Restart the client VM and retest Windows Authentication.
  * You may try to create a SQL Server login, but then receive the following error: 
        
        Windows NT user or group domain\name not found. Check the name again.
            

This may have occurred because domain local groups are not supported; if applicable, use global or universal groups instead.

  * If SQL Server queries result in the following error, note that IP addresses aren't supported for users from domains connected through a trust relationship: 
        
        The login is from an untrusted domain.
            

The following actions might resolve this issue:

    * If an IP address is used to connect users from a managed domain, follow the instructions in [Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/security/kerberos/configuring-kerberos-over-ip).
    * Avoid using any proxies, and always use the same DNS name to connect to Cloud SQL for SQL Server, as you see the name in the Google Cloud console.
  * If an instance has ongoing problems with Windows Authentication (whether or not the instance was recently updated), try unjoining it from the domain and then rejoining it. To do so, use the [update procedure](https://docs.cloud.google.com/sql/docs/sqlserver/update-an-instance-with-windows-authentication) to unjoin and then to rejoin the domain. Doing so doesn't remove any existing Windows-authenticated users or logins that exist in your databases. However, removing Windows Authentication causes an instance to [restart](https://docs.cloud.google.com/sql/faq#shutdown).
  * [Use the customer-managed Active Directory Diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/cmad-diagnosis-tool) to troubleshoot Active Directory setup issues with your customer-managed domain.



## Troubleshoot

The following table lists common error messages and ways to help address them:

For this error... | The issue might be... | Try this...  
---|---|---  
`Per-product, per-project Service Account (P4 SA) not found for project.` | The service account name is incorrect. | On the [ Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts), make sure you created a service account for the correct user project.  
`The operation completed but an update to Active Directory failed. You may experience issues with Windows Authentication on this instance, please see https://cloud.google.com/sql/docs/sqlserver/configure-cmad for tips.` | The required updates couldn't be performed on the CMAD domain. | If you experience issues with Windows Authentication, you can try unjoining the CMAD domain and then rejoining it. To do so, use the update procedure to unjoin and then to rejoin the domain. Doing so doesn't remove any existing Windows-authenticated users or logins that exist in your databases. However, removing Windows Authentication causes an instance to [restart](https://docs.cloud.google.com/sql/faq#shutdown).  
`This instance would need new network architecture to support Active Directory. See https://cloud.google.com/sql/docs/sqlserver/configure-cmad."` | This instance doesn't use the new network architecture. | [Upgrade the instance to the new network architecture.](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture)  
`Admin credential secret name / Organizational unit / DNS Server names is required or Invalid Admin credential secret name / OrganizationalUnit / DNS Server names provided.` | Admin credentials, Organization unit, and DNS Servers are required parameters. | Retry your request with these parameters specified.  
`Integration failed due to insufficient permissions. The Service Agent for this project must be granted the secretmanager.secrets.getIamPolicy and secretmanager.secrets.setIamPolicy permissions on the provided admin credential key in Secret Manager.` | The Service Agent for this project lacks necessary permissions. | Create a custom role with `secretmanager.secrets.getIamPolicy` and `secretmanager.secrets.setIamPolicy` permissions and assign it to the service agent for this project. For more information, see [Secret Manager roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager).  
  
## What's next

  * [Customer-managed Active Directory (CMAD) overview](https://docs.cloud.google.com/sql/docs/sqlserver/cmad)
  * [Use the customer-managed Active Directory Diagnosis tool](https://docs.cloud.google.com/sql/docs/sqlserver/cmad-diagnosis-tool)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
