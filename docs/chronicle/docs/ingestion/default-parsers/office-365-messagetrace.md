---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace/
title: Collect Office 365 Message Trace logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:19.340585+00:00
---

# Collect Office 365 Message Trace logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/office-365-messagetrace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Office 365 Message Trace logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Office 365 Message Trace logs to Google Security Operations using multiple ingestion methods. An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `OFFICE_365_MESSAGETRACE` ingestion label.

Office 365 Message Trace is a Microsoft Exchange Online feature that tracks email messages as they travel through the Exchange Online mail flow pipeline. Message trace logs provide detailed information about each email message, including sender and recipient addresses, subject, delivery status, source and destination IP addresses, and message size. This data is essential for troubleshooting mail delivery issues, investigating suspicious email activity, and monitoring email traffic patterns.

Message trace data is retrieved programmatically using the `Get-MessageTraceV2` cmdlet in [Exchange Online PowerShell](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2). The Exchange Online PowerShell module (ExchangeOnlineManagement) is [officially supported](https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2#supported-operating-systems-for-the-exchange-online-powershell-module) on Windows, macOS, and Linux with PowerShell 7.4.0 or later (and Windows PowerShell 5.1 on Windows).

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * A Microsoft 365 tenant with Exchange Online
  * A Global Administrator, Exchange Administrator, or Security Reader role in Microsoft 365
  * Access to Google Cloud Console (for API key creation, GCS, and webhooks)
  * Permissions to create and manage feeds in Google SecOps
  * A dedicated Windows, macOS, or Linux server or workstation to run the export script: 
    * **Windows** : Windows 10/11 or Windows Server 2016 or later with Windows PowerShell 5.1 (built-in) or PowerShell 7.4.0 or later
    * **macOS** : macOS 13 Ventura or later with [PowerShell 7.4.0 or later](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-macos)
    * **Linux** : Debian 11+, Ubuntu 20.04+, RHEL 8+, or Fedora 36+ with [PowerShell 7.4.0 or later](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-linux)
  * Network connectivity from the export machine to both Microsoft 365 and the Google SecOps ingestion endpoint



## Set up the export environment

Office 365 Message Trace does not have a built-in push capability. You must run an export script on a dedicated Windows, macOS, or Linux server or workstation that retrieves message trace data from Exchange Online using PowerShell and sends it to Google SecOps.

Message trace data is available through Exchange Online PowerShell with the following retention limits:

  * `Get-MessageTraceV2`: Returns data for the last **10 days**. Results are available instantly.
  * `Start-HistoricalSearch`: Returns data for **10 to 90 days**. Results are prepared as downloadable CSV reports and may take several hours.



The following steps install PowerShell and the Exchange Online PowerShell module on your machine.

### Install PowerShell

#### Windows

Windows PowerShell 5.1 is included with Windows 10, Windows 11, and Windows Server 2016 or later. No additional installation is required.

  * To verify your PowerShell version, open **PowerShell** and run:
        
        $PSVersionTable.PSVersion
        

  * Optionally, to install PowerShell 7 for improved performance, open **Command Prompt** or **PowerShell** as an administrator and run:
        
        winget install --id Microsoft.PowerShell --source winget
        




#### macOS

  1. Install [Homebrew](https://brew.sh/) if not already installed.
  2. Open **Terminal** and run the following command:
         
         brew install powershell/tap/powershell
         

  3. Verify the installation by running:
         
         pwsh --version
         

The output should display `PowerShell 7.x.x` or later.




#### Linux (Debian/Ubuntu)

  1. Open a terminal with root or sudo privileges.
  2. Run the following commands:
         
         sudo apt-get update
         sudo apt-get install -y wget apt-transport-https software-properties-common
         source /etc/os-release
         wget -q "https://packages.microsoft.com/config/ubuntu/$VERSION_ID/packages-microsoft-prod.deb"
         sudo dpkg -i packages-microsoft-prod.deb
         rm packages-microsoft-prod.deb
         sudo apt-get update
         sudo apt-get install -y powershell
         

  3. Verify the installation by running:
         
         pwsh --version
         




#### Linux (RHEL/CentOS/Fedora)

  1. Open a terminal with root or sudo privileges.
  2. Register the Microsoft repository:
         
         curl "https://packages.microsoft.com/config/rhel/$(rpm -E %rhel)/prod.repo" | sudo tee /etc/yum.repos.d/microsoft.repo
         

  3. Install PowerShell:
         
         sudo dnf install -y powershell
         

  4. Verify the installation by running:
         
         pwsh --version
         




### Install the Exchange Online PowerShell module

After installing PowerShell, install the Exchange Online management module. This step is the same on all platforms.

  1. Launch PowerShell:

     * **Windows** : Open **PowerShell** or **PowerShell 7** as an administrator
     * **macOS and Linux** : Open a terminal and run `pwsh`
  2. Run the following command:
         
         Install-Module -Name ExchangeOnlineManagement -Scope CurrentUser -Force
         

  3. If prompted to install from an untrusted repository (PSGallery), enter `Y` to confirm.

  4. Verify the installation by running:
         
         Import-Module ExchangeOnlineManagement
         Get-Module ExchangeOnlineManagement | Select-Object Name, Version
         




The output should display the module name and version number.

### Set up certificate-based authentication (required for scheduled scripts)

The `Connect-ExchangeOnline -UserPrincipalName` method requires interactive sign-in and cannot be used in scheduled scripts. For unattended execution, set up certificate-based authentication with an Azure AD (Microsoft Entra ID) application.

#### Create a self-signed certificate

  * **Windows** (run in PowerShell as administrator):
        
        mkdir C:\Certs
        $cert = New-SelfSignedCertificate -Subject "CN=MessageTraceExport" -CertStoreLocation "Cert:\CurrentUser\My" -KeyExportPolicy Exportable -KeySpec KeyExchange -KeyLength 2048 -NotAfter (Get-Date).AddYears(2)
        $cert.Thumbprint
        Export-Certificate -Cert $cert -FilePath "C:\Certs\MessageTraceExport.cer"
        

Save the thumbprint value for use in later steps.

  * **macOS and Linux** (run in a terminal):
        
        mkdir -p /opt/certs
        openssl req -x509 -newkey rsa:2048 -keyout /opt/certs/messagetrace-key.pem -out /opt/certs/messagetrace-cert.pem -days 730 -nodes -subj "/CN=MessageTraceExport"
        openssl pkcs12 -export -out /opt/certs/messagetrace.pfx -inkey /opt/certs/messagetrace-key.pem -in /opt/certs/messagetrace-cert.pem -passout pass:
        chmod 644 /opt/certs/messagetrace.pfx
        

**Note:** The `chmod 644` command makes the `.pfx` file readable by the PowerShell process. Without it, `Connect-ExchangeOnline` can fail to load the certificate with a permissions error on Linux.
  * Get the certificate thumbprint:
        
        openssl x509 -in /opt/certs/messagetrace-cert.pem -noout -fingerprint -sha1 | sed 's/://g' | cut -d= -f2
        

Save the thumbprint value for use in later steps.




#### Register the application in Microsoft Entra ID

  1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com/).
  2. Go to **Identity > Applications > App registrations**.
  3. Click **New registration**.
  4. Provide the following configuration details: 
     * **Name** : Enter `MessageTraceExport`
     * **Supported account types** : Select **Accounts in this organizational directory only**
  5. Click **Register**.
  6. On the application overview page, copy the **Application (client) ID** and save it.
  7. Copy the **Directory (tenant) ID** from the overview page and save it.



#### Upload the certificate to the application

  1. On the application page, go to **Certificates & secrets > Certificates**.
  2. Click **Upload certificate**.
  3. Upload the certificate file: 
     * **Windows** : Upload `C:\Certs\MessageTraceExport.cer`
     * **macOS and Linux** : Upload `/opt/certs/messagetrace-cert.pem`
  4. Click **Add**.



#### Assign API permissions

The export script runs the `Get-MessageTraceV2` cmdlet, which requires two **Office 365 Exchange Online** application permissions: `Exchange.ManageAsApp` (to authenticate as an app) and `ReportingWebService.Read.All` (to read message trace data). If `ReportingWebService.Read.All` is missing, the script fails with a `403` `The caller does not have permission` error.

  1. On the application page, go to **API permissions**.
  2. Click **Add a permission**.
  3. Select **APIs my organization uses**.
  4. Search for and select **Office 365 Exchange Online**.
  5. Select **Application permissions**.
  6. Add both of the following permissions: 
     * Expand **Exchange** and select **Exchange.ManageAsApp**.
     * Expand **ReportingWebService** and select **ReportingWebService.Read.All**.
  7. Click **Add permissions**.
  8. Click **Grant admin consent for <your organization>** and confirm.

**Note:** The app registration includes a default **Microsoft Graph** `User.Read` (delegated) permission. It is not used by app-only certificate authentication and does not need to be granted; you can leave it as is.



#### Assign the Exchange Administrator role

  1. In the Microsoft Entra admin center, go to **Identity > Roles & admins > All roles**.
  2. Search for and select **Exchange Administrator**.
  3. Click **Add assignments**.
  4. Click **No member selected** and search for the `MessageTraceExport` application.
  5. Select the application and click **Next**.
  6. Select **Active** as the assignment type.
  7. Click **Assign**.



#### Verify an unattended connection

Launch PowerShell and run:

  * **Windows:**
        
        Connect-ExchangeOnline -CertificateThumbprint "<CERTIFICATE_THUMBPRINT>" -AppId "<APPLICATION_ID>" -Organization "yourdomain.onmicrosoft.com"
        Get-MessageTraceV2 -StartDate (Get-Date).AddHours(-1) -EndDate (Get-Date) -ResultSize 1
        Disconnect-ExchangeOnline -Confirm:$false
        

  * **macOS and Linux** (run `pwsh` first):
        
        Connect-ExchangeOnline -CertificateFilePath "/opt/certs/messagetrace.pfx" -AppId "<APPLICATION_ID>" -Organization "yourdomain.onmicrosoft.com"
        Get-MessageTraceV2 -StartDate (Get-Date).AddHours(-1) -EndDate (Get-Date) -ResultSize 1
        Disconnect-ExchangeOnline -Confirm:$false
        

Replace `<CERTIFICATE_THUMBPRINT>`, `<APPLICATION_ID>`, and `yourdomain.onmicrosoft.com` with your actual values. If the command returns message trace data (or an empty result set with no errors), the authentication is working correctly.




## Choose your ingestion method

Google SecOps supports multiple ingestion methods for Office 365 Message Trace logs. Select the method that best fits your environment:

Ingestion Method | Use Case | Latency | Setup Complexity  
---|---|---|---  
**Webhook** | Real-time push from scripts or applications | Seconds | Low  
**Google Cloud Storage V2** | Batch export to GCS bucket | Minutes to hours | Medium  
  
## Option 1: Webhook ingestion

Use this method when you have a script or application that can send `HTTP POST` requests containing message trace data to Google SecOps.

### Create a webhook feed in Google SecOps

#### Create the feed

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Office 365 Message Trace - Webhook`).
  5. Select **Webhook** as the **Source type**.
  6. Select **Office 365 Message Trace** as the **Log type**.
  7. Click **Next**.
  8. Specify values for the following input parameters: 
     * **Split delimiter** (optional): Enter `\n` to split newline-delimited JSON events
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  9. Click **Next**.
  10. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



#### Generate and save a secret key

After creating the feed, you must generate a secret key for authentication:

  1. On the feed details page, click **Generate Secret Key**.
  2. A dialog displays the secret key.
  3. **Copy and save** the secret key securely.

**Important:** The secret key is displayed only once and cannot be retrieved later. If you lose it, you must generate a new secret key.



#### Get the feed endpoint URL

  1. Go to the **Details** tab of the feed.
  2. In the **Endpoint Information** section, copy the **Feed endpoint URL**.
  3. The URL format is:
         
         https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import
         

Where `{region}` is the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`), and `{parent}` is the resource path in the format `projects/<PROJECT_ID>/locations/<LOCATION>/instances/<INSTANCE_ID>/logTypes/<LOG_TYPE>`.

  4. Save this URL for the next steps.

  5. Click **Done**.




