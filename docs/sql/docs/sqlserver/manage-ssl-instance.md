---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance/
title: Manage SSL/TLS certificates \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:33.812168+00:00
---

# Manage SSL/TLS certificates  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage SSL/TLS certificates Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/manage-ssl-instance "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to manage your server certificate authority (CA) certificates. 

## Use encrypted connections

Learn more about [how SQL Server uses encrypted connections](https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine?view=sql-server-ver15#to-configure-the-client-to-request-encrypted-connections).

## Manage server CA certificates (per-instance CA)

This section describes how to manage server CA certificates that are created internally by Cloud SQL. This is the default server CA mode in Cloud SQL. In this certificate authority hierarchy, Cloud SQL creates a server CA for each instance.

### Rotate server CA certificates

If you've received a notice about your certificates expiring, or you want to initiate a rotation, then take the following steps to complete the rotation. Before you start the rotation, you must have a new server CA on the instance. If a new server CA has already been created, then you can skip the first step in the following procedure.

  1. Create a new server CA.
  2. Download the new server CA certificate information.
  3. Update your clients to use the new server CA certificate information.
  4. Complete the rotation, which moves the active certificate into the "previous" slot and updates the newly added certificate to be the active certificate.

After rotating the SSL certificate, your App Engine and Cloud SQL Auth Proxy connections will automatically receive a new certificate when they connect.

### Console

Download the new server CA certificate, encoded as a PEM file, to your local environment:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Click to expand **Manage certificates**.
  6. Select **Rotate CA certificate**. 

If there are no eligible certificates, then the rotate option is unavailable. You must create a new [server CA certificate](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#server-cert-list-view).

  7. Click **Download Certificates**.



Update all of your SQL Server clients to use the new information by copying the downloaded file to your client host machines, replacing the existing `server-ca.pem` file.

After you have updated your clients, complete the rotation:

  1. Return to the **Security** tab.
  2. Click to expand **Manage certificates**.
  3. Select **Rotate CA certificate**.
  4. Confirm that your clients are connecting properly.

If any clients are not connecting using the newly rotated certificate, then you can select **Rollback CA certificate** to rollback to the previous configuration.




### gcloud

  1. Create a server CA certificate: 
         
         gcloud sql ssl server-ca-certs create \
         --instance=INSTANCE

  2. Download the certificate information to a local PEM file: 
         
         gcloud sql ssl server-ca-certs list \
         --format="value(cert)" \
         --instance=INSTANCE_NAME > \
         FILE_PATH/FILE_NAME.pem

  3. Update all of your clients to use the new information by copying the downloaded file to your client host machines, replacing the existing server-ca.pem files.
  4. After you have updated your clients, complete the rotation: 
         
         gcloud sql ssl server-ca-certs rotate \
         --instance=INSTANCE_NAME
               

  5. Confirm that your clients are connecting properly.

If any clients are not connecting using the newly rotated certificate, then you can rollback to the previous configuration. 




### REST v1

  1. Download your server CA certificates: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/listServerCas

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/listServerCas"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/listServerCas" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "certs": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2020-02-10T17:18:54.935Z",
          "expirationTime": "2030-02-07T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
           certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2019-11-14T22:43:56.458Z",
          "expirationTime": "2029-11-11T22:44:56.458Z"
        }
      ],
      "activeVersion": "active-version",
      "kind": "sql#instancesListServerCas"
    }
    
    

  2. Complete the rotation: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




### REST v1beta4

  1. Download your server CA certificates: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/listServerCas

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/listServerCas"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/listServerCas" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "certs": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2020-02-10T17:18:54.935Z",
          "expirationTime": "2030-02-07T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
           certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2019-11-14T22:43:56.458Z",
          "expirationTime": "2029-11-11T22:44:56.458Z"
        }
      ],
      "activeVersion": "active-version",
      "kind": "sql#instancesListServerCas"
    }
    
    

  2. Complete the rotation: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




If you receive an error when you try to rotate a certificate that says `No upcoming/previous Server CA Certificate exists`, then verify that you're running the command on an instance that uses the per-instance CA hierarchy. You can view which CA hierarchy is configured for a Cloud SQL instance by using the `gcloud sql instances describe` command. For more information, see [View instance information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info).

### Roll back a certificate rotation operation

