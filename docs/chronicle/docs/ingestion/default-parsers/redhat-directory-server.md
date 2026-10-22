---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redhat-directory-server/
title: Collect Red Hat Directory Server LDAP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:59.518186+00:00
---

# Collect Red Hat Directory Server LDAP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/redhat-directory-server/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Red Hat Directory Server LDAP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Red Hat Directory Server LDAP logs to Google Security Operations using the Bindplane agent.

Red Hat Directory Server is an enterprise-class LDAP directory service built on open standards that provides centralized user identity management, authentication, and access control for Linux and UNIX environments. Directory Server stores access, error, audit, audit fail, and security logs in the `/var/log/dirsrv/slapd-instance_name/` directory, recording client connections, LDAP operations, configuration changes, failed operations, and security events such as authentication attempts and authorization issues.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Red Hat Directory Server host
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Root or sudo access to the Red Hat Directory Server host
  * Red Hat Directory Server 11 or later installed and running
  * The `rsyslog` service installed and running on the Directory Server host



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

## Get a Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The customer ID is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Linux operating system according to the following instructions.

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
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          udplog:
            listen_address: "0.0.0.0:514"
        
        exporters:
          chronicle/redhat_ds:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: REDHAT_DIRECTORY_SERVER
            raw_log_field: body
        
        service:
          pipelines:
            logs/redhat_ds:
              receivers:
                - udplog
              exporters:
                - chronicle/redhat_ds
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: The receiver type based on protocol: 
      * `udplog` for UDP syslog
      * `tcplog` for TCP syslog
      * `syslog` for RFC 3164/5424 syslog
    * `0.0.0.0`: IP address to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Specific IP address to listen on one interface
    * `514`: Port number to listen on (for example, `514`, `1514`, `6514`)
  * **Exporter configuration:**

    * `<customer_id>`: Customer ID from the earlier step
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * Adjust the `creds_file_path` to the path of your service account JSON key file (Option 1), depending on the platform: 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/redhat_ds:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: REDHAT_DIRECTORY_SERVER
            raw_log_field: body
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

  * After editing, save the file: 
    * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

    1. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    2. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           




## Enable audit and audit fail logging in Red Hat Directory Server

By default, Red Hat Directory Server enables access, error, and security logging, but disables audit and audit fail logging. Enable these logs to capture all directory changes and failed operations.

  1. Open a terminal with root or sudo privileges on the Directory Server host.
  2. Enable the audit log by running the following command:
         
         dsconf -D "cn=Directory Manager" instance_name config replace nsslapd-auditlog-logging-enabled=on
         

**Note:** Replace `instance_name` with the actual name of your Directory Server instance.
  3. Enable the audit fail log by running the following command:
         
         dsconf -D "cn=Directory Manager" instance_name config replace nsslapd-auditfaillog-logging-enabled=on
         

  4. Verify that all log types are enabled:
         
         dsconf -D "cn=Directory Manager" instance_name config get nsslapd-accesslog-logging-enabled nsslapd-errorlog-logging-enabled nsslapd-auditlog-logging-enabled nsslapd-auditfaillog-logging-enabled nsslapd-securitylog-logging-enabled
         

  5. Verify that the log files exist in the log directory:
         
         ls -la /var/log/dirsrv/slapd-instance_name/
         

**Note:** You should see the following log files: `access`, `errors`, `audit`, `security`. The audit fail log writes to the same file as the audit log by default unless a separate path is configured using the `nsslapd-auditfaillog` attribute.



### Optional: enable logging using the web console

  1. Sign in to the Red Hat Directory Server web console.
  2. Select the instance.
  3. Go to **Server > Logging**.
  4. Select the log type you want to enable (for example, **Audit Log**).
  5. Enable the logging toggle for the selected log type.
  6. Click **Save Log Settings**.



## Configure rsyslog to forward Directory Server logs to the Bindplane agent

Red Hat Directory Server writes logs to files in `/var/log/dirsrv/slapd-instance_name/` rather than to syslog directly. Use the rsyslog `imfile` module to monitor these log files and forward the entries to the Bindplane agent.

  1. Create a new rsyslog configuration file for Directory Server log forwarding:
         
         sudo nano /etc/rsyslog.d/rhds-forward.conf
         

  2. Add the following content to the configuration file:
         
         # Load the imfile module to read log files
         module(load="imfile" PollingInterval="10")
         
         # Monitor the access log
         input(type="imfile"
             File="/var/log/dirsrv/slapd-instance_name/access"
             Tag="dirsrv-access"
             Severity="info"
             Facility="local6")
         
         # Monitor the error log
         input(type="imfile"
             File="/var/log/dirsrv/slapd-instance_name/errors"
             Tag="dirsrv-errors"
             Severity="err"
             Facility="local6")
         
         # Monitor the audit log
         input(type="imfile"
             File="/var/log/dirsrv/slapd-instance_name/audit"
             Tag="dirsrv-audit"
             Severity="info"
             Facility="local6")
         
         # Monitor the security log
         input(type="imfile"
             File="/var/log/dirsrv/slapd-instance_name/security"
             Tag="dirsrv-security"
             Severity="info"
             Facility="local6")
         
         # Forward all Directory Server logs to the Bindplane agent
         local6.* @BINDPLANE_IP:514
         

