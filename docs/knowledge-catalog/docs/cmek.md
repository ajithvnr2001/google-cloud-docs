---
url: https://docs.cloud.google.com/knowledge-catalog/docs/cmek/
title: Enable customer-managed encryption keys \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:19.978806+00:00
---

# Enable customer-managed encryption keys  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/cmek/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Enable customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to encrypt Knowledge Catalog (formerly Dataplex Universal Catalog) data with customer-managed encryption keys (CMEK).

## Overview

By default, Knowledge Catalog encrypts customer content at rest. Knowledge Catalog handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Knowledge Catalog. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Knowledge Catalog resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Knowledge Catalog uses one CMEK per location for all Knowledge Catalog resources.

You can configure a CMEK key at the organization level in Knowledge Catalog.

For more information about CMEK in general, including when and why to enable it, see [Customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek).

## Benefits of CMEK

CMEK lets you do the following:

  * Manage key lifecycle operations and access permissions.
  * Track key usage with the Key Inventory API and Key Usage dashboards in Cloud KMS, which let you see things such as which keys protect which resources. Cloud Logging tells you when the keys were accessed and by whom.
  * Meet specific regulatory requirements by managing your encryption keys.



## How CMEK works with Knowledge Catalog

Knowledge Catalog encryption administrators in your Google Cloud project can configure CMEK for Knowledge Catalog by providing the Cloud KMS key. Then, Knowledge Catalog uses the specified Cloud KMS key to encrypt all data, including existing data and any new resources created within Knowledge Catalog.

