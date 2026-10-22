---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-ioc/
title: Collect Palo Alto Networks IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:34.216701+00:00
---

# Collect Palo Alto Networks IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Palo Alto Networks IOC logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api). 

This document explains how to ingest Palo Alto Networks indicators of compromise (IOCs) to Google Security Operations using STIX over TAXII. The `stix_taxii` ingestion script (a Cloud Run function) pulls indicators from a Palo Alto TAXII 2.1 server on a schedule and sends them to Google SecOps using the `STIX` log type.

**Note:** The legacy AutoFocus method (the `PAN_IOC` log type and the `autofocus.paloaltonetworks.com` custom threat feed) is deprecated. Palo Alto AutoFocus reached end-of-life on 30 September 2025, so the AutoFocus feed no longer has a live data source. Use the STIX/TAXII method described in this guide instead.

Palo Alto Networks exposes IOCs as a STIX 2.1 feed over TAXII from Cortex XSOAR or XSIAM Threat Intelligence Management (TIM). The `STIX` parser in Google SecOps maps the common indicator types (IPv4 addresses, domains, URLs, file hashes, and email addresses) to the UDM.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance, and the Google SecOps ingestion authentication file (the service account JSON) and Customer ID.
  * A Google Cloud project with billing enabled and permissions to create service accounts, Secret Manager secrets, Cloud Run functions, and Cloud Scheduler jobs.
  * **Palo Alto Cortex XSOAR** or **XSIAM** with a **Threat Intelligence Management (TIM)** license, and privileged access to configure integrations.

**Note:** The current Unit 42 Intelligence feed is delivered as a Palo-managed integration inside Cortex XSOAR or XSIAM and does not expose a standalone TAXII endpoint. To ingest Unit 42 indicators or your own aggregated indicators, publish them from Cortex TIM using the TAXII2 Server integration described in the next section.



## Set up the Palo Alto TAXII 2.1 feed in Cortex TIM

The **TAXII2 Server** integration publishes your Cortex XSOAR or XSIAM indicators as an outbound TAXII 2.1 feed that the ingestion script pulls.

  1. In Cortex XSOAR or XSIAM, install the **TAXII Server** content pack from **Settings & Info > Settings > Integrations > Marketplace**.
  2. Go to **Settings > Integrations > Instances**, search for **TAXII2 Server** , and click **Add instance**.
  3. Provide the following configuration details: 
     * **Name** : Enter a name for the instance (for example, `SecOps-TAXII`).
     * **Long Running Instance** : Enable this option.
     * **TAXII2 Server version** : Select **2.1**.
     * **Credentials** : Set the username and password that the ingestion script uses for HTTP Basic authentication.
  4. In the **Collection JSON** field, paste the following. It publishes one collection named `SecOpsIOCs` that contains the indicator types the `STIX` parser supports:
         
         {
             "SecOpsIOCs": {
                 "query": "type:IP or type:Domain or type:URL or type:File or type:Email",
                 "description": "Indicators exported to Google SecOps"
             }
         }
         

  5. Click **Save & exit** and enable the instance. Confirm that the instance status shows as running.

  6. In the Google SecOps playground or the integration's command bar, run the following commands and save the output:
         
         !taxii-server-info
         !taxii-server-list-collections
         

  7. From the command output, save these values for the deployment step:

     * **Discovery URL** : The API root URL returned by `!taxii-server-info` (for example, `https://ext-TENANT.crtx.REGION.paloaltonetworks.com/xsoar/instance/execute/SecOps-TAXII/threatintel/`).
     * **Collection name** : `SecOpsIOCs`.
     * **Username** and **Password** : The Basic authentication credentials you set.



## Enable required Google Cloud APIs

  1. In the Google Cloud console, open **Cloud Shell** and run:
         
         gcloud services enable \
             cloudfunctions.googleapis.com \
             cloudbuild.googleapis.com \
             cloudscheduler.googleapis.com \
             secretmanager.googleapis.com
         




## Store credentials in Secret Manager

The script reads the Google SecOps service account JSON and the TAXII password from Secret Manager.

  1. Create the Google SecOps ingestion service account secret from your ingestion authentication file:
         
         gcloud secrets create secops-ingestion-sa --data-file=./ingestion-auth.json
         

  2. Create the TAXII password secret:
         
         printf '%s' 'YOUR_TAXII_PASSWORD' | gcloud secrets create taxii-password --data-file=-
         

  3. Save both resource names in the form `projects/PROJECT_ID/secrets/SECRET_NAME/versions/latest`. You use them in `.env.yml`.




## Create a service account for the function

  1. Create a runtime service account for the Cloud Run function:
         
         gcloud iam service-accounts create stix-taxii-sa \
             --display-name="STIX/TAXII ingestion function"
         

  2. Grant it access to the two secrets:
         
         gcloud secrets add-iam-policy-binding secops-ingestion-sa \
             --member="serviceAccount:stix-taxii-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/secretmanager.secretAccessor"
         gcloud secrets add-iam-policy-binding taxii-password \
             --member="serviceAccount:stix-taxii-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/secretmanager.secretAccessor"
         




