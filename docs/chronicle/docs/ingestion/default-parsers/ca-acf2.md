---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-acf2/
title: Collect CA ACF2 logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:09.680255+00:00
---

# Collect CA ACF2 logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ca-acf2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect CA ACF2 logs

**Parser Version:** 2.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest CA ACF2 logs to Google Security Operations using Bindplane agent.

Broadcom ACF2 (Access Control Facility 2) for z/OS is a mainframe security product that provides access control, authentication, and auditing for IBM z/OS systems. ACF2 logs security events to IBM System Management Facility (SMF) records (default type 230), including authentication attempts, data set access violations, resource access events, TSO command logging, and database modifications. These SMF records must be forwarded to Chronicle using a third-party agent such as BMC AMI Defender for z/OS.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the BMC AMI Defender for z/OS agent
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * BMC AMI Defender for z/OS installed and running on the z/OS LPAR where ACF2 is active
  * Access to modify the BMC AMI Defender parameter files in the `amihlq.CZAGENT.PARM` data set
  * Authority to start or modify the CZAGENT started task on z/OS



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
           chronicle/acf2_logs:
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
             customer_id: 'YOUR_CUSTOMER_ID'
             endpoint: chronicle.googleapis.com
             log_type: CA_ACF2
             raw_log_field: body
             ingestion_labels:
               env: production
               source: acf2
         
         service:
           pipelines:
             logs/acf2_to_chronicle:
               receivers:
                 - udplog
               exporters:
                 - chronicle/acf2_logs
         

  2. Replace the following placeholders:

     * Receiver configuration:

       * `listen_address`: Set to `0.0.0.0:514` to listen on all interfaces on UDP port 514

         * For Linux systems running as non-root, use port `1514` or higher
         * Match this port with the BMC AMI Defender SERVER statement configuration
     * Exporter configuration:

       * `creds_file_path`: Full path to the service account JSON key file (Option 1):

         * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
         * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
       * `customer_id`: Replace `YOUR_CUSTOMER_ID` with your `customer ID`. For details, see Get Google SecOps customer ID.

       * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.

       * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.

       * `endpoint`: Keep set to `chronicle.googleapis.com`.

       * `log_type`: Set to `CA_ACF2` (Chronicle ingestion label for ACF2 logs)

       * `ingestion_labels`: Optional labels to categorize logs (customize as needed)




### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/acf2_logs:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'YOUR_CUSTOMER_ID'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: CA_ACF2
            raw_log_field: body
            ingestion_labels:
              env: production
              source: acf2
        


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
           




## Configure BMC AMI Defender for z/OS to forward ACF2 SMF records

### Edit the $$$SERVR parameter member

  1. Sign in to the z/OS system using TSO/ISPF or a 3270 emulator.
  2. Navigate to the BMC AMI Defender parameter library: 
     1. Enter `ISPF` at the TSO READY prompt.
     2. Select option **2** (Edit).
     3. In the **ISPF Library** field, enter the data set name: `amihlq.CZAGENT.PARM` (replace `amihlq` with your installation high-level qualifier).
     4. Press **Enter**.
  3. Edit the **$$$SERVR** member: 
     1. Type `E` next to the **$$$SERVR** member.
     2. Press **Enter**.
  4. Locate the SERVER statement section (approximately line 40-60).
  5. Uncomment one of the SERVER statements by removing the leading semicolon (`;`).
  6. Configure the SERVER statement with the Bindplane agent IP address and port:
         
         SERVER bindplane-host-ip:514 TRANS(UDP) MAXMSG(2000)
         

     * Replace `bindplane-host-ip` with the IP address of the Bindplane agent host (for example, `192.168.1.100`).
     * If using a non-standard port (for example, `1514`), specify: `bindplane-host-ip:1514`.
     * `TRANS(UDP)` specifies UDP transport protocol (recommended for syslog).
     * `MAXMSG(2000)` sets the maximum message length to 2000 bytes (ACF2 records may require larger sizes).
  7. Verify the OPTIONS statement for syslog format:

     1. Scroll up to locate the OPTIONS statements (approximately line 10-30).
     2. Ensure one of the following OPTIONS statements is uncommented based on your preferred format:
            
            OPTIONS IF(RFC 3164) SIEM(RFC 3164) TIMESTAMP INSTNAME(SIEM.Agent)
            

        * **RFC 3164** : Standard syslog format (recommended for Chronicle)
        * **CEF** : Common Event Format (alternative)
        * **LEEF** : Log Event Extended Format (alternative)
        * **JSON** : JSON format (alternative)
  8. Save the changes:

     1. Press **F3** to exit the editor.
     2. Type `SAVE` when prompted.
     3. Press **Enter**.



### Edit the $$$CONFG parameter member to enable ACF2 SMF record collection

  1. In the `amihlq.CZAGENT.PARM` data set member list, edit the **$$$CONFG** member:

     1. Type `E` next to the **$$$CONFG** member.
     2. Press **Enter**.
  2. Locate the ACF2 SMF record selection switch (search for `ACF2` or `SMF 230`).

  3. Uncomment the SELECT statement for ACF2:
         
         SELECT IF(ACF2) SMF(ACF2)
         

     * This enables collection of ACF2 SMF records (default type 230).
     * If your site uses a different SMF record type for ACF2, verify the type with the command: `ACF SHOW SYSTEMS` in TSO.
  4. Save the changes:

     1. Press **F3** to exit the editor.
     2. Type `SAVE` when prompted.
     3. Press **Enter**.



