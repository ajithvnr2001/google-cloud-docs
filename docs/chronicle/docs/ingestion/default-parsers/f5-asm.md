---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-asm/
title: Collect F5 ASM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:03.987333+00:00
---

# Collect F5 ASM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-asm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 ASM logs

**Parser Version:** 33.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 Application Security Manager (ASM) logs to Google Security Operations using the Bindplane agent.

F5 BIG-IP ASM is a web application firewall (WAF) that generates syslog messages for HTTP request violations, policy enforcement actions, and security events. The parser supports multiple log formats (CEF, syslog, CSV, Splunk, JSON) and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the F5 BIG-IP appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to F5 BIG-IP tmsh



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         

The service should show as **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
            udplog:
                listen_address: "0.0.0.0:514"
        
        exporters:
            chronicle/f5_asm:
                compression: gzip
                creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
                customer_id: '<customer_id>'
                endpoint: malachiteingestion-pa.googleapis.com
                log_type: F5_ASM
                raw_log_field: body
        
        service:
            pipelines:
                logs/f5_asm_to_chronicle:
                    receivers:
                        - udplog
                    exporters:
                        - chronicle/f5_asm
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to ingestion authentication file: 
      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `endpoint`: Regional endpoint URL: 
      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for complete list



### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
    * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

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

      1. Press `Win+R`, type `services.msc`, and press Enter.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.
      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure syslog in F5 ASM

  1. Sign in to the **tmsh** instance by typing the following command:
         
         tmsh
         

  2. Edit syslog configuration using the following command:
         
         edit /sys syslog all-properties
         

  3. Syslog configuration opens in the `vi` text editor and appears similar to the following example:
         
         modify syslog {
             auth-priv-from notice
             auth-priv-to emerg
             cron-from warning
             cron-to emerg
             daemon-from notice
             daemon-to emerg
             description none
             include none
             iso-date disabled
             kern-from notice
             kern-to emerg
             mail-from notice
             mail-to emerg
             messages-from notice
             messages-to warning
             remote-servers none
             user-log-from notice
             user-log-to emerg
         }
         

  4. Replace the `include none` line with the following syslog filter:
         
         include `
             filter f_audit{
                 match(AUDIT);
             };
             destination d_syslog_server {
                 udp(\`<bindplane-ip>\` port (<bindplane-port>));
             };
             log {
                 source(s_syslog_pipe);
                 filter(f_audit);
                 destination(d_syslog_server);
             };
         `
         

  5. Replace `<bindplane-ip>` and `<bindplane-port>` with the actual IP address and port number configured for your Bindplane agent.

  6. Exit `vi` by typing the following key sequence:
         
         :wq!
         

  7. At the following prompt, type `y` to save the changes to the file:
         
         Save changes? (y/n/e)
         

  8. Save the configuration by typing the following command:
         
         save /sys config
         




## UDM mapping table