After you complete a certificate rotation, your clients must all use the new certificate to connect to your Cloud SQL instance. If the clients aren't updated properly to use the new certificate information, then they can't connect using SSL/TLS to your instance. If this happens, then you can roll back to the previous certificate configuration.

A rollback operation moves the active certificate into the "upcoming" slot (replacing any "upcoming" certificate). The "previous" certificate becomes the active certificate, returning your certificate configuration to the state it was in before you completed the rotation.

**Note:** Certificate rollback is available only until the old certificate expires.

To roll back to the previous certificate configuration:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Click to expand **Manage certificates**.
  6. Select **Rollback CA certificate**. 

If there are no eligible certificates, then the rollback option is unavailable. Otherwise, the rollback action completes after a few seconds.




### gcloud
    
    
    gcloud sql ssl server-ca-certs rollback \
    --instance=INSTANCE_NAME
       

### REST v1

  1. Download your server CA certificates: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/listServerCas

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/listServerCas"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/listServerCas" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "certs": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2020-02-10T17:18:54.935Z",
          "expirationTime": "2030-02-07T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
           certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2019-11-14T22:43:56.458Z",
          "expirationTime": "2029-11-11T22:44:56.458Z"
        }
      ],
      "activeVersion": "active-version",
      "kind": "sql#instancesListServerCas"
    }
    
    

  2. Copy the `sha1Fingerprint` field for the version you want to roll back to. 

Look for the version with a createTime value immediately earlier than the version with the sha1Fingerprint value shown as `activeVersion`.

  3. Roll back the rotation: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa

Request JSON body: 
    
    {
      "rotateServerCaContext": {"nextVersion": "sha1Fingerprint"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




### REST v1beta4

  1. Download your server CA certificates: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/listServerCas

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/listServerCas"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/listServerCas" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "certs": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2020-02-10T17:18:54.935Z",
          "expirationTime": "2030-02-07T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
           certSerialNumber": "cert-serial-number",
          "cert": "cert-value",
          "commonName": "ca-server-name",
          "sha1Fingerprint": "sha1Fingerprint",
          "instance": "instance-id",
          "createTime": "2019-11-14T22:43:56.458Z",
          "expirationTime": "2029-11-11T22:44:56.458Z"
        }
      ],
      "activeVersion": "active-version",
      "kind": "sql#instancesListServerCas"
    }
    
    

  2. Copy the `sha1Fingerprint` field for the version you want to roll back to. 

Look for the version with a createTime value immediately earlier than the version with the sha1Fingerprint value shown as `activeVersion`.

  3. Roll back the rotation: 

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa

Request JSON body: 
    
    {
      "rotateServerCaContext": {"nextVersion": "sha1Fingerprint"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




If you receive an error when you try to roll back a certificate CA rotation that says `No upcoming/previous Server CA Certificate exists`, then verify that you're running the command on an instance that uses the per-instance CA hierarchy. You can view which CA hierarchy is configured for a Cloud SQL instance by using the `gcloud sql instances describe` command. For more information, see [View instance information](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info).

### Initiate a rotation

You don't need to wait for the email from Cloud SQL to start a rotation. You can start one at any time. When you start a rotation, a new certificate is created and placed into the "upcoming" slot. If a certificate is already present in the "upcoming" slot at the time of your request, then that certificate is deleted. There can be only one upcoming certificate.

To initiate a rotation:

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Click to expand **Manage certificates**.
  6. Click **Create new CA certificate**.
  7. Select **Rotate CA certificate**. 

If there are no eligible certificates, then the rotate option is unavailable.

  8. Complete the rotation as described in Rotate server CA certificates.



### gcloud

  1. Initiate the rotation: 
         
         gcloud sql ssl server-ca-certs create \
         --instance=INSTANCE_NAME
              

  2. Complete the rotation as described in Rotate server CA certificates.



### REST v1

  1. Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/rotateServerCa" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  2. Complete the rotation as described in Rotate server CA certificates.



### REST v1beta4

  1. Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/rotateServerCa" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

  2. Complete the rotation as described in Rotate server CA certificates.



### Get information about a server CA certificate

You can get information about your server CA certificate, such as when it expires or what level of encryption it provides.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Select the **Security** tab. 

In **Manage server CA certificates** , you can see the expiration date of your server CA certificate in the table.

To see the certificate type, use the `gcloud sql ssl server-ca-certs list --instance=INSTANCE_NAME` command.




### gcloud
    
    
    gcloud sql ssl server-ca-certs list \
    --instance=INSTANCE_NAME

### REST v1

When you describe your instance, you can see details about the server CA certificate: 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=serverCaCert

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=serverCaCert"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id?fields=serverCaCert" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "serverCaCert":
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "cert-serial-number",
        "cert": "cert-value-",
        "commonName": "ca-server-name",
        "sha1Fingerprint": "sha1Fingerprint",
        "instance": "instance-id",
        "createTime": "2020-02-10T17:18:54.935Z",
        "expirationTime": "2030-02-07T17:19:54.935Z"
      }
    }
    

