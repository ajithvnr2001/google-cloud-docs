---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardium/
title: Collect IBM Guardium logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:53:20.579374+00:00
---

# Collect IBM Guardium logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardium/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM Guardium logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM Guardium logs to Google Security Operations using Bindplane.

IBM Guardium is a database activity monitoring and data protection platform that provides real-time monitoring, auditing, and protection for databases and file systems. Guardium offers vulnerability assessment, data discovery and classification, database activity monitoring, and compliance reporting capabilities.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and IBM Guardium Collector
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to the IBM Guardium CLI
  * IBM Guardium version 9.1 or later for encrypted syslog support (optional)



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
          chronicle/guardium:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: GUARDIUM
            raw_log_field: body
            ingestion_labels:
              log_source: guardium
        
        service:
          pipelines:
            logs/guardium_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/guardium
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * Use `udplog` for UDP syslog (most common for Guardium).
    * Use `tcplog` for TCP syslog if required.
    * Listen address `0.0.0.0:514` listens on all interfaces on port 514.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID from the previous step.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `log_type`: Must be `GUARDIUM`.
    * `ingestion_labels`: Optional labels in YAML format.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/guardium:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: GUARDIUM
            raw_log_field: body
            ingestion_labels:
              log_source: guardium
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

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

      1. Press `Win+R`, type `services.msc`, and press **Enter**.
      2. Locate **observIQ OpenTelemetry Collector**.
      3. Right-click and select **Restart**.

      4. Verify the service is running:
             
             sc query observiq-otel-collector
             

      5. Check logs for errors:
             
             type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
             




## Configure IBM Guardium syslog forwarding

### Configure syslog destination via CLI

To create a syslog destination for events on IBM Guardium, you must log in to the command-line interface and define the IP address for the Bindplane agent host.

  1. Using SSH, log in to IBM Guardium Collector as the CLI user.
  2. Type the following commands to configure the syslog destination:

     * **For UDP syslog (recommended):**
           
           store remotelog add non_encrypted daemon.all BINDPLANE_AGENT_IP udp
           

     * **For TCP syslog:**
           
           store remotelog add non_encrypted daemon.all BINDPLANE_AGENT_IP:514 tcp
           

     * **For specific severity levels:**
           
           store remotelog add non_encrypted daemon.alert BINDPLANE_AGENT_IP udp
           store remotelog add non_encrypted daemon.err BINDPLANE_AGENT_IP udp
           store remotelog add non_encrypted daemon.warning BINDPLANE_AGENT_IP udp
           

       * Replace `BINDPLANE_AGENT_IP` with the IP address of the host where Bindplane agent is installed.
  3. Verify the configuration by running:
         
         show remotelog
         

The output should display your configured remote syslog destination.

**Note:** Guardium application messages originate from the `daemon` facility. The priority levels (`alert`, `err`, `warning`) correspond to severity levels configured in Guardium policies.



### Configure encrypted syslog (optional)

If you require encrypted syslog forwarding, IBM Guardium version 9.1 and above supports TLS encryption over TCP.

  1. Obtain the public certificate in PEM format from the certificate authority used by your remote syslog receiver.
  2. Log in to the CLI on the Guardium Collector.
  3. Type the following command:
         
         store remotelog add encrypted daemon.all BINDPLANE_AGENT_IP:6514 tcp
         

  4. When prompted, paste the CA certificate in PEM format, including the BEGIN and END lines, then press `Ctrl+D`.

  5. Guardium stores the certificate as `/etc/pki/rsyslog/ca.pem`.

**Note:** Encryption works only in TCP mode. Without the `tcp` parameter, syslog forwarding defaults to UDP, and encryption does not work.



### Configure message template (optional)

Guardium supports multiple message formats including CEF (Common Event Format) and LEEF (Log Event Extended Format). The default format is suitable for most deployments.

To customize the message template:

  1. Sign in to the Guardium appliance GUI as a user with admin privileges.
  2. Go to **Administration Console > Configuration > Global Profile**.
  3. In the **Message Template** section, edit the template with your desired format.
  4. Click **Save**.

