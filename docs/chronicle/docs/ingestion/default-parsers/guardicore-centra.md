---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardicore-centra/
title: Collect Akamai Guardicore Segmentation (formerly Guardicore Centra) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:50:26.474108+00:00
---

# Collect Akamai Guardicore Segmentation (formerly Guardicore Centra) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardicore-centra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Akamai Guardicore Segmentation (formerly Guardicore Centra) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to configure Akamai Guardicore Segmentation (formerly Guardicore Centra) to push logs to Google Security Operations using the Akamai Unified Log Streamer (ULS) with HTTP output.

Guardicore Centra is a micro-segmentation platform that provides Zero Trust network security for data centers, cloud environments, and endpoints. It delivers visibility into application dependencies, breach detection through deception technology, and granular segmentation controls to prevent lateral movement and contain threats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Guardicore Centra instance (cloud or on-premises)
  * A Linux server to run Akamai ULS (minimum: 1 vCPU, 1 GB RAM, 500 MB disk)
  * Python 3.9 or later installed on the ULS server
  * Administrator access to Guardicore Centra to create a read-only API user
  * Outbound HTTPS access from the ULS server to Google SecOps ingestion endpoints
  * Access to Google Cloud console (for API key creation)



## Create the feed in Google SecOps

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed. For example, `Guardicore Centra Logs`.
  5. Select **Webhook** as the **Source type**.
  6. Select **Guardicore Centra** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` to split multi-line events (ULS sends newline-delimited JSON).
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



### Generate and save the secret key

After creating the feed, you must generate a secret key for authentication as follows:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is only displayed once and cannot be retrieved later. If you lose it, you must generate a new secret key.

### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is either:
         
         https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs
         

or
         
         https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs
         

  4. Save this URL for the next steps.

  5. Click **Done**.




## Create a Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud console.

### Create the API key

  1. Go to the [Google Cloud console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project. This is the project associated with your Google SecOps instance.
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Guardicore Webhook API Key`).
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** drop-down, search for and select **Chronicle API**.
  3. Click **Save**.
  4. Copy the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.

## Configure Guardicore Centra credentials

### Create a read-only API user in Guardicore Centra

ULS authenticates to the Centra API with a portal user. Create a dedicated user with read-only permissions rather than using an administrator account as follows:

  1. Sign in to the Guardicore Centra management console.
  2. Go to **Administration > Users**.
  3. Click **Create User**.
  4. Provide the following configuration details: 
     * **Username** : Enter a name for the integration user (for example, `secops-uls`).
     * **Password** : Enter a password.
     * **Permission scheme** : Select **Support** (read-only access).
  5. Click **Save**.
  6. Sign out and then sign in with the new user, and complete the mandatory password change.
  7. Note the hostname of the Centra management console (without `https://`). ULS uses this as the API hostname.



### Create the .edgerc file for Guardicore authentication

Akamai ULS reads Guardicore credentials from the `.edgerc` file, from the `gc_hostname`, `gc_username` and `gc_password` keys.

  1. On the ULS server, create the `.edgerc` file in the home directory as follows:
         
         nano ~/.edgerc
         

  2. Add the following configuration:
         
         [default]
         gc_hostname = your-instance.cloud.guardicore.com
         gc_username = your_username
         gc_password = your_password
         

Replace the following values:

     * `your-instance.cloud.guardicore.com` \- Your Guardicore Centra management hostname (without `https://`)
     * `your_username` \- The username of the read-only API user created in the previous section
     * `your_password` \- That user's password

**Example:**
    
    [default]
    gc_hostname = cus-1234.cloud.guardicore.com
    gc_username = secops-uls
    gc_password = MySecurePassword123
    

  3. Save and close the file.

  4. Set appropriate permissions as follows:
         
         chmod 600 ~/.edgerc
         


