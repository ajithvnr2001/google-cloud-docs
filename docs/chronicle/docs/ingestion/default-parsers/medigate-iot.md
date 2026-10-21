---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/medigate-iot/
title: Collect Claroty xDome for Healthcare logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:35.535483+00:00
---

# Collect Claroty xDome for Healthcare logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/medigate-iot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Claroty xDome for Healthcare logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Claroty xDome for Healthcare logs to Google SecOps using Bindplane agent.

Claroty xDome for Healthcare (formerly Medigate Device Security Platform) is a healthcare-focused cybersecurity platform that provides visibility, threat detection, and risk management for medical IoT (XIoT) devices. The platform monitors connected medical devices, identifies vulnerabilities, detects anomalous behavior, and provides actionable insights to protect healthcare networks from cyber threats.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Claroty xDome for Healthcare
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Claroty xDome for Healthcare management console
  * Administrator or Security Manager role in Claroty xDome for Healthcare



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
          syslog:
            tcp:
              listen_address: "0.0.0.0:514"
            protocol: rfc5424
        
        exporters:
          chronicle/claroty_xdome:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: MEDIGATE_IOT
            raw_log_field: body
        
        service:
          pipelines:
            logs/claroty_to_chronicle:
              receivers:
                - syslog
              exporters:
                - chronicle/claroty_xdome
        




### Configuration parameters

  * Replace the following placeholders:

    * **Receiver configuration:**

      * The receiver is configured for TCP syslog using RFC 5424 protocol
      * Listen address `0.0.0.0:514` accepts connections on all interfaces on port 514
      * For Linux non-root installations, use port `1514` instead of `514`
    * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1):

      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Replace `YOUR_CUSTOMER_ID` with the Customer ID from the previous step

    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

    * `endpoint`: Keep set to `chronicle.googleapis.com`.

    * `log_type`: Set to `MEDIGATE_IOT` (supports both Claroty and Medigate log formats)

  * Example configuration for Linux
        
        receivers:
          syslog:
            tcp:
              listen_address: "0.0.0.0:1514"
            protocol: rfc5424
        
        exporters:
          chronicle/claroty_xdome:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
            endpoint: chronicle.googleapis.com
            log_type: MEDIGATE_IOT
            raw_log_field: body
            ingestion_labels:
              env: production
              source: claroty_xdome
        
        service:
          pipelines:
            logs/claroty_to_chronicle:
              receivers:
                - syslog
              exporters:
                - chronicle/claroty_xdome
        




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/claroty_xdome:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: MEDIGATE_IOT
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure Claroty xDome for Healthcare syslog forwarding

### Sign in to Claroty xDome for Healthcare

  1. Sign in to the **Claroty xDome for Healthcare** web console.
  2. Go to **Settings > System Settings > My Integrations**.



### Create a new syslog integration

  1. Click **Add Integration**.
  2. In the **Integration Type** drop-down, select **Syslog**.
  3. Provide the following configuration details: 
     * **Integration Name** : Enter a descriptive name (for example, `Chronicle-SIEM`).
     * **Description** (optional): Enter `Integration with Google Chronicle SIEM`.



### Configure syslog server settings

In the **Syslog Server** section, provide the following details:

  * **Host** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
  * **Port** : Enter `514` (or `1514` if using non-root Linux installation).
  * **Protocol** : Select **TCP**.
  * **Message Format** : Select **CEF** (Common Event Format).
  * **Syslog Protocol Standard** : Select **RFC 5424**.



### Select log types to export

In the **Export Types** section, select the log types to forward to Google SecOps:

  * **Alerts** : Security alerts and risk alerts
  * **Vulnerabilities** : CVE data and vulnerability information
  * **Device Changes** : Asset inventory changes
  * **OT Activity Events** : Operational technology communication events

**Note:** You can select specific alert types by clicking **Configure Alert Types** and choosing from categories such as Network Anomalies, Policy Violations, Malware Detection, and Unauthorized Access.

### Configure timezone settings

  1. In the **Timezone** section, select **UTC** from the dropdown.

**Note:** Using UTC timezone ensures consistent timestamp normalization in Google SecOps.

### Test and save the configuration

  1. Click **Test Connection** to verify connectivity to the Bindplane agent.
  2. Verify that the test shows **Connection Successful**.
  3. Click **Save** to activate the syslog integration.



