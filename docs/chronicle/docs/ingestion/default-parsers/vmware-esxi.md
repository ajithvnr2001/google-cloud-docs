---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-esxi/
title: Collect VMware ESXi logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:40.594218+00:00
---

# Collect VMware ESXi logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-esxi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VMware ESXi logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest VMware ESXi logs to Google Security Operations using Bindplane. VMware ESXi is a bare-metal hypervisor that installs directly on physical servers to partition them into multiple virtual machines. ESXi logs capture host system events, authentication activity, virtual machine operations, storage and network events, and hypervisor kernel messages.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the VMware ESXi host (root or administrator role) via the ESXi Host Client or vSphere Client.



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**.

     * Save the file securely on the system where Bindplane will be installed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional installation resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: YOUR_CUSTOMER_ID
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'VMWARE_ESX'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - udplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `YOUR_CUSTOMER_ID` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.



## Restart Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure VMware ESXi syslog forwarding

ESXi supports native syslog forwarding over UDP. You can configure it using the ESXi Host Client, vSphere Client, or the ESXi Shell (SSH).

### Option - ESXi Host Client or vSphere Client

  1. Sign in to the **ESXi Host Client** (`https://<esxi-host>/ui`) or the **vSphere Client** and select the ESXi host.
  2. Go to **Manage > System > Advanced Settings**.
  3. Search for `Syslog.global.logHost`.
  4. Click **Edit** and set the value to:

     * `udp://<BINDPLANE_IP>:514`
     * To add multiple syslog servers, separate them with commas (for example, `udp://<BINDPLANE_IP>:514,udp://<BACKUP_IP>:514`).
  5. Click **Save**.

  6. Search for `Syslog.global.logDir` to verify that local logging is also enabled (for example, `[] /scratch/log`).




### Option - ESXi Shell (SSH)

  1. Connect to the ESXi host via SSH.
  2. Run the following command to configure the remote syslog server:
         
         esxcli system syslog config set --loghost="udp://<BINDPLANE_IP>:514"
         

  3. Reload the syslog service:
         
         esxcli system syslog reload
         

  4. Verify the configuration:
         
         esxcli system syslog config get
         




### Configure ESXi firewall for syslog

  1. If the ESXi firewall is enabled, open the syslog outbound rule. Connect via SSH and run:
         
         esxcli network firewall ruleset set --ruleset-id=syslog --enabled=true
         

  2. Refresh the firewall rules:
         
         esxcli network firewall refresh
         

  3. Verify the syslog firewall rule is enabled:
         
         esxcli network firewall ruleset list | grep syslog
         




For more information, see the [VMware ESXi syslog documentation](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-monitoring/GUID-9F67DB52-F469-451F-B6C8-DAE8D95976E7.html).

## UDM Mapping Table

