---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/create-secret-cmek-encryption/
title: Add CMEK encryption to regional secrets \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:34.842688+00:00
---

# Add CMEK encryption to regional secrets  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/create-secret-cmek-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Add CMEK encryption to regional secrets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can create new secrets with customer-managed encryption keys (CMEK) and update existing secrets to use CMEK keys.

## Overview

[CMEK](https://docs.cloud.google.com/kms/docs/cmek#cmek) adds an extra layer of security and control over your sensitive data stored as regional secrets. You can use CMEK to meet the following goals:

  * Have complete control over the encryption keys used to protect your secrets.
  * Use your own key management system with potentially stricter security policies, auditing capabilities, and compliance features.
  * Comply with data sovereignty regulations by keeping the keys within your own infrastructure.
  * Define fine-grained access controls for your encryption keys, specifying who can use them and for what purposes.



### Limitations:

Using CMEK with regional secrets has the following limitations:

  * [Cloud Key Management Service Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)) isn't supported for regional secrets.
  * The location of the CMEK key must be the same as the location of the regional secret.



## Before you begin

  1. [Enable the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager), once per project.
  2. Assign the Secret Manager Admin role (`roles/secretmanager.admin`) on the project, folder, or organization.
  3. Authenticate to the Secret Manager API using one of the following ways:

     * If you use client libraries to access the Secret Manager API, set up [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).
     * If you use the Google Cloud CLI to access the Secret Manager API, use your [Google Cloud CLI credentials](https://docs.cloud.google.com/sdk/docs/authenticate) to authenticate.
     * To authenticate a REST call, use either Google Cloud CLI credentials or Application Default Credentials.
  4. To enable CMEK and to create the CMEK keys and key rings that you require for this step, see [Enable customer-managed encryption keys for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/cmek).




## Create a regional secret with CMEK encryption

To create a new secret with CMEK encryption, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab, and then click **Create regional secret**.

  3. On the **Create regional secret** page, enter a name for the secret in the **Name** field. A secret name can contain uppercase and lowercase letters, numerals, hyphens, and underscores. The maximum allowed length for a name is 255 characters.

  4. Enter a value for the secret (for example, `abcd1234`). The secret value can be in any format but must not be larger than 64 KiB. You can also upload a text file containing the secret value using the **Upload file** option. This action automatically creates the secret version.

  5. Choose the location where you want your regional secret to be stored from the **Region** list.

  6. Under **Encryption** , select **Customer-managed encryption key (CMEK)** , and then choose your CMEK key from the **Encryption key** list. Ensure that your CMEK key exists in the specified location and your Secret Manager project has the necessary permissions to use the key.

  7. Click **Create secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) where you want to create the secret
  * KMS_PROJECT_ID: the ID of your Google Cloud project that is running Cloud Key Management Service.
  * KMS_KEY_LOCATION: the location of your Cloud KMS key. This must be the same location as your secret.
  * YOUR_KEY_RING: the name of the key ring in Cloud KMS where you have stored your CMEK key.
  * YOUR_CMEK_KEY: the specific customer-managed encryption key (CMEK) that you have created within your chosen key ring in Cloud KMS.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION
        --regional-kms-key-name="projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION
        --regional-kms-key-name="projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION
        --regional-kms-key-name="projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) where you want to create the secret.
  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * KMS_PROJECT_ID: the ID of your Google Cloud project that is running Cloud Key Management Service.
  * KMS_KEY_LOCATION: the location of your Cloud KMS key. This must be the same location as your secret.
  * YOUR_KEY_RING: the name of the key ring in Cloud KMS where you have stored your CMEK key.
  * YOUR_CMEK_KEY: the specific customer-managed encryption key (CMEK) that you have created within your chosen key ring in Cloud KMS.



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {"customer_managed_encryption": {"kms_key_name": "projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"}}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-03-27T13:30:07.437859Z",
      "etag": "\"1614a467b60423\""
      "customerManagedEncryption": {
        "kmsKeyName": "projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
      }
    }
    
    

## Update an existing secret to use CMEK

To update an existing secret to use CMEK, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.

  3. To edit a secret, use one of the following methods:

     * Locate the secret in the list and click the more_vert**Actions** menu associated with that secret. In the **Actions** menu, click **Edit**.

     * Click the secret name to go to the secret details page. On the secret details page, click edit**Edit secret**.

  4. On the **Edit secret** page, go to the **Encryption** section.

  5. Under **Encryption** , select **Customer-managed encryption key (CMEK)** , and then select your CMEK key from the **Encryption key** list. Ensure that your CMEK key exists in the specified location and your Secret Manager project has the necessary permissions to use the key.

  6. Click **Update secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * KMS_PROJECT_ID: the ID of your Google Cloud project that is running Cloud Key Management Service.
  * KMS_KEY_LOCATION: the location of your Cloud KMS key. This must be the same location as your secret.
  * YOUR_KEY_RING: the name of the key ring in Cloud KMS where you have stored your CMEK key.
  * YOUR_CMEK_KEY: the specific customer-managed encryption key (CMEK) that you have created within your chosen key ring in Cloud KMS.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION
        --regional-kms-key-name="projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION
        --regional-kms-key-name="projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --location=LOCATION
        --regional-kms-key-name="projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret.
  * PROJECT_ID: the Google Cloud project ID.
  * SECRET_ID: the ID of the secret.
  * KMS_PROJECT_ID: the ID of your Google Cloud project that is running Cloud Key Management Service.
  * KMS_KEY_LOCATION: the location of your Cloud KMS key. This must be the same location as your secret.
  * YOUR_KEY_RING: the name of the key ring in Cloud KMS where you have stored your CMEK key.
  * YOUR_CMEK_KEY: the specific customer-managed encryption key (CMEK) that you have created within your chosen key ring in Cloud KMS.



HTTP method and URL: 
    
    
    PATCH https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=customer_managed_encryption

Request JSON body: 
    
    
    {"customer_managed_encryption": {"kms_key_name": "projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/YOUR_KEY_RING/cryptoKeys/YOUR_CMEK_KEY"}}"
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=customer_managed_encryption"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID?updateMask=customer_managed_encryption" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-03-27T13:30:07.437859Z",
      "etag": "\"16211daf5f29c5\""
      "customerManagedEncryption": {
        "kmsKeyName": "projects/KMS_PROJECT_ID/locations/KMS_KEY_LOCATION/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
      }
    }
    
    

## What's next

  * [Add a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs)
  * [Create and manage annotations](https://docs.cloud.google.com/secret-manager/regional-secrets/add-annotations-rs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
