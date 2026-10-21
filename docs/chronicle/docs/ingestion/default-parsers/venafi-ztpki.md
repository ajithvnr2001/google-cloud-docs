---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/venafi-ztpki/
title: Collect CyberArk Machine Identity Security logs (formerly Venafi) \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:08.704637+00:00
---

# Collect CyberArk Machine Identity Security logs (formerly Venafi)  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/venafi-ztpki/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CyberArk Machine Identity Security logs (formerly Venafi)

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest CyberArk Machine Identity Security (formerly known as Venafi) logs to Google Security Operations using Bindplane. CyberArk Machine Identity Security provides automated certificate lifecycle management, machine identity protection, and zero-trust PKI services. It enables organizations to discover, manage, and automate the provisioning and renewal of TLS/SSL certificates and cryptographic keys across their infrastructure.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the Venafi Configuration Console (VCC).



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
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
         




### Linux Installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         




### Additional Installation Resources

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure Bindplane Agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/etc/bindplane-agent/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           tcplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <your_customer_id>
             endpoint: malachiteingestion-pa.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'VENAFI_ZTPKI'
             raw_log_field: body
             ingestion_labels:
         
         service:
           pipelines:
             logs/source0__chronicle_w_labels-0:
               receivers:
                 - tcplog
               exporters:
                 - chronicle/chronicle_w_labels
         



  * Replace the port and IP address as required in your infrastructure.
  * Replace `<your_customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved in Step 1.



## Restart the Bindplane Agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure Syslog forwarding on CyberArk Machine Identity Security (formerly Venafi)

  1. Sign in to the **Venafi Configuration Console (VCC)**.
  2. Go to **Configuration > System Preferences > Logging**.
  3. In the **Syslog Settings** section, select **Enable Syslog**.

  4. Provide the following configuration details:

     * **Syslog Server** : Enter the IP address of the Bindplane agent host.
     * **Port** : Enter `514` (or the port you configured in the Bindplane agent).
     * **Protocol** : Select **TCP**.
     * **Syslog Format** : Select **RFC 5424** (recommended) or **RFC 3164**.
  5. In the **Log Categories** section, select the event types to forward:

     * Certificate lifecycle events (issuance, renewal, revocation)
     * Policy violations and compliance alerts
     * Authentication and authorization events
     * Administrative actions and configuration changes
     * Discovery scan results
  6. Click **Save** to apply the configuration.

  7. Verify logs are being sent by checking the Bindplane agent logs on your host system.




For detailed, version-specific instructions, consult the [Venafi documentation](https://docs.venafi.com/) or contact CyberArk support.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`account_list` | `additional.fields` | Merged  
`data_name_label` | `additional.fields` | Merged  
`data_value_label` | `additional.fields` | Merged  
`grouping_name_label` | `additional.fields` | Merged  
`grouping_value_label` | `additional.fields` | Merged  
`text1_name_label` | `additional.fields` | Merged  
`text2_name_label` | `additional.fields` | Merged  
`text2_value_label` | `additional.fields` | Merged  
`value1_name_label` | `additional.fields` | Merged  
`value2_name_label` | `additional.fields` | Merged  
`value2_value_label` | `additional.fields` | Merged  
`description` | `metadata.description` | Directly mapped  
`created_at` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`not_after` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`not_before` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`time_stamp` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ssZ`  
`timestamp` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`name` | `metadata.product_event_type` | Directly mapped  
`%{id}` | `metadata.product_log_id` | Merged  
`event_id` | `metadata.product_log_id` | Directly mapped  
`id` | `metadata.product_log_id` | Mapped when `id` != ``  
`organization_name` | `network.organization_name` | Directly mapped  
`issuer_dn` | `network.tls.client.certificate.issuer` | Directly mapped  
`serial` | `network.tls.client.certificate.serial` | Directly mapped  
`fingerprint` | `network.tls.client.certificate.sha1` | Directly mapped  
`fingerprint_sha256` | `network.tls.client.certificate.sha256` | Directly mapped  
`dvc_ip` | `principal.asset.ip` | Merged  
`dvc_ip` | `principal.ip` | Merged  
`organization_id_label` | `principal.user.attribute.labels` | Merged  
`subject_dn_label` | `principal.user.attribute.labels` | Merged  
`user_email` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `user_email`  
`common_name` | `principal.user.user_display_name` | Directly mapped  
`user_id` | `principal.user.userid` | Directly mapped  
`certificate_id_label` | `security_result.detection_fields` | Merged  
`certificate_request_id_label` | `security_result.detection_fields` | Merged  
`deleted_at_label` | `security_result.detection_fields` | Merged  
`imported_label` | `security_result.detection_fields` | Merged  
`key_algorithm_label` | `security_result.detection_fields` | Merged  
`key_size_label` | `security_result.detection_fields` | Merged  
`revocation_reason_label` | `security_result.detection_fields` | Merged  
`revocation_status_label` | `security_result.detection_fields` | Merged  
`signature_algorithm_label` | `security_result.detection_fields` | Merged  
`updated_at_label` | `security_result.detection_fields` | Merged  
`policy_id` | `security_result.rule_id` | Directly mapped  
`policy_name` | `security_result.rule_name` | Directly mapped  
`text1_value` | `target.asset.ip` | Merged  
`text1_value` | `target.ip` | Merged  
`target_port` | `target.port` | Directly mapped  
`subsystem_label` | `target.resource.attribute.labels` | Merged  
`object` | `target.resource.name` | Directly mapped  
`object_id` | `target.resource.product_object_id` | Directly mapped  
`account_name` | `target.user.user_display_name` | Directly mapped  
`account_id` | `target.user.userid` | Directly mapped  
N/A | `metadata.event_type` | Constant: `GENERIC_EVENT`  
N/A | `metadata.product_name` | Constant: `VENAFI ZTPKI`  
N/A | `metadata.vendor_name` | Constant: `VENAFI ZTPKI`  
N/A | `security_result.severity` | Constant: `LOW`  
`time_stamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`name` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`dvc_ip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`object` | `event.idm.read_only_udm.target.resource.name` | Mapped from changelog  
`object_subsystem` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`event_id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`description` | `event.idm.read_only_udm.metadata.description` | Mapped from changelog  
`object_id` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`value1.value` | `event.idm.read_only_udm.target_port` | Mapped from changelog  
`value1.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`text2.value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`data.value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`grouping.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`grouping.value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`value2.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`value2.value` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`text1.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`text2.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`text1.value` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`severity` | `event.idm.read_only_udm.security_result.severity` | Mapped from changelog  
`key_size" and "key_algorithm` | `security_result.detection_fields` | Mapped from changelog  
`fringerprint_sha1` | `network.tls.client.certificate.sha1` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/venafi-ztpki-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
