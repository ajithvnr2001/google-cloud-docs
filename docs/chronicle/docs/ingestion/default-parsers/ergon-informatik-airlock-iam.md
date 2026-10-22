---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam/
title: Collect Ergon Informatik Airlock IAM logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:39.218179+00:00
---

# Collect Ergon Informatik Airlock IAM logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ergon-informatik-airlock-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Ergon Informatik Airlock IAM logs

**Parser Version:** 3.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Ergon Informatik Airlock IAM logs into Google Security Operations using the Bindplane agent.

Airlock IAM is an identity and access management solution that provides authentication, authorization, and user self-service capabilities. It generates structured JSON logs for authentication events, user trail activities, audit logs, and administrative actions across its Loginapp, Adminapp, Transaction Approval, Service Container, and API Policy Service modules.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or a Linux host with `systemd`
  * Network connectivity between the Bindplane agent and Airlock IAM server
  * If running behind a proxy, ensure that firewall ports are open according to the Bindplane agent requirements
  * Administrative access to the Airlock IAM instance
  * SSH or console access to the Airlock IAM server to edit configuration files



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
         

The service status should be **RUNNING**.




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         

The service status should be **active (running)**.




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
           chronicle/airlock_iam:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'YOUR_CUSTOMER_ID'
             endpoint: chronicle.googleapis.com
             log_type: ERGON_INFORMATIK_AIRLOCK_IAM
             raw_log_field: body
             ingestion_labels:
               env: production
               source: airlock_iam
         
         service:
           pipelines:
             logs/airlock_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/airlock_iam
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on port 51. For Linux systems running as non-root, use port `1514` or higher.
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `YOUR_CUSTOMER_ID`: Replace with your Google SecOps customer ID from the previous step

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `ingestion_labels`: Optional labels to categorize logs (modify as needed)




### Example configuration for Windows
    
    
    receivers:
      udplog:
        listen_address: "0.0.0.0:514"
    
    exporters:
      chronicle/airlock_iam:
        protocol: https
        # Region of your instance, for example us, europe, asia-southeast1
        location: <LOCATION>
        # Project number of the Google Cloud project linked to the instance
        project: '<PROJECT_NUMBER>'
        compression: gzip
        creds_file_path: 'C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json'
        customer_id: 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'
        endpoint: chronicle.googleapis.com
        log_type: ERGON_INFORMATIK_AIRLOCK_IAM
        raw_log_field: body
        ingestion_labels:
          env: production
          source: airlock_iam
    
    service:
      pipelines:
        logs/airlock_to_chronicle:
          receivers:
            - udplog
          exporters:
            - chronicle/airlock_iam
    

### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/airlock_iam:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: ERGON_INFORMATIK_AIRLOCK_IAM
            raw_log_field: body
            ingestion_labels:
              env: production
              source: airlock_iam
        


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
           




## Configure Airlock IAM syslog forwarding

  1. Connect to the Airlock IAM server using SSH or console access.
  2. Navigate to the instance directory:
         
         cd /opt/airlock/iam/instances/<instance_name>/
         

