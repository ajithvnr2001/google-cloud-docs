---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kong-gateway/
title: Collect Kong Gateway logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:53.578956+00:00
---

# Collect Kong Gateway logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kong-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Kong Gateway logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to collect Kong Gateway and Kong Konnect logs into Google Security Operations using multiple ingestion methods, including webhooks, syslog via Bindplane agent, and cloud storage.

Kong Gateway is an open-source, cloud-native API gateway built on top of NGINX. It provides traffic management, authentication, rate limiting, analytics, and logging capabilities for APIs and microservices. Kong Konnect is the SaaS management platform for Kong Gateway that provides centralized control plane management, audit logging, and observability.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A running Kong Gateway instance (self-managed) or a Kong Konnect account (SaaS)
  * Administrative access to the Kong Gateway Admin API on port `8001` (HTTP) or `8444` (HTTPS)
  * For Kong Konnect: A Personal Access Token (PAT) or System Account token with appropriate permissions
  * Access to Google Cloud Console (for API key creation, if using webhook ingestion)



## Configure Kong Gateway to push logs using webhook (HTTP Log plugin)

This method uses the Kong Gateway HTTP Log plugin to send request and response logs directly to a Google SecOps webhook endpoint via HTTP POST. Each proxied request generates a JSON log entry that is sent to the configured endpoint.

### Create webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Kong Gateway Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Kong Gateway** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` to split newline-delimited JSON events
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.



**Important** : The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.

#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




### Create Google Cloud API key

Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

#### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Chronicle instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



#### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Chronicle Webhook API Key`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Chronicle API, reducing security risk if the key is compromised.



### Construct the webhook URL

  * Combine the Chronicle endpoint URL and API key:
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




Save this full URL for the Kong Gateway HTTP Log plugin configuration.

### Configure Kong Gateway HTTP Log plugin

The HTTP Log plugin sends request and response logs to an HTTP endpoint via POST requests in JSON format. You can enable the plugin globally (for all services and routes), per service, or per route using the Kong Admin API.

#### Enable the HTTP Log plugin globally

  * To send logs for all proxied requests to Google SecOps, enable the plugin globally by sending the following request to the Kong Admin API:
        
        curl -i -X POST http://localhost:8001/plugins/ \
            --header "Accept: application/json" \
            --header "Content-Type: application/json" \
            --data '{
                "name": "http-log",
                "config": {
                    "http_endpoint": "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>",
                    "method": "POST",
                    "timeout": 3000,
                    "keepalive": 60000,
                    "retry_count": 1,
                    "queue": {
                        "max_batch_size": 100,
                        "max_coalescing_delay": 10
                    }
                }
            }'
        




Replace the following:

  * `<ENDPOINT_URL>`: The Google SecOps feed endpoint URL
  * `<API_KEY>`: The Google Cloud API key
  * `<SECRET_KEY>`: The Google SecOps webhook secret key



#### Enable the HTTP Log plugin for a specific service

  * To send logs only for a specific service, send the following request:
        
        curl -i -X POST http://localhost:8001/services/{serviceName|Id}/plugins/ \
            --header "Accept: application/json" \
            --header "Content-Type: application/json" \
            --data '{
                "name": "http-log",
                "config": {
                    "http_endpoint": "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>",
                    "method": "POST",
                    "timeout": 3000,
                    "keepalive": 60000,
                    "retry_count": 1
                }
            }'
        

Replace `{serviceName|Id}` with the name or ID of the target service.




#### Enable the HTTP Log plugin for a specific route

  * To send logs only for a specific route, send the following request:
        
        curl -i -X POST http://localhost:8001/routes/{routeName|Id}/plugins/ \
            --header "Accept: application/json" \
            --header "Content-Type: application/json" \
            --data '{
                "name": "http-log",
                "config": {
                    "http_endpoint": "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>",
                    "method": "POST",
                    "timeout": 3000,
                    "keepalive": 60000,
                    "retry_count": 1
                }
            }'
        

Replace `{routeName|Id}` with the name or ID of the target route.




