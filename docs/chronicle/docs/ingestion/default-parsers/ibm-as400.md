---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-as400/
title: Collect IBM AS/400 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:27:46.156721+00:00
---

# Collect IBM AS/400 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ibm-as400/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect IBM AS/400 logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest IBM AS/400 logs into Google Security Operations using the Bindplane agent.

IBM AS/400 is an enterprise operating system that provides integrated database, security, and application services. The system generates security audit logs through QAUDJRN (audit journal), system operation logs through QHST (history log), database journals for application data changes, and exit point logs for network access monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or a Linux host with `systemd`
  * Network connectivity between the Bindplane agent and IBM AS/400 system
  * If running behind a proxy, ensure that firewall ports are open per the Bindplane agent requirements
  * IBM AS/400 7.2 with PTF Group 19 or later, or IBM AS/400 7.3 with PTF Group 7 or later (for native syslog generation)
  * IBM AS/400 user profile with *USE authority to QAUDJRN journal and journal receivers
  * PASE for i (5770SS1 Option 33) installed on the IBM AS/400 system
  * Access to IBM AS/400 command line (5250 session or SSH)



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

  * Linux:
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * Windows:
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  1. Replace the entire contents of `config.yaml` with the following configuration:
         
         receivers:
           udplog:
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/ibm_i:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'YOUR_CUSTOMER_ID'
             endpoint: chronicle.googleapis.com
             log_type: IBM_AS400
             raw_log_field: body
             ingestion_labels:
               env: production
               source: ibm_i
         
         service:
           pipelines:
             logs/ibm_i_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/ibm_i
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514. For Linux systems running as non-root, use port `1514` or higher.
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1). Make sure that you save the credentials file as `ingestion-auth.json` in one of the following locations:

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Your Google SecOps customer ID from the previous step

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `IBM_AS400`

       * `ingestion_labels`: Optional labels for filtering and organization




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/ibm_i:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: IBM_AS400
            raw_log_field: body
            ingestion_labels:
              env: production
              source: ibm_i
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

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
           




## Configure IBM AS/400 syslog forwarding

### Enable IBM AS/400 auditing

  1. Sign in to IBM AS/400 using a 5250 terminal session or SSH.
  2. Run the following command to enable auditing:
         
         CHGSECAUD QAUDCTL(*AUDLVL) QAUDLVL(*AUTFAIL *SECURITY *CREATE *DELETE)
         

**Note:** This command creates the QAUDJRN journal if it does not exist and enables auditing for authorization failures, security events, object creation, and deletion. Adjust the QAUDLVL values based on your security requirements.



### Create the syslog configuration file

  1. Start a QShell session:
         
         STRQSH
         

  2. Create the syslog configuration directory if it does not exist:
         
         mkdir -p /QOpenSys/etc
         

  3. Create the syslog configuration file:
         
         touch /QOpenSys/etc/syslog.conf
         

  4. Edit the syslog configuration file using the `edtf` editor:
         
         edtf /QOpenSys/etc/syslog.conf
         

  5. Add the following line to forward all syslog messages to the Bindplane agent:
         
         *.* @BINDPLANE_AGENT_IP:514
         

Replace `BINDPLANE_AGENT_IP` with the IP address of the host running the Bindplane agent.

**Note:** The `@` symbol indicates UDP transport. For TCP transport, use `@@` instead. Ensure there is a tab character (not spaces) between `*.*` and the `@` symbol. The file must use LF (Line Feed) line endings only, not CRLF.
  6. Save and exit the editor:

     * Press `F3` to exit.
     * Press `F10` to save when prompted.
  7. Exit QShell:
         
         exit
         




### Start the syslog daemon

  1. Submit a batch job to start the syslog daemon:
         
         SBMJOB CMD(STRQSH CMD('/QOpenSys/usr/sbin/syslogd')) JOB(SYSLOGD) JOBQ(QSYSNOMAX)
         

  2. Verify the syslog daemon is running:
         
         STRQSH
         
         
         ps -ef | grep syslogd
         

