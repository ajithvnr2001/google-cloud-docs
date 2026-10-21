---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-support-portal/
title: Collect Broadcom Support Portal Audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:02:24.364985+00:00
---

# Collect Broadcom Support Portal Audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/broadcom-support-portal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Broadcom Support Portal Audit logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Broadcom Support Portal Audit logs to Google Security Operations using Bindplane agent.

Broadcom Support Portal provides centralized access to support resources, case management, and product downloads for Broadcom enterprise products. The platform generates audit logs that capture user authentication events, job execution activities, resource access, and administrative operations across the portal infrastructure.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Broadcom Support Portal infrastructure
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Administrative access to the Broadcom Support Portal with permissions to configure syslog forwarding



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **Ingestion Authentication File**. Save the file securely on the system where Bindplane will be installed.

**Note:** This JSON file contains credentials for authenticating the Bindplane agent to Google SecOps.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.

**Note:** The `customer ID` is required for configuring the Bindplane agent exporter.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

  * Windows installation

    1. Open **Command Prompt** or **PowerShell** as an administrator.
    2. Run the following command:
           
           msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
           

    3. Wait for the installation to complete.

    4. Verify the installation by running:
           
           sc query observiq-otel-collector
           

The service should show as **RUNNING**.

  * Linux installation

    1. Open a terminal with root or sudo privileges.
    2. Run the following command:
           
           sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
           

    3. Wait for the installation to complete.

    4. Verify the installation by running:
           
           sudo systemctl status observiq-otel-collector
           

The service should show as **active (running)**.




### Additional installation resources

For additional installation options and troubleshooting, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * Linux:
        
        sudo nano /etc/bindplane-agent/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/broadcom:
             compression: gzip
             creds_file_path: '/etc/bindplane-agent/ingestion-auth.json'
             customer_id: 'your-customer-id'
             endpoint: malachiteingestion-pa.googleapis.com
             log_type: BROADCOM_SUPPORT_PORTAL
             raw_log_field: body
         
         service:
           pipelines:
             logs/broadcom_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/broadcom
         

  2. Replace the following placeholders:



  * Receiver configuration:

    * `listen_address`: IP address and port to listen on:

      * `0.0.0.0:514` to listen on all interfaces on port 514 (requires root on Linux)
      * `0.0.0.0:1514` to listen on an unprivileged port (recommended for Linux non-root)
    * Receiver type options:

      * `udplog` for UDP syslog (default)
      * `tcplog` for TCP syslog
  * Exporter configuration:

    * `creds_file_path`: Full path to the Google SecOps ingestion authentication file:

      * **Linux** : `/etc/bindplane-agent/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your `customer ID`. For details, see Get Google SecOps customer ID.

    * `endpoint`: Regional endpoint URL:

      * **US** : `malachiteingestion-pa.googleapis.com`
      * **Europe** : `europe-malachiteingestion-pa.googleapis.com`
      * **Asia** : `asia-southeast1-malachiteingestion-pa.googleapis.com`
      * See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints) for the complete list



### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux:

    1. Run the following command:
           
           sudo systemctl restart observiq-otel-collector
           

    2. Verify the service is running:
           
           sudo systemctl status observiq-otel-collector
           

    3. Check logs for errors:
           
           sudo journalctl -u observiq-otel-collector -f
           



  * To restart the Bindplane agent in Windows:

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
           




## Configure Broadcom Support Portal syslog forwarding

Broadcom Support Portal can forward audit log events via syslog to external collectors for SIEM integration.

### Configure remote syslog logging

  1. Sign in to the **Broadcom Support Portal** administration console.
  2. Go to **Administration > Logs > Remote Logging**.
  3. Enable **Remote Syslog**.
  4. Configure the following syslog parameters:

     * **Syslog Server Address** : Enter the IP address or hostname of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter the port matching the Bindplane agent `listen_address` (for example, `514`).
     * **Protocol** : Select **UDP** (default) or **TCP** to match the Bindplane agent receiver type.
  5. Click **Save**.




### Select audit event categories

  1. In the **Remote Logging** configuration, select the audit event categories to forward:

     * **User authentication events** : Login and logout activities
     * **Job events** : Job execution status and state changes
     * **Resource access events** : Access to support resources and downloads
     * **Administrative events** : Configuration changes and administrative operations
  2. Click **Save**.

**Note:** Specific event categories and configuration options depend on your Broadcom Support Portal deployment and license level. Refer to the Broadcom Support Portal documentation for your specific version.



### Verify syslog forwarding

  1. After saving the syslog configuration, perform a test action in the Broadcom Support Portal (for example, sign in or access a resource).
  2. Check the Bindplane agent logs for incoming syslog messages:

     * **Linux** : `sudo journalctl -u observiq-otel-collector -f`
     * **Windows** : `type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"`
  3. Verify that audit log messages appear in the logs.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
