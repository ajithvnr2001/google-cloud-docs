---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc/
title: Collect Crowdstrike IOC logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:20.769169+00:00
---

# Collect Crowdstrike IOC logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Crowdstrike IOC logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect CrowdStrike IOC logs using the CrowdStrike Chronicle Intel Bridge, a Docker container that forwards threat intelligence indicators from CrowdStrike Falcon Intelligence to Google Security Operations.

CrowdStrike Falcon Intelligence provides threat intelligence indicators, including domains, IP addresses, file hashes, URLs, email addresses, file paths, file names, and mutex names. The Chronicle Intel Bridge polls the CrowdStrike Intel API and forwards these indicators to Google Security Operations for threat detection and analysis.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the CrowdStrike Falcon Console with permissions to create API clients
  * CrowdStrike Falcon Intelligence subscription
  * Docker installed on a system that can run continuously to poll CrowdStrike and forward indicators
  * All systems in the deployment architecture are configured in the UTC time zone



## Get Google SecOps credentials

### Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



### Download Google SecOps service account file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Click **Download Ingestion Authentication File**.
  4. Save the JSON file to a secure location on the system where you will run the Docker container (for example, `/path/to/service-account.json`).



## Configure CrowdStrike Falcon API access

To enable the Chronicle Intel Bridge to retrieve indicators, you need to create an API client with read permissions for Falcon Intelligence Indicators.

### Create API client

  1. Sign in to the **CrowdStrike Falcon Console**.
  2. Go to **Support and resources > Resources and tools > API Clients and Keys**.
  3. Click **Add new API client**.
  4. Provide the following configuration details: 
     * **Client name** : Enter a descriptive name (for example, `Chronicle Intel Bridge`).
     * **Description** : Optional: Enter `Integration with Google Chronicle for threat intelligence indicators`.
  5. In the **API scopes** section, select the **Read** checkbox next to **Indicators (Falcon Intelligence)**.
  6. Click **Create**.



### Record API credentials

  * After creating the API client, a dialog displays your credentials:

    * **Client ID** : Your unique client identifier (for example, `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`)
    * **Client Secret** : Your API secret key
    * **Base URL** : The fully qualified domain name for your region (for example, `api.us-2.crowdstrike.com`)
**Important:** Copy and save the client secret immediately. It cannot be retrieved after closing this dialog.**Note:** Your Base URL varies depending on your CrowdStrike cloud region. Use the correct base URL displayed in the dialog.



## Regional endpoints

CrowdStrike Falcon uses different API endpoints based on your cloud region:

Region | Base URL | Console URL  
---|---|---  
**US-1** | `api.crowdstrike.com` | `https://falcon.crowdstrike.com`  
**US-2** | `api.us-2.crowdstrike.com` | `https://falcon.us-2.crowdstrike.com`  
**EU-1** | `api.eu-1.crowdstrike.com` | `https://falcon.eu-1.crowdstrike.com`  
**US-GOV-1** | `api.laggar.gcw.crowdstrike.com` | `https://falcon.laggar.gcw.crowdstrike.com`  
**US-GOV-2** | `api.us-gov-2.crowdstrike.com` | `https://falcon.us-gov-2.crowdstrike.com`  
  
Use the base URL that corresponds to your CrowdStrike Falcon instance region. The region code (for example, `us-1`, `us-2`, `eu-1`) is used in the Docker configuration.

## Deploy the CrowdStrike Chronicle Intel Bridge

The Chronicle Intel Bridge is a Docker container that runs continuously to poll CrowdStrike Falcon Intelligence for indicators and forward them to Google Security Operations.