You should see a process entry for `/QOpenSys/usr/sbin/syslogd`.

  3. Exit QShell:
         
         exit
         




### Create a script to forward audit journal entries to syslog

  1. Create a shell script to extract audit journal entries and send them to syslog:
         
         STRQSH
         

  2. Create the script file:
         
         touch /home/syslog_audit.sh
         chmod 755 /home/syslog_audit.sh
         

  3. Edit the script:
         
         edtf /home/syslog_audit.sh
         

  4. Add the following content to the script:
         
         #!/QOpenSys/pkgs/bin/bash
         
         # IBM i Audit Journal to Syslog Forwarder
         # Extracts QAUDJRN entries in syslog format and sends to syslog daemon
         
         # Get timestamp from 5 minutes ago
         START_TIME=$(date -u -d '5 minutes ago' '+%Y-%m-%d %H:%M:%S')
         
         # Query audit journal for recent entries in RFC 5424 syslog format
         system "RUNSQL SQL('SELECT syslog_event FROM TABLE(QSYS2.DISPLAY_JOURNAL(''QSYS'',''QAUDJRN'',STARTING_TIMESTAMP => ''$START_TIME'', GENERATE_SYSLOG => ''RFC 5424'')) AS X WHERE syslog_event IS NOT NULL') OUTPUT(*PRINT)" | while read -r line
         do
           if [ ! -z "$line" ]; then
             logger -p local0.info "$line"
           fi
         done
         

  5. Save and exit the editor.

  6. Exit QShell:
         
         exit
         




### Schedule the script to run periodically

  1. Create a CL program to call the shell script:
         
         CRTSRCPF FILE(QGPL/QCLSRC) RCDLEN(112)
         

  2. Add a member for the CL program:
         
         ADDPFM FILE(QGPL/QCLSRC) MBR(SYSLOGAUD)
         

  3. Edit the member:
         
         STRSEU SRCFILE(QGPL/QCLSRC) SRCMBR(SYSLOGAUD)
         

  4. Add the following CL code:
         
         PGM
           STRQSH CMD('/home/syslog_audit.sh')
         ENDPGM
         

  5. Save and exit by pressing F3.

  6. Create the CL program:
         
         CRTCLPGM PGM(QGPL/SYSLOGAUD) SRCFILE(QGPL/QCLSRC)
         

  7. Create a job schedule entry to run the program every 5 minutes:
         
         ADDJOBSCDE JOB(SYSLOGAUD) CMD(CALL PGM(QGPL/SYSLOGAUD)) FRQ(*DAILY) SCDDATE(*NONE) SCDDAY(*ALL) SCDTIME('00:00:00') RELDAYMON(*NONE)
         

**Note:** This creates a basic schedule. For production use, consider using a job scheduler or the WRKJOBSCDE command to configure more sophisticated scheduling with proper error handling and logging.



### Forward history log entries to syslog

  1. Create a similar script for history log entries:
         
         STRQSH
         

  2. Create the script file:
         
         touch /home/syslog_history.sh
         chmod 755 /home/syslog_history.sh
         

  3. Edit the script:
         
         edtf /home/syslog_history.sh
         

  4. Add the following content:
         
         #!/QOpenSys/pkgs/bin/bash
         
         # IBM i History Log to Syslog Forwarder
         
         # Get timestamp from 5 minutes ago
         START_TIME=$(date -u -d '5 minutes ago' '+%Y-%m-%d %H:%M:%S')
         
         # Query history log for recent entries in RFC 3164 syslog format
         system "RUNSQL SQL('SELECT syslog_event FROM TABLE(QSYS2.HISTORY_LOG_INFO(START_TIME => ''$START_TIME'', GENERATE_SYSLOG => ''RFC 3164'')) AS X WHERE syslog_event IS NOT NULL') OUTPUT(*PRINT)" | while read -r line
         do
           if [ ! -z "$line" ]; then
             logger -p local1.info "$line"
           fi
         done
         

  5. Save and exit the editor.

  6. Exit QShell:
         
         exit
         

  7. Create a similar CL program and job schedule for the history log script following the same steps as for the audit journal.