Field name | UDM  
---|---  
`/BAD_MSG/request-violations/violation[n]/actual_value_length` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/cookie/cookie_name` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/cookie/cookie_pattern` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/cookie/cookie_value` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/evasions[n]/blocking_mask` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/evasions[n]/buffer` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/evasions[n]/length` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/evasions[n]/offset` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/expected_value_length` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/extension` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/flg_disallowed_file_type` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/header/header_name` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/header/header_value` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/http_sanity_checks_status` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/http_sub_violation` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/http_sub_violation_status` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/method_code` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/method_violation_details` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/parameter_data/enforcement_level` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/parameter_data/name` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/parameter_data/value` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/post_len` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/query_len` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/qs_len` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/qs_len_limit` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/sig_data[n]/blocking_mask` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/sig_data[n]/kw_data/buffer` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/sig_data[n]/kw_data/length` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/sig_data[n]/kw_data/offset` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/sig_data[n]/sig_id` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/sig_data[n]/specific_desc` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/total_len` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/total_len_limit` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/uri_len` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/uri_len_limit` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/value_length_type` | `security_result.detection_fields`  
`/BAD_MSG/request-violations/violation[n]/wildcard_entity` | `security_result.detection_fields`  
`/BAD_MSG/response_violations/violation[n]/cfg_target` | `security_result.detection_fields`  
`/BAD_MSG/response_violations/violation[n]/leakage_type` | `security_result.detection_fields`  
`/BAD_MSG/response_violations/violation[n]/pattern_type` | `security_result.detection_fields`  
`/BAD_MSG/response_violations/violation[n]/response_code` | `security_result.detection_fields`  
`/BAD_MSG/response_violations/violation[n]/viol_index` | `security_result.detection_fields`  
`/BAD_MSG/response_violations/violation[n]/viol_name` | `security_result.detection_fields`  
`/BAD_MSG/violation_masks/alarm` | `security_result.detection_fields`  
`/BAD_MSG/violation_masks/block` | `security_result.detection_fields`  
`/BAD_MSG/violation_masks/learn` | `security_result.detection_fields`  
`/BAD_MSG/violation_masks/staging` | `security_result.detection_fields`  
`/s-Envelope/s-Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`/s-Envelope/s-Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`/s-Envelope/s-Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`/s-Envelope/s-Body/inquireTransaction/user` | `security_result.detection_fields`  
`/s-Envelope/s-Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`/s-Envelope/s-Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`/s-Envelope/s-Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`/s-Envelope/s-Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`/s-Envelope/s-Body/processTransaction/accessCode` | `security_result.detection_fields`  
`/s-Envelope/s-Body/processTransaction/companyId` | `security_result.detection_fields`  
`/s-Envelope/s-Body/processTransaction/txnPin` | `security_result.detection_fields`  
`/s-Envelope/s-Body/processTransaction/user` | `security_result.detection_fields`  
`/s-Envelope/s-Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`/s-Envelope/s-Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`/s-Envelope/s-Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`/s-Envelope/s-Body/validateAccountNumber/user` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/inquireTransaction/user` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/processTransaction/accessCode` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/processTransaction/companyId` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/processTransaction/txnPin` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/processTransaction/user` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`/soap-Envelope/soap-Body/validateAccountNumber/user` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/inquireTransaction/user` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/processTransaction/accessCode` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/processTransaction/companyId` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/processTransaction/txnPin` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/processTransaction/user` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`/soap:Envelope/soap:Body/validateAccountNumber/user` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/inquireTransaction/user` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/processTransaction/accessCode` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/processTransaction/companyId` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/processTransaction/txnPin` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/processTransaction/user` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`/soapenv-Envelope/soapenv-Body/validateAccountNumber/user` | `security_result.detection_fields`  
`_csrfToken` | `security_result.detection_fields`  
`Accept` | `additional.fields`  
`accept` | `additional.fields`  
`Accept-Charset` | `additional.fields`  
`Accept-Encoding` | `additional.fields`  
`accept-encoding` | `additional.fields`  
`acceptEncoding` | `security_result.detection_fields`  
`Accept-Language` | `additional.fields`  
`accept-language` | `additional.fields`  
`acceptLanguage` | `security_result.detection_fields`  
`Access-Control-Request-Headers` | `security_result.detection_fields`  
`Access-Control-Request-Method` | `network.http.method`  
`AccountSid` | `target.resource.product_object_id`  
`AccountType` | `target.user.attribute.roles.description`  
`act` | `security_result.action`   
`security_result.action_details`  
`act1` | `security_result.action`  
`Action` | `additional.fields`  
`action` | `security_result.action`   
`security_result.action_details`  
`action_summary` | `security_result.detection_fields`  
`additional_bot_signatures` | `security_result.detection_fields`  
`actual_mitigation_action` | `security_result.detection_fields`  
`actual_mitigation_action_reason` | `security_result.detection_fields`  
`alert_level` | `security_result.severity`  
`anomalies` | `additional.fields`  
`anomaly_categories` | `additional.fields`  
`apache_module` | `security_result.detection_fields`  
`ApiVersion` | `security_result.detection_fields`  
`App-Name` | `target.application`  
`Application` | `target.application`  
`Application-Type` | `security_result.detection_fields`  
`application_display_name` | `additional.fields`  
`application_version` | `security_result.detection_fields`  
`appID` | `security_result.detection_fields`  
`app_protocol` | `network.application_protocol`  
`app-version` | `security_result.detection_fields`  
`attack_type` | `metadata.description`  
`attacktype` | `security_result.category_details`  
`audit_component` | `additional.fields`  
`auth` | `principal.user.userid`  
`authCode` | `security_result.detection_fields`  
`auth_level` | `principal.user.attribute.roles.name`  
`auth_status` | `security_result.action`   
`security_result.summary`  
`batchKey` | `security_result.detection_fields`  
`batchNo` | `security_result.detection_fields`  
`BEAuthenticator` | `security_result.detection_fields`  
`bigip_mgmt_ip` | `intermediary.ip`  
`bigip_mgmt_ip2` | `intermediary.ip`  
`bill.isRecurring` | `security_result.detection_fields`  
`bill.productId` | `security_result.detection_fields`  
`blocking_exception_reason` | `security_result.detection_fields`  
`bot_name` | `additional.fields`  
`bot_signature` | `additional.fields`  
`bot_signature_category` | `additional.fields`  
`browser_actual_verification_action` | `additional.fields`  
`browser_configured_verification_action` | `additional.fields`  
`browser_verification_status` | `security_result.detection_fields`  
`bundle-version` | `additional.fields`  
`bytes_in` | `network.received_bytes`  
`bytes_out` | `network.sent_bytes`  
`c6a1` | `intermediary.ip`   
Condition:   
`[c6a1Label] == "device_address"`  
`c6a2` | `principal.ip`   
`principal.asset.ip`   
Condition:   
`[c6a2Label] == "source_address"`  
`c6a3` | `target.ip`   
`target.asset.ip`   
Condition:   
`[c6a3Label] == "destination_address"`  
`c6a4` | `security_result.about.ip`   
`security_result.about.asset.ip`   
Condition:   
`[c6a4Label] == "ip_address_intelligence"`  
`Cache-Control` | `additional.fields`  
`captcha_result` | `security_result.detection_fields`  
`captcha_status` | `security_result.detection_fields`  
`category` | `security_result.category_details`  
`cdn-loop` | `security_result.detection_fields`  
`CF-Connecting-IP` | `principal.ip`   
`principal.asset.ip`  
`cf-cert-presented` | `principal.asset.attribute.labels`  
`cf-cert-revoked` | `principal.asset.attribute.labels`  
`cf-cert-verified` | `principal.asset.attribute.labels`  
`cf-ipcity` | `principal.location.city`  
`CF-IPCountry` | `principal.location.country_or_region`  
`cf-ipcountry` | `principal.location.country_or_region`  
`cf-ipcontinent` | `principal.asset.attribute.labels`  
`cf-iplatitude` | `principal.location.region_coordinates.latitude`  
`cf-iplongitude` | `principal.location.region_coordinates.longitude`  
`cf-ipmetro-code` | `principal.asset.attribute.labels`  
`cf-ipostal-code` | `principal.asset.attribute.labels`  
`cf-iregion` | `principal.location.state`  
`cf-iregion-code` | `principal.asset.attribute.labels`  
`cf-itimezone` | `principal.asset.attribute.labels`  
`cf-ray` | `principal.asset.attribute.labels`  
`CF-Visitor` | `security_result.detection_fields`  
`CF-Visitor.scheme` | `principal.asset.attribute.labels`  
`challenge_failure_reason` | `additional.fields`  
`Channel` | `security_result.detection_fields`  
`channel` | `security_result.detection_fields`  
`Check-Id` | `additional.fields`  
`childTableRef` | `security_result.detection_fields`  
`CIPHER` | `network.tls.cipher`  
`city` | `principal.location.city`  
`class` | `additional.fields`  
`classification_reason` | `security_result.detection_fields`  
`clearGadgetId` | `security_result.detection_fields`  
`client-request-id` | `additional.fields`  
`client_id` | `security_result.detection_fields`  
`client_ip` | `principal.ip`  
`client_ip_geo_location` | `principal.location.country_or_region`  
`client_port` | `principal.port`  
`client_request_uri` | `target.url`  
`client_type` | `additional.fields`  
`Client-Version` | `security_result.detection_fields`  
`cmd_data` | `principal.process.command_line`  
`cn2 and cn2label` | `security_result.detection_fields`  
`cn3` | `principal.asset_id`   
Condition:   
`[cn3Label] == "device_id"`   
Otherwise:   
`security_result.detection_fields`  
`cn4 and cn4label` | `additional.fields`   
Condition:   
`[cs4label] == "whitelistData"`  
`cn5 and cn5label` | `additional.fields`  
`collected_time` | `metadata.collected_timestamp`  
`component` | `additional.fields`  
`COMPRESSION` | `security_result.detection_fields`  
`configured_mitigation_action` | `security_result.detection_fields`  
`configured_mitigation_action_reason` | `security_result.detection_fields`  
`configuration_date_time` | `security_result.detection_fields`  
`Connection` | `additional.fields`  
`connection` | `additional.fields`  
`contactNo` | `principal.user.phone_numbers`  
`Content-Length` | `additional.fields`  
`content-length` | `additional.fields`  
`Content-Type` | `additional.fields`  
`content-type` | `additional.fields`  
`context_name` | `additional.fields`  
`context_type` | `additional.fields`  
`contextPath` | `security_result.detection_fields`  
`Correlation-Id` | `security_result.detection_fields`  
`country` | `principal.location.country_or_region`  
`cs1` | `security_result.rule_id`  
`cs2` | `security_result.summary`   
Condition:   
`[cs2Label] == "reason"`   
Otherwise:   
`security_result.detection_fields`  
`cs3` | `security_result.detection_fields`  
`cs4 and cs4label` | `additional.fields`  
`cs5` | `principal.ip`   
`principal.asset.ip`  
`currency` | `security_result.detection_fields`  
`currency_type` | `security_result.detection_fields`  
`current_monitor_state_1` | `security_result.detection_fields`  
`current_monitor_state_2` | `security_result.detection_fields`  
`currentFormName` | `security_result.detection_fields`  
`custMobile` | `security_result.detection_fields`  
`data.bits` | `network.sent_bytes`  
`data.name` | `network.tls.cipher`  
`data.sessionid` | `network.session_id`  
`data.version` | `network.tls.version`  
`data_mwh_requestId` | `security_result.detection_fields`  
`data_renegotiation` | `security_result.detection_fields`  
`datosReto` | `security_result.detection_fields`  
`DATE` | `metadata.event_timestamp`  
`date_time` | `metadata.event_timestamp`  
`dependentInfo.DependentRel2Name` | `security_result.detection_fields`  
`dependentInfo.MasterObjectId` | `security_result.detection_fields`  
`dependentInfo.MasterObjectTableRef` | `security_result.detection_fields`  
`dependentInfo.RelationshipTag` | `security_result.detection_fields`  
`desc` | `security_result.description`  
`description` | `metadata.description`  
`DEST_IP` | `target.ip`  
`dest_ip` | `target.ip`  
`DEST_PORT` | `target.port`  
`dest_port` | `target.port`  
`DeviceBrand` | `principal.asset.hardware.manufacturer` (accepts only strings)   
`principal.asset.attribute.labels` (is used when DeviceBrand contains a integer instead of a string)  
`device.app_signature` | `principal.asset.attribute.labels`  
`device.app_version` | `principal.asset.platform_software.platform_version`  
`device_blade` | `intermediary.asset.attribute.labels`  
`device.build_number` | `principal.asset.attribute.labels`  
`device.device_id` | `principal.asset_id`  
`device_id` | `principal.asset_id`  
`device_id_action` | `security_result.detection_fields`  
`device_id_status` | `security_result.detection_fields`  
`device.manufacturer` | `principal.asset.hardware.manufacturer`  
`DeviceModel` | `principal.asset.hardware.model`  
`device.model` | `principal.asset.hardware.model`  
`DeviceName` | `principal.asset.attribute.labels`  
`DeviceOsFamily` | `principal.asset.platform_software.platform`  
`device.os_version` | `principal.platform_version`  
`DeviceOsVersion` | `principal.platform_version`  
`device.platform` | `principal.asset.platform_software.platform`  
`device_product` | `additional.fields`  
`device.sdk_int` | `principal.asset.attribute.labels`  
`DeviceScreenDensity` | `principal.asset.attribute.labels`  
`DeviceScreenH` | `principal.asset.attribute.labels`  
`DeviceScreenW` | `principal.asset.attribute.labels`  
`DeviceSerial` | `principal.asset.hardware.serial_number`  
`deviceSerialNo` | `principal.asset.hardware.serial_number`  
`DeviceUnique` | `principal.asset.product_object_id`  
`DeviceVendorId` | `principal.asset.attribute.labels`  
`device_version` | `metadata.product_version`  
`dimensioneLista` | `security_result.detection_fields`  
`DNT` | `security_result.detection_fields`  
`dos_attack_detection_mode` | `security_result.detection_fields`  
`dos_attack_event` | `security_result.detection_fields`  
`dos_attack_id` | `security_result.detection_fields`  
`dos_attack_latency` | `security_result.detection_fields`  
`dos_attack_name` | `security_result.detection_fields`  
`dos_attack_tps` | `security_result.detection_fields`  
`dos_baseline_latency` | `additional.fields`  
`dos_baseline_tps` | `additional.fields`  
`dos_dropped_requests_count` | `additional.fields`  
`dos_incoming_requests_count` | `additional.fields`  
`dos_mitigation_action` | `security_result.detection_fields`  
`dos_mitigation_reason` | `security_result.detection_fields`  
`dpt` | `target.port`  
`dhost` | `target.hostname`  
`dst` | `target.ip`  
`dvc` | `intermediary.ip`  
`dvchost` | `intermediary.hostname`  
`ECID-Context` | `security_result.detection_fields`  
`EE_I_ConsultaListadoProcesosCRM.codigoEntidad` | `security_result.detection_fields`  
`EE_I_VerificacionBeneficiario.codigoEntidad` | `security_result.detection_fields`  
`EE_I_VerificacionBeneficiario.ibanBeneficiario` | `security_result.detection_fields`  
`EE_I_VerificacionBeneficiario.ibanOrdenante` | `security_result.detection_fields`  
`EE_I_VerificacionBeneficiario.nombreBeneficiario` | `security_result.detection_fields`  
`email` | `principal.user.email_addresses`  
`end` | `additional.fields`  
`enforced_by` | `additional.fields`  
`environment` | `security_result.detection_fields`  
`errorcode` | `security_result.action`   
`security_result.rule_id`  
`error_message` | `security_result.summary`  
`errdefs_msg_name` | `additional.fields`  
`errdefs_msgno` | `additional.fields`  
`eventId` | `security_result.detection_fields`  
`event_time` | `metadata.event_timestamp`  
`expected_state` | `security_result.detection_fields`  
`expDate` | `security_result.detection_fields`  
`expires_in` | `security_result.detection_fields`  
`externalId` | `additional.fields`  
`f5_action` | `security_result.action`  
`f5_file` | `security_result.detection_fields`  
`f5_http_method` | `network.http.method`  
`f5_id` | `security_result.rule_id`  
`f5_line` | `security_result.detection_fields`  
`f5_name` | `additional.fields`  
`f5_path` | `security_result.detection_fields`  
`f5_rev` | `security_result.rule_version`  
`f5_rule_accuracy` | `security_result.detection_fields`  
`f5_rule_maturity` | `security_result.detection_fields`  
`f5_rule_version` | `security_result.detection_fields`  
`f5_signature` | `security_result.rule_name`  
`f5_sig_two` | `security_result.threat_id`  
`f5_tag` | `security_result.detection_fields`  
`f5_unique_id` | `network.session_id`  
`f5_uri` | `target.url`  
`f5_waf_msg` | `security_result.summary`  
`facility` | `additional.fields`  
`family_name` | `principal.user.last_name`  
`Fixed-Device-Id` | `security_result.detection_fields`  
`flavor` | `security_result.detection_fields`  
`folder` | `principal.file.full_path`  
`form_data` | `additional.fields`  
`From` | `principal.user.phone_numbers`  
`fragment` | `security_result.detection_fields`  
`geo_info` | `security_result.detection_fields`  
`geo_location` | `principal.location.country_or_region`  
`given_name` | `principal.user.first_name`  
`grant_type` | `security_result.detection_fields`  
`hashing_cf` | `security_result.detection_fields`  
`hashingCF` | `security_result.detection_fields`  
`headless_signatures` | `security_result.detection_fields`  
`header-one` | `additional.fields`  
`Host` | `target.hostname`   
`target.asset.hostname`  
`Hostname` | `principal.hostname`  
`http_class_name` | `security_result.detection_fields`  
`http_method` | `network.http.method`  
`http_protocol_indication` | `network.application_protocol`  
`http_request` | `network.http.referral_url`  
`http_version` | `network.application_protocol_version`  
`human_behaviour` | `security_result.detection_fields`  
`id` | `additional.fields`  
`idApp` | `target.resource.product_object_id`  
`identificativointermediariopa` | `security_result.detection_fields`  
`identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`idExterno` | `security_result.detection_fields`  
`idReto` | `security_result.detection_fields`  
`id_token` | `security_result.detection_fields`  
`I-Twilio-Idempotency-Token` | `security_result.detection_fields`  
`If-Modified-Since` | `security_result.detection_fields`  
`ifModifiedSince` | `security_result.detection_fields`  
`If-None-Match` | `security_result.detection_fields`  
`ifNoneMatch` | `security_result.detection_fields`  
`Image` | `target.file.full_path`  
`imei` | `security_result.detection_fields`  
`incap-client-ip` | `principal.ip`   
`principal.asset.ip`  
`inquiretransaction_accessCode` | `security_result.detection_fields`  
`inquiretransaction_companyId` | `security_result.detection_fields`  
`inquiretransaction_txnPin` | `security_result.detection_fields`  
`inquiretransaction_user` | `security_result.detection_fields`  
`internal_timestamp` | `metadata.event_timestamp`  
`intermediary_Ip` | `intermediary.ip`  
`intermediary_port` | `intermediary.port`  
`invoiceNo` | `security_result.detection_fields`  
`ip` | `security_result.about.ip`  
`IP_ADDRESS` | `principal.ip`   
`principal.asset.ip`  
`ip_addr_int` | `security_result.detection_fields`  
`ip_addr_intelli` | `security_result.detection_fields`  
`IP_CLIENT` | `principal.ip`  
`ip_client` | `principal.ip`  
`IpIntelligenceCategory` | `additional.fields`  
`ip_route_domain` | `principal.ip`   
`principal.asset.ip`  
`Ipv4AddressIntelligence` | `additional.fields`  
`irule` | `security_result.rule_name`  
`irule-version` | `security_result.rule_version`  
`isDccTransaction` | `security_result.detection_fields`  
`isDebugConnected` | `security_result.detection_fields`  
`isDebuggable` | `security_result.detection_fields`  
`isHooked` | `security_result.detection_fields`  
`isRunningInEmulator` | `security_result.detection_fields`  
`isSignedWithDebugKey` | `security_result.detection_fields`  
`isTamperedApk` | `security_result.detection_fields`  
`is_trunct` | `security_result.detection_fields`  
`isWrongCert` | `security_result.detection_fields`  
`jailbroken_or_rooted_device` | `security_result.detection_fields`  
`Keep-Alive` | `additional.fields`  
`lat` | `security_result.detection_fields`  
`lbCookie` | `security_result.detection_fields`  
`level` | `security_result.severity`  
`link` | `target.url`  
`listener` | `security_result.detection_fields`  
`lng` | `security_result.detection_fields`  
`Locale` | `security_result.detection_fields`  
`log_event` | `security_result.detection_fields`  
`manage_ip_addr` | `intermediary.ip`  
`management_ip_address` | `intermediary.ip`  
`management_ip_address_2` | `intermediary.ip`  
`max_amount` | `security_result.detection_fields`  
`member_with_port` | `security_result.detection_fields`  
`MessageSid` | `security_result.detection_fields`  
`MessageStatus` | `security_result.detection_fields`  
`meta_data.object_type` | `security_result.detection_fields`  
`METHOD` | `network.http.method`  
`method` | `network.http.method`  
`micro_service_hostname` | `additional.fields`  
`micro_service_matched_wildcard_url` | `additional.fields`  
`micro_service_name` | `additional.fields`  
`micro_service_type` | `additional.fields`  
`microservice` | `additional.fields`  
`min_amount` | `security_result.detection_fields`  
`mobile_application_name` | `security_result.detection_fields`  
`mobile_application_version` | `security_result.detection_fields`  
`mobile_debugger_enabled_device` | `security_result.detection_fields`  
`mobile_in_emulation_mode` | `security_result.detection_fields`  
`mobile_is_app` | `additional.fields`  
`mock` | `security_result.detection_fields`  
`model` | `principal.asset.hardware.model`  
`module` | `security_result.detection_fields`  
`monitor_details` | `security_result.detection_fields`  
`monitor_status` | `security_result.detection_fields`  
`monitor_type_1` | `security_result.detection_fields`  
`monitor_type_2` | `security_result.detection_fields`  
`msg` | `security_result.summary`  
`msgg` | `security_result.description`  
`msg_type` | `security_result.detection_fields`  
`Name` | `principal.user.user_display_name`  
`nativeDeviceId` | `principal.asset.product_object_id`  
`net.host.ip` | `principal.ip`   
`principal.asset.ip`  
`net.host.name` | `principal.hostname`   
`principal.asset.hostname`  
`net.host.port` | `principal.port`  
`net.peer.ip` | `principal.ip`   
`principal.asset.ip`  
`net.peer.name` | `target.hostname`   
`target.asset.hostname`  
`net.peer.port` | `target.port`  
`net.transport` | `network.ip_protocol`  
`network_http_method` | `network.http.method`  
`new_request_status` | `additional.fields`  
`nickname` | `security_result.detection_fields`  
`nii` | `security_result.detection_fields`  
`nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`num_of_attempts` | `additional.fields`  
`num_trans` | `security_result.detection_fields`  
`oauth_server` | `security_result.detection_fields`  
`Ocp-Apim-Subscription-Key` | `security_result.detection_fields`  
`ODJFS-AUTH-TOKEN` | `security_result.detection_fields`  
`Opcode` | `security_result.severity`  
`Origin` | `additional.fields`  
`origin` | `additional.fields`  
`originId` | `security_result.detection_fields`  
`os` | `principal.asset.platform_software.platform`  
`Os-Version` | `principal.platform_version`  
`os_name` | `security_result.detection_fields`  
`packageName` | `security_result.detection_fields`  
`partition` | `additional.fields`  
`partition_name` | `intermediary.asset.attribute.labels`  
`path` | `target.url`  
`pathContext` | `target.application`  
`paymentMode` | `security_result.detection_fields`  
`phost` | `security_result.detection_fields`  
`pideUsuario` | `security_result.detection_fields`  
`platform` | `principal.asset.platform_software.platform`  
`POLICY` | `security_result.rule_name`  
`policy` | `security_result.rule_name`  
`policy_apply_date` | `security_result.detection_fields`  
`policy_name` | `security_result.rule_name`  
`pool` | `security_result.detection_fields`  
`pool_name` | `security_result.detection_fields`  
`postalCode` | `principal.asset.attribute.labels`  
`post_len` | `security_result.detection_fields`  
`Pragma` | `additional.fields`  
`pragma` | `additional.fields`  
`previous_action` | `additional.fields`  
`previous_initiated_action` | `security_result.detection_fields`  
`previous_initiated_action_status` | `security_result.detection_fields`  
`previous_request_date_time` | `security_result.detection_fields`  
`previous_state` | `security_result.detection_fields`  
`previous_support_id` | `security_result.detection_fields`  
`principal_data.hostname` | `principal.hostname`   
`principal.asset.hostname`  
`principal_data.ip` | `principal.ip`   
`principal.asset.ip`  
`principal_ipv6` | `principal.ip`   
`principal.asset.ip`  
`principal_mail` | `principal.user.email_addresses`  
`Priority` | `additional.fields`  
`priority` | `additional.fields`  
`priority_value` | `additional.fields`  
`process` | `target.application`  
`process_id` | `principal.process.pid`  
`processtransaction_accessCode` | `security_result.detection_fields`  
`processtransaction_companyId` | `security_result.detection_fields`  
`processtransaction_txnPin` | `security_result.detection_fields`  
`processtransaction_user` | `security_result.detection_fields`  
`product_name` | `security_result.rule_type`  
`prod_id` | `metadata.product_log_id`  
`properties.branch` | `target.resource.attribute.labels`  
`properties.build` | `target.resource.attribute.labels`  
`properties.commit` | `target.resource.attribute.labels`  
`properties.deployment-environment` | `target.resource.attribute.labels`  
`properties.issueId` | `target.resource.attribute.labels`  
`properties.issueMatchesProjectContext` | `target.resource.attribute.labels`  
`properties.projectId` | `target.resource.attribute.labels`  
`properties.projectType` | `target.resource.attribute.labels`  
`properties.pullrequest` | `target.resource.attribute.labels`  
`properties.review` | `target.resource.attribute.labels`  
`properties.timeDelta` | `target.resource.attribute.labels`  
`PROTO` | `network.application_protocol`  
`protocol` | `network.application_protocol`  
`ProviderGuid` | `target.resource.id`  
`Proxy-Authorization` | `security_result.detection_fields`  
`Proxy-Connection` | `security_result.detection_fields`  
`proxy_errorcode` | `security_result.detection_fields`  
`proxy_id` | `security_result.rule_id`  
`proxy_message` | `security_result.detection_fields`  
`pushNotificationEnabled` | `security_result.detection_fields`  
`Qualys-Scan` | `security_result.detection_fields`  
`QUERY_STR` | `additional.fields`  
`query` | `security_result.detection_fields`  
`query_string` | `additional.fields`  
`query_str` | `security_result.detection_fields`  
`QUOTEDATA` | `security_result.detection_fields`  
`rangeDa` | `security_result.detection_fields`  
`rating` | `security_result.severity_details`  
`RawDlrDoneDate` | `security_result.detection_fields`  
`rawrequest` | `target.url`  
`received_bytes` | `network.received_bytes`  
`received_state` | `security_result.detection_fields`  
`Referer` | `network.http.referral_url`  
`referer` | `network.http.referral_url`  
`referrer` | `network.http.referral_url`  
`registerDevice` | `security_result.detection_fields`  
`related_pid` | `additional.fields`  
`remote_request_ip` | `principal.ip`   
`principal.asset.ip`  
`reputation` | `security_result.detection_fields`  
`REQ` | `additional.fields`  
`REQ_STATUS` | `security_result.action`  
`req_status` | `security_result.action`   
`security_result.action_details`   
`security_result.detection_fields`  
`req_status_value` | `security_result.action`   
`security_result.action_details`  
`request` | `target.url`  
`request_body_size` | `additional.fields`  
`Request-Context` | `security_result.detection_fields`  
`request_date_time` | `security_result.detection_fields`  
`Request-Id` | `security_result.detection_fields`  
`request_id` | `additional.fields`  
`requestClientApplication` | `network.http.user_agent`   
`network.http.parsed_user_agent`  
`requestMethod` | `network.http.method`  
`request_status` | `security_result.action`   
`security_result.action_details`  
`request_side` | `security_result.detection_fields`  
`resource_name` | `target.resource.name`  
`RESP_CODE` | `network.http.response_code`  
`resp` | `security_result.detection_fields`  
`resp_code` | `network.http.response_code`  
`response` | `security_result.summary`  
`response_code` | `network.http.response_code`  
`riskIT.deviceSignature.browser.userAgent` | `network.http.user_agent`   
`network.http.parsed_user_agent`  
`riskIT.deviceSignature.camera.autoFocus` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.flash` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.frontCamera` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.frontCameraSupportedFormats` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.frontCameraSupportedSizes` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.numberOfCameras` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.rearCamera` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.rearCameraSupportedFormats` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.camera.rearCameraSupportedSizes` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.collector` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.collectorVersion` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.extra.account` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.extra.securityPolicy` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.location.latitude` | `principal.location.region_coordinates.latitude`  
`riskIT.deviceSignature.location.longitude` | `principal.location.region_coordinates.longitude`  
`riskIT.deviceSignature.screen.displayId` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.screen.height` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.screen.orientation` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.screen.width` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.androidId` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.board` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.brand` | `principal.asset.hardware.manufacturer`  
`riskIT.deviceSignature.system.cpuAbi` | `principal.asset.hardware.cpu_platform`  
`riskIT.deviceSignature.system.debuggerAttached` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.deviceName` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.hardware` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.host` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.id` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.jailBroken` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.locale` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.model` | `principal.asset.hardware.model`  
`riskIT.deviceSignature.system.numberOfProcessors` | `principal.asset.hardware.cpu_number_cores`  
`riskIT.deviceSignature.system.osVersion` | `principal.platform_version`  
`riskIT.deviceSignature.system.platform` | `principal.asset.platform_software.platform`  
`riskIT.deviceSignature.system.processName` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.radio` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.tags` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.timeZone` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.totalDiskSpace` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.totalMemory` | `principal.asset.hardware.ram`  
`riskIT.deviceSignature.system.type` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.system.user` | `principal.user.userid`  
`riskIT.deviceSignature.telephony.carrierIsoCountryCode` | `principal.location.country_or_region`  
`riskIT.deviceSignature.telephony.carrierMobileCountryCode` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.carrierMobileNetworkCode` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.carrierName` | `principal.network.carrier_name`  
`riskIT.deviceSignature.telephony.cellIpAddress` | `principal.ip`   
`principal.asset.ip`  
`riskIT.deviceSignature.telephony.isRoamingNetwork` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.networkType` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.phoneType` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.simIsoCountryCode` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.simOperatorName` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.telephony.simSerialNumber` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.wifi.broadcastAddress` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.wifi.connected` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.wifi.gatewayAddress` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.wifi.macAddress` | `principal.mac`   
`principal.asset.mac`  
`riskIT.deviceSignature.wifi.netmaskAddress` | `principal.asset.attribute.labels`  
`riskIT.deviceSignature.wifi.userEnabled` | `principal.asset.attribute.labels`  
`riskIT.ipAddress` | `principal.ip`   
`principal.asset.ip`  
`rrn` | `security_result.detection_fields`  
`RS_VISITOR_ID` | `security_result.detection_fields`  
`rt` | `metadata.event_timestamp`  
`rule_name` | `security_result.rule_name`  
`rule_summary` | `security_result.summary`  
`rule_version` | `metadata.product_version`  
`save_payee` | `security_result.detection_fields`  
`schedule_frequency` | `security_result.detection_fields`  
`schedule_occurrence` | `security_result.detection_fields`  
`scope_details` | `additional.fields`  
`sec-ch-ua` | `security_result.detection_fields`  
`sec-ch-ua-mobile` | `additional.fields`  
`sec-ch-ua-platform` | `principal.asset.platform_software.platform`  
`sec-fetch-dest` | `additional.fields`  
`Sec-Fetch-Dest` | `additional.fields`  
`sec-fetch-mode` | `additional.fields`  
`Sec-Fetch-Mode` | `additional.fields`  
`sec-fetch-site` | `additional.fields`  
`Sec-Fetch-Site` | `additional.fields`  
`Sec-Fetch-Storage-Access` | `security_result.detection_fields`  
`sec-fetch-user` | `additional.fields`  
`Sec-Fetch-User` | `additional.fields`  
`Sec-Fetch-User` | `additional.fields`  
`sequence_id` | `additional.fields`  
`server_ip` | `target.ip`  
`server_port` | `target.port`  
`service_id` | `target.resource.product_object_id`  
`SESS_ID` | `network.session_id`  
`session_id` | `network.session_id`  
`session_status` | `security_result.detection_fields`  
`sessionDataId` | `security_result.detection_fields`  
`sessionDataKey` | `security_result.detection_fields`  
`Set-Cookie` | `security_result.detection_fields`  
`set_cookie` | `security_result.detection_fields`  
`severity` | `security_result.severity`  
`severity_number` | `security_result.severity`  
`sg_event_id` | `security_result.detection_fields`  
`sg_message_id` | `security_result.detection_fields`  
`sg_template_id` | `security_result.detection_fields`  
`sg_template_name` | `security_result.detection_fields`  
`Shield` | `security_result.detection_fields`  
`signature` | `security_result.detection_fields`  
`SIG_IDS` | `security_result.rule_id`  
`sig_cves` | `security_result.detection_fields`  
`sig_ids` | `security_result.detection_fields`  
`SIG_NAMES` | `security_result.rule_name`   
Condition:   
`[policy_name] == ""`  
`SmsSid` | `security_result.detection_fields`  
`SmsStatus` | `security_result.detection_fields`  
`snat_ip` | `principal.nat_ip`  
`snat_port` | `principal.nat_port`  
`SOAPAction` | `additional.fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/inquireTransaction/user` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/processTransaction/accessCode` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/processTransaction/companyId` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/processTransaction/txnData` | `additional.fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/processTransaction/txnPin` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/processTransaction/user` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`SOAP-ENV-Envelope/SOAP-ENV-Body/validateAccountNumber/user` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/inquireTransaction/user` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/processTransaction/accessCode` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/processTransaction/companyId` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/processTransaction/txnPin` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/processTransaction/user` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`soap-Envelope/soap-Body/validateAccountNumber/user` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/inquireTransaction/user` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/processTransaction/accessCode` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/processTransaction/companyId` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/processTransaction/txnPin` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/processTransaction/user` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`soap:Envelope/soap:Body/validateAccountNumber/user` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/inquireTransaction/accessCode` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/inquireTransaction/companyId` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/inquireTransaction/txnPin` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/inquireTransaction/user` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/dimensioneLista` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/identificativoIntermediarioPA` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/identificativoStazioneIntermediarioPA` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/nodoChiediListaPendentiRPT/rangeDa` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/processTransaction/accessCode` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/processTransaction/companyId` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/processTransaction/txnPin` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/processTransaction/user` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/validateAccountNumber/accessCode` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/validateAccountNumber/companyId` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/validateAccountNumber/txnPin` | `security_result.detection_fields`  
`soapenv-Envelope/soapenv-Body/validateAccountNumber/user` | `security_result.detection_fields`  
`sort_order` | `security_result.detection_fields`  
`SourceModuleName` | `target.resource.name`  
`SourceModuleType` | `observer.application`  
`source_host` | `principal.hostname`   
`principal.asset.hostname`  
`source_ip` | `principal.ip`   
`principal.asset.ip`  
`spt` | `principal.port`  
`src` | `principal.nat_ip`   
Condition:   
`[src] != [cs5]`  
`SRC_PORT` | `principal.port`  
`src_port` | `principal.port`  
`srcport` | `principal.port`  
`SSL_Client_Cert` | `security_result.detection_fields`  
`ssl_error_code` | `security_result.detection_fields`  
`ssl_routine` | `security_result.detection_fields`  
`staged_sig_cves` | `security_result.detection_fields`  
`staged_sig_ids` | `security_result.detection_fields`  
`staged_sig_names` | `security_result.detection_fields`  
`stagedThreatCampaignNames` | `additional.fields`  
`staged_threat_campaign_names` | `security_result.detection_fields`  
`start` | `additional.fields`  
`start_date` | `security_result.detection_fields`  
`state` | `principal.location.state`  
`status` | `security_result.summary`  
`SUB_VIOLATIONS` | `additional.fields`  
`sub_process` | `additional.fields`  
`sub_violates` | `security_result.summary`  
`sub_violations` | `security_result.detection_fields`  
`suid` | `principal.user.userid`  
`summary` | `security_result.summary`  
`SUPPORT_ID` | `additional.fields`  
`suser` | `principal.user.user_display_name`  
`tap_event_id` | `security_result.detection_fields`  
`tap_vid` | `security_result.detection_fields`  
`target_data.application` | `target.application`  
`target_data.ip` | `target.ip`   
`target.asset.ip`  
`target_url` | `target.url`  
`taxCode` | `security_result.detection_fields`  
`terminalId` | `security_result.detection_fields`  
`threat_campaign_names` | `security_result.detection_fields`  
`thread_id` | `security_result.detection_fields`  
`tls` | `network.tls.version`  
`tls_version` | `network.tls.version`  
`tmm_unit` | `security_result.detection_fields`  
`To` | `target.user.phone_numbers`  
`token` | `security_result.detection_fields`  
`t_port` | `target.port`  
`traceNo` | `security_result.detection_fields`  
`traceparent` | `security_result.detection_fields`  
`Transfer-Encoding` | `security_result.detection_fields`  
`transfer_type` | `security_result.detection_fields`  
`transType` | `security_result.detection_fields`  
`True-Client-IP` | `principal.ip`   
`principal.asset.i`  
`true-client-ip` | `principal.ip`   
`principal.asset.ip`  
`tty` | `additional.fields`  
`TYPE` | `security_result.category`   
`security_result.category_details`  
`type` | `metadata.product_event_type`  
`uniqueId` | `security_result.detection_fields`  
`Upgrade-Insecure-Requests` | `security_result.detection_fields`  
`URI` | `target.url`  
`url` | `principal.url`  
`user` | `principal.user.userid`  
`USER_AGENT` | `network.http.user_agent`   
`network.http.parsed_user_agent`  
`User-Agent` | `network.http.user_agent`   
`network.http.parsed_user_agent`  
`user_display_name` | `principal.user.user_display_name`  
`UserID` | `principal.user.userid`  
`user_id` | `principal.user.userid`  
`user_name` | `principal.user.userid`  
`userName` | `principal.user.email_addresses`  
`user_remarks` | `security_result.detection_fields`  
`user_type` | `principal.asset.attribute.labels`  
`usuarioBE` | `security_result.detection_fields`  
`uuid` | `security_result.detection_fields`  
`validateaccountnumber_accessCode` | `security_result.detection_fields`  
`validateaccountnumber_companyId` | `security_result.detection_fields`  
`validateaccountnumber_txnPin` | `security_result.detection_fields`  
`validateaccountnumber_user` | `security_result.detection_fields`  
`vAT` | `security_result.detection_fields`  
`verb` | `network.http.method`  
`versionCode` | `security_result.detection_fields`  
`versionName` | `security_result.detection_fields`  
`VFPJSESSION` | `security_result.detection_fields`  
`Via` | `security_result.detection_fields`  
`VIP` | `security_result.detection_fields`  
`VIRTUAL` | `network.tls.client.server_name`  
`VIRTUAL_address` | `target.resource.name`  
`virtual_server_name` | `network.tls.client.server_name`  
`virtualserver` | `network.tls.client.server_name`  
`violation_mask_alarm` | `security_result.detection_fields`  
`violation_mask_block` | `security_result.detection_fields`  
`violation_mask_learn` | `security_result.detection_fields`  
`violation_mask_staging` | `security_result.detection_fields`  
`violation_rating` | `security_result.detection_fields`  
`violations` | `security_result.description`  
`virus_name` | `security_result.threat_name`  
`vs_ip` | `intermediary.ip`  
`vs_name` | `target.resource.name`  
`vs_port` | `intermediary.port`  
`web_application_name` | `target.application`  
`websocket_direction` | `network.direction = Inbound`   
Condition:   
(if `[websocket_direction] == "clientToServer"`)   
`network.direction = OUTBOUND`   
Condition:   
(if `[websocket_direction] == "ServerToclient"`)  
`websocket_message_type` | `security_result.detection_fields`  
`wm_client_ip` | `principal.ip`   
`principal.asset.ip`  
`WORKIDENTIFIER` | `security_result.detection_fields`  
`wtfpc` | `security_result.detection_fields`  
`X-Amzn-Trace-Id` | `security_result.detection_fields`  
`X-Bug-Bounty` | `security_result.detection_fields`  
`X-Bug-Bounty-Contact` | `security_result.detection_fields`  
`X-Bug-Bounty-Purpose` | `security_result.detection_fields`  
`X-Client-Ip` | `principal.ip`   
`principal.asset.ip`  
`x-codsecent` | `security_result.detection_fields`  
`X-Cnection` | `security_result.detection_fields`  
`X-Correlation-ID` | `security_result.detection_fields`  
`x-correlation-id` | `security_result.detection_fields`  
`x-country-code` | `principal.location.country_or_region`  
`x-dtpc` | `security_result.detection_fields`  
`X-Environment` | `security_result.detection_fields`  
`X-EVENT-TYPE` | `metadata.product_event_type`  
`X-F5-VIP` | `target.ip`   
`target.asset.ip`  
`XFF` | `principal.ip`  
`X-FORWARDED-PORT` | `target.port`  
`X-FORWARDED-PROTO` | `network.application_protocol`  
`X-Forwarded-For` | `principal.ip`   
`principal.asset.ip`  
`X-Forwarded-Proto` | `network.application_protocol`  
`x-forwarded-client-cert` | `security_result.detection_fields`  
`x-fwd-hdr-val` | `security_result.detection_fields`  
`X-header-postpay-addons-uri` | `security_result.detection_fields`  
`X-Home-Region` | `security_result.detection_fields`  
`x-iapp-real-ip` | `principal.ip`   
`principal.asset.ip`  
`X-ma-bid` | `security_result.detection_fields`  
`X-ma-did` | `security_result.detection_fields`  
`X-ma-hostname` | `security_result.detection_fields`  
`X-ma-pid` | `security_result.detection_fields`  
`X-ma-sid` | `security_result.detection_fields`  
`X-MicrosoftAjax` | `security_result.detection_fields`  
`x-msisdnToken` | `security_result.detection_fields`  
`X-msisdnToken` | `security_result.detection_fields`  
`X-OAUTH-IDENTITY-DOMAIN-NAME` | `security_result.detection_fields`  
`X-ORIGINAL-HOST` | `principal.hostname`  
`X-Original-URL` | `principal.url`  
`X-OWA-ActionId` | `additional.fields`  
`X-OWA-ActionName` | `additional.fields`  
`X-OWA-Attempt` | `additional.fields`  
`X-OWA-CANARY` | `additional.fields`  
`X-OWA-ClientBuildVersion` | `security_result.detection_fields`  
`X-OWA-CorrelationId` | `metadata.product_log_id`  
`X-OWA-ExplicitLogonUser` | `principal.user.email_addresses`  
`X-OWA-UrlPostData` | `security_result.detection_fields`  
`X-Requested-With` | `additional.fields`  
`x-request-application` | `metadata.product_event_type`  
`X-ROBOT-AGENT` | `security_result.detection_fields`  
`X-ROBOT-LICENSE` | `security_result.detection_fields`  
`X-ROBOT-MACHINE-ENCODED` | `security_result.detection_fields`  
`X-ROBOT-SERVICE-USERNAME-ENCODED` | `security_result.detection_fields`  
`X-ROBOT-VERSION` | `security_result.detection_fields`  
`X-Remote-Addr` | `principal.ip`   
`principal.asset.ip`  
`x-session` | `security_result.detection_fields`  
`X-Twilio-Email-Event-Webhook-Signature` | `security_result.detection_fields`  
`X-Twilio-Email-Event-Webhook-Timestamp` | `security_result.detection_fields`  
`X-Twilio-Signature` | `security_result.detection_fields`  
`X-UIPATH-INSTALLATION-ID` | `security_result.detection_fields`  
`X-UIPATH-INSTALLATION-VERSION` | `security_result.detection_fields`  
`X-UIPATH-Localization` | `security_result.detection_fields`  
`X-wa-sid` | `security_result.detection_fields`  
`xWpammRequestId` | `security_result.detection_fields`  
`X-XSRF-TOKEN` | `additional.fields`  
`X-xforwarded-client-cert` | `security_result.detection_fields`  
  