### REST v1beta4

When you describe your instance, you can see details about the server CA certificate: 

Before using any of the request data, make the following replacements: 

  * project-id: The project ID
  * instance-id: The instance ID



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=serverCaCert

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=serverCaCert"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id?fields=serverCaCert" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "serverCaCert":
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "cert-serial-number",
        "cert": "cert-value-",
        "commonName": "ca-server-name",
        "sha1Fingerprint": "sha1Fingerprint",
        "instance": "instance-id",
        "createTime": "2020-02-10T17:18:54.935Z",
        "expirationTime": "2030-02-07T17:19:54.935Z"
      }
    }
    

### View the content of CA certificates

You can use `openssl storeutl` to view the content of CA certificates.

When you run the [sql ssl server-ca-certs list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/server-ca-certs/list) command, you might get multiple CA certificates from previous rotation-related operations.

### gcloud

  1. Run the following command: 
         
         gcloud sql ssl server-ca-certs list \
           --instance=INSTANCE_NAME \
           --format='value(cert)' > temp_cert.pem

Replace INSTANCE_NAME with the name of the instance.

  2. Use `openssl` to examine the contents of the CA certificates.
    
    openssl storeutl -noout -text temp_cert.pem
       




### View the content of a server certificate

You can use `nmap` to view the content of server certificates. To download and install `nmap`, visit <https://nmap.org/>. 

### gcloud

To view the server certificate content, run the following command:

nmap -sV -p 1433 --script ssl-cert INSTANCE_IP_ADDRESS -Pn 

Replace INSTANCE_IP_ADDRESS with the IP address of the instance.

### External server SSL expiry notification

  * If the external server's server CA certificate is expiring, then rotate the SSL certificates, including the server CA certificate on the on-premises instance. This step depends on how the on-premises instance is managed. Steps can vary if, for example, you're using an RDS server CA certificate, Cloud SQL server CA certificate, or database-generic server CA certificate.
  * If the client certificate is expiring, then you need to generate a new certificate and key. This applies to both Google Cloud-managed SSL certificates and self-signed certificates.
  * Update the Cloud SQL source representation instance with the new SSL certificates.



## Manage server certificates (shared CA)

This section describes how to manage server certificates on instances that use shared CAs or customer-managed CAs.

You can opt in to using shared CAs as the server CA mode for your instance by specifying `GOOGLE_MANAGED_CAS_CA` for the `serverCaMode` setting (Cloud SQL Admin API) or the `--server-ca-mode` flag ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)) when you [create](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance) or [edit](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance) your instance.

