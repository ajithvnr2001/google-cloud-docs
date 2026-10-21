---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vandyke-vshell-sftp/
title: Collect VanDyke VShell SFTP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:30:36.874289+00:00
---

# Collect VanDyke VShell SFTP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vandyke-vshell-sftp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect VanDyke VShell SFTP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest VanDyke VShell SFTP logs to Google Security Operations using either Bindplane with Syslog or Amazon S3 with a log shipper.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the VanDyke VShell server or management console
  * For **Option 1** : A Windows 2016 or later or Linux host with `systemd` for the Bindplane agent
  * For **Option 2** : AWS account with S3 access and NXLog/Fluent Bit on the VShell server



## Get Google SecOps ingestion authentication file

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agents**.
  3. Download the **Ingestion Authentication File**.
  4. Save the file securely on the system where Bindplane will be installed or where you'll configure the feed.



## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Option 1: Integration via Bindplane and Syslog

This option provides real-time log streaming with minimal latency and is recommended for most deployments.

### Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

#### Windows installation

  1. Open the **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
         




#### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
         




### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

## Configure the BindPlane agent to ingest Syslog and send to Google SecOps

  1. Access the configuration file:

     * Locate the `config.yaml` file. Typically, it's in the `/opt/observiq-otel-collector/` directory on Linux or in the installation directory on Windows.
     * Open the file using a text editor (for example, `nano`, `vi`, or Notepad).
  2. Edit the `config.yaml` file as follows:
         
         receivers:
           udplog:
             # Replace the port and IP address as required
             listen_address: "0.0.0.0:514"
         
         exporters:
           chronicle/chronicle_w_labels:
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: YOUR_CUSTOMER_ID
             endpoint: malachiteingestion-pa.googleapis.com
             # Custom log type - requires parser extension
             log_type: 'VANDYKE_SFTP'
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
     * Replace `YOUR_CUSTOMER_ID` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the authentication file was saved.
     * For TCP instead of UDP, replace `udplog` with `tcplog`.



## Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in **Linux** , run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

  * To restart the Bindplane agent in **Windows** , you can either use the **Services** console or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




## Configure Syslog forwarding on VanDyke VShell

### For VShell on Windows

  1. Sign in to the **VShell Control Panel**.
  2. Go to **Logging** settings.
  3. Configure remote syslog logging: 
     * Enable logging to **remote syslog server**.
     * **Server address** : Enter the Bindplane IP address.
     * **Port** : Enter 514 (or your configured port).
     * **Protocol** : Select **UDP** (or TCP if configured).
     * **Message groups** : Select **Connection** , **Authentication** , **SFTP** , **FTPS** , **HTTPS** , **Errors** , **Warnings** , and **Informational**.
  4. Click **Apply** > **OK**.



### For VShell on Linux/macOS

  1. Edit the **vshelld_config** file (typically `/etc/vshell/vshelld_config`).
  2. Configure the following parameters:
         
         SyslogFacility LOG_LOCAL3
         LogLevel INFO
         

  3. Configure your system's **syslog** to forward LOG_LOCAL3 to the Bindplane agent:

     * Edit `/etc/rsyslog.conf` or `/etc/syslog-ng/syslog-ng.conf`.
     * Add: `local3.* @bindplane-agent-ip:514` (for UDP) or `local3.* @@bindplane-agent-ip:514` (for TCP).
  4. Restart the VShell service and syslog service:
         
         sudo systemctl restart vshelld
         sudo systemctl restart rsyslog
         




## Option 2: Integration via AWS S3

This option is useful for environments that require log archival or where direct syslog forwarding is not feasible. Note that this requires a log shipper on the VShell server since AWS Lambda cannot access on-premises files.

### Configure AWS S3 bucket and IAM for Google SecOps

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `vandyke-sftp-logs`).
  3. Create a **User** following this user guide: [Creating an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).
  4. Select the created **User**.
  5. Select **Security credentials** tab.
  6. Click **Create Access Key** in section **Access Keys**.
  7. Select **Third-party service** as **Use case**.
  8. Click **Next**. 
     * Optional: Add description tag.
  9. Click **Create access key**.
  10. Click **Download .csv file** to save the **Access Key** and **Secret Access Key** for future reference.
  11. Click **Done**.
  12. Select **Permissions** tab.
  13. Click **Add permissions** in section **Permissions policies**.
  14. Select **Add permissions**.
  15. Select **Attach policies directly**.
  16. Search for **AmazonS3FullAccess** policy.
  17. Select the policy.
  18. Click **Next**.
  19. Click **Add permissions**.



