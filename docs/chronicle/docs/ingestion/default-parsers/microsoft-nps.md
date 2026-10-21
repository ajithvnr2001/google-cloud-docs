---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-nps/
title: Collect Microsoft Network Policy Server (NPS) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:55:47.990767+00:00
---

# Collect Microsoft Network Policy Server (NPS) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-nps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Microsoft Network Policy Server (NPS) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Microsoft Network Policy Server (NPS) logs to Google Security Operations using Google Cloud Storage V2.

Microsoft Network Policy Server (NPS) is a Windows Server role that provides RADIUS authentication, authorization, and accounting. NPS enables centralized management of network access policies for wireless devices, VPN connections, switches, and remote access. NPS does not have native cloud export capabilities or APIs, so logs must be collected using a third-party forwarder.

## Before you begin

Ensure that you have the following prerequisites:

  * A Google SecOps instance
  * A GCP project with Cloud Storage API enabled
  * Permissions to create and manage GCS buckets
  * Permissions to manage IAM policies on GCS buckets
  * Privileged access to the Windows Server running NPS
  * Administrator access to install NXLog on the NPS server



## Configure NPS logging

### Enable NPS accounting logs

  1. On the Windows Server running NPS, open **Server Manager**.
  2. Go to **Tools > Network Policy Server**.
  3. In the NPS console, expand **Accounting** in the left navigation.
  4. Right-click **Accounting** and select **Configure Accounting**.
  5. In the **Accounting Configuration** wizard, click **Next**.
  6. Select **Log to a text file on the local computer** and click **Next**.
  7. In the **Configure Log File Properties** page, configure the following: 
     * **Directory** : Leave as default (`%systemroot%\System32\LogFiles`) or specify a custom path
     * **Format** : Select **DTS Compliant** (recommended by Microsoft for structured XML format)
     * **Create a new log file** : Select **Daily** or **Weekly** based on your log volume
  8. Click **Next**.
  9. Review the summary and click **Finish**.

**Note:** The default log file location is `C:\Windows\System32\LogFiles`. NPS creates log files with the naming convention `INyymmdd.log` (for example, `IN250315.log` for March 15, 2025).

### Enable NPS audit logging

  1. Open **Command Prompt** as Administrator on the NPS server.
  2. Run the following command to enable NPS audit logging:
         
         auditpol /set /subcategory:"Network Policy Server" /success:enable /failure:enable
         

  3. Verify the audit policy is enabled:
         
         auditpol /get /subcategory:"Network Policy Server"
         


**Note:** This enables Windows Event Log entries for NPS authentication events (Event IDs 6272-6280) in addition to the text file logs.

## Install and configure NXLog on the NPS server