**Note:** ULS validates that all three `gc_*` keys are present before it starts a Guardicore feed. The `linode_hostname` and `linode_token` keys belong to the separate Linode integration and are not read for Guardicore.

## Install Akamai ULS

### Install ULS from GitHub

  1. On the ULS server, clone the ULS repository as follows:
         
         git clone https://github.com/akamai/uls.git
         cd uls
         

  2. Install Python dependencies:
         
         pip3 install -r requirements.txt
         

  3. Install the Guardicore log fetcher module (`gc-logs`) into the `ext` directory of the ULS checkout:
         
         git clone -q --depth 1 -b v0.0.8 --single-branch https://github.com/MikeSchiessl/gc-logs.git ext/cli-gc
         pip3 install -r ext/cli-gc/bin/requirements.txt
         

**Note:** ULS loads the Guardicore module from `ext/cli-gc`. The module is published in the `gc-logs` repository referenced by the ULS installation documentation and Dockerfile; the former `guardicore/log-fetcher` repository no longer exists. The `v0.0.8` tag is the version pinned by the ULS Dockerfile (`GC_CLI_VERSION`); use the tag from the ULS release you install.
  4. Verify the installation:
         
         python3 bin/uls.py --help
         




## Configure ULS to send logs to Google SecOps

### Construct the Google SecOps webhook URL

  * Combine the Google SecOps endpoint URL and API key as follows:
        
        <ENDPOINT_URL>?key=<API_KEY>
        

  * **Example:**
        
        https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=AIzaSyD...
        




### Run ULS for the Guardicore NETLOG feed

The `NETLOG` feed contains network flow logs from Guardicore agents.

  1. Run ULS with the following command:
         
         python3 bin/uls.py \
             --input gc \
             --feed NETLOG \
             --output http \
             --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" \
             --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' \
             --httpformat '%s'
         

     * Replace the following values: 
       * `YOUR_API_KEY` \- The Google Cloud API key created earlier
       * `YOUR_SECRET_KEY` \- The Google SecOps secret key generated earlier
  2. ULS starts streaming `NETLOG` events to Google SecOps.




### Run ULS for the Guardicore INCIDENT feed

The `INCIDENT` feed contains security incidents detected by Guardicore.

  1. Run ULS with the following command:
         
         python3 bin/uls.py \
             --input gc \
             --feed INCIDENT \
             --output http \
             --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" \
             --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' \
             --httpformat '%s'
         

     * Replace the following values: 
       * `YOUR_API_KEY` \- The Google Cloud API key created earlier
       * `YOUR_SECRET_KEY` \- The Google SecOps secret key generated earlier
  2. ULS starts streaming `INCIDENT` events to Google SecOps.




### Run ULS for the Guardicore AGENT feed

The `AGENT` feed contains agent status and health information.

  1. Run ULS with the following command:
         
         python3 bin/uls.py \
             --input gc \
             --feed AGENT \
             --output http \
             --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" \
             --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' \
             --httpformat '%s'
         

     * Replace the following values: 
       * `YOUR_API_KEY` \- The Google Cloud API key created earlier
       * `YOUR_SECRET_KEY` \- The Google SecOps secret key generated earlier
  2. ULS will start streaming `AGENT` events to Google SecOps.




### Run ULS for Guardicore SYSTEM feed

The `SYSTEM` feed contains system alerts and events.

  1. Run ULS with the following command:
         
         python3 bin/uls.py \
             --input gc \
             --feed SYSTEM \
             --output http \
             --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" \
             --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' \
             --httpformat '%s'
         

     * Replace the following values: 
       * `YOUR_API_KEY` \- The Google Cloud API key created earlier
       * `YOUR_SECRET_KEY` \- The Google SecOps secret key generated earlier
  2. ULS will start streaming `SYSTEM` events to Google SecOps.




### Run ULS for the Guardicore AUDIT feed