**Note:** Replace `<instance_name>` with your actual Airlock IAM instance name (for example, `default`).
  3. Edit the Log4j configuration file for all modules:
         
         nano log4j/all-modules.xml
         

  4. Add the Syslog appender configuration in the `<Appenders>` section:
         
         <Syslog name="SYSLOG" 
                 facility="LOCAL1" 
                 host="BINDPLANE_AGENT_IP" 
                 port="514" 
                 protocol="UDP" 
                 format="RFC 5424" 
                 includeMDC="true" 
                 mdcId="mdc" 
                 newLine="true">
             <ExceptionPattern>%ex{full}</ExceptionPattern>
             <ThresholdFilter level="INFO"/>
         </Syslog>
         

  5. Configure the Syslog appender parameters:

     * **host** : Replace `BINDPLANE_AGENT_IP` with the IP address of the Bindplane agent host (for example, `192.168.1.100`)
     * **port** : Set to `514` (or `1514` if Bindplane agent is configured for non-privileged port)
     * **protocol** : Set to `UDP` (or `TCP` if you configured tcplog receiver in Bindplane)
     * **format** : Set to `RFC 5424` for structured syslog format
     * **facility** : Set to `LOCAL1` (or another facility code as needed: `LOCAL0` through `LOCAL7`)
     * **ThresholdFilter level** : Set to `INFO` to send INFO and higher severity logs, or `DEBUG` for all logs
  6. Add the appender reference inside the `<Root>` logger section:
         
         <Loggers>
           <Root level="${sys:iam.log.level}">
             <AppenderRef ref="SYSLOG"/>
           </Root>
         </Loggers>
         

  7. Complete example configuration:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <Configuration name="Custom Log4j 2 Configuration for All IAM Modules">
           <Appenders>
             <Syslog name="SYSLOG" 
                     facility="LOCAL1" 
                     host="192.168.1.100" 
                     port="514" 
                     protocol="UDP" 
                     format="RFC 5424" 
                     includeMDC="true" 
                     mdcId="mdc" 
                     newLine="true">
               <ExceptionPattern>%ex{full}</ExceptionPattern>
               <ThresholdFilter level="INFO"/>
             </Syslog>
           </Appenders>
           <Loggers>
             <Root level="${sys:iam.log.level}">
               <AppenderRef ref="SYSLOG"/>
             </Root>
           </Loggers>
         </Configuration>
         

  8. Save the configuration file:

Press `Ctrl+O`, then `Enter`, then `Ctrl+X`

  9. The Log4j configuration is monitored for changes every 60 seconds by default. The new syslog forwarding will activate automatically without requiring a restart.

  10. Verify that logs are being sent to the Bindplane agent:
         
         sudo journalctl -u observiq-otel-collector -f
         

**Note:** You should see log entries being received and forwarded to Google SecOps.
  11. Verify that logs are arriving in Google SecOps:

     1. Sign in to the Google SecOps console.
     2. Go to **SIEM > Search**.
     3. Run a search query:
            
            metadata.log_type = "ERGON_INFORMATIK_AIRLOCK_IAM"
            

     4. Verify that Airlock IAM logs appear in the search results.




## Additional configuration options

### Configure TCP syslog instead of UDP

If you prefer TCP delivery instead of UDP:

  1. In the Bindplane agent `config.yaml` file, change the receiver to `tcplog`:
         
         receivers:
           tcplog:
             listen_address: "0.0.0.0:514"
         

  2. In the Airlock IAM `log4j/all-modules.xml` file, change the protocol to `TCP`:
         
         <Syslog name="SYSLOG" 
                 facility="LOCAL1" 
                 host="192.168.1.100" 
                 port="514" 
                 protocol="TCP" 
                 format="RFC 5424" 
                 includeMDC="true" 
                 mdcId="mdc" 
                 newLine="true">
           <ExceptionPattern>%ex{full}</ExceptionPattern>
           <ThresholdFilter level="INFO"/>
         </Syslog>
         

  3. Restart the Bindplane agent to apply the receiver change.




### Configure different log levels

  * To send only WARNING and higher severity logs:
        
        <ThresholdFilter level="WARN"/>
        

  * To send all logs including DEBUG:
        
        <ThresholdFilter level="DEBUG"/>
        




Available log levels, from lowest to highest severity:

  * `TRACE`
  * `DEBUG`
  * `INFO`
  * `WARN`
  * `ERROR`
  * `FATAL`



### Configure multiple Airlock IAM instances

  * If you have multiple Airlock IAM instances sending to the same Bindplane agent, use ingestion labels to differentiate them:
        
        exporters:
          chronicle/airlock_iam_prod:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: ERGON_INFORMATIK_AIRLOCK_IAM
            raw_log_field: body
            ingestion_labels:
              env: production
              instance: prod-iam-01
        
          chronicle/airlock_iam_dev:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: chronicle.googleapis.com
            log_type: ERGON_INFORMATIK_AIRLOCK_IAM
            raw_log_field: body
            ingestion_labels:
              env: development
              instance: dev-iam-01
        
        service:
          pipelines:
            logs/airlock_prod:
              receivers:
                - udplog
              exporters:
                - chronicle/airlock_iam_prod
        
            logs/airlock_dev:
              receivers:
                - udplog
              exporters:
                - chronicle/airlock_iam_dev
        