### Set environment variables

  1. Before running the Docker container, set the following environment variables with the credentials you collected:
         
         export FALCON_CLIENT_ID="your-client-id"
         export FALCON_CLIENT_SECRET="your-client-secret"
         export FALCON_CLOUD_REGION="your-cloud-region"
         export CHRONICLE_CUSTOMER_ID="your-customer-id"
         export CHRONICLE_REGION="your-chronicle-region"
         

  2. Replace the placeholder values:

     * `your-client-id`: The Client ID from the CrowdStrike API client
     * `your-client-secret`: The Client Secret from the CrowdStrike API client
     * `your-cloud-region`: Your CrowdStrike cloud region (for example, `us-1`, `us-2`, `eu-1`, `us-gov-1`, `us-gov-2`)
     * `your-customer-id`: Your Google SecOps Customer ID
     * `your-chronicle-region`: Your Google SecOps region (see Chronicle region configuration below)



### Chronicle region configuration

The `CHRONICLE_REGION` environment variable specifies which Google SecOps regional endpoint to use. The following values are supported:

  * **Legacy region codes:**

    * `US` (default if not specified)
    * `EU`
    * `UK`
    * `IL`
    * `AU`
    * `SG`
  * **Google Cloud region codes:**

    * `EUROPE`
    * `EUROPE-WEST2`
    * `EUROPE-WEST3`
    * `EUROPE-WEST6`
    * `EUROPE-WEST9`
    * `EUROPE-WEST12`
    * `ME-WEST1`
    * `ME-CENTRAL1`
    * `ME-CENTRAL2`
    * `ASIA-SOUTH1`
    * `ASIA-SOUTHEAST1`
    * `ASIA-NORTHEAST1`
    * `AUSTRALIA-SOUTHEAST1`
    * `SOUTHAMERICA-EAST1`
    * `NORTHAMERICA-NORTHEAST2`
**Note:** Region codes are case-insensitive. If not specified or if an unrecognized value is provided, it defaults to the US multi-region endpoint.



### Run the Docker container

Choose one of the following deployment methods:

  * **Interactive mode (foreground):**

Use this mode for testing and troubleshooting:
        
        docker run -it --rm \
          --name chronicle-intel-bridge \
          -e FALCON_CLIENT_ID="$FALCON_CLIENT_ID" \
          -e FALCON_CLIENT_SECRET="$FALCON_CLIENT_SECRET" \
          -e FALCON_CLOUD_REGION="$FALCON_CLOUD_REGION" \
          -e CHRONICLE_CUSTOMER_ID="$CHRONICLE_CUSTOMER_ID" \
          -e CHRONICLE_REGION="$CHRONICLE_REGION" \
          -e GOOGLE_SERVICE_ACCOUNT_FILE=/gcloud/sa.json \
          -v /path/to/your/service-account.json:/gcloud/sa.json:ro \
          quay.io/crowdstrike/chronicle-intel-bridge:latest
        

  * **Detached mode (background with restart policy):**

Use this mode for production deployment:
        
        docker run -d --restart unless-stopped \
          --name chronicle-intel-bridge \
          -e FALCON_CLIENT_ID="$FALCON_CLIENT_ID" \
          -e FALCON_CLIENT_SECRET="$FALCON_CLIENT_SECRET" \
          -e FALCON_CLOUD_REGION="$FALCON_CLOUD_REGION" \
          -e CHRONICLE_CUSTOMER_ID="$CHRONICLE_CUSTOMER_ID" \
          -e CHRONICLE_REGION="$CHRONICLE_REGION" \
          -e GOOGLE_SERVICE_ACCOUNT_FILE=/gcloud/sa.json \
          -v /path/to/your/service-account.json:/gcloud/sa.json:ro \
          quay.io/crowdstrike/chronicle-intel-bridge:latest
        

Replace `/path/to/your/service-account.json` with the actual path to the Google SecOps service account JSON file you downloaded earlier.

**Note:** The `--restart unless-stopped` flag ensures the container automatically restarts if it stops unexpectedly or if the Docker daemon restarts.



### Verify the deployment