### CSV logs

Input Column | Destination Field | Conditions  
---|---|---  
IF `[column4]` != "asm-policy" |  |   
IF column5 is not a valid IP |  |   
`column1` | `target_ip` |   
`column2` | `target_port` |   
`column3` | `geo_location` | `[column3]` not in `["N/A", ""]`  
`column3` | `target_ip` | `[column3]` != "" AND `[column3]` =~ "^[0-9.]"  
`column5` | `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` |   
`column6` | `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` |   
`column6` | `VIOLATION_DETAILS` | `[column6]` =~ ".*xml"  
`column7` | `intermediary_Ip` | `[column7]` != "" AND GROK %{IP:`column7`} succeeds  
`column8` | `network_http_method` | `[column8]` in `["GET","POST","PUT","DELETE","PATCH","HEAD","OPTIONS"]`  
`column7` | `network_http_method` | ELSE IF `[column7]` in `["GET","POST", ...]`  
`column9` | `event.idm.read_only_udm.additional.fields` | `[column9]` not in `["", "N/A"]` AND NOT TimeStamp  
`column9` | `policy_apply_date` | `[column9]` not in `["", "N/A"]` AND IS TimeStamp  
`column10` | `security_result.rule_name` | !`[column10_is_ip]` AND `[column10]` == `[column3]` AND `[column10]` != ""  
`column11` | `app_protocol` | `[column11]` != ""  
`column13` | _Varies (KV)_ | `[column13]` != ""  
`column14` | `req_status_value` | `[column14]` in `["blocked", "allowed", "alerted", "passed"]`  
`column18` | `request_id` | `[column18]` != ""  
`column19` | `severity_level` | `[column19]` =~ "(?i)(Informational  
`column22` | `principal_port` | `[column22]` not in `["", "N/A"]` AND `[column22]` is numeric  
`column23` | `event.idm.read_only_udm.metadata.product_log_id` | `[column23]` not in `["", "N/A"]`  
`column25` | `syslog_host` | `[syslog_host]` == "" AND `[column25]` != ""  
`column26` | `event.idm.read_only_udm.network.http.referral_url` | `[column26]` not in `["", "N/A"]`  
`column27` | `VIOLATION_DETAILS` | `[column27]` =~ ".*xml"  
`column28` | `VIOLATION_DETAILS` | `[column27]` !~ "._xml" AND`[column28]` =~ "._xml"  
`column28` | `security_result.description` | `[column27]` !~ "._xml" AND`[column28]` !~ "._xml" AND `[column28]` not in `["", "N/A"]` AND `[column28]` is NOT numeric  
`column15` | `response` | IF `[column27]` !~ ".*xml": `[column15]` != ""  
`column16` | `network_http_response_code` | IF `[column27]` !~ ".*xml": `[column16]` not in `["","-"]`  
`column24` | `session_id` | IF `[column27]` !~ ".*xml": `[column24]` != ""  
`column29` | `security_result.summary` | IF `[column27]` !~ ".*xml": `[column29]` != ""  
`column24` | `resource_name` | IF `[column27]` =~ ".*xml": `[column24]` != ""  
`column31` | `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` |   
If column5 is valid IP |  |   
`column1` | `target_ip` |   
`column2` | `target_port` |   
`column3` | `geo_location` | `[column3]` is NOT valid IP  
`column3` | `target_ip` | `[column3]` != "" AND `[column3]` is valid IP  
`column6` | `principal_ip` | `[column6]` != "" AND GROK %{IP:`column6`} succeeds  
`column7` | `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` |   
`column7` | `VIOLATION_DETAILS` | `[column7]` =~ ".*xml"  
`column8` | `intermediary_Ip` | `[column8]` not in `["", "N/A"]` AND GROK %{IP:`column8`} succeeds  
`column9` | `network_http_method` | `[column9]` in `["GET","POST", ...]`  
`column8` | `network_http_method` | ELSE IF `[column8]` in `["GET","POST", ...]`  
`column9` | `collected_time` | `[column9]` =~ "^[0-9]+"  
`column22` | `request_body_size` | `[column22]` =~ "^[0-9]+$"  
`column10` | `event.idm.read_only_udm.additional.fields` | `[column10]` not in `["", "N/A"]` AND NOT TimeStamp  
`column10` | `policy_apply_date` | `[column10]` not in `["", "N/A"]` AND IS TimeStamp  
`column11` | `security_result.rule_name` | `[column11_is_ip]` AND `[column11]` == `[column4]` AND `[column11]` != ""  
`column4` | `policy_name` | ELSE IF `[column11]` != `[column4]` AND `[column4]` != "" AND `[column4]` is NOT numeric  
`column4` | `target_port` | ELSE IF `[column4]` is numeric  
`column12` | `app_protocol` |   
`column13` | _Varies (KV)_ | `[column13]` != ""  
`column15` | `req_status_value` | `[column15]` in `["blocked", "allowed", "alerted", "passed"]`  
`column19` | `request_id` |   
`column20` | `severity_level` | `[column20]` =~ "(?i)(Informational  
`column23` | `principal_port` | `[column23]` not in `["", "N/A"]` AND `[column23]` is numeric  
`column26` | `syslog_host` | `[syslog_host]` == "" AND `[column26]` != ""  
`column27` | `event.idm.read_only_udm.network.http.referral_url` | `[column27]` not in `["", "N/A"]`  
`column28` | `VIOLATION_DETAILS` | `[column28]` =~ ".*xml"  
`column29` | `VIOLATION_DETAILS` | `[column28]` !~ "._xml" AND`[column29]` =~ "._xml"  
`column29` | `security_result.description` | `[column28]` !~ "._xml" AND`[column29]` !~ "._xml" AND `[column29]` not in `["", "N/A"]` AND `[column29]` is NOT numeric  
`column16` | `response` | IF `[column28]` !~ ".*xml": `[column16]` != ""  
`column17` | `network_http_response_code` | IF `[column28]` !~ ".*xml": `[column17]` not in `["","-"]`  
`column25` | `session_id` | IF `[column28]` !~ ".*xml": `[column25]` != ""  
`column30` | `security_result.summary` | IF `[column28]` !~ ".*xml": `[column30]` != ""  
`column25` | `principal_ip` | IF `[column28]` =~ ".*xml": `[column25]` != "" AND !`[column25_is_ip]`  
`column16` | `network_http_response_code` | IF `[column28]` =~ ".*xml": `[column25]` != "" AND `[column16]` != ""  
`column19` | `severity_level` | IF `[column28]` =~ ".*xml": `[column25]` != "" AND `[column19]` =~ "(?i)(Informational...)"  
`column24` | `session_id` | IF `[column28]` =~ ".*xml": `[column25]` != "" AND `[column24]` not in `["", "N/A"]`  
`column25` | `resource_name` | IF `[column28]` =~ ".*xml" AND `[column25]` == "": `[column25]` != ""  
`column24` | `event.idm.read_only_udm.metadata.product_log_id` | IF `[column28]` =~ ".*xml" AND `[column25]` == "": `[column24]` not in `["", "N/A"]`  
`column32` | `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` |   
`column33` | `request` |   
`column34` | `response` |   
IF `[column4]` == "asm-policy" |  |   
`column1` | `principal_ip` | `[column1]` != "" AND `[column1]` =~ "^[0-9.]"  
`column2` | `principal_port` | `[column2]` not in `["","N/A","none"]`  
`column3` | `principal_ip` | `[column3]` != "" AND `[column3]` =~ "^[0-9.]"  
`column4` | `event.idm.read_only_udm.metadata.product_event_type` | `[column4]` != ""  
`column6` | `principal_ip` | `[column6]` != "" AND `[column6]` is valid IP  
`column6` | `req_status_value` | ELSE IF `[column6]` in `["blocked", "allowed", ...]`  
`column6` | `support_id` | ELSE `[column6]` != ""  
`column7` | `severity_level` | `[column7]` =~ "(?i)(Informational...)"  
`column8` | `geo_location` | `[column8]` not in `["N/A", ""]`  
`column9` | `VIOLATION_DETAILS` | `[column9]` =~ ".*xml"  
`column9` | `event.idm.read_only_udm.target.application` | ELSE IF `[column9]` != ""  
`column11` | `intermediary_Ip` | GROK %{IP:`column11`} succeeds  
`column16` | `target_ip` | GROK %{IP:`column16`} succeeds  
`column18` | `network_http_method` | `[column18]` not in `["","N/A","none"]`  
`column24` | `policy_apply_date` |   
`column26` | `app_protocol` |   
`column29` | `target_url` | `[column29]` != "" AND Grok match  
`column29` | _Varies (KV)_ | `[column29]` != "" AND Grok match  
`column30` | `req_status_value` | `[column30]` in `["blocked", "allowed", ...]`  
`column31` | `security_result.summary` |   
`column32` | `network_http_response_code` | `[column32]` != ""  
`column35` | `severity` |   
`column55` | `VIOLATION_DETAILS` | `[column55]` =~ ".*xml"  
`column58` | `VIOLATION_DETAILS` | `[column58]` =~ ".*xml"  
`column60` | `security_result.description` | `[column60]` not in `["","N/A","none"]`  
`column62` | `event.idm.read_only_udm.target.resource.name` |   
IF !`[utf_error]` (Entire block is under this condition. If `[utf_error]` is true, message is dropped) IF !`[utf_error]` |  |   
`column2` | `principalIp` | (inside !`[utf_error]`)  
`column1` | `column1` | (inside !`[utf_error]`)  
"IF `[no_ip_address]` (Grok on column2 failed)" |  |   
`column1` | `date_time` |   
`column2` | `attackType` |   
`column3` | `principalIp` |   
`column11` | `method` |   
`column12` | `url` |   
`column13` | `app_protocol` |   
`column10` | `targetIp` |   
`column9` | `intermediaryIp` |   
`column19` | `rating` |   
`column15` | `req_status` |   
`column5` | `geo_location` |   
`column27` | `VIOLATION_DETAILS` | if `[column27]` is similar to xml data  
`column25` | `VIOLATION_DETAILS` | if `[column27]` not similar to xml data  
"ELSE (of `[no_ip_address]`) (Grok on column2 succeeded)" |  |   
`column1` | `date_time` |   
`attack_type` | `attackType` |   
`column10` | `method` |   
`column11` | `url` |   
`column12` | `app_protocol` |   
`column9` | `targetIp` |   
`column8` | `intermediaryIp` |   
`column18` | `rating` |   
`column14` | `req_status` |   
`column5` | `geo_location` | !`[no_ip_address]` AND `[column5]` not in `["N/A", ""]`  
`column17` | `severity` | !`[no_ip_address]` AND `[column17]` not in `["N/A", ""]`  
`column20` | `request_id` | !`[no_ip_address]` AND `[column20]` not in `["N/A", ""]`  
`column26` | `x_forwarded_for` | !`[no_ip_address]` AND `[column26]` not in `["N/A", ""]`  
`column4` | `dest_port` | `[column3]` =~ "^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$"  
`column3` | `dest_port` | ELSE (of `[column3]` ip check)  
`column15` | `resp_code` | N/A  
`column16` | `resp_code` | IF `[column15_not_resp_code]`  
`column17` | `resp_code` | IF `[column15_not_resp_code]` AND `[column16_not_resp_code]`  
`attackType` | `attack_type` | `[attackType]` not in `["N/A", ""]`  
`intermediaryIp` | `intermediary_Ip` | `[intermediaryIp]` != ""  
`principalIp` | `principal_ip` | `[principalIp]` != ""  
`targetIp` | `target_ip` | `[targetIp]` =~ "^(?:[0-9]{1,3}[.]){3}[0-9]{1,3}$"  
`resp_code` | `network_http_response_code` | `[resp_code]` != ""  
`dest_port` | `target_port` | `[dest_port]` != ""  
`url` | `target_url` | `[url]` != ""  
`intermediary_Ip` | `intermediary.ip` | `[intermediary_Ip]` != ""  
ELSE (of !`[utf_error]`) |  |   
Drop message with TAG_UNSUPPORTED |  |   
  