### Create or edit the SMF ACF2 statement parameter member

  1. In the `amihlq.CZAGENT.PARM` data set member list, check if a member named **$$$ACF2** or **SMFACF2** exists.
  2. If the member does not exist, create it:

     1. Type `C` (Create) on the command line.
     2. Enter the member name: `$$$ACF2`.
     3. Press **Enter**.
  3. Edit the member and add the following SMF ACF2 statement:
         
         SMF ACF2(230) FACILITY(SECURITY4) SEVERITY(INFORMATIONAL)
         

     * `ACF2(230)`: Specifies the SMF record type for ACF2 (default is 230; verify with `ACF SHOW SYSTEMS`).
     * `FACILITY(SECURITY4)`: Sets the syslog facility to Security (4).
     * `SEVERITY(INFORMATIONAL)`: Sets the default severity to Informational.

       * Invalid password or authority violations are automatically sent with severity ERROR.
       * Resource violations are automatically sent with severity ERROR.
  4. Optionally, configure specific ACF2 subtypes and severities:
         
         SMF ACF2(230) +
           FACILITY(SECURITY4) +
           SEVERITY(INFORMATIONAL) +
           SUBTYPES(P SEV(ERROR)) +
           SUBTYPES(V SEV(ERROR)) +
           SUBTYPES(D SEV(ERROR))
         

     * Subtype **P** : Invalid password or authority events (ERROR severity)
     * Subtype **V** : Resource violations (ERROR severity)
     * Subtype **D** : Data set access violations (ERROR severity)
  5. Save the changes:

     1. Press **F3** to exit the editor.
     2. Type `SAVE` when prompted.
     3. Press **Enter**.



### Refresh the BMC AMI Defender parameter file

  1. Exit ISPF and return to the TSO READY prompt.
  2. Issue the MODIFY command to reload the parameter file:
         
         F CZAGENT,PARMS
         

     * Replace `CZAGENT` with your BMC AMI Defender started task name if different.
     * This command reloads the parameter file without stopping the agent.
  3. Verify the configuration by checking the CZAPRINT output:

     1. In ISPF, select option **3.4** (DSLIST).
     2. Enter the data set name pattern: `CZAGENT.CZAPRINT` (or your site-specific naming convention).
     3. Press **Enter**.
     4. Type `B` (Browse) next to the most recent CZAPRINT data set.
     5. Press **Enter**.
     6. Search for messages indicating successful connection to the syslog server:

        * `CZA0070I Connected to server bindplane-host-ip:514`
        * `CZA0100I SMF ACF2 statement processed`
  4. If the CZAGENT started task is not running, start it:
         
         S CZAGENT
         




### Verify ACF2 log forwarding

  1. Generate test ACF2 security events:

     1. In TSO, attempt to access a data set you do not have permission to access.
     2. Attempt to log on with an invalid password (use a test account).
     3. Execute a TSO command that is logged by ACF2.
  2. Check the Bindplane agent logs to verify receipt of ACF2 syslog messages:

     * Linux:
           
           sudo journalctl -u observiq-otel-collector -f | grep ACF2
           

     * Windows:
           
           type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log" | findstr ACF2
           

  3. Sign in to the Google SecOps console and verify that ACF2 logs are being ingested:

     1. Go to **Search > UDM Search**.
     2. Enter the following query:
            
            metadata.log_type = "CA_ACF2"
            

     3. Verify that ACF2 security events appear in the search results.




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
| extensions.auth.mechanism | The authentication mechanism used.  
| extensions.auth.type | The type of authentication.  
sum | metadata.description | A description of the event.  
| metadata.event_type | The type of event.  
event_type, cat | metadata.product_event_type | The product-specific event type.  
product_version | metadata.product_version | The version of the product.  
terminal | principal.hostname | The hostname associated with the principal.  
name | principal.user.user_display_name | The display name of the user.  
usrName | principal.user.userid | The user ID.  
| security_result.action | The action taken by the security system.  
| security_result.category | The category of the security result.  
class | security_result.category_details | Additional details about the security result category.  
reason | security_result.severity | The severity level of the security result.  
reason | security_result.severity_details | Detailed severity information.  
logstr | security_result.summary | A summary of the security result.  
job_id | target.application | The application being targeted.  
job_group | target.group.group_display_name | The display name of the group.  
| target.namespace | The namespace of the target.  
dsn | target.resource.name | The name of the resource.  
vol | target.resource.parent | The parent resource.  
res, dsn | target.resource.product_object_id | The product-specific object identifier.  
| target.resource.resource_type | The type of resource.  
name | target.user.user_display_name | The display name of the target user.  
usrName | target.user.userid | The user ID of the target user.  
product_name | metadata.product_name | The name of the product generating the event.  
vendor_name | metadata.vendor_name | The name of the vendor.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-acf2-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