After starting the container, verify that indicators are being forwarded to Google Security Operations:

  1. Check the container logs:
         
         docker logs chronicle-intel-bridge
         

  2. In the Google SecOps console, search for events with the log type `CROWDSTRIKE_IOC`.

  3. Verify that indicator data is appearing in your Google SecOps instance.




## Advanced configuration

For advanced configuration options, you can customize the Intel Bridge behavior using a configuration file.

  1. Download the `config.ini` file from the [CrowdStrike Chronicle Intel Bridge repository](https://github.com/CrowdStrike/chronicle-intel-bridge).
  2. Modify the configuration file according to your requirements.
  3. Mount the configuration file to the container using the volume flag:
         
         docker run -d --restart unless-stopped \
           --name chronicle-intel-bridge \
           -e FALCON_CLIENT_ID="$FALCON_CLIENT_ID" \
           -e FALCON_CLIENT_SECRET="$FALCON_CLIENT_SECRET" \
           -e FALCON_CLOUD_REGION="$FALCON_CLOUD_REGION" \
           -e CHRONICLE_CUSTOMER_ID="$CHRONICLE_CUSTOMER_ID" \
           -e CHRONICLE_REGION="$CHRONICLE_REGION" \
           -e GOOGLE_SERVICE_ACCOUNT_FILE=/gcloud/sa.json \
           -v /path/to/your/service-account.json:/gcloud/sa.json:ro \
           -v /path/to/your/config.ini:/ccib/config.ini:ro \
           quay.io/crowdstrike/chronicle-intel-bridge:latest
         




## Supported indicator types

The CrowdStrike Indicator of Compromise (IoC) parser supports the following indicator types:

Indicator Type | Description  
---|---  
**domain** | Domain names associated with malicious activity  
**email_address** | Email addresses used in attacks  
**file_name** | Malicious file names  
**file_path** | File system paths associated with threats  
**hash_md5** | MD5 file hashes  
**hash_sha1** | SHA-1 file hashes  
**hash_sha256** | SHA-256 file hashes  
**ip_address** | IP addresses associated with malicious activity  
**mutex_name** | Mutex names used by malware  
**url** | URLs associated with threats  
  
## Manage the Docker container

Use the following Docker commands to manage the Chronicle Intel Bridge:

  * **View container status:**
        
        docker ps -a | grep chronicle-intel-bridge
        

  * **View container logs:**
        
        docker logs chronicle-intel-bridge
        

  * **Follow container logs in real-time:**
        
        docker logs -f chronicle-intel-bridge
        

  * **Stop the container:**
        
        docker stop chronicle-intel-bridge
        

  * **Start the container:**
        
        docker start chronicle-intel-bridge
        

  * **Restart the container:**
        
        docker restart chronicle-intel-bridge
        

  * **Remove the container:**
        
        docker stop chronicle-intel-bridge
        docker rm chronicle-intel-bridge
        




## Troubleshooting

If you encounter issues with the Chronicle Intel Bridge:

  1. Verify that the CrowdStrike API credentials are correct and have the **Indicators (Falcon Intelligence): READ** scope.
  2. Verify that the Google SecOps Customer ID is correct.
  3. Verify that the Google SecOps service account JSON file is valid and accessible to the Docker container.
  4. Verify that the CrowdStrike cloud region is correct (for example, `us-1`, `us-2`, `eu-1`).
  5. Verify that the Google SecOps region is correct.
  6. Check the container logs for error messages:
         
         docker logs chronicle-intel-bridge
         

  7. Verify network connectivity from the Docker host to both CrowdStrike API endpoints and Google SecOps ingestion endpoints.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
when | metadata.event_timestamp | Value copied directly  
messageid | metadata.id | Value copied directly  
protocol | network.ip_protocol | Value copied directly  
deviceName | principal.hostname | Value copied directly  
srcAddr | principal.ip | Value copied directly  
srcPort | principal.port | Value copied directly  
action | security_result.action | Value copied directly  
dstAddr | target.ip | Value copied directly  
dstPort | target.port | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/crowdstrike-ioc-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
