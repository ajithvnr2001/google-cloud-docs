---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-asm/
title: Collect F5 BIG-IP ASM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:05.742307+00:00
---

# Collect F5 BIG-IP ASM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-asm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect F5 BIG-IP ASM logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest F5 BIG-IP Application Security Manager (ASM) logs to Google Security Operations by using Bindplane. The parser handles various log formats (syslog, CSV, CEF, etc.) and normalizes them into UDM. It uses grok patterns and key-value extractions to parse fields, XML filtering for violation details, conditional logic for event categorization and severity mapping, and merges extracted fields into the UDM schema.

## Before you begin

  * Ensure that you have a Google Security Operations instance.
  * Ensure that you are using Windows 2016 or later, or a Linux host with `systemd`.
  * If running behind a proxy, ensure firewall [ports](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) are open.
  * Ensure that you have privileged access to F5 BIG-IP ASM.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

  * For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).



## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     1. Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     2. Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             udplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:514"
         
         exporters:
             chronicle/chronicle_w_labels:
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <customer_id>
                 endpoint: malachiteingestion-pa.googleapis.com
                 # Add optional ingestion labels for better organization
                 ingestion_labels:
                     log_type: F5_ASM
                     raw_log_field: body
         
         service:
             pipelines:
                 logs/source0__chronicle_w_labels-0:
                     receivers:
                         - udplog
                     exporters:
                         - chronicle/chronicle_w_labels
         

  3. Replace the port and IP address as required in your infrastructure.

  4. Replace `<customer_id>` with the actual customer ID.

  5. Update `/path/to/ingestion-authentication-file.json` to the path where the authentication file was saved in the [Get Google SecOps ingestion authentication file](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-bigip-asm#get-auth-file) section.




## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart bindplane-agent
        

  * To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
        
        net stop BindPlaneAgent && net start BindPlaneAgent
        




## Configure Remote Logging on F5 BIG-IP ASM

  1. Sign in to the **ASM Console** Web UI.
  2. Go to **Security > Event Logs > Logging Profiles**.
  3. Click **Create**.
  4. Provide the following configuration details:

     * **Profile Name** : enter a unique name for the profile.
     * Select **Application Security**.
     * On the Application Security tab, select **Advanced** (if additional configurations are required).
     * **Storage Destination** : select **Remote Storage**.
     * **Logging Format** : Select Common Event Format (CEF).
     * Clear **Local storage**.
     * **Protocol** : select **UDP** or **TCP** (depending on your Bindplane agent configuration).
     * **Server Addresses** : enter the Bindplane agent IP Address.
     * **Port** : selected by default `514`. Update the port setting according to your Bindplane agent configuration.
     * Click **Add**.
     * Select **Guarantee logging**.
     * Select **Report detected anomalies**.
     * **Facility** : select `LOG_LOCAL6` (you can optionally select the facility category of the logged traffic, the possible values are `LOG_LOCAL0` through `LOG_LOCAL7`).
**Note:** If you have more than one security policy you can use the same remote logging server for both applications, and use the facility filter to sort the data for each.
  5. Click **Finished**.


**Note:** When you create a logging profile for remote storage, the system stores the data for the associated security policy on one or more remote systems. Next, you can associate the logging profile with the virtual server used by the security policy.

## Associate a logging profile with a security policy

**Note:** A logging profile determines where events are logged and what details are included. By default, when you create a security policy, the system associates the Log Illegal Requests profile with the virtual server used by the policy. You can change which logging profile is associated with the security policy or assign a new one to the virtual server.

  1. Click **Local Traffic > Virtual Servers**.
  2. Click the name of the virtual server used by the security policy.
  3. From the **Security** menu, select **Policies**.
  4. Ensure that the **Application Security Policy** setting is **Enabled** , and that **Policy** is set to the security policy you want.
  5. Ensure that the **Log Profile** setting is set to **Enabled**.
  6. From the **Available** list, select the profile to use for the security policy, and move it into the **Selected** list.
  7. Click **Update**.



## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`act` | `security_result.action` | If `act` is `blocked`, maps to BLOCK. If `act` is `passed` or `legal`, maps to ALLOW. If `act` contains `alerted`, maps to QUARANTINE. Otherwise, defaults to ALLOW for Splunk format.  
`app` | `network.application_protocol` | Directly maps to HTTPS if present in the raw log.  
`attack_type` | `security_result.category_details`, `metadata.description` | Used in conjunction with other fields to determine `security_result.category`. If no other description is available, it becomes the event description. For Splunk format logs, it is used to determine category and summary if `violations` is empty.  
`client_ip` | `principal.ip`, `principal.asset.ip` | Directly maps to principal IP.  
`cn1` | `network.http.response_code` | Directly maps to HTTP response code.  
`cn2` | `security_result.severity_details` | Directly maps to security result severity details. Used with `response_code` to determine if an event is an alert.  
`column1` | `principal.ip`, `principal.asset.ip` | Maps to principal IP for certain CSV formatted logs.  
`column2` | `target.port` | Maps to target port for certain CSV formatted logs.  
`column3` | `target.ip`, `target.asset.ip` | Maps to target IP for certain CSV formatted logs.  
`column4` | `security_result.severity` | Maps to security result severity for certain CSV formatted logs. Values `Information`, `Informational`, `0`, `4` map to INFORMATIONAL. `Warning`, `1`, `3` map to MEDIUM. `Error`, `2` map to ERROR. `Critical`, `CRITICAL`, `critical` map to CRITICAL.  
`column7` | `security_result.detection_fields`, `network.http.response_code` | Contains XML data. `viol_name` within `request-violations` is extracted and added as detection fields with key `Request Violation Name_index`. `viol_name` within `response_violations` is extracted and added as detection fields with key `Response Violation Name_index`. `response_code` within `response_violations` maps to `network.http.response_code`.  
`column8` | `security_result.rule_name` | Maps to security result rule name for certain CSV formatted logs.  
`cs1` | `security_result.rule_name` | Directly maps to security result rule name.  
`cs2` | `security_result.summary` | Directly maps to security result summary.  
`cs5` | `principal.ip`, `principal.asset.ip`, `additional.fields` | If `cs5` contains a JNDI LDAP URL, it is added as an additional field with key `JNDI_LDAP_URL`. Otherwise, if it contains comma-separated IPs, any IP different from `principal_ip` is added as an additional principal IP.  
`cs6` | `principal.location.country_or_region` | Directly maps to principal location country or region.  
`data` | `network.session_id`, `network.sent_bytes`, `network.tls.version` | If present, parsed as JSON to extract `sessionid`, `bits` (mapped to `sent_bytes`), and `version`.  
`date_time` | `metadata.event_timestamp` | Directly maps to event timestamp after parsing and converting to the correct format.  
`dest_ip` | `target.ip`, `target.asset.ip` | Directly maps to target IP.  
`dest_port` | `target.port` | Directly maps to target port.  
`dhost` | `target.hostname` | Directly maps to target hostname.  
`dpt` | `target.port` | Directly maps to target port.  
`dst` | `target.ip` | Directly maps to target IP.  
`dvc` | `intermediary.ip` | Directly maps to intermediary IP.  
`dvchost` | `target.hostname`, `intermediary.hostname` | Directly maps to target hostname and intermediary hostname.  
`errdefs_msgno` | `additional.fields` | Added as an additional field with key `errdefs_msgno`.  
`externalId` | `additional.fields` | Added as an additional field with key `Support_Id`.  
`f5_host` | `target.hostname`, `intermediary.hostname` | Directly maps to target hostname and intermediary hostname.  
`geo_info` | `principal.location.country_or_region`, `security_result.detection_fields` | Maps to principal location country or region. Also added as a detection field with key `geo_info`.  
`host` | `target.hostname` | Directly maps to target hostname.  
`ids` | `additional.fields` | Parsed as a comma-separated list of support IDs. Each ID is added to a list-valued additional field with key `supportid`.  
`ip_addr_intelli` | `security_result.detection_fields` | Added as a detection field with key `ip_addr_intelli`.  
`ip_client` | `principal.ip` | Directly maps to principal IP.  
`ip_route_domain` | `principal.ip`, `principal.asset.ip` | The IP portion is extracted and mapped to principal IP.  
`irule` | `security_result.rule_name` | Directly maps to security result rule name.  
`irule-version` | `security_result.rule_version` | Directly maps to security result rule version.  
`level` | `security_result.severity`, `security_result.severity_details` | Used to determine security result severity. `error` or `warning` map to HIGH. `notice` maps to MEDIUM. `information` or `info` map to LOW. The raw value is also mapped to `severity_details`.  
`logtime` | `metadata.event_timestamp` | Directly maps to event timestamp after parsing.  
`management_ip_address`, `management_ip_address_2` | `intermediary.ip` | Directly maps to intermediary IP.  
`method` | `network.http.method` | Directly maps to HTTP method.  
`msg` | `security_result.summary`, `metadata.description` | Directly maps to security result summary for some log formats. If no other description is available, it becomes the event description.  
`policy_name` | `security_result.about.resource.name`, `security_result.rule_name` | Directly maps to security result resource name or rule name.  
`process` | `target.application` | Directly maps to target application.  
`process_id` | `principal.process.pid` | Directly maps to principal process ID.  
`protocol` | `network.application_protocol`, `network.ip_protocol`, `app_protocol` | Directly maps to application protocol or IP protocol depending on the log format.  
`proxy_id` | `security_result.rule_id` | Directly maps to security result rule ID.  
`query_string` | `additional.fields` | Added as an additional field with key `query_string`.  
`referrer` | `network.http.referral_url` | Directly maps to HTTP referral URL.  
`req_method` | `network.http.method` | Directly maps to HTTP method.  
`req_status` | `security_result.action`, `security_result.action_details`, `security_result.detection_fields` | If `blocked`, maps `security_result.action` to BLOCK. If `passed` or `legal`, maps to ALLOW. If contains `alerted`, maps to QUARANTINE. The raw value is also mapped to `action_details` and added as a detection field with key `req_status`.  
`request` | `target.url` | Directly maps to target URL.  
`requestMethod` | `network.http.method` | Directly maps to HTTP method.  
`resp` | `security_result.detection_fields` | Added as a detection field with key `resp`.  
`resp_code` | `network.http.response_code` | Directly maps to HTTP response code.  
`response` | `security_result.summary` | Directly maps to security result summary.  
`response_code` | `network.http.response_code` | Directly maps to HTTP response code.  
`route_domain` | `additional.fields` | Added as an additional field with key `route_domain`.  
`rt` | `metadata.event_timestamp` | Directly maps to event timestamp after parsing.  
`sev` | `security_result.severity`, `security_result.severity_details` | Used to determine security result severity. `ERROR` maps to ERROR. The raw value is also mapped to `severity_details`.  
`severity` | `security_result.severity`, `security_result.severity_details` | Used to determine security result severity. `Informational` maps to LOW, `Error` or `warning` map to HIGH, `critical` maps to CRITICAL, `notice` maps to MEDIUM, `information` or `info` map to LOW. The raw value is also mapped to `severity_details`.  
`sig_ids` | `security_result.rule_id` | Directly maps to security result rule ID.  
`sig_names` | `security_result.rule_name` | Directly maps to security result rule name.  
`snat_ip` | `principal.nat_ip` | Directly maps to principal NAT IP.  
`snat_port` | `principal.nat_port` | Directly maps to principal NAT port.  
`src` | `principal.ip`, `principal.asset.ip` | Directly maps to principal IP.  
`spt` | `principal.port` | Directly maps to principal port.  
`sub_violates` | `security_result.about.resource.attribute.labels` | Added as a label with key `Sub Violations` to security result resource attributes.  
`sub_violations` | `security_result.about.resource.attribute.labels` | Added as a label with key `Sub Violations` to security result resource attributes.  
`summary` | `security_result.summary` | Directly maps to security result summary.  
`support_id` | `metadata.product_log_id` | Prefixed with `support_id -` and mapped to product log ID.  
`suid` | `network.session_id` | Directly maps to network session ID.  
`suser` | `principal.user.userid` | Directly maps to principal user ID.  
`timestamp` | `metadata.event_timestamp` | Directly maps to event timestamp after parsing and converting to the correct format.  
`unit_host` | `principal.hostname`, `principal.asset.hostname` | Directly maps to principal hostname.  
`uri` | `principal.url` | Directly maps to principal URL.  
`user_id` | `principal.user.userid` | Directly maps to principal user ID.  
`user_name` | `principal.user.user_display_name` | Directly maps to principal user display name.  
`username` | `principal.user.userid` | Directly maps to principal user ID.  
`useragent` | `network.http.user_agent`, `network.http.parsed_user_agent` | Directly maps to HTTP user agent. Also parsed and mapped to parsed user agent.  
`virtualserver` | `network.tls.client.server_name` | Directly maps to TLS client server name.  
`violate_details` | `security_result.detection_fields`, `network.http.response_code` | Contains XML data. `viol_name` within `request-violations` is extracted and added as detection fields with key `Request Violation Name_index`. `viol_name` within `response_violations` is extracted and added as detection fields with key `Response Violation Name_index`. `response_code` within `response_violations` maps to `network.http.response_code`.  
`violate_rate` | `security_result.detection_fields` | Added as a detection field with key `violate_rate`.  
`violation_rating` | `security_result.about.resource.attribute.labels` | Added as a label with key `Violations Rating` to security result resource attributes.  
`violations` | `security_result.description` | Directly maps to security result description. For Splunk format logs, it is used to determine summary if present.  
`virus_name` | `security_result.threat_name` | Directly maps to security result threat name.  
`vs_name` | `network.tls.client.server_name` | Directly maps to TLS client server name.  
`websocket_direction` | `network.direction` | If `clientToServer`, maps to INBOUND. If `ServerToclient`, maps to OUTBOUND.  
`websocket_message_type` | `security_result.detection_fields` | Added as a detection field with key `WebsocketMessageType`.  
`x_fwd_hdr_val` | `principal.ip`, `principal.asset.ip` | Directly maps to principal IP.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
