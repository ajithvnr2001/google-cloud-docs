---
url: https://docs.cloud.google.com/secret-manager/docs/cmek/
title: Enable customer-managed encryption keys for Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:31.728666+00:00
---

# Enable customer-managed encryption keys for Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Enable customer-managed encryption keys for Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

By default, Secret Manager encrypts customer content at rest. Secret Manager handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Secret Manager. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Secret Manager resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Secret Manager provides tools for storing, managing, and accessing sensitive data in your applications.

**Caution:** If you temporarily disable or permanently destroy the CMEK, the data encrypted with that key cannot be decrypted and therefore is unaccessible.

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Secret Manager resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Secret Manager. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

Secret Manager is only compatible with Cloud KMS Autokey when creating resources using Terraform or the REST API.

To learn how to use manually-created CMEKs to protect your Secret Manager resources, see CMEK with automatic replication and CMEK with user managed replication on this page. 

To learn how to use CMEKs created by Cloud KMS Autokey to protect your Secret Manager resources, see [Using Autokey with Secret Manager resources](https://docs.cloud.google.com/kms/docs/create-resource-with-autokey#secret-manager-autokey).

## How CMEK works in Secret Manager

Before writing a secret version to persistent storage in a particular location, Secret Manager encrypts the data with a unique data encryption key (DEK). This DEK is then encrypted with a replica-specific key, called a key encryption key (KEK) that is owned by the Secret Manager service.

When using CMEK for Secret Manager, the KEK is called a CMEK key and is a symmetric key you manage within Cloud KMS. The CMEK key must be in the same Google Cloud location as the secret version replica it encrypts. You can also use a Cloud EKM key in the CMEK policy for encryption and decryption.

This guide walks through how to configure Secret Manager to use CMEK. For more information about CMEK in general, including when and why to enable it, see the [Cloud Key Management Service documentation](https://docs.cloud.google.com/kms/docs/cmek).

**Note:** Secret Manager uses the `primary` Cloud KMS key version for CMEK encryption. CMEK cannot be configured with a specific key version.

## Key rotation

When you rotate a Cloud Key Management Service key, the new key version becomes the `primary` version. Secret Manager uses the following logic for key rotation:

  * New secret versions created after the rotation automatically use the new primary key version for encryption.
  * Existing secret versions aren't automatically re-encrypted. Secret Manager can still access secret versions that were encrypted with previous key versions as long as those key versions remain enabled. For example, if you add a new version to a CMEK-protected secret and then rotate the key, the original secret version is encrypted with its original key version, and the new secret version is encrypted with the new key version. Both secret versions are accessible.



## Limitations

CMEK is available only in the Secret Manager [`v1`](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets) API and Google Cloud CLI.

## Before you begin

You may choose to store all resources in the same project or to store secrets and keys in separate projects. Read Cloud KMS [Separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties) to better understand this decision.

Complete the following prerequisites to set up Secret Manager and Cloud KMS:

  * **Secret Manager:**

    * Create or use an existing project to hold your Secret Manager resources.
    * If necessary, complete the steps in the [Configuring Secret Manager](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager) section of the Secret Manager quickstart.
  * **Cloud KMS:**

    * Create or use an existing project to hold your Cloud KMS resources.
    * If necessary, [enable the Cloud KMS API](https://docs.cloud.google.com/kms/docs/quickstart#before_you_begin).



Set the following variables to the project IDs of your Secret Manager and Cloud KMS projects.
    
    
    This is an editable variable. Set it to your Secret Manager project ID and the
    value will be used in all commands on this page.
    SM_PROJECT_ID
    
    This is an editable variable. Set it to your Cloud KMS project ID and the value
    will be used in all commands on this page.
    KMS_PROJECT_ID
    

Authenticate to Google Cloud:

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud auth login

**Note:** Cloud KMS usage is subject to Cloud HSM and Cloud EKM [additional quota limitations](https://docs.cloud.google.com/kms/docs/quotas#cloud_hsm_quotas) depending on the type of CMEK key used. Secret Manager calls Cloud KMS every time it performs a cryptographic operation. CMEK key usage is billed to the Cloud KMS project.

## Creating a service agent identity

**Note:** To create a service identity with the required permissions, you must have `resourcemanager.projects.setIamPolicy` permission. This permission is included in the Project Owner, Project IAM Admin, and Organization Administrator roles.

You need to create a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) identity for each project that requires customer-managed encryption keys.

To create a service identity with Google Cloud CLI, run the following command:

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud beta services identity create \
        --service "secretmanager.googleapis.com" \
        --project "SM_PROJECT_ID"

Which will return a service identity name in the following format:
    
    
    service-PROJECT_NUMBER@gcp-sa-secretmanager.iam.gserviceaccount.com
    

Save the service identity name:
    
    
    The following variable is editable. Click on it to update the value, and it will
    be reflected throughout this documentation page.
    
    SM_SERVICE_IDENTITY
    

You will grant this service identity access to the CMEK Cloud KMS keys used to encrypt and decrypt your secrets.

## CMEK with automatic replication

This section covers secrets that are configured via an automatic replication policy.

For secrets that use the automatic replication policy, your CMEK key must be located in the `global` Cloud KMS multi-region. If you're using a Cloud EKM key, you cannot configure your secret to use automatic replication because Cloud EKM keys are not available in the `global` region. To learn more about using Cloud EKM keys, see Add a Cloud EKM key to a CMEK policy.

Create a symmetric Cloud KMS key in the `global` Cloud KMS region, or use an existing key. This example creates a new key ring called `secret-manager-cmek`, then creates a new key called `my-cmek-key` on it.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keyrings create "secret-manager-cmek" \
        --project "KMS_PROJECT_ID" \
        --location "global"
    
    
    gcloud kms keys create "my-cmek-key" \
        --project "KMS_PROJECT_ID" \
        --location "global" \
        --keyring "secret-manager-cmek" \
        --purpose "encryption"

Grant the service identity for Secret Manager access to encrypt and decrypt using the CMEK key. This command grants the Cloud KMS Encrypter / Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the `my-cmek-key` Cloud KMS key to the service identity.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys add-iam-policy-binding "my-cmek-key" \
        --project "KMS_PROJECT_ID" \
        --location "global" \
        --keyring "secret-manager-cmek" \
        --member "serviceAccount:SM_SERVICE_IDENTITY" \
        --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

Create a secret with automatic replication. The resource name of the CMEK key is stored as metadata on the secret.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets create "SECRET_ID" \
        --replication-policy "automatic" \
        --kms-key-name "projects/KMS_PROJECT_ID/locations/global/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key" \
        --project "SM_PROJECT_ID"

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

Set the value of `replication.automatic.customerManagedEncryption.kmsKeyName` to the resource name for the CMEK key.
    
    
    curl "https://secretmanager.googleapis.com/v1/projects/${SM_PROJECT_ID}/secrets?secretId=SECRET_ID" \
        --request "POST" \
        --header "Content-Type: application/json" \
        --header "Authorization: Bearer ACCESS_TOKEN" \
        --data-binary @- <<EOF
    {
      "replication":{
        "automatic":{
          "customerManagedEncryption":{
            "kmsKeyName": "projects/KMS_PROJECT_ID/locations/global/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
          }
        }
      }
    }
    EOF

Now, each time a secret version is created in that secret, the secret version's payload is automatically encrypted using the key before being written to persistent storage, as long as the service identity has access to the CMEK key. If the service identity loses access or if the key becomes unavailable, an attempt to create a new secret version or access an existing one returns an error.

Add a new secret version. Notice that you don't specify the Cloud KMS key's resource name; it is read from the secret's metadata.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    echo -n "SECRET_DATA" | gcloud secrets versions add "SECRET_ID" \
        --project "SM_PROJECT_ID" \
        --data-file -

The secret version is created, even if the caller doesn't have direct access to use the CMEK key. The service identity for Secret Manager, rather than the caller, is responsible for encrypting and decrypting secrets when reading or writing them.

Similarly, you don't need direct access to the CMEK key in order to access the secret. The service identity accesses the key and encrypts or decrypts the secret on your behalf.

Access the secret version you just created:

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets versions access "latest" \
        --project "SM_PROJECT_ID" \
        --secret "SECRET_ID"

### Update CMEK configuration

Create a new symmetric KMS keys in the `global` Cloud KMS multi-region.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys create "my-other-key" \
        --project "KMS_PROJECT_ID" \
        --location "global" \
        --keyring "secret-manager-cmek" \
        --purpose "encryption"

Grant the service identity for Secret Manager access to encrypt and decrypt using the new CMEK key. This command grants the Cloud KMS Encrypter / Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the `my-other-key` Cloud KMS key to the service identity.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys add-iam-policy-binding "my-other-key" \
        --project "KMS_PROJECT_ID" \
        --location "global" \
        --keyring "secret-manager-cmek" \
        --member "serviceAccount:SM_SERVICE_IDENTITY" \
        --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

Modify the CMEK configuration on a secret by updating the replication on the secret with the new Cloud KMS key resource names.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets replication update "SECRET_ID" \
        --set-kms-key "projects/KMS_PROJECT_ID/locations/global/keyRings/secret-manager-cmek/cryptoKeys/my-other-key" \
        --project "SM_PROJECT_ID"

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    curl "https://secretmanager.googleapis.com/v1/projects/${SM_PROJECT_ID}/secrets/SECRET_ID?updateMask=replication" \
        --request "PATCH" \
        --header "Authorization: Bearer ACCESS_TOKEN" \
        --header "Content-Type: application/json" \
        --data-binary @- <<EOF
    {
      "replication": {
        "automatic":{
          "customerManagedEncryption":{
            "kmsKeyName": "projects/KMS_PROJECT_ID/locations/global/keyRings/secret-manager-cmek/cryptoKeys/my-other-key"
          }
        }
      }
    }
    EOF

**Warning:** Updating the CMEK configuration only applies to new secret versions. Existing secret versions are not re-encrypted. Existing secret versions can't be accessed if the CMEK key that encrypted it is unavailable. If a key is destroyed, the secret data is unrecoverable.**Note:** Secret Manager does not currently support modifying other properties of the replication policy other than the CMEK configuration.

## CMEK with user managed replication

This section covers secrets that are configured with a user managed replication policy. With a user managed replication policy, you control the Google Cloud location where the secret is stored. Secrets are always accessible from every Google Cloud location.

Secrets with a user managed replication policy must use Cloud KMS keys that map exactly to the locations in which the secret versions are stored. The examples in this guide store a secret in two separate locations: us-east1, us- central1. Requests to access the secret are routed to one of these locations.

In each of the two regions, create a key ring and a Cloud KMS key with the purpose of encryption, or use an existing key. This example creates a new key ring called `"secret-manager-cmek"`, then creates a key called `"my-cmek-key"` in each region.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keyrings create "secret-manager-cmek" \
        --project "KMS_PROJECT_ID" \
        --location "us-east1"
    
    
    gcloud kms keys create "my-cmek-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-east1" \
        --keyring "secret-manager-cmek" \
        --purpose "encryption"
    
    
    gcloud kms keyrings create "secret-manager-cmek" \
        --project "KMS_PROJECT_ID" \
        --location "us-central1"
    
    
    gcloud kms keys create "my-cmek-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-central1" \
        --keyring "secret-manager-cmek" \
        --purpose "encryption"

Grant the service identity for Secret Manager permission to encrypt and decrypt using the CMEK key by granting the Cloud KMS Encrypter / Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) for each of the CMEK keys individually or for all keys in the project.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys add-iam-policy-binding "my-cmek-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-east1" \
        --keyring "secret-manager-cmek" \
        --member "serviceAccount:SM_SERVICE_IDENTITY" \
        --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"
    
    
    gcloud kms keys add-iam-policy-binding "my-cmek-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-central1" \
        --keyring "secret-manager-cmek" \
        --member "serviceAccount:SM_SERVICE_IDENTITY" \
        --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

Create a CMEK enabled secret with user managed replication. The resource name of the CMEK key is stored as metadata on the secret.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    cat <<EOF > ./replication-policy.json
    {
      "userManaged":{
        "replicas":[
          {
            "location":"us-east1",
            "customerManagedEncryption":{
              "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-east1/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
            }
          },
          {
            "location":"us-central1",
            "customerManagedEncryption":{
              "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-central1/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
            }
          }
        ]
      }
    }
    EOF
    
    
    gcloud secrets create "my-ummr-secret" \
        --replication-policy-file ./replication-policy.json \
        --project "SM_PROJECT_ID"

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

Set the value of `replication.userManaged.replicas.customerManagedEncryption.kmsKeyName`to the resource names for the CMEK keys.
    
    
    curl "https://secretmanager.googleapis.com/v1/projects/SM_PROJECT_ID/secrets?secretId=my-ummr-secret" \
    --request "POST" \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer ACCESS_TOKEN" \
    --data-binary @- <<EOF
    {
      "replication":{
        "userManaged":{
          "replicas":[
            {
              "location":"us-east1",
              "customerManagedEncryption":{
                "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-east1/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
              }
            },
            {
              "location":"us-central1",
              "customerManagedEncryption":{
                "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-central1/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key"
              }
            }
          ]
        }
      }
    }
    EOF

Now, each time a secret version is created in that secret, the secret version's payload is automatically encrypted using the key before being written to persistent storage, as long as the service identity has access to the CMEK key. If the service identity loses access or if the key becomes unavailable, an attempt to create a new secret version or access an existing one returns an error.

Add a new secret version. Notice that you don't specify the Cloud KMS key's resource name; it is read from the secret's metadata.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    echo -n "SECRET_DATA" | gcloud secrets versions add "my-ummr-secret" \
        --project "SM_PROJECT_ID" \
        --data-file -

The secret version is created, even if the caller doesn't have direct access to use the CMEK key. The service identity for Secret Manager, rather than the caller, is responsible for encrypting and decrypting secrets when reading or writing them.

Similarly, you don't need direct access to the CMEK key in order to access the secret. The service identity accesses the key and encrypts or decrypts the secret on your behalf.

Access the secret version you just created.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets versions access "latest" \
        --project "SM_PROJECT_ID" \
        --secret "my-ummr-secret"

### Update CMEK configuration

Create two new symmetric KMS keys in the same regions as the secret.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys create "my-other-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-east1" \
        --keyring "secret-manager-cmek" \
        --purpose "encryption"
    
    
    gcloud kms keys create "my-other-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-central1" \
        --keyring "secret-manager-cmek" \
        --purpose "encryption"

Grant the service identity for Secret Manager access to encrypt and decrypt using the new CMEK keys. This command grants the Cloud KMS Encrypter / Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the `my-other-key` Cloud KMS keys to the service identity.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys add-iam-policy-binding "my-other-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-east1" \
        --keyring "secret-manager-cmek" \
        --member "serviceAccount:SM_SERVICE_IDENTITY" \
        --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"
    
    
    gcloud kms keys add-iam-policy-binding "my-other-key" \
        --project "KMS_PROJECT_ID" \
        --location "us-central1" \
        --keyring "secret-manager-cmek" \
        --member "serviceAccount:SM_SERVICE_IDENTITY" \
        --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

Modify the CMEK configuration on a secret by updating the replication on the secret with the new Cloud KMS key resource names.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets replication update "my-ummr-secret" \
        --set-kms-key "projects/KMS_PROJECT_ID/locations/us-east1/keyRings/secret-manager-cmek/cryptoKeys/my-other-key" \
        --location us-east1 \
        --project "SM_PROJECT_ID"
    
    
    gcloud secrets replication update "my-ummr-secret" \
        --set-kms-key "projects/KMS_PROJECT_ID/locations/us-central1/keyRings/secret-manager-cmek/cryptoKeys/my-other-key" \
        --location us-central1 \
        --project "SM_PROJECT_ID"

In order to update multiple keys in a secret simultaneously, you may get and set the replication policy via a file.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets replication get "my-ummr-secret" \
        --project "SM_PROJECT_ID" \
        --format=json > ./replication-policy.json

Update the file to reflect desired CMEK configuration in your preferred editor. Then set the new policy:
    
    
    gcloud secrets replication set "my-ummr-secret" \
        --replication-policy-file ./replication-policy.json \
        --project "SM_PROJECT_ID"

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    curl "https://secretmanager.googleapis.com/v1/projects/${SM_PROJECT_ID}/secrets/my-ummr-secret?updateMask=replication" \
        --request "PATCH" \
        --header "Authorization: Bearer ACCESS_TOKEN" \
        --header "Content-Type: application/json" \
        --data-binary @- <<EOF
    {
      "replication":{
        "userManaged":{
          "replicas":[
            {
              "location":"us-east1",
              "customerManagedEncryption":{
                "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-east1/keyRings/secret-manager-cmek/cryptoKeys/my-other-key"
              }
            },
            {
              "location":"us-central1",
              "customerManagedEncryption":{
                "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-central1/keyRings/secret-manager-cmek/cryptoKeys/my-other-key"
              }
            }]
          }
        }
      }
    EOF

**Warning:** Updating the CMEK configuration only applies to new secret versions. Existing secret versions are not re-encrypted. Existing secret versions can't be accessed if the CMEK key that encrypted it is unavailable. If a key is destroyed, the secret data is unrecoverable.**Note:** Secret Manager does not currently support modifying other properties of the replication policy other than the CMEK configuration.

## View secret version CMEK configuration

To inspect a secret version's metadata, including whether the secret version is CMEK-enabled and the resource name of the CMEK key version, view its metadata.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets versions describe "latest" \
        --secret "SECRET_ID" \
        --project "SM_PROJECT_ID"

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    curl "https://secretmanager.googleapis.com/v1/projects/SM_PROJECT_ID/secrets/SECRET_ID/versions/latest" \
        --request "GET" \
        --header "Authorization: Bearer ACCESS_TOKEN" \
        --header "Content-Type: application/json"

This returns the full Cloud KMS resource name of the key version used to encrypt the secret version.
    
    
    {
      "name": "projects/PROJECT_NUMBER/secrets/SECRET_ID/versions/1",
      "createTime": "2021-07-...",
      "state": "ENABLED",
      "replicationStatus": {
        "automatic": {
          "customerManagedEncryption": {
            "kmsKeyVersionName": "projects/KMS_PROJECT_ID/locations/global/keyRings/secret-manager-cmek/cryptoKeys/my-cmek-key/cryptoKeyVersions/1"
          }
        }
      }
    }
    

## Add a Cloud EKM key to a CMEK policy

This section covers adding a [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) key to a CMEK policy. These steps enable a Cloud EKM key to be used to encrypt or decrypt secrets.

Since Cloud EKM does not currently support the `global` multi-region, Cloud EKM keys can only be used with secrets configured for user managed replication.

Create a symmetric key in the `us-central1` Cloud KMS region (or any region except for `global`). This example creates a new key ring called `secret-manager-cmek-ekm`, then creates a new key called `my-ekm-key` on the key ring.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 

Create a new key ring:
    
    
    gcloud kms keyrings create "secret-manager-cmek-ekm" \
      --project "KMS_PROJECT_ID" \
      --location "us-central1"

Create a key in that key ring:
    
    
    gcloud kms keys create "my-ekm-key" \
      --keyring "secret-manager-cmek-ekm" \
      --location "us-central1" \
      --purpose "encryption" \
      --protection-level "external" \
      --skip-initial-version-creation \
      --default-algorithm "external-symmetric-encryption"

Next, create a new version of `my-ekm-key` using the external URI of the key. For more information on external URIs for Cloud EKM keys, see [Create an external key](https://docs.cloud.google.com/kms/docs/ekm-internet#create_external_key).

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys versions create \
      --key "my-ekm-key" \
      --keyring "secret-manager-cmek-ekm" \
      --location "us-central1" \
      --external-key-uri EXTERNAL_KEY_URI \
      --primary

Grant the service identity for Secret Manager access to encrypt and decrypt using the external key. This command grants the Cloud KMS Encrypter / Decrypter role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on `my-ekm-key` to the service identity.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud kms keys add-iam-policy-binding "my-ekm-key" \
      --project "KMS_PROJECT_ID" \
      --location "us-central1" \
      --keyring "secret-manager-cmek-ekm" \
      --member "serviceAccount:SM_SERVICE_IDENTITY" \
      --role "roles/cloudkms.cryptoKeyEncrypterDecrypter"

Create a CMEK enabled secret that uses a Cloud EKM key.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    cat <<EOF > ./replication-policy.json
    {
      "userManaged":{
        "replicas":[
          {
            "location":"us-central1",
            "customerManagedEncryption":{
              "kmsKeyName":"projects/KMS_PROJECT_ID/locations/us-central1/keyRings/secret-manager-cmek-ekm/cryptoKeys/my-ekm-key"
            }
          }
        ]
      }
    }
    EOF
    
    
    gcloud secrets create "my-ekm-secret" \
        --replication-policy-file ./replication-policy.json \
        --project "SM_PROJECT_ID"

Now, each time a secret version is created in `my-ekm-secret`, the secret version's payload is automatically encrypted using the Cloud EKM key before being written to persistent storage, as long as the service identity has access to the key. If the service identity loses access or if the key becomes unavailable, an attempt to create a new secret version or access an existing one returns an error.

Add a new secret version. Notice that the key's resource name is read from the secret's metadata.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    echo -n "SECRET_DATA" | gcloud secrets versions add "my-ekm-secret" \
        --project "SM_PROJECT_ID" \
        --data-file -

The secret version is created, even if the caller doesn't have direct access to use the key. The service identity for Secret Manager, rather than the caller, is responsible for encrypting and decrypting secrets when reading or writing them.

Access the secret version you just created. This is where the service identity accesses the key and encrypts or decrypts the secret on your behalf.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets versions access "latest" \
      --project "SM_PROJECT_ID" \
      --secret "my-ekm-secret"

## Disable CMEK

Remove CMEK configuration from a secret by updating the replication policy.

### gcloud

To use Secret Manager on the command line, first [Install or upgrade to version 378.0.0 or higher of the Google Cloud CLI](https://docs.cloud.google.com/sdk/install). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    gcloud secrets replication update "SECRET_ID" --remove-cmek \
        --project "SM_PROJECT_ID"

### API

These examples use [curl](https://curl.haxx.se/) to demonstrate using the API. You can generate [access tokens](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials) with `gcloud auth print-access-token`. On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    curl "https://secretmanager.googleapis.com/v1/projects/${SM_PROJECT_ID}/secrets/SECRET_ID?updateMask=replication" \
        --request "PATCH" \
        --header "Authorization: Bearer ACCESS_TOKEN" \
        --header "Content-Type: application/json" \
        --data-binary @- <<EOF
    {
      "replication":{
        "automatic":{}
      }
    }
    EOF

**Warning:** Removing CMEK configuration only applies to new secret versions. Existing secret versions are not affected. Existing secret versions can't be accessed if the CMEK key that encrypted it is unavailable. If a key is destroyed, the secret data is unrecoverable.

## What's next

  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
