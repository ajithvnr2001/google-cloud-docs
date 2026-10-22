---
url: https://docs.cloud.google.com/kms/docs/migrate-external-keys/
title: Migrate external keys \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:53.100532+00:00
---

# Migrate external keys  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/migrate-external-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Migrate external keys Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to migrate your Cloud EKM keys between the external over internet (`EXTERNAL`) and external over VPC (`EXTERNAL_VPC`) protection levels. Migrating external keys is only supported for gcloud CLI and the Cloud KMS API.

## Migration use cases

When a key has the `EXTERNAL` or `EXTERNAL_VPC` protection level, you can do any of the following:

  * Rotate the key, creating a new key version with a different Cloud EKM protection level than the parent key. For example, you can rotate a key in the `EXTERNAL` protection level to create a new key version in the `EXTERNAL_VPC` protection level.
  * Update a key version to use a different Cloud EKM protection level for the same key material. For example, you can update a key version in the `EXTERNAL` protection level to use the same key material and the same key version resource with the `EXTERNAL_VPC` protection level instead.
  * Rotate an `EXTERNAL_VPC` key or update an `EXTERNAL_VPC` key version to use a different `EkmConnection` than the parent key.



Migrating an existing key version between the two Cloud EKM protection levels lets you change how you access your external key material without needing to reconfigure your applications or re-encrypt your data and with zero downtime. Your migrated key uses the same key material and the same resource identifier.

When you migrate a key version from the `EXTERNAL` protection level to the `EXTERNAL_VPC` protection level, you associate an `EkmConnection` resource with the key version and add the `ekmConnectionKeyPath`. When you migrate a key version from the `EXTERNAL_VPC` to the `EXTERNAL` protection level, you add a `externalKeyUri` to replace the `EkmConnection` and `ekmConnectionKeyPath`.

If a key version has an `EkmConnection` associated with it, that connection is used for all key version operations, even if the parent key has a different `EkmConnection`.

### Migrating to external over VPC

Migrating from the external over internet protection level to the external over VPC protection level provides improved reliability for your Cloud EKM keys. You get the benefits of [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc), including robust isolation and better operational support.

You can also migrate between different VPC configurations—for example, to upgrade from using VPC with [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) to using VPC with [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview).

## Before you begin