**Note:** Replace `instance_name` with the actual name of your Directory Server instance (for example, `localhost`). Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host. Use `@` for UDP or `@@` for TCP. The protocol must match the receiver type configured in the Bindplane agent `config.yaml`.
  3. Verify the rsyslog configuration syntax:
         
         sudo rsyslogd -N1
         

  4. Restart the rsyslog service to apply the changes:
         
         sudo systemctl restart rsyslog
         

  5. Verify that Directory Server logs are being forwarded by checking the Bindplane agent logs:
         
         sudo journalctl -u observiq-otel-collector -f
         

**Note:** Generate an LDAP operation (for example, run an `ldapsearch` query) to produce access log entries and confirm that the Bindplane agent is receiving events.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`attrs_label` | `about.labels` | Merged  
`cn_label` | `about.labels` | Merged  
`conn_label` | `about.labels` | Merged  
`csn_label` | `about.labels` | Merged  
`err_label` | `about.labels` | Merged  
`etime_label` | `about.labels` | Merged  
`fd_label` | `about.labels` | Merged  
`filter_label` | `about.labels` | Merged  
`label` | `about.labels` | Merged  
`method_label` | `about.labels` | Merged  
`msgid_label` | `about.labels` | Merged  
`name_label` | `about.labels` | Merged  
`nentries_label` | `about.labels` | Merged  
`offset_label` | `about.labels` | Merged  
`op_label` | `about.labels` | Merged  
`optime_label` | `about.labels` | Merged  
`org_label` | `about.labels` | Merged  
`ou_label` | `about.labels` | Merged  
`scope_label` | `about.labels` | Merged  
`slot_label` | `about.labels` | Merged  
`tag_label` | `about.labels` | Merged  
`targetop_label` | `about.labels` | Merged  
`version_label` | `about.labels` | Merged  
`wtime_label` | `about.labels` | Merged  
`desc` | `metadata.description` | Directly mapped  
`creationDate` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`recordDate` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`time` | `metadata.event_timestamp` | Parsed as `dd/MMM/yyyy:HH:mm:ss Z`  
`ts` | `metadata.event_timestamp` | Parsed as `MMM d HH:mm:ss`  
`operation` | `metadata.product_event_type` | Directly mapped  
`mrId` | `metadata.product_log_id` | Directly mapped  
`properties._ecs_agent_version` | `metadata.product_version` | Directly mapped  
`host` | `principal.asset.hostname` | Directly mapped  
`oid` | `principal.asset.product_object_id` | Directly mapped  
`host` | `principal.hostname` | Directly mapped  
`client_ip` | `principal.ip` | Merged  
`namespace` | `principal.namespace` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`sec_result` | `security_result` | Merged  
`properties._hostname` | `target.asset.hostname` | Directly mapped  
`properties.host` | `target.asset.hostname` | Directly mapped  
`properties._hostname` | `target.hostname` | Directly mapped  
`properties.host` | `target.hostname` | Directly mapped  
`target_ip` | `target.ip` | Merged  
`properties.country` | `target.location.country_or_region` | Directly mapped  
`properties._file_path` | `target.process.file.full_path` | Directly mapped  
`properties._file_size` | `target.process.file.size` | Renamed/mapped  
`discipline_label` | `target.resource.attribute.labels` | Merged  
`document_type_label` | `target.resource.attribute.labels` | Merged  
`environment_label` | `target.resource.attribute.labels` | Merged  
`hostgroup_label` | `target.resource.attribute.labels` | Merged  
`platform_label` | `target.resource.attribute.labels` | Merged  
`product_label` | `target.resource.attribute.labels` | Merged  
`project_label` | `target.resource.attribute.labels` | Merged  
`base` | `target.user.group_identifiers` | Merged  
`dn` | `target.user.group_identifiers` | Merged  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `metadata.product_name` | Constant: `REDHAT_DIRECTORY_SERVER`  
N/A | `metadata.vendor_name` | Constant: `REDHAT`  
N/A | `target.platform` | Constant: `LINUX`  
`properties._file_inode` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties._file_offset` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`conn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`op` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`err` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`tag` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`nentries` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`wtime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`optime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`etime` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`csn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cn` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ou` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`filter` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`attrs` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`scope` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`o` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`targetop` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`msgid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`method` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`version` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fd` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`slot` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`properties.discipline" ,"properties.document_type" ,"properties.environment" ,"properties.hostgroup" ,"properties.platform" ,"properties.product` | `target.resource.attribute.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/redhat-directory-server-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