The AUDIT feed contains audit logs of administrative actions.

  1. Run ULS with the following command:
         
         python3 bin/uls.py \
             --input gc \
             --feed AUDIT \
             --output http \
             --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" \
             --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' \
             --httpformat '%s'
         

     * Replace the following values: 
       * `YOUR_API_KEY` \- The Google Cloud API key created earlier
       * `YOUR_SECRET_KEY` \- The Google SecOps secret key generated earlier
  2. ULS will start streaming `AUDIT` events to Google SecOps.




## Run ULS as a background service

To ensure ULS runs continuously, configure it as a `systemd` service.

### Create a systemd service file for the NETLOG feed

  1. Create a service file:
         
         sudo nano /etc/systemd/system/uls-guardicore-netlog.service
         

  2. Add the following content:
         
         [Unit]
         Description=Akamai ULS - Guardicore NETLOG
         After=network.target
         
         [Service]
         Type=simple
         User=root
         WorkingDirectory=/root/uls
         ExecStart=/usr/bin/python3 /root/uls/bin/uls.py --input gc --feed NETLOG --output http --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' --httpformat '%%s'
         Restart=always
         RestartSec=10
         
         [Install]
         WantedBy=multi-user.target
         

     * Replace the following values: 
       * `/root/uls` \- The path where you cloned the ULS repository
       * `YOUR_API_KEY` \- The Google Cloud API key
       * `YOUR_SECRET_KEY` \- The Google SecOps secret key
  3. Save and close the file.

  4. Enable and start the service:
         
         sudo systemctl daemon-reload
         sudo systemctl enable uls-guardicore-netlog.service
         sudo systemctl start uls-guardicore-netlog.service
         

  5. Check the service status:
         
         sudo systemctl status uls-guardicore-netlog.service
         




### Create additional services for other feeds

Repeat the preceding steps for each feed you want to collect (`INCIDENT, AGENT, SYSTEM, AUDIT`), creating separate service files as follows:

  * `/etc/systemd/system/uls-guardicore-incident.service`
  * `/etc/systemd/system/uls-guardicore-agent.service`
  * `/etc/systemd/system/uls-guardicore-system.service`
  * `/etc/systemd/system/uls-guardicore-audit.service`



Change the `--feed` parameter and service name accordingly in each file.

## Verify log ingestion

  1. Wait 5-10 minutes for logs to be ingested and processed.
  2. In the Google SecOps console, go to **Search**.
  3. Run the following UDM search query:
         
         metadata.vendor_name = "Guardicore"
         

  4. If logs are ingested successfully, you should see Guardicore events in the search results.

  5. You can also search for specific feed types:
         
         metadata.vendor_name = "Guardicore" AND metadata.product_name = "Centra"
         




## Troubleshooting

### ULS connection errors

If ULS fails to connect to Guardicore do the following:

  1. Verify the `.edgerc` file contains the correct hostname and credentials.
  2. Test connectivity to your Guardicore instance as follows:
         
         curl -u "username:password" https://your-instance.cloud.guardicore.com/api/v3.0/visibility
         

  3. Check that the Guardicore instance is accessible from the ULS server.




### ULS HTTP output errors

If ULS fails to send logs to Google SecOps, do the following:

  1. Verify that the API and secret keys are correct.
  2. Check that the Google SecOps endpoint URL is correct for your region.
  3. Verify outbound HTTPS connectivity from the ULS server:
         
         curl -I https://malachiteingestion-pa.googleapis.com
         

  4. Review ULS logs for error messages:
         
         sudo journalctl -u uls-guardicore-netlog.service -f
         




### Logs don't display in the platform

If logs don't appear in Google SecOps, do the following:

  1. Verify the webhook feed is in **Active** status in **SIEM Settings > Feeds**.
  2. Check the feed's **Health** tab for ingestion errors.
  3. Verify the split delimiter is set to `\n` in the feed configuration.
  4. Ensure the log type is set to **Guardicore Centra**.



### Self-signed certificate errors