Before you can migrate Cloud EKM keys, you must have the following:

  1. A Google Cloud project with both billing and the Cloud KMS API enabled.
  2. To get the permission that you need to migrate external keys, ask your administrator to grant you the [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`) IAM role on the project or a parent resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `cloudkms.cryptoKeys.update` permission, which is required to migrate external keys. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  3. If you're migrating to the external over internet (`EXTERNAL`) protection level, then you must [Set up Cloud EKM over the internet](https://docs.cloud.google.com/kms/docs/set-up-ekm-internet) if you haven't already.
  4. If you're migrating to the external over VPC (`EXTERNAL_VPC`) protection level or migrating to a new VPC network, then you must [Create an EKM connection](https://docs.cloud.google.com/kms/docs/create-ekm-connection) if you haven't already.



## Create a new manually managed external over VPC key version

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create a new external over VPC key version on an existing Cloud EKM key, use the `kms keys versions create` command with the `--protection-level`, `--crypto-key-backend`, and `--ekm-connection-key-path` flags:
    
    
    gcloud kms keys versions create \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --protection-level "external-vpc" \
        --crypto-key-backend EKM_CONNECTION_PATH \
        --ekm-connection-key-path EXTERNAL_KEY_PATH
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EKM_CONNECTION_PATH`: the resource identifier of the EKM connection that you want to use for the new key version—for example, `projects/PROJECT_ID/locations/LOCATION/ekmConnections/EKM_CONNECTION`
  * `EXTERNAL_KEY_PATH`: the path to the new external key version from your EKM connection—for example, `v0/path/to/my/key`.



If the parent key is 

If the key is a symmetric encryption key and you want to make the new key version the primary version, add the `--primary` flag.

For information on all flags and possible values, run the command with the `--help` flag.

### REST

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To create a new external over VPC key version on an existing Cloud EKM key, create a new key version by calling the [CryptoKeyVersions.create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{
                "protectionLevel": "EXTERNAL_VPC",
                "externalProtectionLevelOptions": {
                  "ekmConnectionKeyPath": "EXTERNAL_KEY_PATH",
                  "ekmConnectionBackendOverride": "EKM_CONNECTION_PATH"
                  },
                }'
    

  * `PROJECT_ID`: the identifier of the project that contains the key that you want to rotate.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EKM_CONNECTION_PATH`: the resource identifier of the EKM connection that you want to use for the new key version—for example, `projects/PROJECT_ID/locations/LOCATION/ekmConnections/EKM_CONNECTION`
  * `EXTERNAL_KEY_PATH`: the path to the new external key version from your EKM connection—for example, `v0/path/to/my/key`.



This command creates a new key version, but doesn't set it as the primary version.

To set your new key version as primary, see [Setting an existing version as the primary key version](https://docs.cloud.google.com/kms/docs/rotate-key#set_primary).

## Create new external over internet key version

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create a new external over internet key version on an existing Cloud EKM key, use the `kms keys versions create` command with the `--protection-level`, and `--external-key-uri` flags:
    
    
    gcloud kms keys versions create \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --protection-level "external" \
        --external-key-uri EXTERNAL_KEY_URI
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_URI`: the URI to the new external key version.



If the key is a symmetric encryption key and you want to make the new key version the primary version, add the `--primary` flag.

For information on all flags and possible values, run the command with the `--help` flag.

### REST

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To create a new external over internet key version on an existing Cloud EKM key, create a new key version by calling the [CryptoKeyVersions.create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{
                "protectionLevel": "EXTERNAL",
                "externalProtectionLevelOptions": {
                  "externalKeyUri": "EXTERNAL_KEY_URI",
                  },
                }'
    

  * `PROJECT_ID`: the identifier of the project that contains the key that you want to rotate.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_URI`: the URI to the new external key version.



This command creates a new key version, but doesn't set it as the primary version.

To set your new key version as primary, see [Setting an existing version as the primary key version](https://docs.cloud.google.com/kms/docs/rotate-key#set_primary).

## Update a key version to use the external over VPC protection mode

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To update an existing `external` key version to the `external-vpc` protection level, use the `kms keys versions update` command with the `--protection-level`, `--crypto-key-backend`, and `--ekm-connection-key-path` flags:
    
    
    gcloud kms keys versions update KEY_VERSION \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --protection-level "external-vpc" \
        --crypto-key-backend EKM_CONNECTION_PATH \
        --ekm-connection-key-path EXTERNAL_KEY_PATH
    

Replace the following:

  * `KEY_VERSION`: the number of the key version that you want to migrate—for example, `3`.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EKM_CONNECTION_PATH`: the resource identifier of the EKM connection that you want to use for the key version—for example, `projects/PROJECT_ID/locations/LOCATION/ekmConnections/EKM_CONNECTION`
  * `EXTERNAL_KEY_PATH`: the new path to the existing external key material from your EKM connection—for example, `v0/path/to/my/key`. The EKM connection and key path must point to the same key material as the current key URI does.



For information on all flags and possible values, run the command with the `--help` flag.

### REST

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To update an existing `external` key version to the `external-vpc` protection level, call the [CryptoKeyVersions.patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/patch) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION?updateMask=protectionLevel,externalProtectionLevelOptions" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{
                "protectionLevel": "EXTERNAL_VPC",
                "externalProtectionLevelOptions": {
                  "ekmConnectionKeyPath": "EXTERNAL_KEY_PATH",
                  "ekmConnectionBackendOverride": "EKM_CONNECTION_PATH"
                  },
                }'
    

  * `PROJECT_ID`: the identifier of the project that contains the key that you want to migrate.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EKM_CONNECTION_PATH`: the resource identifier of the EKM connection that you want to use for the key version—for example, `projects/PROJECT_ID/locations/LOCATION/ekmConnections/EKM_CONNECTION`
  * `EXTERNAL_KEY_PATH`: the new path to the existing external key material from your EKM connection—for example, `v0/path/to/my/key`. The EKM connection and key path must point to the same key material as the current key URI does.



## Update a key version to use the external over internet protection mode

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To update an existing `external-vpc` key version to the `external` protection level, use the `kms keys versions update` command with the `--protection-level` and `--external-key-uri` flags:
    
    
    gcloud kms keys versions update KEY_VERSION \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --protection-level "external" \
        --external-key-uri EXTERNAL_KEY_URI
    

Replace the following:

  * `KEY_VERSION`: the number of the key version that you want to migrate—for example, `3`.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_URI`: the new URI to the existing external key material in your EKM. The URI must point to the same key material as the current EKM connection and external key.



For information on all flags and possible values, run the command with the `--help` flag.

### REST

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To update an existing `external-vpc` key version to the `external` protection level, call the [CryptoKeyVersions.patch](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/patch) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION?updateMask=protectionLevel,externalProtectionLevelOptions" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{
                "protectionLevel": "EXTERNAL",
                "externalProtectionLevelOptions": {
                  "externalKeyUri": "EXTERNAL_KEY_URI",
                  },
                }'
    

  * `PROJECT_ID`: the identifier of the project that contains the key that you want to migrate.
  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_URI`: the new URI to the existing external key material in your EKM. The URI must point to the same key material as the current EKM connection and external key.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
