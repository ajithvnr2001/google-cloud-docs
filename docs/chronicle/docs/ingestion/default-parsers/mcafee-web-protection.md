---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-protection/
title: Collect Skyhigh Secure Web Gateway (On-Premises) logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:01.744917+00:00
---

# Collect Skyhigh Secure Web Gateway (On-Premises) logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mcafee-web-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Skyhigh Secure Web Gateway (On-Premises) logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest Skyhigh Secure Web Gateway (On-Premises) logs to Google SecOps using Google Cloud Storage.

Skyhigh Secure Web Gateway (formerly McAfee Web Gateway) is an on-premises web security solution that provides malware detection, URL filtering, application control, data loss prevention, and HTTPS inspection to protect organizations from web-based threats and enforce acceptable use policies.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance
  * Privileged access to the **Skyhigh Secure Web Gateway** management console
  * A GCP project with Cloud Storage API enabled
  * A Linux-based collection server with network access to the Skyhigh Secure Web Gateway appliance and outbound access to Google Cloud Storage
  * Skyhigh Secure Web Gateway version 7.x or later



## Configure Skyhigh Secure Web Gateway access log format

Configure the Log Handler rule set to generate access log entries in JSON format.

  1. Sign in to the **Skyhigh Secure Web Gateway** management console.
  2. Go to **Policy > Rule Sets**.
  3. Click **Log Handler** in the left navigation.
  4. Expand the **Default** rule set.
  5. Select the nested **Access Log** rule set.
  6. Click **Add > Rule** to create a new rule.
  7. Configure the rule with the following settings: 
     * **Name** : Enter `Write access log data for collection`
     * **Criteria** : Select **Always**
     * **Action** : Select **Continue**
     * **Event** : Click **Add > Event**
  8. In the Add Event dialog: 
     1. Select **Set User-Defined.logLine**.
     2. Click **Parameters**.
     3. Build the log line value by combining the required properties. Use the **User-Defined.logLine** property to concatenate the fields into the desired format.
     4. Click **OK**.
  9. Add a second event to write the log line to the access log file: 
     1. Click **Add > Event**.
     2. Select **File System Logging**.
     3. Click **Parameters**.
     4. For the **message** parameter, select **User-Defined.logLine**.
     5. Click **OK**.
  10. Click **Finish** to save the rule.
  11. Click **Save Changes** at the top of the page.