### Supported features

  * Knowledge Catalog supports CMEK encryption for the following features:

    * [Auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview)
    * [Data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview)
    * [Data discovery](https://docs.cloud.google.com/bigquery/docs/automatic-discovery)
    * [Data insights](https://docs.cloud.google.com/bigquery/docs/data-insights)
    * [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview)
    * [Business Glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries)
    * [Knowledge Catalog search](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets)
  * [Data Lineage](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage) doesn't store customer core content or sensitive data, and therefore doesn't require CMEK encryption.

  * Assured Workloads customers can't use other Knowledge Catalog features because CMEK encryption is not supported for them.

  * Customers who don't use Assured Workloads can use other features, but data is encrypted using Google default encryption.




## Considerations

  * By default, each organization is provisioned using Google default encryption.
  * The Organization Administrator can switch to CMEK in Knowledge Catalog for any location.
  * Knowledge Catalog supports Cloud KMS keys, Cloud HSM keys, and Cloud External Key Manager keys.
  * Key rotation is supported, and after it is available, the new key version is automatically used for data encryption. Existing data is also encrypted with this new version.
  * Knowledge Catalog retains data backups for a maximum of 15 days. Any backups created after you enable CMEK are encrypted using the specified KMS key. Data backed up before enabling CMEK remains encrypted with Google's default encryption for a maximum of 15 days.



## Limitations

  * Switching to CMEK is an irreversible process. After you opt for CMEK, you cannot revert to Google default encryption.
  * After a Cloud KMS key is configured for Knowledge Catalog, it cannot be updated or changed.
  * Knowledge Catalog supports organization-level encryption only. As a result, the encryption configuration is set at the organization level for a given location and is used to encrypt Knowledge Catalog data for all projects within that organization and location. CMEK encryption is not supported for specific projects under an organization or folder. Setting CMEK-related organization policies requires careful consideration.
  * Knowledge Catalog doesn't support CMEK in the global region.
  * When CMEK is enabled for Knowledge Catalog, the following features don't work:

    * Cross-organizational metadata Search
  * When you enable CMEK in Knowledge Catalog, don't migrate projects into or out of the CMEK organization. Modifying a project's organizational placement will result in a permanent loss of Knowledge Catalog-stored metadata for that project.




## Upgrade existing CMEK configurations

If you enabled CMEK in Knowledge Catalog before November 7, 2025, run the following command to extend CMEK coverage to Knowledge Catalog and Knowledge Catalog search:
    
    
      gcloud dataplex encryption-config update organizations/ORG_ID/locations/LOCATION/encryptionConfigs/default --enable-metastore-encryption
    

  * Replace ORG_ID with the ID of the organization that contains the key.
  * Replace LOCATION with the location of the organization that contains the key.



When the data is encrypted, you might get a [Knowledge Catalog availability issue](https://docs.cloud.google.com/knowledge-catalog/docs/cmek#data_encryption_and_api_availability).

If you enable CMEK for the first time after November 7, 2025, Knowledge Catalog Metastore and Search are included in the CMEK coverage by default.

## Protect your encryption keys

**Warning:** You are responsible for managing your CMEK keys. If a key is disabled or destroyed, you will lose access to the data that is encrypted by that key.

To ensure continued access to the data that is encrypted by CMEK, follow these best practices:

  * Ensure that your CMEK keys remain enabled and accessible. If a key is disabled or destroyed, Knowledge Catalog data becomes inaccessible. If the key is unavailable for more than 30 days, data encrypted with that key is automatically deleted and cannot be recovered.
  * If the Cloud KMS key is destroyed and unrecoverable, all associated Knowledge Catalog data will be permanently lost.
  * In cases where Cloud KMS is temporarily unavailable, Knowledge Catalog continues to support full operations on a best-effort basis for up to one hour. After this period, data will become temporarily inaccessible as a protective measure.
  * When using Cloud EKM, be aware that Google doesn't control the availability of your externally managed keys. Short-term key unavailability results in temporary data inaccessibility. Key unavailability that continues for 30 days results in permanent data loss.



## Knowledge Catalog availability

The following sections outline the process and expected operational impact when you enable CMEK for your Knowledge Catalog organization.

### Initial infrastructure provisioning

After you save the encryption configuration, Knowledge Catalog sets up the necessary infrastructure. This process typically takes 6 to 8 hours. During this provisioning phase, you retain full access to all Knowledge Catalog features and functionalities, and the data remains encrypted through Google-managed encryption. If the organization policy `constraints/gcp.restrictNonCmekServices` is set, then resource creation requests fail until the provisioning phase is complete.

### Data encryption and API availability

After infrastructure provisioning, Knowledge Catalog begins encrypting existing data stored within the organization. To ensure data integrity and prevent potential inconsistencies during this encryption process, Dataplex API methods are temporarily unavailable. This restriction prevents data update operations. When you initially activate CMEK for Knowledge Catalog, all existing data is encrypted. This one-time operation is estimated to take up to two hours.

### Post-encryption operations

After successful completion of the existing data encryption, Dataplex API methods are fully available. Creating or modifying data within Knowledge Catalog is automatically encrypted using the configured CMEK, without any operational interruptions or API restrictions.

## Create a key and enable CMEK

The following instructions explain how to create a key and enable CMEK for Knowledge Catalog. You can use a key created directly in Cloud KMS or an externally managed key that you make available with [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm).

  1. In the Google Cloud project where you want to manage your keys, do the following:

     1. [Enable the Cloud Key Management Service API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com).

     2. [Create a Cloud KMS key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) in the location where you want to use it.

     3. Create a key using one of the following options:

        * [Create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key).
        * [Create an external key](https://docs.cloud.google.com/kms/docs/create-external-key).

If you use an external key manager (Cloud EKM), you must grant the Cloud KMS service account access to your key in your external key management partner system. If you connect to your external key manager over a VPC, you must also grant the Cloud EKM service account (`service-KEY_PROJECT_NUMBER@gcp-sa-ekms.iam.gserviceaccount.com`) the Service Directory Viewer (`roles/servicedirectory.viewer`) and Private Service Connect Authorized Service (`roles/servicedirectory.pscAuthorizedService`) roles in your VPC project. For more information, see [Create an EKM connection](https://docs.cloud.google.com/kms/docs/create-ekm-connection).

  2. Create and display the Google-managed service account:
         
         gcloud beta services identity create \
             --service=dataplex.googleapis.com \
             --organization=ORG_ID
         

Replace ORG_ID with the ID of the organization that contains the key.

If you're prompted to install the Google Cloud CLI beta commands component, enter `Y`.

The gcloud CLI `services identity` command creates or gets the specific Google-managed service account that Knowledge Catalog can use to access the Cloud KMS key.

The service account ID is formatted as `service-org-ORG_ID@gcp-sa-dataplex.iam.gserviceaccount.com`. A CMEK-specific service account is also created, formatted as `service-org-ORG_ID@gcp-sa-dataplex-cmek.iam.gserviceaccount.com`. The CMEK-specific service account is used for encrypting and decrypting data stored in Knowledge Catalog. If you use VPC Service Controls for the Cloud KMS key, you must grant access to the CMEK-specific service account by using an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

  3. Grant the [CryptoKey Encrypter/Decrypter IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the Knowledge Catalog service account. Grant this permission on the key you created.

If you are using an external key manager (Cloud EKM), ensure that your external key manager system also grants access permissions to the Cloud KMS service account (`service-KEY_PROJECT_NUMBER@gcp-sa-cloudkms.iam.gserviceaccount.com`).

###  Console 

     1. Go to the **Key management** page.

[Go to Key management](https://console.cloud.google.com/security/kms)

     2. Click the key ring.

     3. In the list of available keys, click the key you created.

     4. Click the **Permissions** tab.

     5. Click **Grant access**.

     6. In the **Grant access** pane that opens, follow these steps to grant access to the Knowledge Catalog service account:

        1. In **Add principals** , enter the service account `service-org-ORG_ID@gcp-sa-dataplex.iam.gserviceaccount.com`.
        2. In **Assign roles** , select the Cloud KMS CryptoKey Encrypter/Decrypter role.
        3. Click **Save**.

###  gcloud 

Grant the service account the `cloudkms.cryptoKeyEncrypterDecrypter` role:
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --location=LOCATION \
        --keyring KEY_RING \
        --project=KEY_PROJECT_ID \
        --member serviceAccount:service-org-ORG_ID@gcp-sa-dataplex.iam.gserviceaccount.com \
        --role roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following:

     * KEY_NAME: the key name
     * LOCATION: the location
     * KEY_RING: the key ring
     * KEY_PROJECT_ID: the key project ID

  4. Assign the Dataplex Encryption Admin role to yourself.

###  Console 

Follow the instructions to [grant an IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

###  gcloud 
         
         gcloud organizations add-iam-policy-binding ORG_ID \
             --member='user:USER_EMAIL' \
             --role='roles/dataplex.encryptionAdmin'
         

Replace the following:

     * ORG_ID: the ID of the organization that contains the key.
     * USER_EMAIL: the email address of the user.

  5. Configure Knowledge Catalog to use your CMEK key.

###  Console 

     1. In the Google Cloud console, go to the Knowledge Catalog page.

[Go to Knowledge Catalog](https://console.cloud.google.com/dataplex)

     2. Click **Settings**.

     3. In **Select region for CMEK** , select a region. The region that you select must match the location of the Cloud KMS key.

     4. In **Select encryption key** , select the key you created.

     5. Click **Save**.

The data encryption process takes a while to complete. When the process completes, the following message appears: `Data Encryption is complete. Your selected CMEK key is now protecting your data.`

###  gcloud 

     1. Set the encryption config in Knowledge Catalog:
            
            gcloud dataplex encryption-config create default \
                --location=LOCATION \
                --organization=ORG_ID \
                --key=KEY_RESOURCE_ID
            

Replace the following:

        * ORG_ID: the ID of the organization that contains the key.
        * KEY_RESOURCE_ID: the [key resource ID](https://docs.cloud.google.com/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version) \- for example, `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME`. Replace PROJECT_ID with the key project ID. 
     2. Check that the encryption process is complete:
            
            gcloud dataplex encryption-config describe default \
                --location=LOCATION \
                --organization=ORG_ID
            

The data encryption process takes a while to complete. When the process completes, the following message appears: `encryptionState: COMPLETED`.




## Logging and monitoring

Audit Knowledge Catalog requests to Cloud KMS by enabling [audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access#config-console-enable) for the Cloud KMS API.

## CMEK organization policies

Google Cloud provides organization policy [constraints](https://docs.cloud.google.com/kms/docs/cmek-org-policy) to enforce CMEK usage and control the permissible Cloud KMS keys within your organization. These constraints help to ensure that data within Knowledge Catalog is consistently protected by CMEK.

  * `constraints/gcp.restrictNonCmekServices` enforces mandatory CMEK usage for Knowledge Catalog resources.

    * Adding `dataplex.googleapis.com` to the list of Google Cloud service names and setting the constraint to `Deny` prohibits the creation of Knowledge Catalog resources that don't have CMEK protection.

    * If a Cloud KMS key is not specified for the requested location in the CMEK encryption settings, requests to create resources within Knowledge Catalog will fail.

    * This policy is validated at the individual resource project level.

  * `constraints/gcp.restrictCmekCryptoKeyProjects` restricts the selection of Cloud KMS keys for CMEK to designated resource hierarchies.

    * By configuring a list of resource hierarchy indicators (projects, folders, or organizations) and setting the constraint to `Allow`, Knowledge Catalog is restricted to using CMEK keys only from the specified locations.

    * If a Cloud KMS key from a disallowed project is provided, requests to create CMEK-protected resources in Knowledge Catalog will fail.

    * This policy is validated at the resource project level during resource creation.

    * This policy is validated at the organization level when configuring CMEK encryption settings.

    * To prevent inconsistencies, make sure that project-level configurations align with organization-wide policies.




For more information about configuring organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

### Knowledge Catalog DataScans CMEK Permissions

When creating Data Profile or Data Quality scans against CMEK-encrypted BigQuery resources, grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to both the Knowledge Catalog Service Agent (`service-<var>PROJECT_NUMBER</var>@gcp-sa-dataplex.iam.gserviceaccount.com`) and the BigQuery Service Agent (`bq-<var>PROJECT_NUMBER</var>@bigquery-encryption.iam.gserviceaccount.com`) on the Cloud Key Management Service key protecting the BigQuery dataset:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --location=LOCATION \
        --keyring=KEYRING_NAME \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
        --role="roles/cloudkms.cryptoKeyEncrypterDecrypter"
    

## What's next

  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
