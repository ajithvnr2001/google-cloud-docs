---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-privilege-cloud/
title: Collect CyberArk Privilege Cloud logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:25:15.050099+00:00
---

# Collect CyberArk Privilege Cloud logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cyberark-privilege-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CyberArk Privilege Cloud logs

**Parser Version:** 14.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CyberArk Privilege Cloud logs to Google Security Operations using Bindplane. CyberArk Privilege Cloud is a SaaS-based privileged access management solution that secures, manages, and monitors privileged credentials in the cloud. It provides automated credential rotation, session isolation and recording, just-in-time access provisioning, and comprehensive audit logging for privileged account activities across hybrid and multi-cloud environments.

**Note:** CyberArk Privilege Cloud syslog forwarding supports only TCP and TLS protocols. UDP is not supported.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * A Windows 2016 or later or Linux host with systemd.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the CyberArk Privilege Cloud administration portal with Vault Admin permissions.
  * A valid TLS certificate for the Bindplane agent host (required for syslog over TLS on port 6514).



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

For additional installation options, consult this [installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest Syslog and send to Google SecOps

  1. Access the Configuration File:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
             tcplog:
                 # Replace the port and IP address as required
                 listen_address: "0.0.0.0:6514"
                 tls:
                     cert_file: '/path/to/server.crt'
                     key_file: '/path/to/server.key'
         
         exporters:
             chronicle/chronicle_w_labels:
                 protocol: https
                 # Region of your instance, for example us, europe, asia-southeast1
                 location: <LOCATION>
                 # Project number of the Google Cloud project linked to the instance
                 project: '<PROJECT_NUMBER>'
                 compression: gzip
                 # Adjust the path to the credentials file you downloaded in Step 1
                 creds_file_path: '/path/to/ingestion-authentication-file.json'
                 # Replace with your actual customer ID from Step 2
                 customer_id: <PLACEHOLDER_CUSTOMER_ID>
                 endpoint: chronicle.googleapis.com
                 # Add optional ingestion labels for better organization
                 log_type: 'CYBERARK_PRIVILEGE_CLOUD'
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
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the **Get Google SecOps credentials for the Bindplane agent** section.
  * Update `/path/to/server.crt` and `/path/to/server.key` with the actual paths to your TLS certificate and key files.

**Note:** CyberArk Privilege Cloud requires TLS for syslog connections. The Bindplane agent must be configured with a valid TLS certificate. If you use a self-signed certificate, you must import the CA certificate into CyberArk Privilege Cloud.



### Configuration without TLS (TCP only)

  * If your network architecture includes a TLS-terminating proxy between CyberArk Privilege Cloud and the Bindplane agent, you can use plain TCP:
        
        receivers:
            tcplog:
                listen_address: "0.0.0.0:514"
        


**Note:** Plain TCP without TLS is only recommended when a TLS-terminating proxy or VPN tunnel provides encryption in transit.

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
            chronicle/chronicle_w_labels:
                compression: gzip
                # Adjust the path to the credentials file you downloaded in Step 1
                creds_file_path: '/path/to/ingestion-authentication-file.json'
                # Replace with your actual customer ID from Step 2
                customer_id: <PLACEHOLDER_CUSTOMER_ID>
                endpoint: malachiteingestion-pa.googleapis.com
                # Add optional ingestion labels for better organization
                log_type: 'CYBERARK_PRIVILEGE_CLOUD'
                raw_log_field: body
                ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

  1. To restart the Bindplane agent in **Linux** , run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
         
         net stop observiq-otel-collector && net start observiq-otel-collector
         




## Configure CyberArk Privilege Cloud syslog forwarding

### Configure SIEM integration in Privilege Cloud

  1. Sign in to the **CyberArk Privilege Cloud** administration portal.
  2. Go to **Administration > Configuration Options > Options > SIEM Integration**.
  3. Select **Enable SIEM Integration** to activate syslog forwarding.
  4. Provide the following configuration details:

     * **SIEM Type** : Select **Syslog**.
     * **Syslog Server Address** : Enter the IP address or FQDN of the Bindplane agent host (for example, `syslog.example.com`).
     * **Syslog Server Port** : Enter `6514`.
     * **Protocol** : Select **TLS**.
     * **Format** : Select **CEF** (Common Event Format).
**Note:** CyberArk Privilege Cloud does not support UDP. Only TCP and TLS protocols are available for syslog forwarding.
  5. In the **Event Types** section, select the event categories to forward:

     * **Vault Audit** : Vault access and credential retrieval events.
     * **Session Audit** : Privileged session monitoring events.
     * **Safe Management** : Safe creation, modification, and deletion events.
     * **User Management** : User provisioning and permission changes.
     * **Policy Changes** : Platform and policy modification events.
  6. Click **Save**.




### Verify the TLS connection

  1. Verify the Bindplane agent is listening on port 6514:
         
         sudo ss -tlnp | grep 6514
         

  2. Verify logs are being received by checking the Bindplane agent logs:
         
         sudo journalctl -u observiq-otel-collector -f
         

  3. If no logs are received, verify the following:

     * The Bindplane agent host is reachable from the internet (CyberArk Privilege Cloud is a SaaS service).
     * Firewall rules allow inbound TCP connections on port 6514.
     * The TLS certificate is valid and not expired.
     * The TLS certificate CN or SAN matches the hostname configured in CyberArk Privilege Cloud.



For more information about CyberArk Privilege Cloud SIEM integration, see the [CyberArk Privilege Cloud documentation](https://docs.cyberark.com/privilege-cloud).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`Header.deviceVendor` | `metadata.vendor_name` | Mapped from the CEF header vendor field. Set to "CyberArk".  
`Header.deviceProduct` | `metadata.product_name` | Mapped from the CEF header product field. Set to "Privilege Cloud".  
`Header.deviceVersion` | `metadata.product_version` | Mapped from the CEF header version field.  
`Header.signatureId` | `metadata.product_event_type` | The audit action code from CEF signature ID.  
`Header.name` | `metadata.description` | The event name from CEF header.  
`Header.severity` | `security_result.severity` | Mapped from CEF severity (0-3=LOW, 4-6=MEDIUM, 7-8=HIGH, 9-10=CRITICAL).  
`suser` | `principal.user.userid` | The user who performed the action.  
`src` | `principal.ip` | The source IP address of the session.  
`shost` | `principal.hostname` | The source hostname.  
`duser` | `target.user.userid` | The target privileged account.  
`dhost` | `target.hostname` | The target system hostname.  
`dst` | `target.ip` | The target system IP address.  
`cs1` | `security_result.detection_fields` | Safe name (key: cs1Label value).  
`cs2` | `security_result.detection_fields` | Account name or additional context (key: cs2Label value).  
`cs3` | `security_result.detection_fields` | Platform ID or policy information (key: cs3Label value).  
`act` | `security_result.action_details` | The action performed (for example, Retrieve, Connect, Update).  
`reason` | `security_result.description` | The reason provided for the privileged access.  
`rt` | `metadata.event_timestamp` | The event receipt time.  
`app` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`Otherinfo` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`AffectedUserName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`RequestId` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`SafeName` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`Database` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`MessageID", "Version", "Safe", "PolicyID", "DeviceType", and "Address` | `additional.fields` | Mapped from changelog  
`GatewayStation` | `target.ip` | Mapped from changelog  
`UserName` | `principal.user.user_display_name` | Mapped from changelog  
`Station` | `principal.ip` | Mapped from changelog  
`Message` | `security_result.summary` | Mapped from changelog  
`Issuer` | `principal.user.userid` | Mapped from changelog  
`File` | `principal.file.full_path` | Mapped from changelog  
`Severity` | `security_result.severity` | Mapped from changelog  
`CPMStatus` | `security_result.action` | Mapped from changelog  
`device_version` | `metadata.product_version` | Mapped from changelog  
`device_event_class_id" and "event_name` | `metadata.product_event_type` | Mapped from changelog  
`msg` | `metadata.description` | Mapped from changelog  
`duser` | `target.user.user_display_name` | Mapped from changelog  
`suser` | `principal.user.user_display_name` | Mapped from changelog  
`cn1", "cn1Label", "cn2", "cn2Label", "cs1", "cs1Label", "cs2", "cs2Label", "cs3", "cs3Label", "cs4", "cs4Label", "cs5", "cs5Label", and "fname` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-privilege-cloud-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
