---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-vulnerabilities/
title: Collect Armis Vulnerabilities logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:15.784159+00:00
---

# Collect Armis Vulnerabilities logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-vulnerabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Armis Vulnerabilities logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Armis Vulnerabilities logs to Google Security Operations using Google Cloud Functions. The parser transforms raw JSON formatted security vulnerability logs into a structured format conforming to the Google SecOps UDM. It extracts various fields from the raw log, maps them to corresponding UDM fields, performs data type conversions, and structures the output for ingestion into the Google SecOps platform. 

## Before you begin

Make sure you have the following prerequisites:

  * Google SecOps instance with customer ID and service account credentials
  * Privileged access to Armis Centrix platform
  * Armis API Secret Key and Server URL
  * Access to Google Cloud with permissions to create Cloud Functions, Secret Manager secrets, and Cloud Scheduler jobs
  * Armis Asset Vulnerability Management (AVM) license or module access



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **customer ID** from the **Organization Details** section.



## Get Google SecOps service account credentials

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File** (service account JSON file).
  4. Save the file securely as you will need to upload it to Google Secret Manager.



## Get Armis API Secret Key

  1. Sign in to the **Armis Centrix** platform.
  2. Go to **Settings > API Management**.
  3. Click **Create** if you need to generate a new API secret key.
  4. Click **Show** to view the secret key.
  5. Copy and save the secret key securely.

**Note:** You will need this key to configure the Cloud Function environment variables.

## Configure Google Secret Manager

This section guides you through using **Google Secret Manager** to securely store the service account key required for the integration.

### Add the Google SecOps service account secret

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/).
  2. Go to **Security > Secret Manager**.
  3. Click **Create Secret**.
  4. Provide the following configuration details: 
     * **Name** : Enter a name for the secret (for example, `secops-service-account`).
     * **Secret value** : Upload the Google SecOps service account JSON file you downloaded earlier, or paste its contents directly.
  5. Click **Create Secret**.
  6. **Copy** the **resource ID** of the created secret in the following format: 
         
         projects/{project_id}/secrets/{secret_id}/versions/{version_id}
         