### Create a Google Cloud API key

Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.

#### Create the API key

  1. Go to the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
  2. Select your project (the project associated with your Google SecOps instance).
  3. Click **Create credentials > API key**.
  4. An API key is created and displayed in a dialog.
  5. Click **Edit API key** to restrict the key.



#### Restrict the API key

  1. In the **API key** settings page: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Webhook API Key - O365 Message Trace`)
  2. Under **API restrictions** : 
     1. Select **Restrict key**.
     2. In the **Select APIs** dropdown, search for and select **Google SecOps API** (or **Chronicle API**).
  3. Click **Save**.
  4. **Copy** the API key value from the **API key** field at the top of the page.
  5. Save the API key securely.

**Note:** Restricting the API key ensures it can only be used with the Google SecOps API, reducing security risk if the key is compromised.



### Create the webhook export script

Create the following PowerShell script on the machine where you set up the export environment. This script retrieves message trace data from Exchange Online and sends it to the Google SecOps webhook endpoint.

#### Windows

  1. Create the script directory:
         
         mkdir C:\Scripts
         

  2. Create a file named `C:\Scripts\messagetrace-webhook.ps1` with the following content:
         
         # Configuration
         $endpointUrl = "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import"
         $apiKey = "<API_KEY>"
         $secretKey = "<SECRET_KEY>"
         $certThumbprint = "<CERTIFICATE_THUMBPRINT>"
         $appId = "<APPLICATION_ID>"
         $organization = "yourdomain.onmicrosoft.com"
         
         # Log file
         $logFile = "C:\Logs\messagetrace-webhook.log"
         if (!(Test-Path "C:\Logs")) { New-Item -ItemType Directory -Path "C:\Logs" }
         
         try {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Starting message trace export"
         
             # Connect to Exchange Online using certificate-based authentication
             Connect-ExchangeOnline -CertificateThumbprint $certThumbprint -AppId $appId -Organization $organization -ShowBanner:$false
         
             # Retrieve message trace data for the last hour (up to 10 days available)
             $startDate = (Get-Date).AddHours(-1)
             $endDate = Get-Date
             $messages = Get-MessageTraceV2 -StartDate $startDate -EndDate $endDate -ResultSize 5000
         
             if ($messages.Count -eq 0) {
                 Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - No messages found in the time range"
                 Disconnect-ExchangeOnline -Confirm:$false
                 exit 0
             }
         
             # Convert to NDJSON (one JSON object per line)
             $ndjson = ($messages | ForEach-Object { $_ | ConvertTo-Json -Compress }) -join "`n"
         
             # Send to Google SecOps webhook
             $headers = @{
                 "X-goog-api-key"       = $apiKey
                 "X-Webhook-Access-Key" = $secretKey
             }
         
             # Send raw UTF-8 bytes so PowerShell does not re-encode the NDJSON body
             $bodyBytes = [System.Text.Encoding]::UTF8.GetBytes($ndjson)
             $response = Invoke-RestMethod -Uri $endpointUrl -Method Post -Headers $headers -Body $bodyBytes -ContentType "application/json"
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Successfully sent $($messages.Count) messages"
         }
         catch {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Error: $_"
         }
         finally {
             Disconnect-ExchangeOnline -Confirm:$false -ErrorAction SilentlyContinue
         }
         

  3. Replace the placeholder values:

     * `<API_KEY>`: The Google Cloud API key
     * `<SECRET_KEY>`: The Google SecOps webhook secret key
     * `<CERTIFICATE_THUMBPRINT>`: The certificate thumbprint from the authentication setup
     * `<APPLICATION_ID>`: The Azure AD application (client) ID
     * `yourdomain.onmicrosoft.com`: Your Microsoft 365 tenant domain



