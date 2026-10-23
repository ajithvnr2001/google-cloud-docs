---
url: https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance/
title: Configure SSL/TLS certificates \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:31.635439+00:00
---

# Configure SSL/TLS certificates  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Configure SSL/TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to enforce SSL/TLS encryption for an instance to ensure that all connections are encrypted. You can also learn more about [how Cloud SQL uses self-managed SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl) to connect to Cloud SQL instances securely.

## Overview

Cloud SQL creates a server certificate automatically when you create your instance. We recommend that you enforce all connections to use SSL/TLS.

SQL Server connections are encrypted by default and require certificate verification.

The following drivers have encryption enabled by default:

  * [Microsoft ODBC Driver 18 and later](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17)
  * [.NET: Microsoft.Data.SqlClient 4.0 and later](https://learn.microsoft.com/en-us/sql/connect/ado-net/introduction-microsoft-data-sqlclient-namespace?view=sql-server-ver17)
  * [Microsoft JDBC Driver 10.2 and later](https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-ver17)



Earlier versions of some drivers might have encryption disabled by default.

You must either install the server certificate on the client machine or pass the `TrustServerCertificate=true` flag in the client connection string. For more information, see [ODBC Driver 18.0 for SQL Server released](https://techcommunity.microsoft.com/blog/sqlserver/odbc-driver-18-0-for-sql-server-released/3169228).

Otherwise, clients can freely connect with no additional changes to their connection strings or certificates, even if you configure the instance with `sslMode` set to `ENCRYPTED_ONLY`.

For more information, see the [Enable encrypted connections to the Database Engine](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-linux-2017) section in the SQL Server documentation.

If you enforce SSL for an instance, then the instance requires a restart. A restart might also be required after you change SSL/TLS certificates. When a restart is required, Cloud SQL automatically restarts the instance for you. The restart of an instance can incur downtime. 

### Enforce SSL/TLS encryption

You can use the [SSL mode](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#ipconfiguration) setting to enforce SSL encryption in the following ways:

  * Allow both non-SSL/non-TLS and SSL/TLS connections. This is the default.

  * Only allow connections encrypted with SSL/TLS. 




If you select **Allow non-SSL/non-TLS and SSL/TLS connections** for your Cloud SQL instance, SSL/TLS connections are accepted, as well as unencrypted and unsecure connections. If you do not require SSL/TLS for all connections, unencrypted connections are still allowed. For this reason, if you are accessing your instance using public IP, we strongly recommend that you enforce SSL for all connections.

You can connect either directly to instances by using SSL/TLS certificates, or you can connect by using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-auth-proxy) or [Cloud SQL Connectors](https://docs.cloud.google.com/sql/docs/sqlserver/connect-connectors). If you connect by using Cloud SQL Auth Proxy or Cloud SQL Connectors, then the connections are automatically encrypted with SSL/TLS. With Cloud SQL Auth Proxy and Cloud SQL Connectors, client and server identities are also automatically verified regardless of the SSL mode setting.

**Note:** We recommend that you update instances using [SSL mode](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#ipconfiguration) instead of using the legacy `require-ssl` parameter. If you update the SSL enforcement configuration on an existing instance, make sure that the values don't conflict with the [`require-ssl`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#ipconfiguration) parameter. Enforcing SSL ensures that all connections are encrypted. **Note:** The Cloud SQL Auth Proxy or Cloud SQL Connectors add another layer of encryption besides SQL Server's built-in encryption. In other words, the connection between the Proxy Client/Cloud SQL Connectors and the Proxy Server would be double-encrypted. **Double encryption** can negatively impact SQL Server performance. We suggest that customers consider carefully before enforcing SSL and using Cloud SQL Auth Proxy or Cloud SQL Connectors at the same time. 

To enable requiring SSL/TLS, do the following:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Select one of the following: 
     * **Allow unencrypted network traffic (not recommended)**
     * **Allow only SSL connections.** This option only allows connections using SSL/TLS encryption.



### gcloud
    
    
       gcloud sql instances patch INSTANCE_NAME \
       --ssl-mode=SSL_ENFORCEMENT_MODE
      

Replace SSL_ENFORCEMENT_MODE with one of the following options: 

  * `ALLOW_UNENCRYPTED_AND_ENCRYPTED` allows non-SSL/non-TLS and SSL/TLS connections. This is the default value.
  * `ENCRYPTED_ONLY` only allows connections encrypted with SSL/TLS. 



### Terraform

To enforce SSL/TLS encryption, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance): 
    
    
    resource "google_sql_database_instance" "sqlserver_instance" {
      name             = "sqlserver-instance"
      region           = "asia-northeast1"
      database_version = "SQLSERVER_2019_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        tier = "db-custom-2-7680"
        ip_configuration {
          ssl_mode = "ENCRYPTED_ONLY"
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




### REST v1

  1. Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * SSL_ENFORCEMENT_MODE: Use one of the following options: 
       * `ALLOW_UNENCRYPTED_AND_ENCRYPTED`: allows non-SSL/non-TLS and SSL/TLS connections.
       * `ENCRYPTED_ONLY`: only allows connections encrypted with SSL/TLS.
     * INSTANCE_ID: The instance ID

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    {
      "settings": {
        "ipConfiguration": {"sslMode": "SSL_ENFORCEMENT_MODE"}
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

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    




### REST v1beta4

  1. Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * SSL_ENFORCEMENT_MODE: Use one of the following options: 
       * `ALLOW_UNENCRYPTED_AND_ENCRYPTED`: allows non-SSL/non-TLS and SSL/TLS connections. 
       * `ENCRYPTED_ONLY`: only allows connections encrypted with SSL/TLS.
     * INSTANCE_ID: The instance ID

HTTP method and URL: 
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    {
      "settings": {
        "ipConfiguration": {"sslMode": "SSL_ENFORCEMENT_MODE"}
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

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    




## Server certificates

Cloud SQL creates a server certificate automatically when you create your instance. As long as the server certificate is valid, you don't need to actively [manage your server certificate](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance). Cloud SQL lets you select between three different [certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies). The CA hierarchy that you select becomes the server CA mode of the instance. If you're using per-instance CA as the server CA mode for your instance, then the server certificates have an expiration date of 10 years. If you're using shared CA or customer-managed CA as the server CA mode of your instance, then the server certificate has an expiration date of 1 year*. After the expiration date, the server certificate is no longer valid, and clients can no longer establish a secure connection to your instance using that certificate. If a client is configured to verify the CA or verify the hostname in the server certificate, then that client's connections to Cloud SQL instances with expired server certificates will fail. To prevent disruption to client connections, enable [automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas) or manually rotate the server certificate before the certificate expires. You're periodically notified that the server certificate is nearing expiration. The notifications are sent the following number of days before the expiration date: 90, 30, 10, 2, and 1.

* For customer-managed CA, the expiration date of your server certificate might be shorter than 1 year if you selected a shorter expiration date for the validity period of your CA.

### List and create server certificates

To view the details of your server certificates in the Google Cloud console, go to the **Connections** page and click the **Security** tab.

In the certificates table, you can see the following details:

  * **Certificate Status** :Upcoming, Active, or Previous
    * **Upcoming** : The certificate is available for use, but isn't active. To make the certificate active, use the rotate procedure.
    * **Active** : The certificate is in use.
    * **Previous** : The certificate is no longer in use. To make the certificate active, use the rollback procedure.
  * **Created** : The date and time the certificate was created
  * **Expires** : The date and time the certificate expires



Before the active certificate expires, you can create a new certificate manually.

### Console

**For instances that use self-signed server certificates (per-instance CA)** :

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Go to the **Manage server CA certificates** section.
  6. Click to expand **Manage certificates**.
  7. Click **Create new CA certificate**.



The new server CA certificate appears in the **Upcoming** slot. If you want to rotate to the new server CA certificate immediately, proceed with [server CA certificate rotation](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#rotate) by updating your clients and completing the rotation.

**For instances that use server certificates issued by a shared CA** :

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Go to the **Manage server certificates** section.
  6. Click to expand **Manage certificates**.
  7. Click **Create server certificate**.



The new server certificate appears in the **Upcoming** slot. If you want to use the new server certificate immediately, proceed with [server certificate rotation](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#rotate-server-cert-cas) by updating your clients and completing the rotation.

### gcloud

**For instances that use self-signed server certificates (per-instance CA)** :

  1. To get information about the server certificate, use the [sql ssl server-ca-certs list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/list) command: 
         
         gcloud sql ssl server-ca-certs list \
         --instance=INSTANCE_NAME

  2. To create a server certificate, use the [sql ssl server-ca-certs create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/create) command: 
         
         gcloud sql ssl server-ca-certs create \
         --instance=INSTANCE_NAME

  3. Download the certificate information to a local PEM file: 
         
         gcloud sql ssl server-ca-certs list \
         --format="value(cert)" \
         --instance=INSTANCE_NAME > \
         FILE_PATH/FILE_NAME.pem

  4. Update all of your clients to use the new information by copying the downloaded file to your client host machines, replacing the existing `server-ca.pem` files.



**For instances that use server certificates issued by a shared CA** :

  1. To get information about the server certificate, use the [sql ssl server-certs list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/list) command: 
         
         gcloud sql ssl server-certs list \
            --instance=INSTANCE_NAME

  2. To create a server certificate, use the [sql ssl server-certs create](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/create) command: 
         
         gcloud sql ssl server-certs create \
            --instance=INSTANCE_NAME

  3. Download the certificate information to a local PEM file: 
         
         gcloud sql ssl server-certs list \
            --format="value(ca_cert.cert)" \
            --instance=INSTANCE_NAME > \
            FILE_PATH/FILE_NAME.pem

  4. Update all of your clients to use the new information by copying the downloaded file to your client host machines, replacing the existing `server-ca.pem` files.



### Terraform

To provide server certificate information as an output, use a [Terraform data source](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/sql_ca_certs): 

  1. Add the following to your Terraform configuration file: 
         
         data "google_sql_ca_certs" "ca_certs" {
              instance = google_sql_database_instance.default.name
            }
         
            locals {
              furthest_expiration_time = reverse(sort([for k, v in data.google_sql_ca_certs.ca_certs.certs : v.expiration_time]))[0]
              latest_ca_cert           = [for v in data.google_sql_ca_certs.ca_certs.certs : v.cert if v.expiration_time == local.furthest_expiration_time]
            }
         
            output "db_latest_ca_cert" {
              description = "Latest CA certificate used by the primary database server"
              value       = local.latest_ca_cert
              sensitive   = true
            }
            

  2. To create the `server-ca.pem` file, run the following command: 
         
         terraform output db_latest_ca_cert > server-ca.pem
            




## Use encrypted connections

Learn more about [how SQL Server uses encrypted connections](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-linux-2017).

## Server identity verification

Server identity verification depends on the server [certificate authority (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) configuration of your Cloud SQL instance.

For instances that use a per-instance CA, verifying the CA also verifies the server identity since each instance has a unique CA. For instances that use a shared CA, verifying the hostname along with verifying the CA is required for server identity verification since server CAs are shared across instances.

If you have per-instance CA, then you can perform DNS name-based server identity verification only for instances that are configured with Private Service Connect. If you have a shared CA, then you can perform DNS name-based server identity verification for all types of instances, namely [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect), [private service access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access), and public IP instances.

If you're using a customer-managed CA, then you can verify the CA trust chain and perform DNS name-based server identity verification for any type of instance that uses customer-managed CA for its `serverCAmode`.

When you select the customer-managed CA option for your instance, you can insert custom DNS names in the SAN field of the server certificate. For more information, see [Edit a custom SAN field](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance#edit-custom-san-instance).

You can view which CA hierarchy is configured for a Cloud SQL instance by viewing instance details. For more information, see [View instance information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info).

### Enable server identity verification

If you select shared CA as the server CA mode of your Cloud SQL instance or if you [set up custom DNS names using custom SAN values](https://docs.cloud.google.com/sql/docs/sqlserver/custom-dns-name), then we recommend that you also enable server identity verification.

Instances that use shared CA as the server CA mode contain the instance DNS name in the Subject Alternative Name (SAN) field of the server certificate. You can get this DNS name by using the instance lookup API and using the response as a hostname for server identity verification. You need to set up DNS resolution for the DNS name.

To enable server identity verification for an instance that uses a shared CA, complete the following steps:

  1. Retrieve the DNS name.

     1. To view summary information about a Cloud SQL instance, including the DNS name of the instance, use the [`gcloud sql instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
            
            gcloud sql instances describe INSTANCE_NAME \
              --project=PROJECT_ID

Make the following replacements:

        * INSTANCE_NAME: the name of the Cloud SQL instance
        * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
     2. In the response, look for the `dnsNames:` field. This field can return multiple DNS names, which have the following formats:

Network configuration | DNS name format | Name level  
---|---|---  
**Private Service Connect** or **Public IP address** | INSTANCE_UID.PROJECT_DNS_LABEL.REGION_NAME.sql.goog.  
  
**Example** :  
`1a23b4cd5e67.1a2b345c6d27.us-central1.sql.goog.` | Instance   
**Private services access** | INSTANCE_UID.PROJECT_DNS_LABEL.REGION_NAME.sql-psa.goog.  
  
**Example** :  
`1a23b4cd5e67.1a2b345c6d27.us-central1.sql-psa.goog.` | Instance   
  2. [Create the DNS record in a DNS zone](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name). If you are connecting privately, then create the DNS record in a [private DNS zone](https://docs.cloud.google.com/dns/docs/dns-overview#private_zone) in the corresponding Virtual Private Cloud (VPC) network.

  3. When you connect to the Cloud SQL for SQL Server instance, configure the DNS name or IP address as the hostname. Then enable server identity verification by specifying the `-N` flag for `sqlcmd` or by selecting the **Encrypt Connection/Encryption** option of SSMS.

Other SQL Server drivers have similar flags or configurations. 




## What's next

  * [Manage](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance) SSL/TLS certificates on your Cloud SQL instance.
  * Learn more about [how encryption is handled in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