#### Enable the HTTP Log plugin via Kong Konnect API

  * If you manage Kong Gateway through Kong Konnect, enable the HTTP Log plugin using the Konnect API:
        
        curl -X POST https://{region}.api.konghq.com/v2/control-planes/{controlPlaneId}/core-entities/plugins/ \
            --header "accept: application/json" \
            --header "Content-Type: application/json" \
            --header "Authorization: Bearer $KONNECT_TOKEN" \
            --data '{
                "name": "http-log",
                "config": {
                    "http_endpoint": "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>",
                    "method": "POST",
                    "timeout": 3000,
                    "keepalive": 60000,
                    "retry_count": 1
                }
            }'
        




Replace the following:

  * `{region}`: The geographic region where your Kong Konnect is hosted (for example, `us`, `eu`)
  * `{controlPlaneId}`: The ID of the control plane
  * `$KONNECT_TOKEN`: Your Personal Access Token (PAT)



#### Enable the HTTP Log plugin via declarative configuration (decK)

  * Add the following to your `kong.yaml` configuration file:
        
        _format_version: "3.0"
        plugins:
          - name: http-log
            config:
              http_endpoint: "<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>"
              method: POST
              timeout: 3000
              keepalive: 60000
              retry_count: 1
              queue:
                max_batch_size: 100
                max_coalescing_delay: 10
        




#### Verify the HTTP Log plugin

  1. Send a test request through Kong Gateway:
         
         curl -i http://localhost:8000/your-route
         

  2. Verify the plugin is enabled by listing plugins:
         
         curl -s http://localhost:8001/plugins/ | grep http-log
         

  3. In Google SecOps, go to **Search** and search for logs with `metadata.log_type = "KONG_GATEWAY"` to confirm log ingestion.




## Configure Kong Konnect audit log webhook

This method configures Kong Konnect (SaaS) to push audit logs (authentication, authorization, and access events) to a Google SecOps webhook endpoint.

### Generate a Kong Konnect Personal Access Token

  1. Sign in to [Kong Konnect](https://cloud.konghq.com/).
  2. Click your **user icon** in the top-right corner to open the context menu.
  3. Click **Personal access tokens**.
  4. Click **Generate Token**.
  5. Enter a name for the token (for example, `Chronicle Audit Log Setup`).
  6. Select an expiration period.
  7. Click **Generate**.
  8. **Copy and save** the token securely. The token is only displayed once.



### Create a Google SecOps webhook feed for Konnect audit logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Kong Konnect Audit Logs`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Kong Gateway** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** : Enter `\n` to split newline-delimited events
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.
  11. Click **Generate Secret Key** and save the secret key.
  12. Go to the **Details** tab and copy the **Feed endpoint URL**.
  13. Create a Google Cloud API key following the steps in the previous section.
  14. Construct the full webhook URL:
         
         <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
         




### Create an audit log destination in Konnect

  * Send a POST request to the Konnect API to create an audit log destination:
        
        curl -X POST "https://global.api.konghq.com/v3/audit-log-destinations" \
            --header "Authorization: Bearer $KONNECT_TOKEN" \
            --header "Content-Type: application/json" \
            --data '{
                "endpoint": "<ENDPOINT_URL>?key=<API_KEY>",
                "authorization": "<SECRET_KEY>",
                "log_format": "json",
                "name": "Chronicle SecOps"
            }'
        




Replace the following:

  * `$KONNECT_TOKEN`: Your Kong Konnect Personal Access Token
  * `<ENDPOINT_URL>`: The Google SecOps feed endpoint URL
  * `<API_KEY>`: The Google Cloud API key
  * `<SECRET_KEY>`: The Google SecOps webhook secret key



Save the `id` value from the response for the next step.

### Enable the audit log webhook

  * Send a PATCH request to enable the webhook:
        
        curl -X PATCH "https://us.api.konghq.com/v3/audit-log-webhook" \
            --header "Authorization: Bearer $KONNECT_TOKEN" \
            --header "Content-Type: application/json" \
            --data '{
                "audit_log_destination_id": "<DESTINATION_ID>",
                "enabled": true
            }'
        

Replace `<DESTINATION_ID>` with the ID returned from the previous step.