#### macOS and Linux

  1. Create the script directory:
         
         sudo mkdir -p /opt/scripts
         sudo mkdir -p /var/log/messagetrace
         

  2. Create a file named `/opt/scripts/messagetrace-webhook.ps1` with the following content:
         
         # Configuration
         $endpointUrl = "https://{region}-chronicle.googleapis.com/v1/{parent}/logs:import"
         $apiKey = "<API_KEY>"
         $secretKey = "<SECRET_KEY>"
         $certFilePath = "/opt/certs/messagetrace.pfx"
         $appId = "<APPLICATION_ID>"
         $organization = "yourdomain.onmicrosoft.com"
         
         # Log file
         $logFile = "/var/log/messagetrace/messagetrace-webhook.log"
         
         try {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Starting message trace export"
         
             # Connect to Exchange Online using certificate-based authentication
             Connect-ExchangeOnline -CertificateFilePath $certFilePath -AppId $appId -Organization $organization -ShowBanner:$false
         
             # Retrieve message trace data for the last hour (up to 10 days available)
             $startDate = (Get-Date).AddHours(-1)
             $endDate = Get-Date
             $messages = Get-MessageTraceV2 -StartDate $startDate -EndDate $endDate -ResultSize 5000
         
             if ($messages.Count -eq 0) {
                 Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - No messages found in the time range"
                 Disconnect-ExchangeOnline -Confirm:$false
                 exit 0
             }
         
             # Convert to NDJSON (one JSON object per line)
             $ndjson = ($messages | ForEach-Object { $_ | ConvertTo-Json -Compress }) -join "`n"
         
             # Send to Google SecOps webhook
             $headers = @{
                 "X-goog-api-key"       = $apiKey
                 "X-Webhook-Access-Key" = $secretKey
             }
         
             # Send raw UTF-8 bytes so PowerShell does not re-encode the NDJSON body
             $bodyBytes = [System.Text.Encoding]::UTF8.GetBytes($ndjson)
             $response = Invoke-RestMethod -Uri $endpointUrl -Method Post -Headers $headers -Body $bodyBytes -ContentType "application/json"
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Successfully sent $($messages.Count) messages"
         }
         catch {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Error: $_"
         }
         finally {
             Disconnect-ExchangeOnline -Confirm:$false -ErrorAction SilentlyContinue
         }
         

  3. Replace the placeholder values:

     * `<API_KEY>`: The Google Cloud API key
     * `<SECRET_KEY>`: The Google SecOps webhook secret key
     * `<APPLICATION_ID>`: The Azure AD application (client) ID
     * `yourdomain.onmicrosoft.com`: Your Microsoft 365 tenant domain
  4. Set file permissions:
         
         sudo chmod 700 /opt/scripts/messagetrace-webhook.ps1
         




