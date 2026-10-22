---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubika-waf/
title: Collect Ubika WAF logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:32.040329+00:00
---

# Collect Ubika WAF logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ubika-waf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ubika WAF logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This docuemnt explains how to ingest Ubika WAF logs to Google Security Operations using the Bindplane agent.

Ubika WAF (formerly DenyAll) is a web application firewall that provides HTTP traffic inspection, bot protection, and API security for on-premise web applications and services.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Ubika WAF appliance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Ubika WAF management console with administrator permissions



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

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/ubika_waf:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: UBIKA_WAF
            raw_log_field: body
        
        service:
          pipelines:
            logs/ubika_waf_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/ubika_waf
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/ubika_waf:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: UBIKA_WAF
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
             




## Configure Ubika WAF syslog forwarding

  1. Sign in to the **Ubika WAF** management console.
  2. Go to **Management > Logs > Syslog Configuration**.
  3. Click **Add** to create a new syslog destination.
  4. Provide the following configuration details: 
     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514`.
     * **Protocol** : Select **TCP**.
     * **Format** : Select the default syslog format.
  5. Select the log types to forward: 
     * Security alert logs
     * Access logs
     * Audit logs
     * System event logs
  6. Click **Save** to apply the configuration.
  7. Verify that logs are being sent by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
sqliFingerprint_label, eaNewRulesWarningMode_label, eaTotalScore_label, matching_part_key_label, matching_part_key_match_label, partKeyOperator_label, partKeyPattern_label, partValue_label, partValueMatch_label, partValueOperator_label, partValuePatternName_label, partValuePatternUid_label, partValuePatternVersion_label, scoringlistRuleId_label, scoringlistRuleWeight_label, ConfigurationUid_list, Matched_Rule_ID_list | additional.fields | Merged with labels from eventt.tokens.sqliFingerprint, eventt.tokens.eaNewRulesWarningMode, eventt.tokens.eaTotalScore, matchingPart.partKey, matchingPart.partKeyMatch, matchingPart.partKeyOperator, matchingPart.partKeyPattern, matchingPart.partValue, matchingPart.partValueMatch, matchingPart.partValueOperator, matchingPart.partValuePatternName, matchingPart.partValuePatternUid, matchingPart.partValuePatternVersion, matchingPart.scoringlistRuleId, matchingPart.scoringlistRuleWeight, eventt.tokens.securityExceptionConfigurationUids, eventt.tokens.securityExceptionMatchedRuleUids  
context.applianceName | intermediary.application | Value copied directly from context.applianceName  
inter_ip | intermediary.asset.ip | Merged from inter_ip (derived from context.backendHost if IP)  
context.backendHost | intermediary.hostname | Set from context.backendHost if not an IP  
inter_ip | intermediary.ip | Set from inter_ip (derived from context.backendHost if IP)  
context.applianceUid | intermediary.file.sha1 | Value copied directly from context.applianceUid  
has_principal, has_target, has_network, has_principal_user, has_target_resource | metadata.event_type | Set to "NETWORK_HTTP" if has_principal, has_target, has_network; "USER_COMMUNICATION" if has_principal, has_principal_user; "STATUS_UPDATE" if has_principal; "USER_RESOURCE_ACCESS" if has_target_resource; else "GENERIC_EVENT"  
tokens.eventType, _type_ , eventt.tokens.eventType, eventData.tokens.eventType | metadata.product_event_type | Value from tokens.eventType if set, else _type_ , else eventt.tokens.eventType, else eventData.tokens.eventType  
eventUid, logAlertUid, eventt.eventUid, tempData.uid, eventData.eventUid | metadata.product_log_id | Value from eventUid if set, else logAlertUid, else eventt.eventUid, else tempData.uid, else eventData.eventUid  
| metadata.product_name | Set to "UBIKA_WAF"  
| metadata.vendor_name | Set to "UBIKA_WAF"  
uri_protocol, request.protocol | network.application_protocol | Set to "HTTP" if uri_protocol == "HTTP" or request.protocol == "HTTP"  
uri_method, request.method | network.http.method | Value from uri_method if set, else request.method  
uri_path, request.path, header.value | network.http.referral_url | Value from uri_path if set, else request.path, else header.value if Referer  
uri_res_code | network.http.response_code | Converted to integer from uri_res_code  
user_agent, header.value | network.http.user_agent | Value from user_agent if set, else header.value if User-Agent  
target_hostname, header.value, request.hostname, tempData.request.hostname | principal.asset.hostname | Value from target_hostname if set, else header.value if Host and not IP, else request.hostname if not IP, else tempData.request.hostname  
src_ip, request.ipSrc, source_ip | principal.asset.ip | Merged from src_ip, request.ipSrc, source_ip (from header.value if Host and IP)  
target_hostname, header.value, request.hostname, tempData.request.hostname | principal.hostname | Value from target_hostname if set, else header.value if Host and not IP, else request.hostname if not IP, else tempData.request.hostname  
src_ip, request.ipSrc, source_ip | principal.ip | Merged from src_ip, request.ipSrc, source_ip (from header.value if Host and IP)  
src_port, header.value | principal.port | Value from src_port if set, else header.value if X-Forwarded-Port, converted to integer  
request.requestUid, tempData.request.requestUid | principal.user.userid | Value from request.requestUid if set, else tempData.request.requestUid  
cookie_label, header_label, reverseProxyName_label, reverseProxyUid_label, tunnelName_label, tunnelUid_label, workflowName_label, workflowUid_label | security_result.about.resource.attribute.labels | Merged with labels from request.cookies, request.headers, context.reverseProxyName, context.reverseProxyUid, context.tunnelName, context.tunnelUid, context.workflowName, context.workflowUid  
vlan_label, riskLevel_label, riskLevelOWASP_label, logAlertUid_label, engine_name_label, resolveType_label, part_label, cwe_label, icxPolicyName_label, icxPolicyUid_label, icxRuleName_label, icxRuleUid_label, eaPolicyName_label, eaPolicyUid_label, eaRuleId_label, eaStaticPolicyUid_label, tag_label, geoipCode_label, geoipName_label, appliance_id_label, backendHost_label, reverseProxyName_label, reverseProxyUid_label, tunnelName_label, tunnelUid_label, workflowName_label, workflowUid_label, reason_label, timestampImport_label, matching_cwe_label, matching_part_label, match_riskLevel_label, match_riskLevelOWASP_label, partValue_label, partValueMatch_label | security_result.detection_fields | Merged with labels from vlan, tokens.riskLevel, tokens.riskLevelOWASP, logAlertUid, eventt.tokens.engineName, eventt.tokens.resolveType, eventt.tokens.part, eventt.tokens.cwe, eventt.tokens.icxPolicyName, eventt.tokens.icxPolicyUid, eventt.tokens.icxRuleName, eventt.tokens.icxRuleUid, eventt.tokens.eaPolicyName, eventt.tokens.eaPolicyUid, eventt.tokens.eaRuleId, eventt.tokens.eaStaticPolicyUid, tempData.context.tags, tempData.context.geoipCode, tempData.context.geoipName, tempData.context.applianceUid, tempData.context.backendHost, tempData.context.reverseProxyName, tempData.context.reverseProxyUid, tempData.context.tunnelName, tempData.context.tunnelUid, tempData.context.workflowName, tempData.context.workflowUid, eventt.tokens.reason, tempData.timestampImport, matchingPart.cwe, matchingPart.part, matchingPart.riskLevel, matchingPart.riskLevelOWASP, matchingPart.partValue, matchingPart.partValueMatch  
desc, tokens.customMessage, eventt.tokens.customMessage, eventData.tokens.customMessage | security_result.description | Value from desc if set, else tokens.customMessage, else eventt.tokens.customMessage, else eventData.tokens.customMessage  
tokens.severity, eventt.tokens.severity, severity_level | security_result.severity | Set to INFORMATIONAL if severity in 1-3; CRITICAL if severity in 4-5; MEDIUM if severity in 6-7; else UNKNOWN_SEVERITY  
tokens.reason, eventt.tokens.reason, eventData.tokens.reason | security_result.summary | Value from tokens.reason if set, else eventt.tokens.reason, else eventData.tokens.reason  
tokens.attackFamily, eventt.tokens.attackFamily, eventData.tokens.attackFamily | security_result.threat_name | Value from tokens.attackFamily if set, else eventt.tokens.attackFamily, else eventData.tokens.attackFamily  
source_ip | src.ip | Set from source_ip (from header.value if Host and IP)  
target_hostname | target.asset.hostname | Value copied directly from target_hostname  
request.ipDst, target_ip_label | target.asset.ip | Merged from request.ipDst, target_ip_label  
tempData.request.path | target.file.full_path | Value copied directly from tempData.request.path  
target_hostname, header.value | target.hostname | Value from target_hostname if set, else header.value if Host  
request.ipDst, target_ip_label | target.ip | Merged from request.ipDst, target_ip_label  
target_port, request.portDst, context.backendPort, tempData.request.portDst, tempData.context.backendPort | target.port | Value from target_port if set, else request.portDst, else context.backendPort, else tempData.request.portDst, else tempData.context.backendPort, converted to integer  
engineUid_label, engine_name_label, cwe_label, resolveType_label, part_label, matching_cwe_label, matching_part_label, match_riskLevel_label, match_riskLevelOWASP_label, matching_part_key_label, matching_part_key_match_label, partKeyOperator_label, partKeyPattern_label, partValue_label, partValueMatch_label, partValueOperator_label, partValuePatternName_label, partValuePatternUid_label, partValuePatternVersion_label, scoringlistRuleId_label, scoringlistRuleWeight_label | target.resource.attribute.labels | Merged with labels from tokens.engineUid, tokens.engineName, tokens.cwe, tokens.resolveType, tokens.part, eventData.tokens.engineUid, eventData.tokens.engineName, eventData.tokens.cwe, eventData.tokens.resolveType, eventData.tokens.part, matchingPart.cwe, matchingPart.part, matchingPart.riskLevel, matchingPart.riskLevelOWASP, matchingPart.partKey, matchingPart.partKeyMatch, matchingPart.partKeyOperator, matchingPart.partKeyPattern, matchingPart.partValue, matchingPart.partValueMatch, matchingPart.partValueOperator, matchingPart.partValuePatternName, matchingPart.partValuePatternUid, matchingPart.partValuePatternVersion, matchingPart.scoringlistRuleId, matchingPart.scoringlistRuleWeight  
target_path | target.url | Value copied directly from target_path  
`headers.value` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`key` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`X-Forwarded-Host` | `event.idm.read_only_udm.security_result.about.resource.attribute.labels` | Mapped from changelog  
`tokens.ipReputationIp` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`tokens.ipReputationIp` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`tokens.matchingParts` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request.body` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`unique_id1` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`thread_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.ipReputationScore` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.eaTotalScore` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.eaPolicyUid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.eaPolicyName` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.eaStaticPolicyUid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.eaRuleId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.eaNewRulesWarningMode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`internal_timestamp` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.securityExceptionConfigurationUid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tokens.icxPolicyName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`tokens.icxPolicyUid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`tokens.icxRuleName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`tokens.icxRuleUid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`tokens.ipReputationThreats` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`message_component` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubika-waf-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