### Install and Configure Log Shipper on VShell Server

Choose one of the following options based on your operating system:

#### Option A: Using NXLog (Windows)

  1. Download and install **NXLog Community Edition** from [nxlog.co](https://nxlog.co/downloads/nxlog-ce).
  2. Edit `C:\Program Files\nxlog\conf\nxlog.conf`:
         
         <Extension json>
             Module      xm_json
         </Extension>
         
         <Extension syslog>
             Module      xm_syslog
         </Extension>
         
         <Input vshell_log>
             Module      im_file
             File        "C:\\Program Files\\VanDyke Software\\VShell\\Log\\VShell.log"
             SavePos     TRUE
         
             <Exec>
                 # Parse VShell log format
                 if $raw_event =~ /^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) "(.*)"$/
                 {
                     $EventTime = $1;
                     $Protocol = $2;
                     $EventType = $3;
                     $SessionID = $4;
                     $ClientIP = $5;
                     $ClientPort = $6;
                     $Username = $7;
                     $Filename = $9;
                     $BytesDown = $10;
                     $BytesUp = $11;
                     $ServerIP = $14;
                     $ServerPort = $15;
                     $EventMessage = $16;
         
                     # Convert to JSON
                     to_json();
                 }
             </Exec>
         </Input>
         
         <Output s3>
             Module      om_exec
             Command     C:\scripts\upload_to_s3.ps1
             Args        %FILEPATH%
         </Output>
         
         <Route vshell_to_s3>
             Path        vshell_log => s3
         </Route>
         

  3. Create PowerShell script `C:\scripts\upload_to_s3.ps1`:
         
         param([string]$FilePath)
         
         $bucket = "vandyke-sftp-logs"
         $key = "vshell/$(Get-Date -Format 'yyyy/MM/dd/HH')/$(Get-Date -Format 'yyyyMMddHHmmss').json"
         
         # Batch logs
         $logs = Get-Content $FilePath | ConvertFrom-Json
         $jsonLines = $logs | ForEach-Object { $_ | ConvertTo-Json -Compress }
         $content = $jsonLines -join "`n"
         
         # Upload to S3
         Write-S3Object -BucketName $bucket -Key $key -Content $content -ProfileName default
         

  4. Create AWS credentials profile:
         
         Set-AWSCredential -AccessKey YOUR_ACCESS_KEY -SecretKey YOUR_SECRET_KEY -StoreAs default
         

  5. Schedule the PowerShell script to run every 5 minutes using Task Scheduler.




#### Option B: Using Fluent Bit (Linux)

  1. Install Fluent Bit:
         
         curl https://raw.githubusercontent.com/fluent/fluent-bit/master/install.sh | sh
         

  2. Configure `/etc/fluent-bit/fluent-bit.conf`:
         
         [SERVICE]
             Flush        5
             Daemon       On
             Log_Level    info
         
         [INPUT]
             Name              tail
             Path              /var/log/vshell/vshell.log
             Parser            vshell_parser
             Tag               vshell.*
             Refresh_Interval  5
             Mem_Buf_Limit     10MB
         
         [PARSER]
             Name        vshell_parser
             Format      regex
             Regex       ^(?<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?<protocol>\S+) (?<event_type>\S+) (?<session_id>\S+) (?<client_ip>\S+) (?<client_port>\S+) (?<username>\S+) (?<dash>\S+) (?<filename>\S+) (?<bytes_down>\S+) (?<bytes_up>\S+) (?<field1>\S+) (?<field2>\S+) (?<server_ip>\S+) (?<server_port>\S+) "(?<event_message>[^"]*)"
         
         [OUTPUT]
             Name                  s3
             Match                 vshell.*
             bucket                vandyke-sftp-logs
             region                us-east-1
             use_put_object        On
             total_file_size       5M
             upload_timeout        10s
             compression           gzip
             s3_key_format         /vshell/%Y/%m/%d/%H/%{hostname}_%{uuid}.json.gz
         

  3. Configure AWS credentials:
         
         export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
         export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
         

  4. Start Fluent Bit:
         
         sudo systemctl enable fluent-bit
         sudo systemctl start fluent-bit
         




## Configure a feed in Google SecOps to ingest VanDyke VShell logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `VanDyke VShell SFTP logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **VanDyke SFTP** as the **Log type** (custom).
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://vandyke-sftp-logs/vshell/`
     * **Source deletion options** : Select **Retain** (recommended) or deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## UDM mapping table