Log Field | UDM Mapping | Logic  
---|---|---  
`@fields.alias` | `event.idm.read_only_udm.principal.cloud.project.alias` | Directly mapped from the JSON log's `@fields.alias` field.  
`@fields.company_name` | `event.idm.read_only_udm.principal.user.company_name` | Directly mapped from the JSON log's `@fields.company_name` field.  
`@fields.facility` | `event.idm.read_only_udm.principal.resource.type` | Directly mapped from the JSON log's `@fields.facility` field.  
`@fields.host` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the JSON log's `@fields.host` field.  
`@fields.privatecloud_id` | `event.idm.read_only_udm.principal.cloud.project.id` | Directly mapped from the JSON log's `@fields.privatecloud_id` field.  
`@fields.privatecloud_name` | `event.idm.read_only_udm.principal.cloud.project.name` | Directly mapped from the JSON log's `@fields.privatecloud_name` field.  
`@fields.procid` | `event.idm.read_only_udm.principal.process.pid` | Directly mapped from the JSON log's `@fields.procid` field.  
`@fields.region_id` | `event.idm.read_only_udm.principal.location.country_or_region` | Directly mapped from the JSON log's `@fields.region_id` field.  
`@fields.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from the JSON log's `@fields.severity` field. If the value is "info" or similar, it's mapped to "INFORMATIONAL".  
`@timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Parsed and converted to a timestamp object from the log's `@timestamp` field using the `date` filter.  
`adapter` | `event.idm.read_only_udm.target.resource.name` | Directly mapped from the raw log's `adapter` field.  
`action` | `event.idm.read_only_udm.security_result.action` | Directly mapped from the raw log's `action` field. Values like "ALLOW" and "BLOCK" are used.  
`action` | `event.idm.read_only_udm.security_result.action_details` | Directly mapped from the raw log's `action` field. Values like "Redirect" are used.  
`administrative_domain` | `event.idm.read_only_udm.principal.administrative_domain` | Directly mapped from the raw log's `administrative_domain` field.  
`agent.hostname` | `event.idm.read_only_udm.intermediary.hostname` | Directly mapped from the JSON log's `agent.hostname` field.  
`agent.id` | `event.idm.read_only_udm.intermediary.asset.id` | Directly mapped from the JSON log's `agent.id` field.  
`agent.name` | `event.idm.read_only_udm.intermediary.asset.name` | Directly mapped from the JSON log's `agent.name` field.  
`agent.type` | `event.idm.read_only_udm.intermediary.asset.type` | Directly mapped from the JSON log's `agent.type` field.  
`agent.version` | `event.idm.read_only_udm.intermediary.asset.version` | Directly mapped from the JSON log's `agent.version` field.  
`app_name` | `event.idm.read_only_udm.principal.application` | Directly mapped from the raw log's `app_name` field.  
`app_protocol` | `event.idm.read_only_udm.network.application_protocol` | Directly mapped from the raw log's `app_protocol` field. If the value matches "http" (case-insensitive), it's mapped to "HTTP".  
`application` | `event.idm.read_only_udm.principal.application` | Directly mapped from the JSON log's `program` field.  
`cmd` | `event.idm.read_only_udm.target.process.command_line` | Directly mapped from the raw log's `cmd` field.  
`collection_time` | `event.idm.read_only_udm.metadata.event_timestamp` | The nanoseconds from the `collection_time` field are added to the seconds from the `collection_time` field to create the `event_timestamp`.  
`data` | `event.idm.read_only_udm.metadata.description` | The raw log message is parsed and relevant parts are extracted to populate the description field.  
`descrip` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the raw log's `descrip` field.  
`dns.answers.data` | `event.idm.read_only_udm.network.dns.answers.data` | Directly mapped from the JSON log's `dns.answers.data` field.  
`dns.answers.ttl` | `event.idm.read_only_udm.network.dns.answers.ttl` | Directly mapped from the JSON log's `dns.answers.ttl` field.  
`dns.answers.type` | `event.idm.read_only_udm.network.dns.answers.type` | Directly mapped from the JSON log's `dns.answers.type` field.  
`dns.questions.name` | `event.idm.read_only_udm.network.dns.questions.name` | Directly mapped from the JSON log's `dns.questions.name` field.  
`dns.questions.type` | `event.idm.read_only_udm.network.dns.questions.type` | Directly mapped from the JSON log's `dns.questions.type` field.  
`dns.response` | `event.idm.read_only_udm.network.dns.response` | Directly mapped from the JSON log's `dns.response` field.  
`ecs.version` | `event.idm.read_only_udm.metadata.product_version` | Directly mapped from the JSON log's `ecs.version` field.  
`event_message` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the JSON log's `event_message` field.  
`event_metadata` | `event.idm.read_only_udm.principal.process.product_specific_process_id` | The `event_metadata` field is parsed to extract the `opID` value, which is then prepended with "opID:" and mapped to the UDM.  
`event_type` | `event.idm.read_only_udm.metadata.event_type` | Directly mapped from the JSON log's `event_type` field.  
`filepath` | `event.idm.read_only_udm.target.file.full_path` | Directly mapped from the raw log's `filepath` field.  
`fields.company_name` | `event.idm.read_only_udm.principal.user.company_name` | Directly mapped from the JSON log's `fields.company_name` field.  
`fields.facility` | `event.idm.read_only_udm.principal.resource.type` | Directly mapped from the JSON log's `fields.facility` field.  
`fields.host` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the JSON log's `fields.host` field.  
`fields.privatecloud_id` | `event.idm.read_only_udm.principal.cloud.project.id` | Directly mapped from the JSON log's `fields.privatecloud_id` field.  
`fields.privatecloud_name` | `event.idm.read_only_udm.principal.cloud.project.name` | Directly mapped from the JSON log's `fields.privatecloud_name` field.  
`fields.procid` | `event.idm.read_only_udm.principal.process.pid` | Directly mapped from the JSON log's `fields.procid` field.  
`fields.region_id` | `event.idm.read_only_udm.principal.location.country_or_region` | Directly mapped from the JSON log's `fields.region_id` field.  
`fields.severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from the JSON log's `fields.severity` field. If the value is "info" or similar, it's mapped to "INFORMATIONAL".  
`host.architecture` | `event.idm.read_only_udm.principal.asset.architecture` | Directly mapped from the JSON log's `host.architecture` field.  
`host.containerized` | `event.idm.read_only_udm.principal.asset.containerized` | Directly mapped from the JSON log's `host.containerized` field.  
`host.hostname` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the JSON log's `host.hostname` field.  
`host.id` | `event.idm.read_only_udm.principal.asset.id` | Directly mapped from the JSON log's `host.id` field.  
`host.ip` | `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` | Directly mapped from the JSON log's `host.ip` field.  
`host.mac` | `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac` | Directly mapped from the JSON log's `host.mac` field.  
`host.name` | `event.idm.read_only_udm.principal.asset.name` | Directly mapped from the JSON log's `host.name` field.  
`host.os.codename` | `event.idm.read_only_udm.principal.asset.os.codename` | Directly mapped from the JSON log's `host.os.codename` field.  
`host.os.family` | `event.idm.read_only_udm.principal.asset.os.family` | Directly mapped from the JSON log's `host.os.family` field.  
`host.os.kernel` | `event.idm.read_only_udm.principal.asset.os.kernel` | Directly mapped from the JSON log's `host.os.kernel` field.  
`host.os.name` | `event.idm.read_only_udm.principal.asset.os.name` | Directly mapped from the JSON log's `host.os.name` field.  
`host.os.platform` | `event.idm.read_only_udm.principal.asset.os.platform` | Directly mapped from the JSON log's `host.os.platform` field.  
`host.os.version` | `event.idm.read_only_udm.principal.asset.os.version` | Directly mapped from the JSON log's `host.os.version` field.  
`iporhost` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the raw log's `iporhost` field.  
`iporhost` | `event.idm.read_only_udm.principal.ip` | Directly mapped from the raw log's `iporhost` field if it's an IP address.  
`iporhost1` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the raw log's `iporhost1` field.  
`kv_data1` | `event.idm.read_only_udm.principal.process.product_specific_process_id` | The `kv_data1` field is parsed to extract the `opID` or `sub` value, which is then prepended with "opID:" or "sub:" respectively and mapped to the UDM.  
`kv_msg` | `event.idm.read_only_udm.additional.fields` | The `kv_msg` field is parsed as key-value pairs and added to the `additional_fields` array in the UDM.  
`kv_msg1` | `event.idm.read_only_udm.additional.fields` | The `kv_msg1` field is parsed as key-value pairs and added to the `additional_fields` array in the UDM.  
`lbdn` | `event.idm.read_only_udm.target.hostname` | Directly mapped from the raw log's `lbdn` field.  
`log.source.address` | `event.idm.read_only_udm.observer.hostname` | Directly mapped from the JSON log's `log.source.address` field, taking only the hostname part.  
`log_event.original` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the JSON log's `event.original` field.  
`log_level` | `event.idm.read_only_udm.security_result.severity_details` | Directly mapped from the JSON log's `log_level` field.  
`logstash.collect.host` | `event.idm.read_only_udm.observer.hostname` | Directly mapped from the JSON log's `logstash.collect.host` field.  
`logstash.collect.timestamp` | `event.idm.read_only_udm.metadata.ingested_timestamp` | Parsed and converted to a timestamp object from the log's `logstash.collect.timestamp` field using the `date` filter.  
`logstash.ingest.host` | `event.idm.read_only_udm.intermediary.hostname` | Directly mapped from the JSON log's `logstash.ingest.host` field.  
`logstash.ingest.timestamp` | `event.idm.read_only_udm.metadata.ingested_timestamp` | Parsed and converted to a timestamp object from the log's `logstash.ingest.timestamp` field using the `date` filter.  
`logstash.process.host` | `event.idm.read_only_udm.intermediary.hostname` | Directly mapped from the JSON log's `logstash.process.host` field.  
`logstash.process.timestamp` | `event.idm.read_only_udm.metadata.ingested_timestamp` | Parsed and converted to a timestamp object from the log's `logstash.process.timestamp` field using the `date` filter.  
`log_type` | `event.idm.read_only_udm.metadata.log_type` | Directly mapped from the raw log's `log_type` field.  
`message` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the JSON log's `message` field.  
`message_to_process` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the raw log's `message_to_process` field.  
`metadata.event_type` | `event.idm.read_only_udm.metadata.event_type` | Set to "GENERIC_EVENT" initially, then potentially overwritten based on the parsed `service` or other log content. Can be values like `PROCESS_LAUNCH`, `NETWORK_CONNECTION`, `USER_LOGIN`, etc.  
`metadata.product_event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Directly mapped from the raw log's `process_id` or `prod_event_type` field.  
`metadata.product_log_id` | `event.idm.read_only_udm.metadata.product_log_id` | Directly mapped from the raw log's `event_id` field.  
`metadata.product_name` | `event.idm.read_only_udm.metadata.product_name` | Set to "ESX".  
`metadata.product_version` | `event.idm.read_only_udm.metadata.product_version` | Directly mapped from the JSON log's `version` field.  
`metadata.vendor_name` | `event.idm.read_only_udm.metadata.vendor_name` | Set to "VMWARE".  
`msg` | `event.idm.read_only_udm.metadata.description` | Directly mapped from the raw log's `msg` field.  
`network.application_protocol` | `event.idm.read_only_udm.network.application_protocol` | Set to "DNS" if the `service` is "named", "HTTPS" if the port is 443, or "HTTP" if the `app_protocol` matches "http".  
`network.direction` | `event.idm.read_only_udm.network.direction` | Determined from keywords in the raw log, such as "IN", "OUT", "->". Can be `INBOUND` or `OUTBOUND`.  
`network.http.method` | `event.idm.read_only_udm.network.http.method` | Directly mapped from the raw log's `method` field.  
`network.http.parsed_user_agent` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Parsed from the `useragent` field using the `convert` filter.  
`network.http.referral_url` | `event.idm.read_only_udm.network.http.referral_url` | Directly mapped from the raw log's `prin_url` field.  
`network.http.response_code` | `event.idm.read_only_udm.network.http.response_code` | Directly mapped from the raw log's `status_code` field and converted to an integer.  
`network.http.user_agent` | `event.idm.read_only_udm.network.http.user_agent` | Directly mapped from the raw log's `useragent` field.  
`network.ip_protocol` | `event.idm.read_only_udm.network.ip_protocol` | Determined from keywords in the raw log, such as "TCP", "UDP".  
`network.received_bytes` | `event.idm.read_only_udm.network.received_bytes` | Directly mapped from the raw log's `rec_bytes` field and converted to an unsigned integer.  
`network.sent_bytes` | `event.idm.read_only_udm.network.sent_bytes` | Extracted from the raw log's `message_to_process` field.  
`network.session_id` | `event.idm.read_only_udm.network.session_id` | Directly mapped from the raw log's `session` field.  
`pid` | `event.idm.read_only_udm.target.process.parent_process.pid` | Directly mapped from the raw log's `pid` field.  
`pid` | `event.idm.read_only_udm.principal.process.pid` | Directly mapped from the JSON log's `pid` field.  
`pid` | `event.idm.read_only_udm.target.process.pid` | Directly mapped from the raw log's `pid` field.  
`port` | `event.idm.read_only_udm.target.port` | Directly mapped from the JSON log's `port` field.  
`principal.application` | `event.idm.read_only_udm.principal.application` | Directly mapped from the raw log's `app_name` or `service` field.  
`principal.asset.hostname` | `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the raw log's `principal_hostname` or `iporhost` field.  
`principal.asset.ip` | `event.idm.read_only_udm.principal.asset.ip` | Directly mapped from the raw log's `syslog_ip` field.  
`principal.hostname` | `event.idm.read_only_udm.principal.hostname` | Directly mapped from the raw log's `principal_hostname` or `iporhost` field.  
`principal.ip` | `event.idm.read_only_udm.principal.ip` | Directly mapped from the raw log's `iporhost` or `syslog_ip` field.  
`principal.port` | `event.idm.read_only_udm.principal.port` | Directly mapped from the raw log's `srcport` field.  
`principal.process.command_line` | `event.idm.read_only_udm.principal.process.command_line` | Directly mapped from the raw log's `cmd` field.  
`principal.process.parent_process.pid` | `event.idm.read_only_udm.principal.process.parent_process.pid` | Directly mapped from the raw log's `parent_pid` field.  
`principal.process.pid` | `event.idm.read_only_udm.principal.process.pid` | Directly mapped from the raw log's `process_id` field.  
`principal.process.product_specific_process_id` | `event.idm.read_only_udm.principal.process.product_specific_process_id` | Extracted from the raw log's `message_to_process` field, usually prefixed with "opID:".  
`principal.url` | `event.idm.read_only_udm.principal.url` | Directly mapped from the raw log's `prin_url` field.  
`principal.user.company_name` | `event.idm.read_only_udm.principal.user.company_name` | Directly mapped from the JSON log's `fields.company_name` field.  
`principal.user.userid` | `event.idm.read_only_udm.principal.user.userid` | Directly mapped from the raw log's `USER` field.  
`priority` | `event.idm.read_only_udm.metadata.product_event_type` | Directly mapped from the raw log's `priority` field.  
`program` | `event.idm.read_only_udm.principal.application` | Directly mapped from the JSON log's `program` field.  
`qname` | `event.idm.read_only_udm.network.dns.questions.name` | Directly mapped from the raw log's `qname` field.  
`response_data` | `event.idm.read_only_udm.network.dns.answers.data` | Directly mapped from the raw log's `response_data` field.  
`response_rtype` | `event.idm.read_only_udm.network.dns.answers.type` | Directly mapped from the raw log's `response_rtype` field. The numeric DNS record type is extracted.  
`response_ttl` | `event.idm.read_only_udm.network.dns.answers.ttl` | Directly mapped from the raw log's `response_ttl` field.  
`rtype` | `event.idm.read_only_udm.network.dns.questions.type` | Directly mapped from the raw log's `rtype` field. The numeric DNS record type is extracted.  
`security_result.action` | `event.idm.read_only_udm.security_result.action` | Determined from keywords or status in the raw log. Can be `ALLOW` or `BLOCK`.  
`security_result.action_details` | `event.idm.read_only_udm.security_result.action_details` | Extracted from the raw log message, providing more context about the action taken.  
`security_result.category` | `event.idm.read_only_udm.security_result.category` | Set to `POLICY_VIOLATION` if the log indicates a firewall rule match.  
`security_result.description` | `event.idm.read_only_udm.security_result.description` | Extracted from the raw log message, providing more context about the security result.  
`security_result.rule_id` | `event.idm.read_only_udm.security_result.rule_id` | Directly mapped from the raw log's `rule_id` field.  
`security_result.severity` | `event.idm.read_only_udm.security_result.severity` | Determined from keywords in the raw log, such as "info", "warning", "error". Can be `INFORMATIONAL`, `LOW`, `MEDIUM`, or `HIGH`.  
`security_result.severity_details` | `event.idm.read_only_udm.security_result.severity_details` | Directly mapped from the raw log's `severity` or `log.syslog.severity.name` field.  
`security_result.summary` | `event.idm.read_only_udm.security_result.summary` | Extracted from the raw log message, providing a concise summary of the security result.  
`service` | `event.idm.read_only_udm.principal.application` | Directly mapped from the raw log's `service` field.  
`source` | `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` | Directly mapped from the raw log's `source` field.  
`src.file.full_path` | `event.idm.read_only_udm.src.file.full_path` | Extracted from the raw log message.  
`src.hostname` | `event.idm.read_only_udm.src.hostname` | Directly mapped from the raw log's `src.hostname` field.  
`src_ip` | `event.idm.read_only_udm.principal.ip` | Directly mapped from the raw log's `src_ip` field.  
`src_mac_address` | `event.idm.read_only_udm.principal.mac` | Directly mapped from the raw log's `src_mac_address` field.  
`srcport` | `event.idm.read_only_udm.principal.port` | Directly mapped from the raw log's `srcport` field.  
`srcip` | `event.idm.read_only_udm.principal.ip` | Directly mapped from the raw log's `srcip` field.  
`subtype` | `event.idm.read_only_udm.metadata.event_type` | Directly mapped from the raw log's `subtype` field.  
`tags` | `event.idm.read_only_udm.metadata.tags` | Directly mapped from the JSON log's `tags` field.  
`target.application` | `event.idm.read_only_udm.target.application` | Directly mapped from the raw log's `target_application` field.  
`target.file.full_path` | `event.idm.read_only_udm.target.file.full_path` | Extracted from the raw log message.  
`target.hostname` | `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname` | Directly mapped from the raw log's `target_hostname` or `iporhost` field.  
`target.ip` | `event.idm.read_only_udm.target.ip` | Directly mapped from the raw log's `target_ip` field.  
`target.mac` | `event.idm.read_only_udm.target.mac` | Directly mapped from the raw log's `target_mac_address` field.  
`target.port` | `event.idm.read_only_udm.target.port` | Directly mapped from the raw log's `target_port` field.  
`target.process.command_line` | `event.idm.read_only_udm.target.process.command_line` | Directly mapped from the raw log's `cmd` field.  
`target.process.parent_process.pid` | `event.idm.read_only_udm.target.process.parent_process.pid` | Directly mapped from the raw log's `parent_pid` field.  
`target.process.pid` | `event.idm.read_only_udm.target.process.pid` | Directly mapped from the raw log's `pid` field.  
`target.process.product_specific_process_id` | `event.idm.read_only_udm.target.process.product_specific_process_id` | Extracted from the raw log's `message_to_process` field, usually prefixed with "opID:".  
`target.resource.name` | `event.idm.read_only_udm.target.resource.name` | Directly mapped from the raw log's `adapter` field.  
`target.resource.resource_type` | `event.idm.read_only_udm.target.resource.resource_type` | Set to `VIRTUAL_MACHINE` if the log indicates a VM operation.  
`target.resource.type` | `event.idm.read_only_udm.target.resource.type` | Set to `SETTING` if the log indicates a setting modification.  
`target.user.userid` | `event.idm.read_only_udm.target.user.userid` | Directly mapped from the raw log's `target_username` or `user1` field.  
`timestamp` | `event.timestamp` | Parsed and converted to a timestamp object from the log's `timestamp` or `data` field using the `date` filter.  
`type` | `event.idm.read_only_udm.additional.fields` | The log's `type` field is added to the `additional_fields` array in the UDM with the key "LogType".  
`user1` | `event.idm.read_only_udm.target.user.userid` | Directly mapped from the raw log's `user1` field.  
`useragent` | `event.idm.read_only_udm.network.http.user_agent` | Directly mapped from the raw log's `useragent` field.  
`vmw_cluster` | `event.idm.read_only_udm.target.resource.name` | Directly mapped from the raw log's `vmw_cluster` field.  
`vmw_datacenter` | `event.idm.read_only_udm.target.resource.name` | Directly mapped from the raw log's `vmw_datacenter` field.  
`vmw_host` | `event.idm.read_only_udm.target.ip` | Directly mapped from the raw log's `vmw_host` field.  
`vmw_object_id` | `event.idm.read_only_udm.target.resource.id` | Directly mapped from the raw log's `vmw_object_id` field.  
`vmw_product` | `event.idm.read_only_udm.target.application` | Directly mapped from the raw log's `vmw_product` field.  
`vmw_vcenter` | `event.idm.read_only_udm.target.cloud.availability_zone` | Directly mapped from the raw log's `vmw_vcenter` field.  
`vmw_vcenter_id` | `event.idm.read_only_udm.target.cloud.availability_zone.id` | Directly mapped from the raw log's `vmw_vcenter_id` field.  
`vmw_vr_ops_appname` | `event.idm.read_only_udm.target.application` | Directly mapped from the raw log's `vmw_vr_ops_appname` field.  
`vmw_vr_ops_clustername` | `event.idm.read_only_udm.target.resource.name` | Directly mapped from the raw log's `vmw_vr_ops_clustername` field.  
`vmw_vr_ops_clusterrole` | `event.idm.read_only_udm.target.resource.type` | Directly mapped from the raw log's `vmw_vr_ops_clusterrole` field.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-esx-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