### Verify log forwarding

  1. Wait 5-10 minutes for logs to begin flowing.
  2. Check the Bindplane agent logs to verify syslog messages are being received:

     * **Linux:**
    
    sudo journalctl -u observiq-otel-collector -f | grep -i claroty
    

     * **Windows:**
    
    type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log" | findstr /i claroty
    

  3. Sign in to the Google SecOps console and verify that Claroty xDome for Healthcare logs appear in the search results.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
info_ip_desc | about.labels | Labels associated with the event  
info.as_org | about.labels |   
info.org | about.labels |   
info.isp | about.labels |   
info.country_code | about.labels |   
info.malicious_anomali_info.itype | about.labels |   
info.malicious_anomali_info.ip | about.labels |   
info.malicious_anomali_info.source | about.labels |   
info.malicious_anomali_info.org | about.labels |   
info.malicious_anomali_info.country | about.labels |   
info.malicious_anomali_info.classification | about.labels |   
info.malicious_anomali_info.maltype | about.labels |   
info.malicious_anomali_info.stream_id | about.labels |   
info.malicious_anomali_info.threat_type | about.labels |   
info.malicious_anomali_info.resource_uri | about.labels |   
info.malicious_anomali_info.threatscore | about.labels |   
info.malicious_anomali_info.confidence | about.labels |   
info.malicious_anomali_info.source_reported_confidence | about.labels |   
info.protocol | about.labels |   
info.human_name | about.labels |   
info.dest.human_name | about.labels |   
info.network | about.labels |   
info.parent_human_name | about.labels |   
info.parent_uid | about.labels |   
target_ip_desc | about.labels |   
label_resource_uri | about.labels |   
label_threatscore | about.labels |   
label_confidence | about.labels |   
label_source_reported_confidence | about.labels |   
alert.mitre_technique_ids | additional.fields | Additional free-form metadata about the event  
alert.mitre_technique_names | additional.fields |   
alert.mitre_technique_enterprise_ids | additional.fields |   
alert.mitre_technique_enterprise_names | additional.fields |   
affected_device.device_type_family | additional.fields |   
affected_device.connection_type_list | additional.fields |   
affected_device.network_list | additional.fields |   
msg_category | additional.fields |   
interface_name | additional.fields |   
interface_type | additional.fields |   
status | additional.fields |   
alert_info.certificate_thumbprint | additional.fields |   
alert_info.certificate_expiry_date | additional.fields |   
alert_info.certificate_start_date | additional.fields |   
alert_info.certificate_type | additional.fields |   
affected_device.management_status | additional.fields |   
affected_device.labels | additional.fields |   
affected_device.site_name | additional.fields |   
events_extra_info.client_id | additional.fields |   
extensions.auth.type | extensions.auth.type | Authentication type  
hostname | intermediary.hostname | Hostname of the intermediary  
events_extra_info.malicious_ip_info.malicious_ip | intermediary.ip | IP address of the intermediary  
incident_type | metadata.description | Description of the event  
text | metadata.description |   
events.description | metadata.description |   
metadata.event_type | metadata.event_type | Type of event  
event_type | metadata.product_event_type | Product event type  
events.type | metadata.product_event_type |   
incident_id | metadata.product_log_id | Product log ID  
events.id | metadata.product_log_id |   
network.application_protocol | network.application_protocol | Application protocol  
network.direction | network.direction | Direction of the network connection  
protocol_number_src | network.ip_protocol | IP protocol  
server_name | network.tls.client.server_name | Server name indicated by the client during TLS handshake  
alert_info.certificate_thumbprint | network.tls.server.certificate.sha256 | SHA256 hash of the server certificate  
version | network.tls.version | TLS version  
proto | network.tls.version_protocol | TLS version protocol  
info.domain | principal.administrative_domain | Administrative domain of the principal  
events_extra_info.domain | principal.administrative_domain |   
affected_device.asset_id | principal.asset.asset_id | Asset ID of the asset  
hardware | principal.asset.hardware | Hardware of the asset  
affected_device.device_name | principal.asset.hostname | Hostname of the asset  
events_extra_info.certificate_info.CN | principal.asset.hostname |   
management_ip | principal.asset.ip | IP address of the asset  
info.ip | principal.asset.ip |   
comm_tuple.src_ip | principal.asset.ip |   
info.tuple.2 | principal.asset.ip |   
info.tuple.3 | principal.asset.ip |   
affected_device.ip_list | principal.asset.ip |   
info.subject_components.CN | principal.hostname | Hostname of the principal  
affected_device.device_name | principal.hostname |   
events_extra_info.certificate_info.CN | principal.hostname |   
management_ip | principal.ip | IP address of the principal  
info.ip | principal.ip |   
comm_tuple.src_ip | principal.ip |   
info.tuple.2 | principal.ip |   
info.tuple.3 | principal.ip |   
affected_device.ip_list | principal.ip |   
info.subject_components.L | principal.location.city | City of the location  
events_extra_info.certificate_info.L | principal.location.city |   
location | principal.location.country_or_region | Country or region of the location  
info.subject_components.C | principal.location.country_or_region |   
events_extra_info.certificate_info.C | principal.location.country_or_region |   
info.subject_components.ST | principal.location.state | State of the location  
events_extra_info.certificate_info.ST | principal.location.state |   
principal.platform | principal.platform | Platform of the principal  
affected_device.os | principal.platform_version | Platform version of the principal  
device_uid | principal.resource.id | ID of the resource  
info.device_type_family | principal.resource.name | Name of the resource  
affected_device.device_type | principal.resource.name |   
affected_device.uid | principal.resource.product_object_id | Product object ID of the resource  
affected_device.device_category | principal.resource.resource_subtype | Subtype of the resource  
principal.resource.resource_type | principal.resource.resource_type | Type of the resource  
info.device_category | principal.resource.type | Type of the resource  
updated_by | principal.user.userid | Userid of the user  
info.login_username | principal.user.userid |   
events_extra_info.sender_id | principal.user.userid |   
events_extra_info.username | principal.user.userid |   
info.malicious_anomali_info.itype | security_result.about.labels | Labels associated with the security result  
info.malicious_anomali_info.ip | security_result.about.labels |   
info.malicious_anomali_info.source | security_result.about.labels |   
info.malicious_anomali_info.org | security_result.about.labels |   
info.malicious_anomali_info.country | security_result.about.labels |   
info.malicious_anomali_info.classification | security_result.about.labels |   
info.malicious_anomali_info.maltype | security_result.about.labels |   
info.malicious_anomali_info.stream_id | security_result.about.labels |   
info.malicious_anomali_info.threat_type | security_result.about.labels |   
events_extra_info.malicious_ip_info.source | security_result.about.labels |   
events_extra_info.malicious_ip_info.threat_type | security_result.about.labels |   
security_result.category | security_result.category | Category of the security result  
alert.category | security_result.category_details | Category details of the security result  
events_extra_info.malicious_ip_info.type | security_result.category_details |   
events_extra_info.malicious_ip_info.confidence | security_result.confidence_details | Confidence details of the security result  
alert.description | security_result.description | Description of the security result  
alert.type_name | security_result.detection_fields | Detection fields associated with the security result  
alert.device_status | security_result.detection_fields |   
alert.category | security_result.detection_fields |   
alert.description | security_result.detection_fields |   
vulnerability_info.name | security_result.detection_fields |   
vulnerability_info.type | security_result.detection_fields |   
vulnerability_info.release_date | security_result.detection_fields |   
vulnerability_info.cves | security_result.detection_fields |   
vulnerability_info.cvssv3_base_score | security_result.detection_fields |   
vulnerability_info.description | security_result.detection_fields |   
vulnerability_info.affected_products | security_result.detection_fields |   
vulnerability_info.is_known_exploited | security_result.detection_fields |   
vulnerability_device_info.relevance_source | security_result.detection_fields |   
vulnerability_info.cvssv2_base_score | security_result.detection_fields |   
affected_device.device_subcategory | security_result.detection_fields |   
affected_device.retired | security_result.detection_fields |   
affected_device.app_version | security_result.detection_fields |   
events_extra_info.communication_type | security_result.detection_fields |   
events_extra_info.malicious_ip_info.tags | security_result.detection_fields |   
alert_info.certificate_thumbprint | security_result.detection_fields |   
alert_info.certificate_expiry_date | security_result.detection_fields |   
alert_info.certificate_start_date | security_result.detection_fields |   
alert_info.certificate_type | security_result.detection_fields |   
alert.id | security_result.rule_id | Rule ID of the security result  
events.alert_id | security_result.rule_id |   
alert.name | security_result.rule_name | Rule name of the security result  
info.malicious_anomali_info.severity | security_result.severity | Severity of the security result  
affected_device.risk_score | security_result.severity_details | Severity details of the security result  
info.malicious_anomali_info.threat_type | security_result.threat_name | Threat name of the security result  
events_extra_info.malicious_ip_info.threat_type | security_result.threat_name |   
target.asset.hostname | target.asset.hostname | Hostname of the target asset  
info.tuple.3 | target.asset.ip | IP address of the target asset  
info.tuple.2 | target.asset.ip |   
comm_tuple.dst_ip | target.asset.ip |   
info.file_name | target.file.full_path | Full path of the target file  
events_extra_info.file_name | target.file.full_path |   
events_extra_info.file_type | target.file.mime_type | MIME type of the target file  
info.fqdn | target.hostname | Hostname of the target  
info.tuple.3 | target.ip | IP address of the target  
info.tuple.2 | target.ip |   
comm_tuple.dst_ip | target.ip |   
country | target.location.country_or_region | Country or region of the target location  
info.geolocation | target.location.country_or_region |   
country | target.location.country_or_region |   
events_extra_info.geo_location | target.location.country_or_region |   
state | target.location.state | State of the target location  
state | target.location.state |   
target_mac | target.mac | MAC address of the target  
comm_tuple.dst_mac | target.mac |   
comm_tuple.dst_port | target.port | Port of the target  
dest_device_uid | target.resource.id | ID of the target resource  
info.login_username | target.user.userid | Userid of the target user  
events_extra_info.username | target.user.userid |   
metadata.product_name | metadata.product_name | Product name  
metadata.vendor_name | metadata.vendor_name | Vendor name  
`events.id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`affected_device.device_name` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`affected_device.device_name` | `event.idm.read_only_udm.principal.asset.hostname` | Mapped from changelog  
`management_ip` | `event.idm.read_only_udm.principal.ip` | Mapped from changelog  
`management_ip` | `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`updated_by` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`affected_device.os` | `event.idm.read_only_udm.principal.platform_version` | Mapped from changelog  
`affected_device.management_status` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`affected_device.labels` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Mapped from changelog  
`events_extra_info.direction` | `event.idm.read_only_udm.network.direction` | Mapped from changelog  
`events_extra_info.ip_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`events.alert_id` | `event.idm.read_only_udm.security_result.rule_id` | Mapped from changelog  
`affected_device.risk_score` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`events_extra_info.communication_type` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`vulnerability_info.name", "vulnerability_info.type", "vulnerability_info.release_date", "cve", "vulnerability_info.cvssv3_base_score", "vulnerability_info.description", "vulnerability_info.affected_products", "vulnerability_info.is_known_exploited", "vulnerability_device_info.relevance", "vulnerability_device_info.relevance_source", "vulnerability_info.cvssv2_base_score", "affected_device.device_subcategory", "affected_device.retired", and "affected_device.app_version` | `security_result.detection_fields` | Mapped from changelog  
`alert.type_name", "alert.device_status", "alert_info.certificate_thumbprint", "alert_info.certificate_expiry_date", "alert_info.certificate_start_date", and "alert_info.certificate_type` | `security_result.detection_fields` | Mapped from changelog  
`alert.mitre_technique_ids", "alert.mitre_technique_names", "alert.mitre_technique_enterprise_ids", "alert.mitre_technique_enterprise_names", "affected_device.device_type_family", "affected_device.connection_type_list", and "affected_device.network_list` | `additional.fields` | Mapped from changelog  
`affected_device.mac_list` | `principal.mac` | Mapped from changelog  
`msg_category", "interface_name", "interface_type", and "status` | `additional.fields` | Mapped from changelog  
`event_extra_info.malicious_ip_info.confidence` | `security_result.confidence_details` | Mapped from changelog  
`event_extra_info.malicious_ip_info.last_update` | `target.file.mime_type` | Mapped from changelog  
`event_extra_info.malicious_ip_info.tags` | `security_result.detection_fields` | Mapped from changelog  
`event_extra_info.malicious_ip_info.type` | `security_result.category_details` | Mapped from changelog  
`events.timestamp` | `metadata.event_timestamp` | Mapped from changelog  
`events_extra_info.malicious_ip_info.severity` | `security_result.severity` | Mapped from changelog  
`events_extra_info.client_id" and "affected_device.site_name` | `additional_fields` | Mapped from changelog  
`comm_tuple.src_port` | `principal.port` | Mapped from changelog  
`comm_tuple.src_mac` | `principal.mac` | Mapped from changelog  
`affected_device.manufacturer` | `hardware.manufacturer` | Mapped from changelog  
`affected_device.model` | `hardware.model` | Mapped from changelog  
`metadata.event_type` | `NETWORK_HTTP` | Mapped from changelog  
`metadata.event_type` | `NETWORK_FTP` | Mapped from changelog  
`security_category` | `NETWORK_MALICIOUS` | Mapped from changelog  
`metadata.event_type` | `USER_LOGIN` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/medigate-iot-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