**Note:** For additional details on configuring custom log formats, refer to the [Skyhigh Secure Web Gateway logging best practices](https://success.skyhighsecurity.com/Skyhigh_Secure_Web_Gateway_\(On-Prem\)/Secure_Web_Gateway_Product_Guide/Best_Practices/Logging_and_Monitoring/Understand_Customized_Logging_and_Log_File_Management).



## Configure File System Logging auto-push

Configure the Skyhigh Secure Web Gateway to automatically push access log files to the collection server.

  1. In the Skyhigh Secure Web Gateway console, go to **Policy > Settings > Engines > File System Logging**.
  2. Select the **Access Log Configuration** settings.
  3. Expand **Settings for Rotation, Pushing, and Deletion**.
  4. In the **Auto Pushing** section: 
     1. Select the **Enable auto pushing** checkbox.
     2. In the **Destination** field, enter the FTP or HTTP URL of the collection server: 
        * FTP example: `ftp://COLLECTION_SERVER_IP:21/swg-logs/`
        * HTTP example: `http://COLLECTION_SERVER_IP:9111/logloader/`
     3. In the **User name** field, enter the username for the collection server.
     4. In the **Password** field, enter the password for the collection server.
  5. In the **Rotation** section, configure the rotation interval based on your log volume: 
     * For high-volume environments, set rotation to every 5-15 minutes
     * For standard environments, set rotation to every 30-60 minutes
  6. Click **Save Changes**.

**Note:** Do not configure log pushing from **Configuration > Log File Manager**, as this sends unwanted system logs. Always configure pushing from **Policy > Settings > Engines > File System Logging**.



## Verify the log prefix

  1. In the Skyhigh Secure Web Gateway console, go to **Configuration > Appliances > Syslog > Log Prefix**.
  2. Verify that the prefix is set to **mwg**.
  3. If the prefix is different, change it to **mwg** and click **Save Changes**.

**Note:** The `mwg` prefix is required for proper log identification by the Google SecOps parser.



## Create Google Cloud Storage bucket

  1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
  2. Select your project or create a new one.
  3. In the navigation menu, go to **Cloud Storage > Buckets**.
  4. Click **Create bucket**.
  5. Provide the following configuration details:

Setting | Value  
---|---  
**Name your bucket** | Enter a globally unique name (for example, `skyhigh-swg-logs`)  
**Location type** | Choose based on your needs (Region, Dual-region, Multi-region)  
**Location** | Select the location (for example, `us-central1`)  
**Storage class** | Standard (recommended for frequently accessed logs)  
**Access control** | Uniform (recommended)  
**Protection tools** | Optional: Enable object versioning or retention policy  
  6. Click **Create**.




## Configure the collection server to upload logs to GCS

Set up a collection server to receive the log files pushed by the Skyhigh Secure Web Gateway and upload them to the GCS bucket.

### Install the gcloud CLI

  1. On the collection server, install the gcloud CLI:
         
         curl https://sdk.cloud.google.com | bash
         exec -l $SHELL
         

  2. Initialize the gcloud CLI:
         
         gcloud init
         

  3. Authenticate with a service account or user account:
         
         gcloud auth login
         

  4. Set the default project:
         
         gcloud config set project PROJECT_ID
         

**Note:** Replace `PROJECT_ID` with your GCP project ID.



### Configure an FTP server to receive pushed logs

  1. Install an FTP server on the collection server (for example, vsftpd):
         
         sudo apt-get install vsftpd -y
         

  2. Create a dedicated directory for the pushed log files:
         
         sudo mkdir -p /var/log/swg-logs
         sudo chown ftp:ftp /var/log/swg-logs
         

  3. Configure the FTP server to allow write access to the log directory.

  4. Start the FTP service:
         
         sudo systemctl enable vsftpd
         sudo systemctl start vsftpd
         




### Create the GCS upload script

  1. Create the upload script:
         
         sudo mkdir -p /opt/swg-gcs-uploader
         

  2. Create the file `/opt/swg-gcs-uploader/upload_to_gcs.sh` with the following content:
         
         #!/bin/bash
         LOG_DIR="/var/log/swg-logs"
         GCS_BUCKET="gs://skyhigh-swg-logs/swg-access-logs/"
         ARCHIVE_DIR="/var/log/swg-logs/archived"
         
         mkdir -p "$ARCHIVE_DIR"
         
         # Upload new log files to GCS
         for log_file in "$LOG_DIR"/*.log; do
             if [ -f "$log_file" ]; then
                 gsutil cp "$log_file" "$GCS_BUCKET"
                 if [ $? -eq 0 ]; then
                     mv "$log_file" "$ARCHIVE_DIR/"
                     echo "$(date): Uploaded and archived $(basename "$log_file")"
                 else
                     echo "$(date): Failed to upload $(basename "$log_file")"
                 fi
             fi
         done
         
         # Clean up archived files older than 7 days
         find "$ARCHIVE_DIR" -type f -mtime +7 -delete
         

  3. Make the script executable:
         
         sudo chmod +x /opt/swg-gcs-uploader/upload_to_gcs.sh
         

  4. Replace `skyhigh-swg-logs` with the actual name of the GCS bucket.




### Schedule the upload script

  1. Open the crontab editor:
         
         sudo crontab -e
         

  2. Add the following entry to run the upload every 10 minutes:
         
         */10 * * * * /opt/swg-gcs-uploader/upload_to_gcs.sh >> /var/log/swg-gcs-uploader.log 2>&1
         

  3. Save and exit.




### Verify the upload

  1. Wait for the Skyhigh Secure Web Gateway to push a log file to the collection server.
  2. Verify the log file is present in the log directory:
         
         ls -la /var/log/swg-logs/
         

  3. Run the upload script manually to test:
         
         sudo /opt/swg-gcs-uploader/upload_to_gcs.sh
         

  4. Verify the file was uploaded to GCS:
         
         gsutil ls gs://skyhigh-swg-logs/swg-access-logs/
         




## Apply configuration to Central Management cluster

If you are running multiple Skyhigh Secure Web Gateway appliances in a Central Management cluster:

  1. Repeat the File System Logging auto-push configuration on every appliance in the cluster.
  2. The Log Handler rule set configuration is synchronized automatically across the cluster.

**Note:** Each appliance must have its own File System Logging settings configured individually.



## Retrieve the Google SecOps service account

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click **Configure a single feed**.
  4. In the **Feed name** field, enter a name for the feed (for example, `Skyhigh SWG Logs`).
  5. Select **Google Cloud Storage V2** as the **Source type**.
  6. Select **McAfee Web Protection** as the **Log type**.
  7. Click **Get Service Account**. A unique service account email will be displayed, for example:
         
         chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
         

  8. Copy this email address for use in the next step.

**Note:** Each Google SecOps instance has a unique service account. Don't use service accounts from other documentation or examples.
  9. Click **Next**.

  10. Specify values for the following input parameters:

     * **Storage bucket URL** : Enter the GCS bucket URI with the prefix path:
           
           gs://skyhigh-swg-logs/swg-access-logs/
           

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

  1. Go to **Cloud Storage > Buckets**.
  2. Click on `skyhigh-swg-logs`.
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
mediaType | additional.fields | Merged with labels from mediaType, reputation, Ssl_scanned, av_scanned_up, av_scanned_down, rbi, dlp  
reputation | additional.fields |   
Ssl_scanned | additional.fields |   
av_scanned_up | additional.fields |   
av_scanned_down | additional.fields |   
rbi | additional.fields |   
dlp | additional.fields |   
intermediary_ip1 | intermediary.ip | Merged from intermediary_ip1, intermediary_ip2, client_ip  
intermediary_ip2 | intermediary.ip |   
client_ip | intermediary.ip |   
intermediary_port | intermediary.port | Converted to integer  
uriScheme | metadata.event_type | Set to "GENERIC_EVENT", overridden to "NETWORK_HTTP" if uriScheme in ["http", "https"]  
uriScheme | network.application_protocol | Set to "HTTPS" if uriScheme matches "https", "HTTP" if matches "http"  
http_action | network.http.method | Value copied directly  
user_agent_comment | network.http.parsed_user_agent | Converted to parsed user agent  
httpStatusCode | network.http.response_code | Converted to integer  
user_agent_comment | network.http.user_agent | Value copied directly  
serverToClientBytes | network.received_bytes | Converted to uinteger  
clientToServerBytes | network.sent_bytes | Converted to uinteger  
Filename | principal.file.full_path | Value copied directly  
source_ip | principal.ip | Value copied directly  
country | principal.location.country_or_region | Value copied directly  
process_name | principal.process.command_line | Value copied directly  
Ssl_client_prot | principal.resource.attribute.labels | Merged with labels from Ssl_client_prot, Ssl_server_prot  
Ssl_server_prot | principal.resource.attribute.labels |   
url | principal.url | Value copied directly  
username | principal.user.userid | Value copied directly  
blockReason | security_result.action | Set to "ALLOW", overridden to "BLOCK" if blockReason not empty  
result | security_result.action_details | Value copied directly  
category | security_result.category_details | Value copied directly  
virus | security_result.detection_fields | Merged with labels from virus, Location, lastRule, applicationType, Mw_probablility, Discarded_host, domain_fronting_url  
Location | security_result.detection_fields |   
lastRule | security_result.detection_fields |   
applicationType | security_result.detection_fields |   
Mw_probablility | security_result.detection_fields |   
Discarded_host | security_result.detection_fields |   
domain_fronting_url | security_result.detection_fields |   
blockReason | security_result.summary | Value copied directly  
requested_path | target.file.full_path | Value copied directly  
requested_host | target.hostname | Value copied directly  
destination_ip | target.ip | Value copied directly  
userID | target.user.userid | Value copied directly  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-web-protection-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