## Release delta

Google SecOps released a new version of the F5 ASM parser, which includes significant changes to the mapping of Parser_Name log fields to UDM fields and changes to the mapping of event types.

### Log-field mapping delta

Log Field | Existing Mapping | New  
---|---|---  
`Accept` | `"security_result.about.resource.attribute.label\nsecurity_result.about.labels"` | `additional.fields`  
`Accept-Charset` | `security_result.about.resource.attribute.labels` | `additional.fields`  
`Accept-Encoding` | `"security_result.about.resource.attribute.labels\nsecurity_result.about.labels"` | `additional.fields`  
`Accept-Language` | `security_result.detection_fields` | `additional.fields`  
`Accept-Language` | `"security_result.detection_fields\nsecurity_result.aboit.labels"` | `additional.fields`  
`AccountType` | `target.user.role_description` | `target.user.attribute.roles.description`  
`act` | `security_result.action == ALLOW` | `security_result.action == QUARATINE`  
`action1` | `security_result.detection_fields` | `security_result.action_details`  
`actual_mitigation_action` | `security_result.detection_fields` | removed "None" values  
`actual_mitigation_action_reason` | `security_result.detection_fields` | removed "None" values  
`attack_type` | `intermediary.hostname and security_result.category_details` | `security_result.category_details`  
`Cache-Control` | `security_result.about.resource.attribute.labels` | `additional.fields`  
`Cache-Control` | `security_result.detection_fields` | `additional.fields`  
`cn2` (rating) | `security_result.severity` | `security_result.detection_fields`  
`Connection` | `"security_result.about.resource.attribute.labels\nsecurity_result.about.labels"` | `additional.fields`  
`Connection` | `security_result.detection_fields` | `additional.fields`  
`Content-Length` | `security_result.about.labels` | `additional.fields`  
`Content-Type` | `security_result.about.labels` | `additional.fields`  
`date_time` | `metadata.event_timestamp` | Removed redundant mapping  
`descrip` | `metadata.descrption` | Removed redundant mapping  
`device_id` | `target.asset.id` | `principal.asset.id`  
`device_product` | `security_result.detection_fields` | `additional.fields`  
`dvchost` | `intermediary.ip and intermedairy.asset.ip` | `intermediary.ip`  
`event_id` (grok extracted value) | `additional.fields` | `principal.process.pid`  
`Keep-Alive` | `security_result.about.resource.attribute.labels` | `additional.fields`  
`net.host.port` | `principal.port and additional.fields` | `additional.fields`  
`net.peer.name` | `"target.hostname, target.asset.hostname\nadditional.fields"` | `target.hostname`  
`net.peer.port` | `target.port and additional.fields` | `additional.fields`  
`policy_name` | `about.resource.name` | `security_result.rule_name`  
`policy_name` | `security_result.about.resource.name` | `security_result.rule_name`  
`Pragma` | `security_result.about.resource.attribute.labels` | `additional.fields`  
`Pragma` | `security_result.detection_fields` | `additional.fields`  
`rating` | `security_result.severity` | Removed redundant mapping  
`Reason` | `security_resultsummary and securtiy_result.detetction_fields` | `security_result.detection_fields`  
`resp_code` | `security_result.severity` | Removed redundant mapping  
`response_code` | `additional.fields and network.http.response_code` | `network.http.response_code`  
`sig_names` | `security_result.rule_name` | `security_result.detection_fields`  
`sub_violations` | `security_result.about.resource.attribute.labels` | `security_result.detection_fields`  
`support_id` | `additional.fields and metadata.product_log_id` | `metadata.product_log_id`  
`SYSLOG headers` | `principal.ip` | `intermediary.ip`  
`uri` | `principal.url and target.url` | `traget.url`  
`violation_rating` | `security_result.about.resource.attribute.labels` | `security_result.detection_fields`  
`X-Forwarded-For` | `security_result.about.resource.attribute.labels` | `principal.ip`  
`XFF` | `intermediary.ip` | `principal.ip`  
`x_forwarded_for_header_value` | `additional.fields` | `principal.ip`  
  
