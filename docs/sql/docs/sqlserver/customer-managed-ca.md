---
url: https://docs.cloud.google.com/sql/docs/sqlserver/customer-managed-ca/
title: Use a customer-managed certificate authority (CA) \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:44.082221+00:00
---

# Use a customer-managed certificate authority (CA)  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/customer-managed-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use a customer-managed certificate authority (CA) Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/customer-managed-ca "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to use the customer-managed certificate authority (CA) option as the server CA mode for your Cloud SQL instance.

## Overview

With the customer-managed CA option, you set up your own CA pool and CA in [Certificate Authority Service (CA Service)](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview). When you select the customer-managed CA option, you set up the CA hierarchy and manage the rotation of CA certificates for your Cloud SQL instances.

Before you can configure a Cloud SQL instance to use the customer-managed CA option, you must create a CA pool in the same region as your instance and at least one CA in that pool using CA Service. The CA can be a [root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca) or a [subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca). You also have the option to create a subordinate CA in CA Service and then chain the subordinate CA to an external root CA. When you configure your instance, you specify the CA pool. Your request is delegated to a project-specific service account, which has the permission to use the CA pool. The service account requests a CA from the pool and Cloud SQL uses that CA to sign the server certificate for the instance.

For the server CA mode for your instance in Cloud SQL, you can choose from the following three options:

  * internal per-instance CA
  * Google-managed shared CA
  * customer-managed CA



You might choose the customer-managed CA option if you need to manage your own CA for compliance reasons. For more information about using the other options, see [Authorize with SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl).

### Workflow

To use the customer-managed CA option, the workflow is as follows:

  1. Create a service account for your Cloud SQL project.
  2. Create a CA pool in CA Service.
  3. Create a CA in CA Service.
  4. Configure the Cloud SQL instance to use the CA. When you configure your instance, you delegate the permission to the service account to sign the server certificate with the CA pool that you created.



## Before you begin

Before you use the customer-managed CA option, make sure you meet the following requirements.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Certificate Authority Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com)

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. Verify that you have the permissions required to complete this guide. 

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Certificate Authority Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com)

  13. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  14. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  15. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Required roles

