---
url: https://docs.cloud.google.com/kms/docs/release-notes/
title: Cloud KMS release notes \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:35:03.480475+00:00
---

# Cloud KMS release notes  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Resources ](https://docs.cloud.google.com/kms/docs/resources)



Send feedback 

#  Cloud KMS release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Key Management Service. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality.

**Current version: v1**

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/kms-release-notes.xml) directly. 

## September 23, 2026

Feature

**Preview:** Cloud EKM supports external key migration. For keys with the `EXTERNAL` or `EXTERNAL_VPC` protection levels, you can create new key versions with either of these protection levels. You can also change the protection level of existing external key versions to change how you access your existing key material with zero downtime and without reconfiguring your applications.

For more information about migrating external keys, see [Migrate external keys](https://docs.cloud.google.com/kms/docs/migrate-external-keys).

## August 24, 2026

Feature

Cloud KMS supports deleting key rings in General Availability.

For more information about deleting Cloud KMS resources, see [Delete Cloud KMS resources](https://docs.cloud.google.com/kms/docs/delete-kms-resources).

## August 06, 2026

Feature

**Preview:** Cloud KMS supports quantum-safe key import. You can use the following quantum-safe import methods:

  * `HPKE_KEM_XWING_HKDF_SHA256_AES_256_GCM`
  * `HPKE_KEM_ML_KEM_768_HKDF_SHA256_AES_256_GCM`
  * `HPKE_KEM_ML_KEM_1024_HKDF_SHA256_AES_256_GCM`



For more information about quantum-safe key import, see [Quantum-safe key import](https://docs.cloud.google.com/kms/docs/quantum-safe-key-import).

## July 29, 2026

Feature

Cloud KMS Autokey with same-project key storage (formerly known as Autokey for delegated key management) is generally available. Autokey with same-project key storage can be used on its own or alongside Autokey with dedicated-project key storage (formerly known as Autokey for centralized key management).

For more information, see [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey). To learn how to set guardrails to constrain how Autokey is used in your organization, see [Control Autokey usage](https://docs.cloud.google.com/kms/docs/control-autokey-usage).

## July 16, 2026

Feature

Cloud KMS supports the following post-quantum computing (PQC) signing algorithms in General Availability:

  * `PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256`
  * `PQ_SIGN_ML_DSA_44`
  * `PQ_SIGN_ML_DSA_44_EXTERNAL_MU`
  * `PQ_SIGN_ML_DSA_65`
  * `PQ_SIGN_ML_DSA_65_EXTERNAL_MU`
  * `PQ_SIGN_ML_DSA_87`
  * `PQ_SIGN_ML_DSA_87_EXTERNAL_MU`
  * `PQ_SIGN_SLH_DSA_SHA2_128S`



For more information about supported algorithms, see [PQC signing algorithms](https://docs.cloud.google.com/kms/docs/algorithms#pqc_signing_algorithms). For more information about PQC signing, see [Post-quantum cryptography (PQC) digital signature](https://docs.cloud.google.com/kms/docs/digital-signatures#pqc).

## July 07, 2026

Feature

The Cloud KMS overview dashboard **Asymmetric PQC insights** chart is generally available. You can use the **Asymmetric PQC insights** chart and details view to identify how many and which of your asymmetric keys are susceptible to attacks from future quantum computers. This information is an important input into your quantum computing modernization planning and process.

For more information about the **Asymmetric PQC insights** chart, see [View asymmetric post-quantum cryptography (PQC) insights](https://docs.cloud.google.com/kms/docs/view-pqc-insights).

## May 14, 2026

Feature

The Cloud KMS **Encryption metrics** dashboard and project-level key tracking are generally available. You can use the **Encryption metrics** dashboard to review summaries and details of your keys used in customer-managed encryption key (CMEK) integrations and the resources that they protect. The **Encryption metrics** dashboard and the key **Usage tracking** tab support both centralized key management using a dedicated key project and delegated key management using keys stored in the same projects as the resources that they protect.

For more information about the **Encryption metrics** dashboard, see [View encryption metrics](https://docs.cloud.google.com/kms/docs/view-encryption-metrics). For more information about project-level key tracking, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

## March 02, 2026

Feature

Cloud KMS deletion of keys and key versions is generally available. Keys and key versions must meet deletion criteria before they can be deleted. Names of deleted keys can't be reused.

For more information, including deletion criteria, see [Delete Cloud KMS resources](https://docs.cloud.google.com/kms/docs/delete-kms-resources).

## February 11, 2026

Feature

Cloud KMS Autokey for projects is available in Public Preview. Autokey for projects lets you enable Cloud KMS Autokey for delegated key management. In delegated key management, keys created by Autokey are created in the same project as the resources they protect. This option is suitable for your organization if project administrators are in charge of key management for the projects they manage.

You can still use Cloud KMS Autokey for centralized key management in a folder, where all keys that protect resources in that folder are created in a dedicated key project. You can also use centralized key management in a folder, with certain projects within that folder configured to use delegated key management and same-project keys instead of creating keys in the dedicated key project.

You can enable Autokey for projects on individual projects or on all projects within a folder. For more information, see [Enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

## January 20, 2026

Feature

Cloud KMS is available in the following region:

  * `asia-southeast3`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## December 17, 2025

Feature

Single-tenant Cloud HSM is now generally available. With Single-tenant Cloud HSM, you can create and manage dedicated single-tenant instances. Each instance is a cluster of partitions on HSMs in a single Cloud KMS region. Google manages the HSMs, but you have administrative control over your instance.

Single-tenant Cloud HSM is available in the following locations:

  * `us-central1`
  * `us-east4`
  * `europe-west1`
  * `europe-west4`



Creating a managing an instance requires quorum approval with two-factor authentication using keys that you create and secure outside of Google Cloud. Single-tenant Cloud HSM instances incur additional costs.

For more information about Single-tenant Cloud HSM, see [Single-tenant Cloud HSM](https://docs.cloud.google.com/kms/docs/single-tenant-hsm). To learn how to create and maintain a Single-tenant Cloud HSM instance, see [Create and manage a Single-tenant Cloud HSM instance](https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm). To see pricing details for Single-tenant Cloud HSM, see [Pricing for Single-tenant Cloud HSM](https://docs.cloud.google.com/kms/pricing#single-tenant).

## September 23, 2025

Feature

Cloud KMS now supports key encapsulation mechanisms (KEMs) for sharing secrets in Preview. KEMs are designed to be resistant to post-quantum attacks. You can use the following KEM algorithms:

  * `ML_KEM_768`
  * `ML_KEM_1024`
  * `KEM_XWING`



For more information about key encapsulation mechanisms, see [Key encapsulation mechanisms](https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms). To learn how to use key encapsulation mechanisms to share secrets, see [Encapsulate and decapsulate using KEMs](https://docs.cloud.google.com/kms/docs/encapsulate-decapsulate).

## June 30, 2025

Feature

Cloud HSM for Google Workspace now lets you use Cloud HSM keys for client-side encryption (CSE) to protect sensitive workloads in Google Workspace. For more information about Cloud HSM for Google Workspace, including how to get started, see [Onboard to Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/onboard-hsm-workspace).

## April 09, 2025

Feature

To help you get the right Cloud KMS keys on-demand, for consistent alignment with recommended encryption practices, Cloud KMS Autokey now has a free tier. The free tier covers the following usage:

  * 100 free active key versions monthly
  * 10,000 free cryptographic operations monthly



The free tier only applies to keys created using Cloud KMS Autokey. Key administration operations including key rotation are always free. For more details, see [Cloud Key Management Service pricing](https://cloud.google.com/kms/pricing)

## March 04, 2025

Feature

Cloud KMS is available in the following region:

  * `europe-north2`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## February 21, 2025

Feature

Cloud KMS now supports the following post-quantum computing (PQC) algorithms for digital signatures in Public Preview:

  * `PQ_SIGN_ML_DSA_65`: Module-lattice-based digital signature algorithm
  * `PQ_SIGN_SLH_DSA_SHA2_128S`: Stateless hash-based digital signature algorithm



To [Retrieve a public key](https://docs.cloud.google.com/kms/docs/retrieve-public-key) for a PQC key, you must use the `gcloud` CLI or the Cloud KMS REST API.

  * For the `gcloud` CLI, use the `--public-key-format nist-pqc` flag.
  * For the REST API, use the `public_key_format=NIST_PQC` header parameter.



For more information about PQC algorithms, see [PQC signing algorithms](https://docs.cloud.google.com/kms/docs/algorithms#pqc_signing_algorithms). For more information about PQC digital signatures, see [Post-quantum cryptography (PQC) digital signature](https://docs.cloud.google.com/kms/docs/digital-signatures#pqc).

## November 18, 2024

Feature

Cloud KMS is available in the following region:

  * `northamerica-south1`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## October 18, 2024

Feature

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Cloud KMS resources. For more information, see [Create custom organization policy constraints for Cloud KMS](https://docs.cloud.google.com/kms/docs/custom-org-policies).

## September 24, 2024

Feature

Cloud KMS with Autokey is now in General Availability for Cloud Storage, Compute Engine, BigQuery, Secret Manager, Cloud SQL, and Spanner.

Autokey simplifies creating and using [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek) by automating provisioning and assignment. With Autokey, key rings, keys, and service accounts don't need to be planned and provisioned before they're needed. Instead, Autokey generates keys on demand as resources are created.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## June 14, 2024

Change

As previously announced, Cloud KMS has changed the default duration of the scheduled for destruction period from 24 hours to 30 days.

As of February 1, 2024, newly created CryptoKeys use the new default duration of 30 days, unless a different duration is specified during key creation. For more information about key destruction, see [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore).

Owners of existing CryptoKeys that had used the default duration were given until May 1, 2024 to opt out from automatically updating those keys to use the new default duration. Existing CryptoKeys that were not opted out have been updated to use the new default duration of 30 days. No further action is required from you.

## May 16, 2024

Feature

Cloud KMS with Autokey is now in Preview for Cloud Storage, Compute Engine, BigQuery, and Secret Manager.

Autokey simplifies creating and using [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek) by automating provisioning and assignment. With Autokey, key rings, keys, and service accounts don't need to be planned and provisioned before they're needed. Instead, Autokey generates keys on demand as resources are created.

Using keys generated by Autokey can help you consistently align with industry standards and recommended practices for data security, including the HSM protection level, separation of duties, key rotation, location, and key specificity. Keys requested using Autokey function identically to other Cloud HSM keys with the same settings.

For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

Feature

Cloud KMS has two new organization policy constraints that you can use to control key version destruction. These constraints became available on November 1, 2023.

For more information, see [Control key version destruction](https://docs.cloud.google.com/kms/docs/control-key-destruction).

## April 15, 2024

Feature

Cloud KMS now supports asymmetric signing and validation using ECDSA on the Curve25519 in PureEdDSA mode, which takes raw data as input instead of hashed data.

For more information on this and other algorithms supported by Cloud KMS, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).

## April 04, 2024

Feature

Bare Metal Rack HSM is generally available for customers with specific business and technical requirements in limited regions.

Bare Metal Rack HSM is an infrastructure-as-a-service offering that lets you deploy large numbers of customer-owned hardware security modules (HSMs) in PCI-compliant facilities next to your Google Cloud workloads. This product helps to accelerate migration of your payment applications to Google Cloud.

For more information, including to compare Bare Metal Rack HSM with Bare Metal HSM, see [Bare Metal Rack HSM](https://docs.cloud.google.com/kms/docs/bare-metal-rack-hsm).

## March 20, 2024

Deprecated

Certificate bundles for verifying attestations for Cloud HSM keys are deprecated. You can no longer download certificate bundles as of March 20, 2024.

Certificate bundles have been replaced by certificate chains. To learn how to use certificate chains to verify attestations for Cloud HSM keys, see [Verifying the attestation manually](https://docs.cloud.google.com/kms/docs/attest-key#verify_chains).

## January 31, 2024

Feature

Cloud KMS is available in the following region:

  * `africa-south1`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## January 18, 2024

Feature

Bare Metal HSM is generally available for customers with specific business and technical requirements in limited regions.

Bare Metal HSM is an infrastructure-as-a-service offering that lets you deploy customer-owned hardware security modules (HSMs) in PCI-compliant facilities next to your Google Cloud workloads. This product helps to accelerate migration of your payment applications to Google Cloud.

For more information, see [Bare Metal HSM](https://docs.cloud.google.com/kms/docs/bare-metal-hsm).

## September 15, 2023

Feature

Cloud KMS is available in the following region:

  * `me-central2`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## August 22, 2023

Feature

Cloud KMS is available in the following region:

  * `europe-west10`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## May 22, 2023

Feature

The Key Usage dashboard in the Google Cloud console and the new KMS Inventory REST API are now generally available.

For more information about the Key Usage dashboard, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

For more information about the KMS Inventory REST API, see [KMS Inventory API](https://docs.cloud.google.com/kms/docs/reference/inventory/rest).

For example curl commands using the KMS Inventory REST API, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage) and [View keys by project](https://docs.cloud.google.com/kms/docs/view-keys-by-project).

## April 18, 2023

Feature

Cloud HSM resources are now available in the following regions:

  * `europe-west12`
  * `me-central1`



For information about which locations are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## March 30, 2023

Feature

Cloud KMS is available in the following region:

  * `me-central1`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## March 24, 2023

Feature

Cloud EKM now supports [coordinated external keys](https://docs.cloud.google.com/kms/docs/ekm#how-coordinated).

Coordinated external keys let you create and manage keys in a compatible external key management system from Cloud KMS over a VPC network. For more information, see [EKM key management from Cloud KMS](https://docs.cloud.google.com/kms/docs/ekm#ekm-management-mode).

Thales CipherTrust Cloud Key Manager is the first external key management partner system that is compatible with EKM key management from Cloud KMS.

## March 23, 2023

Feature

Cloud KMS is available in the following region:

  * `europe-west12`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## January 19, 2023

Feature

Cloud KMS and Cloud EKM resources are available in the `in` (India) multi-regional location. Cloud HSM resources are **not** available in this location.

For information about which [Google Cloud Locations](https://docs.cloud.google.com/about/locations) are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see [Cloud KMS Locations](https://docs.cloud.google.com/kms/docs/locations).

## December 09, 2022

Feature

The Key Usage dashboard in the Google Cloud console and the new KMS Inventory REST API are now in Preview.

For more information about the Key Usage dashboard, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage).

For more information about the KMS Inventory REST API, see [KMS Inventory API](https://docs.cloud.google.com/kms/docs/reference/inventory/rest).

For example curl commands using the KMS Inventory REST API, see [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage) and [View keys by project](https://docs.cloud.google.com/kms/docs/view-keys-by-project).

## October 31, 2022

Feature

Cloud HSM resources are now available in the following regions:

  * `europe-southwest1`
  * `europe-west9`
  * `me-west1`



For information about which locations are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## September 12, 2022

Feature

Cloud KMS is available in the following region:

  * `me-west1`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## June 29, 2022

Feature

Customers enrolled in Key Access Justifications will now see justifications listed in Cloud Audit Logs for Cloud KMS.

## June 08, 2022

Feature

Cloud EKM now supports Dataproc Metastore. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## June 07, 2022

Feature

Cloud KMS is available in the following region:

`us-south1`

For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## May 24, 2022

Feature

Cloud KMS is available in the following region:

  * `us-east5`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## May 10, 2022

Feature

Cloud KMS is available in the following region:

  * `europe-southwest1`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## May 03, 2022

Feature

Cloud KMS is available in the following region:

  * `europe-west9`



For more information, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## March 30, 2022

Feature

Two new organization policy constraints are now available in Preview to help ensure CMEK usage across an organization:

  * `constraints/gcp.restrictNonCmekServices` requires CMEK protection.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` limits which Cloud KMS keys are used for CMEK protection.



To learn more, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## March 25, 2022

Feature

Cloud EKM now supports Cloud Bigtable and Log Storage in Cloud Logging. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## March 18, 2022

Feature

Using Cloud EKM with a Virtual Private Network is now generally available. This means you can access your external key manager with a private endpoint.

See [Using Cloud EKM with VPC](https://docs.cloud.google.com/kms/docs/ekm-virtual-private-cloud) to learn more.

## February 28, 2022

Feature

Cloud HSM resources are now available in the following regions:

  * `asia1`
  * `eur3`
  * `eur4`
  * `nam3`
  * `nam4`
  * `nam6`
  * `nam9`



For information about which locations are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## February 14, 2022

Announcement

Virtru is now available as a supported Cloud EKM partner. See [Supported key managers](https://docs.cloud.google.com/kms/docs/ekm#supported_partners) to learn more.

## January 31, 2022

Feature

You can now use Cloud EKM with a Virtual Private Network (preview). This means you can access your external key manager with a private endpoint.

See [Using Cloud EKM with VPC](https://docs.cloud.google.com/kms/docs/ekm-virtual-private-cloud) to learn more.

## January 28, 2022

Feature

Cloud EKM now supports Cloud Run, Dataproc, and Vertex AI. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## January 05, 2022

Feature

Cloud HSM is now available in the [Melbourne (australia-southeast2)](https://docs.cloud.google.com/kms/docs/locations#regional:) region.

## December 23, 2021

Feature

[Asymmetric keys](https://docs.cloud.google.com/kms/docs/ekm-internet#create_asymmetric_signing_ekm_key) for Cloud EKM are now generally available (GA).

## December 07, 2021

Change

The Cloud EKM cryptographic requests quota has been increased from 10 QPS to 100 QPS. If you use quotas to determine how much you are billed, this change could increase the amount you spend on Cloud KMS. See [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#cloud_ekm_quotas) for more details.

## November 16, 2021

Feature

Cloud KMS is now available in the [Santiago (southamerica-west1)](https://docs.cloud.google.com/kms/docs/locations#regional:) region.

## November 03, 2021

Feature

You can now attest HSM keys using certificate chains via gcloud command-line tool, Cloud Console, or Cloud KMS API. See [Verifying attestations](https://docs.cloud.google.com/kms/docs/attest-key) to learn more.

## September 09, 2021

Feature

Cloud KMS now provides a library that conforms to the PKCS #11 standard, which enables working with existing applications that use the PKCS #11 API. See [Library for PKCS #11](https://docs.cloud.google.com/kms/docs/reference/pkcs11-library) to learn more.

## September 03, 2021

Feature

[Re-importing previously destroyed keys](https://docs.cloud.google.com/kms/docs/importing-a-key#re-import_a_previously_destroyed_key) is now supported in Cloud KMS.

## August 20, 2021

Feature

You can now retrieve random bytes from the random number generator in Cloud HSM. See [Generating random bytes](https://docs.cloud.google.com/kms/docs/generate-random) to learn more.

Feature

MAC keys are now supported by Cloud KMS. See [Creating and validating MAC digital signatures](https://docs.cloud.google.com/kms/docs/create-validate-mac-signatures) to learn more.

Feature

Cloud KMS now supports a configurable [variable soft deletion](https://docs.cloud.google.com/kms/docs/key-states#variable_soft_deletion) window for cryptographic keys.

## July 29, 2021

Feature

Cloud EKM now supports Artifact Registry, Logs Router in Cloud Logging, and Cloud Spanner. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## June 21, 2021

Feature

Several fields related to [verifying end-to-end data integrity](https://docs.cloud.google.com/kms/docs/data-integrity-guidelines) for cryptographic operations are generally available (GA).

## May 19, 2021

Change

The [Cloud KMS and Cloud HSM SLA](https://cloud.google.com/kms/sla) has been updated.

## March 31, 2021

Feature

Cloud EKM now supports Dataflow Appliance and Pub/Sub. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## March 24, 2021

Feature

The `europe-central2` region in Warsaw is now available. See [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations) for more details.

## February 01, 2021

Feature

Cloud EKM adds support for Dataflow shuffle and Secret Manager. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## October 28, 2020

Feature

Cloud EKM now supports Cloud SQL and GKE. For more information, see [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## July 14, 2020

Feature

Cloud HSM resources are available in the `us-west4` and `asia-southeast2` regions. Cloud KMS resources were already available in these regions.

For information about which [Cloud Locations](https://docs.cloud.google.com/about/locations) are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see the [Cloud KMS regional locations](https://docs.cloud.google.com/kms/docs/locations#regional).

## June 22, 2020

Feature

Keys hosted by [Thales](https://thalesdocs.com/dpod/services/key_management_services/ekms/ekms_setup_guide/index.html) are now supported in Cloud EKM. To learn more, see [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm).

## June 08, 2020

Feature

Cloud KMS and Cloud EKM resources are available in the `asia-southeast2` region. Cloud HSM resources are **not** available in this region.

For information about which [Cloud Locations](https://docs.cloud.google.com/about/locations) are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see the [Cloud KMS regional locations](https://docs.cloud.google.com/kms/docs/locations#regional).

## May 28, 2020

Feature

Several fields related to data integrity have been added to the Cloud KMS API, along with guidelines for using them. To learn more about maintaining data integrity when performing cryptographic operations, see [Verifying end-to-end data integrity](https://docs.cloud.google.com/kms/docs/data-integrity-guidelines).

## April 30, 2020

Feature

[Hosted Private HSM](https://docs.cloud.google.com/kms/docs/hosted-private-hsm) is generally available.

## April 20, 2020

Feature

Cloud KMS and Cloud EKM resources are available in the `us-west4` region. Cloud HSM resources are **not** available in this region.

Cloud HSM resources are available in the `global` multi-regional location.

For information about which [Cloud Locations](https://docs.cloud.google.com/about/locations) are supported by Cloud KMS, Cloud HSM, and Cloud EKM, see the [Cloud KMS regional locations](https://docs.cloud.google.com/kms/docs/locations#regional).

## April 15, 2020

Feature

[Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm) is generally available.

## March 18, 2020

Feature

[Importing keys](https://docs.cloud.google.com/kms/docs/importing-a-key) into Cloud KMS software keys is generally available (GA).

## March 05, 2020

Feature

Cloud EKM resources are now available in the `asia-northeast3` and `us-west3` [locations](https://docs.cloud.google.com/kms/docs/locations).

## February 25, 2020

Feature

Cloud KMS resources can now be created in the `us-west3` region.

Cloud HSM resources are now also available in the `us-west3` region.

Cloud EKM resources are not available in the `us-west3` region.

For information about which [Cloud Locations](https://docs.cloud.google.com/about/locations) are supported by Cloud KMS, Cloud HSM, and Cloud EKM, refer to [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations#regional).

## February 20, 2020

Feature

You can now import key material into Cloud KMS software keys. For more information, see [Key import](https://docs.cloud.google.com/kms/docs/key-import). Importing key material into Cloud HSM keys is already generally available.

## January 24, 2020

Feature

Cloud KMS resources can now be created in the `asia-northeast3` region.

Cloud HSM resources are now also available in the `asia-northeast3` region.

**Note:** Cloud EKM resources are _not available_ in the `asia-northeast3` region.

Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations). For the list of all regions supported by Cloud KMS, Cloud HSM, and Cloud EKM, see the [Cloud KMS regional locations](https://docs.cloud.google.com/kms/docs/locations#regional).

## December 17, 2019

Feature

[Cloud External Key Manager (Cloud EKM) (Beta)](https://docs.cloud.google.com/kms/docs/ekm) allows you to encrypt data stored in Google Cloud using keys stored in a supported partner external key management system. You can encrypt or decrypt data in BigQuery, Compute Engine persistent disks, or directly using the Cloud KMS API.

You can learn about [changes to the API](https://docs.cloud.google.com/kms/docs/ekm#api_changes) since the Alpha release.

## August 22, 2019

Breaking

The Cryptographic Requests quota has been increased from 600 QPM to 60,000 QPM. If you use quotas to determine how much you are billed, this change could increase the amount you end up spending on your Cloud KMS. 

If you require a smaller quota than 60,000 QPM, or you don't need a quota increase, go to the [Cloud Console Quotas page](https://console.cloud.google.com/iam-admin/quotas?service=cloudkms.googleapis.com) and set a new value for Cryptographic requests per minute. HSM specific quotas will not be increased.

## July 02, 2019

Feature

The [`gcloud beta kms import-jobs`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/import-jobs) command group was released as part of [`gcloud 253.0.0`](https://docs.cloud.google.com/sdk/docs/release-notes#25300_2019-07-02).

## July 01, 2019

Feature

Introduction of import key functionality into the Cloud KMS beta release.

**Note:** You can import only into keys with [protection level](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels) **HSM**.

The following are additions to the API definition.

### New resources

[`ImportJob`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs) has been added as a resource.

The `ImportJob` resource contains the following methods:

  * [`ImportJobs.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/create)
  * [`ImportJobs.get`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/get)
  * [`ImportJobs.getIamPolicy`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/getIamPolicy)
  * [`ImportJobs.list`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/list)
  * [`ImportJobs.setIamPolicy`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/setIamPolicy)
  * [`ImportJobs.testIamPermissions`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs/testIamPermissions)



The `ImportJob` resource contains the following enums:

  * [`ImportJobState`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#importjobstate)
  * [`ImportMethod`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#importmethod)



The `ImportJob` resource contains the following type:

  * [`WrappingPublicKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.importJobs#wrappingpublickey)



### New methods

  * [`CryptoKeyVersions.import`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/import)



### New fields

  * [`CreateCryptoKeyRequest.skip_initial_version_creation`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create#body.QUERY_PARAMETERS.skip_initial_version_creation)
  * [`CryptoKeyVersions.import_failure_reason`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.import_failure_reason)
  * [`CryptoKeyVersions.import_job`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.import_job)
  * [`CryptoKeyVersions.import_time`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.import_time)



### New enums

  * [`CryptoKeyVersionState.PENDING_IMPORT`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.PENDING_IMPORT)
  * [`CryptoKeyVersionState.IMPORT_FAILED`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.CryptoKeyVersionState.ENUM_VALUES.IMPORT_FAILED)



### New permissions

  * `cloudkms.cryptoKeyVersions.useToImport`
  * `cloudkms.importJobs.create`
  * `cloudkms.importJobs.get`
  * `cloudkms.importJobs.getIamPolicy`
  * `cloudkms.importJobs.list`
  * `cloudkms.importJobs.setIamPolicy`



For more information about Cloud KMS permissions, see [Permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

## June 28, 2019

Feature

Cloud HSM resources are now available in the following regional locations:

  * `asia-east2`
  * `europe-west6`
  * `us-west2`



For the list of all supported regions, see [Supported regions](https://docs.cloud.google.com/kms/docs/locations).

## June 27, 2019

Feature

Introduction of the Cloud KMS beta release to support filtering and sorting results from the following `list` operations.

  * [keyRings.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/list)
  * [cryptoKeys.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list)
  * [cryptoKeyVersions.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list)



For more information, see [Sorting and filtering list results](https://docs.cloud.google.com/kms/docs/sorting-and-filtering).

## June 20, 2019

Feature

Cloud HSM resources are now available in the following regional locations:

  * `asia-northeast1`
  * `asia-northeast2`



For the list of all supported regions, see [Supported regions](https://docs.cloud.google.com/kms/docs/locations).

## June 11, 2019

Change

The `gcloud kms` command group was updated as part of [gcloud 250.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#25000_2019-06-11).

  * Promoted the following commands to GA. 
    * `gcloud kms asymmetric-decrypt`.
    * `gcloud kms asymmetric-sign`.
    * `gcloud kms keys versions get-public-key`.
  * Promoted the following flags in `gcloud kms keys` command group to GA. 
    * `--attestation-file`.
    * `--default-algorithm`.
    * `--purpose`.
    * `--protection-level`.



## June 04, 2019

Feature

Cloud HSM resources are now available in the following regional locations:

  * `asia-south1`
  * `europe-north1`
  * `europe-west1`
  * `europe-west4`



For the list of all supported regions, see [Supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).

## May 13, 2019

Feature

Cloud HSM resources are now available in the `us` multi-regional location. For the list of all supported regions, see [Supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).

## April 18, 2019

Feature

Cloud KMS resources can now be created in the `asia-northeast2` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## April 02, 2019

Feature

Cloud HSM resources are now available in the `asia-southeast`1 regional location. For the list of all supported regions, see [Supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).

## March 11, 2019

Feature

Cloud KMS resources can now be created in the `europe-west6` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## February 26, 2019

Feature

`CAVIUM_V2_COMPRESSED` has been added as an enum value to [`AttestationFormat`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/KeyOperationAttestation#AttestationFormat). To learn how to verify an attestation that is in the `CAVIUM_V2_COMPRESSED` format, see [Verifying Attestations](https://docs.cloud.google.com/kms/docs/attest-key).

## December 14, 2018

Feature

Announced general availability of [asymmetric keys](https://docs.cloud.google.com/kms/docs/asymmetric-encryption) and [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) in Cloud KMS.

## December 13, 2018

Feature

Cloud HSM resources are now available in the `europe-west3` regional location. For the list of all supported regions, see [Supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).

## December 06, 2018

Feature

Cloud HSM resources are now available in the `europe-west2` regional location. For the list of all supported regions, see [Supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).

## November 12, 2018

Feature

Cloud KMS resources can now be created in the `eur4` and `nam4` dual-regions. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## October 26, 2018

Feature

Cloud KMS resources can now be created in the `asia-east2` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## October 11, 2018

Feature

New algorithms have been added:

  * RSA_SIGN_PSS_4096_SHA512
  * RSA_SIGN_PKCS1_4096_SHA512
  * RSA_DECRYPT_OAEP_4096_SHA512



For the list of all supported algorithms, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).

## September 27, 2018

Feature

Cloud HSM resources are now available in the `us-central1` regional location. For the list of all supported regions, see [Supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).

## September 05, 2018

Feature

Attestations that are downloaded via the Google Cloud Platform Console are no longer base64-encoded. This matches the raw format of the attestations downloaded via the `gcloud` command-line tool and the Cloud KMS API. The instructions for [Verifying Attestations](https://docs.cloud.google.com/kms/docs/attest-key) expect the attestation to be in raw format, not base64-encoded.

## August 20, 2018

Feature

Introduction of asymmetric keys and Cloud HSM into the Cloud KMS beta release.

Additions to the API definition:

  * New method for creating digital signatures: 
    * [CryptoKeys.asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign)
  * New method for retrieving an asymmetric key's public key: 
    * [CryptoKeyVersions.getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)
  * New method for decrypting data encoded with an asymmetric public key generated by Cloud KMS: 
    * [CryptoKeyVersions.asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt)
  * New types: 
    * [CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionAlgorithm)
    * [CryptoKeyVersionTemplate](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyVersionTemplate)
    * [CryptoKeyVersionView](https://docs.cloud.google.com/kms/docs/reference/rest/v1/CryptoKeyVersionView)
    * [ProtectionLevel](https://docs.cloud.google.com/kms/docs/reference/rest/v1/ProtectionLevel)
  * New fields: 
    * [CryptoKey.versionTemplate](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.version_template)
    * [CryptoKeyVersion.algorithm](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.algorithm)
    * [CryptoKeyVersion.attestation](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.attestation)
    * [CryptoKeyVersion.generateTime](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.generate_time)
    * [CryptoKeyVersion.protectionLevel](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions#CryptoKeyVersion.FIELDS.protection_level)
    * [LocationMetadata.hsmAvailable](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations#LocationMetadata.FIELDS.hsm_available)
  * The [CryptoKey.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list) method now contains a [versionView](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/list#body.QUERY_PARAMETERS.version_view) query parameter that lists the fields of the primary key version to include in the response.
  * The [CryptoKeyVersion.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list) method now contains a [view](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/list#body.QUERY_PARAMETERS.view) query parameter that lists the fields to include in the response.
  * The [LocationMetadata](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations#LocationMetadata) resource returned by the [Locations.get](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/get) and [Locations.list](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations/list) methods now contain an `hsm_available` field. The `hsm_available` field is a `bool` that indicates whether the location supports Hardware Security Modules (HSMs).



Feature

Cloud HSM resources are now available in the `us-east1` and `us-west1` regional locations.

## July 14, 2018

Feature

Cloud KMS resources can now be created in the `us-west2` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## June 14, 2018

Feature

Cloud KMS resources can now be created in the `europe-north1` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## April 12, 2018

Feature

Cloud KMS resources can now be created in the following regions:

  * `asia-south1`
  * `australia-southeast1`
  * `europe-west2`
  * `europe-west3`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-east4`



Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## April 11, 2018

Change

The URL of the Cloud KMS page in the Google Cloud Platform Console has been changed from https://console.cloud.google.com/iam-admin/kms to https://console.cloud.google.com/security/kms.

## April 03, 2018

Feature

The name of the [Cloud KMS](https://console.cloud.google.com/iam-admin/kms?_ga=2.253907791.-615102279.1537806205) page in the Google Cloud Platform Console has been changed from **Encryption keys** to **Cryptographic keys**.

## March 29, 2018

Feature

Cloud KMS resources can now be created in the `asia-northeast1` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## February 08, 2018

Feature

Cloud KMS resources can now be created in the `asia`, `europe`, and `us` multi-regional locations. Learn more about [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## January 31, 2018

Feature

Announced general availability of [IAM custom roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#custom_roles) for Cloud KMS.

## January 22, 2018

Feature

The `gcloud kms locations list` command now supports the `europe-west4` region.

## January 17, 2018

Feature

The Google Cloud Platform console now supports the `europe-west4` region. You can create new key rings in this region using the console, the API and the `gcloud` command-line tool. The `gcloud kms locations list` command will support this region approximately January 22, 2018. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## January 10, 2018

Feature

Cloud KMS resources can now be created in the `europe-west4` region. You can use this region to create new key rings using the API and the `gcloud` command-line tool. This region will not be viewable in the Google Cloud Platform console or returned by `gcloud kms locations list` until approximately January 17, 2018. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## October 11, 2017

Change

Promoted `keys update` from `gcloud beta kms` to `gcloud kms` as part of [gcloud 175.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#17500_2017-10-11).

## October 04, 2017

Change

The [Envelope Encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption) topic provides more information about key wrapping and envelope encryption.

## September 19, 2017

Change

Batch operations are no longer supported.

## September 06, 2017

Feature

Labels can now be applied to CryptoKeys:

  * The [`CryptoKey`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey) type now contains the [`labels`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.labels) field.
  * To learn more about this feature, see [Labeling CryptoKeys](https://docs.cloud.google.com/kms/docs/labeling-keys).



Feature

`gcloud` changes:

  * The `gcloud kms keys create` command has a new parameter, `--labels`. Use this parameter to specify labels when you create a key.
  * The output from the `gcloud kms keys list` command now contains a `LABELS` column.
  * The [`gcloud beta kms keys update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/keys/update) command is new. This command supports updating an existing key.



These changes are effective in [`gcloud` version 170.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#17000_2017-09-06).

## August 23, 2017

Feature

Cloud KMS resources can now be created in the `asia-southeast1` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## August 18, 2017

Change

Cloud KMS is now available in a larger group of countries.

## June 14, 2017

Change

Promoted `encrypt` and `decrypt` commands from `gcloud beta kms` to `gcloud kms` as part of [gcloud 159.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#15900_2017-06-14).

## June 07, 2017

Deprecated

API version v1beta1 has been turned off. Please use v1 API endpoint.

Change

As part of [gcloud 158.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#15800_2017-06-07), when using `gcloud` to update IAM policies, data access logs can be enabled for key rings and keys, in addition to projects which were already supported.

  * [`gcloud kms keyrings set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keyrings/set-iam-policy)
  * [`gcloud kms keys set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/set-iam-policy)



## May 31, 2017

Feature

Added `encrypt` and `decrypt` commands to `gcloud beta kms` as part of [gcloud 157.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#15700_2017-05-31).

  * [Added examples](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) for using `gcloud beta kms encrypt` and `gcloud beta kms decrypt`.



## May 02, 2017

Feature

Data Access audit logs can now be self-enabled for Cloud KMS. For more information, see [Cloud Audit Logging documentation](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).

  * [Updated documentation](https://docs.cloud.google.com/kms/docs/logging) on logs types in Cloud KMS.



## April 17, 2017

Feature

Cloud KMS resources can now be created in the `us-west1` region. Learn more about [Cloud Locations](https://docs.cloud.google.com/about/locations).

## March 22, 2017

Change

Promoted `gcloud beta kms` commands to `gcloud kms` as part of [gcloud 148.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#14800_2017-03-22).

## March 15, 2017

Change

Renamed `cryptokey` to `key` as part of [gcloud 147.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#14700_2017-03-15).

Renamed `gcloud kms cryptokeys` as `gcloud kms keys`. Renamed the `--cryptokey` flag as `--key`. Deprecated the `cryptokey` variants.

## March 08, 2017

Feature

Launch of Cloud KMS to **General Availability**.

  * Updated client libraries and code samples in C#, Go, Java, Node.js, PHP, Python, and Ruby.
  * [New Secret Management documentation](https://docs.cloud.google.com/kms/docs/secret-management) that explains how to protect secrets using Cloud KMS.
  * Added a [Service Level Agreement (SLA)](https://cloud.google.com/kms/sla).



Change

API version from v1beta1 to v1.

  * The v1beta1 API is deprecated and will be turned down no sooner than June 7, 2017.
  * To start using the v1 API, follow the process to [install the client library](https://docs.cloud.google.com/kms/docs/reference/libraries#installing_the_client_library) for your preferred language. Other than the API version, your code shouldn't need any other changes.



## January 11, 2017

Feature

Launch of Cloud KMS to **Beta**. Use Cloud KMS to create, use, rotate, automatically rotate, and destroy symmetric AES256 encryption keys. Cloud KMS is [accessible via](https://docs.cloud.google.com/kms/docs/accessing-the-api)

  * REST API
  * Google APIs Client Libraries in go, python, and java
  * Cloud Console user interface



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
