---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/train-models-to-detect-money-laundering/
title: Train and test models designed to detect money laundering \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:06.529310+00:00
---

# Train and test models designed to detect money laundering  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/train-models-to-detect-money-laundering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train and test models designed to detect money laundering

**Important:** Completing this quickstart will result in charges to your Google Cloud account. For information on pricing, see the [Pricing page](https://cloud.google.com/financial-services/anti-money-laundering/pricing). Note that the sample dataset used in this quickstart contains 100,000 parties.

This quickstart guides you through an end-to-end implementation of a model to detect money laundering using the Anti Money Laundering AI (AML AI) API. In this guide, you learn how to train and test models to detect money laundering through the following steps:

  1. Prepare your Cloud environment and create an AML AI instance.
  2. Provide synthetic transaction data in the form of BigQuery tables.
  3. Train and backtest a model with input data.
  4. Register parties and make model predictions.



After creating prediction results, this guide analyzes a single case of an example party that is laundering money by [structuring funds](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview#money-laundering-structuring-funds).

## Before you begin

**Important:** After you create your project, the API is not automatically visible. You must contact your Google representative before you can enable the API.

This section describes how to set up a Google Cloud account, enable the required Google Cloud services, and grant the required permissions to run the quickstart.

If you are going to use an existing project that you don't own, you may need your administrator to grant you certain permissions to access the existing project. For more information, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable financialservices.googleapis.com bigquery.googleapis.com cloudkms.googleapis.com bigquerydatatransfer.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/financialservices.admin, roles/cloudkms.admin, roles/bigquery.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the required APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable financialservices.googleapis.com bigquery.googleapis.com cloudkms.googleapis.com bigquerydatatransfer.googleapis.com

  16. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/financialservices.admin, roles/cloudkms.admin, roles/bigquery.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

These roles fulfill the following required permissions: 

#### Required permissions

The following permissions are required to complete this quickstart:

Permission | Description  
---|---  
`resourcemanager.projects.get`| Get a Google Cloud project  
`resourcemanager.projects.list`| List Google Cloud projects  
`cloudkms.keyRings.create`| Create a Cloud KMS key ring  
`cloudkms.cryptoKeys.create`| Create a Cloud KMS key  
`financialservices.v1instances.create`| Create an AML AI instance  
`financialservices.operations.get`| Get an AML AI operation  
`cloudkms.cryptoKeys.getIamPolicy`| Get the IAM policy on a Cloud KMS key  
`cloudkms.cryptoKeys.setIamPolicy`| Set the IAM policy on a Cloud KMS key  
`bigquery.datasets.create`| Create a BigQuery dataset  
`bigquery.datasets.get`| Get a BigQuery dataset  
`bigquery.transfers.get`| Get a BigQuery Data Transfer Service transfer  
`bigquery.transfers.update`| Create or delete a BigQuery Data Transfer Service transfer  
`bigquery.datasets.setIamPolicy`| Set the IAM policy on a BigQuery dataset  
`bigquery.datasets.update`| Update a BigQuery dataset  
`financialservices.v1datasets.create`| Create an AML AI dataset  
`financialservices.v1engineconfigs.create`| Create an AML AI engine config  
`financialservices.v1models.copyFrom`| Copy from an AML AI model  
`financialservices.v1models.copyTo`| Copy to an AML AI instance  
`financialservices.v1models.create`| Create an AML AI model  
`financialservices.v1backtests.create`| Create an AML AI backtest result  
`financialservices.v1backtests.exportMetadata`| Export metadata from an AML AI backtest result  
`financialservices.v1instances.importRegisteredParties`| Import registered parties into an AML AI instance  
`financialservices.v1predictions.create`| Create an AML AI prediction result  
`bigquery.jobs.create`| Create a BigQuery job  
`bigquery.tables.getData`| Get data from a BigQuery table  
`financialservices.v1predictions.delete`| Delete an AML AI prediction result  
`financialservices.v1backtests.delete`| Delete an AML AI backtest result  
`financialservices.v1models.delete`| Delete an AML AI model  
`financialservices.v1engineconfigs.delete`| Delete an AML AI engine config  
`financialservices.v1datasets.delete`| Delete an AML AI dataset  
`financialservices.v1instances.delete`| Delete an AML AI instance  
`bigquery.datasets.delete`| Delete a BigQuery dataset  
  
  18. The API requests in this guide use the same Google Cloud project and location and hard-coded resource IDs to make the guide easier to complete. The resource IDs follow the pattern `my-`_resource-type_ (for example, `my-key-ring` and `my-model`). 

Make sure the following replacements are defined for this guide:

     * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
     * `PROJECT_NUMBER`: the project number associated with `PROJECT_ID`. You can find the project number on the [IAM Settings](https://console.cloud.google.com/iam-admin/settings) page. 
     * `LOCATION`: the location of the API resources; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

       * `us-central1`
       * `us-east1`
       * `europe-west2`
       * `europe-west6`

**Important:** After you enable the Financial Services API, you must contact your Google representative to allowlist all AML AI functionality before proceeding. Make sure to inform the representative of the [location](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations) in which you want to create your API resources.

## Create an instance

This section describes how to create an instance. The AML AI instance sits at the root of all other AML AI resources. Each instance requires a single associated customer-managed encryption key (CMEK) which is used to encrypt any data created by AML AI.

### Create a key ring

To create a key ring, use the [`projects.locations.keyRings.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create) method.

### REST

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings?key_ring_id=my-key-ring"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings?key_ring_id=my-key-ring" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring",
      "createTime": CREATE_TIME
    }
    

### gcloud

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keyrings create my-key-ring \
      --location LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keyrings create my-key-ring `
      --location LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keyrings create my-key-ring ^
      --location LOCATION

You should receive an empty response: 
    
    
    $

### Create a key

To create a key, use the [`projects.locations.keyRings.cryptoKeys`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method.

### REST

Request JSON body: 
    
    
    {
      "purpose": "ENCRYPT_DECRYPT"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "purpose": "ENCRYPT_DECRYPT"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys?crypto_key_id=my-key"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "purpose": "ENCRYPT_DECRYPT"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys?crypto_key_id=my-key" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key",
      "primary": {
        "name": "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1",
        "state": "ENABLED",
        "createTime": CREATE_TIME,
        "protectionLevel": "SOFTWARE",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION",
        "generateTime": GENERATE_TIME
      },
      "purpose": "ENCRYPT_DECRYPT",
      "createTime": CREATE_TIME,
      "versionTemplate": {
        "protectionLevel": "SOFTWARE",
        "algorithm": "GOOGLE_SYMMETRIC_ENCRYPTION"
      },
      "destroyScheduledDuration": "86400s"
    }
    

### gcloud

Before using any of the command data below, make the following replacements: 

  * `LOCATION`: the location of the key ring; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keys create my-key \
      --keyring my-key-ring \
      --location LOCATION \
      --purpose "encryption"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keys create my-key `
      --keyring my-key-ring `
      --location LOCATION `
      --purpose "encryption"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud kms keys create my-key ^
      --keyring my-key-ring ^
      --location LOCATION ^
      --purpose "encryption"

You should receive an empty response: 
    
    
    $

### Create the instance using the API

To create an instance, use the [`projects.locations.instances.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/create) method.

Request JSON body: 
    
    
    {
      "kmsKey": "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "kmsKey": "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=my-instance"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "kmsKey": "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances?instance_id=my-instance" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

If successful, the response body contains a [long-running operation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations) that contains an ID which can be used to retrieve the ongoing status of the asynchronous operation. Copy the returned `OPERATION_ID` to use in the next section.

**Note:** By default, instances are not provisioned for production use, but will work for the data referenced from this page. If you intend to use the instance for production, see [Create an AML AI instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/set-up-instance#support) for provisioning information.

### Check for the result

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get) method to check if the instance has been created. If the response contains `"done": false`, repeat the command until the response contains `"done": true`.

Operations in this guide can take a few minutes to several hours to complete. You must wait until an operation completes before moving forward in this guide because the API uses the output of some methods as input to other methods.

Before using any of the request data, make the following replacements: 

  * `OPERATION_ID`: the identifier for the operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "endTime": END_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.Instance",
        "name": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key",
        "state": "ACTIVE"
      }
    }
    

## Grant access to the CMEK key

The API automatically creates a service account in your project. The service account needs access to the CMEK key so it can use the key to encrypt and decrypt the underlying data. Grant access to the key.
    
    
    gcloud kms keys add-iam-policy-binding "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring/cryptoKeys/my-key" \
      --keyring "projects/PROJECT_ID/locations/LOCATION/keyRings/my-key-ring" \
      --location "LOCATION" \
      --member "serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com" \
      --role="roles/cloudkms.cryptoKeyEncrypterDecrypter" \
      --project="PROJECT_ID"

## Create BigQuery datasets

This section describes how to create input and output BigQuery datasets, and then copy sample banking data into the input dataset.

### Create an output dataset

[Create a dataset](https://docs.cloud.google.com/bigquery/docs/datasets) to be used to send the AML pipeline outputs to.

### Bash
    
    
    bq mk \
      --location=LOCATION \
      --project_id=PROJECT_ID \
      my_bq_output_dataset
    

### PowerShell
    
    
    bq mk `
      --location=LOCATION `
      --project_id=PROJECT_ID `
      my_bq_output_dataset
    

### Create an input dataset

Create a dataset to copy the sample banking tables into.

### Bash
    
    
    bq mk \
      --location=LOCATION \
      --project_id=PROJECT_ID \
      my_bq_input_dataset
    

### PowerShell
    
    
    bq mk `
      --location=LOCATION `
      --project_id=PROJECT_ID `
      my_bq_input_dataset
    

### Copy the sample dataset

**Note:** The sample data is protected by the same allowlist that protects API enablement documented in the Before you begin section.

Sample banking data is provided as a BigQuery dataset in [Google's shared dataset project](https://docs.cloud.google.com/bigquery/public-data). You must have access to the AML AI API for this dataset to be accessible. Key features of this dataset include the following:

  * 100,000 parties
  * A time period from January 1, 2020 to January 1, 2023
  * 300 negative and 20 positive risk cases per month
  * Risk cases with the following attributes: 
    * Half of the positive risk cases are for structuring activity which occurred in the two months preceding the `AML_PROCESS_START` event
    * The other half covers parties with the highest amount of received money in the two months preceding the `AML_PROCESS_START` event
    * Negative cases are randomly generated
    * A 0.1% chance for the risk case to be generated in the opposite state (for example, a random party that is positive, or a party that has structuring activity or the highest income and is reported negative)
  * The AML schema is defined in the [AML input data model](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model).


  1. Copy the sample banking data into the input dataset you created.

### Bash
         
         bq mk --transfer_config \
           --project_id=PROJECT_ID \
           --data_source=cross_region_copy \
           --target_dataset="my_bq_input_dataset" \
           --display_name="Copy the AML sample dataset." \
           --schedule=None \
           --params='{
             "source_project_id":"bigquery-public-data",
             "source_dataset_id":"aml_ai_input_dataset",
             "overwrite_destination_table":"true"
           }'
         

### PowerShell
         
         bq mk --transfer_config `
         --project_id=PROJECT_ID `
         --data_source=cross_region_copy `
         --target_dataset="my_bq_input_dataset" `
         --display_name="Copy the AML sample dataset." `
         --schedule=None `
         --params='{\"source_project_id\":\"bigquery-public-data\",\"source_dataset_id\":\"aml_ai_input_dataset\",\"overwrite_destination_table\":\"true\"}'
         

  2. Monitor the data transfer job.

### Bash
         
         bq ls --transfer_config \
         --transfer_location=LOCATION \
         --project_id=PROJECT_ID \
         --filter="dataSourceIds:cross_region_copy"
         

### PowerShell
         
         bq ls --transfer_config `
         --transfer_location=LOCATION `
         --project_id=PROJECT_ID `
         --filter="dataSourceIds:cross_region_copy"
         

After the transfer completes, a data transfer job with the display name `Copy the AML sample dataset` is created.

You can also check the [status of the transfer](https://docs.cloud.google.com/bigquery/docs/working-with-transfers#get_transfer_details) using the Google Cloud console.

You should see something like the following output.
         
         name                           displayName         dataSourceId       state
         -------------------------------------------  -----------------------  -----------------  ---------
         projects/294024168771/locations/us-central1  Copy AML sample dataset  cross_region_copy  SUCCEEDED
         




### Grant access to the BigQuery datasets

The API automatically creates a service account in your project. The service account needs access to the BigQuery input and output datasets.

  1. Grant read access to the input dataset and its tables.

### Bash
         
         bq query --project_id=PROJECT_ID --use_legacy_sql=false \
           'GRANT `roles/bigquery.dataViewer` ON SCHEMA `PROJECT_ID.my_bq_input_dataset` TO "serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com"'
         

### PowerShell
         
         bq query --project_id=PROJECT_ID --use_legacy_sql=false "GRANT ``roles/bigquery.dataViewer`` ON SCHEMA ``PROJECT_ID.my_bq_input_dataset`` TO 'serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com'"
         

  2. Grant write access to the output dataset.

### Bash
         
         bq query --project_id=PROJECT_ID --use_legacy_sql=false \
           'GRANT `roles/bigquery.dataEditor` ON SCHEMA `PROJECT_ID.my_bq_output_dataset` TO "serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com"'
         

### PowerShell
         
         bq query --project_id=PROJECT_ID --use_legacy_sql=false "GRANT ``roles/bigquery.dataEditor`` ON SCHEMA ``PROJECT_ID.my_bq_output_dataset`` TO 'serviceAccount:service-PROJECT_NUMBER@gcp-sa-financialservices.iam.gserviceaccount.com'"
         




## Create an AML AI dataset

Create an AML AI dataset to specify the input BigQuery dataset tables and the time range to use.

To create a dataset, use the [`projects.locations.instances.datasets.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/create) method.

Request JSON body: 
    
    
    {
      "tableSpecs": {
        "party": "bq://PROJECT_ID.my_bq_input_dataset.party",
        "account_party_link": "bq://PROJECT_ID.my_bq_input_dataset.account_party_link",
        "transaction": "bq://PROJECT_ID.my_bq_input_dataset.transaction",
        "risk_case_event": "bq://PROJECT_ID.my_bq_input_dataset.risk_case_event",
        "party_supplementary_data": "bq://PROJECT_ID.my_bq_input_dataset.party_supplementary_data"
      },
      "dateRange": {
        "startTime": "2020-01-01T00:00:0.00Z",
        "endTime": "2023-01-01T00:00:0.00Z"
      },
      "timeZone": {
        "id": "UTC"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "tableSpecs": {
        "party": "bq://PROJECT_ID.my_bq_input_dataset.party",
        "account_party_link": "bq://PROJECT_ID.my_bq_input_dataset.account_party_link",
        "transaction": "bq://PROJECT_ID.my_bq_input_dataset.transaction",
        "risk_case_event": "bq://PROJECT_ID.my_bq_input_dataset.risk_case_event",
        "party_supplementary_data": "bq://PROJECT_ID.my_bq_input_dataset.party_supplementary_data"
      },
      "dateRange": {
        "startTime": "2020-01-01T00:00:0.00Z",
        "endTime": "2023-01-01T00:00:0.00Z"
      },
      "timeZone": {
        "id": "UTC"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets?dataset_id=my-dataset"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "tableSpecs": {
        "party": "bq://PROJECT_ID.my_bq_input_dataset.party",
        "account_party_link": "bq://PROJECT_ID.my_bq_input_dataset.account_party_link",
        "transaction": "bq://PROJECT_ID.my_bq_input_dataset.transaction",
        "risk_case_event": "bq://PROJECT_ID.my_bq_input_dataset.risk_case_event",
        "party_supplementary_data": "bq://PROJECT_ID.my_bq_input_dataset.party_supplementary_data"
      },
      "dateRange": {
        "startTime": "2020-01-01T00:00:0.00Z",
        "endTime": "2023-01-01T00:00:0.00Z"
      },
      "timeZone": {
        "id": "UTC"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets?dataset_id=my-dataset" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

You can check for the result of the operation using the new operation ID. (You can do this for the remaining API requests used in this guide.)

## Create an engine config

Create an AML AI engine config to automatically tune hyperparameters based on a given engine version and the data provided. Engine versions are released periodically and correspond to different model logic (for example, targeting a retail line of business versus a commercial one).

To create an engine config, use the [`projects.locations.instances.engineConfigs.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create) method.

This stage involves hyperparameter tuning which can take some time to process. Provided your data does not change substantially, this step can be used to create and test many models.

Request JSON body: 
    
    
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineVersions/aml-commercial.default.v004.008.202411-001",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2021-07-01T00:00:00Z"
      },
      "performanceTarget": {
        "partyInvestigationsPerPeriodHint": "30"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineVersions/aml-commercial.default.v004.008.202411-001",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2021-07-01T00:00:00Z"
      },
      "performanceTarget": {
        "partyInvestigationsPerPeriodHint": "30"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs?engine_config_id=my-engine-config"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "engineVersion": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineVersions/aml-commercial.default.v004.008.202411-001",
      "tuning": {
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2021-07-01T00:00:00Z"
      },
      "performanceTarget": {
        "partyInvestigationsPerPeriodHint": "30"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs?engine_config_id=my-engine-config" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Create a model

In this step, you train an AML AI model by using 12 months of data leading up to 2021-07-01.

To create a model, use the [`projects.locations.instances.models.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/create) method.

Request JSON body: 
    
    
    {
        "engineConfig": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config",
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2021-07-01T00:00:00Z"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
        "engineConfig": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config",
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2021-07-01T00:00:00Z"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models?model_id=my-model"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
        "engineConfig": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config",
        "primaryDataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2021-07-01T00:00:00Z"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models?model_id=my-model" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Create a backtest result

Backtest prediction uses the trained model on existing historical data. Create a backtest result on the 12 months of data leading up to January 2023, which were not used in training. These months are used to determine how many cases we might need to work had we used the model trained to July 2021 in production during January to December 2022.

To create a backtest result, use the [`projects.locations.instances.backtestResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/create) method.

Request JSON body: 
    
    
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2023-01-01T00:00:00Z",
        "backtestPeriods": 12,
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "150"
        }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2023-01-01T00:00:00Z",
        "backtestPeriods": 12,
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "150"
        }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults?backtest_result_id=my-backtest-results"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2023-01-01T00:00:00Z",
        "backtestPeriods": 12,
        "performanceTarget": {
          "partyInvestigationsPerPeriodHint": "150"
        }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults?backtest_result_id=my-backtest-results" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Export backtest results metadata

Once a backtest has been run, you need to export its results to BigQuery to view them. To export metadata from the backtest result, use the [`projects.locations.instances.backtestResults.exportMetadata`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/exportMetadata) method.

Request JSON body: 
    
    
    {
      "structuredMetadataDestination": {
        "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_backtest_results_metadata",
        "writeDisposition": "WRITE_TRUNCATE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "structuredMetadataDestination": {
        "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_backtest_results_metadata",
        "writeDisposition": "WRITE_TRUNCATE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results:exportMetadata"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "structuredMetadataDestination": {
        "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_backtest_results_metadata",
        "writeDisposition": "WRITE_TRUNCATE"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results:exportMetadata" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results",
        "verb": "exportMetadata",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Once the operation has completed, do the following:

  1. Open BigQuery in the Google Cloud console.

[Go to the Google Cloud console](https://console.cloud.google.com/bigquery)

  2. In the **Explorer** pane, find and expand your project.

  3. Expand **my_bq_output_dataset** and click **my_backtest_results_metadata**.

  4. On the menu bar, click **Preview**.

  5. In the **name** column, find the row with **ObservedRecallValues**.

![Observed recall values in BigQuery.](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/observed-recall.png)

  6. Assume that your capacity for investigations is 120 per month. Find the recall value object with `"partyInvestigationsPerPeriod": "120"``. For the following sample values, if you limit investigations to parties with risk scores greater than 0.53, then you can expect to investigate 120 new parties each month. Over the backtesting period, the year 2022, you would identify 86% of cases that the previous system identified (and possibly others, which were not identified by your current processes).
         
         {
           "recallValues": [
             ...
             {
               "partyInvestigationsPerPeriod": "105",
               "recallValue": 0.8142077,
               "scoreThreshold": 0.6071321
             },
             {
               "partyInvestigationsPerPeriod": "120",
               "recallValue": 0.863388,
               "scoreThreshold": 0.5339603
             },
             {
               "partyInvestigationsPerPeriod": "135",
               "recallValue": 0.89071035,
               "scoreThreshold": 0.4739899
             },
             ...
           ]
         }
         




See more about the other fields in the [backtest results](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#backtest-results).

By changing the `partyInvestigationsPerPeriodHint` field, you can modify the number of investigations a backtest produces. To obtain scores to investigate, register parties and produce predictions against them.

## Import registered parties

Before creating prediction results, you need to import registered parties (that is, customers in the dataset).

To import registered parties, use the [`projects.locations.instances.importRegisteredParties`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties) method.

Request JSON body: 
    
    
    {
      "partyTables": [
         "bq://PROJECT_ID.my_bq_input_dataset.party_registration"
      ],
      "mode": "REPLACE",
      "lineOfBusiness": "COMMERCIAL"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "partyTables": [
         "bq://PROJECT_ID.my_bq_input_dataset.party_registration"
      ],
      "mode": "REPLACE",
      "lineOfBusiness": "COMMERCIAL"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance:importRegisteredParties"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "partyTables": [
         "bq://PROJECT_ID.my_bq_input_dataset.party_registration"
      ],
      "mode": "REPLACE",
      "lineOfBusiness": "COMMERCIAL"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance:importRegisteredParties" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance",
        "verb": "importRegisteredParties",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

Keep [checking for the result](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/train-models-to-detect-money-laundering#check-for-result) of that operation until it completes. When it completes, you should see that 10,000 parties were registered in the JSON output.

## Create a prediction result

Create a prediction result on the last 12 months in the dataset; these months were not used during training. Creating prediction results creates scores for each party in each month across all the prediction periods.

To create a prediction result, use the [`projects.locations.instances.predictionResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/create) method.

Request JSON body: 
    
    
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2023-01-01T00:00:00Z",
        "predictionPeriods": "12",
        "outputs": {
          "predictionDestination": {
            "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_prediction_results",
            "writeDisposition": "WRITE_TRUNCATE"
          },
          "explainabilityDestination": {
            "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_prediction_results_explainability",
            "writeDisposition": "WRITE_TRUNCATE"
          }
        }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2023-01-01T00:00:00Z",
        "predictionPeriods": "12",
        "outputs": {
          "predictionDestination": {
            "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_prediction_results",
            "writeDisposition": "WRITE_TRUNCATE"
          },
          "explainabilityDestination": {
            "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_prediction_results_explainability",
            "writeDisposition": "WRITE_TRUNCATE"
          }
        }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/predictionResults?prediction_result_id=my-prediction-results"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
        "model": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "dataset": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "endTime": "2023-01-01T00:00:00Z",
        "predictionPeriods": "12",
        "outputs": {
          "predictionDestination": {
            "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_prediction_results",
            "writeDisposition": "WRITE_TRUNCATE"
          },
          "explainabilityDestination": {
            "tableUri": "bq://PROJECT_ID.my_bq_output_dataset.my_prediction_results_explainability",
            "writeDisposition": "WRITE_TRUNCATE"
          }
        }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/predictionResults?prediction_result_id=my-prediction-results" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/predictionResults/my-prediction-results",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Analyze a single structuring case in the Google Cloud console

**Note:** Due to differences in engine versions and the evolution of synthetic data over time, these results may not exactly match your outputs.

  1. Open BigQuery in the Google Cloud console.

[Go to the Google Cloud console](https://console.cloud.google.com/bigquery)

  2. In the details pane, click the **Untitled Query** tab to see the editor.

  3. Copy the following SQL statement into the editor and click **Run**.
         
         SELECT *
         FROM `PROJECT_ID.my_bq_input_dataset.transaction`
         WHERE account_id = '1E60OAUNKP84WDKB' AND DATE_TRUNC(book_time, MONTH) = "2022-08-01"
         ORDER by book_time
         

This statement checks account ID `1E60OAUNKP84WDKB` in August 2022. This account is linked to party ID `EGS4NJD38JZ8NTL8`. You can find the party ID for a given account ID by using the [AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink) table.

The transaction data shows frequent round transactions targeted at a single account shortly after a large cash deposit, which looks suspicious. These transactions could be indicative of smurfing (that is, breaking up a large transaction of money into smaller transaction amounts) or structuring.

![Suspicious transaction data for a single party.](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/transaction-data-for-single-party.png)

  4. Copy the following SQL statement into the editor and click **Run**.
         
         SELECT *
         FROM `PROJECT_ID.my_bq_input_dataset.risk_case_event`
         WHERE party_id = 'EGS4NJD38JZ8NTL8'
         

This statement shows that there was a risk case leading to the exit of this party. The risk case started two months after the suspicious activity.

![Risk case events for a single party.](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/risk-case-events-for-single-party.png)

  5. Copy the following SQL statement into the editor and click **Run**.
         
         SELECT *
         FROM `PROJECT_ID.my_bq_output_dataset.my_prediction_results`
         WHERE party_id = 'EGS4NJD38JZ8NTL8'
         ORDER BY risk_period_end_time
         

By checking the prediction results, you can see that the party's risk score jumps from nearly zero (note the exponent value) to high values in the months following the suspicious activity. Your results may vary from the results shown.

![Risk scores increasing for a single party.](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/prediction-data-for-single-party.png)

**The risk score is not a probability. A risk score should always be evaluated relative to other risk scores.** For example, a seemly small value can be considered positive in cases where the other risk scores are lower.

**Note:** Due to differences in engine versions and the evolution of synthetic data over time, the results obtained may differ from these screenshots. Model results shouldn't be interpreted as a probability of money laundering; model results should be interpreted relative to the same customer over time and to other customers. The numbers obtained for explainability and risk score may differ.
  6. Copy the following SQL statement into the editor and click **Run**.
         
         SELECT *
         FROM `PROJECT_ID.my_bq_output_dataset.my_prediction_results_explainability`
         WHERE party_id = 'EGS4NJD38JZ8NTL8'
         AND risk_period_end_time = '2022-10-01'
         

By checking the explainability results, you can see that the correct feature families score the highest values.

![Explainability results for predictions.](https://docs.cloud.google.com/static/financial-services/anti-money-laundering/images/explainability-data-for-single-party.png)




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

### Delete the prediction result

To delete a prediction result, use the [`projects.locations.instances.predictionResults.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/delete) method.

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/predictionResults/my-prediction-results"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/predictionResults/my-prediction-results" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/predictionResults/my-prediction-results",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Delete the backtest result

To delete a backtest result, use the [`projects.locations.instances.backtestResults.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/delete) method.

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/backtestResults/my-backtest-results",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Delete the model

To delete a model, use the [`projects.locations.instances.models.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/delete) method.

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/models/my-model",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Delete the engine config

To delete an engine config, use the [`projects.locations.instances.engineConfigs.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/delete) method.

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/engineConfigs/my-engine-config",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Delete the dataset

To delete a dataset, use the [`projects.locations.instances.datasets.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/delete) method.

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance/datasets/my-dataset",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Delete the instance

To delete an instance, use the [`projects.locations.instances.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/delete) method. 

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/my-instance" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": CREATE_TIME,
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/my-instance",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

### Delete the BigQuery datasets
    
    
    bq rm -r -f -d PROJECT_ID:my_bq_input_dataset
    
    
    
    bq rm -r -f -d PROJECT_ID:my_bq_output_dataset
    

### Delete the transfer job configuration

  1. List the transfer jobs in the project.

### Bash
         
         bq ls --transfer_config \
           --transfer_location=LOCATION \
           --project_id=PROJECT_ID  \
           --filter="dataSourceIds:cross_region_copy"
         

### PowerShell
         
         bq ls --transfer_config `
           --transfer_location=LOCATION `
           --project_id=PROJECT_ID `
           --filter="dataSourceIds:cross_region_copy"
         

  2. Output similar to the following should be returned.
         
         name                                                                                       displayName                    dataSourceId       state
         ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
         projects/PROJECT_NUMBER/locations/LOCATION/transferConfigs/TRANSFER_CONFIG_ID    Copy the AML sample dataset.   cross_region_copy   SUCCEEDED
         

Copy the entire name, starting with `projects/` and ending in the `TRANSFER_CONFIG_ID`.

  3. Delete the transfer config.

### Bash
         
         bq rm --transfer_config TRANSFER_CONFIG_NAME
         

### PowerShell
         
         bq rm --transfer_config TRANSFER_CONFIG_NAME
         




## What's next

  * Read about key concepts in the [overview](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)
  * View the [reference documentation](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
