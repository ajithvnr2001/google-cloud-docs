---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-beyondinsight/
title: Collect BeyondTrust BeyondInsight logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:07.037947+00:00
---

# Collect BeyondTrust BeyondInsight logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/beyondtrust-beyondinsight/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect BeyondTrust BeyondInsight logs

**Parser Version:** 7.0

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest BeyondTrust BeyondInsight logs to Google Security Operations using the Bindplane agent.

BeyondTrust BeyondInsight is a privileged access management platform that generates syslog messages for security events, authentication, and administrative activity. The parser normalizes fields and maps them to the Unified Data Model (UDM).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Windows Server 2016 or later, or Linux host with `systemd`
  * Network connectivity between the Bindplane agent and the BeyondTrust BeyondInsight instance
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
  * Privileged access to an instance of BeyondTrust BeyondInsight



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
          chronicle/beyondtrust_beyondinsight:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: chronicle.googleapis.com
            log_type: BEYONDTRUST_BEYONDINSIGHT
            raw_log_field: body
        
        service:
          pipelines:
            logs/beyondtrust_beyondinsight_to_chronicle:
              receivers:
                - udplog
              exporters:
                - chronicle/beyondtrust_beyondinsight
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on: 
      * `0.0.0.0` to listen on all interfaces (recommended)
      * Port `514` is the standard syslog port (requires root on Linux; use `1514` for non-root)
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Customer ID copied from the Google SecOps console
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/beyondtrust_beyondinsight:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: '<customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: BEYONDTRUST_BEYONDINSIGHT
            raw_log_field: body
        


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
             




## Configure syslog event forwarding in BeyondTrust BeyondInsight

  1. Sign in to the **BeyondTrust** web UI.
  2. Go to **Appliance > Security > Appliance Administration**.
  3. Go to the **Syslog** section.
  4. Click **Add new server**.
  5. Provide the following configuration details: 
     * **Hostname** : Enter the Bindplane agent IP address.
     * **Format** : Select **RFC 5424**.
     * **Port** : Defaults to `UDP:514`.
  6. Click **Save**.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`AgentDesc_label` | `additional.fields` | Merged  