**Note:** Configure each Airlock IAM instance to send logs to the same Bindplane agent IP address and port. Use ingestion labels to filter logs in Google SecOps.



## Troubleshooting

### Logs not appearing in Google SecOps

  1. Verify that the Bindplane agent is receiving logs:
         
         sudo journalctl -u observiq-otel-collector -f
         

  2. Check for network connectivity from Airlock IAM to the Bindplane agent:
         
         telnet BINDPLANE_AGENT_IP 514
         

  3. Verify that the Log4j configuration is valid:
         
         cat /opt/airlock/iam/instances/<instance_name>/log4j/all-modules.xml
         

  4. Check Airlock IAM logs for errors:
         
         tail -f /opt/airlock/iam/instances/<instance_name>/logs/loginapp.log
         




### Bindplane agent errors

  1. Check Bindplane agent logs for errors:
         
         sudo journalctl -u observiq-otel-collector -n 100
         

  2. Verify that the `config.yaml` syntax is correct. YAML is indentation-sensitive.

  3. Verify that the ingestion authentication file path is correct and that the file exists.

  4. Test network connectivity to the Google SecOps endpoint:
         
         curl -v https://chronicle.googleapis.com
         




### Firewall configuration

Ensure the following firewall rules are configured:

**Inbound to Bindplane agent:**

  * Protocol: UDP (or TCP if using tcplog)
  * Port: 514 (or your configured port)
  * Source: Airlock IAM server IP address



