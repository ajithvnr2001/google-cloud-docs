---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd/
title: Collect Linux Audit Daemon logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:19.947646+00:00
---

# Collect Linux Audit Daemon logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Linux Audit Daemon logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Linux Audit Daemon (auditd) logs to Google Security Operations using Bindplane.

The Linux Audit Daemon is the userspace component of the Linux auditing system. It records security-relevant events on the system, including file access, system calls, authentication events, and SELinux denials. Auditd logs are essential for compliance monitoring, intrusion detection, and forensic analysis on Linux hosts.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * If running behind a proxy, ensure firewall ports are open per the [Bindplane agent requirements](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration).
  * Root or sudo access on the Linux host running auditd.
  * The `auditd` package installed and running on the source Linux host.
  * The `audispd-plugins` package installed on the source Linux host (provides the `audisp-syslog` plugin).



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



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

  1. Access the configuration file:

     * **Linux** : `/opt/observiq-otel-collector/config.yaml`
     * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\config.yaml`
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
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
             customer_id: '<your_customer_id>'
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'AUDITD'
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
  * Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value.
  * Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
  * Replace `<your_customer_id>` with the actual Customer ID.
  * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in the **Get Google SecOps credentials for the Bindplane agent** section.



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: '<your_customer_id>'
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'AUDITD'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

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
         




## Configure auditd to forward logs via syslog

The `audisp syslog` plugin forwards audit events to syslog, which then sends them to the Bindplane agent. This is the recommended method for forwarding auditd logs.

**Note:** On RHEL/CentOS 8+ and modern distributions using audit 3.x, the audisp plugins directory is `/etc/audit/plugins.d/`. On older distributions (RHEL/CentOS 7 and earlier), the directory is `/etc/audisp/plugins.d/`. The steps below use the modern path. Adjust the path if you are running an older distribution.

### Install the audisp syslog plugin

  1. Sign in to the Linux host running auditd with root or sudo privileges.
  2. Install the `audispd-plugins` package:

     * **RHEL/CentOS/Fedora** :
    
    sudo yum install audispd-plugins
    

     * **Debian/Ubuntu** :
    
    sudo apt install audispd-plugins
    




### Configure the syslog plugin

  1. Edit the syslog plugin configuration file:
         
         sudo nano /etc/audit/plugins.d/syslog.conf
         

**Note:** On RHEL/CentOS 7 and earlier, the file is located at `/etc/audisp/plugins.d/syslog.conf`.
  2. Set the following values in the file:
         
         active = yes
         direction = out
         path = /sbin/audisp-syslog
         type = always
         args = LOG_LOCAL6
         format = string
         

     * **active** : Set to `yes` to enable the plugin.
     * **path** : The path to the `audisp-syslog` binary.
     * **type** : Set to `always` to run the plugin as an external program.
     * **args** : The syslog facility to use. `LOG_LOCAL6` is recommended to separate audit logs from other syslog messages.
     * **format** : Set to `string` to pass events in a text format suitable for syslog.



### Configure audit rules (optional)

  1. Edit the audit rules file to define which events to capture:
         
         sudo nano /etc/audit/rules.d/audit.rules
         

  2. Add rules based on your monitoring requirements. For example:
         
         ## Delete all existing rules
         -D
         
         ## Set buffer size (increase for high-volume systems)
         -b 8192
         
         ## Set failure mode (1 = printk, 2 = panic)
         -f 1
         
         ## Monitor authentication-related files
         -w /etc/passwd -p wa -k identity
         -w /etc/group -p wa -k identity
         -w /etc/shadow -p wa -k identity
         -w /etc/sudoers -p wa -k sudoers
         
         ## Monitor login events
         -w /var/log/faillog -p wa -k logins
         -w /var/log/lastlog -p wa -k logins
         
         ## Monitor process execution
         -a always,exit -F arch=b64 -S execve -k exec
         
         ## Monitor network configuration changes
         -a always,exit -F arch=b64 -S sethostname -S setdomainname -k network
         
         ## Make the configuration immutable (must be the last rule)
         -e 2
         

**Note:** The `-e 2` rule makes the audit configuration immutable. After setting this rule, a system reboot is required to change the configuration.
  3. Load the new audit rules:
         
         sudo augenrules --load
         




### Restart auditd

  1. Restart the auditd service to apply the plugin and rules changes:
         
         sudo service auditd restart
         

**Note:** On systems using audit 3.x, you can also use `sudo systemctl restart auditd`. On older systems, use `sudo service auditd restart` because auditd manages its own service lifecycle independently from systemd.



### Configure rsyslog to forward audit logs to Bindplane

  1. Create a new rsyslog configuration file for audit log forwarding:
         
         sudo nano /etc/rsyslog.d/audit-forward.conf
         

  2. Add the following line to forward logs via UDP to the Bindplane agent:
         
         local6.* @<BINDPLANE_IP>:514
         

**Note:** Use `@@` instead of `@` for TCP forwarding. Replace `<BINDPLANE_IP>` with the IP address of your Bindplane agent host.
  3. Restart rsyslog to apply the changes:
         
         sudo systemctl restart rsyslog
         




### Verify log forwarding

  1. On the source Linux host, generate a test audit event:
         
         sudo auditctl -w /tmp/test_audit -p wa -k test_chronicle
         

  2. Trigger the watch by touching the file:
         
         touch /tmp/test_audit
         

  3. On the Bindplane agent host, verify that logs are being received:
         
         sudo journalctl -u observiq-otel-collector -f
         




## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`acct` | `target.user.userid` | Value taken from `acct` field.  
`addr` | `principal.ip` | Value taken from `addr` field if it is a valid IP address.  
`arch` | `additional.fields` | Added as a key-value pair with key "arch".  
`auid` | `principal.user.userid` | Value taken from `auid` field. Used as the audit user ID.  
`comm` | `target.process.command_line` | Value taken from `comm` field.  
`cwd` | `additional.fields` | Added as a key-value pair with key "cwd".  
`exe` | `target.process.file.full_path` | Value taken from `exe` field.  
`exit` | `additional.fields` | Added as a key-value pair with key "exit".  
`gid` | `principal.user.group_identifiers` | Value taken from `gid` field.  
`hostname` | `principal.hostname` | Value taken from `hostname` field.  
`key` | `security_result.detection_fields` | Added as a key-value pair with key "audit_key".  
`msg` | `metadata.description` | Parsed from the `msg` field. Contains the audit event message.  
`name` | `target.file.full_path` | Value taken from `name` field when applicable.  
`node` | `principal.hostname` | Value taken from `node` field if `hostname` is not present.  
`op` | `metadata.product_event_type` | Value taken from `op` field (operation type).  
`pid` | `principal.process.pid` | Value taken from `pid` field.  
`ppid` | `principal.process.parent_process.pid` | Value taken from `ppid` field.  
`res` | `security_result.action` | Set to "ALLOW" if `res` is "success" or "1". Set to "BLOCK" if `res` is "failed" or "0".  
`ses` | `network.session_id` | Value taken from `ses` field (session ID).  
`subj` | `principal.process.file.full_path` | Value taken from `subj` field (SELinux subject context).  
`syscall` | `additional.fields` | Added as a key-value pair with key "syscall".  
`terminal` | `additional.fields` | Added as a key-value pair with key "terminal".  
`type` | `metadata.product_event_type` | Value taken from `type` field (audit record type, e.g., SYSCALL, USER_LOGIN, EXECVE).  
`uid` | `principal.user.userid` | Value taken from `uid` field.  
| `metadata.event_type` | Derived from audit record type. Set to "USER_LOGIN" for login events, "USER_LOGOUT" for logout events, "PROCESS_LAUNCH" for exec events, "FILE_MODIFICATION" for file events. Defaults to "GENERIC_EVENT".  
| `metadata.product_name` | Set to "auditd".  
| `metadata.vendor_name` | Set to "Linux".  
`home` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`shell` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`name` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`name` | `event.idm.read_only_udm.target.group.group_display_name` | Mapped from changelog  
`UID` | `event.idm.read_only_udm.target.user.product_object_id` | Mapped from changelog  
`GID` | `event.idm.read_only_udm.target.user.group_identifiers` | Mapped from changelog  
`GID` | `event.idm.read_only_udm.target.group.product_object_id` | Mapped from changelog  
`key_type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`hash` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`key_fingerprint` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`user` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`error_detail1` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`service_name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`ssh_disconnect_code` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`labels.bp_csoc` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`labels.bp_env_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`labels.log.file.name` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`resource.labels.node_id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`intermediary_host` | `event.idm.read_only_udm.intermediary.hostname` | Mapped from changelog  
`PWD` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`log_details` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`indicator.SUID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.UID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.AUID` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`type_crypto_props.msg` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`usr` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`pi` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`cmnd` | `event.idm.read_only_udm.target.process.command_line` | Mapped from changelog  
`proctitle_value` | `event.idm.read_only_udm.principal.process.file.full_path` | Mapped from changelog  
`filename` | `event.idm.read_only_udm.principal.process.file.names` | Mapped from changelog  
`filepath` | `event.idm.read_only_udm.target.file.full_path` | Mapped from changelog  
`uid` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`acct` | `event.idm.read_only_udm.principal.user.user_display_name` | Mapped from changelog  
`exe` | `event.idm.read_only_udm.target.process.file.full_path` | Mapped from changelog  
`pid` | `event.idm.read_only_udm.principal.process.pid` | Mapped from changelog  
`auid` | `event.idm.read_only_udm.about.user.userid` | Mapped from changelog  
`ses` | `event.idm.read_only_udm.network.session_id` | Mapped from changelog  
`addr` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`subj` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`res` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`op` | `event.idm.read_only_udm.security_result.summary` | Mapped from changelog  
`msg_value` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`grantors_value` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.msg` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.grantors` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`terminal` | `event.idm.read_only_udm.principal.application` | Mapped from changelog  
`sec_result` | `event.idm.read_only_udm.security_result` | Mapped from changelog  
`hostname` | `event.idm.read_only_udm.principal.hostname` | Mapped from changelog  
`indicator.mode` | `event.idm.read_only_udm.src.user.attribute.permissions` | Mapped from changelog  
`indicator.nametype` | `event.idm.read_only_udm.security_result.rule_name` | Mapped from changelog  
`indicator.cap_frootid` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.cap_fver` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.cap_fi` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.cap_fp` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`indicator.cap_fe` | `event.idm.read_only_udm.security_result.detection_fields` | Mapped from changelog  
`OUID` | `event.idm.read_only_udm.principal.user.userid` | Mapped from changelog  
`OGID` | `event.idm.read_only_udm.principal.group.group_display_name` | Mapped from changelog  
`action_data` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`target_email` | `event.idm.ready_only_udm.target.user.email_addresses` | Mapped from changelog  
`target_port` | `event.idm.ready_only_udm.target.port` | Mapped from changelog  
`status` | `event.idm.ready_only_udm.security_result.action_details` | Mapped from changelog  
`to_email` | `event.idm.ready_only_udm.network.email.to` | Mapped from changelog  
`target_hostname` | `event.idm.ready_only_udm.target.hostname` | Mapped from changelog  
`"relay_data"` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`"delays_data"` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`"delay_data"` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`and "dns_data"` | `event.idm.ready_only_udm.additional.fields` | Mapped from changelog  
`bytes_sent` | `event.idm.ready_only_udm.network.sent_bytes` | Mapped from changelog  
`bytes_received` | `event.idm.ready_only_udm.network.received_bytes` | Mapped from changelog  
`response_code` | `event.idm.ready_only_udm.network.http.response_code` | Mapped from changelog  
`principal_user_name` | `principal.user.userid` | Mapped from changelog  
`remote` | `principal.ip` | Mapped from changelog  
`method` | `network.http.method` | Mapped from changelog  
`path` | `principal.file.full_path` | Mapped from changelog  
`code` | `additional.fields` | Mapped from changelog  
`size` | `principal.file.size` | Mapped from changelog  
`agent` | `network.http.user_agent` | Mapped from changelog  
`az` | `principal.location.name` | Mapped from changelog  
`ec2_instance_id` | `principal.asset.product_object_id` | Mapped from changelog  
`private_ip` | `principal.ip` | Mapped from changelog  
`ProviderName` | `additional.fields` | Mapped from changelog  
`Version` | `additional.fields` | Mapped from changelog  
`Task` | `additional.fields` | Mapped from changelog  
`EventRecordID` | `additional.fields` | Mapped from changelog  
`ThreadID` | `additional.fields` | Mapped from changelog  
`messageType` | `target.resource.attribute.labels` | Mapped from changelog  
`owner` | `principal.user.userid` | Mapped from changelog  
`logevent.id` | `metadata.product_log_id` | Mapped from changelog  
`logGroup` | `secu_result.about.resource.name` | Mapped from changelog  
`logStream` | `secu_result.about.resource.attribute.labels` | Mapped from changelog  
`ip_addr` | `principal.ip` | Mapped from changelog  
`gd` | `secu_result.description` | Mapped from changelog  
`process` | `target.application` | Mapped from changelog  
`pid` | `target.process.pid` | Mapped from changelog  
`status_code` | `network.http.response_code` | Mapped from changelog  
`url` | `network.http.referral_url` | Mapped from changelog  
`useragent` | `network.http.user_agent` | Mapped from changelog  
`request` | `additional.fields` | Mapped from changelog  
`tls_version` | `network.tls.version` | Mapped from changelog  
`hostname_is` | `principal.hostname` | Mapped from changelog  
`referrer` | `network.http.referral_url` | Mapped from changelog  
`metadata.event_type` | `USER_LOGIN` | Mapped from changelog  
`metadata.event_type` | `PROCESS_UNCATEGORIZED` | Mapped from changelog  
`srcIP` | `principal.ip` | Mapped from changelog  
`username` | `principal.user.user_display_name` | Mapped from changelog  
`type_syscall_props.msg` | `additional.fields` | Mapped from changelog  
`sw", "sw_type", and "subj` | `security_result.detection_fields` | Mapped from changelog  
`indicator.SYSCALL` | `security_result.detection_fields` | Mapped from changelog  
`exe` | `principal.process.file.full_path` | Mapped from changelog  
`target.user.userid` | `principal.user.userid` | Mapped from changelog  
`target_user_name` | `target.user.userid` | Mapped from changelog  
`field` | `field33` | Mapped from changelog  
`fp` | `network.tls.client.certificate.sha256` | Mapped from changelog  
`pid` | `principal.process.pid` | Mapped from changelog  
`syslog-tag` | `security_result.detection_fields` | Mapped from changelog  
`inter_ip` | `intermediary.ip` | Mapped from changelog  
`inter_hostname` | `intermediary.hostname` | Mapped from changelog  
`grp` | `target.group.group_display_name` | Mapped from changelog  
`id` | `about.user.userid` | Mapped from changelog  
`acct` | `target.user.user_display_name` | Mapped from changelog  
`uid` | `principal.user.userid` | Mapped from changelog  
`auid` | `about.user.userid` | Mapped from changelog  
`auid` | `target.user.userid` | Mapped from changelog  
`op" and "id` | `security_result.summary` | Mapped from changelog  
`op" and "acct` | `security_result.summary` | Mapped from changelog  
`labels.compute.googleapis.com/resource_name","jsonPayload._HOSTNAME" , "CollectorHostName", "HOSTNAME", and "Computer` | `principal.hostname` | Mapped from changelog  
`HostIP` | `principal.ip` | Mapped from changelog  
`ProcessID" and "jsonPayload._PID` | `principal.process.pid` | Mapped from changelog  
`SyslogMessage` | `metadata.description` | Mapped from changelog  
`TenantId", "_ItemId", "_Internal_WorkspaceResourceId", "_ResourceId", and "Facility` | `additional.fields` | Mapped from changelog  
`SeverityLevel` | `security_result.severity` | Mapped from changelog  
`SourceSystem` | `principal.platform` | Mapped from changelog  
`jsonPayload._COMM` | `principal.application` | Mapped from changelog  
`jsonPayload._EXE` | `target.process.file.full_path` | Mapped from changelog  
`jsonPayload._AUDIT_FIELD_FILE` | `target.file.full_path` | Mapped from changelog  
`jsonPayload._AUDIT_FIELD_HASH` | `target.file.hash` | Mapped from changelog  
`jsonPayload._AUDIT_SESSION` | `network.session_id` | Mapped from changelog  
`jsonPayload._PPID` | `principal.process.parent_process.pid` | Mapped from changelog  
`jsonPayload._AUDIT_FIELD_A0", "jsonPayload._AUDIT_FIELD_A1", "jsonPayload._AUDIT_FIELD_A2", "jsonPayload._AUDIT_FIELD_A3", "jsonPayload._BOOT_ID", and "jsonPayload._AUDIT_FIELD_EXIT` | `security_result.detection_fields` | Mapped from changelog  
`id` | `target.user.userid` | Mapped from changelog  
`ID` | `target.user.user_display_name` | Mapped from changelog  
`user_name` | `principal.user.userid` | Mapped from changelog  
`principal_user_userid` | `principal.user.userid` | Mapped from changelog  
`vendor_name` | `Linux` | Mapped from changelog  
`product_name` | `AuditD` | Mapped from changelog  
`ip` | `target.ip` | Mapped from changelog  
`success` | `security_result.summary` | Mapped from changelog  
`syscall", "exit", "tty", "a0", "a1", "a2", "a3` | `security_result.about.labels` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/auditd-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
