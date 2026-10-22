---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dlp/
title: Collect Zscaler DLP logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:00.477812+00:00
---

# Collect Zscaler DLP logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zscaler DLP logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export Zscaler DLP logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.

For more information, see [Data ingestion to Google SecOps overview](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of Zscaler DLP and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.

The deployment contains the following components:

  * **Zscaler DLP** : The platform from which you collect logs.

  * **Google SecOps feed** : The Google SecOps feed that fetches logs from Zscaler DLP and writes logs to Google SecOps.

  * **Google Security Operations** : retains and analyzes the logs.




An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `ZSCALER_DLP` label.

## Before you begin

Ensure you have the following prerequisites:

  * Access to Zscaler Internet Access console. For more information, see [Secure Internet and SaaS Access ZIA Help](https://help.zscaler.com/zia/getting-started).
  * Zscaler DLP 2024 or later
  * All systems in the deployment architecture are configured with the UTC time zone.
  * The API key which is needed to complete feed setup in Google Security Operations. For more information, see [Setting up API keys](https://support.google.com/googleapi/answer/6158862).



## Set up feeds

To configure this log type, follow these steps:

  1. Go to **SIEM Settings > Feeds**.
  2. Click **Add New Feed**.
  3. Click the **Zscaler** feed pack.
  4. Locate the required log type and click **Add New Feed**. 
  5. Enter values for the following input parameters:

     * **Source Type** : Webhook (Recommended)
     * **Split delimiter** : the character used to separate logs lines. Leave blank if no delimiter is used.

**Advanced options**

     * **Feed Name** : A prepopulated value that identifies the feed.
     * **Asset Namespace** : [Namespace associated with the feed](https://docs.cloud.google.com/chronicle/docs/investigation/asset-namespaces).
     * **Ingestion Labels** : Labels applied to all events from this feed.
  6. Click **Create Feed**.




For more information about configuring multiple feeds for different log types within this product family, see [Configure feeds by product](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds).

## Set up Zscaler DLP

  1. In Zscaler Internet Access console, go to **Administration > Nanolog Streaming Service > Cloud NSS Feeds**.
  2. Click **Add Cloud NSS Feed**.
  3. Enter a name for the feed in the **Feed Name** field.
  4. Select **NSS for Web** in **NSS Type**.
  5. Select the status from the **Status** list to activate or deactivate the NSS feed.
  6. Keep the value in the **SIEM Rate** menu as **Unlimited**. To suppress the output stream due to licensing or other constraints, change the value.
  7. Select **Other** in the **SIEM Type** list.
  8. Select **Disabled** in the **OAuth 2.0 Authentication** list.
  9. Enter a size limit for an individual HTTP request payload to the SIEM's best practice in **Max Batch Size** (for example, **512 KB**).
  10. Enter the HTTPS URL of the Chronicle API endpoint in the API URL in the following format: 
         
         https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
         

     * `CHRONICLE_REGION`: region where your Google SecOps instance is hosted (for example, **US**).
     * `GOOGLE_PROJECT_NUMBER`: Google Cloud project number.
     * `LOCATION`: Google SecOps region (for example, **US**).
     * `CUSTOMER_ID`: Chronicle customer ID.
     * `FEED_ID`: Feed ID shown on the Feed UI on the new webhook created.

Sample API URL:
    
    https://us-chronicle.googleapis.com/v1alpha/projects/12345678910/locations/US/instances/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/feeds/yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy:importPushLogs
    

  11. Click **Add HTTP Header** , and then add HTTP headers in the following format:

     * `Header 1`: **Key1:** `X-goog-api-key` and **Value1:** API Key generated on Google Cloud's API Credentials.
     * `Header 2`: **Key2:** `X-Webhook-Access-Key` and **Value2:** API secret key generated on webhook's "SECRET KEY".
  12. Select **Endpoint DLP** from the **Log Types** list.

  13. Select **JSON** in the **Feed Output Type** list.

  14. Disable **JSON Array Notation**.

  15. Set **Feed Escape Character** to `, \ "`.

  16. To add a new field to the **Feed Output Format,** select **Custom** in the **Feed Output Type** list.

  17. Copy-paste the **Feed Output Format** and add new fields. Ensure the key names match the actual field names.

The following is the default **Feed Output Format** :
         
         \{ "sourcetype" : "zscalernss-edlp", "event" :\{"time":"%s{time}","recordid":"%d{recordid}","login":"%s{user}","dept":"%s{department}","filetypename":"%s{filetypename}","filemd5":"%s{filemd5}","dlpdictnames":"%s{dlpdictnames}","dlpdictcount":"%s{dlpcounts}","dlpenginenames":"%s{dlpengnames}","channel":"%s{channel}","actiontaken":"%s{actiontaken}","severity":"%s{severity}","rulename":"%s{triggeredrulelabel}","itemdstname":"%s{itemdstname}"\}\}
         

  18. Select the time zone for the **Time** field in the output file in the **Timezone** list. By default, the time zone is set to your organization's time zone.

  19. Review the configured settings.

  20. Click **Save** to test connectivity. If the connection is successful, a green tick accompanied by the message **Test Connectivity Successful: OK (200)** appears.




For more information about Google SecOps feeds, see [Google SecOps feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

## Supported Zscaler DLP log formats

The Zscaler DLP parser supports logs in JSON format.

## Supported Zscaler DLP sample logs

  * JSON:
        
        {
          "sourcetype": "zscalernss-edlp",
          "event": {
            "time": "Thu Jun 20 21:14:56 2024",
            "recordid": "7382697059455533057",
            "login": "dummy@domain.com",
            "dept": "General Group",
            "filetypename": "xlsx",
            "filemd5": "9a2d0d62c22994a98f65939ddcd3eb8f",
            "dlpdictnames": "Social Security Number (US): Detect leakage of United States Social Security Numbers|Credit Cards: Detect leakage of credit card information|Aadhaar Card Number (India): Detect Leakage of Indian Aadhaar Card Numbers",
            "dlpdictcount": "1428|141|81",
            "dlpenginenames": "Dummy Engine|cc|PCI|GLBA|HIPAA",
            "channel": "Removable Storage",
            "actiontaken": "Confirm Allow",
            "severity": "High Severity",
            "rulename": "Endpoint_DLP_",
            "itemdstname": "Removable Storage"
          }
        }
        




## UDM Mapping Table

The following table lists the log fields of the `ZSCALER_DLP` log type and their corresponding UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`mon` | `additional.fields[mon]` |   
`day` | `additional.fields[day]` |   
`scantime` | `additional.fields[scantime]` |   
`numdlpengids` | `security_result.detection_fields[numdlpengids]` |   
`numdlpdictids` | `security_result.detection_fields[numdlpdictids]` |   
`recordid` | `metadata.product_log_id` |   
`scanned_bytes` | `additional.fields[scanned_bytes] ` |   
`dlpidentifier` | `security_result.detection_fields[dlpidentifier]` |   
`login` | `principal.user.user_display_name` |   
`b64user` | `principal.user.user_display_name` |   
`euser` | `principal.user.user_display_name` |   
`ouser` | `principal.user.user_display_name` |   
`dept` | `principal.user.department` |   
`b64department` | `principal.user.department` |   
`edepartment` | `principal.user.department` |   
`odepartment` | `principal.user.department` |   
`odevicename` | `security_result.detection_fields[odevicename]` |   
`devicetype` | `principal.asset.attribute.labels[devicetype]` |   
`` | `principal.asset.platform_software.platform` | If the `deviceostype` log field value matches the regular expression pattern `(?i)Windows`, then the `principal.asset.platform_software.platform` UDM field is set to `WINDOWS`.  
`devicename, b64devicename, edevicename, odevicename` | `principal.asset.asset_id` | If the `devicename` log field value is _not_ empty, then the `asset_id:devicename` log field is mapped to the `principal.asset.asset_id` UDM field.  
  
If the `b64devicename` log field value is _not_ empty, then the `asset_id:b64devicename` log field is mapped to the `principal.asset.asset_id` UDM field.  
  
If the `edevicename` log field value is _not_ empty, then the `asset_id:edevicename` log field is mapped to the `principal.asset.asset_id` UDM field.  
  
If the `odevicename` log field value is _not_ empty, then the `asset_id:odevicename` log field is mapped to the `principal.asset.asset_id` UDM field.  
`deviceplatform` | `principal.asset.attribute.labels[deviceplatform]` |   
`deviceosversion` | `principal.asset.platform_software.platform_version` |   
`devicemodel` | `principal.asset.hardware.model` |   
`deviceappversion` | `principal.asset.software.version` |   
`deviceowner` | `principal.asset.attribute.labels[deviceowner]` |   
`b64deviceowner` | `principal.asset.attribute.labels[b64deviceowner]` |   
`edeviceowner` | `principal.asset.attribute.labels[edeviceowner]` |   
`odeviceowner` | `principal.asset.attribute.labels[odeviceowner]` |   
`devicehostname` | `principal.hostname` |   
`b64devicehostname` | `principal.hostname` |   
`edevicehostname` | `principal.hostname` |   
`odevicehostname` | `principal.hostname` |   
`datacenter` | `target.location.name` |   
`datacentercity` | `target.location.city` |   
`datacentercountry` | `target.location.country_or_region` |   
`dsttype` | `target.resource.resource_subtype` |   
`filedoctype` | `additional.fields[filedoctype]` |   
`filedstpath` | `target.file.full_path` |   
`b64filedstpath` | `target.file.full_path` |   
`efiledstpath` | `target.file.full_path` |   
`filemd5` | `target.file.md5` | If the `filemd5` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `filemd5` log field is mapped to the `target.file.md5` UDM field.  
`filesha` | `target.file.sha256` | If the `filesha` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `filesha` log field is mapped to the `target.file.sha256` UDM field.  
`filesrcpath` | `src.file.full_path` |   
`b64filesrcpath` | `src.file.full_path` |   
`efilesrcpath` | `src.file.full_path` |   
`filetypecategory` | `additional.fields[filetypecategory]` |   
`filetypename` | `target.file.file_type` | If the `filetypename` log field value matches the regular expression `(?i)(xlsx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XLSX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(xls)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XLS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(cab)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CAB`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pcapng|pcap|cap)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CAP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(tar.gz|egg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYTHON_PKG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(gzip|tgz|gz)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GZIP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(zip)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZIP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(gif)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GIF`.  
Else, if the log message matches the regular expression `(?i)(\\bdos\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(exe|com)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOS_EXE`.  
Else, if the log message matches the regular expression `(?i)(\\bne_exe\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(exe)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_NE_EXE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(exe)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PE_EXE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(msi)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MSI`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ocx|sys)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PE_DLL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pdf|(portable\\s*document\\s*format))`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PDF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(docx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOCX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(doc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOC`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(html|htm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_HTML`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(jar)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAR`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(jpeg|jpg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JPEG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(mov)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MOV`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(mp3)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MP3`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(mp4)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MP4`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(png)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PNG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pptx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PPTX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ppt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PPT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rar)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RAR`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ace)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ACE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(apk|aar|dex)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ANDROID`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(plist)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLE_PLIST`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(applescript)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLESCRIPT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(app)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(scpt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLESCRIPT_COMPILED`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(arc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ARC`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(arj)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ARJ`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(asd)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ASD`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(asf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ASF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(avi)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_AVI`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(awk)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_AWK`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(bmp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_BMP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dib)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DIB`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(bz2)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_BZIP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(chm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CHM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(cljc|cljs|clj)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CLJ`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(crt|cer)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CRT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(crx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CRX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(csv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CSV`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(deb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DEB`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dmg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DMG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(divx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DIVX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(com)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOS_COM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dwg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DWG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dxf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DXF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dyalog)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DYALOG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dzip)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DZIP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(epub|mobi|azw)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EBOOK`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(elf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ELF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(eml)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EMAIL_TYPE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(emf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EMF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(eot)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EOT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(eps)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EPS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(flac)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLAC`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(fla)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLA`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(fli)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLI`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(flc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLC`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(flv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLV`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(fpx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FPX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(xcf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GIMP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(go)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GOLANG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(gul)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GUL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(hwp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_HWP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ico)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ICO`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(indd|idml)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_IN_DESIGN`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ipa)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_IPHONE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ips)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_IPS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(iso)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ISOIMAGE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(java)` AND the `filetypename` log field value does NOT match the regular expression `(?i)(javascript)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAVA`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(class)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAVA_BYTECODE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(jmod)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JMOD`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(jng)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JNG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(json)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JSON`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(js)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAVASCRIPT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(kgb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_KGB`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(tex)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LATEX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(lzfse)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LZFSE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(vmlinuz|ko)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LINUX_KERNEL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(bundle|framework)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`.  
Else, if the log message matches the regular expression `(?i)(\\bmach\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(dylib|o)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(so|initrd|vmlinux|pkg.tar.zst|ext4|ext3|ext2|swap)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LINUX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ini)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_INI`.  
Else, if the log message matches the regular expression `(?i)(\\blinux\\b)` AND the `filetypename` log field value matches the regular expression `sfs`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LINUX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(lnk)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LNK`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(m4)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_M4`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(midi|mid)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MIDI`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(mkv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MKV`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(mpg|mpeg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MPEG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(sz_)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MSCOMPRESS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(dll)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_NE_DLL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(odg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(odp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ods)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(odt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ogg|oga|ogv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OGG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(one)` AND the `filetypename` log field value does NOT match the regular expression `(?i)(none)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ONE_NOTE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pst|ost)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OUTLOOK`.  
Else, if the log message matches the regular expression `(?i)(\\boutlook\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(msg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OUTLOOK`.  
Else, if the log message matches the regular expression `(?i)(\\bemail\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(msg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EMAIL_TYPE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(prc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PALMOS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pdb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PDB`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pem)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PEM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pgp|gpg|asc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PGP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(php)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PHP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pkg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PKG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ps1|psm1)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_POWERSHELL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ppsx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PPSX`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(psd)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PSD`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ps)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pyc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYC`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(py|pyw)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYTHON`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(whl)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYTHON_WHL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(qt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_QUICKTIME`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rm|rmvb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rom|bin)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ROM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rpm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RPM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rtf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RTF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RUBY`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(rz)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RZIP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(7z)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SEVENZIP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(sgml|sgm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SGML`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(bash|csh|zsh)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SHELLSCRIPT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(sql)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SQL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(sqfs|sfs)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SQUASHFS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(svg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SVG`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(swf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SWF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(sis|sisx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SYMBIAN`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(3gp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_T3GP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(tar)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TAR`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(tga)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TARGA`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(3ds|max)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_THREEDS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(tif|tiff)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TIFF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(torrent)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TORRENT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(ttf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TTF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(vba)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_VBA`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(vhd|vhdx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_VHD`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(wav)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WAV`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(webm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WEBM`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(webp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WEBP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(wer)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WER`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(wma)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WMA`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(wmv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WMV`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(woff|woff2)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WOFF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(xml)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XML`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(xpi)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XPI`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(xwd)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XWD`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(zst)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZST`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(Makefile|makefile|mk)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MAKEFILE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(zlib)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZLIB`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(hqx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(hfs|dsk|toast)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH_HFS`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(bh|log|dat)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_BLACKHOLE`.  
Else, if the log message matches the regular expression `(?i)(\\bcookie\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(txt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_COOKIE`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(txt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TEXT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(docx|xlsx|pptx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OOXML`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(odt|ods|odp|odg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODF`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(for|f90|f95)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FORTRAN`.  
Else, if the log message matches the regular expression `(?i)(\\bwince\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(exe|cab|dll)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WINCE`.  
Else, if the log message matches the regular expression `(?i)(\\bscript\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(py|js|pl|rb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SCRIPT`.  
Else, if the log message matches the regular expression `(?i)(\\bapplesingle\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(as|bin)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLESINGLE`.  
Else, if the log message matches the regular expression `(?i)(\\bmacintosh\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(dylib|a)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH_LIB`.  
Else, if the log message matches the regular expression `(?i)(\\bappledouble\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(ad|._)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLEDOUBLE`.  
Else, if the log message matches the regular expression `(?i)(\\bobjetivec\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(m|mm|h)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OBJETIVEC`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(obj|lib)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_COFF`.  
Else, if the log message matches the regular expression `(?i)(\\bcpp\\b)` AND the `filetypename` log field value matches the regular expression `(?i)(hpp|cpp|cc|cxx|h)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CPP`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pas|pp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PASCAL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)(pl|pm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PERL`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)\\bsh\\b`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SHELLSCRIPT`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)\\bc\\b$`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_C`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)\\bn\\b$`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_NEKO`.  
Else, if the `filetypename` log field value matches the regular expression `(?i)\\bf\\b`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FORTRAN`.  
Else, the UDM field `additional.fields.key` is set to `filetypename` and the log field value `filetypename` is mapped to the `additional.fields.value` UDM field, provided the `filetypename` value is not empty.  
`itemdstname` | `target.resource.name` |   
`b64itemdstname` | `target.resource.name` |   
`eitemdstname` | `target.resource.name` |   
`itemname` | `target.resource.attribute.labels[itemname]` |   
`b64itemname` | `target.resource.attribute.labels[b64itemname]` |   
`eitemname` | `target.resource.attribute.labels[eitemname]` |   
`itemsrcname` | `src.resource.name` |   
`b64itemsrcname` | `src.resource.name` |   
`eitemsrcname` | `src.resource.name` |   
`itemtype` | `target.resource.attribute.labels[itemtype]` |   
`ofiledstpath` | `target.file.full_path` |   
`ofilesrcpath` | `src.file.full_path` |   
`oitemdstname` | `target.resource.name` |   
`oitemname` | `target.resource.attribute.labels[oitemname]` |   
`odlpengnames` | `security_result.detection_fields[odlpengnames]` |   
`oitemsrcname` | `src.resource.name` |   
`srctype` | `src.resource.resource_subtype` |   
`actiontaken` | `security_result.action_details` |   
`` | `security_result.action` | If the `actiontaken` log field value matches the regular expression pattern `(?i)allow`, then the `security_result.action` UDM field is set to `ALLOW`.  
  
Else, if the `actiontaken` log field value matches the regular expression pattern `(?i)block`, then the `security_result.action` UDM field is set to `BLOCK`.  
`activitytype` | `metadata.product_event_type` |   
`addinfo` | `additional.fields[addinfo]` |   
`channel` | `security_result.detection_fields[channel]` |   
`confirmaction` | `security_result.detection_fields[confirmaction]` |   
`confirmjust` | `security_result.description` |   
`dlpdictcount` | `security_result.detection_fields[dlpdictcount]` |   
`dlpdictnames` | `security_result.detection_fields[dlpdictnames]` |   
`b64dlpdictnames` | `security_result.detection_fields[b64dlpdictnames]` |   
`edlpdictnames` | `security_result.detection_fields[edlpdictnames]` |   
`dlpenginenames` | `security_result.detection_fields[dlpenginenames]` |   
`b64dlpengnames` | `security_result.detection_fields[b64dlpengnames]` |   
`edlpengnames` | `security_result.detection_fields[edlpengnames]` |   
`expectedaction` | `security_result.detection_fields[expectedaction]` |   
`logtype` | `security_result.category_details` |   
`odlpdictnames` | `security_result.detection_fields[odlpdictnames]` |   
`ootherrulelabels` | `security_result.rule_labels[ootherrulelabels]` |   
`otherrulelabels` | `security_result.rule_labels[otherrulelabels]` |   
`b64otherrulelabels` | `security_result.rule_labels[b64otherrulelabels]` |   
`eotherrulelabels` | `security_result.rule_labels[eotherrulelabels]` |   
`otriggeredrulelabel` | `security_result.rule_name` |   
`severity` | `security_result.severity_details` |   
`` | `security_result.severity` | If the `severity` log field value matches the regular expression pattern `(?i)High`, then the `security_result.severity` UDM field is set to `HIGH`.  
  
Else, if the `severity` log field value matches the regular expression pattern `(?i)Medium`, then the `security_result.severity` UDM field is set to `MEDIUM`.  
  
Else, if the `severity` log field value matches the regular expression pattern `(?i)Low`, then the `security_result.severity` UDM field is set to `LOW`.  
  
Else, if the `severity` log field value matches the regular expression pattern `(?i)Info`, then the `security_result.severity` UDM field is set to `INFORMATIONAL`.  
`rulename` | `security_result.rule_name` |   
`b64triggeredrulelabel` | `security_result.rule_name` |   
`etriggeredrulelabel` | `security_result.rule_name` |   
`zdpmode` | `security_result.detection_fields[zdpmode]` |   
`tz` | `additional.fields[tz]` |   
`ss` | `additional.fields[ss]` |   
`mm` | `additional.fields[mm]` |   
`hh` | `additional.fields[hh]` |   
`dd` | `additional.fields[dd]` |   
`mth` | `additional.fields[mth]` |   
`yyyy` | `additional.fields[yyyy]` |   
`sourcetype` | `additional.fields[sourcetype]` |   
`eventtime` | `metadata.event_timestamp` |   
`time` | `metadata.collected_timestamp` |   
`rtime` | `additional.fields[rtime]` |   
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Zscaler`.  
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `DLP`.  
`` | `metadata.event_type` | If the `activitytype` log field value is one of the following, then the `metadata.event_type` UDM field is set to `FILE_UNCATEGORIZED`: 

  * `Upload`
  * `Download`

Else, if the `activitytype` log field value is `File Copy`, then the `metadata.event_type` UDM field is set to `FILE_COPY`.  
  
Else, if the `activitytype` log field value is `File Read`, then the `metadata.event_type` UDM field is set to `FILE_READ`.  
  
Else, if the `activitytype` log field value is `File Write`, then the `metadata.event_type` UDM field is set to `FILE_MODIFICATION`.  
  
Else, if the `activitytype` log field value is `Email Sent`, then the `metadata.event_type` UDM field is set to `EMAIL_UNCATEGORIZED`.  
  
Else, if the `activitytype` log field value is `Print`, then the `metadata.event_type` UDM field is set to `STATUS_UPDATE`.  
  
Else, if one of the `devicehostname`, `b64devicehostname`, `edevicehostname`, or `odevicehostname` log fields is not empty, and one of the `filedstpath`, `b64filedstpath`, `efiledstpath`, `ofiledstpath`, `filemd5`, `filesha`, or `filetypename` log fields is not empty, then if one of the `filesrcpath`, `b64filesrcpath`, `efilesrcpath`, or `ofiledstpath` log fields is not empty, the `metadata.event_type` UDM field is set to `FILE_COPY`, otherwise it is set to `FILE_UNCATEGORIZED`.  
  
Else, if one of the `devicehostname`, `b64devicehostname`, `edevicehostname`, or `odevicehostname` log fields is not empty, then the `metadata.event_type` UDM field is set to `STATUS_UPDATE`.  
  
Else, the `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-dlp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