To use customer-managed CA as the server CA mode for your instance, you must specify `CUSTOMER_MANAGED_CAS_CA` for the `serverCaMode` setting (Cloud SQL Admin API) or the `--server-ca-mode` flag ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)) when you [create](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance) or [edit](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance) your instance, and you must have a valid CA pool and CA. For more information, see [Use customer-managed CA](https://docs.cloud.google.com/sql/docs/sqlserver/customer-managed-ca).

### Enable or disable automatic server certificate rotation

We recommend that you enable automatic server certificate rotation. With this feature enabled, Cloud SQL automatically rotates your server certificate during your regularly scheduled [maintenance update](https://docs.cloud.google.com/sql/docs/sqlserver/maintenance) or when you [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/sqlserver/self-service-maintenance) up to 180 days before the certificate expires. Automatic certificate rotation helps you avoid connection interruptions caused by expired certificates and eliminates the need to rotate the certificates manually.

**Note:** Your server certificate won't be rotated automatically if maintenance updates are skipped or during the maintenance event, Cloud SQL detects that the certificate has more than 180 days left until its expiration date.

You can enable automatic server certificate rotation when you [create your instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance) or when you edit your existing instance.

The following procedure describes how to edit an existing instance to enable or disable automatic server certificate rotation.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In the **Customize your instance** section, expand **Show configuration options**.
  5. Click **Security** to expand the security configuration section.
  6. Do one of the following: 
     * To enable automatic server certificate rotation, select the **Rotate server certificates automatically** checkbox.
     * To disable automatic server certificate rotation, clear the **Rotate server certificates automatically** checkbox.
  7. Click **Save**.



### gcloud

To edit server certificate rotation mode for an instance, use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --project=PROJECT_ID \
      --server-certificate-rotation-mode=SERVER_CERTIFICATE_ROTATION_MODE

Make the following replacements:

  * INSTANCE_NAME: the name of the Cloud SQL instance that has a server certificate that you're modifying
  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that contains the instance
  * SERVER_CERTIFICATE_ROTATION_MODE: specify either `NO_AUTOMATIC_ROTATION` or `AUTOMATIC_ROTATION_DURING_MAINTENANCE`.



### REST v1

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project. This project contains a Cloud SQL instance that has a server certificate that you're managing.
  * INSTANCE_NAME: the name of the instance.
  * SERVER_CERTIFICATE_ROTATION_MODE: specify either `NO_AUTOMATIC_ROTATION` or `AUTOMATIC_ROTATION_DURING_MAINTENANCE`.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "kind": "sql#instance",
      "name": "INSTANCE_NAME",
      "project": "PROJECT_ID",
      "settings": {
        "ipConfiguration": {
          "serverCertificateRotationMode": "SERVER_CERTIFICATE_ROTATION_MODE"
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
      "insertTime": "2026-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch). 

### REST v1beta4

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID or [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your Google Cloud project. This project contains a Cloud SQL instance that has a server certificate that you're managing.
  * INSTANCE_NAME: the name of the instance.
  * SERVER_CERTIFICATE_ROTATION_MODE: specify either `NO_AUTOMATIC_ROTATION` or `AUTOMATIC_ROTATION_DURING_MAINTENANCE`.




HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_NAME

Request JSON body: 
    
    
    {
      "kind": "sql#instance",
      "name": "INSTANCE_NAME",
      "project": "PROJECT_ID",
      "settings": {
        "ipConfiguration": {
          "serverCertificateRotationMode": "SERVER_CERTIFICATE_ROTATION_MODE"
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
      "insertTime": "2026-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_NAME",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch) is constructed for this task, see the [APIs Explorer on the instances:patch page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/patch). 

### Manually rotate server certificates

If you've received a notice about your server certificates expiring or you want to initiate a rotation, but you don't have automatic server certificate rotation enabled, then take the following steps to complete the rotation. Before you start the rotation, there must be a new server certificate created for the upcoming rotation. If there is already a new server certificate created for the upcoming rotation, then you can skip the first step in the following procedure.

To rotate the server certificate on your instance, perform the following steps:

  1. If you need a new server certificate, then [create one](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance#create-server-certificate-cas). 

  2. If your clients already trust the latest regional CA bundle, then this step is optional. However, if you need to update your clients with server CA information, then do the following:

     1. Download the latest server CA information.
     2. Update your clients to use the latest server CA information.
  3. Complete the rotation by moving the active certificate to the previous slot, and updating the new certificate to be the active certificate.




### Console

Download the server CA certificate information, encoded as a PEM file, to your local environment:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Click to expand **Manage certificates**.
  6. Confirm that the **Rotate server certificate** option appears as an available option; however, don't select it yet. 

If there are no eligible certificates, then the rotate option is unavailable. You must create a new [server certificate](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance#server-cert-list-view).

  7. Click **Download certificates**.



Update all of your SQL Server clients to use the new information by copying the downloaded file to your client host machines, replacing the existing `server-ca.pem` file.

After you have updated your clients, complete the rotation:

  1. Return to the **Security** tab.
  2. Click to expand **Manage certificates**.
  3. Select **Rotate certificate**.
  4. In the **Confirm certificate rotation** dialog, click **Rotate**.
  5. Confirm that your clients are connecting properly.

If any clients are not connecting using the newly rotated certificate, then you can select **Rollback certificate** to rollback to the previous configuration.




### gcloud

  1. To create a server certificate, use the following command: 
         
         gcloud sql ssl server-certs create \
         --instance=INSTANCE

Replace INSTANCE with the name of the instance. 
  2. Make sure that you're using the latest CA bundle. If you aren't using the latest CA bundle, then run the following command to download the latest server CA information for the instance to a local PEM file: 
         
         gcloud sql ssl server-certs list \
         --format="value(ca_cert.cert)" \
         --instance=INSTANCE_NAME > \
         FILE_PATH/server-ca.pem

Or download the CA bundles from the root and regional CA certificate bundle table on this page.

Then update all of your clients to use new server CA information by copying the downloaded file to your client host machines, replacing the existing `server-ca.pem` files.

  3. After you update all your clients (if client updates are required), complete the rotation: 
         
         gcloud sql ssl server-certs rotate \
         --instance=INSTANCE_NAME
               

  4. Confirm that your clients are connecting properly.

If any clients aren't connecting using the newly rotated server certificate, then roll back to the previous configuration. 




### REST v1

  1. Create a server certificate.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/addServerCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/addServerCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/addServerCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  2. If you need to download server CA certificate information, then you can use the following command.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "caCerts": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_ONE",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_ONE",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-10T17:18:54.935Z",
          "expirationTime": "2034-07-10T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_TWO",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_TWO",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-14T22:43:56.458Z",
          "expirationTime": "2034-11-11T22:44:56.458Z"
        }
      ],
      "serverCerts": [
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_ONE",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_ONE",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-16T18:11:39Z",
        "expirationTime": "2025-09-16T18:11:38Z"
      },
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_TWO",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_TWO",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-10T20:56:06Z",
        "expirationTime": "2025-09-10T20:56:05Z"
      }
    ],
      "activeVersion": "sha1Fingerprint_SERVER_CERT_TWO",
      "kind": "sql#instancesListServerCertificates"
    }
    
    

  3. Complete the rotation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: The project ID
     * INSTANCE_ID: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-09-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/operation-id",
      "targetProject": "PROJECT_ID"
    }
    




### REST v1beta4

  1. Create a server certificate.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/addServerCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/addServerCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/addServerCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

  2. If you need to download server CA certificate information, then you can use the following command.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "caCerts": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_ONE",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_ONE",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-10T17:18:54.935Z",
          "expirationTime": "2034-07-10T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_TWO",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_TWO",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-14T22:43:56.458Z",
          "expirationTime": "2034-11-11T22:44:56.458Z"
        }
      ],
      "serverCerts": [
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_ONE",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_ONE",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-16T18:11:39Z",
        "expirationTime": "2025-09-16T18:11:38Z"
      },
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_TWO",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_TWO",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-10T20:56:06Z",
        "expirationTime": "2025-09-10T20:56:05Z"
      }
    ],
      "activeVersion": "sha1Fingerprint_SERVER_CERT_TWO",
      "kind": "sql#instancesListServerCertificates"
    }
    
    

  3. Complete the rotation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2024-09-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    




