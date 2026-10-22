---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-ltm/
title: Collect F5 BIG-IP LTM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:24.298084+00:00
---

# Collect F5 BIG-IP LTM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-ltm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 BIG-IP LTM logs 

**Parser Version:** 24.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 BIG-IP LTM logs to Google Security Operations using the Bindplane agent.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Windows 2016 or later or Linux host with `systemd`
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the F5 BIG-IP LTM device (TMSH or web UI)



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

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

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** Using the correct regional endpoint is required for data residency compliance. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for more information.

## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. On Linux, the default path is `/opt/observiq-otel-collector/config.yaml`. On Windows, it's in the installation directory.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           # UDP syslog listener (RFC 5424 over UDP)
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: "/opt/observiq-otel-collector/ingestion-auth.json"
             customer_id: "<YOUR_CUSTOMER_ID>"
             endpoint: chronicle.googleapis.com
             log_type: "F5_BIGIP_LTM"
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/f5ltm:
               receivers: [udplog]
               exporters: [chronicle/chronicle_w_labels]
         

     * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
     * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
     * Replace `<YOUR_CUSTOMER_ID>` with the actual Customer ID from Step 2.
     * Update `/opt/observiq-otel-collector/ingestion-auth.json` to the path where the service account key file (Option 1) was saved in Step 1.

**Configuration notes:**

     * The `listen_address` is set to `0.0.0.0:514` to accept syslog from any source. Adjust if you need to restrict to specific interfaces.
     * UDP port 514 is the standard syslog port. If port 514 requires root privileges, you may use a port higher than 1024 (for example, `5514`) and adjust F5 configuration accordingly.
     * For **TCP** instead of UDP, create a `tcplog` receiver and set the F5 Remote High-Speed Log protocol to `tcp`.
  3. Save the file and exit the editor.




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            creds_file_path: "/opt/observiq-otel-collector/ingestion-auth.json"
            customer_id: "<YOUR_CUSTOMER_ID>"
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: "F5_BIGIP_LTM"
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure F5 BIG-IP LTM syslog forwarding

### Option A: Using TMSH (Command Line Interface)

#### Step 1: Create pool for syslog destination

  1. Connect to the F5 BIG-IP LTM device using SSH.
  2. Run the following commands:
         
         tmsh create ltm pool f5_syslog_pool members add { <BINDPLANE_IP>:514 } monitor gateway_icmp
         

     * Replace `<BINDPLANE_IP>` with the IP address of your Bindplane agent host.



#### Step 2: Create log destination

> 
>     tmsh create sys log-config destination remote-high-speed-log f5_hsl_dest protocol udp pool-name f5_syslog_pool
>     
>     tmsh create sys log-config destination remote-syslog f5_remote_syslog_dest format rfc5424 remote-high-speed-log f5_hsl_dest
>     

**Note:** The `format rfc5424` setting ensures proper parsing of structured syslog messages.

#### Step 3: Create log publisher

> 
>     tmsh create sys log-config publisher f5_log_publisher destinations add { f5_remote_syslog_dest }
>     

#### Step 4: Create request logging profile

> 
>     tmsh create ltm profile request-log f5_ltm_request_log \
>       request-log-pool f5_syslog_pool request-log-protocol mds-udp \
>       request-log-template 'event_source="request_logging",hostname="$BIGIP_HOSTNAME",client_ip="$CLIENT_IP",server_ip="$SERVER_IP",http_method="$HTTP_METHOD",http_uri="$HTTP_URI",http_host="${host}",virtual_name="$VIRTUAL_NAME",event_timestamp="$DATE_HTTP"' \
>       request-logging enabled \
>       response-log-pool f5_syslog_pool response-log-protocol mds-udp \
>       response-log-template 'event_source="response_logging",hostname="$BIGIP_HOSTNAME",client_ip="$CLIENT_IP",server_ip="$SERVER_IP",http_method="$HTTP_METHOD",http_uri="$HTTP_URI",http_host="${host}",virtual_name="$VIRTUAL_NAME",http_statcode="$HTTP_STATCODE",event_timestamp="$DATE_HTTP"' \
>       response-logging enabled
>     

**Note:** The `${host}` variable captures the HTTP Host header, which is essential for web security detections.