### Add the Armis API Secret Key secret

  1. In **Secret Manager** , click **Create Secret**.
  2. Provide the following configuration details: 
     * **Name** : Enter a name for the secret (for example, `armis-api-secret`).
     * **Secret value** : Paste the Armis API Secret Key you obtained earlier.
  3. Click **Create Secret**.
  4. **Copy** the **resource ID** of the created secret in the following format: 
         
         projects/{project_id}/secrets/{secret_id}/versions/{version_id}`
         




## Download and prepare the ingestion script

  1. Access the official Google SecOps ingestion scripts repository at https://github.com/chronicle/ingestion-scripts.
  2. Download the contents of the **armis** directory from the repository.
  3. Download the **common** directory from the repository (required dependency).
  4. Create a new directory for the Cloud Function deployment on your local machine.
  5. Copy the contents of both the **armis** and **common** directories into your deployment directory.

**Note:** The **armis** directory contains the main ingestion script (`main.py`) and configuration template (`.env.yml`). The **common** directory provides shared utility functions required by the ingestion script.

## Configure environment variables

  1. Open the `.env.yml` file in a text editor.
  2. Edit the file with the following configuration:
         
         CHRONICLE_CUSTOMER_ID: <YOUR_CUSTOMER_ID>
         CHRONICLE_REGION: "us"
         CHRONICLE_SERVICE_ACCOUNT: projects/{project_id}/secrets/{chronicle-secret-id}/versions/{version_id}
         CHRONICLE_NAMESPACE: <YOUR_NAMESPACE>
         POLL_INTERVAL: "10"
         ARMIS_SERVER_URL: https://<your-armis-instance>.armis.com
         ARMIS_API_SECRET_KEY: projects/{project_id}/secrets/{armis-secret-id}/versions/{version_id}
         HTTPS_PROXY: 
         CHRONICLE_DATA_TYPE: ARMIS_VULNERABILITIES
         

     * Replace the following values:

       * `<YOUR_CUSTOMER_ID>`: Your Google SecOps customer ID
       * `projects/{project_id}/secrets/{chronicle-secret-id}/versions/{version_id}`: The full resource ID path of your Google SecOps service account secret from Secret Manager
       * `<YOUR_NAMESPACE>`: Optional namespace for Google Security Operations logs (for example, `armis-vulnerabilities`)
       * `<your-armis-instance>`: Your Armis tenant subdomain (for example, if your URL is https://company.armis.com, use `company`)
       * `projects/{project_id}/secrets/{armis-secret-id}/versions/{version_id}`: The full resource ID path of your Armis API secret from Secret Manager

**Note:** The poll interval should match the Cloud Scheduler frequency to avoid data loss or duplication.

## Deploy the Cloud Function

### Deploy using Cloud Function Gen2 (recommended)

  1. Open **Cloud Shell** or your local terminal with gcloud CLI installed.
  2. Navigate to the directory containing the ingestion script files.
  3. Run the following command:
         
         gcloud functions deploy armis-vulnerabilities-ingestion \
           --gen2 \
           --entry-point main \
           --trigger-http \
           --runtime python39 \
           --env-vars-file .env.yml \
           --memory 512MB \
           --timeout 3600s \
           --region us-central1
         




### Deploy using Cloud Function Gen1 (Alternative)

  * Run the following command:
        
        gcloud functions deploy armis-vulnerabilities-ingestion \
          --entry-point main \
          --trigger-http \
          --runtime python39 \
          --env-vars-file .env.yml \
          --memory 512MB \
          --timeout 540s \
          --region us-central1
        


**Note:** Gen2 functions support longer execution times (up to 60 minutes) compared to Gen1 (maximum 9 minutes). For large vulnerability datasets, Gen2 is recommended.

## Create a Cloud Scheduler job

  1. In the Google Cloud console, go to **Cloud Scheduler**.
  2. Click **Create Job**.
  3. Provide the following configuration details: 
     * **Name** : Enter a name for the job (for example, `armis-vulnerabilities-scheduler`).
     * **Region** : Select the same region as your Cloud Function (for example, `us-central1`).
     * **Frequency** : Enter the schedule using cron syntax (for example, `*/10 * * * *` for every 10 minutes).
     * **Timezone** : Select your preferred timezone (for example, UTC).
  4. Click **Continue**.
  5. Select **HTTP** as the target type.
  6. Provide the following configuration details: 
     * **URL** : In the Cloud Functions console, go to your function's **TRIGGER** tab and copy the trigger URL. Paste it here.
     * **HTTP method** : Select **POST**.
  7. Click **Auth header > Add OIDC token**.
  8. Select the **Service account** used by the Cloud Function.
  9. Click **Create**.

**Note:** The Cloud Scheduler uses the selected service account's OIDC token to authenticate and invoke the HTTP Cloud Function. Ensure the service account has the **Cloud Functions Invoker** role.**Note:** The scheduler frequency must match the `POLL_INTERVAL` value in your `.env.yml` file to prevent data loss or duplication.

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
affectedDevicesCount | read_only_udm.security_result.detection_fields.value | Direct mapping, converted to string.  
attackComplexity | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
attackVector | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
availabilityImpact | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
avmRating | read_only_udm.security_result.detection_fields.value | Direct mapping.  
botnets | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Concatenated into a single string if multiple botnets exist.  
cisaDueDate | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
collection_time.nanos | read_only_udm.metadata.event_timestamp.nanos | Direct mapping.  
collection_time.seconds | read_only_udm.metadata.event_timestamp.seconds | Direct mapping.  
commonName | read_only_udm.extensions.vulns.vulnerabilities.name | Direct mapping.  
confidentialityImpact | read_only_udm.security_result.detection_fields.value | Direct mapping.  
cveUid | read_only_udm.extensions.vulns.vulnerabilities.cve_id | Direct mapping.  
cvssScore | read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score | Direct mapping, converted to float.  
description | read_only_udm.metadata.description | Direct mapping.  
epssPercentile | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping, converted to string.  
epssScore | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping, converted to string.  
exploitabilityScore | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping, converted to string.  
firstReferencePublishDate | read_only_udm.extensions.vulns.vulnerabilities.first_found | Parsed to timestamp, handles formats with and without milliseconds.  
firstWeaponizedReferencePublishDate | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
hasRansomware | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping, converted to string.  
id | read_only_udm.metadata.product_log_id | Direct mapping.  
impactScore | read_only_udm.security_result.detection_fields.value | Direct mapping, converted to string.  
integrityImpact | read_only_udm.security_result.detection_fields.value | Direct mapping.  
isWeaponized | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping, converted to string.  
latestExploitUpdate | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
numOfExploits | read_only_udm.security_result.detection_fields.value | Direct mapping, converted to string.  
numberOfThreatActors | read_only_udm.security_result.detection_fields.value | Direct mapping, converted to string.  
orgPriorityManualChangeReason | read_only_udm.security_result.detection_fields.value | Direct mapping.  
orgPriorityManualChangedBy | read_only_udm.principal.user.userid | Direct mapping.  
orgPriorityManualUpdateTime | read_only_udm.principal.labels.value | Direct mapping.  
privilegesRequired | read_only_udm.security_result.detection_fields.value | Direct mapping.  
publishedDate | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
reportedByGoogleZeroDays | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping, converted to string.  
scope | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
severity | read_only_udm.extensions.vulns.vulnerabilities.severity | Mapped to CRITICAL, HIGH, MEDIUM, LOW based on value, original value also mapped to severity_details.  
status | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Direct mapping.  
threatTags | read_only_udm.extensions.vulns.vulnerabilities.about.labels.value | Concatenated into a single string if multiple threat tags exist.  
userInteraction | read_only_udm.about.labels.value | Direct mapping.  
vulnerabilities_matches | read_only_udm.metadata.url_back_to_product | Direct mapping.  
| read_only_udm.metadata.event_type | Set to "GENERIC_EVENT".  
| read_only_udm.metadata.product_name | Set to "ARMIS".  
| read_only_udm.metadata.vendor_name | Set to "ARMIS".  
| read_only_udm.metadata.log_type | Set to "ARMIS_VULNERABILITIES".  
| read_only_udm.extensions.vulns.vulnerabilities.severity_details | "severity" field value is mapped to this field  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/armis-vulnerabilities-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
