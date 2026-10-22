---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-email-dlp/
title: Collect Zscaler Email DLP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:56.197298+00:00
---

# Collect Zscaler Email DLP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-email-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zscaler Email DLP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how you can export Zscaler Email DLP logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.

For more information, see [Data ingestion to Google SecOps overview](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of Zscaler Email DLP and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.

The deployment contains the following components:

  * **Zscaler Email DLP** : The platform from which you collect logs.

  * **Google SecOps feed** : The Google SecOps feed that fetches logs from Zscaler Email DLP and writes logs to Google SecOps.

  * **Google SecOps** : Retains and analyzes the logs.




An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `ZSCALER_EMAIL_DLP` ingestion label.

## Before you begin

Ensure you have the following prerequisites:

  * Access to Zscaler Internet Access console. For more information, see [Secure Internet and SaaS Access ZIA Help](https://help.zscaler.com/zia/getting-started).
  * Zscaler Email DLP 2026 or later
  * All systems in the deployment architecture are configured with the UTC time zone.
  * The API key which is needed to complete feed setup in Google Security Operations. For more information, see [Setting up API keys](https://support.google.com/googleapi/answer/6158862).



## Set up feeds

There are two different entry points to set up feeds in the Google SecOps platform: 

  * **SIEM Settings > Feeds**
  * **Content Hub > Content Packs**

**Note:** The Content Hub is not available on the SIEM standalone platform. To upgrade, contact your Google SecOps representative.

## Set up feeds from SIEM Settings > Feeds

To configure multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

To configure a single feed, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. On the next page, click **Configure a single feed**. 
  4. In the **Feed name** field, enter a name for the feed; for example, **Zscaler Email DLP Logs**.
  5. Select **Webhook** as the **Source Type**.
  6. Select **Zscaler Email DLP** as the **Log Type**.
  7. Click **Next**.
  8. Optional: Enter values for the following input parameters: 
     1. **Split delimiter** : The delimiter that is used to separate the logs lines. Leave blank if a delimiter is not used.
     2. **Asset namespace** : The asset namespace.
     3. **Ingestion labels** : The label to be applied to the events from this feed.
  9. Click **Next**.
  10. Review your new feed configuration, and then click **Submit**.
  11. Click **Generate Secret Key** to generate a secret key to authenticate this feed.



## Set up feeds from the Content Hub

Specify values for the following fields:

  * **Split delimiter** : The delimiter that is used to separate log lines, such as `\n`.



**Advanced options**

  * **Feed Name** : A prepopulated value that identifies the feed.
  * **Source Type** : Method used to collect logs into Google SecOps.
  * **Asset namespace** : The [asset namespace](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
  * **Ingestion labels** : The label applied to the events from this feed.
  * Click **Next**.
  * Review the feed configuration in the **Finalize** screen, and then click **Submit**.
  * Click **Generate Secret Key** to generate a secret key to authenticate this feed.



## Set up Zscaler Email DLP

  1. In the Zscaler Internet Access console, click **Administration > Nanolog Streaming Service > Cloud NSS Feeds** and then click **Add Cloud NSS Feed**.
  2. The **Add Cloud NSS Feed** window appears. In the **Add Cloud NSS Feed** window, enter the details.
  3. Enter a name for the feed in the **Feed Name** field.
  4. Select **NSS for Web** in **NSS Type**.
  5. Select the status from the **Status** list to activate or deactivate the NSS feed.
  6. Keep the value in the **SIEM Rate** drop-down as **Unlimited**. To suppress the output stream due to licensing or other constraints, change the value.
  7. Select **Other** in the **SIEM Type** list.
  8. Select **Disabled** in the **OAuth 2.0 Authentication** list.
  9. Enter a size limit for an individual HTTP request payload in **Max Batch Size**. Configure this value to **512 KB** , as this is the recommended best practice for optimal SIEM ingestion. (Note: Lower batch sizes can sometimes reduce latency at the cost of more frequent HTTP requests).
  10. Enter the HTTPS URL of the Chronicle API endpoint in the API URL in the following format:
         
         https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
         

     * `CHRONICLE_REGION`: Region where your Chronicle instance is hosted. For example, US.
     * `GOOGLE_PROJECT_NUMBER`: Google Cloud project number.
     * `LOCATION`: Chronicle region. For example, US.
     * `CUSTOMER_ID`: Chronicle customer ID.
     * `FEED_ID`: Feed ID shown on Feed UI on the new webhook created
     * Sample API URL:
    
    https://us-chronicle.googleapis.com/v1alpha/projects/12345678910/locations/US/instances/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/feeds/yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy:importPushLogs
    

  11. Click **Add HTTP Header** , and then add HTTP headers in the following format:

     * `Header 1`: **Key1:** `X-goog-api-key` and **Value1:** API Key generated on Google Cloud's API Credentials.
     * `Header 2`: **Key2:** `X-Webhook-Access-Key` and **Value2:** API secret key generated on webhook's "SECRET KEY".
  12. Select **Email DLP** in the **Log Types** list.

  13. Select **JSON** in the **Feed Output Type** list.

  14. Disable **JSON Array Notation**.

  15. Set **Feed Escape Character** to `, \ "`.

  16. To add a new field to the **Feed Output Format,** select **Custom** in the **Feed Output Type** list.

  17. Copy-paste the **Feed Output Format** and add new fields. Ensure the key names match the actual field names.

  18. Following is the default **Feed Output Format** :
         
         \{"sourcetype": "zscalernss-emaildlp", "event": \{"mailsenttime": "%s{mail_sent_time}", "scantime": "%u{scan_time}", "recordid": "%llu{recordid}", "company": "%s{company}", "tenant": "%s{tenant}", "user": "%s{username}", "dept": "%s{departmentname}", "filenames": "%s{ac_names}", "filemd5s": "%s{ac_md5s}", "doctypes": "%s{ac_doctypes}", "filesizes": "%s{ac_sizes}", "filetypes": "%s{ac_filetypes}", "dlpdictnames": "%s{dlpdictnames}", "dlpdictcnts": "%s{dlpdictcnts}", "dlpengnames": "%s{dlpengnames}", "dlpidentifier": "%llu{dlpidentifier}", "triggeredrcpts": "%s{trigg_rcpts}", "severity": "%s{severity}", "action": "%s{action}", "rulename": "%s{rulelabels}", "otherrcpts": "%s{other_rcpts}", "subject": "%s{subject}", "msgid": "%s{msgid}"\}\}
         

  19. Select the timezone for the **Time** field in the output file in the **Timezone** list. By default, the timezone is set to your organization's time zone.

  20. Review the configured settings. 

  21. Click **Save** to test connectivity. If the connection is successful, a green tick accompanied by the message **Test Connectivity Successful: OK (200)** appears.




For more information about Google SecOps feeds, see [Google SecOps feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

## Supported Zscaler Email DLP log formats

The Zscaler Email DLP parser supports logs in JSON format.

## Supported Zscaler Email DLP Sample Logs

  * JSON
        
        {
            "sourcetype": "zscalernss-emaildlp",
            "event": {
                "mailsenttime": "Wed Feb 4 04:11:09 2026",
                "scantime": "25",
                "recordid": "7602857773514883073",
                "company": "Sample Company",
                "tenant": "sample.com",
                "user": "dummyuser@sample.com",
                "dept": "Default Department",
                "filenames": "test.xlsx",
                "filemd5s": "0d67b8287a735240724384f293ee364f",
                "doctypes": "None",
                "filesizes": "8824",
                "filetypes": "xlsx",
                "dlpdictnames": "Credit Cards: Detect leakage of credit card information",
                "dlpdictcnts": "10",
                "dlpengnames": "",
                "dlpidentifier": "7602857773514883076",
                "triggeredrcpts": "test2@sample.com",
                "severity": "High Severity",
                "action": "Block",
                "rulename": "DLP_Rule_7",
                "otherrcpts": "None",
                "subject": "Test Subject",
                "msgid": "863fcac3-4040-495f-9ec6-b41abd054ca7@sample.com"
            }
        }
        
        




## Field mapping reference

The following table lists common fields of the `ZSCALER_EMAIL_DLP` log type and their corresponding UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`sourcetype` | `additional.fields[sourcetype]` |   
`` | `metadata.event_type` | The `metadata.event_type` UDM field is set to `EMAIL_TRANSACTION`, provided `principal` and `metadata` objects are populated.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Zscaler`.  
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `Email DLP`.  
`time` | `metadata.collected_timestamp` |   
`ss` | `additional.fields[ss]` |   
`mm` | `additional.fields[mm]` |   
`hh` | `additional.fields[hh]` |   
`day` | `additional.fields[day]` |   
`dd` | `additional.fields[dd]` |   
`mon` | `additional.fields[mon]` |   
`mth` | `additional.fields[mth]` |   
`yyyy` | `additional.fields[yyyy]` |   
`rtime` | `additional.fields[rtime]` |   
`rss` | `additional.fields[rss]` |   
`rmm` | `additional.fields[rmm]` |   
`rhh` | `additional.fields[rhh]` |   
`rday` | `additional.fields[rday]` |   
`rdd` | `additional.fields[rdd]` |   
`rmon` | `additional.fields[rmon]` |   
`rmth` | `additional.fields[rmth]` |   
`ryyyy` | `additional.fields[ryyyy]` |   
`tz` | `additional.fields[tz]` |   
`datacenter` | `intermediary.location.name` |   
`datacentercity` | `intermediary.location.city` |   
`datacentercountry` | `intermediary.location.country_or_region` |   
`company` | `principal.user.company_name` |   
`dept` | `principal.user.department` |   
`owner` | `principal.user.email_addresses` |  If the `owner` log field value is not empty and matches the regular expression pattern `(^.@.$)` and `(^.{0,255}$)`, then the `owner` log field is mapped to the `principal.user.email_addresses` UDM field.   
`sender` | `principal.user.email_addresses` |  If the `sender` log field value is not empty and matches the regular expression pattern `(^.@.$)` and `(^.{0,255}$)`, then the `sender` log field is mapped to the `principal.user.email_addresses` UDM field.   
`user` | `principal.user.email_addresses` |  If the `user` log field value is not empty and matches the regular expression pattern `(^.@.$)` and `(^.{0,255}$)`, then the `user` log field is mapped to the `principal.user.email_addresses` UDM field.   
`extusername` | `principal.user.email_addresses` |  If the `extusername` log field value is not empty and matches the regular expression pattern `(^.@.$)` and `(^.{0,255}$)`, then the `extusername` log field is mapped to the `principal.user.email_addresses` UDM field.   
`owner` | `principal.user.userid` |  If the `owner` log field value is _not_ empty and 

  * If the `owner` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the `EMAILLOCALPART` is extracted from the `owner` log field using the Grok pattern, and the `EMAILLOCALPART` log field is mapped to the `principal.user.userid` UDM field.
  * Else, `owner` log field is mapped to the `principal.user.userid` UDM field.

  
  
Else, if the `sender` log field value is _not_ empty and 

  * If the `sender` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the `EMAILLOCALPART` is extracted from the `sender` log field using the Grok pattern, and the `EMAILLOCALPART` log field is mapped to the `principal.user.userid` UDM field.
  * Else, `sender` log field is mapped to the `principal.user.userid` UDM field.

  
  
Else, if the `user` log field value is _not_ empty and 

  * If the `user` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the `EMAILLOCALPART` is extracted from the `user` log field using the Grok pattern, and the `EMAILLOCALPART` log field is mapped to the `principal.user.userid` UDM field.
  * Else, `user` log field is mapped to the `principal.user.userid` UDM field.

  
  
Else, if the `extusername` log field value is _not_ empty and 

  * If the `extusername` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the `EMAILLOCALPART` is extracted from the `extusername` log field using the Grok pattern, and the `EMAILLOCALPART` log field is mapped to the `principal.user.userid` UDM field.
  * Else, `extusername` log field is mapped to the `principal.user.userid` UDM field.

  
`owner` | `network.email.from` |  If the `owner` log field value is _not_ empty and the `owner` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)` then, `owner` log field is mapped to the `network.email.from` UDM field.  
  
Else, if the `sender` log field value is _not_ empty and the `sender` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)` then, `sender` log field is mapped to the `network.email.from` UDM field.  
  
Else, if the `user` log field value is _not_ empty and the `user` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)` then, `user` log field is mapped to the `network.email.from` UDM field.  
  
Else, if the `extusername` log field value is _not_ empty and the `extusername` log field value matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)` then, `extusername` log field is mapped to the `network.email.from` UDM field.  
  
  
`mailsenttime` | `metadata.event_timestamp` |   
`zs_rcv_time` | `additional.fields[zs_rcv_time]` |   
`zs_sent_time` | `additional.fields[zs_sent_time]` |   
`epochmail_sent_time` | `additional.fields[epochmail_sent_time]` |   
`tenant` | `principal.administrative_domain` |   
`appname` | `principal.application` |   
`msgid` | `network.email.mail_id` |   
`subject` | `network.email.subject` |   
`filemd5s` | `security_result.about.file.md5 ` |  Attachment MD5 hashes separated by pipe delimiters (`|`) are extracted from the `filemd5s` log field, then each extracted MD5 hash is mapped to the `security_result.about.file.md5` UDM field.   
`filesizes` | `security_result.about.file.size` |  Email attachment sizes separated by pipe delimiters (`|`) are extracted from the `filesizes` log field, then each extracted email attachment size is mapped to the `security_result.about.file.size` UDM field.   
`filetypes` | `security_result.about.file.file_type` |  Email attachment filetypes separated by pipe delimiters (`|`) are extracted from the `filetypes` log field, and 

  * If the extracted email attachment file type matches the regular expression `(?i)(xlsx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_XLSX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(xls)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_XLS`
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(cab)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CAB`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pcapng|pcap|cap)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CAP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(tar.gz|egg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PYTHON_PKG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(gzip|tgz|gz)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_GZIP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(zip)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ZIP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(gif)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_GIF`. 
  * Else, if the log message matches the regular expression `(?i)(\\bdos\\b)` AND the `filetype` log field value matches the regular expression `(?i)(exe|com)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DOS_EXE`. 
  * Else, if the log message matches the regular expression `(?i)(\\bne_exe\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(exe)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_NE_EXE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(exe)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PE_EXE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(msi)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MSI`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ocx|sys)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PE_DLL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pdf|(portable\\s*document\\s*format))`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PDF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(docx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DOCX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(doc)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DOC`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(html|htm)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_HTML`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(jar)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JAR`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(jpeg|jpg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JPEG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(mov)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MOV`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(mp3)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MP3`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(mp4)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MP4`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(png)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PNG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pptx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PPTX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ppt)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PPT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rar)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_RAR`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ace)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ACE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(apk|aar|dex)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ANDROID`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(plist)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_APPLE_PLIST`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(applescript)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_APPLESCRIPT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(app)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_APPLE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(scpt)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_APPLESCRIPT_COMPILED`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(arc)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ARC`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(arj)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ARJ`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(asd)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ASD`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(asf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ASF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(avi)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_AVI`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(awk)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_AWK`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(bmp)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_BMP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dib)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DIB`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(bz2)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_BZIP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(chm)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CHM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(cljc|cljs|clj)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CLJ`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(crt|cer)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CRT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(crx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CRX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(csv)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CSV`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(deb)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DEB`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dmg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DMG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(divx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DIVX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(com)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DOS_COM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dwg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DWG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dxf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DXF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dyalog)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DYALOG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dzip)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_DZIP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(epub|mobi|azw)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_EBOOK`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(elf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ELF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(eml)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_EMAIL_TYPE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(emf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_EMF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(eot)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_EOT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(eps)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_EPS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(flac)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FLAC`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(fla)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FLA`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(fli)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FLI`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(flc)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FLC`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(flv)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FLV`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(fpx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FPX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(xcf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_GIMP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(go)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_GOLANG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(gul)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_GUL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(hwp)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_HWP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ico)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ICO`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(indd|idml)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_IN_DESIGN`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ipa)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_IPHONE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ips)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_IPS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(iso)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ISOIMAGE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(java)` AND the extracted email attachment file type does NOT match the regular expression `(?i)(javascript)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JAVA`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(class)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JAVA_BYTECODE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(jmod)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JMOD`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(jng)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JNG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(json)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JSON`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(js)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_JAVASCRIPT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(kgb)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_KGB`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(tex)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_LATEX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(lzfse)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_LZFSE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(vmlinuz|ko)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_LINUX_KERNEL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(bundle|framework)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`. 
  * Else, if the log message matches the regular expression `(?i)(\\bmach\\b)` AND the `filetype` log field value matches the regular expression `(?i)(dylib|o)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(so|initrd|vmlinux|pkg.tar.zst|ext4|ext3|ext2|swap)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_LINUX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ini)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_INI`. 
  * Else, if the log message matches the regular expression `(?i)(\\blinux\\b)` AND the `filetype` log field value matches the regular expression `sfs`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_LINUX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(lnk)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_LNK`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(m4)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_M4`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(midi|mid)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MIDI`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(mkv)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MKV`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(mpg|mpeg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MPEG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(sz_)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MSCOMPRESS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(dll)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_NE_DLL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(odg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ODG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(odp)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ODP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ods)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ODS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(odt)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ODT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ogg|oga|ogv)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_OGG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(one)` AND the extracted email attachment file type does NOT match the regular expression `(?i)(none)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ONE_NOTE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pst|ost)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_OUTLOOK`. 
  * Else, if the log message matches the regular expression `(?i)(\\boutlook\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(msg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_OUTLOOK`. 
  * Else, if the log message matches the regular expression `(?i)(\\bemail\\b)` AND the `filetype` log field value matches the regular expression `(?i)(msg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_EMAIL_TYPE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(prc)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PALMOS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pdb)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PDB`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pem)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PEM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pgp|gpg|asc)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PGP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(php)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PHP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pkg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PKG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ps1|psm1)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_POWERSHELL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ppsx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PPSX`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(psd)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PSD`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ps)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pyc)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PYC`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(py|pyw)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PYTHON`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(whl)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PYTHON_WHL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(qt)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_QUICKTIME`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rm|rmvb)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_RM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rom|bin)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ROM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rpm)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_RPM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rtf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_RTF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rb)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_RUBY`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(rz)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_RZIP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(7z)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SEVENZIP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(sgml|sgm)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SGML`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(bash|csh|zsh)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SHELLSCRIPT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(sql)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SQL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(sqfs|sfs)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SQUASHFS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(svg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SVG`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(swf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SWF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(sis|sisx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SYMBIAN`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(3gp)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_T3GP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(tar)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_TAR`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(tga)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_TARGA`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(3ds|max)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_THREEDS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(tif|tiff)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_TIFF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(torrent)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_TORRENT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(ttf)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_TTF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(vba)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_VBA`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(vhd|vhdx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_VHD`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(wav)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WAV`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(webm)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WEBM`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(webp)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WEBP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(wer)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WER`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(wma)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WMA`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(wmv)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WMV`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(woff|woff2)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WOFF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(xml)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_XML`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(xpi)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_XPI`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(xwd)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_XWD`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(zst)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ZST`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(Makefile|makefile|mk)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MAKEFILE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(zlib)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ZLIB`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(hqx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(hfs|dsk|toast)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH_HFS`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(bh|log|dat)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_BLACKHOLE`. 
  * Else, if the log message matches the regular expression `(?i)(\\bcookie\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(txt)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_COOKIE`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(txt)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_TEXT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(docx|xlsx|pptx)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_OOXML`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(odt|ods|odp|odg)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_ODF`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(for|f90|f95)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FORTRAN`. 
  * Else, if the log message matches the regular expression `(?i)(\\bwince\\b)` AND the `filetype` log field value matches the regular expression `(?i)(exe|cab|dll)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_WINCE`. 
  * Else, if the log message matches the regular expression `(?i)(\\bscript\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(py|js|pl|rb)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SCRIPT`. 
  * Else, if the log message matches the regular expression `(?i)(\\bapplesingle\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(as|bin)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_APPLESINGLE`. 
  * Else, if the log message matches the regular expression `(?i)(\\bmacintosh\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(dylib|a)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH_LIB`. 
  * Else, if the log message matches the regular expression `(?i)(\\bappledouble\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(ad|._)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_APPLEDOUBLE`. 
  * Else, if the log message matches the regular expression `(?i)(\\bobjetivec\\b)` AND the extracted email attachment file type matches the regular expression `(?i)(m|mm|h)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_OBJETIVEC`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(obj|lib)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_COFF`. 
  * Else, if the log message matches the regular expression `(?i)(\\bcpp\\b)` AND the `filetype` log field value matches the regular expression `(?i)(hpp|cpp|cc|cxx|h)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_CPP`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pas|pp)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PASCAL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)(pl|pm)`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_PERL`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)\\bsh\\b`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_SHELLSCRIPT`. 
  * Else, if the extracted email attachment file type matches the regular expression `(?i)\\bc\\b$`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_C`.
  * Else, if the extracted email attachment file type matches the regular expression `(?i)\\bn\\b$`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_NEKO`.
  * Else, if the extracted email attachment file type matches the regular expression `(?i)\\bf\\b`, then the `security_result.about.file.file_type` UDM field is set to `FILE_TYPE_FORTRAN`. 
  * Else, the UDM field `additional.fields.key` is set to `file_type_%{index}` and the extracted email attachment file type is mapped to the `additional.fields.value` UDM field. 

  
`doctypes` | `security_result.detection_fields[doctypes]` |  Document-types separated by pipe delimiters (`|`) are extracted from the `doctypes` log field, then the UDM field `security_result.detection_fields.key` is set to `doctypes_%{index}` and the document-type is mapped to the `security_result.detection_fields.value` UDM field.   
`filenames` | `security_result.about.file.names` |  Attachment file-names separated by pipe delimiters (`|`) are extracted from the `filenames` log field, then the extracted attachment file-name is mapped to the `security_result.about.file.names` UDM field.   
`triggeredrcpts` | `network.email.to` |  Email addresses separated by pipe delimiters (`|`) are extracted from the `triggeredrcpts` log field, and if each extracted email address matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the extracted email address is mapped to the `network.email.to` UDM field.   
`triggeredrcpts` | `target.user.email_addresses` |  Email addresses separated by pipe delimiters (`|`) are extracted from the `triggeredrcpts` log field, and if each extracted email address matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the extracted email address is mapped to the `target.user.email_addresses` UDM field.   
`triggeredrcpts` | `security_result.about.email` |  Email addresses separated by pipe delimiters (`|`) are extracted from the `triggeredrcpts` log field and then combined using comma (`,`), and 

  * If the combined email addresses matches the regular expression pattern `(^.{0,255}$)` then, the combined email addresses is mapped to `security_result.about.email` UDM field.
  * Else, the UDM field `additional.fields.key` is set to `triggeredrcpts` and the combined email addresses is mapped to the `additional.fields.value` UDM field.

  
`otherrcpts` | `network.email.to` |  Email addresses separated by pipe delimiters (`|`) are extracted from the `otherrcpts` log field, and if each extracted email address matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the extracted email address is mapped to the `network.email.to` UDM field.   
`otherrcpts` | `target.user.email_addresses` |  Email addresses separated by pipe delimiters (`|`) are extracted from the `otherrcpts` log field, and if each extracted email address matches the regular expression patterns `(^.+@.+$)` and `(^.{0,255}$)`, then the extracted email address is mapped to the `target.user.email_addresses` UDM field.   
`trigg_rcpt_doms` | `security_result.about.domain.name` |  Unique triggered recipient-domains separated by pipe delimiters (`|`) are extracted from the `trigg_rcpt_doms` log field and then combined using comma (`,`), and 

  * If the combined recipient-domains matches the regular expression pattern `(^.{0,255}$)` then, the combined recipient-domains is mapped to `security_result.about.domain.name` UDM field.
  * Else, the UDM field `additional.fields.key` is set to `trigg_rcpt_doms` and the combined recipient-domains is mapped to the `additional.fields.value` UDM field.

  
`other_rcpt_doms` | `about.domain.name` |  Unique recipient-domains separated by pipe delimiters (`|`) are extracted from the `other_rcpt_doms` log field and then combined using comma (`,`), and 

  * If the combined recipient-domains matches the regular expression pattern `(^.{0,255}$)` then, the combined recipient-domains is mapped to `about.domain.name` UDM field.
  * Else, the UDM field `additional.fields.key` is set to `other_rcpt_doms` and the combined recipient-domains is mapped to the `additional.fields.value` UDM field.

  
`scantime` | `security_result.detection_fields[scantime]` |   
`dlpidentifier` | `security_result.detection_fields[dlpidentifier]` |   
`dlpdictnames` | `security_result.category_details` |  DLP dict-names separated by pipe delimiters (`|`) are extracted from the `dlpdictnames` log field, then each extracted DLP dict-name is mapped to the `security_result.category_details` UDM field.   
`dlpdictcnts` | `security_result.detection_fields[dlpdictcnts]` |  DLP dict-counts separated by pipe delimiters (`|`) are extracted from the `dlpdictcnts` log field, then the UDM field `security_result.detection_fields.key` is set to `dlpdictcnts_%{index}` and the DLP dict-count is mapped to the `security_result.detection_fields.value` UDM field.   
`dlpengnames` | `security_result.detection_fields[dlpengnames]` |  DLP engine-names separated by pipe delimiters (`|`) are extracted from the `dlpengnames` log field, then the UDM field `security_result.detection_fields.key` is set to `dlpengnames_%{index}` and the DLP engine-name is mapped to the `security_result.detection_fields.value` UDM field.   
`recordid` | `metadata.product_log_id` |   
`logtype` | `metadata.product_event_type` |   
`severity` | `security_result.severity_details` |   
`` | `security_result.severity` |  If the `severity` log field value matches the regular expression pattern `(^High.*)`, then the `security_result.severity` UDM field is set to `High`.  
  
Else, if the `severity` log field value matches the regular expression pattern `(^Info.*)`, then the `security_result.severity` UDM field is set to `INFORMATIONAL`.  
  
Else, if the `severity` log field value matches the regular expression pattern `(^Medium.*)`, then the `security_result.severity` UDM field is set to `MEDIUM`.  
  
Else, if the `severity` log field value matches the regular expression pattern `(^Low.*)`, then the `security_result.severity` UDM field is set to `LOW`.  
  
Else, the `security_result.severity` UDM field is set to `UNKNOWN_SEVERITY`.   
`actions` | `security_result.action_details` |  Actions separated by pipe delimiters (`|`) are extracted from the `actions` log field, then combined using comma (`,`) is mapped to the `security_result.action_details` UDM field.   
`` | `security_result.action` |  Actions separated by pipe delimiters (`|`) are extracted from the `action` log field and 

  * If the extracted action matches the regular expression pattern `(^Allow.*)`, then the UDM `security_result.action` is set to `ALLOW`
  * Else, if the extracted action matches the regular expression pattern `(^Block.*)`, then the UDM `security_result.action` is set to `BLOCK`
  * Else, if the extracted action matches the regular expression pattern `(Quarantine)`, then the UDM `security_result.action` is set to `QUARANTINE`
  * Else, the UDM field `security_result.action` is set to `UNKNOWN_ACTION`

  
`rulename` | `security_result.rule_labels` |  Rulenames separated by pipe delimiters (`|`) are extracted from the `rulename` log field, then the extracted rulename is mapped to the `security_result.rule_labels` UDM field.   
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-email-dlp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