### Schedule the export script

Configure the script to run automatically at regular intervals (for example, every hour).

**Note:** The `Get-MessageTraceV2` cmdlet returns data for the last 10 days. Results are available instantly. Running the script every hour ensures continuous coverage without data gaps. For historical data from 10 to 90 days, use the [`Start-HistoricalSearch`](https://learn.microsoft.com/en-us/powershell/module/exchange/start-historicalsearch) cmdlet, which generates downloadable CSV reports (results may take several hours to prepare).

#### Windows

  1. Open **Task Scheduler** : Press `Win+R`, type `taskschd.msc`, and press `Enter`.
  2. In the right pane, click **Create Task**.
  3. On the **General** tab: 
     * **Name** : Enter `MessageTrace Webhook Export`
     * Select **Run whether user is logged on or not**
     * Select **Run with highest privileges**
  4. On the **Triggers** tab: 
     1. Click **New**.
     2. Set **Begin the task** to **On a schedule**.
     3. Select **Daily** , set **Start** time to `12:00:00 AM` (midnight, so it repeats on whole hours), and set **Recur every 1 days**.
     4. Select **Repeat task every** `1 hour` for a duration of **Indefinitely**.
     5. Select **Enabled**.
     6. Click **OK**.
  5. On the **Actions** tab:

     1. Click **New**.
     2. Set **Action** to **Start a program**.
     3. In the **Program/script** field, enter:
            
            powershell.exe
            

     4. In the **Add arguments** field, enter:
            
            -NoProfile -ExecutionPolicy Bypass -File "C:\Scripts\messagetrace-webhook.ps1"
            

     5. Click **OK**.

  6. On the **Settings** tab:

     * Select **Allow task to be run on demand**
     * Clear the **Stop the task if it runs longer than** checkbox
  7. Click **OK** and enter the service account credentials when prompted.




#### macOS

  1. Create a launchd plist file at `~/Library/LaunchAgents/com.chronicle.messagetrace-webhook.plist`:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
         <plist version="1.0">
         <dict>
             <key>Label</key>
             <string>com.chronicle.messagetrace-webhook</string>
             <key>ProgramArguments</key>
             <array>
                 <string>/usr/local/bin/pwsh</string>
                 <string>-NoProfile</string>
                 <string>-File</string>
                 <string>/opt/scripts/messagetrace-webhook.ps1</string>
             </array>
             <key>StartInterval</key>
             <integer>3600</integer>
             <key>StandardOutPath</key>
             <string>/var/log/messagetrace/launchd-stdout.log</string>
             <key>StandardErrorPath</key>
             <string>/var/log/messagetrace/launchd-stderr.log</string>
             <key>RunAtLoad</key>
             <true/>
         </dict>
         </plist>
         

**Note:** If you use an Apple Silicon Mac (M1, M2, M3, M4), replace `/usr/local/bin/pwsh` with `/opt/homebrew/bin/pwsh`.
  2. Load the job:
         
         launchctl load ~/Library/LaunchAgents/com.chronicle.messagetrace-webhook.plist
         

  3. Verify the job is loaded:
         
         launchctl list | grep messagetrace
         




#### Linux

  1. Open the crontab editor:
         
         crontab -e
         

  2. Add the following line to run the script every hour:
         
         0 * * * * /usr/bin/pwsh -NoProfile -File /opt/scripts/messagetrace-webhook.ps1 >> /var/log/messagetrace/cron.log 2>&1
         

  3. Save and exit the editor.

  4. Verify the cron job is registered:
         
         crontab -l
         




### Verify log ingestion

  1. Run the script manually to test:

**Windows:**
         
         powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Scripts\messagetrace-webhook.ps1"
         

**macOS and Linux:**
         
         pwsh -NoProfile -File /opt/scripts/messagetrace-webhook.ps1
         

  2. Check the log file for errors:

**Windows:**
         
         Get-Content "C:\Logs\messagetrace-webhook.log" -Tail 10
         

**macOS and Linux:**
         
         tail -10 /var/log/messagetrace/messagetrace-webhook.log
         

  3. In Google SecOps, go to **Search** and verify that logs with `metadata.log_type = "OFFICE_365_MESSAGETRACE"` appear.




## Option 2: Google Cloud Storage V2 ingestion

Use this method when your export script writes message trace logs to a Google Cloud Storage bucket.

### Create a GCS bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `office365-messagetrace-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




### Install Google Cloud CLI

Install the Google Cloud CLI on the same machine where you set up the export environment. The `gsutil` command (included with the Google Cloud CLI) is used to upload files to the GCS bucket.

#### Windows

  1. Download the [Google Cloud CLI installer](https://docs.cloud.google.com/sdk/docs/install-sdk#windows) (`GoogleCloudSDKInstaller.exe`).
  2. Run `GoogleCloudSDKInstaller.exe`. On the **Installation Options** screen, keep the defaults selected. Click **Install**. When the installation completes, keep **Run`gcloud init`** selected, and click **Finish**.
  3. Verify the installation by opening **Command Prompt** and running:
         
         gcloud --version
         gsutil --version
         




#### macOS

  1. Open **Terminal** and run the following command:
         
         brew install google-cloud-sdk
         

  2. Verify the installation:
         
         gcloud --version
         gsutil --version
         




#### Linux (Debian/Ubuntu)

  1. Open a terminal with root or sudo privileges.
  2. Run the following commands:
         
         sudo apt-get install -y apt-transport-https ca-certificates gnupg curl
         curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
         echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee /etc/apt/sources.list.d/google-cloud-sdk.list
         sudo apt-get update
         sudo apt-get install -y google-cloud-cli
         

  3. Verify the installation:
         
         gcloud --version
         gsutil --version
         




#### Linux (RHEL/CentOS/Fedora)

  1. Open a terminal with root or sudo privileges.
  2. Create the repository file:
         
         sudo tee /etc/yum.repos.d/google-cloud-sdk.repo << 'EOF'
         [google-cloud-cli]
         name=Google Cloud CLI
         baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el9-x86_64
         enabled=1
         gpgcheck=1
         repo_gpgcheck=0
         gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
         EOF
         

  3. Install the Google Cloud CLI:
         
         sudo dnf install -y google-cloud-cli
         

  4. Verify the installation:
         
         gcloud --version
         gsutil --version
         




### Authenticate Google Cloud CLI

  1. Run the following command to authenticate:
         
         gcloud auth login
         

  2. Set the project that contains your GCS bucket:
         
         gcloud config set project <PROJECT_ID>
         

Replace `<PROJECT_ID>` with your Google Cloud project ID.




For unattended (scheduled) use, authenticate with a service account key. This service account is used by the export script to upload files to the GCS bucket. It is separate from the Google SecOps service account used to read from the bucket (configured in a later step).

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/iam-admin/serviceaccounts) and select your project.
  2. Click **Create Service Account**.
  3. In the **Service account name** field, enter a name (for example, `chronicle-gcs-export`).
  4. Click **Create and Continue**.
  5. In the **Grant this service account access to project** section, select the **Storage Object Creator** role.
  6. Click **Done**.
  7. In the service accounts list, click the service account you created.
  8. Go to the **Keys** tab.
  9. Click **Add Key > Create new key**.
  10. Select **JSON** and click **Create**.
  11. Save the downloaded JSON key file: 
     * **Windows** : `C:\Certs\gcs-service-account.json`
     * **macOS and Linux** : `/opt/certs/gcs-service-account.json`
  12. Activate the service account:
         
         gcloud auth activate-service-account --key-file=<PATH_TO_KEY_FILE>
         




### Create the GCS export script

#### Windows

  1. Create a file named `C:\Scripts\messagetrace-gcs.ps1` with the following content:
         
         # Configuration
         $certThumbprint = "<CERTIFICATE_THUMBPRINT>"
         $appId = "<APPLICATION_ID>"
         $organization = "yourdomain.onmicrosoft.com"
         $gcsBucket = "gs://office365-messagetrace-logs/messagetrace/"
         $localLogDir = "C:\Logs\MessageTrace"
         
         # Log file
         $logFile = "C:\Logs\messagetrace-gcs.log"
         if (!(Test-Path $localLogDir)) { New-Item -ItemType Directory -Path $localLogDir }
         
         try {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Starting message trace export to GCS"
         
             # Connect to Exchange Online using certificate-based authentication
             Connect-ExchangeOnline -CertificateThumbprint $certThumbprint -AppId $appId -Organization $organization -ShowBanner:$false
         
             # Retrieve message trace data for the last hour (up to 10 days available)
             $startDate = (Get-Date).AddHours(-1)
             $endDate = Get-Date
             $messages = Get-MessageTraceV2 -StartDate $startDate -EndDate $endDate -ResultSize 5000
         
             if ($messages.Count -eq 0) {
                 Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - No messages found in the time range"
                 Disconnect-ExchangeOnline -Confirm:$false
                 exit 0
             }
         
             # Convert to NDJSON (one JSON object per line)
             $ndjson = $messages | ForEach-Object { $_ | ConvertTo-Json -Compress }
             $fileName = "messagetrace_$(Get-Date -Format 'yyyyMMddHHmmss').json"
             $filePath = Join-Path $localLogDir $fileName
             $ndjson | Out-File -FilePath $filePath -Encoding UTF8
         
             # Upload to GCS
             gsutil cp $filePath $gcsBucket
         
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Uploaded $fileName with $($messages.Count) messages"
         
             # Remove local file after successful upload
             Remove-Item $filePath
         }
         catch {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Error: $_"
         }
         finally {
             Disconnect-ExchangeOnline -Confirm:$false -ErrorAction SilentlyContinue
         }
         

  2. Replace the placeholder values:

     * `<CERTIFICATE_THUMBPRINT>`: The certificate thumbprint from the authentication setup
     * `<APPLICATION_ID>`: The Azure AD application (client) ID
     * `yourdomain.onmicrosoft.com`: Your Microsoft 365 tenant domain
     * `office365-messagetrace-logs`: Your GCS bucket name



#### macOS and Linux

  1. Create a file named `/opt/scripts/messagetrace-gcs.ps1` with the following content:
         
         # Configuration
         $certFilePath = "/opt/certs/messagetrace.pfx"
         $appId = "<APPLICATION_ID>"
         $organization = "yourdomain.onmicrosoft.com"
         $gcsBucket = "gs://office365-messagetrace-logs/messagetrace/"
         $localLogDir = "/var/log/messagetrace/export"
         
         # Log file
         $logFile = "/var/log/messagetrace/messagetrace-gcs.log"
         if (!(Test-Path $localLogDir)) { New-Item -ItemType Directory -Path $localLogDir }
         
         try {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Starting message trace export to GCS"
         
             # Connect to Exchange Online using certificate-based authentication
             Connect-ExchangeOnline -CertificateFilePath $certFilePath -AppId $appId -Organization $organization -ShowBanner:$false
         
             # Retrieve message trace data for the last hour (up to 10 days available)
             $startDate = (Get-Date).AddHours(-1)
             $endDate = Get-Date
             $messages = Get-MessageTraceV2 -StartDate $startDate -EndDate $endDate -ResultSize 5000
         
             if ($messages.Count -eq 0) {
                 Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - No messages found in the time range"
                 Disconnect-ExchangeOnline -Confirm:$false
                 exit 0
             }
         
             # Convert to NDJSON (one JSON object per line)
             $ndjson = $messages | ForEach-Object { $_ | ConvertTo-Json -Compress }
             $fileName = "messagetrace_$(Get-Date -Format 'yyyyMMddHHmmss').json"
             $filePath = Join-Path $localLogDir $fileName
             $ndjson | Out-File -FilePath $filePath -Encoding UTF8
         
             # Upload to GCS
             gsutil cp $filePath $gcsBucket
         
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Uploaded $fileName with $($messages.Count) messages"
         
             # Remove local file after successful upload
             Remove-Item $filePath
         }
         catch {
             Add-Content -Path $logFile -Value "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') - Error: $_"
         }
         finally {
             Disconnect-ExchangeOnline -Confirm:$false -ErrorAction SilentlyContinue
         }
         

  2. Replace the placeholder values:

     * `<APPLICATION_ID>`: The Azure AD application (client) ID
     * `yourdomain.onmicrosoft.com`: Your Microsoft 365 tenant domain
     * `office365-messagetrace-logs`: Your GCS bucket name
  3. Set file permissions:
         
         sudo chmod 700 /opt/scripts/messagetrace-gcs.ps1
         




### Schedule the GCS export script

**Note:** The `Get-MessageTraceV2` cmdlet returns data for the last 10 days. Results are available instantly. Running the script every hour ensures continuous coverage without data gaps. For historical data from 10 to 90 days, use the [`Start-HistoricalSearch`](https://learn.microsoft.com/en-us/powershell/module/exchange/start-historicalsearch) cmdlet, which generates downloadable CSV reports (results may take several hours to prepare).

#### Windows

  1. Open **Task Scheduler** : Press `Win+R`, type `taskschd.msc`, and press `Enter`.
  2. In the right pane, click **Create Task**.
  3. On the **General** tab: 
     * **Name** : Enter `MessageTrace GCS Export`
     * Select **Run whether user is logged on or not**
     * Select **Run with highest privileges**
  4. On the **Triggers** tab: 
     1. Click **New**.
     2. Set **Begin the task** to **On a schedule**.
     3. Select **Daily** , set **Start** time to `12:00:00 AM` (midnight, so it repeats on whole hours), and set **Recur every 1 days**.
     4. Select **Repeat task every** `1 hour` for a duration of **Indefinitely**.
     5. Select **Enabled**.
     6. Click **OK**.
  5. On the **Actions** tab:

     1. Click **New**.
     2. Set **Action** to **Start a program**.
     3. In the **Program/script** field, enter:
            
            powershell.exe
            

     4. In the **Add arguments** field, enter:
            
            -NoProfile -ExecutionPolicy Bypass -File "C:\Scripts\messagetrace-gcs.ps1"
            

     5. Click **OK**.

  6. On the **Settings** tab:

     * Select **Allow task to be run on demand**
     * Clear the **Stop the task if it runs longer than** checkbox
  7. Click **OK** and enter the service account credentials when prompted.




#### macOS

  1. Create a launchd plist file at `~/Library/LaunchAgents/com.chronicle.messagetrace-gcs.plist`:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
         <plist version="1.0">
         <dict>
             <key>Label</key>
             <string>com.chronicle.messagetrace-gcs</string>
             <key>ProgramArguments</key>
             <array>
                 <string>/usr/local/bin/pwsh</string>
                 <string>-NoProfile</string>
                 <string>-File</string>
                 <string>/opt/scripts/messagetrace-gcs.ps1</string>
             </array>
             <key>StartInterval</key>
             <integer>3600</integer>
             <key>StandardOutPath</key>
             <string>/var/log/messagetrace/launchd-gcs-stdout.log</string>
             <key>StandardErrorPath</key>
             <string>/var/log/messagetrace/launchd-gcs-stderr.log</string>
             <key>RunAtLoad</key>
             <true/>
         </dict>
         </plist>
         

**Note:** If you use an Apple Silicon Mac (M1, M2, M3, M4), replace `/usr/local/bin/pwsh` with `/opt/homebrew/bin/pwsh`.
  2. Load the job:
         
         launchctl load ~/Library/LaunchAgents/com.chronicle.messagetrace-gcs.plist
         

  3. Verify the job is loaded:
         
         launchctl list | grep messagetrace
         




#### Linux

  1. Open the crontab editor:
         
         crontab -e
         

  2. Add the following line to run the script every hour:
         
         0 * * * * /usr/bin/pwsh -NoProfile -File /opt/scripts/messagetrace-gcs.ps1 >> /var/log/messagetrace/cron-gcs.log 2>&1
         

  3. Save and exit the editor.

  4. Verify the cron job is registered:
         
         crontab -l
         




### Verify the GCS upload

  1. Run the script manually to test:

**Windows:**
         
         powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Scripts\messagetrace-gcs.ps1"
         

**macOS and Linux:**
         
         pwsh -NoProfile -File /opt/scripts/messagetrace-gcs.ps1
         

  2. Verify the file was uploaded to the GCS bucket:
         
         gsutil ls gs://office365-messagetrace-logs/messagetrace/
         

  3. Check the log file for errors:

**Windows:**
         
         Get-Content "C:\Logs\messagetrace-gcs.log" -Tail 10
         

**macOS and Linux:**
         
         tail -10 /var/log/messagetrace/messagetrace-gcs.log
         




### Get a Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Office 365 Message Trace - GCS`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **Office 365 Message Trace** as the **Log type**.
  7. Click **Get Service Account**.
  8. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  9. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.



### Grant IAM permissions

  1. Go to **Cloud Storage > Buckets**.
  2. Click on your bucket name.
  3. Go to the **Permissions** tab.
  4. Click **Grant access**.
  5. Provide the following configuration details: 
     * **Add principals** : Paste the Google SecOps service account email
     * **Assign roles** : Select **Storage Object Viewer**
  6. Click **Save**.

**Note:** If you plan to use the deletion option "Delete transferred files" or "Delete transferred files and empty directories," grant **Storage Object Admin** role instead of Storage Object Viewer.



### Configure a Google SecOps feed for GCS

  1. Continue from the feed creation page (or go to **SIEM Settings > Feeds > Add New Feed**).
  2. Click **Next**.
  3. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://office365-messagetrace-logs/messagetrace/
           

**Note:** Always include the trailing slash (/) at the end of the URI.
     * **Source deletion option** : Select the deletion option according to your preference: 
       * **Never** : Never deletes any files after transfers (recommended for testing)
       * **Delete transferred files** : Deletes files after successful transfer
       * **Delete transferred files and empty directories** : Deletes files and empty directories after successful transfer
     * **Maximum File Age** : Include files modified in the last number of days (default is 180 days)
     * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces)
     * **Ingestion labels** : The label to be applied to the events from this feed
  4. Click **Next**.

  5. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.




## UDM mapping table

The following table lists the log fields of the `OFFICE_365_MESSAGETRACE` log type and their corresponding UDM fields.

Log Field | UDM Mapping | Logic  
---|---|---  
`additional_AdditionalFields` | `additional.fields` | Merged  
`additional_DeliveryLocation` | `additional.fields` | Merged  
`additional_OrgLevelPolicy` | `additional.fields` | Merged  
`additional_connectors` | `additional.fields` | Merged  
`additional_delivery_action` | `additional.fields` | Merged  
`additional_fields_UrlLocation` | `additional.fields` | Merged  
`additional_orgLevelAction` | `additional.fields` | Merged  
`end_date_label` | `additional.fields` | Merged  
`index_label` | `additional.fields` | Merged  
`metadata_id_label` | `additional.fields` | Merged  
`operationName_label` | `additional.fields` | Merged  
`start_date_label` | `additional.fields` | Merged  
`tenant_label` | `additional.fields` | Merged  
`type_label` | `additional.fields` | Merged  
`properties.AuthenticationDetails` | `extensions.auth.auth_details` | Directly mapped  
`Received` | `metadata.event_timestamp` | Parsed as `UNIX_MS`  
`time` | `metadata.event_timestamp` | Parsed as `ISO8601`  
`tenantId` | `metadata.product_deployment_id` | Directly mapped  
`category` | `metadata.product_event_type` | Directly mapped  
`MessageTraceId` | `metadata.product_log_id` | Directly mapped  
`SenderAddress` | `network.email.from` | Directly mapped  
`properties.SenderFromAddress` | `network.email.from` | Directly mapped  
`MessageId` | `network.email.mail_id` | Directly mapped  
`Subject` | `network.email.subject` | Merged  
`properties.Subject` | `network.email.subject` | Merged  
`RecipientAddress` | `network.email.to` | Merged  
`properties.RecipientEmailAddress` | `network.email.to` | Merged  
`Size` | `network.received_bytes` | Directly mapped  
`Organization` | `principal.administrative_domain` | Directly mapped  
`properties.SenderFromDomain` | `principal.administrative_domain` | Directly mapped  
`FromIP` | `principal.ip` | Merged  
`properties.FileName` | `principal.process.file.names` | Merged  
`properties.SHA256` | `principal.process.file.sha256` | Directly mapped  
`properties.FileSize` | `principal.process.file.size` | Renamed/mapped  
`additional_UserLevelAction` | `principal.user.attribute.labels` | Merged  
`additional_UserLevelPolicy` | `principal.user.attribute.labels` | Merged  
`sender_email_from_domain_label` | `principal.user.attribute.labels` | Merged  
`properties.SenderFromAddress` | `principal.user.email_addresses` | Merged  
`properties.SenderObjectId` | `principal.user.product_object_id` | Directly mapped  
`properties.SenderDisplayName` | `principal.user.user_display_name` | Directly mapped  
`action` | `security_result.action` | Merged  
`Status` | `security_result.action_details` | Directly mapped  
`security_result_category` | `security_result.category` | Merged  
`properties.ConfidenceLevel` | `security_result.confidence_details` | Directly mapped  
`detect_method` | `security_result.detection_fields` | Merged  
`detection_method` | `security_result.rule_name` | Directly mapped  
`properties.ThreatNames` | `security_result.threat_name` | Directly mapped  
`properties.UrlDomain` | `target.asset.hostname` | Directly mapped  
`ToIP` | `target.asset.ip` | Merged  
`properties.UrlDomain` | `target.hostname` | Directly mapped  
`ToIP` | `target.ip` | Merged  
`properties.Url` | `target.url` | Directly mapped  
`properties.RecipientEmailAddress` | `target.user.email_addresses` | Merged  
`properties.RecipientObjectId` | `target.user.product_object_id` | Directly mapped  
N/A | `metadata.event_type` | Constant: `EMAIL_TRANSACTION`  
N/A | `network.direction` | Constant: `INBOUND`  
N/A | `principal.process.file.file_type` | Constant: `FILE_TYPE_PNG`  
N/A | `security_result.confidence` | Constant: `HIGH_CONFIDENCE`  
`id` | `event.idm.read_only_udm.metadata.product_log_id` | Mapped from changelog  
`receivedDateTime` | `event.idm.read_only_udm.metadata.event_timestamp` | Mapped from changelog  
`fromIP` | `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` | Mapped from changelog  
`toIP` | `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` | Mapped from changelog  
`status` | `event.idm.read_only_udm.security_result.action_details` | Mapped from changelog  
`size` | `event.idm.read_only_udm.network.received_bytes` | Mapped from changelog  
`senderAddress` | `event.idm.read_only_udm.network.email.from` | Mapped from changelog  
`recipientAddress` | `event.idm.read_only_udm.network.email.to` | Mapped from changelog  
`subject` | `event.idm.read_only_udm.network.email.subject` | Mapped from changelog  
`messageId` | `event.idm.read_only_udm.network.email.mail_id` | Mapped from changelog  
`properties.SenderMailFromDomain", "properties.UserLevelAction", and "properties.UserLevelPolicy` | `principal.user.attribute.labels` | Mapped from changelog  
`properties.EmailDirection` | `network.direction` | Mapped from changelog  
`properties.DeliveryAction", "properties.DeliveryLocation", "properties.Connectors", "properties.OrgLevelAction", "properties.OrgLevelPolicy", "properties.AdditionalFields", and "properties.UrlLocation` | `additional.fields` | Mapped from changelog  
`operationName", "Tenant` | `additional.fields` | Mapped from changelog  
`properties.DetectionMethods` | `security_result.detection_fields` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/office-365-messagetrace-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