If your Guardicore instance uses a self-signed certificate, ULS may fail with SSL verification errors. To bypass SSL verification (not recommended for production) do the following:

  * Add the `--httpinsecure` flag to the ULS command:
        
        python3 bin/uls.py \
            --input gc \
            --feed NETLOG \
            --output http \
            --httpurl "https://<REGION>-chronicle.googleapis.com/v1alpha/projects/<PROJECT_NUMBER>/locations/<REGION>/instances/<INSTANCE_ID>/feeds/<FEED_ID>:importPushLogs?key=YOUR_API_KEY" \
            --httpauthheader '{"X-Webhook-Access-Key": "YOUR_SECRET_KEY"}' \
            --httpformat '%s' \
            --httpinsecure
        


**Note:** Using `--httpinsecure` disables SSL certificate verification and should only be used in testing environments.

## Available Guardicore feeds

Akamai ULS supports the following Guardicore feeds:

Feed Name | Description | ULS Feed Parameter  
---|---|---  
`NETLOG` | Network flow logs from Guardicore agents | `NETLOG`  
`INCIDENT` | Security incidents detected by Guardicore | `INCIDENT`  
`AGENT` | Agent status and health information | `AGENT`  
`SYSTEM` | System Alerts** | System-level alerts and events  
`AUDIT Logs` | Administrative actions and configuration changes | `AUDIT`  
  
## Authentication methods reference

Google SecOps webhook feeds support multiple authentication methods. Akamai ULS uses the hybrid method with the API key in the URL and the secret key in header.

### Method used by ULS: Hybrid (URL + Header)

  * **Request format:**
        
        POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
        Content-Type: application/json
        X-Webhook-Access-Key: <SECRET_KEY>
        
        {"event": "data", "timestamp": "2025-01-15T10:30:00Z"}
        

  * **ULS command format:**
        
        --httpurl "<ENDPOINT_URL>?key=<API_KEY>"
        --httpauthheader '{"X-Webhook-Access-Key": "<SECRET_KEY>"}'
        




### Authentication header names

Google SecOps accepts the following header names for authentication:

**For the API key:**

  * `X-goog-api-key` (recommended)
  * `X-goog-api-key` (case-insensitive)



**For the secret key:**

  * `X-Webhook-Access-Key` (recommended)
  * `X-Webhook-Access-Key` (case-insensitive)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max single log line** | 1 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 90 seconds  
**Retry behavior** | Sender-managed. Google SecOps returns HTTP 429 when the burst limit is exceeded; the sending system must buffer and retry.  
  
### Best practices

  * Run separate ULS instances for each feed type to improve reliability and troubleshooting.
  * Monitor ULS service status using systemd and set up alerts for service failures.
  * Rotate Guardicore credentials periodically and update the `.edgerc` file.
  * Use a dedicated service account in Guardicore with read-only API access.
  * Configure log rotation for ULS logs to prevent disk space issues.
  * Test failover scenarios by running ULS on multiple servers with load balancing.



## UDM mapping table

The following table lists the log fields of the Guardicore Centra log and their corresponding UDM fields.

Log Field | UDM Field | Description  
---|---|---  
`timestamp` | `metadata.event_timestamp` | Event timestamp  
`source_ip` | `principal.ip` | Source IP address  
`destination_ip` | `target.ip` | Destination IP address  
`source_port` | `principal.port` | Source port number  
`destination_port` | `target.port` | Destination port number  
`protocol` | `network.ip_protocol` | Network protocol  
`action` | `security_result.action` | Security action taken  
`severity` | `security_result.severity` | Event severity  
`user` | `principal.user.userid` | Username  
`hostname` | `principal.hostname` | Source hostname  
`process_name` | `principal.process.file.full_path` | Process name  
`incident_id` | `security_result.detection_fields.key` | Incident identifier  
`description` | `security_result.description` | Event description  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardicore-centra-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
