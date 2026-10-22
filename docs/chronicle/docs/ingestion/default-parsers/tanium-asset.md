---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-asset/
title: Collect Tanium Asset logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:05.259895+00:00
---

# Collect Tanium Asset logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-asset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Tanium Asset logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to ingest Tanium Asset logs to Google Security Operations using two different methods.

You can choose between Tanium Connect's native Amazon S3 export or real-time syslog forwarding using Bindplane. Both methods use Tanium Connect module to extract asset data from Tanium and forward it to Chronicle for analysis and monitoring.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the Tanium Console (Connect module) to configure export destinations
  * Choose your preferred integration method: 
    * **Option 1 (Recommended)** : Privileged access to **AWS** (S3, IAM) for native S3 export
    * **Option 2** : A Windows 2016 or later or Linux host with `systemd` for Bindplane agent installation



## Option 1: Configure Tanium Asset logs export using AWS S3

**Note:** This export process uses Tanium Connect's native S3 integration for automated delivery.

### Create an Amazon S3 bucket

  1. Create **Amazon S3 bucket** following this user guide: [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)
  2. Save bucket **Name** and **Region** for future reference (for example, `tanium-asset-logs`).
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



### Configure Tanium Connect for S3 Export

  1. Sign in to the **Tanium Console** with administrator privileges.
  2. Go to **Modules > Connect > Overview** and click **Create Connection**.
  3. Click **Create**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Asset S3 Export`).
     * **Description** : Optional description for this connection.
     * **Enable** : Select **Enable** to run on a schedule.
  5. Click **Next**.
  6. In **Source** configuration: 
     * **Source** : Select **Saved Question**.
     * **Question** : Choose an existing saved question that returns Asset data or create a new one with Asset-related sensors (for example, Computer Name, IP Address, OS Platform, Domain).
     * **Computer Group** : Select the computer group to target for asset data collection.
  7. Click **Next**.
  8. In **Destination** configuration: 
     * **Destination** : Choose **AWS S3**.
     * **Name** : Enter a destination name (for example, `Chronicle Asset S3`).
     * **AWS Access Key ID** : Enter the Access Key ID from the IAM user.
     * **AWS Secret Access Key** : Enter the Secret Access Key from the IAM user.
     * **S3 Bucket Name** : `tanium-asset-logs`.
     * **S3 Key Prefix** : `tanium/assets/` (optional prefix for organization).
     * **Region** : Select the AWS region where your S3 bucket is located.
  9. Click **Next**.
  10. In **Formatting** configuration: 
     * **Format** : Select **JSON** for structured data export.
     * **Columns** : Select the Asset fields you want to export and format them appropriately.
  11. Click **Next**.
  12. In **Schedule** configuration: 
     * **Schedule** : Configure delivery schedule (for example, every hour or daily).
     * **Start Date/Time** : Set when the connection should start running.
  13. Click **Save** to create the connection and start automated S3 export.



### (Optional) Create read-only IAM user & keys for Google SecOps

  1. Go to **AWS Console > IAM > Users > Add users**.
  2. Click **Add users**.
  3. Provide the following configuration details: 
     * **User** : Enter `secops-reader`.
     * **Access type** : Select **Access key — Programmatic access**.
  4. Click **Create user**.
  5. Attach minimal read policy (custom): **Users > secops-reader > Permissions > Add permissions > Attach policies directly > Create policy**.
  6. JSON:
         
         {
           "Version": "2012-10-17",
           "Statement": [
             {
               "Effect": "Allow",
               "Action": ["s3:GetObject"],
               "Resource": "arn:aws:s3:::tanium-asset-logs/*"
             },
             {
               "Effect": "Allow",
               "Action": ["s3:ListBucket"],
               "Resource": "arn:aws:s3:::tanium-asset-logs"
             }
           ]
         }
         

  7. Name = `secops-reader-policy`.

  8. Click **Create policy > search/select > Next > Add permissions**.

  9. Create access key for `secops-reader`: **Security credentials > Access keys > Create access key > download the `.csv` (you will paste these values into the feed)**.




### Configure a feed in Google SecOps to ingest Tanium Asset logs

  1. Go to **SIEM Settings > Feeds**.
  2. Click **\+ Add New Feed**.
  3. In the **Feed name** field, enter a name for the feed (for example, `Tanium Asset logs`).
  4. Select **Amazon S3 V2** as the **Source type**.
  5. Select **Tanium Asset** as the **Log type**.
  6. Click **Next**.
  7. Specify values for the following input parameters: 
     * **S3 URI** : `s3://tanium-asset-logs/tanium/assets/`
     * **Source deletion options** : Select deletion option according to your preference.
     * **Maximum File Age** : Include files modified in the last number of days. Default is 180 days.
     * **Access Key ID** : User access key with access to the S3 bucket.
     * **Secret Access Key** : User secret key with access to the S3 bucket.
     * **Asset namespace** : the [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion labels** : the label applied to the events from this feed.
  8. Click **Next**.
  9. Review your new feed configuration in the **Finalize** screen, and then click **Submit**.



## Option 2: Configure Tanium Asset logs export using syslog and Bindlane

### Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



#### Option 1: Create a service account for the Chronicle API (recommended)

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

#### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

### Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



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
         




#### Additional installation resources

For additional installation options, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

### Configure the Bindplane agent to ingest Syslog and send to Google SecOps

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
             protocol: https
             # Region of your instance, for example us, europe, asia-southeast1
             location: <LOCATION>
             # Project number of the Google Cloud project linked to the instance
             project: '<PROJECT_NUMBER>'
             compression: gzip
             # Adjust the path to the credentials file you downloaded in Step 1
             creds_file_path: '/path/to/ingestion-authentication-file.json'
             # Replace with your actual customer ID from Step 2
             customer_id: <PLACEHOLDER_CUSTOMER_ID>
             endpoint: chronicle.googleapis.com
             # Add optional ingestion labels for better organization
             log_type: 'TANIUM_ASSET'
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
     * Replace `<PLACEHOLDER_CUSTOMER_ID>` with the actual Customer ID.
     * Update `/path/to/ingestion-authentication-file.json` to the file path where the service account key file (Option 1) was saved in Step 1.



#### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/chronicle_w_labels:
            compression: gzip
            # Adjust the path to the credentials file you downloaded in Step 1
            creds_file_path: '/path/to/ingestion-authentication-file.json'
            # Replace with your actual customer ID from Step 2
            customer_id: <PLACEHOLDER_CUSTOMER_ID>
            endpoint: malachiteingestion-pa.googleapis.com
            # Add optional ingestion labels for better organization
            log_type: 'TANIUM_ASSET'
            raw_log_field: body
            ingestion_labels:
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Restart the Bindplane agent to apply the changes

  * To restart the Bindplane agent in Linux, run the following command:
        
        sudo systemctl restart observiq-otel-collector
        

  * To restart the Bindplane agent in Windows, you can either use the **Services** console or enter the following command:
        
        net stop observiq-otel-collector && net start observiq-otel-collector
        




### Configure Syslog forwarding on Tanium Asset

  1. Sign in to the **Tanium Console** with administrator privileges.
  2. Go to **Modules > Connect > Overview** and click **Create Connection**.
  3. Click **Create**.
  4. Provide the following configuration details: 
     * **Name** : Enter a descriptive name (for example, `Google SecOps Asset Integration`).
     * **Description** : Optional description for this connection.
     * **Enable** : Select **Enable** to run on a schedule.
  5. Click **Next**.
  6. In **Source** configuration: 
     * **Source** : Select **Saved Question**.
     * **Question** : Choose an existing saved question that returns Asset data or create a new one with Asset-related sensors.
     * **Computer Group** : Select the computer group to target for asset data collection.
  7. Click **Next**.
  8. In **Destination** configuration: 
     * **Destination** : Choose **SIEM/Syslog**.
     * **Name** : Enter a destination name (for example, `Chronicle Asset Syslog`).
     * **Host** : Enter the Bindplane IP.
     * **Port** : Enter the Bindplane port number (for example, `514`).
     * **Protocol** : Select **UDP**.
     * **Format** : Select **SYSLOG RFC 5424**.
     * **Timezone** : Select **UTC** timezone for universal consistency across systems.
  9. Click **Next**.
  10. In **Formatting** configuration: 
     * **Format** : Select **JSON**.
     * **Columns** : Select the Asset fields you want to forward (for example, Computer Name, IP Address, OS Platform, Domain).
  11. Click **Next**.
  12. In **Schedule** configuration: 
     * **Schedule** : Configure delivery schedule (for example, every hour).
     * **Start Date/Time** : Set when the connection should start running.
  13. Click **Save** to create the connection and start forwarding.



## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`application_name` | `entity.metadata.source_labels.value` | Value is taken from the "application_name" field if it exists in the raw log.  
`application_vendor` | `entity.metadata.source_labels.value` | Value is taken from the "application_vendor" field if it exists in the raw log.  
`application_version` | `entity.metadata.product_version` | Value is taken from the "application_version" field if it exists in the raw log.  
`BIOS_Current_Language` | `entity.metadata.source_labels.value` | Value is taken from the "BIOS_Current_Language" field if it exists in the raw log.  
`BIOS_Release_Date` | `entity.metadata.source_labels.value` | Value is taken from the "BIOS_Release_Date" field if it exists in the raw log.  
`BIOS_Vendor` | `entity.metadata.source_labels.value` | Value is taken from the "BIOS_Vendor" field if it exists in the raw log.  
`BIOS_Version` | `entity.metadata.product_version` | Value is taken from the "BIOS_Version" field if it exists in the raw log.  
`Chassis Type` | `entity.entity.asset.category` | Value is taken from the "Chassis Type" field if it exists in the raw log.  
`Computer ID` | `entity.entity.asset.product_object_id` | Value is taken from the "Computer ID" field if it exists in the raw log. Also used to populate entity.relations.entity.asset.asset_id with the prefix "id: ".  
`Computer Name` | `entity.entity.asset.hostname` | Value is taken from the "Computer Name" field if it exists in the raw log.  
`Count` | `entity.metadata.source_labels.value` | Value is taken from the "Count" field if it exists in the raw log.  
`Endpoint Fingerprint` | `entity.entity.asset.hardware.serial_number` | Value is taken from the "Endpoint Fingerprint" field if it exists in the raw log.  
`IP Address` | `entity.entity.asset.ip` | Values are taken from the "IP Address" field and added as separate IP addresses to the array.  
`Last Logged In User` | `entity.relations.entity.user.userid` | Value is taken from the "Last Logged In User" field, with any domain prefix removed, if it exists in the raw log.  
`Last Reboot` | `entity.entity.asset.last_boot_time` | Value is parsed from the "Last Reboot" field and formatted as a timestamp if it exists in the raw log.  
`MAC Address` | `entity.entity.asset.mac` | Values are taken from the "MAC Address" field and added as separate MAC addresses to the array.  
`Manufacturer` | `entity.entity.asset.hardware.manufacturer` | Value is taken from the "Manufacturer" field if it exists in the raw log.  
`Operating System` | `entity.entity.asset.platform_software.platform_version` | Value is taken from the "Operating System" field if it exists in the raw log. Used to determine the value of entity.entity.asset.platform_software.platform (WINDOWS, LINUX, or MAC).  
`platform` | `entity.entity.asset.platform_software.platform_version` | Value is taken from the "platform" field if it exists in the raw log. Used to determine the value of entity.entity.asset.platform_software.platform (WINDOWS, LINUX, or MAC).  
`serial_number` | `entity.entity.asset.hardware.serial_number` | Value is taken from the "serial_number" field if it exists in the raw log.  
`version` | `entity.entity.asset.platform_software.platform_version` | Value is taken from the "version" field if it exists in the raw log. Used to determine the value of entity.entity.asset.platform_software.platform (WINDOWS, LINUX, or MAC).  
N/A | `entity.metadata.collected_timestamp` | Set to the create_time of the batch.  
N/A | `entity.metadata.vendor_name` | Always set to "TANIUM_ASSET".  
N/A | `entity.metadata.product_name` | Always set to "TANIUM_ASSET".  
N/A | `entity.metadata.entity_type` | Always set to "ASSET".  
N/A | `entity.relations.entity_type` | Always set to "USER".  
N/A | `entity.relations.relationship` | Always set to "OWNS".  
`comp_serial_num` | `_asset_entity.asset.product_object_id` | Mapped from changelog  
`application_name", "count", "application_vendor", "BIOS_Release_Date", "BIOS_Vendor", and "BIOS_Current_Language` | `metadata.source_labels` | Mapped from changelog  
`application_version" and "BIOS_Version` | `metadata.product_version` | Mapped from changelog  
`computer_id` | `entity.asset.asset_id` | Mapped from changelog  
`comp_serial_num` | `hardware.serial_number` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-asset-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