### Roll back a certificate rotation

After you complete a server certificate rotation, all your clients must use the new certificate to connect to your Cloud SQL instance. If the clients aren't updated properly to use the new certificate information, then they can't connect using SSL/TLS to your instance. If this happens, then you can roll back to the previous certificate configuration.

A rollback operation moves the active certificate into the "upcoming" slot, which replaces any "upcoming" certificate. The "previous" certificate becomes the active certificate and returns your certificate configuration to its previous state before you completed the rotation.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Select the **Security** tab.
  5. Click to expand **Manage certificates**.
  6. Select **Rollback server certificate**. 

If there are no eligible certificates, then the rollback option is unavailable.

  7. In the **Confirm certificate rollback** dialog, select **Rollback**. 

The rollback might take a few seconds to complete.




### gcloud
    
    
    gcloud sql ssl server-certs rollback \
    --instance=INSTANCE_NAME
       

### REST v1

  1. List your server certificates.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "caCerts": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_ONE",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_ONE",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-10T17:18:54.935Z",
          "expirationTime": "2034-07-10T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_TWO",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_TWO",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-14T22:43:56.458Z",
          "expirationTime": "2034-11-11T22:44:56.458Z"
        }
      ],
      "serverCerts": [
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_ONE",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_ONE",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-16T18:11:39Z",
        "expirationTime": "2025-09-16T18:11:38Z"
      },
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_TWO",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_TWO",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-10T20:56:06Z",
        "expirationTime": "2025-09-10T20:56:05Z"
      }
    ],
      "activeVersion": "sha1Fingerprint_SERVER_CERT_TWO",
      "kind": "sql#instancesListServerCertificates"
    }
    
    

  2. Copy the `sha1Fingerprint` field for the version you want to roll back to.