**Note:** Replace `us.api.konghq.com` with the regional API endpoint matching your Konnect region (for example, `eu.api.konghq.com` for Europe).



### Verify Konnect audit log delivery

  1. Trigger an audit log event by making a Konnect API request:
         
         curl -X GET "https://us.api.konghq.com/v2/control-planes" \
             --header "Authorization: Bearer $KONNECT_TOKEN"
         

  2. Wait 1-2 minutes for the log to propagate.

  3. In Google SecOps, search for logs with `metadata.log_type = "KONG_GATEWAY"`.




### Konnect audit log webhook behavior

  * Konnect retries webhook delivery on `429` (Too Many Requests) and `500` (Server Error) HTTP status codes.
  * Minimum retry wait time: 1 second.
  * Maximum retry wait time: 30 seconds.
  * Maximum number of retries: 4.
  * Konnect retains audit logs for 7 days. After 7 days, logs are permanently deleted.
  * Supported log formats: `cef` (ArcSight CEF Format), `json`, and `cps` (CrowdStrike Parsing Standard).



## Authentication methods reference

Chronicle webhook feeds support multiple authentication methods. Choose the method that your vendor supports.

### Method 1: Query parameters

  * Kong Gateway HTTP Log plugin supports passing credentials in the URL.

  * **URL format:**
        
        <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
        

  * **Example:**
        
        https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import?key=AIzaSyD...&secret=abcd1234...
        




### Method 2: Custom headers with query parameter

Kong Gateway HTTP Log plugin supports custom HTTP headers via the `config.headers` parameter. You can pass the API key in the URL and the secret key in a custom header.

  * **Kong Admin API example:**
        
        curl -i -X POST http://localhost:8001/plugins/ \
            --header "Accept: application/json" \
            --header "Content-Type: application/json" \
            --data '{
                "name": "http-log",
                "config": {
                    "http_endpoint": "<ENDPOINT_URL>?key=<API_KEY>",
                    "method": "POST",
                    "timeout": 3000,
                    "headers": {
                        "x-chronicle-auth": "<SECRET_KEY>"
                    }
                }
            }'
        




### Authentication header names

Chronicle accepts the following header names for authentication:

**For API key:**

  * `x-goog-chronicle-auth` (recommended)
  * `X-Goog-Chronicle-Auth` (case-insensitive)



**For secret key:**

  * `x-chronicle-auth` (recommended)
  * `X-Chronicle-Auth` (case-insensitive)



## Webhook limits and best practices

### Request limits

Limit | Value  
---|---  
**Max request size** | 4 MB  
**Max QPS (queries per second)** | 15,000  
**Request timeout** | 30 seconds  
**Retry behavior** | Automatic with exponential backoff  
  
### Kong HTTP Log plugin queue configuration

Parameter | Description | Recommended Value  
---|---|---  
**config.queue.max_batch_size** | Maximum number of log entries per batch | `100`  
**config.queue.max_coalescing_delay** | Maximum time (seconds) to wait before sending a batch | `10`  
**config.queue.max_entries** | Maximum number of entries in the queue | `10000`  
**config.queue.max_retry_time** | Maximum time (seconds) to retry failed deliveries | `60`  
**config.queue.initial_retry_delay** | Initial wait time (seconds) before retrying | `0.01`  
  
## Configure Kong Gateway syslog forwarding using Bindplane agent

This method uses the Kong Gateway Syslog plugin to write logs to the local syslog daemon, which are then collected by the Bindplane agent and forwarded to Google SecOps. This approach is suitable for self-managed Kong Gateway deployments.

### Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



#### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

#### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

### Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



### Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

#### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

#### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

#### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

### Configure Bindplane agent to ingest syslog and send to Google SecOps

#### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




#### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/kong_gateway:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: KONG_GATEWAY
            raw_log_field: body
        
        service:
          pipelines:
            logs/kong_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/kong_gateway
        




#### Configuration parameters

Replace the following placeholders:

  * **Exporter configuration:**

    * `<CUSTOMER_ID>`: The Google SecOps customer ID copied in the previous step
    * **creds_file_path** : Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/kong_gateway:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: KONG_GATEWAY
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

#### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



### Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           

  * To restart the Bindplane agent in Windows, choose one of the following options:

    * Command Prompt or PowerShell as administrator:
          
          net stop observiq-otel-collector && net start observiq-otel-collector
          

  * Services console:

    1. Press Win+R, type services.msc, and press Enter.
    2. Locate **observIQ OpenTelemetry Collector**.
    3. Right-click and select **Restart**.
    4. Verify the service is running:
           
           sc query observiq-otel-collector
           

    5. Check logs for errors:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
           




### Configure Kong Gateway syslog forwarding

There are two methods to forward Kong Gateway logs via syslog: using the Syslog plugin (for per-request API traffic logs) and using `kong.conf` (for system-level access and error logs).

#### Method 1: Enable the Syslog plugin via Admin API

  * The Syslog plugin logs each proxied request and response to the local syslog daemon in JSON format. Enable the plugin globally by sending the following request to the Kong Admin API:
        
        curl -i -X POST http://localhost:8001/plugins/ \
            --header "Accept: application/json" \
            --header "Content-Type: application/json" \
            --data '{
                "name": "syslog",
                "config": {
                    "log_level": "info",
                    "successful_severity": "info",
                    "client_errors_severity": "info",
                    "server_errors_severity": "info"
                }
            }'
        




The Syslog plugin configuration parameters:

  * **log_level** : The minimum log level to send to syslog. Accepted values: `debug`, `info`, `notice`, `warning`, `err`, `crit`, `alert`, `emerg`. Default: `info`.
  * **successful_severity** : Syslog severity for successful requests (2xx status codes). Default: `info`.
  * **client_errors_severity** : Syslog severity for client error requests (4xx status codes). Default: `info`.
  * **server_errors_severity** : Syslog severity for server error requests (5xx status codes). Default: `info`.

**Note:** The Syslog plugin writes to the local syslog daemon using the `user` facility. The syslog daemon must be running on the Kong Gateway host and configured with a logging level severity equal to or lower than the `config.log_level` value.



#### Method 2: Configure kong.conf for remote syslog forwarding

  * To forward Kong Gateway system logs (access logs and error logs) directly to a remote syslog server, edit the `kong.conf` file and set the following parameters:
        
        proxy_access_log=syslog:server=<BINDPLANE_IP>:514,facility=user,tag=kong_proxy_access,severity=info
        proxy_error_log=syslog:server=<BINDPLANE_IP>:514,facility=user,tag=kong_proxy_error,severity=info
        admin_access_log=syslog:server=<BINDPLANE_IP>:514,facility=user,tag=kong_admin_access,severity=info
        admin_error_log=syslog:server=<BINDPLANE_IP>:514,facility=user,tag=kong_admin_error,severity=info
        




Replace `<BINDPLANE_IP>` with the IP address of the host running the Bindplane agent.

  * After editing `kong.conf`, restart Kong Gateway:
        
        kong restart
        




#### Method 3: Enable the Syslog plugin via declarative configuration (decK)

  * Add the following to your `kong.yaml` configuration file:
        
        _format_version: "3.0"
        plugins:
          - name: syslog
            config:
              log_level: info
              successful_severity: info
              client_errors_severity: info
              server_errors_severity: info
        




#### Verify syslog forwarding

  1. Send a test request through Kong Gateway:
         
         curl -i http://localhost:8000/your-route
         

  2. Check the Bindplane agent logs for incoming syslog messages:
         
         sudo journalctl -u observiq-otel-collector -f
         

  3. In Google SecOps, search for logs with `metadata.log_type = "KONG_GATEWAY"` to confirm log ingestion.




## Kong Gateway log format reference

All Kong Gateway logging plugins (HTTP Log, Syslog, File Log, TCP Log, UDP Log) output logs in the same JSON format. Each log entry contains the following fields:

Field | Description  
---|---  
**request** | Properties of the client request including headers, method, URI, size, and URL  
**response** | Properties of the response including status code, headers, and size  
**latencies.kong** | Internal Kong Gateway processing latency in milliseconds  
**latencies.proxy** | Time for the upstream service to process the request in milliseconds  
**latencies.request** | Total request time from first byte received to last byte sent in milliseconds  
**latencies.receive** | Time to receive and process the upstream response in milliseconds  
**service** | Properties of the Gateway Service associated with the request  
**route** | Properties of the specific Route requested  
**client_ip** | The original client IP address  
**tries** | Load balancer iterations including IP, port, and balancer latency  
**workspace** | UUID of the Workspace associated with the request  
**workspace_name** | Name of the Workspace associated with the request  
**upstream_uri** | The URI sent to the upstream service  
**upstream_status** | HTTP status code received from the upstream service  
**source** | Indicates whether the response was generated by `kong` or `upstream`  
**started_at** | Unix timestamp of when the request processing started  
**consumer** | The authenticated Consumer (only present if authentication is enabled)  
**authenticated_entity** | Properties of the authenticated credential (only present if authentication is enabled)  
  
## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
intermediary_host | intermediary | Merged from intermediary hash containing hostname from intermediary_host and ip from xff_ips  
xff_ips | intermediary |   
service.host | metadata.event_type | Set to "NETWORK_CONNECTION" if service.host or client_ip not empty, else "STATUS_UNCATEGORIZED" if target not empty, else "GENERIC_EVENT"  
client_ip | metadata.event_type |   
request.headers.x-consumer-id | metadata.ingestion_labels | Merged as label with key "x-consumer-id" and value from request.headers.x-consumer-id  
metadata._id | metadata.product_log_id | Value copied directly  
metadata.version | metadata.product_version | Value copied directly  
application_protocol | network.application_protocol | Value from application_protocol set from route.protocols or service.protocol  
request.method | network.http.method | Value copied directly  
response.status | network.http.response_code | Converted to integer  
response.size | network.received_bytes | Converted to uinteger  
request.size | network.sent_bytes | Converted to uinteger  
agent.name | observer.asset_id | Concatenated from agent.name and agent.id  
agent.id | observer.asset_id |   
agent.hostname | observer.hostname | Value copied directly  
agent.version | observer.platform_version | Value copied directly  
agent.ephemeral_id | observer.resource.attribute.labels | Merged as label with key "ephemeral_id" and value from agent.ephemeral_id  
cloud.availability_zone | principal.cloud.availability_zone | Value copied directly  
cloud.instance.id | principal.cloud.project.id | Value copied directly  
cloud.instance.name | principal.cloud.project.name | Value copied directly  
cloud.machine.type | principal.cloud.project.type | Set to "VIRTUAL_MACHINE" if not empty  
principal_host | principal.hostname | Value from principal_host if not empty, else host.fqdn  
host.fqdn | principal.hostname |   
host.ip | principal.ip | Merged from host.ip array  
host.mac | principal.mac | Merged from host.mac array  
host.os.name | principal.platform | Set to "LINUX" if matches (?i)Linux, "WINDOWS" if matches (?i)windows, "MAC" if matches (?i)mac  
host.os.version | principal.platform_version | Value copied directly  
request.headers.content-type | principal.resource.attribute.labels | Merged from labels with key "content-type" and value from request.headers.content-type, and key "auth_type" and value from request.decoded_headers.authorization.auth_type  
request.decoded_headers.authorization.auth_type | principal.resource.attribute.labels |   
request.url | principal.url | Value copied directly  
request.decoded-headers.authorization.user | principal.user.user_display_name | Value copied directly  
log_level | security_result | Merged from security_result hash with severity set based on log_level regex matches  
service.host | target.asset_id | Concatenated from service.host and service.id  
service.id | target.asset_id |   
log.file.path | target.file.full_path | Value copied directly  
service.host | target.hostname | Value copied directly if service.host is not an IP  
client_ip | target.ip | Merged from client_ip and service_host if service.host is an IP  
service_host | target.ip |   
service.port | target.port | Converted to integer  
response.headers.set-cookie | target.resource.attribute.labels | Merged from labels with key "set-cookie" and value from response.headers.set-cookie, and key "route.id" and value from route.id  
route.id | target.resource.attribute.labels |   
metadata.vendor_name | metadata.vendor_name | Set to "KONG_GATEWAY"  
metadata.product_name | metadata.product_name | Set to "KONG_GATEWAY"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kong-gateway-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