### Verify syslog forwarding

  1. Test the logger command to verify syslog forwarding:
         
         STRQSH
         
         
         logger -p local0.notice "Test message from IBM i"
         

  2. Check the Bindplane agent logs to verify the message was received:

**Linux:**
         
         sudo journalctl -u observiq-otel-collector -f
         

**Windows:**
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         

  3. Verify logs are appearing in Google SecOps:

     1. Sign in to the Google SecOps console.
     2. Go to **Search > UDM Search**.
     3. Search for `metadata.vendor_name = "IBM" AND metadata.product_name = "AS400"`.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
device_vendor | about.asset.asset_id | Concatenated  
device_product | about.asset.asset_id | Concatenated  
deviceExternalId | about.asset.asset_id | Concatenated  
filePath | about.file.full_path | if not empty  
fileHash | about.file.full_path | if not hash  
about_file_path | about.file.full_path | fallback  
_hash | about.file.sha256 | if not empty  
fileHash | about.file.sha256 | if hash  
fsize | about.file.size | Converted to uinteger  
dvchost | about.hostname |   
ips | about.ip | Merged array, IP validation  
dvcmac | about.mac | if valid MAC  
deviceTranslatedAddress | about.nat_ip |   
permissions | about.resource.attribute.permissions |   
additional_* | additional.fields | Merged labels  
about | about | Merged  
additional | additional | Renamed  
metadata | metadata | Renamed  
Received | metadata.collected_timestamp | Converted using yyyy-MM-ddTHH:mm:ss  
job_msg | metadata.description | if not empty  
metadata.description | metadata.description | fallback  
metadata_event_type | metadata.event_type | if not empty, else GENERIC_EVENT  
file_full_path | metadata.event_type | Set to PROCESS_UNCATEGORIZED if present  
event_name | metadata.event_type | Set to SCAN_UNCATEGORIZED if in (LogSpyware, LogPredictiveMachineLearning)  
principal machine ID + target machine ID | metadata.event_type | Set to NETWORK_HTTP if both present  
target machine ID | metadata.event_type | Set to USER_UNCATEGORIZED if present without principal  
principal machine ID | metadata.event_type | Set to STATUS_UPDATE if present  
device_event_class_id | metadata.product_event_type | Concatenated with " - " separator if both present, else alone  
event_name | metadata.product_event_type | Concatenated with " - " separator if both present, else alone  
externalId | metadata.product_log_id |   
device_product | metadata.product_name |   
device_version | metadata.product_version |   
device_vendor | metadata.vendor_name | if not empty, else "IBM - device_vendor", else "IBM"  
app_protocol_output | network.application_protocol | if not empty  
deviceDirection | network.direction | INBOUND if == 0, OUTBOUND if == 1  
requestMethod | network.http.method |   
requestClientApplication | network.http.user_agent |   
ip_protocol_out | network.ip_protocol | if not empty  
in | network.received_bytes | Converted to uinteger  
out | network.sent_bytes | Converted to uinteger  
observer | observer | Renamed  
principal | principal | Renamed  
sntdom | principal.administrative_domain |   
sourceServiceName | principal.application | if not empty  
name | principal.application | fallback  
hardware | principal.asset.hardware | Merged  
hostname | principal.asset.hostname | if not empty  
hostinfo.name | principal.asset.hostname | fallback  
hostinfo.hostname | principal.asset.hostname | fallback  
host | principal.asset.ip | Merged  
src | principal.asset.ip | Merged  
principal_ip | principal.asset.ip | Merged  
hostinfo.ip | principal.asset.ip | Merged array  
log.file.path | principal.file.full_path |   
Group_name | principal.group.group_display_name | if not empty  
Gruppenavn | principal.group.group_display_name | fallback  
Device_name | principal.hostname | if not empty  
Enhetsnavn | principal.hostname | fallback  
principal_ip | principal.ip | Merged  
src | principal.ip | Merged  
host | principal.ip | Merged  
hostinfo.ip | principal.ip | Merged array  
smac | principal.mac | Merged  
hostinfo.mac | principal.mac | Merged array  
sourceTranslatedAddress | principal.nat_ip |   
hostinfo.os.platform | principal.platform | if not empty  
hostinfo.os.name | principal.platform | WINDOWS if matches (?i)Window, LINUX if matches (?i)Linux  
hostinfo.os.kernel | principal.platform_patch_level |   
hostinfo.os.version | principal.platform_version |   
spt | principal.port | Converted to integer  
deviceProcessName | principal.process.command_line | if not empty  
sproc | principal.process.command_line | fallback  
Subject | principal.process.command_line | fallback  
Emne | principal.process.command_line | fallback  
Path | principal.process.command_line | fallback  
File_name | principal.process.file.full_path | if not empty  
Object | principal.process.file.full_path | fallback  
Objekt | principal.process.file.full_path | fallback  
Infected_Resource | principal.process.file.full_path | fallback  
spid | principal.process.pid |   
codename_label | principal.resource.attribute.labels | Merged  
family_label | principal.resource.attribute.labels | Merged  
log_offset_label | principal.resource.attribute.labels | Merged  
version_label | principal.resource.attribute.labels | Merged  
hostinfo.id | principal.resource.product_object_id |   
principal_role | principal.user.attribute.roles |   
temp_duser | principal.user.user_display_name | if not empty  
suser | principal.user.user_display_name | fallback  
CustomerName | principal.user.user_display_name | fallback  
temp_duid | principal.user.userid | if not empty  
suid | principal.user.userid | fallback  
user_name | principal.user.userid | fallback  
User | principal.user.userid | fallback  
Bruker | principal.user.userid | fallback  
security_result | security_result | Merged  
act | security_result.action | ALLOW if in (accept, notified); BLOCK if in (deny, blocked)  
outcome | security_result.action | ALLOW if REDIRECTED_USER_MAY_PROCEED; BLOCK if BLOCKED; FAIL if Failure  
categoryOutcome | security_result.action | ALLOW if Success; BLOCK if Failure  
cs2 | security_result.action | ALLOW if Allow; BLOCK if Denied  
act | security_result.action_details | if not empty  
Action_Taken | security_result.action_details | fallback  
cat | security_result.category_details |   
msg_data_2 | security_result.description | if not empty  
security_result.description | security_result.description | fallback  
Type | security_result.description | fallback  
Scan_Type | security_result.description | fallback  
operation_label | security_result.detection_fields | Merged  
operasjon_label | security_result.detection_fields | Merged  
permission_label | security_result.detection_fields | Merged  
tillatelse_label | security_result.detection_fields | Merged  
infection_channel_label | security_result.detection_fields | Merged  
spyware_Grayware_Type_label | security_result.detection_fields | Merged  
threat_probability_label | security_result.detection_fields | Merged  
mwProfile | security_result.rule_name |   
severity | security_result.severity | LOW if 0-3 or LOW; MEDIUM if 4-6 or MEDIUM/INFO/SUBSTANTIAL; HIGH if 7-8 or HIGH/SEVERE; CRITICAL if 9-10 or VERY-HIGH/CRITICAL  
appcategory | security_result.summary | if not empty  
Result | security_result.summary | fallback  
reason | security_result.summary | fallback  
Spyware | security_result.threat_name | if not empty  
Virus_Malware_Name | security_result.threat_name | fallback  
Unknown_Threat | security_result.threat_name | fallback  
oldFilePath | src.file.full_path |   
oldFileSize | src.file.size | Converted to uinteger  
old_permissions | src.resource.attribute.permissions |   
target | target | Renamed  
dntdom | target.administrative_domain |   
destinationServiceName | target.application |   
logcollector_hostname | target.asset.hostname |   
dst | target.asset.ip | Merged  
dst_ip | target.asset.ip | Merged  
temp_dhost | target.hostname | if not empty  
shost | target.hostname | if not IP  
dst_ip | target.ip | Merged  
dst | target.ip | Merged  
IPv6_Address | target.ip | Merged  
dmac | target.mac |   
destination_translated_address | target.nat_ip |   
destinationTranslatedPort | target.nat_port | Converted to integer  
dpt | target.port | Converted to integer  
dproc | target.process.command_line |   
file_full_path | target.process.file.full_path |   
dpid | target.process.pid |   
resource_Type_label | target.resource.attribute.labels | Merged  
request | target.url |   
target_role | target.user.attribute.roles |   
temp_duser | target.user.user_display_name | if not empty  
CustomerName | target.user.user_display_name | fallback  
temp_duid | target.user.userid | if not empty  
User | target.user.userid | fallback  
Bruker | target.user.userid | fallback  
logcollector_timestamp | metadata.collected_timestamp | Converted using ISO8601 or MMM d HH:mm:ss  
metadata_event_type | metadata.event_type | if not empty, else GENERIC_EVENT  
event_type | metadata.product_event_type | if not empty  
product_event_type | metadata.product_event_type | fallback  
device_vendor | metadata.vendor_name | if not empty, else "IBM"  
device_product | metadata.product_name |   
agent.hostname | observer.asset.hostname |   
agent.type | observer.asset_id | Concatenated  
agent.id | observer.asset_id | Concatenated  
agent.version | observer.platform_version |   
sntdom | principal.administrative_domain |   
sourceServiceName | principal.application |   
hostname | principal.asset.hostname |   
host | principal.asset.ip | Merged  
src | principal.asset.ip | Merged  
hostinfo.ip | principal.asset.ip | Merged array  
log.file.path | principal.file.full_path |   
hostname | principal.hostname |   
principal_ip | principal.ip | Merged  
src | principal.ip | Merged  
host | principal.ip | Merged  
hostinfo.ip | principal.ip | Merged array  
smac | principal.mac | Merged  
hostinfo.mac | principal.mac | Merged array  
hostinfo.os.platform | principal.platform |   
hostinfo.os.kernel | principal.platform_patch_level |   
hostinfo.os.version | principal.platform_version |   
spt | principal.port | Converted to integer  
sproc | principal.process.command_line |   
spid | principal.process.pid |   
codename_label | principal.resource.attribute.labels | Merged  
family_label | principal.resource.attribute.labels | Merged  
log_offset_label | principal.resource.attribute.labels | Merged  
version_label | principal.resource.attribute.labels | Merged  
hostinfo.id | principal.resource.product_object_id |   
suser | principal.user.user_display_name |   
suid | principal.user.userid |   
act | security_result.action | ALLOW if in (accept, notified); BLOCK if in (deny, blocked)  
outcome | security_result.action | ALLOW if REDIRECTED_USER_MAY_PROCEED; BLOCK if BLOCKED; FAIL if Failure  
categoryOutcome | security_result.action | ALLOW if Success; BLOCK if Failure  
cs2 | security_result.action | ALLOW if Allow; BLOCK if Denied  
act | security_result.action_details |   
cat | security_result.category_details |   
msg_data_2 | security_result.description |   
mwProfile | security_result.rule_name |   
severity | security_result.severity | LOW if 0-3; MEDIUM if 4-6; HIGH if 7-8; CRITICAL if 9-10  
reason | security_result.summary |   
logcollector_hostname | target.asset.hostname |   
dst | target.asset.ip | Merged  
temp_dhost | target.hostname |   
dst_ip | target.ip | Merged  
mac_address | target.mac |   
dpt | target.port | Converted to integer  
dproc | target.process.command_line |   
dpid | target.process.pid |   
temp_duser | target.user.user_display_name |   
temp_duid | target.user.userid |   
`target_userid` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`process` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_info` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`log_event` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`event_type` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`sev` | `event.idm.read_only_udm.severity` | Mapped from changelog  
`access_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`actual_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`jrn_seq` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`job_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`user_name` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`job_number` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`eff_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`logical_partition` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`auth_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`cmd_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`object` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`object_library` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`object_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ifs_path` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`specific_data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ip_addr` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`port` | `event.idm.read_only_udm.principal.port` | Mapped from changelog  
`action` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`val_job` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`val_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`val_jobno` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pgm_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`pgm_libr` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`workstation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`causing_user` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`field` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`op_violation` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-as400-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