ParallelDestination, STORAGE_TYPE, JOB_NAME, kubernetes.docker_id, kubernetes.pod_id | target.resource.attribute.labels | Merged with corresponding labels  
destinationName, responseDestinationName, DESTINATION_NAME | target.application | Value from DESTINATION_NAME if not empty, else responseDestinationName if not null or empty, else destinationName  
kubernetes.container_hash | target.file.full_path | Extracted using grok pattern %{DATA:filepath}:%{GREEDYDATA:file_sha}  
kubernetes.container_hash | target.file.sha256 | Extracted using grok pattern %{DATA:filepath}:%{GREEDYDATA:file_sha}  
groupId | target.user.group_identifiers | Merged from groupId  
dispatch, companyId | additional.fields | Merged with dispatch_label and companyId_label  
response, responseId | security_result.detection_fields | Merged with response_label and responseId_label  
kubernetes.container_image, kubernetes.container_name, kubernetes.namespace_name, kubernetes.pod_name | principal.resource.attribute.labels | Merged with corresponding labels  
GROUP_NAME | principal.group.group_display_name | Value copied directly  
kubernetes.host | principal.asset.hostname | Value copied directly  
kubernetes.host | principal.hostname | Value copied directly  
payload | principal.resource.product_object_id | Value copied directly  
severity | security_result.severity | Uppercased and set if in allowed list  
description, JOB_STATE | security_result.description | Value from description if not empty, else JOB_STATE  
timestramp | metadata.event_timestamp | Parsed using ISO8601, yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ, yyyy-MM-dd HH:mm:ss.SSS formats  
| metadata.event_type | Set to "USER_LOGIN" if has_principal, has_target, user_login; "USER_LOGOUT" if has_principal, has_target, user_logout; "STATUS_UPDATE" if has_principal; else "GENERIC_EVENT"  
| extensions.auth.type | Set to "AUTHTYPE_UNSPECIFIED" if user login or logout event  
| metadata.product_name | Set to "BROADCOM_SUPPORT_PORTAL"  
| metadata.vendor_name | Set to "BROADCOM_SUPPORT_PORTAL"  
`module` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`socket_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`fd` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`family` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`level` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`timestamp_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`session_duration` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`correlationId` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`className` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`proto` | `event.idm.read_only_udm.network.ip_protocol` | Mapped from changelog  
`request_url_details` | `event.idm.read_only_udm.network.http.referral_url` | Mapped from changelog  
`log_level` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`log_level` | `event.idm.read_only_udm.security_result.severity_details` | Mapped from changelog  
`principal_userId_details` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`target_url_details` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`url_details` | `event.idm.read_only_udm.target.url` | Mapped from changelog  
`desc` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`user_email` | `event.idm.read_only_udm.principal.user.email_addresses` | Mapped from changelog  
`principal_application` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`principal_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`method_details` | `event.idm.read_only_udm.network.http.method` | Mapped from changelog  
`application_protocol_details` | `event.idm.read_only_udm.network.application_protocol_version` | Mapped from changelog  
`application_protocol_data` | `event.idm.read_only_udm.network.application_protocol` | Mapped from changelog  
`response_code_details` | `event.idm.read_only_udm.network.http.response_code` | Mapped from changelog  
`received_bytes_details` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`sent_byte_details` | `event.idm.read_only_udm.network.sent_bytes` | Mapped from changelog  
`user_agent_details` | `event.idm.read_only_udm.network.http.user_agent` | Mapped from changelog  
`user_agent_details` | `event.idm.read_only_udm.network.http.parsed_user_agent` | Mapped from changelog  
`target_ip` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`target_port` | `event.idm.read_only_udm.target.port` | Mapped from changelog  
`principal_port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`product_log_id_details` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`application_details` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/broadcom-support-portal-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