Log field | UDM mapping | Logic  
---|---|---  
`agent.id` | `read_only_udm.observer.asset_id` | Concatenates "filebeat:" with the value of agent.id field  
`agent.type` | `read_only_udm.observer.application` | Directly maps the value of agent.type field  
`agent.version` | `read_only_udm.observer.platform_version` | Directly maps the value of agent.version field  
`ecs.version` | `read_only_udm.metadata.product_version` | Directly maps the value of ecs.version field  
`host.architecture` | `read_only_udm.target.asset.hardware.cpu_platform` | Directly maps the value of host.architecture field  
`host.hostname` | `read_only_udm.target.hostname` | Directly maps the value of host.hostname field  
`host.id` | `read_only_udm.principal.asset_id` | Concatenates "VANDYKE_SFTP:" with the value of host.id field  
`host.ip` | `read_only_udm.target.ip` | Directly maps each IP address in the host.ip array to a separate read_only_udm.target.ip field  
`host.mac` | `read_only_udm.target.mac` | Directly maps each MAC address in the host.mac array to a separate read_only_udm.target.mac field  
`host.os.kernel` | `read_only_udm.target.platform_patch_level` | Directly maps the value of host.os.kernel field  
`host.os.platform` | `read_only_udm.target.platform` | Maps the value of host.os.platform to WINDOWS, LINUX, MAC, or UNKNOWN_PLATFORM based on the value  
`host.os.version` | `read_only_udm.target.platform_version` | Directly maps the value of host.os.version field  
`log.file.path` | `read_only_udm.principal.process.file.full_path` | Directly maps the value of log.file.path field  
`logstash.collect.timestamp` | `read_only_udm.metadata.collected_timestamp` | Parses the timestamp from logstash.collect.timestamp field and converts it to a timestamp object  
`logstash.irm_environment` | `read_only_udm.additional.fields.value.string_value` | Directly maps the value of logstash.irm_environment field. The key is set to "irm_environment"  
`logstash.irm_region` | `read_only_udm.additional.fields.value.string_value` | Directly maps the value of logstash.irm_region field. The key is set to "irm_region"  
`logstash.irm_site` | `read_only_udm.additional.fields.value.string_value` | Directly maps the value of logstash.irm_site field. The key is set to "irm_site"  
`logstash.process.host` | `read_only_udm.observer.hostname` | Directly maps the value of logstash.process.host field  
`message` |  | Used for extracting various fields using grok patterns and regular expressions  
| `read_only_udm.metadata.event_type` | Set to "NETWORK_FTP"  
| `read_only_udm.metadata.log_type` | Set to "VANDYKE_SFTP"  
| `read_only_udm.metadata.product_event_type` | Extracted from the message field using a grok pattern  
| `read_only_udm.metadata.product_name` | Set to "VANDYKE_SFTP"  
| `read_only_udm.metadata.vendor_name` | Set to "VANDYKE SOFTWARE"  
| `read_only_udm.network.application_protocol` | Set to "SSH" if the description field contains "SSH2" or "SSH", otherwise set to "HTTP" if the method field matches HTTP methods  
| `read_only_udm.network.http.method` | Extracted from the message field using a grok pattern, only if it matches common HTTP methods  
| `read_only_udm.network.http.referral_url` | Extracted from the message field using a grok pattern  
| `read_only_udm.network.http.response_code` | Extracted from the message field using a grok pattern and converted to an integer  
| `read_only_udm.network.ip_protocol` | Set to "TCP" if the description field contains "TCP"  
| `read_only_udm.principal.ip` | Extracted from the message field using a grok pattern  
| `read_only_udm.principal.port` | Extracted from the message field using a grok pattern and converted to an integer  
| `read_only_udm.security_result.description` | Extracted from the message field using a grok pattern  
| `read_only_udm.security_result.severity` | Set to "HIGH" if syslog_severity is "error" or "warning", "MEDIUM" if it's "notice", and "LOW" if it's "information" or "info"  
| `read_only_udm.security_result.severity_details` | Directly maps the value of syslog_severity field  
| `read_only_udm.target.ip` | Extracted from the message field using a grok pattern  
| `read_only_udm.target.port` | Extracted from the message field using a grok pattern and converted to an integer  
| `read_only_udm.target.process.pid` | Extracted from the message field using a grok pattern  
`syslog_severity` |  | Used for determining the severity of the security_result  
`username` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`username` | `event.idm.read_only_udm.target.user.user_display_name` | Mapped from changelog  
`id` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`reason` | `security_result.summary` | Mapped from changelog  
`srcip` | `principal.ip` | Mapped from changelog  
`username` | `principal.user.user_display_name` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vandyke-sftp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