#### Step 5: Apply logging profile to virtual server

> 
>     tmsh modify ltm virtual <VIRTUAL_SERVER_NAME> profiles add { f5_ltm_request_log }
>     

  * Replace `<VIRTUAL_SERVER_NAME>` with the name of your virtual server.



#### Step 6: Save configuration

> 
>     tmsh save sys config
>     

### Option B: Using F5 Web UI (Configuration Utility)

#### Step 1: Create pool for syslog destination

  1. Sign in to the **F5 BIG-IP LTM** web interface.
  2. Go to **Local Traffic > Pools > Pool List**.
  3. Click **Create**.
  4. Provide the following configuration details: 
     * **Name** : Enter `f5_syslog_pool`.
     * **Health Monitors** : Select **gateway_icmp**.
  5. In the **Resources** section, under **New Members** : 
     * **Address** : Enter the Bindplane agent IP address.
     * **Service Port** : Enter `514`.
  6. Click **Add**.
  7. Click **Finished**.



#### Step 2: Create remote high-speed log destination

  1. Go to **System > Logs > Configuration > Log Destinations**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter `f5_hsl_dest`.
     * **Type** : Select **Remote High-Speed Log**.
     * **Protocol** : Select **UDP**.
     * **Pool Name** : Select `f5_syslog_pool`.
  4. Click **Finished**.



#### Step 3: Create remote syslog destination

  1. Go to **System > Logs > Configuration > Log Destinations**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter `f5_remote_syslog_dest`.
     * **Type** : Select **Remote Syslog**.
     * **Syslog Format** : Select **RFC 5424**.
     * **Remote High-Speed Log** : Select `f5_hsl_dest`.
  4. Click **Finished**.



#### Step 4: Create log publisher

  1. Go to **System > Logs > Configuration > Log Publishers**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter `f5_log_publisher`.
     * **Destinations** : Move `f5_remote_syslog_dest` from **Available** to **Selected**.
  4. Click **Finished**.



#### Step 5: Create request logging profile

  1. Go to **Local Traffic > Profiles > Other > Request Logging**.
  2. Click **Create**.
  3. Provide the following configuration details: 
     * **Name** : Enter `f5_ltm_request_log`.
     * **Parent Profile** : Select `request-log`.
  4. Under **Request Settings** :

     * **Request Logging** : Select **Enabled**.
     * **Request Log Protocol** : Select **mds-udp**.
     * **Request Log Pool** : Select `f5_syslog_pool`.
     * **Request Log Template** : Enter the following:
           
           event_source="request_logging",hostname="$BIGIP_HOSTNAME",client_ip="$CLIENT_IP",server_ip="$SERVER_IP",http_method="$HTTP_METHOD",http_uri="$HTTP_URI",http_host="${host}",virtual_name="$VIRTUAL_NAME",event_timestamp="$DATE_HTTP"
           

  5. Under **Response Settings** :

     * **Response Logging** : Select **Enabled**.
     * **Response Log Protocol** : Select **mds-udp**.
     * **Response Log Pool** : Select `f5_syslog_pool`.
     * **Response Log Template** : Enter the following:
           
           event_source="response_logging",hostname="$BIGIP_HOSTNAME",client_ip="$CLIENT_IP",server_ip="$SERVER_IP",http_method="$HTTP_METHOD",http_uri="$HTTP_URI",http_host="${host}",virtual_name="$VIRTUAL_NAME",http_statcode="$HTTP_STATCODE",event_timestamp="$DATE_HTTP"
           

  6. Click **Finished**.




#### Step 6: Apply request logging profile to virtual server

  1. Go to **Local Traffic > Virtual Servers > Virtual Server List**.
  2. Click the virtual server name to open its **Properties** tab.
  3. From the **Configuration** list, select **Advanced**.
  4. From the **Request Logging Profile** list, select `f5_ltm_request_log`.
  5. Click **Update**.

**Note:** Don't change the virtual server's **Default Pool**. `f5_syslog_pool` is the HSL log destination (already wired to the Request Logging Profile in Step 5 through `request-log-pool`); the Default Pool must remain the application backend pool that balances production traffic.

## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`blade_field` | `about.resource.attribute.labels` | Merged  
`client_field` | `about.resource.attribute.labels` | Merged  
`device_field` | `about.resource.attribute.labels` | Merged  
`node_field` | `about.resource.attribute.labels` | Merged  
`path_field` | `about.resource.attribute.labels` | Merged  
`pool_member_field` | `about.resource.attribute.labels` | Merged  
`query_field` | `about.resource.attribute.labels` | Merged  
`snat_field` | `about.resource.attribute.labels` | Merged  
`vs_field` | `about.resource.attribute.labels` | Merged  
`vs_name_field` | `about.resource.attribute.labels` | Merged  
`Access_Profile_field` | `additional.fields` | Merged  
`Listener_field` | `additional.fields` | Merged  
`captcha_result_field` | `additional.fields` | Merged  
`errdefs_msgno_field` | `additional.fields` | Merged  
`false_positive_field` | `additional.fields` | Merged  
`http_uri_label` | `additional.fields` | Merged  
`partition_name_field` | `additional.fields` | Merged  
`process` | `additional.fields` | Mapped: `sshd` → `ssh_server_version_label`, `sshd` → `ssh_client_version_label`  
`query_string_label` | `additional.fields` | Merged  
`request_status_label` | `additional.fields` | Merged  
`sig_ids_field` | `additional.fields` | Merged  
`sig_names_field` | `additional.fields` | Merged  
`sig_set_names_field` | `additional.fields` | Merged  
`ssh_client_version_label` | `additional.fields` | Merged  
`ssh_server_version_label` | `additional.fields` | Merged  
`staged_sig_ids_field` | `additional.fields` | Merged  
`staged_sig_names_field` | `additional.fields` | Merged  
`staged_sig_set_names_field` | `additional.fields` | Merged  
`staged_threat_campaign_names_field` | `additional.fields` | Merged  
`support_id_label` | `additional.fields` | Merged  
`threat_campaign_names_field` | `additional.fields` | Merged  
`action_data` | `extensions.auth.type` | Mapped: `session opened` → `AUTHTYPE_UNSPECIFIED`, `session closed` → `AUTHTYPE_UNSPECIFIED`  
`loglevel` | `extensions.auth.type` | Mapped: `warning` → `VPN`  
`process` | `extensions.auth.type` | Mapped: `apmd` → `VPN`, `httpd` → `AUTHTYPE_UNSPECIFIED`, `sshd` → `AUTHTYPE_UNSPECIFIED`  
`i_ip` | `intermediary.asset.ip` | Merged  
`dvc` | `intermediary.hostname` | Directly mapped  
`dvc_ip` | `intermediary.ip` | Merged  
`i_ip` | `intermediary.ip` | Merged  
`i_port` | `intermediary.port` | Renamed/mapped  
`action_data` | `metadata.description` | Directly mapped  
`desc` | `metadata.description` | Directly mapped  
`description` | `metadata.description` | Directly mapped  
`process` | `metadata.description` | Directly mapped  
`timestamp` | `metadata.event_timestamp` | Parsed as `dd MMM yyyy HH:mm:ss`  
`ts` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`event_type` | `metadata.event_type` | Directly mapped  
`product_event_type` | `metadata.product_event_type` | Directly mapped  
`producteventtype` | `metadata.product_event_type` | Directly mapped  
`eventId` | `metadata.product_log_id` | Directly mapped  
`protocol` | `network.application_protocol` | Mapped: `(?i)ssh` → `SSH`, `(?i)HTTPS` → `HTTPS`  
`request` | `network.application_protocol` | Mapped: `(?i)(http)` → `HTTP`  
`http_method` | `network.http.method` | Directly mapped  
`method` | `network.http.method` | Directly mapped  
`method_req` | `network.http.method` | Directly mapped  
`header.User-Agent` | `network.http.parsed_user_agent` | Renamed/mapped  
`header.Referer` | `network.http.referral_url` | Directly mapped  
`url_string` | `network.http.referral_url` | Directly mapped  
`resp_code` | `network.http.response_code` | Renamed/mapped  
`response_code` | `network.http.response_code` | Directly mapped  
`header.User-Agent` | `network.http.user_agent` | Directly mapped  
`user_agent` | `network.http.user_agent` | Directly mapped  
`ip_protocol_out` | `network.ip_protocol` | Directly mapped  
`process` | `network.ip_protocol` | Mapped values (five total, for example, `tmm` → `TCP`, `httpd` → `TCP`, `sshd` → `TCP`)  
`byte_code` | `network.received_bytes` | Directly mapped  
`bytes_in` | `network.received_bytes` | Directly mapped  
`process` | `network.received_bytes` | Mapped: `logger` → `uinteger`  
`bytes_out` | `network.sent_bytes` | Directly mapped  
`Session_ID` | `network.session_id` | Directly mapped  
`session_id` | `network.session_id` | Directly mapped  
`cipher` | `network.tls.cipher` | Directly mapped  
`cipher_name` | `network.tls.cipher` | Directly mapped  
`ssl_cipher` | `network.tls.cipher` | Directly mapped  
`sni_host` | `network.tls.client.server_name` | Directly mapped  
`tls_version` | `network.tls.version` | Directly mapped  
`ssl_version` | `network.tls.version_protocol` | Directly mapped  
`tlsproto` | `network.tls.version_protocol` | Mapped: `HTTP/1.1` → `HTTP`  
`principalHost` | `observer.hostname` | Directly mapped  
`principalIp` | `observer.ip` | Merged  
`process` | `observer.ip` | Mapped: `tmm` → `principalIp`, `sshd` → `principalIp`  
`label` | `principal.asset.attribute.labels` | Merged  
`process` | `principal.asset.attribute.labels` | Mapped: `tmm` → `label`  
`device` | `principal.asset.hostname` | Directly mapped  
`dvc` | `principal.asset.hostname` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`principalHost` | `principal.asset.hostname` | Directly mapped  
`principal_ip` | `principal.asset.hostname` | Directly mapped  
`unit_host` | `principal.asset.hostname` | Directly mapped  
`Client_IP` | `principal.asset.ip` | Merged  
`client_ip` | `principal.asset.ip` | Merged  
`ip1` | `principal.asset.ip` | Merged  
`ip_client` | `principal.asset.ip` | Merged  
`loglevel` | `principal.asset.ip` | Mapped: `warning` → `src_ip`  
`manage_ip_addr` | `principal.asset.ip` | Merged  
`p_ip` | `principal.asset.ip` | Merged  
`principalIp` | `principal.asset.ip` | Merged  
`principal_ip` | `principal.asset.ip` | Merged  
`process` | `principal.asset.ip` | Mapped values (10 total, for example, `apmd` → `src_ip`, `tmm` → `p_ip`, `tmm` → `src_ip`)  
`src_ip` | `principal.asset.ip` | Mapped: `ip` → `x_ip`  
`x_ip` | `principal.asset.ip` | Merged  
`device` | `principal.hostname` | Directly mapped  
`dvc` | `principal.hostname` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`principalHost` | `principal.hostname` | Directly mapped  
`principal_ip` | `principal.hostname` | Directly mapped  
`unit_host` | `principal.hostname` | Directly mapped  
`Client_IP` | `principal.ip` | Merged  
`client_ip` | `principal.ip` | Merged  
`ip1` | `principal.ip` | Merged  
`ip_client` | `principal.ip` | Merged  
`loglevel` | `principal.ip` | Mapped: `warning` → `src_ip`  
`manage_ip_addr` | `principal.ip` | Merged  
`p_ip` | `principal.ip` | Merged  
`principalIp` | `principal.ip` | Merged  
`principal_ip` | `principal.ip` | Merged  
`process` | `principal.ip` | Mapped values (10 total, for example, `apmd` → `src_ip`, `tmm` → `p_ip`, `tmm` → `src_ip`)  
`src_ip` | `principal.ip` | Mapped: `ip` → `x_ip`  
`x_ip` | `principal.ip` | Merged  
`Country` | `principal.location.country_or_region` | Directly mapped  
`geoCountry` | `principal.location.country_or_region` | Directly mapped  
`State` | `principal.location.state` | Directly mapped  
`geoState` | `principal.location.state` | Directly mapped  
`snat_ip` | `principal.nat_ip` | Merged  
`snat_port` | `principal.nat_port` | Directly mapped  
`client_port` | `principal.port` | Directly mapped  
`p_port` | `principal.port` | Renamed/mapped  
`prin_port` | `principal.port` | Renamed/mapped  
`principalPort` | `principal.port` | Renamed/mapped  
`source_parent_process_id` | `principal.process.parent_process.pid` | Directly mapped  
`source_process_id` | `principal.process.pid` | Directly mapped  
`bank_label` | `principal.resource.attribute.labels` | Merged  
`dgl_count_label` | `principal.resource.attribute.labels` | Merged  
`dgl_value_label` | `principal.resource.attribute.labels` | Merged  
`error_reason_label` | `principal.resource.attribute.labels` | Merged  
`function_id_label` | `principal.resource.attribute.labels` | Merged  
`information_label` | `principal.resource.attribute.labels` | Merged  
`operation_label` | `principal.resource.attribute.labels` | Merged  
`process` | `principal.resource.attribute.labels` | Mapped values (11 total, for example, `tmm` → `bank_label`, `tmm` → `service_label`, `tmm` → `operat...)  
`reason_code_label` | `principal.resource.attribute.labels` | Merged  
`request_label` | `principal.resource.attribute.labels` | Merged  
`service_label` | `principal.resource.attribute.labels` | Merged  
`ssl_function_label` | `principal.resource.attribute.labels` | Merged  
`url` | `principal.url` | Directly mapped  
`process` | `principal.user.attribute.roles` | Mapped: `rest(pam_audit)` → `role`  
`role` | `principal.user.attribute.roles` | Merged  
`userRole` | `principal.user.attribute.roles` | Mapped: `(?i)Administrator` → `role`  
`header.X-HackerOne` | `principal.user.userid` | Directly mapped  
`principalId` | `principal.user.userid` | Directly mapped  
`userId` | `principal.user.userid` | Directly mapped  
`sr_label` | `security_result.about.resource.attribute.labels` | Merged  
`action` | `security_result.action` | Merged  
`process` | `security_result.action` | Mapped: `httpd` → `sec_action`  
`sec_action` | `security_result.action` | Merged  
`action_details` | `security_result.action_details` | Directly mapped  
`security_category` | `security_result.category_details` | Merged  
`description` | `security_result.description` | Directly mapped  
`msg1` | `security_result.description` | Directly mapped  
`reason` | `security_result.description` | Directly mapped  
`detection_policy_name` | `security_result.detection_fields` | Merged  
`event_source_label` | `security_result.detection_fields` | Merged  
`module_label` | `security_result.detection_fields` | Merged  
`req_status_label` | `security_result.detection_fields` | Merged  
`status1_label` | `security_result.detection_fields` | Merged  
`violations_field` | `security_result.detection_fields` | Merged  
`policy` | `security_result.rule_name` | Directly mapped  
`rule_name` | `security_result.rule_name` | Directly mapped  
`loglevel` | `security_result.severity` | Directly mapped  
`severity` | `security_result.severity` | Mapped: `(?i)(Info/Informational)` → `INFORMATIONAL`, `(?i)Error` → `ERROR`, `(?i)Warning` →...  
`auth_status` | `security_result.summary` | Directly mapped  
`loglevel` | `security_result.summary` | Mapped: `warning` → `Authentication failure`  
`process` | `security_result.summary` | Mapped: `apmd` → `Authentication failure`  
`status` | `security_result.summary` | Directly mapped  
`summary` | `security_result.summary` | Directly mapped  
`process` | `target.application` | Directly mapped  
`dvc` | `target.asset.hostname` | Directly mapped  
`host` | `target.asset.hostname` | Directly mapped  
`http_host` | `target.asset.hostname` | Directly mapped  
`Virtual_IP` | `target.asset.ip` | Merged  
`process` | `target.asset.ip` | Mapped: `tmm` → `t_ip`  
`server_ip` | `target.asset.ip` | Merged  
`t_ip` | `target.asset.ip` | Merged  
`targetIp` | `target.asset.ip` | Directly mapped  
`target_ip` | `target.asset.ip` | Merged  
`vip` | `target.asset.ip` | Merged  
`File` | `target.file.full_path` | Directly mapped  
`targetFile` | `target.file.full_path` | Directly mapped  
`dvc` | `target.hostname` | Directly mapped  
`host` | `target.hostname` | Directly mapped  
`http_host` | `target.hostname` | Directly mapped  
`Virtual_IP` | `target.ip` | Merged  
`process` | `target.ip` | Mapped: `tmm` → `t_ip`  
`server_ip` | `target.ip` | Merged  
`t_ip` | `target.ip` | Merged  
`target_ip` | `target.ip` | Merged  
`vip` | `target.ip` | Merged  
`server_port` | `target.port` | Directly mapped  
`t_port` | `target.port` | Renamed/mapped  
`targetPort` | `target.port` | Renamed/mapped  
`action_data` | `target.process.command_line` | Directly mapped  
`cmd_data` | `target.process.command_line` | Directly mapped  
`command_line` | `target.process.command_line` | Directly mapped  
`pid` | `target.process.pid` | Directly mapped  
`virtual_name` | `target.resource.name` | Directly mapped  
`path` | `target.url` | Directly mapped  
`request_path` | `target.url` | Directly mapped  
`uri` | `target.url` | Directly mapped  
`uri_path` | `target.url` | Directly mapped  
`uri_query` | `target.url` | Directly mapped  
`process` | `target.user.attribute.roles` | Mapped: `httpd` → `role`  
`role` | `target.user.attribute.roles` | Merged  
`user` | `target.user.userid` | Directly mapped  
`user2` | `target.user.userid` | Directly mapped  
`userId` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `VPN`  
N/A | `metadata.product_name` | Constant: `BIG-IP Local Traffic Manager (LTM)`  
N/A | `metadata.vendor_name` | Constant: `F5`  
N/A | `network.application_protocol` | Constant: `HTTP`  
N/A | `network.ip_protocol` | Constant: `TCP`  
N/A | `network.tls.version_protocol` | Constant: `HTTP`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `security_result.summary` | Constant: `Authentication failure`  
`syslog_priority` | `event.idm.read_only_udm.security_result.priority_details` | Mapped from changelog  
`target_path` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog  
`client_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`client_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`response_code` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`backend_ip` | `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`backend_port` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`ssl_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` | Mapped from changelog  
`ssh_server_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ssh_client_version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`prin_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`process` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`eventId` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`p_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`p_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`p_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`i_ip` | `event.idm.read_only_udm.intermediary.ip` | Mapped from changelog  
`i_ip` | `event.idm.read_only_udm.intermediary.asset.ip` | Mapped from changelog  
`i_port` | `event.idm.read_only_udm.intermediary.port` | Mapped from changelog  
`t_ip` | `event.idm.read_only_udm.target.ip` | Mapped from changelog  
`t_ip` | `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`t_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`src_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`client_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`client_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`'tls_version'` | `event.idm.read_only_udm.network.tls.version` | Mapped from changelog  
`cipher` | `event.idm.read_only_udm.network.tls.cipher` | Mapped from changelog  
`request_path` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.target.process.pid` | Mapped from changelog  
`cmd_data` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`module` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`src_ip" and "src_port" from "reason` | `principal.ip` | Mapped from changelog  
`bank", "service", "operation", and "information` | `principal.resource.attribute.labels` | Mapped from changelog  
`vs_name", "path", "query", "node", "pool_member", "vs", "device", "blade", "client", and "snat` | `about.resource.attribute.labels` | Mapped from changelog  
`support_id", "query_string", and "request_status` | `additional.fields` | Mapped from changelog  
`dest_ip` | `target_ip` | Mapped from changelog  
`dest_port` | `targetPort` | Mapped from changelog  
`src_port` | `principalPort` | Mapped from changelog  
`ip_client" and "manage_ip_addr` | `principal.ip` | Mapped from changelog  
`violations", "policy_name" and "req_status` | `security_result.detection_fields.` | Mapped from changelog  
`staged_threat_campaign_names","staged_sig_ids","threat_campaign_names","staged_sig_names","captcha_result","sig_set_names","staged_sig_set_names", "sig_ids", "sig_names","resp_code" and "false_positive` | `additional.fields` | Mapped from changelog  
`errdefs_msgno", "partition_name", "Listener", "Access_Profile` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-bigip-ltm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