**Outbound from Bindplane agent:**

  * Protocol: HTTPS (TCP 443)
  * Destination: Google SecOps regional endpoint
  * Purpose: Log delivery to Google SecOps



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
expire_time | additional.fields | Merged as label with key "expire_time" if not empty  
mobile | additional.fields | Merged as label with key "mobile" if not empty  
sn | additional.fields | Merged as label with key "sn" if not empty  
CONFIG_CONTEXT | additional.fields | Merged as label with key "CONFIG_CONTEXT" if not empty  
department | additional.fields | Merged as label with key "department" if not empty  
ctxData | additional.fields | Merged as label with key "ctxData" if not empty  
displayLanguage | additional.fields | Merged as label with key "displayLanguage" if not empty  
nrPwdTrialsForUserDeletion | additional.fields | Merged as label with key "nrPwdTrialsForUserDeletion" if not empty  
authInstant | additional.fields | Merged as label with key "authInstant" if not empty  
auditToken | additional.fields | Merged as label with key "auditToken" if not empty  
authPlugin | additional.fields | Merged as label with key "authPlugin" if not empty  
latestIdPropagation | additional.fields | Merged as label with key "latestIdPropagation" if not empty  
service | additional.fields | Merged as label with key "service" if not empty  
ldap_type | additional.fields | Merged as label with key "ldap_type" if not empty  
report_message | additional.fields | Merged as label with key "report_message" if not empty  
authenteeProvidedId | additional.fields | Merged as label with key "authenteeProvidedId" if not empty  
representerId | additional.fields | Merged as label with key "representerId" if not empty  
engine | additional.fields | Merged as label with key "engine" if not empty  
channel | additional.fields | Merged as label with key "channel" if not empty  
authnFactor | additional.fields | Merged as label with key "authnFactor" if not empty  
authnFactorDetail | additional.fields | Merged as label with key "authnFactorDetail" if not empty  
required_roles | additional.fields | Merged as label with key "required_roles" if not empty  
target_pattern | additional.fields | Merged as label with key "target_pattern" if not empty  
nameid | additional.fields | Merged as label with key "nameid" if not empty  
plugin_name | additional.fields | Merged as label with key "plugin_name" if not empty  
mechanism | additional.fields | Merged as label with key "mechanism" if not empty  
new_session_id | additional.fields | Merged as label with key "new_session_id" if not empty  
former_session_id | additional.fields | Merged as label with key "former_session_id" if not empty  
req_id | additional.fields | Merged as label with key "req_id" if not empty  
auth_method | additional.fields | Merged as label with key "auth_method" if not empty  
otp | additional.fields | Merged as label with key "otp" if not empty  
mob_num | additional.fields | Merged as label with key "mob_num" if not empty  
jsessionid | additional.fields | Merged as label with key "jsessionid" if not empty  
creationDate | additional.fields | Merged as label with key "creationDate" if not empty  
lastLogin | additional.fields | Merged as label with key "lastLogin" if not empty  
accountStatus | additional.fields | Merged as label with key "accountStatus" if not empty  
companyAdministrator | additional.fields | Merged as label with key "companyAdministrator" if not empty  
companyCustomer | additional.fields | Merged as label with key "companyCustomer" if not empty  
privateCustomer | additional.fields | Merged as label with key "privateCustomer" if not empty  
otpNotifyChannel | additional.fields | Merged as label with key "otpNotifyChannel" if not empty  
nas_identifier | additional.fields | Merged as label with key "nas_identifier" if not empty  
session_id | additional.fields | Merged as label with key "session_id" if not empty  
authPluginClassName | extensions.auth.auth_details | Value copied directly if present  
authenticator_type | extensions.auth.auth_details | Value copied directly if present and authPluginClassName is empty  
logon_type | extensions.auth.mechanism | Value copied directly  
N/A | intermediary | Merged from intermediary object  
FORWARD_LOCATION | intermediary.url | Value copied directly  
metadata_description | metadata.description | Value copied directly  
N/A | metadata.event_type | Set based on event context; determined by parser logic  
REQUEST_ID | metadata.product_log_id | Value copied directly  
airlock_version | metadata.product_version | Value copied directly  
method | network.http.method | Value copied directly  
user_agent | network.http.user_agent | Value copied directly  
packet_size | network.received_packets | Value converted to integer  
GSID | network.session_id | Value copied directly  
host | principal.hostname | Value copied directly  
CLIENT_IP | principal.ip | Value copied directly  
UID | principal.user.userid | Value copied directly  
role_name | role.name | Value copied directly  
authenteeType | role.type | Value copied directly  
N/A | security_result | Merged from security_result object  
action | security_result.action_details | Value copied directly if present  
authMethodShortDesc | security_result.action_details | Value merged if present  
action_detail | security_result.action_details | Value merged if present  
category_value | security_result.category | Value copied directly  
actionGroup | security_result.category_details | Value copied directly  
result_description | security_result.description | Value copied directly  
exception | security_result.summary | Value copied directly if present  
STATLOG | security_result.summary | Value copied directly if present and exception is empty  
mob_num | src.asset.type | Value copied directly  
mail | src.email | Value copied directly if present  
email | src.email | Value copied directly if present and mail is empty  
src_ip | src.ip | Value copied directly  
src_port | src.port | Value converted to integer  
role | src.user.attribute.roles | Value copied directly  
company | src.user.company_name | Value copied directly  
firstName | src.user.first_name | Value copied directly  
lastName | src.user.last_name | Value copied directly  
status | src.user.user_authentication_status | Value copied directly  
displayName | src.user.user_display_name | Value copied directly if present  
username | src.user.user_display_name | Value copied directly if present and displayName is empty  
src_user | src.user.user_display_name | Value copied directly if present and displayName/username are empty  
authenteeId | src.user.userid | Value copied directly if present  
src_userid | src.user.userid | Value copied directly if present and authenteeId is empty  
UID | src.user.userid | Value copied directly if present and authenteeId/src_userid are empty  
file_path | target.file.full_path | Value copied directly  
target_hostname | target.hostname | Value copied directly  
target_port | target.port | Value converted to integer  
task_name | target.resource.name | Value copied directly  
target_url | target.url | Value copied directly  
N/A | metadata.product_name | Set to "Ergon Informatik Airlock IAM"  
N/A | metadata.vendor_name | Set to "Ergon Informatik"  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ergon-informatik-airlock-iam-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