## Deploy the ingestion script

The `stix_taxii` ingestion script is a Cloud Run function that pulls indicators from the TAXII server and streams them to Google SecOps using the Ingestion API. It always ingests using the `STIX` log type.

  1. In **Cloud Shell** , clone the ingestion scripts repository:
         
         git clone https://github.com/chronicle/ingestion-scripts.git
         cp -r ingestion-scripts/common ingestion-scripts/stix_taxii/common
         cd ingestion-scripts/stix_taxii
         

  2. Create a file named `.env.yml` with the following contents. Replace the placeholder values with the ones you saved earlier:
         
         CHRONICLE_CUSTOMER_ID: "YOUR_CUSTOMER_ID"
         CHRONICLE_REGION: "us"
         CHRONICLE_SERVICE_ACCOUNT: "projects/PROJECT_ID/secrets/secops-ingestion-sa/versions/latest"
         TAXII_VERSION: "2.1"
         TAXII_DISCOVERY_URL: "https://ext-TENANT.crtx.REGION.paloaltonetworks.com/xsoar/instance/execute/SecOps-TAXII/threatintel/"
         TAXII_COLLECTION_NAMES: "SecOpsIOCs"
         TAXII_USERNAME: "YOUR_TAXII_USERNAME"
         TAXII_PASSWORD_SECRET_PATH: "projects/PROJECT_ID/secrets/taxii-password/versions/latest"
         POLL_INTERVAL: "60"
         

**Note:** `CHRONICLE_SERVICE_ACCOUNT` and `TAXII_PASSWORD_SECRET_PATH` are Secret Manager resource names, not the raw values. Leave `TAXII_COLLECTION_NAMES` empty to pull all collections.
  3. Deploy the function:
         
         gcloud functions deploy stix-taxii-ingestion \
             --gen2 \
             --entry-point main \
             --trigger-http \
             --runtime python312 \
             --region us-central1 \
             --service-account stix-taxii-sa@PROJECT_ID.iam.gserviceaccount.com \
             --timeout 540 \
             --memory 512MB \
             --no-allow-unauthenticated \
             --env-vars-file .env.yml
         

  4. Save the function's trigger URL from the deployment output (for example, `https://us-central1-PROJECT_ID.cloudfunctions.net/stix-taxii-ingestion`).




## Schedule the function with Cloud Scheduler

  1. Grant the service account permission to invoke the function:
         
         gcloud functions add-invoker-policy-binding stix-taxii-ingestion \
             --region=us-central1 \
             --member="serviceAccount:stix-taxii-sa@PROJECT_ID.iam.gserviceaccount.com"
         

  2. Create a scheduler job that calls the function every hour (match the frequency to `POLL_INTERVAL`):
         
         gcloud scheduler jobs create http stix-taxii-scheduler \
             --location=us-central1 \
             --schedule="0 */1 * * *" \
             --uri="FUNCTION_TRIGGER_URL" \
             --http-method=POST \
             --oidc-service-account-email="stix-taxii-sa@PROJECT_ID.iam.gserviceaccount.com" \
             --oidc-token-audience="FUNCTION_TRIGGER_URL"
         




## Verify the deployment

  1. Trigger an initial run:
         
         gcloud scheduler jobs run stix-taxii-scheduler --location=us-central1
         

  2. Review the function logs:
         
         gcloud functions logs read stix-taxii-ingestion --region=us-central1 --gen2 --limit=50
         

  3. In Google SecOps, search for events with the `STIX` log type to confirm that the indicators are ingested.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`observable.object.properties.type` | `categorization` | Directly mapped  
`type` | `categorization` | Directly mapped  
`x_ctix_confidence_score` | `confidence_score` | Renamed/mapped  
`name` | `domain_and_ports.domain` | Directly mapped  
`observable.object.properties.value` | `domain_and_ports.domain` | Directly mapped  
`value` | `domain_and_ports.domain` | Directly mapped  
`type` | `feed_name` | Mapped: `"ipv4","ipv4-addr", "scan_ip", "mal_ip"` → `STIX-IOC`, `"phish_domain", "domain", "...  
`src_ip` | `ip_and_ports.ip_address` | Directly mapped  
`value` | `ip_and_ports.ip_address` | Directly mapped  
`src_port` | `ip_and_ports.ports` | Merged  
`type` | `ip_and_ports.ports` | Mapped: `"ipv4","ipv4-addr", "scan_ip", "mal_ip"` → `src_port`, `ipv4-addr` → `src_port`  
`created` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`modified` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`valid_from` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`valid_until` | `metadata.event_timestamp` | Parsed as `ISO8601`  
N/A | `feed_name` | Constant: `STIX-IOC`  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stix-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