`AgentID_label` | `additional.fields` | Merged  
`AgentVer_label` | `additional.fields` | Merged  
`Approver_label` | `additional.fields` | Merged  
`AuditID_label` | `additional.fields` | Merged  
`Base_address_label` | `additional.fields` | Merged  
`Category_label` | `additional.fields` | Merged  
`CertIssuer_label` | `additional.fields` | Merged  
`CertSerial_label` | `additional.fields` | Merged  
`Entry_address_label` | `additional.fields` | Merged  
`EventDesc_label` | `additional.fields` | Merged  
`EventName_label` | `additional.fields` | Merged  
`EventSubject_label` | `additional.fields` | Merged  
`Failed_label` | `additional.fields` | Merged  
`Image_size_label` | `additional.fields` | Merged  
`LogID_label` | `additional.fields` | Merged  
`LogTime_label` | `additional.fields` | Merged  
`ObjectID_label` | `additional.fields` | Merged  
`ObjectTypeID_label` | `additional.fields` | Merged  
`ObjectType_label` | `additional.fields` | Merged  
`Operation_label` | `additional.fields` | Merged  
`Reason_label` | `additional.fields` | Merged  
`RefType_label` | `additional.fields` | Merged  
`ReleaseRequestId_label` | `additional.fields` | Merged  
`RoleUsed_label` | `additional.fields` | Merged  
`Server_date_label` | `additional.fields` | Merged  
`Signer_label` | `additional.fields` | Merged  
`Start_time_label` | `additional.fields` | Merged  
`TicketNumber_label` | `additional.fields` | Merged  
`TicketSystem_label` | `additional.fields` | Merged  
`Type_label` | `additional.fields` | Merged  
`Version_label` | `additional.fields` | Merged  
`WorkgroupDesc_label` | `additional.fields` | Merged  
`WorkgroupID_label` | `additional.fields` | Merged  
`WorkgroupLocation_label` | `additional.fields` | Merged  
`accountdisabled01003_label` | `additional.fields` | Merged  
`accountname_label` | `additional.fields` | Merged  
`accountnameformat_label` | `additional.fields` | Merged  
`action_type_label` | `additional.fields` | Merged  
`actiontype_label` | `additional.fields` | Merged  
`address_label` | `additional.fields` | Merged  
`agentdesc_label` | `additional.fields` | Merged  
`agentid_label` | `additional.fields` | Merged  
`agentver_label` | `additional.fields` | Merged  
`alias_label` | `additional.fields` | Merged  
`app_user_id_label` | `additional.fields` | Merged  
`approver_label` | `additional.fields` | Merged  
`appuserid_label` | `additional.fields` | Merged  
`auditid_label` | `additional.fields` | Merged  
`authenticationtype_label` | `additional.fields` | Merged  
`automanagementflag_label` | `additional.fields` | Merged  
`badpwcount01008_label` | `additional.fields` | Merged  
`badpwcount0101_label` | `additional.fields` | Merged  
`browserinfo_label` | `additional.fields` | Merged  
`bt_Category_label` | `additional.fields` | Merged  
`btcategory_label` | `additional.fields` | Merged  
`btuser_label` | `additional.fields` | Merged  
`can_manage_ownership_label` | `additional.fields` | Merged  
`can_share_secret_label` | `additional.fields` | Merged  
`category_label` | `additional.fields` | Merged  
`changeafterrelease_label` | `additional.fields` | Merged  
`changepasswordfrequency_label` | `additional.fields` | Merged  
`changepasswordtime_label` | `additional.fields` | Merged  
`changereasoncd_label` | `additional.fields` | Merged  
`checkpassword_label` | `additional.fields` | Merged  
`clarityactive_label` | `additional.fields` | Merged  
`code_label` | `additional.fields` | Merged  
`countrycode01011_label` | `additional.fields` | Merged  
`countrycode0101_label` | `additional.fields` | Merged  
`createdate_label` | `additional.fields` | Merged  
`details_label` | `additional.fields` | Merged  
`deviceExternalId_label` | `additional.fields` | Merged  
`dllversion_label` | `additional.fields` | Merged  
`dnsname_label` | `additional.fields` | Merged  
`dsskeyruleid_label` | `additional.fields` | Merged  
`dump_label` | `additional.fields` | Merged  
`elevationcommand_label` | `additional.fields` | Merged  
`endpointprivilegemanagementactive_label` | `additional.fields` | Merged  
`endpointprivilegemanagementformacactive_label` | `additional.fields` | Merged  
`endpointprivilegemanagementformacsettings_label` | `additional.fields` | Merged  
`endpointprivilegemanagementformacvulnerabilitiesactive_label` | `additional.fields` | Merged  
`endpointprivilegemanagementforunixlinuxactive_label` | `additional.fields` | Merged  
`endpointprivilegemanagementforunixlinuxsettings_label` | `additional.fields` | Merged  
`endpointprivilegemanagementsettings_label` | `additional.fields` | Merged  
`endpointprivilegemanagementvulnerabilitiesactive_label` | `additional.fields` | Merged  
`endpointprotectionplatformattackeventsactive_label` | `additional.fields` | Merged  
`endpointprotectionplatformmalwareeventsactive_label` | `additional.fields` | Merged  
`endpointprotectionplatformvulnerabilitiesactive_label` | `additional.fields` | Merged  
`eventType_label` | `additional.fields` | Merged  
`eventdesc_label` | `additional.fields` | Merged  
`eventseverity_label` | `additional.fields` | Merged  
`eventsubject_label` | `additional.fields` | Merged  
`eventtype_label` | `additional.fields` | Merged  
`evtdatatype_label` | `additional.fields` | Merged  
`evtsrcipbi_label` | `additional.fields` | Merged  
`evtstatus_label` | `additional.fields` | Merged  
`evtsubjbi_label` | `additional.fields` | Merged  
`expires01006_label` | `additional.fields` | Merged  
`expires0101_label` | `additional.fields` | Merged  
`facility_label` | `additional.fields` | Merged  
`failed_label` | `additional.fields` | Merged  
`fallback_label` | `additional.fields` | Merged  
`fallbackcode_label` | `additional.fields` | Merged  
`fileintegritymonitoringactive_label` | `additional.fields` | Merged  
`folder_id_label` | `additional.fields` | Merged  
`folder_label` | `additional.fields` | Merged  
`formatVersion_label` | `additional.fields` | Merged  
`fullname0101_label` | `additional.fields` | Merged  
`functionalaccountid_label` | `additional.fields` | Merged  
`groupid_label` | `additional.fields` | Merged  
`isactive_label` | `additional.fields` | Merged  
`isareleaseduration_label` | `additional.fields` | Merged  
`isautomanagementenabled_label` | `additional.fields` | Merged  
`isdynamicsystem_label` | `additional.fields` | Merged  
`lastlogoff01005_label` | `additional.fields` | Merged  
`lastlogoff0101_label` | `additional.fields` | Merged  
`lastlogon01004_label` | `additional.fields` | Merged  
`lastlogon0101_label` | `additional.fields` | Merged  
`linked_label` | `additional.fields` | Merged  
`linkedaccount_label` | `additional.fields` | Merged  
`log_type_status_label` | `additional.fields` | Merged  
`logid_label` | `additional.fields` | Merged  
`logonserver0101_label` | `additional.fields` | Merged  
`managedaccountid_label` | `additional.fields` | Merged  
`managedentitytype_label` | `additional.fields` | Merged  
`managedsystemid_label` | `additional.fields` | Merged  
`managedsystemname_label` | `additional.fields` | Merged  
`maxreleaseduration_label` | `additional.fields` | Merged  
`maxstorage01007_label` | `additional.fields` | Merged  
`maxstorage0101_label` | `additional.fields` | Merged  
`memberofgroup01001_label` | `additional.fields` | Merged  
`memberofgroup0101_label` | `additional.fields` | Merged  
`netbiosname_label` | `additional.fields` | Merged  
`notes_label` | `additional.fields` | Merged  
`numberoflogons01009_label` | `additional.fields` | Merged  
`numberoflogons0101_label` | `additional.fields` | Merged  
`nvps_active_label` | `additional.fields` | Merged  
`nvps_areaname_label` | `additional.fields` | Merged  
`nvps_beyondinsightapplicationauditenabled_label` | `additional.fields` | Merged  
`nvps_context_label` | `additional.fields` | Merged  
`nvps_genericappliancehealthseverity_label` | `additional.fields` | Merged  
`nvps_hostname_label` | `additional.fields` | Merged  
`nvps_name_label` | `additional.fields` | Merged  
`nvps_outputpipeline_label` | `additional.fields` | Merged  
`nvps_port_label` | `additional.fields` | Merged  
`objectid_label` | `additional.fields` | Merged  
`objecttype_label` | `additional.fields` | Merged  
`objecttypeid_label` | `additional.fields` | Merged  
`operation_label` | `additional.fields` | Merged  
`os_label` | `additional.fields` | Merged  
`ownerid_label` | `additional.fields` | Merged  
`password_label` | `additional.fields` | Merged  
`passwordage0101_label` | `additional.fields` | Merged  
`passwordexpired01013_label` | `additional.fields` | Merged  
`passwordexpired0101_label` | `additional.fields` | Merged  
`passwordruleid_label` | `additional.fields` | Merged  
`platformid_label` | `additional.fields` | Merged  
`platformname_label` | `additional.fields` | Merged  
`priority_label` | `additional.fields` | Merged  
`privilege01002_label` | `additional.fields` | Merged  
`privilege0101_label` | `additional.fields` | Merged  
`referenceid_label` | `additional.fields` | Merged  
`releaseduration_label` | `additional.fields` | Merged  
`releaseid_label` | `additional.fields` | Merged  
`resetonmimatch_label` | `additional.fields` | Merged  
`result_label` | `additional.fields` | Merged  
`rid01012_label` | `additional.fields` | Merged  
`rid0101_label` | `additional.fields` | Merged  
`roleadded_label` | `additional.fields` | Merged  
`roleused_label` | `additional.fields` | Merged  
`samaccountname_label` | `additional.fields` | Merged  
`secret_type_label` | `additional.fields` | Merged  
`smartruletitle_label` | `additional.fields` | Merged  
`source01014_label` | `additional.fields` | Merged  
`source0101_label` | `additional.fields` | Merged  
`sshkeyenforcementmode_label` | `additional.fields` | Merged  
`subjectdescription_label` | `additional.fields` | Merged  
`ticketnumber_label` | `additional.fields` | Merged  
`timeout_label` | `additional.fields` | Merged  
`title_label` | `additional.fields` | Merged  
`transactiongroup_label` | `additional.fields` | Merged  
`userID_label` | `additional.fields` | Merged  
`userid_label` | `additional.fields` | Merged  
`version_label` | `additional.fields` | Merged  
`workgroupdesc_label` | `additional.fields` | Merged  
`workgroupid_label` | `additional.fields` | Merged  
`workgrouplocation_label` | `additional.fields` | Merged  
`agentid` | `extensions.auth.type` | Mapped: `generic_appliance_health` → `MACHINE`  
`category` | `extensions.auth.type` | Mapped: `Login` → `MACHINE`, `Logout` → `MACHINE`  
`eventdesc` | `extensions.auth.type` | Mapped: `successfully logged on` → `MACHINE`  
`nvps.clienthost` | `intermediary.asset.hostname` | Directly mapped  
`nvps.hostname` | `intermediary.asset.hostname` | Directly mapped  
`nvps.source` | `intermediary.asset.hostname` | Directly mapped  
`hostname` | `intermediary.asset.ip` | Merged  
`inter_ip` | `intermediary.asset.ip` | Merged  
`sourceip` | `intermediary.asset.ip` | Merged  
`inter` | `intermediary.hostname` | Directly mapped  
`nvps.clienthost` | `intermediary.hostname` | Directly mapped  
`nvps.hostname` | `intermediary.hostname` | Directly mapped  
`nvps.source` | `intermediary.hostname` | Directly mapped  
`hostname` | `intermediary.ip` | Merged  
`inter_ip` | `intermediary.ip` | Merged  
`sourceip` | `intermediary.ip` | Merged  
`Category` | `metadata.description` | Directly mapped  
`devTime` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`eventdate` | `metadata.event_timestamp` | Parsed as `yyyy-MM-dd HH:mm:ss`  
`rt` | `metadata.event_timestamp` | Parsed as `MMM dd yyyy HH:mm:ss`  
`time` | `metadata.event_timestamp` | Parsed as `MMM dd HH:mm:ss`  
`ts` | `metadata.event_timestamp` | Parsed as `yyyy-MM-ddTHH:mm:ss`  
`agentid` | `metadata.event_type` | Mapped: `generic_appliance_health` → `USER_LOGIN`, `generic_appliance_health` → `USER_LOGOUT`  
`category` | `metadata.event_type` | Mapped: `Login` → `USER_LOGIN`, `Logout` → `USER_LOGOUT`  
`eventdesc` | `metadata.event_type` | Mapped: `successfully logged on` → `USER_LOGIN`  
`has_principal` | `metadata.event_type` | Mapped: `true` → `NETWORK_CONNECTION`, `true` → `STATUS_UPDATE`  
`has_user` | `metadata.event_type` | Mapped: `true` → `USER_UNCATEGORIZED`  
`eventid` | `metadata.product_event_type` | Directly mapped  
`product_event` | `metadata.product_event_type` | Directly mapped  
`nvps.id` | `metadata.product_log_id` | Directly mapped  
`Product` | `metadata.product_name` | Directly mapped  
`appname` | `metadata.product_name` | Directly mapped  
`product` | `metadata.product_name` | Directly mapped  
`version` | `metadata.product_version` | Directly mapped  
`vendor` | `metadata.vendor_name` | Directly mapped  
`nvps.domainname` | `principal.administrative_domain` | Directly mapped  
`shost` | `principal.asset.hostname` | Directly mapped  
`sourcehost` | `principal.asset.hostname` | Directly mapped  
`src_host` | `principal.asset.hostname` | Directly mapped  
`ip` | `principal.asset.ip` | Merged  
`src` | `principal.asset.ip` | Merged  
`src_ip` | `principal.asset.ip` | Merged  
`nvps.workgroupname` | `principal.group.group_display_name` | Directly mapped  
`shost` | `principal.hostname` | Directly mapped  
`sourcehost` | `principal.hostname` | Directly mapped  
`src_host` | `principal.hostname` | Directly mapped  
`ip` | `principal.ip` | Merged  
`souirceip` | `principal.ip` | Merged  
`src` | `principal.ip` | Merged  
`src_ip` | `principal.ip` | Merged  
`OS` | `principal.platform` | Mapped: `Windows` → `WINDOWS`, `Linux` → `LINUX`  
`Os` | `principal.platform` | Mapped: `Windows` → `WINDOWS`, `Linux` → `LINUX`  
`OS` | `principal.platform_version` | Directly mapped  
`Os` | `principal.platform_version` | Directly mapped  
`Filename` | `principal.process.file.full_path` | Directly mapped  
`MD5` | `principal.process.file.md5` | Directly mapped  
`SHA1` | `principal.process.file.sha1` | Directly mapped  
`ParentProcessID` | `principal.process.parent_pid` | Directly mapped  
`ProcessID` | `principal.process.pid` | Directly mapped  
`resource` | `principal.resource.id` | Directly mapped  
`Company_name` | `principal.user.company_name` | Directly mapped  
`username` | `principal.user.email_addresses` | Mapped: `^.+@.+$` → `username`  
`UserID` | `principal.user.product_object_id` | Directly mapped  
`userId` | `principal.user.product_object_id` | Directly mapped  
`Name` | `principal.user.user_display_name` | Directly mapped  
`UserName` | `principal.user.user_display_name` | Directly mapped  
`usrName` | `principal.user.user_display_name` | Directly mapped  
`BeyondTrustBeyondInsightUser` | `principal.user.userid` | Directly mapped  
`src_user` | `principal.user.userid` | Directly mapped  
`user` | `principal.user.userid` | Directly mapped  
`nvps.sid0101` | `principal.user.windows_sid` | Directly mapped  
`sid01015` | `principal.user.windows_sid` | Directly mapped  
`Category` | `security_result.category_details` | Merged  
`Description` | `security_result.description` | Directly mapped  
`nvps.description` | `security_result.description` | Directly mapped  
`nvps.message` | `security_result.description` | Directly mapped  
`nvps.reason` | `security_result.description` | Directly mapped  
`changedt_label` | `security_result.detection_fields` | Merged  
`createdate_label` | `security_result.detection_fields` | Merged  
`eventdate_label` | `security_result.detection_fields` | Merged  
`evtdate_label` | `security_result.detection_fields` | Merged  
`lastupdatedate_label` | `security_result.detection_fields` | Merged  
`logtime_label` | `security_result.detection_fields` | Merged  
`nextchangedate_label` | `security_result.detection_fields` | Merged  
`removerole_label` | `security_result.detection_fields` | Merged  
`smartruleid_label` | `security_result.detection_fields` | Merged  
`systemname_label` | `security_result.detection_fields` | Merged  
`token_label` | `security_result.detection_fields` | Merged  
`BeyondTrustBeyondInsightEventSeverity` | `security_result.severity` | Mapped: `0` → `INFORMATIONAL`, `3` → `LOW`, `6` → `MEDIUM`, `9` → `HIGH`  
`eventseverity` | `security_result.severity` | Mapped: `0` → `INFORMATIONAL`, `3` → `LOW`, `6` → `MEDIUM`  
`severity` | `security_result.severity` | Mapped: `0` → `INFORMATIONAL`  
`eventname` | `security_result.summary` | Directly mapped  
`agentid` | `target.application` | Mapped: `AppAudit` → `BeyondInsight Application GUI`, `generic_appliance_health` → `BeyondIn...  
`ManagedSystem` | `target.asset.hostname` | Directly mapped  
`dst` | `target.asset.ip` | Merged  
`ips` | `target.asset.ip` | Merged  
`nvps.folderpath` | `target.file.full_path` | Directly mapped  
`nvps.filename` | `target.file.names` | Merged  
`nvps.filehash` | `target.file.sha256` | Directly mapped  
`ManagedSystem` | `target.hostname` | Directly mapped  
`dst_host` | `target.hostname` | Directly mapped  
`dst` | `target.ip` | Merged  
`ips` | `target.ip` | Merged  
`SecretId` | `target.resource.id` | Directly mapped  
`nvps.target` | `target.resource.name` | Directly mapped  
`nvps.title` | `target.resource.name` | Directly mapped  
`nvps.secretid` | `target.resource.product_object_id` | Directly mapped  
`nvps.secrettype` | `target.resource.resource_subtype` | Directly mapped  
`URL` | `target.url` | Directly mapped  
`nvps.email` | `target.user.email_addresses` | Merged  
`nvps.ownersdisplay` | `target.user.user_display_name` | Directly mapped  
`ManagedAccount` | `target.user.userid` | Directly mapped  
`dst_user` | `target.user.userid` | Directly mapped  
`nvps.owner` | `target.user.userid` | Directly mapped  
`nvps.username` | `target.user.userid` | Directly mapped  
N/A | `extensions.auth.type` | Constant: `MACHINE`  
N/A | `metadata.event_type` | Constant: `NETWORK_CONNECTION`  
N/A | `principal.platform` | Constant: `WINDOWS`  
N/A | `security_result.severity` | Constant: `INFORMATIONAL`  
N/A | `target.application` | Constant: `BeyondInsight Application GUI`  
`nvps.filehash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`filehash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`sourceip` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`nvps.xforwardedfor` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`nvps.userid` | `event.idm.read_only_udm.principal.user.product_object_id` | Mapped from changelog  
`eventid` | `event.idm.read_only_udm.metadata.product_event_type` | Mapped from changelog  
`nvps.email` | `event.idm.read_only_udm.target.user.email_addresses` | Mapped from changelog  
`nvps.ownersdisplay` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`nvps.filename` | `event.idm.read_only_udm.target.file.names` | Mapped from changelog  
`nvps.filehash` | `event.idm.read_only_udm.target.file.sha256` | Mapped from changelog  
`nvps.secretid` | `event.idm.read_only_udm.target.resource.product_object_id` | Mapped from changelog  
`nvps.secrettype` | `event.idm.read_only_udm.target.resource.resource_subtype` | Mapped from changelog  
`nvps.folderpath` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`nvps.notes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`notes` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`nvps.ticketnumber` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ticketnumber` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`nvps.approver` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`approver` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`nvps.ownerid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ownerid` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/beyondtrust-beyondinsight-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