**Note:** Message template changes affect only remote log shipping and require restarting the inspection engines.

## Configure policy to send alerts to syslog

Policies in IBM Guardium are responsible for reacting to events and forwarding the event information to the remote syslog receiver.

### Configure policy alert action

  1. Sign in to the Guardium appliance GUI.
  2. Click the **Tools** tab.
  3. From the left navigation, select **Policy Builder**.
  4. From the **Policy Finder** pane, select an existing policy and click **Edit Rules**.
  5. Click **Edit this Rule individually**.
  6. The **Access Rule Definition** is displayed.
  7. Click **Add Action**.
  8. From the **Action** list, select one of the following alert types: 
     * **Alert Per Match** : A notification is provided for every policy violation.
     * **Alert Daily** : A notification is provided the first time a policy violation occurs that day.
     * **Alert Once Per Session** : A notification is provided per policy violation for unique session.
     * **Alert Per Time Granularity** : A notification is provided per your selected timeframe.
  9. From the **Message Template** list, select the required template or keep **Default**.
  10. From **Notification Type** , select **SYSLOG**.
  11. Click **Add** , then click **Apply**.
  12. Click **Save**.
  13. Repeat this process for all rules within the policy that you want to forward to Google SecOps.



### Install the policy

Any new or edited policy in IBM Guardium must be installed before the updated alert actions or rule changes can occur.

  1. Click the **Administration Console** tab.
  2. From the left navigation, select **Configuration > Policy Installation**.
  3. From the **Policy Installer** pane, select the policy that you modified in the previous step.
  4. From the drop-down list, select **Install and Override**.
  5. A confirmation is displayed to install the policy to all Inspection Engines.
  6. Click **OK**.

