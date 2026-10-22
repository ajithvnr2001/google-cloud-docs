---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip-authhub/
title: Collect Symantec VIP Authentication Hub logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:11.277103+00:00
---

# Collect Symantec VIP Authentication Hub logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/symantec-vip-authhub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Symantec VIP Authentication Hub logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Symantec VIP Authentication Hub logs to Google Security Operations using the Bindplane agent.

Symantec VIP Authentication Hub is a cloud-based identity and authentication platform that generates syslog messages for authentication events, user synchronization, API access, OAuth flows, and LDAP directory operations. The parser extracts fields from JSON-formatted logs and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Symantec VIP Authentication Hub
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Symantec VIP Gateway web UI



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

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/symantec_vip_authhub:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: SYMANTEC_VIP_AUTHHUB
            raw_log_field: body
        
        service:
          pipelines:
            logs/symantec_vip_authhub_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/symantec_vip_authhub
        




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
          chronicle/symantec_vip_authhub:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: SYMANTEC_VIP_AUTHHUB
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
             




## Configure syslog in Symantec VIP Authentication Hub

  1. Sign in to the **Symantec VIP Gateway** web UI.
  2. Go to **Logs > Syslog Configuration**.
  3. If configuring Syslog for the first time, select **Yes** when prompted. If already configured, click **Edit**.
  4. Provide the following configuration details: 
     * **Syslog Facility** : Select **LOG_LOCAL0**.
     * **Syslog Host** : Enter the Bindplane agent IP address.
     * **Syslog Port** : Enter the Bindplane agent port number (for example, `514` for **UDP**).
  5. Click **Save**.
  6. Go to **Identity providers > Self Service Portal Configuration**.
  7. Edit the following configuration details: 
     * **Logging Level** : Select **Info**.
     * **Enable Syslog** : Select **Yes**.
  8. Click **Submit**.
  9. Go to **Identity providers > VIP Manager Authentication Configuration**.
  10. Edit the following configuration details: 
     * **Logging Level** : Select **Info**.
     * **Enable Syslog** : Select **Yes**.
  11. Click **Submit**.
  12. Go to **User Store > LDAP Directory Synchronization**.
  13. Edit the following configuration details: 
     * **Log Level** : Select **Info**.
     * **Enable Syslog** : Select **Yes**.
  14. Click **Submit**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`/auth/v1/authenticate` | `security_result.detection_fields[].value` | The value is taken from the `/auth/v1/authenticate` field in the raw log and assigned to a `security_result.detection_fields` object with the key `api`.  