To get the permissions that you need to create a Cloud SQL-specific service account, ask your administrator to grant you the [Service Account Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`) IAM role on for each individual project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To get the permissions that you need to create a CA pool and CA, ask your administrator to grant you the CA Service Operation Manager(`roles/privateca.caManager`) IAM role on CA Service. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a project-specific service account

In the project where you plan to create your Cloud SQL instances, create a dedicated service account that will handle the request to create and sign the server certificates for your Cloud SQL instances.

### gcloud

Run the following command to create a service account for your Cloud SQL project:
    
    
    gcloud beta services identity create \
      --service=sqladmin.googleapis.com \
      --project=PROJECT_ID

Replace `PROJECT_ID` with the ID of the project where you plan to create your Cloud SQL instances.

The command creates a service account named `service-PROJECT_ID@gcp-sa-cloud-sql.iam.gserviceaccount.com` in the project. Make a note of the **CA Service Certificate Requester** service account name.

## Create a CA pool

Create a CA pool in CA Service.

You can create a CA pool in the same project where you plan to create your Cloud SQL instances, or you can create the CA pool in a different project. However, if you create the CA pool in a different project, then VPC Service Controls might block you from creating any Cloud SQL instances depending on organization policy. To fix the issue, make sure that the project that hosts the CA pool and CA and the project that hosts Cloud SQL belong to the same service perimeter. For more information, see [Service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) and [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).

To create a CA pool, follow the instructions in [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool). You can accept the default values for the CA pool, with the following required configuration settings:

  * Create the CA pool in the _same region_ where you plan to create your Cloud SQL instance. For a list of regions that are supported by Cloud SQL, see [Regions](https://docs.cloud.google.com/sql/docs/sqlserver/locations#location-r). 
  * Allow configuration based certificate requests.
  * Allow DNS names in subject alternative names (SAN). When you configure the identity constraints of the CA pool, don't set any restrictions on the format for the DNS names that might conflict with what Cloud SQL might add to the SAN.
  * If you configure the identity constraints for the CA pool, then make sure that you allow IP addresses as a format in the SAN.



## Provide the service account with access to the CA pool

To make sure the service account has the permissions to request and sign certificates for your Cloud SQL instances, grant the following role to the service account for the CA pool that you created:

  * `roles/privateca.certificateRequester`



### gcloud

Run the [ `gcloud privateca pools`](https://docs.cloud.google.com/sdk/gcloud/reference/privateca/pools/add-iam-policy-binding) command to grant the service account access to the CA pool:
    
    
    gcloud privateca pools add-iam-policy-binding CA_POOL_ID \
      --project=PROJECT_ID \
      --location=REGION \
      --member serviceAccount:SERVICE_ACCOUNT_NAME \
      --role=roles/privateca.certificateRequester

Make the following replacements:

  * `CA_POOL_ID` with the ID of the CA pool that you created.
  * `PROJECT_ID` with the ID of the project where you plan to create your Cloud SQL instances.
  * `REGION` with the region where you created the CA pool.
  * `SERVICE_ACCOUNT_NAME` with the name of the **CA Service Certificate Requester** service account that you created for the project previously.



## Create a CA in the CA pool

Create at least one CA in the CA pool that you created.

You can create a root CA or a subordinate CA.

To create a root CA, follow the instructions in [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca). You can accept the default values for the CA, but make sure that you create the CA in the **Enabled** state.

When you configure the **CA key size and algorithm** , you can select any key size and algorithm. Cloud SQL generates its server certificates using **EC P-256 (SHA 256)** elliptic curve keys, but your CA cryptographic keys don't have to match. 

If you create a subordinate CA, then you need to create and configure your root CA first.

  * To create a subordinate CA in CA Service, follow the instructions in [Create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-subordinate-ca).

  * To create a subordinate CA from an external root CA, follow the instructions in [Create a subordinate CA from an external root CA](https://docs.cloud.google.com/certificate-authority-service/docs/create-sub-ca-from-external-ca).




## Configure a Cloud SQL instance to use a customer-managed CA

You can configure a Cloud SQL instance to use the customer-managed CA option when you create the instance. You can also update the server CA mode of an existing an instance from using the per-instance CA or shared CA option to use a customer-managed CA instead.

### Create an instance

To create a Cloud SQL instance that uses the customer-managed CA option, do the following.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. In the **Instance ID** , enter a name for the instance.
  3. Select a database engine, database version, Cloud SQL edition, region, and availability type, or accept the defaults as described in [Create an instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance).
  4. In **Customize your instance** section, expand **Show configuration options**.
  5. Click **Security**.
  6. In the **Server certificate authority mode** section, select **Customer managed CAS certificate authority**.
  7. From the **CA pool** menu, select a CA pool for your instance. The CA pool must be in the same region that you select for your instance. If you don't have a CA pool yet, then click **New pool** to create a new pool.
  8. Optional: To [enable automatic rotation of your server certificates](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas), select the **Rotate server certificates automatically** checkbox.
  9. Click **Create instance**.



### gcloud
    
    
    gcloud sql instances create "INSTANCE_NAME" \
      --database-version=DATABASE_VERSION \
      --project=PROJECT_ID \
      --region=REGION \
      --server-ca-mode=CUSTOMER_MANAGED_CAS_CA \
      --server-ca-pool=projects/PROJECT_ID_CAS/locations/REGION/caPools/CA_POOL_ID

Make the following replacements:

  * `INSTANCE_NAME` with the name of the Cloud SQL instance that you want to create.
  * `DATABASE_VERSION` with the [`enum` of the version](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/SqlDatabaseVersion) of the Cloud SQL instance that you want to create. 
  * `PROJECT_ID` with the ID of the project where you plan to create your Cloud SQL instances.
  * `PROJECT_ID_CAS` with the ID of the project where you created your CA_POOL_ID. This project might be the same or different from where you want to create your Cloud SQL instance. 
  * `REGION` with the region where you created the CA pool. You must create your instance in the same region as the CA pool.
  * `CA_POOL_ID` with the ID of the CA pool that you created.



### REST

To create a Cloud SQL instance that uses the customer-managed CA option, use the [`instances.insert`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/insert) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID` the ID of the project where you plan to create your Cloud SQL instances. 
  * `PROJECT_ID_CAS` the ID of the project where you created your CA_POOL_ID. This project might be the same or different from where you want to create your Cloud SQL instance. 
  * `INSTANCE_ID` the name of the Cloud SQL instance that you want to create.
  * `REGION` the region where you created the CA pool. You must create your instance in the same region as the CA pool.
  * `CA_POOL_ID` with the ID of the CA pool that you created.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name":"INSTANCE_ID",
      "region":"REGION",
      "databaseVersion": "DATABASE_VERSION",
      "settings":{
         "ipConfiguration":
          {
             "serverCaPool": "projects/PROJECT_ID_CAS/locations/REGION/caPools/CA_POOL_ID",
             "serverCaMode": "CUSTOMER_MANAGED_CAS_CA"
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID_CSQL/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

### Update an instance to use a customer-managed CA

Before you update an instance to use a customer-managed CA, do the following:

  * Review the list of Google Cloud services that don't support connections to Cloud SQL instances that are configured to use a customer-managed CA. If your deployment is required to use the service, then you might need to delay the update.
  * If you're using the Cloud SQL Auth Proxy or any of the Cloud SQL Language Connectors to connect to the instance, then make sure that they're running the minimum required versions. For the Cloud SQL Auth Proxy, make sure you're using version 2.14.3 or later. For the minimum required versions of the Cloud SQL Language Connectors, see [Cloud SQL Language Connectors requirements](https://docs.cloud.google.com/sql/docs/sqlserver/language-connectors#requirements).
  * Make sure that you've already created a CA pool and you've provided the service account with access to the CA pool.
  * Make sure there's at least one CA in the CA pool.
  * To avoid any interruptions after the update, download the certificates from your customer-managed CA and set up your database clients to trust your CA.

**Caution:** Your primary instance and replicas require a restart when you switch to the customer-managed CA option. As a result, database services might be temporarily unavailable for up to a minute for each instance during the update. For example, if you have two instances, then your total downtime might be up to two minutes. 

Use the following procedure to update a Cloud SQL instance to use the customer-managed CA option.

**Note:** You can also use the same commands in the following procedure to update the CA pool for a Cloud SQL instance that's already been configured to use the customer-managed CA option.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In **Customize your instance** section, expand **Show configuration options**.
  5. Click **Security**.
  6. In the **Server certificate authority mode** section, select **Customer managed CAS certificate authority**.
  7. From the **CA pool** menu, select a CA pool for your instance. The CA pool must be in the same region that you select for your instance. If you don't have a CA pool yet, then click **New pool** to create a new pool.
  8. Optional: To [enable automatic rotation of your server certificates](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas), select the **Rotate server certificates automatically** checkbox.
  9. Click **Save**.



### gcloud

To update your instance, run the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --server-ca-mode=CUSTOMER_MANAGED_CAS_CA \
    --server-ca-pool=projects/PROJECT_ID_CAS/locations/REGION/caPools/CA_POOL_ID

For the `--server-ca-mode` flag, make sure that you specify `CUSTOMER_MANAGED_CAS_CA`.

Replace the following:

  * `INSTANCE_NAME`: the name of the Cloud SQL instance you want to patch.
  * `PROJECT_ID_CAS` with the ID of the project where your CA_POOL_ID is. This project might be the same or different from where your Cloud SQL instance is. 
  * `REGION` with the region where you created the CA pool. Your instance must be in the same region as the CA pool.
  * `CA_POOL_ID`: the ID of the CA pool that you want to assign to the instance. You can also use this command to change the CA pool for an instance that's already configured to use`CUSTOMER_MANAGED_CAS_CA`



### REST

To update a Cloud SQL instance to use the customer-managed CA option, use the [`instances.patch`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/patch) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID` the ID of the project where your Cloud SQL instance is. 
  * `INSTANCE_ID` the name of the Cloud SQL instance that you want to patch.
  * `PROJECT_ID_CAS` the ID of the project where you created your CA_POOL_ID. This project might be the same or different from where your Cloud SQL instance is. 
  * `REGION` the region where you created the CA pool. You must create your instance in the same region as the CA pool.
  * `CA_POOL_ID` the ID of the CA pool that you want to assign to the instance. You can also use this command to change the CA pool for an instance that's already configured to use`CUSTOMER_MANAGED_CAS_CA`.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":{
         "ipConfiguration":
          {
             "serverCaPool": "projects/PROJECT_ID_CAS/locations/REGION/caPools/CA_POOL_ID",
             "serverCaMode": "CUSTOMER_MANAGED_CAS_CA"
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Switch an instance from customer-managed CA to shared CA

You can update an instance that uses customer-managed CA to use a [shared CA](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#shared-regional-ca) (`GOOGLE_MANAGED_CAS_CA`). However, you can't update an instance that's configured to use a customer-managed CA to use the [per-instance CA](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#per-instance-ca) (`GOOGLE_MANAGED_INTERNAL_CA`).

Before you update an instance to use a shared CA, [download the global and regional CA bundles](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#download-root-regional-ca-bundles), copy them to your database clients, and let them trust these CAs. Setting up the certificates before switching server CA mode configuration can help avoid potential interruption for your database clients.

To switch the server CA mode of your instance to use the shared CA, use the following procedure.

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Edit**.
  4. In **Customize your instance** section, expand **Show configuration options**.
  5. Click **Security**.
  6. In the **Server certificate authority mode section** , select **Google managed CAS certificate authority**.
  7. Optional: To [enable automatic rotation of your server certificates ](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas), select the **Rotate server certificates automatically** checkbox.
  8. Click **Save**.



### gcloud

To update your instance, run the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
    --server-ca-mode=GOOGLE_MANAGED_CAS_CA \
    --server-ca-pool=""

In the command, do the following:

  * Replace `INSTANCE_NAME` following with the name of the Cloud SQL instance you want to patch.
  * For the `--server-ca-mode` flag, specify `GOOGLE_MANAGED_CAS_CA`.
  * For the `--server-ca-pool` flag, you must specify an empty string, or `""`.



### REST

To update a Cloud SQL instance that uses the customer-managed CA to use the shared CA option, use the [`instances.patch`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/patch) method and specify the following properties:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID` the ID of the project where your Cloud SQL instance is. 
  * `INSTANCE_ID` the name of the Cloud SQL instance that you want to patch.



HTTP method and URL: 
    
    
    PATCH https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

Request JSON body: 
    
    
    {
      "settings":{
         "ipConfiguration":
          {
             "serverCaPool": "",
             "serverCaMode": "GOOGLE_MANAGED_CAS_CA"
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
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2025-01-16T02:32:12.281Z",
      "operationType": "UPDATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

## Troubleshoot

Issue | Troubleshooting  
---|---  
You receive the following error message: `PERMISSION_DENIED: Permission `privateca.certificates.create` denied on CA_POOL_ID`.  |  Make sure that you granted the `roles/privateca.certificateRequester` role to the service account that you created for your Cloud SQL project. For more information, see Provide the service account with access to the CA pool.   
You receive the following error message: `PERMISSION_DENIED: Request is prohibited by organization's policy vpcServiceControlsUniqueIdentifier VPC_SERVICE_CONTROLS_UNIQUE_IDENTIFIER.` |  Make sure that you configure VPC Service Controls so that the project that hosts the CA Service CA pool and CA and the project that hosts Cloud SQL belong to the same service perimeter. For more information, see [Service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters) and [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).   
You receive one of the following `INVALID ARGUMENT` error messages:

  * `Public key algorithm is not permitted by the CaPool's issuance policy.`
  * `This CaPool's issuance policy does not permit passthrough subjects and/or subject alternative names, and thus can only be used with the REFLECTED_SPIFFE subject mode.`
  * `Config issuance mode is not permitted by the CaPool's issuance policy. `

|  Check the configuration settings of your CA pool and your CA. Make sure that you meet all the requirements listed in Create a CA pool and Create a CA in the CA pool.  
You receive the following error message: `RESOURCE_EXHAUSTED` |  This represents quota issues with CA Service. Verify the quota for CA Service in your project. Check whether you might be using requests in your CA pool outside of Cloud SQL. For more information, see [Quotas and limits](https://docs.cloud.google.com/certificate-authority-service/quotas).   
You receive the following error message: `NOT FOUND: parent resource CA_POOL_ID not found.` | Check the project ID, location, and name of the CA pool that you specified when you created your Cloud SQL instance. Make sure that you didn't make any typos.   
You receive the following error message: `FAILED_PRECONDITION: There are no enabled CAs in the CaPool. Please ensure that there is at least one enabled Certificate Authority to issue a certificate.` | Make sure that you have created at least one CA in the CA pool that you specified when you created your Cloud SQL instance, and that the CA is in the enabled state.   
You receive the following error message: `FAILED_PRECONDITION: Per-Product Per-Project Service Account (P4 SA) SERVICE_ACCOUNT_NAME not found for project PROJECT_ID.` | Make sure that you have created the service account for your Cloud SQL project. For more information, see Create a project-specific service account.   
You receive the following error message: `INVALID ARGUMENT: Invalid format for server CA pool.` | Make sure that you specified the CA pool in the correct format: `projects/PROJECT_ID/locations/REGION/caPools/CA_POOL_ID`  
You receive the following error message: `INVALID ARGUMENT: The instance's server CA pool must be in the same region as the instance.` | Make sure that you the CA pool is in the same region as the Cloud SQL instance that you want to create.  
  
## What's next

  * Learn more about [CA hierarchies in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies)
  * [Set up a custom DNS name](https://docs.cloud.google.com/sql/docs/sqlserver/custom-dns-name) for your instance



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