**Note:** Alerts sent to the syslog server are sent from the Collector. Ensure you configure syslog forwarding on the Collector appliance that generates the alerts.

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
deviceNtDomain | about.administrative_domain | Administrative domain of the about entity  
deviceExternalId | about.asset.asset_id | Asset identifier  
filePath, fileHash | about.file.full_path | Full path of the file  
_hash, fileHash | about.file.sha256 | SHA256 hash of the file  
fsize | about.file.size | Size of the file  
dvchost | about.hostname | Hostname of the about entity  
dvc | about.ip | IP address of the about entity  
smac, dmac, dvcmac | about.mac | MAC address of the about entity  
deviceProcessName, Subject, Emne, Path | about.process.command_line | Command line of the process  
dvcpid | about.process.pid | Process ID  
filePermission | about.resource.attribute.permissions | Permissions associated with the resource  
| extensions.auth.type | Authentication type  
sender_ip | intermediary.ip | IP address of the intermediary  
| intermediary | Intermediary entity details  
Received, Generated, timestamp | metadata.collected_timestamp | Timestamp when the event was collected  
msg, signature_name | metadata.description | Description of the event  
| metadata.event_type | Type of event (e.g., USER_LOGIN, NETWORK_CONNECTION)  
device_event_class_id, event_name, eventType | metadata.product_event_type | Product-specific event type  
externalId | metadata.product_log_id | Product log identifier  
| metadata.product_version | Version of the product  
| network.application_protocol | Application protocol used in the network connection  
deviceDirection | network.direction | Direction of the network traffic  
requestMethod | network.http.method | HTTP method used in the request  
requestClientApplication | network.http.user_agent | User agent string from the HTTP request  
proto | network.ip_protocol | IP protocol used  
in | network.received_bytes | Number of bytes received  
out | network.sent_bytes | Number of bytes sent  
session_id | network.session_id | Session identifier for the network connection  
sntdom, Domain, Domene | principal.administrative_domain | Administrative domain of the principal  
sourceServiceName, source_program | principal.application | Application associated with the principal  
prin_host, Device_name, Enhetsnavn, shost, principal_hostname, client_hostname | principal.asset.hostname | Hostname of the principal asset  
sender_ip, src_ip, src, principal_ip, client_ip | principal.asset.ip | IP address of the principal asset  
Group_name, Gruppenavn | principal.group.group_display_name | Display name of the principal group  
prin_host, Device_name, Enhetsnavn, shost, principal_hostname, client_hostname | principal.hostname | Hostname of the principal  
sender_ip, src_ip, src, principal_ip, client_ip | principal.ip | IP address of the principal  
smac | principal.mac | MAC address of the principal  
sourceTranslatedAddress | principal.nat_ip | NAT IP address of the principal  
sourceTranslatedPort | principal.nat_port | NAT port of the principal  
spt, client_port | principal.port | Port used by the principal  
sproc | principal.process.command_line | Command line of the principal process  
spid | principal.process.pid | Process ID of the principal  
spriv | principal.user.attribute.roles | Roles associated with the principal user  
suser, usrName, CustomerName | principal.user.user_display_name | Display name of the principal user  
dbUser, usrName, db_user, os_user, suid, db_username | principal.user.userid | User ID of the principal  
| security_result | Security result details  
| security_result.action | Action taken in the security result  
act, Action_Taken | security_result.action_details | Details of the action taken  
cat | security_result.category_details | Category details of the security result  
msg_data_2, alert_description, Type, Scan_Type | security_result.description | Description of the security result  
operation_label, operasjon_label, permission_label, tillatelse_label, infection_channel_label, spyware_Grayware_Type_label, threat_probability_label | security_result.detection_fields | Fields used for detection in the security result  
mwProfile, alert_name | security_result.rule_name | Name of the rule that triggered the security result  
severity, event_severity | security_result.severity | Severity level of the security result  
reason, ruleDesc, appcategory, Result | security_result.summary | Summary of the security result  
Spyware, Virus_Malware_Name, Unknown_Threat | security_result.threat_name | Name of the threat detected  
oldFilePath | src.file.full_path | Full path of the source file  
oldFileSize | src.file.size | Size of the source file  
oldFilePermission | src.resource.attribute.permissions | Permissions of the source resource  
os_user | src.user.userid | User ID of the source user  
dntdom | target.administrative_domain | Administrative domain of the target  
destinationServiceName, service_name | target.application | Application associated with the target  
prin_host, dest_host, server_hostname | target.asset.hostname | Hostname of the target asset  
dst_ip, dest_ip, server_ip, IPv6_Address | target.asset.ip | IP address of the target asset  
temp_dhost, dest_host, server_hostname | target.hostname | Hostname of the target  
dst_ip, dst, dest_ip, server_ip, IPv6_Address | target.ip | IP address of the target  
dmac | target.mac | MAC address of the target  
destinationTranslatedAddress | target.nat_ip | NAT IP address of the target  
destinationTranslatedPort | target.nat_port | NAT port of the target  
dpt, dstPort, dest_port, server_port | target.port | Port used by the target  
dproc, full_sql | target.process.command_line | Command line of the target process  
File_name, Object, Objekt, Infected_Resource | target.process.file.full_path | Full path of the target process file  
dpid, full_sql_id | target.process.pid | Process ID of the target  
session_start | target.resource.attribute.creation_time | Creation time of the target resource  
additional_environment_name, additional_db_protocol_version, additional_dbProtocolVersion, additional_operation_name, additional_signature_id, resource_Type_label | target.resource.attribute.labels | Labels associated with the target resource  
session_end | target.resource.attribute.last_update_time | Last update time of the target resource  
db_name, database_name | target.resource.name | Name of the target resource  
db_type, server_type | target.resource.resource_subtype | Subtype of the target resource  
| target.resource.resource_type | Type of the target resource  
request | target.url | URL associated with the target  
dpriv, roles | target.user.attribute.roles | Roles associated with the target user  
temp_duser, CustomerName | target.user.user_display_name | Display name of the target user  
temp_duid, User, Bruker, db_username | target.user.userid | User ID of the target  
| metadata.product_name | Name of the product  
| metadata.vendor_name | Name of the vendor  
`query` | `additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardium-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
