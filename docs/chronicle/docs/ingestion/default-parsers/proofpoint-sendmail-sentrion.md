---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-sendmail-sentrion/
title: Collect Proofpoint Sendmail Sentrion logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:12.585815+00:00
---

# Collect Proofpoint Sendmail Sentrion logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-sendmail-sentrion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Proofpoint Sendmail Sentrion logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Proofpoint Sendmail Sentrion logs to Google Security Operations using the Bindplane agent.

Proofpoint Sendmail Sentrion is an enterprise mail transfer agent (MTA) that provides security controls, message tracking, and policy enforcement for outbound and inbound email. It logs mail transactions through the standard syslog `mail` facility.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the Proofpoint Sendmail Sentrion MTA server
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the Proofpoint Sendmail Sentrion server with root or administrator permissions



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
          chronicle/proofpoint_sentrion:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: chronicle.googleapis.com
            log_type: PROOFPOINT_SENDMAIL_SENTRION
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/sentrion_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/proofpoint_sentrion
        




### Configuration parameters

  * Replace the following placeholders:

  * **Receiver configuration:**

    * `udplog`: Receives syslog over UDP. Use `tcplog` if you configured TCP transport in the syslog configuration.
    * `0.0.0.0:514`: Listens on all interfaces on port 514. Change the port if needed (for example, `1514` for non-root Linux).
  * **Exporter configuration:**

    * `<CREDS_FILE_PATH>`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `<CUSTOMER_ID>`: Customer ID from the **Get Google SecOps customer ID** step.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/proofpoint_sentrion:
            compression: gzip
            creds_file_path: '<CREDS_FILE_PATH>'
            customer_id: '<CUSTOMER_ID>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: PROOFPOINT_SENDMAIL_SENTRION
            raw_log_field: body
            ingestion_labels:
              env: production
        


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
             




## Configure Proofpoint Sendmail Sentrion syslog forwarding

Sendmail Sentrion uses the standard syslog `mail` facility to write mail transaction logs. The default log locations depend on the operating system:

OS | Default log path  
---|---  
**RHEL / CentOS** | `/var/log/maillog`  
**Debian / Ubuntu** | `/var/log/mail.log`  
**Solaris** | `/var/log/syslog` (filtered by `mail.*`)  
**Note:** The Sentrion management console may configure additional log paths under `/var/log/sentrion/` or a custom directory. Check the Sentrion configuration for the exact path.

### Option 1: Configure syslog forwarding using rsyslog

  1. Edit the syslog configuration file on the Sentrion MTA server:
         
         sudo nano /etc/rsyslog.d/sentrion.conf
         

  2. Add the following rule to forward mail facility logs to the Bindplane agent:
         
         mail.*    @BINDPLANE_AGENT_IP:514
         

**Note:** Use `@` for UDP or `@@` for TCP transport. Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host.
  3. Save the file and restart the rsyslog service:
         
         sudo systemctl restart rsyslog
         

  4. Verify that logs are being forwarded by checking the Bindplane agent logs.




### Option 2: Configure syslog forwarding via the Sentrion management console

  1. Sign in to the **Sentrion management console**.
  2. Navigate to **Configuration > Logging** (or **System > Log Settings**).
  3. Configure remote syslog settings: 
     * **Syslog server** : Enter the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * **Port** : Enter `514` (must match the Bindplane agent receiver port).
     * **Protocol** : Select **UDP** (must match the Bindplane agent receiver configuration).
     * **Log level** : Set to capture all mail transaction events.
  4. Click **Apply** or **Save**.
  5. Verify that logs are being forwarded by checking the Bindplane agent logs.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| additional.fields | Merged from tty_label and pwd_label  
action | security_result.action_details | Value copied directly  
action_result | security_result.summary | Value copied directly if present  
app | principal.application | Value copied directly  
app_proto | network.application_protocol | Value copied directly  
auth | security_result.detection_fields | Merged as auth_label (key: auth, value: auth)  
bits | security_result.detection_fields | Merged as bits_label (key: bits, value: bits)  
categorization | security_result.category_details | Value copied directly  
cipher | network.tls.cipher | Value copied directly  
class | security_result.detection_fields | Merged as class_label (key: class, value: class)  
cluster | principal.resource.attribute.labels | Merged as cluster_label (key: cluster, value: cluster)  
COMMAND | principal.process.command_line | Value copied directly  
daemon | security_result.detection_fields | Merged as daemon_label (key: daemon, value: daemon)  
delay | security_result.detection_fields | Merged as delay_label (key: delay, value: delay)  
description | security_result.description | Value copied directly  
details | metadata.description | Value copied directly  
disposition | security_result.detection_fields | Merged as disposition_label (key: disposition, value: disposition)  
dsn | security_result.detection_fields | Merged as dsn_label (key: dsn, value: dsn)  
event_type | metadata.event_type | Value copied directly  
from | network.email.from | Extracted as valid_from using grok pattern if valid email  
host | principal.asset.hostname, principal.hostname | Value copied directly  
ip | principal.asset.ip, principal.ip | Value copied directly  
job_name | principal.resource.attribute.labels | Merged as job_name_label (key: job_name, value: job_name)  
mailer | security_result.detection_fields | Merged as mailer_label (key: mailer, value: mailer)  
msgid | network.email.mail_id | Value copied directly after removing < and >  
mtaqid | principal.resource.product_object_id | Value copied directly  
nw_direction | network.direction | Set to OUTBOUND if matches (?i)Outbound  
nrcpts | security_result.detection_fields | Merged as nrcpts_label (key: nrcpts, value: nrcpts)  
pid | principal.process.pid | Value copied directly  
port | principal.port | Value copied directly and converted to integer  
pri | security_result.detection_fields | Merged as pri_label (key: priority, value: pri)  
processor | principal.resource.attribute.labels | Merged as processor_label (key: processor, value: processor)  
product_event_type | metadata.product_event_type | Value copied directly  
reject_msg | security_result.summary | Value copied directly if action_result, stat, and status empty  
relay_domain | intermediary.hostname | Value copied directly  
relay_ip | intermediary.ip | Value copied directly  
ruleset | security_result.rule_name | Value copied directly  
severity | security_result.severity | Set to INFORMATIONAL if matches (?i)info  
size | network.sent_bytes | Value copied directly and converted to uinteger  
STARTTLS | security_result.detection_fields | Merged as starttls_label (key: STARTTLS, value: STARTTLS)  
stat | security_result.summary | Value copied directly if action_result empty  
status | security_result.summary | Value copied directly if action_result, stat, and reject_msg empty  
subject | network.email.subject, security_result.detection_fields | Value copied directly and merged as subject_label (key: subject, value: subject)  
tls_verify, verify | security_result.action, security_result.description | Set to ALLOW if matches (?i)OK, BLOCK if matches (?i)FAIL; description set to tls_verify - tls_verify; tls_verify from verify if tls_verify empty  
to | network.email.to | Extracted as valid_to from array using grok pattern for each email  
USER, user | principal.user.userid | Value from USER if not empty, else from user  
version | network.tls.version | Value copied directly  
xdelay | security_result.detection_fields | Merged as xdelay_label (key: xdelay, value: xdelay)  
| metadata.product_name | Set to "Proofpoint Sendmail Sentrion"  
| metadata.vendor_name | Set to "PROOFPOINT_SENDMAIL_SENTRION"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-sendmail-sentrion-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