### Additional changes

  * **Removed "N/A" Value Mappings:**

    * "N/A" values are no longer mapped for `principal.location.country_or_region`.
    * "N/A" values are no longer mapped for `principal.user.userid`.
  * **Removed Direct Protocol/Direction Mappings:**

    * The direct mapping of messages containing "UDP" to `network.ip_protocol` has been removed.
    * The direct mapping of messages containing "HTTPS" to `network.application_protocol` has been removed.
    * The static setting of `network.direction` to `INBOUND` has been removed.
    * The direct mapping of messages containing "HTTPS/1.1" to `network.network.tls.version` has been removed.
  * **Updated URL Mapping:**

    * Previously, `req_host` and `req_uri` were merged to map to `target.url`. This has been updated to map only `req_uri` to `target.url`.
  * **Modified Action Setting:**

    * The action of setting `security_result.action` to `ALLOW` when `"num_of_attempts"` is not null has been removed.
  * **Removed Static IP Mappings:**

    * The static mapping of `dvc_ip` to `0.0.0.0` has been removed.
    * The static mapping of `target_ip` to `0.0.0.0` has been removed.
  * **Revised`externalid` Mapping:**

    * The mapping for `externalid` now populates `additional.fields`, with the key name changed from `Support_id` to `externalid`.
  * **Updated Severity Mappings:**

    * Numeric `[severity_level]` values (for example, "1", "2", "3") are now remapped to "LOW". This standardizes numeric severity codes to a consistent scale.
    * "warning" logs are now consolidated and mapped to "MEDIUM", simplifying severity categorization.
    * The order of severity checks has been adjusted to prioritize from most to least severe: `ERROR`, `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, and finally `INFORMATIONAL`.
  * **Removed Invalid Values:**

    * Values containing literal double quotes (`\"`) have been removed from `principal.url`.
    * Invalid values (those starting with `*` or `$`) have been removed from `network.http.parsed_user_agent`.



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-asm-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
