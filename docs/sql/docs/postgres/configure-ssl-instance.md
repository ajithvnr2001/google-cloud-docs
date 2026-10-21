---
url: https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance/
title: Configure SSL/TLS certificates \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:56.585261+00:00
---

# Configure SSL/TLS certificates  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/configure-ssl-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Configure SSL/TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance "View this page for the SQL Server database engine")

This page describes how to enforce SSL/TLS encryption for an instance to ensure that all connections are encrypted. You can also learn more about [how Cloud SQL uses self-managed SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl) to connect to Cloud SQL instances securely.

## Overview

Cloud SQL creates a server certificate automatically when you create your instance. We recommend that you enforce all connections to use SSL/TLS.

To validate the client certificate and the server's identity using SSL/TLS certificates, you must create a client certificate and download the certificates to your PostgreSQL client host machine.

**Note:** Cloud SQL recommends mutual authentication, which involves using certificates to authenticate both the client and server. Enforcing SSL/TLS encryption with valid client certificates makes mutual TLS required for all clients. However, if SSL/TLS is not enforced with valid client certificates, then connecting with non-mutual TLS using the server certificate is still possible. 

For more information, consult [the documentation for your database engine](https://www.postgresql.org/docs/current/ssl-tcp.html#SSL-SERVER-FILES). 

When you enforce SSL for an instance, the instance does not require a restart. However, changes to SSL/TLS certificates might result in an automatic restart of the instance and can incur downtime. 

A change to SSL mode configuration applies only to new connections. If you enforce SSL and your instance has existing unencrypted connections, then the connections stay connected and unencrypted. To close any unencrypted connections and enforce SSL on all connections, you must restart your instance.

### Enforce SSL/TLS encryption

You can use the [SSL mode](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances#ipconfiguration) setting to enforce SSL encryption in the following ways:

  * Allow both non-SSL/non-TLS and SSL/TLS connections. The client certificate isn't verified for SSL/TLS connections. This is the default.

  * Only allow connections encrypted with SSL/TLS. The client certificate isn't verified for SSL connections.



  * Only allow connections encrypted with SSL/TLS and with valid client certificates.



If you select **Allow non-SSL/non-TLS and SSL/TLS connections** for your Cloud SQL instance, SSL/TLS connections are accepted, as well as unencrypted and unsecure connections. If you do not require SSL/TLS for all connections, unencrypted connections are still allowed. For this reason, if you are accessing your instance using public IP, we strongly recommend that you enforce SSL for all connections.

You can connect either directly to instances by using SSL/TLS certificates, or you can connect by using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/connect-auth-proxy) or [Cloud SQL Connectors](https://docs.cloud.google.com/sql/docs/postgres/connect-connectors). If you connect by using Cloud SQL Auth Proxy or Cloud SQL Connectors, then the connections are automatically encrypted with SSL/TLS. With Cloud SQL Auth Proxy and Cloud SQL Connectors, client and server identities are also automatically verified regardless of the SSL mode setting.

**Note:** We recommend that you update instances using [SSL mode](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances#ipconfiguration) instead of using the legacy `require-ssl` parameter. If you update the SSL enforcement configuration on an existing instance, make sure that the values don't conflict with the [`require-ssl`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances#ipconfiguration) parameter.

To enable requiring SSL/TLS, do the following:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Select one of the following: 
     * **Allow unencrypted network traffic (not recommended)**
     * **Allow only SSL connections.** This option only allows connections using SSL/TLS encryption. Certificates aren't validated.
     * **Require trusted client certificates.** This option only allows connections from clients that use a valid client certificate and are SSL encrypted. If a client or user connects using [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication), then they must use either the Cloud SQL Auth Proxy or Cloud SQL Connectors to enforce client identity verification.



### gcloud
    
    
       gcloud sql instances patch INSTANCE_NAME \
       --ssl-mode=SSL_ENFORCEMENT_MODE
      

Replace SSL_ENFORCEMENT_MODE with one of the following options: 

  * `ALLOW_UNENCRYPTED_AND_ENCRYPTED` allows non-SSL/non-TLS and SSL/TLS connections. For SSL connections, the client certificate is not verified. This is the default value.
  * `ENCRYPTED_ONLY` only allows connections encrypted with SSL/TLS. The client certificate isn't verified for SSL connections. 
  * `TRUSTED_CLIENT_CERTIFICATE_REQUIRED` only allows connections encrypted with SSL/TLS and with valid client certificates. If a client or user connects using [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication), then they must use either the Cloud SQL Auth Proxy or Cloud SQL Connectors to enforce client identity verification. 
For more information, see [ Settings for Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#ssl_mode). 


### Terraform

To enforce SSL/TLS encryption, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance): 
    
    
    resource "google_sql_database_instance" "postgres_instance" {
      name             = "postgres-instance"
      region           = "asia-northeast1"
      database_version = "POSTGRES_14"
      settings {
        tier = "db-custom-2-7680"
        ip_configuration {
          # The following SSL enforcement options only allow connections encrypted with SSL/TLS and with
          # valid client certificates. Please check the API reference for other SSL enforcement options:
          # https://cloud.google.com/sql/docs/postgres/admin-api/rest/v1beta4/instances#ipconfiguration
          ssl_mode = "TRUSTED_CLIENT_CERTIFICATE_REQUIRED"
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
       * `ALLOW_UNENCRYPTED_AND_ENCRYPTED`: allows non-SSL/non-TLS and SSL/TLS connections. For SSL connections, the client certificate isn't verified. This is the default value.
       * `ENCRYPTED_ONLY`: only allows connections encrypted with SSL/TLS.
       * `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`: only allows connections encrypted with SSL/TLS and with valid client certificates. If a client or user connects using [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication), then they must use either the Cloud SQL Auth Proxy or Cloud SQL Connectors to enforce client identity verification. 
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
       * `ALLOW_UNENCRYPTED_AND_ENCRYPTED`: allows non-SSL/non-TLS and SSL/TLS connections. For SSL connections, the client certificate isn't verified. This is the default value. 
       * `ENCRYPTED_ONLY`: only allows connections encrypted with SSL/TLS.
       * `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`: only allows connections encrypted with SSL/TLS and with valid client certificates. If a client or user connects using [IAM database authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication), then they must use either the Cloud SQL Auth Proxy or Cloud SQL Connectors to enforce client identity verification. 
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

Cloud SQL creates a server certificate automatically when you create your instance. As long as the server certificate is valid, you don't need to actively [manage your server certificate](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance). Cloud SQL lets you select between three different [certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/postgres/authorize-ssl#certificate_authority_ca_hierarchies). The CA hierarchy that you select becomes the server CA mode of the instance. If you're using per-instance CA as the server CA mode for your instance, then the server certificates have an expiration date of 10 years. If you're using shared CA or customer-managed CA as the server CA mode of your instance, then the server certificate has an expiration date of 1 year*. After the expiration date, the server certificate is no longer valid, and clients can no longer establish a secure connection to your instance using that certificate. If a client is configured to verify the CA or verify the hostname in the server certificate, then that client's connections to Cloud SQL instances with expired server certificates will fail. To prevent disruption to client connections, enable [automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#automatic-server-certificate-rotation-cas) or manually rotate the server certificate before the certificate expires. You're periodically notified that the server certificate is nearing expiration. The notifications are sent the following number of days before the expiration date: 90, 30, 10, 2, and 1.

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



The new server CA certificate appears in the **Upcoming** slot. If you want to rotate to the new server CA certificate immediately, proceed with [server CA certificate rotation](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#rotate) by updating your clients and completing the rotation.

**For instances that use server certificates issued by a shared CA** :

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Go to the **Manage server certificates** section.
  6. Click to expand **Manage certificates**.
  7. Click **Create server certificate**.



The new server certificate appears in the **Upcoming** slot. If you want to use the new server certificate immediately, proceed with [server certificate rotation](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance#rotate-server-cert-cas) by updating your clients and completing the rotation.

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
            




## Client certificates

### Create a new client certificate

You can create up to 10 client certificates for each instance. To create client certificates, you must have the [`Cloud SQL Admin` IAM role](https://docs.cloud.google.com/sql/docs/mysql/iam-roles).

Here are some important things to know about client certificates:

  * If you lose the private key for a certificate, you must create a new one; the private key cannot be recovered.
  * By default, the client certificate has an expiration date of 10 years.
  * You are not notified when client certificates are nearing expiration.
  * Your Cloud SQL instance must be in the running state to create a SSL certificate.



### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Click **Create client certificate**.
  6. In the **Create a client certificate** dialog, add a unique name.
  7. Click **Create**.
  8. In the first section of the **New SSL certificate created** dialog, click **Download client-key.pem** to download the private key to a file named `client-key.pem`. **Important:** Store this private key securely. If you lose it, you must create a new client certificate.
  9. In the second section, click **Download client-cert.pem** to download the client certificate to a file named `client-cert.pem`. 
  10. In the third section, click **Download server-ca.pem** to download the server certificate to a file named `server-ca.pem`. 
  11. Click **Close**. 



### gcloud

  1. Create a client certificate using the [ `ssl client-certs create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/create) command:
         
         gcloud sql ssl client-certs create CERT_NAME client-key.pem \
         --instance=INSTANCE_NAME

**Important:** Store this private key securely. If you lose it, you must create a new client certificate.
  2. Retrieve the public key for the certificate you just created and copy it into the `client-cert.pem` file with the [`ssl client-certs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/client-certs/describe) command:
         
         gcloud sql ssl client-certs describe CERT_NAME \
         --instance=INSTANCE_NAME \
         --format="value(cert)" > client-cert.pem

  3. Copy the server certificate into the `server-ca.pem` file using the [`instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) command:
         
         gcloud sql instances describe INSTANCE_NAME \
         --format="value(serverCaCert.cert)" > server-ca.pem




### Terraform

To create a client certificate, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_ssl_cert): 
    
    
    resource "google_sql_ssl_cert" "postgres_client_cert" {
      common_name = "postgres_common_name"
      instance    = google_sql_database_instance.postgres_instance.name
    }

### REST v1

  1. Create an SSL/TLS certificate, giving it a unique name for this instance:

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * client-cert-name: The client cert name

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/sslCerts

Request JSON body: 
    
    {
      "commonName" : "client-cert-name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/sslCerts"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/sslCerts" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#sslCertsInsert",
      "operation": {
        "kind": "sql#operation",
        "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
        "status": "PENDING",
        "user": "user@example.com",
        "operationType": "UPDATE",
        "name": "operation-id",
        "targetId": "instance-id",
        "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
        "targetProject": "doc-test-01",
        "insertTime": "2020-02-13T00:11:20.677Z"
      },
      "serverCaCert": {
        "kind": "sql#sslCert",
        "certSerialNumber": "server-cert-serial-number",
        "cert": "server-cert-value",
        "commonName": "server-cert-name,
        "sha1Fingerprint": "server-cert-sha1Fingerprint",
        "instance": "instance-id",
        "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/sslCerts/operation-id",
        "createTime": "2019-11-25T20:12:06.764Z",
        "expirationTime": "2029-11-22T20:13:06.764Z"
      },
      "clientCert": {
        "certInfo": {
          "kind": "sql#sslCert",
          "certSerialNumber": "client-cert-serial-number-2",
          "cert": "client-cert-value",
          "commonName": "client-cert-name",
          "sha1Fingerprint": "client-cert-sha1Fingerprint-2",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/sslCerts/operation-id",
          "createTime": "2020-02-13T00:10:20.595Z",
          "expirationTime": "2030-02-10T00:11:20.595Z"
        },
        "certPrivateKey": "private-key-value"
      }
    }
    
    

  2. Copy all of the certificate contents within the quotation marks (but not the quotation marks themselves) from the response into local files as follows: 
     1. Copy `serverCaCert.cert` into `server-ca.pem`.
     2. Copy `clientCert.cert` into `client-cert.pem`.
     3. Copy `certPrivateKey` into `client-key.pem`.
**Important:** Store this private key securely. If you lose it, you must create a new client certificate.



### REST v1beta4

  1. Create an SSL/TLS certificate, giving it a unique name for this instance:

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID
     * client-cert-name: The client cert name

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/sslCerts

Request JSON body: 
    
    {
      "commonName" : "client-cert-name"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/sslCerts"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/sslCerts" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#sslCertsInsert",
      "operation": {
        "kind": "sql#operation",
        "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
        "status": "PENDING",
        "user": "user@example.com",
        "operationType": "UPDATE",
        "name": "operation-id",
        "targetId": "instance-id",
        "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
        "targetProject": "doc-test-01",
        "insertTime": "2020-02-13T00:11:20.677Z"
      },
      "serverCaCert": {
        "kind": "sql#sslCert",
        "certSerialNumber": "server-cert-serial-number",
        "cert": "server-cert-value",
        "commonName": "server-cert-name,
        "sha1Fingerprint": "server-cert-sha1Fingerprint",
        "instance": "instance-id",
        "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/sslCerts/operation-id",
        "createTime": "2019-11-25T20:12:06.764Z",
        "expirationTime": "2029-11-22T20:13:06.764Z"
      },
      "clientCert": {
        "certInfo": {
          "kind": "sql#sslCert",
          "certSerialNumber": "client-cert-serial-number-2",
          "cert": "client-cert-value",
          "commonName": "client-cert-name",
          "sha1Fingerprint": "client-cert-sha1Fingerprint-2",
          "instance": "instance-id",
          "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/sslCerts/operation-id",
          "createTime": "2020-02-13T00:10:20.595Z",
          "expirationTime": "2030-02-10T00:11:20.595Z"
        },
        "certPrivateKey": "private-key-value"
      }
    }
    
    

  2. Copy all of the certificate contents within the quotation marks (but not the quotation marks themselves) from the response into local files as follows: 
     1. Copy `serverCaCert.cert` into `server-ca.pem`.
     2. Copy `clientCert.cert` into `client-cert.pem`.
     3. Copy `certPrivateKey` into `client-key.pem`.
**Important:** Store this private key securely. If you lose it, you must create a new client certificate.



At this point, you have:

  * A server certificate saved as `server-ca.pem`.
  * A client public key certificate saved as `client-cert.pem`.
  * A client private key saved as `client-key.pem`.

Depending on which tool you use to connect, these three items are specified in different ways. For example, when connecting using psql command-line client, these three files are the values for the `sslrootcert`, `sslcert`, and `sslkey` parameters in the psql connection string. For an example connection using psql client and SSL/TLS, see [Connecting with psql client](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect). 

## Server identity verification

Server identity verification depends on the server [certificate authority (CA) hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) configuration of your Cloud SQL instance.

For instances that use a per-instance CA, verifying the CA also verifies the server identity since each instance has a unique CA. For instances that use a shared CA, verifying the hostname along with verifying the CA is required for server identity verification since server CAs are shared across instances.

If you have per-instance CA, then you can perform DNS name-based server identity verification only for instances that are configured with Private Service Connect. If you have a shared CA, then you can perform DNS name-based server identity verification for all types of instances, namely [Private Service Connect](https://docs.cloud.google.com/sql/docs/postgres/about-private-service-connect), [private service access](https://docs.cloud.google.com/sql/docs/postgres/configure-private-services-access), and public IP instances.

If you're using a customer-managed CA, then you can verify the CA trust chain and perform DNS name-based server identity verification for any type of instance that uses customer-managed CA for its `serverCAmode`.

When you select the customer-managed CA option for your instance, you can insert custom DNS names in the SAN field of the server certificate. For more information, see [Edit a custom SAN field](https://docs.cloud.google.com/sql/docs/postgres/edit-instance#edit-custom-san-instance).

You can view which CA hierarchy is configured for a Cloud SQL instance by viewing instance details. For more information, see [View instance information](https://docs.cloud.google.com/sql/docs/postgres/instance-info).

### Enable server identity verification

If you select shared CA as the server CA mode of your Cloud SQL instance or if you [set up custom DNS names using custom SAN values](https://docs.cloud.google.com/sql/docs/postgres/custom-dns-name), then we recommend that you also enable server identity verification.

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

  3. When you connect to the Cloud SQL for PostgreSQL instance, configure the DNS name as the hostname. Then enable server identity verification in your client.

For example, when using the `psql` client, specify the flag `sslmode=verify-full`. Other PostgreSQL client drivers have similar configuration flags.




## What's next

  * [Manage](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance) SSL/TLS certificates on your Cloud SQL instance.
  * Learn more about [how encryption is handled in Google Cloud](https://cloud.google.com/security/encryption-in-transit).
  * [Connect](https://docs.cloud.google.com/sql/docs/postgres/connect-admin-ip#connect-ssl) to your Cloud SQL instance using SSL/TLS certificates.
  * Learn more about [how PostgreSQL uses SSL/TLS certificates](https://www.postgresql.org/docs/current/static/libpq-ssl.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