Look for the version with a `createTime` value immediately earlier than the version with the `sha1Fingerprint` value shown as `activeVersion`.

  3. Roll back the rotation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate

Request JSON body: 
    
    {
      "rotateServerCertificateContext": {"nextVersion": "sha1Fingerprint"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate"

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
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate" | Select-Object -Expand Content

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

  1. List your server certificates.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/listServerCertificates" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "caCerts": [
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_ONE",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_ONE",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-10T17:18:54.935Z",
          "expirationTime": "2034-07-10T17:19:54.935Z"
        },
        {
          "kind": "sql#sslCert",
          "certSerialNumber": "CERT_SERIAL_NUMBER_CA_CERT_TWO",
          "cert": "CERT_VALUE",
          "commonName": "CA_SERVER_NAME",
          "sha1Fingerprint": "sha1Fingerprint_CA_CERT_TWO",
          "instance": "INSTANCE_NAME",
          "createTime": "2024-07-14T22:43:56.458Z",
          "expirationTime": "2034-11-11T22:44:56.458Z"
        }
      ],
      "serverCerts": [
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_ONE",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_ONE",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-16T18:11:39Z",
        "expirationTime": "2025-09-16T18:11:38Z"
      },
      {
        "kind": "sql#sslCert",
        "certSerialNumber": "CERT_SERIAL_NUMBER_SERVER_CERT_TWO",
        "cert": "CERT_VALUE"
        "commonName": "SUBJECT_VALUE",
        "sha1Fingerprint": "sha1Fingerprint_SERVER_CERT_TWO",
        "instance": "INSTANCE_NAME",
        "createTime": "2024-09-10T20:56:06Z",
        "expirationTime": "2025-09-10T20:56:05Z"
      }
    ],
      "activeVersion": "sha1Fingerprint_SERVER_CERT_TWO",
      "kind": "sql#instancesListServerCertificates"
    }
    
    

  2. Copy the `sha1Fingerprint` field for the version you want to roll back to.

Look for the version with a `createTime` value immediately earlier than the version with the `sha1Fingerprint` value shown as `activeVersion`.

  3. Roll back the rotation.

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the project ID
     * INSTANCE_ID: the instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate

Request JSON body: 
    
    {
      "rotateServerCertificateContext": {"nextVersion": "sha1Fingerprint"}
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate"

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
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID/rotateServerCertificate" | Select-Object -Expand Content

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
    




### View the content of CA certificates

You can use the `openssl storeutl` utility to view the content of CA certificates.

When you run the [sql ssl server-certs list](https://docs.cloud.google.com/sdk/gcloud/reference/sql/ssl/server-certs/list) command, you always get multiple CA certificates due to the trust chain. You might also get multiple CA certificates from previous rotation-related operations.

### gcloud

  1. Run the following command: 
         
         gcloud sql ssl server-certs list \
           --instance=INSTANCE_NAME \
           --format='value(ca_cert.cert)' > temp_cert.pem

Replace INSTANCE_NAME with the name of the instance.

  2. Use `openssl` to examine the contents of the CA certificates.
    
    openssl storeutl -noout -text temp_cert.pem
       




### Download root and regional CA certificate bundles for a shared CA

If you're using a Google-managed shared CA configuration, then you can download the root and regional CA certificate bundles from the following table.

These certificate bundles don't apply to instances that use the per-instance or customer-managed CA options.

| Region name | Location | Certificate bundle  
---|---|---|---  
**Global** |  |  |   
| CA for all regions | All locations | [`global.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/global.pem)  
**Asia** |  |  |   
| `asia-east1` | Taiwan | [`asia-east1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-east1.pem)  
| `asia-east2` | Hong Kong | [`asia-east2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-east2.pem)  
| `asia-northeast1` | Tokyo | [`asia-northeast1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-northeast1.pem)  
| `asia-northeast2` | Osaka | [`asia-northeast2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-northeast2.pem)  
| `asia-northeast3` | Seoul | [`asia-northeast3.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-northeast3.pem)  
| `asia-south1` | Mumbai | [`asia-south1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-south1.pem)  
| `asia-south2` | Delhi | [`asia-south2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-south2.pem)  
| `asia-southeast1` | Singapore | [`asia-southeast1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-southeast1.pem)  
| `asia-southeast2` | Jakarta | [`asia-southeast2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-southeast2.pem)  
| `asia-southeast3` | Bangkok | [`asia-southeast3.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/asia-southeast3.pem)  
**Africa** |  |  |   
| `africa-south1` | Johannesburg | [`africa-south1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/africa-south1.pem)  
**Australia** |  |  |   
| `australia-southeast1` | Sydney | [`australia-southeast1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/australia-southeast1.pem)  
| `australia-southeast2` | Melbourne | [`australia-southeast2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/australia-southeast2.pem)  
**Europe** |  |  |   
| `europe-central2` | Warsaw | [`europe-central2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-central2.pem)  
| `europe-north1` | Finland | [`europe-north1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-north1.pem)  
| `europe-north2` | Stockholm | [`europe-north2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-north2.pem)  
| `europe-southwest1` | Madrid | [`europe-southwest1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-southwest1.pem)  
| `europe-west1` | Belgium | [`europe-west1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west1.pem)  
| `europe-west2` | London | [`europe-west2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west2.pem)  
| `europe-west3` | Frankfurt | [`europe-west3.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west3.pem)  
| `europe-west4` | Netherlands | [`europe-west4.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west4.pem)  
| `europe-west6` | Zürich | [`europe-west6.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west6.pem)  
| `europe-west8` | Milan | [`europe-west8.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west8.pem)  
| `europe-west9` | Paris | [`europe-west9.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west9.pem)  
| `europe-west10` | Berlin | [`europe-west10.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west10.pem)  
| `europe-west12` | Turin | [`europe-west12.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/europe-west12.pem)  
**Middle East** |  |  |   
| `me-central1` | Doha | [`me-central1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/me-central1.pem)  
| `me-central2` | Dammam | [`me-central2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/me-central2.pem)  
| `me-west1` | Tel Aviv | [`me-west1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/me-west1.pem)  
**North America** |  |  |   
| `northamerica-northeast1` | Montréal | [`northamerica-northeast1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/northamerica-northeast1.pem)  
| `northamerica-northeast2` | Toronto | [`northamerica-northeast2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/northamerica-northeast2.pem)  
| `northamerica-south1` | Mexico | [`northamerica-south1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/northamerica-south1.pem)  
| `us-central1` | Iowa | [`us-central1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-central1.pem)  
| `us-east1` | South Carolina | [`us-east1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-east1.pem)  
| `us-east4` | Northern Virginia | [`us-east4.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-east4.pem)  
| `us-east5` | Columbus | [`us-east5.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-east5.pem)  
| `us-south1` | Dallas | [`us-south1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-south1.pem)  
| `us-west1` | Oregon | [`us-west1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-west1.pem)  
| `us-west2` | Los Angeles | [`us-west2.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-west2.pem)  
| `us-west3` | Salt Lake City | [`us-west3.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-west3.pem)  
| `us-west4` | Las Vegas | [`us-west4.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/us-west4.pem)  
**South America** |  |  |   
| `southamerica-east1` | São Paulo | [`southamerica-east1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/southamerica-east1.pem)  
| `southamerica-west1` | Santiago | [`southamerica-west1.pem`](https://storage.googleapis.com/cloudsql-ca-bundles/southamerica-west1.pem)  
  
## Reset the SSL/TLS configuration

You can completely reset your SSL/TLS configuration.

**Caution:** Performing this action removes the ability to connect to your instance using SSL/TLS until you create new client certificates to replace any that were previously in use.

### Console 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Select **Connections** from the SQL navigation menu.
  4. Go to the **Reset SSL configuration** section.
  5. Click **Reset SSL Configuration**.



### gcloud

  1. Refresh the certificate:
         
         gcloud sql instances reset-ssl-config INSTANCE_NAME




### REST v1beta4

  1. Refresh the certificate:

Before using any of the request data, make the following replacements: 

     * project-id: The project ID
     * instance-id: The instance ID

HTTP method and URL: 
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/resetSslConfig

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/resetSslConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/resetSslConfig" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2020-01-20T21:30:35.667Z",
      "operationType": "UPDATE",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    




## What's next

  * Learn more about [SSL/TLS in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl).
  * [Configure SSL/TLS](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance) on your Cloud SQL instance. 
  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
