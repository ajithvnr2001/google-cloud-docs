---
url: https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops/
title: Configure CMEK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:46.224950+00:00
---

# Configure CMEK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/cmek_for_secops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure CMEK

Supported in:

Google SecOps 

This document outlines how to configure customer-managed encryption keys (CMEK) for Google Security Operations. Google SecOps encrypts customer data at rest by default using [Google default encryption](https://docs.cloud.google.com/kms/docs/cmek#default-encryption) without any additional actions from you. However, for more control over encryption keys or when mandated by an organization, CMEK is available for Google SecOps instances.

CMEKs are encryption keys that you own, manage, and store in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service). Using CMEKs provides full control over encryption keys, including managing their lifecycle, rotation, and access policies. When you configure CMEK, the service automatically encrypts all data using the specified key. Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek).

**Note:** Certain transient system-generated temporary files may briefly utilize Google's standard platform encryption rather than your CMEK during data processing operations.

CMEK is available in all regions where Google SecOps is supported. For a complete list of regions supported by Google SecOps, see [SecOps Services Locations Page](https://cloud.google.com/terms/secops/data-residency).

**Important:** `eu` and `us` are multi-regions. When you select `eu (multiple regions in European Union)`, you must additionally configure a CMEK in the `europe-west1` region. When you select `us (multiple regions in United States)`, you must additionally configure a CMEK in the `us-central1` region. **Note:** `eu and us` are **Multi-region** location type, where the [Spanner](https://cloud.google.com/spanner) database is spread across multiple regions. `europe-west1` and `us-central1` are (single-region) **Region** location type. Google SecOps uses Google Cloud services, and some of them support only a single region. Because CMEKs have a strong colocation requirement and the Spanner database is spread across multiple regions, Google SecOps and Google Cloud services require two different CMEK locations.

## Use CMEKs in Cloud KMS

To control your encryption keys, you can use CMEKs in Cloud KMS with CMEK-integrated services, including Google SecOps, as follows:

  * You manage and store these keys in Cloud KMS.
  * Data in the Google SecOps Data Lake is encrypted at rest.
  * When you configure your Google SecOps instance with a CMEK, it uses the selected Cloud KMS key to encrypt data at rest within the Data Lake.
  * Using CMEK with Cloud KMS may incur additional costs, depending on your usage patterns.



Learn more about [Cloud KMS pricing](https://cloud.google.com/kms/pricing).

## Feature availability with Cloud KMS

The following table summarizes the availability of key features with Cloud KMS for Google SecOps customers:

Feature | Cloud KMS State | Roadmap / ETA | Notes/Details  
---|---|---|---  
Data Tables | Cloud KMS compliant | Available |   
Gemini in Google SecOps | Cloud KMS compliant | Available | Includes: Generate search queries, Generate a YARA-L rule using Gemini, Assistance with threat intelligence and security questions, Get documentation summaries, Create and edit a playbook, Use the Gemini case summary widget, and Use the Triage and Investigation Agent to investigate alerts. Excludes: SecOps Lab. For new AI features, Cloud KMS timelines will be provided on a case-by-case basis.  
BigQuery Exports | Standard / Enterprise: BYOBQ → Cloud KMS compliant | GA | For Enterprise Plus (Advanced BigQuery Export): This moved from Private Preview to Public Preview on July 1, 2026, and Cloud Key Management Service (CMEK) compliance is already live in Public Preview. For Cloud KMS and VPC Service Controls users, direct access to the Google managed project for exports can be blocked (breaking Exports feature) or this direct-access path would stay non-compliant.  
Looker Dashboards | Won't be Cloud KMS compliant | Deprecated in favor of built-in Dashboards | Built-in dashboards will be the main dashboarding capability moving forward and are already Cloud KMS compliant.  
Built-in Dashboard | Email with attachment - Not end-to-end Cloud KMS compliant | Public Preview | This option is less secure because the attachment cannot be controlled by Google SecOps once received by email servers and clients.  
Built-in Dashboard | Email with Cloud Storage bucket link for the report - Cloud KMS compliant | Public Preview | This option is Cloud KMS compliant as the report will be stored in Cloud Storage with Cloud KMS encryption.  
Data Taps | Excluded from services (will no longer be considered for GA) | Not proceeding to GA | When enabling Cloud KMS and VPC Service Controls support for all Google SecOps services, DataTap will be excluded.  
  
## Enable CMEK

**Note:** You can enable CMEKs only on a new Google SecOps instance, not on an existing one.

The following steps outline the high-level process to onboard CMEK with Google SecOps:

  1. [Configure a Google Cloud project for Google SecOps](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project): Accept the provisioning invitation to begin. Our expert Google SecOps team will handle the specialized configuration and integration. 
  2. [Create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key) in the region where you plan to host your instance.
  3. [Create a new Google SecOps instance](https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud) and select the CMEK key you created in Step 2. You'll be prompted to grant Google SecOps access to this key during instance creation.
  4. Optional: Set a [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) schedule for each key. Google recommends this security practice to minimize the impact of potential key compromise.



Once you've completed onboarding, you no longer need to provide a key using API or UI for that instance.

## Key management

Google recommends that you manage your keys using Cloud KMS. Google SecOps can't detect or act on any key changes until they're propagated by Cloud KMS. 

Google SecOps supports two types of key management:

  * [Create a Cloud KMS Key](https://docs.cloud.google.com/kms/docs/create-key): this is what Google recommends.
  * [Use the Cloud External Key Manager (Cloud EKM))](https://docs.cloud.google.com/kms/docs/ekm): using Cloud EKM keys may affect availability due to reliance on external systems.



### Manage key rotation

**Warning:** Confirm your [SOAR instance is migrated](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp#check-migration) to Google.com (Stage 1) before you rotate the key, otherwise disablement or destruction of the previous CMEK key can lead to irrecoverable data-loss. If your SOAR instance is not yet migrated to Google.com, contact your customer representative. After a key is rotated, wait for two weeks after the rotation begins before you disable or destroy the previous CMEK.

You must destroy the key before deleting it as follows: 

  1. Disable the key or key version. This step is usually optional, but some organization policies require the key to be disabled prior to destruction.
  2. Destroy the key version.
  3. Delete the key.



### Data access and permanent data loss

**Warning:** Don't disable keys that are in active use. Disabling keys that are in active use can lead to permanent data loss.

Google recommends that you monitor logs to detect keys that have become unavailable while there's still time to prevent data loss.

After Google SecOps loses access to data, the data is deleted after 30 days.

Google SecOps can lose access to data due to an intentional action of a user (for example, key revocation) or an unintentional action (for example, an EKM connectivity drop). This means that Google SecOps can't read, write, or update existing data, and it can't ingest, store, or process any new data.

If Google SecOps regains access to data (for example, when you re-enable the key), Google SecOps automatically starts ingesting and processing new data. However, it may take up to two weeks for the system to fully resume these operations.

## CMEK organization policy constraints

To enforce CMEK usage for Google SecOps, you can apply the following organization policy constraints at the organization, folder, or project level:

  * `constraints/gcp.restrictNonCmekServices`: Requires services to use CMEK. If you enforce `constraints/gcp.restrictNonCmekServices` on an organization and list Google SecOps as a restricted service, then you must select a CMEK key when you create your Google SecOps instance.

**Important:** If you enforce this constraint with Google SecOps as a restricted service, but don't provide a CMEK when creating an instance, then Google SecOps won't be provisioned.
  * `constraints/gcp.restrictCmekCryptoKeyProjects`: Requires that the CMEK key for Google SecOps come from a specific project or set of projects.




If you enforce both constraints on the organization that would contain your Google SecOps instance, then you _must_ enable CMEK using a key from a project that you specify when applying the organization policies.

For information about how organization policies are evaluated across the Google Cloud resource hierarchy (organizations, folders, and projects), see [Understanding hierarchy evaluation](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-hierarchy).

For general information about using CMEK organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