### Download and install NXLog

  1. On the NPS server, download NXLog Enterprise Edition from the [NXLog website](https://nxlog.co/products/nxlog-enterprise-edition).
  2. Run the installer and follow the installation wizard.
  3. Accept the default installation path (`C:\Program Files\nxlog`) or specify a custom path.
  4. Complete the installation.



### Configure NXLog to collect NPS logs

  1. On the NPS server, navigate to the NXLog configuration directory: 
     * Default path: `C:\Program Files\nxlog\conf`
  2. Open the file `nxlog.conf` in a text editor (for example, Notepad) with Administrator privileges.
  3. Replace the entire contents of `nxlog.conf` with the following configuration:
         
         ## NXLog configuration for Microsoft NPS log collection
         ## Collects NPS logs and forwards to Google Cloud Storage
         
         define ROOT C:\Program Files\nxlog
         define LOGDIR C:\Windows\System32\LogFiles
         define GCS_BUCKET your-gcs-bucket-name
         define GCS_PREFIX nps-logs
         define GCS_CREDENTIALS C:\nxlog-credentials\gcs-service-account.json
         
         Moduledir %ROOT%\modules
         CacheDir %ROOT%\data
         Pidfile %ROOT%\data\nxlog.pid
         SpoolDir %ROOT%\data
         LogFile %ROOT%\data\nxlog.log
         LogLevel INFO
         
         <Extension nps>
             Module xm_nps
         </Extension>
         
         <Extension json>
             Module xm_json
         </Extension>
         
         <Input nps_logs>
             Module im_file
             File '%LOGDIR%\IN*.log'
             SavePos TRUE
             ReadFromLast TRUE
             Recursive FALSE
             InputType nps
             <Exec>
                 # Parse NPS logs (DTS Compliant format)
                 # Add hostname for tracking
                 $Hostname = hostname();
         
                 # Convert to JSON
                 to_json();
             </Exec>
         </Input>
         
         <Output gcs>
             Module om_file
             File '%ROOT%\data\gcs-upload\nps-' + strftime(now(), '%Y%m%d-%H%M%S') + '.json'
             <Exec>
                 # Rotate output file every hour
                 if (file_size(file_name()) > 100000000) file_cycle();
             </Exec>
         </Output>
         
         <Route nps_to_gcs>
             Path nps_logs => gcs
         </Route>
         

  4. In the configuration file, replace the following placeholders:

     * `your-gcs-bucket-name`: Your GCS bucket name (created in the next section)
     * Verify the `LOGDIR` path matches your NPS log file location
  5. Save the file.


**Note:** This configuration collects NPS logs from the default location and writes them to local JSON files. In the next steps, you will configure a script to upload these files to GCS.

## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `nps-logs-chronicle`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Create GCS service account for NXLog

### Create service account

  1. In the **GCP Console** , go to **IAM & Admin > Service Accounts**.
  2. Click **Create Service Account**.
  3. Provide the following configuration details: 
     * **Service account name** : Enter `nxlog-nps-uploader` (for example)
     * **Service account description** : Enter `Service account for NXLog to upload NPS logs to GCS`
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, add the following role: 
     1. Click **Select a role**.
     2. Search for and select **Storage Object Creator**.
  6. Click **Continue**.
  7. Click **Done**.



### Download service account key

  1. On the **Service Accounts** page, click on the service account you just created (`nxlog-nps-uploader`).
  2. Go to the **Keys** tab.
  3. Click **Add Key > Create new key**.
  4. Select **JSON** as the key type.
  5. Click **Create**.
  6. The JSON key file will be downloaded to your computer.
  7. Copy the JSON key file to the NPS server at the following location: 
     * `C:\nxlog-credentials\gcs-service-account.json`
  8. Create the directory `C:\nxlog-credentials` if it does not exist.

**Note:** Protect this key file with appropriate NTFS permissions. Only the NXLog service account and administrators should have read access.

## Configure automated GCS upload

### Create PowerShell upload script

  1. On the NPS server, create a new directory: 
     * `C:\nxlog-scripts`
  2. Create a new file named `upload-to-gcs.ps1` in the directory.
  3. Open the file in a text editor and paste the following PowerShell script:
         
         # PowerShell script to upload NXLog output files to Google Cloud Storage
         # Uses gsutil command-line tool
         
         $ErrorActionPreference = "Stop"
         
         # Configuration
         $LocalLogDir = "C:\Program Files\nxlog\data\gcs-upload"
         $GcsBucket = "gs://nps-logs-chronicle/nps-logs/"
         $ArchiveDir = "C:\Program Files\nxlog\data\archive"
         $LogFile = "C:\nxlog-scripts\upload.log"
         
         # Function to write log messages
         function Write-Log {
             param([string]$Message)
             $Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
             "$Timestamp - $Message" | Out-File -FilePath $LogFile -Append
         }
         
         Write-Log "Starting GCS upload process"
         
         # Check if gsutil is available
         try {
             $null = gsutil version
         } catch {
             Write-Log "ERROR: gsutil not found. Please install Google Cloud SDK."
             exit 1
         }
         
         # Activate service account
         $ServiceAccountKey = "C:\nxlog-credentials\gcs-service-account.json"
         if (-not (Test-Path $ServiceAccountKey)) {
             Write-Log "ERROR: Service account key not found at $ServiceAccountKey"
             exit 1
         }
         
         try {
             gcloud auth activate-service-account --key-file=$ServiceAccountKey 2>&1 | Out-Null
             Write-Log "Service account activated successfully"
         } catch {
             Write-Log "ERROR: Failed to activate service account: $_"
             exit 1
         }
         
         # Create archive directory if it doesn't exist
         if (-not (Test-Path $ArchiveDir)) {
             New-Item -ItemType Directory -Path $ArchiveDir | Out-Null
             Write-Log "Created archive directory: $ArchiveDir"
         }
         
         # Get all JSON files in the local log directory
         $Files = Get-ChildItem -Path $LocalLogDir -Filter "*.json" -File
         
         if ($Files.Count -eq 0) {
             Write-Log "No files to upload"
             exit 0
         }
         
         Write-Log "Found $($Files.Count) file(s) to upload"
         
         # Upload each file to GCS
         $SuccessCount = 0
         $FailCount = 0
         
         foreach ($File in $Files) {
             try {
                 # Upload to GCS
                 gsutil cp $File.FullName $GcsBucket 2>&1 | Out-Null
         
                 # Move to archive on success
                 Move-Item -Path $File.FullName -Destination $ArchiveDir -Force
         
                 Write-Log "Uploaded and archived: $($File.Name)"
                 $SuccessCount++
             } catch {
                 Write-Log "ERROR uploading $($File.Name): $_"
                 $FailCount++
             }
         }
         
         Write-Log "Upload complete. Success: $SuccessCount, Failed: $FailCount"
         

  4. In the script, replace the following values:

     * `$GcsBucket`: Your GCS bucket URI (for example, `gs://nps-logs-chronicle/nps-logs/`)
  5. Save the file.




### Install Google Cloud SDK

  1. On the NPS server, download the Google Cloud SDK installer from [Google Cloud SDK](https://docs.cloud.google.com/sdk/docs/install-sdk).
  2. Run the installer and follow the installation wizard.
  3. During installation, select **Install bundled Python** if Python is not already installed.
  4. Complete the installation.
  5. Open a new **Command Prompt** and verify the installation:
         
         gsutil version
         


**Note:** The `gsutil` command-line tool is included with the Google Cloud SDK and is used to upload files to GCS.

### Create scheduled task for automated upload

  1. On the NPS server, open **Task Scheduler**.
  2. In the right panel, click **Create Task**.
  3. In the **General** tab, configure the following: 
     * **Name** : Enter `NXLog GCS Upload`
     * **Description** : Enter `Upload NPS logs to Google Cloud Storage`
     * **Security options** : Select **Run whether user is logged on or not**
     * **Security options** : Check **Run with highest privileges**
     * **Configure for** : Select **Windows Server 2016** or your server version
  4. In the **Triggers** tab: 
     1. Click **New**.
     2. **Begin the task** : Select **On a schedule**.
     3. **Settings** : Select **Daily**.
     4. **Recur every** : Enter `1` days.
     5. **Repeat task every** : Select **15 minutes**.
     6. **for a duration of** : Select **Indefinitely**.
     7. Click **OK**.
  5. In the **Actions** tab: 
     1. Click **New**.
     2. **Action** : Select **Start a program**.
     3. **Program/script** : Enter `powershell.exe`.
     4. **Add arguments** : Enter `-ExecutionPolicy Bypass -File "C:\nxlog-scripts\upload-to-gcs.ps1"`.
     5. Click **OK**.
  6. In the **Conditions** tab: 
     * Uncheck **Start the task only if the computer is on AC power**.
  7. In the **Settings** tab: 
     * Check **Run task as soon as possible after a scheduled start is missed**.
     * Check **If the task fails, restart every** : Enter `5 minutes`.
  8. Click **OK**.
  9. Enter the credentials for the account that will run the task (must have Administrator privileges).
  10. Click **OK**.



### Test the upload process

  1. On the NPS server, open **Task Scheduler**.
  2. In the left panel, expand **Task Scheduler Library**.
  3. Right-click the task **NXLog GCS Upload** and select **Run**.
  4. Wait a few seconds for the task to complete.
  5. Open the log file at `C:\nxlog-scripts\upload.log` to verify the upload was successful.
  6. Go to the **GCP Console > Cloud Storage > Buckets**.
  7. Click on your bucket name (`nps-logs-chronicle`).
  8. Navigate to the `nps-logs/` folder.
  9. Verify that JSON files with NPS logs are present.



## Start NXLog service

  1. On the NPS server, open **Services** (run `services.msc`).
  2. Locate the **nxlog** service in the list.
  3. Right-click the **nxlog** service and select **Start**.
  4. Verify the service status is **Running**.
  5. To verify NXLog is collecting logs, check the NXLog log file: 
     * `C:\Program Files\nxlog\data\nxlog.log`
  6. Look for messages indicating successful log collection:
         
         INFO im_file: monitoring file 'C:\Windows\System32\LogFiles\IN250315.log'
         


**Note:** NXLog will automatically start collecting NPS logs and writing them to the local output directory. The scheduled task will upload these files to GCS every 15 minutes.

## Retrieve the Google SecOps service account

Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.

### Get the service account email

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Microsoft NPS Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **MICROSOFT_NPS** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         ```none
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         ```
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://nps-logs-chronicle/nps-logs/
           

       * Replace: 
         * `nps-logs-chronicle`: Your GCS bucket name.
         * `nps-logs/`: The prefix/folder path where logs are stored.
**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing).
       * **Delete transferred files** : Deletes files after successful transfer.
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer.
**Note:** If you select a deletion option, the service account must have **Storage Object Admin** role instead of Storage Object Viewer. Update IAM permissions accordingly.
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  11. Click **Next**.

  12. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## Grant IAM permissions to the Google SecOps service account

  * The Google SecOps service account needs **Storage Object Viewer** role on your GCS bucket.


  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name (`nps-logs-chronicle`).
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
Version | additional.fields | Merged with corresponding objects if not empty  
Channel | additional.fields |   
Keywords | additional.fields |   
Opcode | additional.fields |   
Task | additional.fields |   
ThreadID | additional.fields |   
EventData.%1 | additional.fields |   
EventData.%2 | additional.fields |   
Channel | channel.value.string_value | Value copied directly  
EventData.%1 | event_data_p1.value.string_value | Value copied directly  
EventData.%2 | event_data_p2.value.string_value | Value copied directly  
Keywords | keywords.value.string_value | Value copied directly  
TimeCreated | metadata.event_timestamp | Converted from UNIX_MS to timestamp  
EventId | metadata.event_type | Set to STATUS_UNCATEGORIZED if EventId == '4400', STATUS_UPDATE if EventId == '13', else GENERIC_EVENT  
EventId | metadata.product_event_type | Value copied directly  
Opcode | opcode.value.string_value | Value copied directly  
Computer | principal.asset.hostname | Value copied from principal.hostname  
Computer | principal.hostname | Value copied directly  
ProcessID | principal.process.pid | Value copied if not empty  
UserId | principal.user.windows_sid | Extracted using regex to get Windows SID  
EventId | security_result.rule_name | Set to "EventID: " + EventId  
Level | security_result.severity | Transformed: INFO/Informational/Information/Normal/NOTICE to INFORMATIONAL, ERROR/Error to ERROR, WARNING/Warning to INFORMATIONAL, DEBUG to INFORMATIONAL, Critical to CRITICAL  
Task | task.value.string_value | Value copied directly  
ThreadID | thread_id.value.string_value | Value copied directly  
Version | version.value.string_value | Value copied directly  
metadata.vendor_name | metadata.vendor_name | Set to "Microsoft"  
ProviderName | metadata.product_name | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-nps-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