`__isAuditIdLcmIdStore` | `additional.fields[].value.string_value` | The value is taken from the `__isAuditIdLcmIdStore` field in the raw log and assigned to an `additional.fields` object with the key `__isAuditIdLcmIdStore`.  
`accessTokenScopes` | `security_result.detection_fields[].value` | The value is taken from the `accessTokenScopes` field in the raw log and assigned to a `security_result.detection_fields` object with the key `accessTokenScopes`.  
`accessTokenTid` | `security_result.detection_fields[].value` | The value is taken from the `accessTokenTid` field in the raw log and assigned to a `security_result.detection_fields` object with the key `accessTokenTid`.  
`api` | `security_result.detection_fields[].value` | The value is taken from the `api` field in the raw log and assigned to a `security_result.detection_fields` object with the key `api`.  
`appId` | `additional.fields[].value.string_value` | The value is taken from the `appId` field in the raw log and assigned to an `additional.fields` object with the key `appId`.  
`appName` | `principal.application` | The value is taken from the `appName` field in the raw log.  
`azpName` | `additional.fields[].value.string_value` | The value is taken from the `azpName` field in the raw log and assigned to an `additional.fields` object with the key `azpName`.  
`bytes_sent` | `network.sent_bytes` | The value is taken from the `bytes_sent` field in the raw log.  
`client` | `principal.asset.ip`, `principal.ip` | The IP address is extracted from the `client` field in the raw log using a grok pattern and added to the `principal.ip` and `principal.asset.ip` fields.  
`clientId` | `additional.fields[].value.string_value`, `principal.user.userid` | The value is taken from the `clientId` field in the raw log and assigned to an `additional.fields` object with the key `clientId`. If the `clientId` field is not empty, it is also used to populate the `principal.user.userid` field.  
`clientIp` | `principal.asset.ip`, `principal.ip` | The value is taken from the `clientIp` field in the raw log and added to the `principal.ip` and `principal.asset.ip` fields.  
`clientTid` | `additional.fields[].value.string_value` | The value is taken from the `clientTid` field in the raw log and assigned to an `additional.fields` object with the key `clientTid`.  
`clientTxnId` | `additional.fields[].value.string_value` | The value is taken from the `clientTxnId` field in the raw log and assigned to an `additional.fields` object with the key `clientTxnId`.  
`contentType` | `additional.fields[].value.string_value` | The value is taken from the `contentType` field in the raw log and assigned to an `additional.fields` object with the key `contentType`.  
`countryISO` | `principal.location.country_or_region` | The value is taken from the `countryISO` field in the raw log.  
`eventId` | `metadata.product_event_type` | The value is taken from the `eventId` field in the raw log.  
`flowStateId` | `additional.fields[].value.string_value` | The value is taken from the `flowStateId` field in the raw log and assigned to an `additional.fields` object with the key `flowStateId`.  
`geo.city_name` | `principal.location.city` | The value is taken from the `geo.city_name` field in the raw log.  
`geo.country_name` | `principal.location.country_or_region` | The value is taken from the `geo.country_name` field in the raw log.  
`geo.location.lat` | `principal.location.region_coordinates.latitude` | The value is taken from the `geo.location.lat` field in the raw log, converted to a float, and renamed to `principal.location.region_coordinates.latitude`.  
`geo.location.lon` | `principal.location.region_coordinates.longitude` | The value is taken from the `geo.location.lon` field in the raw log, converted to a float, and renamed to `principal.location.region_coordinates.longitude`.  
`guid` | `metadata.product_log_id` | The value is taken from the `guid` field in the raw log.  
`host` | `principal.asset.hostname`, `principal.hostname` | The value is taken from the `host` field in the raw log, stripped of any quotes, and added to the `principal.hostname` and `principal.asset.hostname` fields.  
`httpMethod` | `network.http.method` | The value is taken from the `httpMethod` field in the raw log.  
`httpReferrer` | `network.http.referral_url` | The value is taken from the `httpReferrer` field in the raw log.  
`identitySourceId` | `additional.fields[].value.string_value` | The value is taken from the `identitySourceId` field in the raw log and assigned to an `additional.fields` object with the key `identitySourceId`.  
`internal-user-sync-ext-resourceGuid` | `target.user.userid` | The value is taken from the `internal-user-sync-ext-resourceGuid` field in the raw log.  
`internal-user-sync-ext-resourceName` | `target.user.email_addresses` | The value is taken from the `internal-user-sync-ext-resourceName` field in the raw log and added to the `target.user.email_addresses` field.  
`issuerUrl` | `target.url` | The value is taken from the `issuerUrl` field in the raw log.  
`kubernetes.annotations.cni.projectcalico.org_containerID` | `target.resource.product_object_id` | The value is taken from the `kubernetes.annotations.cni.projectcalico.org_containerID` field in the raw log.  
`kubernetes.annotations.cni.projectcalico.org_podIP` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.annotations.cni.projectcalico.org_podIP` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `podIP`.  
`kubernetes.annotations.cni.projectcalico.org_podIPs` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.annotations.cni.projectcalico.org_podIPs` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `podIPs`.  
`kubernetes.container_hash` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.container_hash` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `container_hash`.  
`kubernetes.container_image` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.container_image` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `container_image`.  
`kubernetes.container_name` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.container_name` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `container_name`.  
`kubernetes.docker_id` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.docker_id` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `docker_id`.  
`kubernetes.host` | `principal.asset.hostname`, `principal.hostname` | The value is taken from the `kubernetes.host` field in the raw log and added to the `principal.hostname` and `principal.asset.hostname` fields.  
`kubernetes.labels.app` |  | This field is not mapped to the IDM object in the UDM.  
`kubernetes.labels.app.kubernetes.io/component` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.app.kubernetes.io/component` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `io_component`.  
`kubernetes.labels.app.kubernetes.io/instance` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.app.kubernetes.io/instance` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `io_instance`.  
`kubernetes.labels.app.kubernetes.io/managed-by` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.app.kubernetes.io/managed-by` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `io_managed-by`.  
`kubernetes.labels.app.kubernetes.io/name` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.app.kubernetes.io/name` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `io_name`.  
`kubernetes.labels.app.kubernetes.io/part-of` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.app.kubernetes.io/part-of` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `io_part-of`.  
`kubernetes.labels.app.kubernetes.io/version` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.app.kubernetes.io/version` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `io_version`.  
`kubernetes.labels.helm.sh/chart` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.helm.sh/chart` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `helm_sh_chart`.  
`kubernetes.labels.helmChartName` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.helmChartName` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `helmChartName`.  
`kubernetes.labels.imageTag` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.imageTag` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `imageTag`.  
`kubernetes.labels.pod-template-hash` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.labels.pod-template-hash` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `pod-template-hash`.  
`kubernetes.namespace_name` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.namespace_name` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `namespace_name`.  
`kubernetes.pod_id` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.pod_id` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `pod_id`.  
`kubernetes.pod_name` | `target.resource.attribute.labels[].value` | The value is taken from the `kubernetes.pod_name` field in the raw log and assigned to a `target.resource.attribute.labels` object with the key `pod_name`.  
`level` | `security_result.severity` | If the `level` field in the raw log matches `notice` or `info` (case-insensitive), the `security_result.severity` field is set to `INFORMATIONAL`.  
`log` | `security_result.description`, `level`, `kv_data` | The `level` and `kv_data` fields are extracted from the `log` field in the raw log using a grok pattern. The `security_result.description` field is populated with the entire `log` field.  
`logtag` | `additional.fields[].value.string_value` | The value is taken from the `logtag` field in the raw log and assigned to an `additional.fields` object with the key `logtag`.  
`method` | `network.http.method` | The value is taken from the `method` field in the raw log.  
`msg` | `metadata.event_type`, `security_result.description` | The value is taken from the `msg` field in the raw log and used to populate the `security_result.description` field. The `metadata.event_type` field is determined based on the content of the `msg` field: * `USER_CREATION` if `msg` contains `Internal user created or updated`. * `USER_LOGIN` if `msg` contains `Authorization Initiated Succesfully`, `Authentication Initiated Successfully`, or `Authentication Successful`. * `USER_RESOURCE_ACCESS` if `msg` contains `Token Generated` or `token verified`. * `NETWORK_CONNECTION` if both `has_principal` and `has_target` are true. * `STATUS_UPDATE` if `has_principal` is true. * `GENERIC_EVENT` otherwise.  
`path` | `principal.file.full_path` | The value is taken from the `path` field in the raw log.  
`principalId` | `additional.fields[].value.string_value`, `principal.user.userid` | The value is taken from the `principalId` field in the raw log and assigned to an `additional.fields` object with the key `principalId`. If the `principalId` field is not `clientId` and is not empty, it is also used to populate the `principal.user.userid` field.  
`principalType` | `additional.fields[].value.string_value` | The value is taken from the `principalType` field in the raw log and assigned to an `additional.fields` object with the key `principalType`.  
`protocol` | `network.application_protocol` | If the `protocol` field in the raw log matches `HTTP` (case-insensitive), the `network.application_protocol` field is set to `HTTP`.  
`referrer` | `network.http.referral_url` | The value is taken from the `referrer` field in the raw log, stripped of any quotes, and assigned to the `network.http.referral_url` field.  
`relVersion` | `metadata.product_version` | The value is taken from the `relVersion` field in the raw log.  
`remoteAddr` | `additional.fields[].value.string_value` | The value is taken from the `remoteAddr` field in the raw log and assigned to an `additional.fields` object with the key `remoteAddr`.  
`requestId` | `additional.fields[].value.string_value` | The value is taken from the `requestId` field in the raw log and assigned to an `additional.fields` object with the key `requestId`.  
`requestTime` | `additional.fields[].value.string_value` | The value is taken from the `requestTime` field in the raw log and assigned to an `additional.fields` object with the key `requestTime`.  
`responseCode` | `network.http.response_code` | The numeric value is extracted from the `responseCode` field in the raw log using a grok pattern, converted to an integer, and assigned to the `network.http.response_code` field.  
`request` | `method`, `path`, `protocol` | The `method`, `path`, and `protocol` fields are extracted from the `request` field in the raw log using a grok pattern after stripping any quotes.  
`server` | `target.asset.hostname`, `target.hostname` | The value is taken from the `server` field in the raw log and added to the `target.hostname` and `target.asset.hostname` fields.  
`service` | `additional.fields[].value.string_value` | The value is taken from the `service` field in the raw log and assigned to an `additional.fields` object with the key `service`.  
`status` | `network.http.response_code` | The value is taken from the `status` field in the raw log, converted to an integer, and assigned to the `network.http.response_code` field.  
`stream` | `additional.fields[].value.string_value` | The value is taken from the `stream` field in the raw log and assigned to an `additional.fields` object with the key `stream`.  
`sub` | `additional.fields[].value.string_value` | The value is taken from the `sub` field in the raw log and assigned to an `additional.fields` object with the key `sub`.  
`subType` | `additional.fields[].value.string_value` | The value is taken from the `subType` field in the raw log and assigned to an `additional.fields` object with the key `subType`.  
`tid` | `additional.fields[].value.string_value` | The value is taken from the `tid` field in the raw log and assigned to an `additional.fields` object with the key `tid`.  
`timestamp` | `metadata.event_timestamp` | The value is taken from the `timestamp` field in the raw log and parsed as an ISO8601 timestamp.  
`tname` | `additional.fields[].value.string_value` | The value is taken from the `tname` field in the raw log and assigned to an `additional.fields` object with the key `tname`.  
`txnId` | `additional.fields[].value.string_value` | The value is taken from the `txnId` field in the raw log and assigned to an `additional.fields` object with the key `txnId`.  
`type` | `additional.fields[].value.string_value` | The value is taken from the `type` field in the raw log and assigned to an `additional.fields` object with the key `type`.  
`userAgent` | `network.http.parsed_user_agent`, `network.http.user_agent` | The value is taken from the `userAgent` field in the raw log and assigned to the `network.http.user_agent` and `network.http.parsed_user_agent` fields. The `network.http.parsed_user_agent` field is then converted to a parsed user agent object.  
`userDN` | `additional.fields[].value.string_value` | The value is taken from the `userDN` field in the raw log and assigned to an `additional.fields` object with the key `userDN`.  
`userGuid` | `additional.fields[].value.string_value` | The value is taken from the `userGuid` field in the raw log and assigned to an `additional.fields` object with the key `userGuid`.  
`userIdpGuid` | `additional.fields[].value.string_value` | The value is taken from the `userIdpGuid` field in the raw log and assigned to an `additional.fields` object with the key `userIdpGuid`.  
`userIP` | `principal.asset.ip`, `principal.ip`, `target.asset.ip`, `target.ip`, `intermediary.ip` | The IP addresses are extracted from the `userIP` field in the raw log using a grok pattern. The first IP address is added to the `principal.ip` and `principal.asset.ip` fields. The second IP address is added to the `target.ip` and `target.asset.ip` fields. The third IP address is added to the `intermediary.ip` field.  
`userLoginId` | `target.user.email_addresses` | If the `userLoginId` field in the raw log is not empty and matches an email address pattern, it is added to the `target.user.email_addresses` field.  
`userLoginIdAttributeMappingName` | `target.user.user_display_name` | The value is taken from the `userLoginIdAttributeMappingName` field in the raw log.  
`userRiskLevel` | `additional.fields[].value.string_value` | The value is taken from the `userRiskLevel` field in the raw log and assigned to an `additional.fields` object with the key `userRiskLevel`.  
`userRiskScore` | `additional.fields[].value.string_value` | The value is taken from the `userRiskScore` field in the raw log and assigned to an `additional.fields` object with the key `userRiskScore`.  
`userIp` | `principal.asset.ip`, `principal.ip` | The value is taken from the `userIp` field in the raw log and added to the `principal.ip` and `principal.asset.ip` fields.  
`userUniversalId` | `additional.fields[].value.string_value` | The value is taken from the `userUniversalId` field in the raw log and assigned to an `additional.fields` object with the key `userUniversalId`.  
`vhost` | `additional.fields[].value.string_value` | The value is taken from the `vhost` field in the raw log and assigned to an `additional.fields` object with the key `vhost`.  
N/A | `extensions.auth.type` | The value is set to `SSO` if the `metadata.event_type` field is `USER_LOGIN`.  
N/A | `metadata.log_type` | The value is set to `SYMANTEC_VIP_AUTHHUB`.  
`azserver-idp-response-verify-cert-ext-idpId", "__THIS_RESOURCE_ID" and "admin-identityprovider-create-ext-resourceGuid` | `principal.user.attribute.cloud.project.id` | Mapped from changelog  
`thread` | `additional.fields` | Mapped from changelog  
`remoteUser` | `additional.fields` | Mapped from changelog  
`kubernetes.labels.app.kubernetes.io_component` | `target.resource.attribute.labels` | Mapped from changelog  
`kubernetes.labels.app.kubernetes.io_instance` | `target.resource.attribute.labels` | Mapped from changelog  
`kubernetes.labels.app.kubernetes.io_name` | `target.resource.attribute.labels` | Mapped from changelog  
`kubernetes.labels.app.kubernetes.io_managed-by` | `target.resource.attribute.labels` | Mapped from changelog  
`kubernetes.labels.app.kubernetes.io_part-of` | `target.resource.attribute.labels` | Mapped from changelog  
`kubernetes.labels.app.kubernetes.io_version` | `target.resource.attribute.labels` | Mapped from changelog  
`kubernetes.labels.helm.sh_chart` | `target.resource.attribute.labels` | Mapped from changelog  
`reqLength` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-authhub-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
