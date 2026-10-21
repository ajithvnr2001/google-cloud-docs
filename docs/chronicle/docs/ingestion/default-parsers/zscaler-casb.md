---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb/
title: Collect Zscaler CASB logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:32:18.555928+00:00
---

# Collect Zscaler CASB logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-casb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zscaler CASB logs

This document describes how you can export Zscaler CASB logs by setting up a Google Security Operations feed and mapping log fields to the Unified Data Model (UDM).

For more information, see [Data ingestion to Google SecOps overview](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of Zscaler CASB and a Google SecOps Webhook feed configured to send logs to Google SecOps. However, deployment details can differ by customer and could be more complex.

The deployment contains the following components:

  * **Zscaler CASB** : The platform from which you collect logs.

  * **Google SecOps feed** : The Google SecOps feed that fetches logs from Zscaler CASB and writes logs to Google SecOps.

  * **Google SecOps** : Retains and analyzes the logs.




An ingestion label identifies the parser that normalizes raw log data into the structured UDM format. This document applies specifically to the parser associated with the ZSCALER_CASB ingestion label.

## Before you begin

  * Ensure that you have access to Zscaler Internet Access console. For more information, see [Secure Internet and SaaS Access ZIA Help](https://help.zscaler.com/zia/getting-started).
  * Ensure that you're using Zscaler CASB version 1.0 or 2.0.
  * Ensure that all systems in the deployment architecture are configured with the UTC time zone.
  * Ensure that you have the API key required to complete feed setup in Google SecOps. For more information, see [Setting up API keys](https://support.google.com/googleapi/answer/6158862).



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

## Set up Zscaler CASB

  1. In the Zscaler Internet Access Console, click **Administration > Nanolog Streaming Service > Cloud NSS Feeds > Add Cloud NSS Feed**.
  2. In the **Add Cloud NSS Feed window** , enter the details.
  3. In the **Feed Name** field, enter a unique name for the feed.
  4. Select **Zscaler for Web** in **NSS Type**.
  5. In the **Status** list, select a status to activate or deactivate the NSS feed.
  6. Leave **SIEM Rate** as **Unlimited** , unless you need to throttle the output stream due to licensing or other constraints.
  7. In the **SIEM Type** list, select **Other**.
  8. In the **OAuth 2.0 Authentication** list, select **Disabled**.
  9. In the **Max Batch Size** field, enter a size limit for an individual HTTP request payload to the SIEM's best practice; for example, `512 KB`.
  10. In the **API URL** field, enter the HTTPS URL of the Chronicle API endpoint using the following format:
         
         https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
         

     * `CHRONICLE_REGION`: Region where your Google SecOps instance is hosted. For example, `US`.
     * `GOOGLE_PROJECT_NUMBER`: Google Cloud project number.
     * `LOCATION`: Chronicle (Google SecOps) region (same as `CHRONICLE_REGION`). For example, `US`.
     * `CUSTOMER_ID`: Chronicle customer ID.
     * `FEED_ID`: ID of the newly created webhook feed (shown in the Feed UI).
     * Sample API URL:
           
           https://us-chronicle.googleapis.com/v1alpha/projects/12345678910/locations/US/instances/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/feeds/yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy:importPushLogs
           

  11. Click **Add HTTP Header** , and then add HTTP headers in the following format:

     * `Header 1`: **Key1:** `X-goog-api-key` and **Value1:** API Key generated on Google Cloud's API Credentials.
     * `Header 2`: **Key2:** `X-Webhook-Access-Key` and **Value2:** API secret key generated in webhook's "SECRET KEY".
  12. In the **Log Types** list, select **SaaS Security** or **SaaS Security Activity**.

  13. In the **Feed Output Type** list, select **JSON**.

  14. Disable **JSON Array Notation**.

  15. Set **Feed Escape Character** to `, \ "`.

  16. In the **Feed Output Type** list, select **Custom** to add a new field to the **Feed Output Format**.

  17. Copy and paste the **Feed Output Format** , and then add new fields, as needed. Ensure the key names match the actual field names.

  18. Following are the default **Feed Output Formats** :

     * SaaS Security
    
    \{ "sourcetype" : "zscalernss-casb", "event" :\{"datetime":"%s{time}","recordid":"%d{recordid}","company":"%s{company}","tenant":"%s{tenant}","login":"%s{user}","dept":"%s{department}","applicationname":"%s{applicationname}","filename":"%s{filename}","filesource":"%s{filesource}","filemd5":"%s{filemd5}","threatname":"%s{threatname}","policy":"%s{policy}","dlpdictnames":"%s{dlpdictnames}","dlpdictcount":"%s{dlpdictcount}","dlpenginenames":"%s{dlpenginenames}","fullurl":"%s{fullurl}","lastmodtime":"%s{lastmodtime}","filescantimems":"%d{filescantimems}","filedownloadtimems":"%d{filedownloadtimems}"\}\}
    

     * SaaS Security Activity
    
    \{ "sourcetype" : "zscalernss-casb", "event" :\{"login":"%s{username}","tenant":"%s{tenant}","object_type":"%d{objtype1}","applicationname":"%s{appname}","object_name_1":"%s{objnames1}","object_name_2":"%s{objnames2}"\}\}
    

  19. From the **Timezone** list, select the time zone for the **Time** field in the output file. By default, the time zone is set to your organization's time zone.

  20. Review the configured settings. 

  21. Click **Save** to test connectivity. If the connection is successful, a green tick accompanied by the message **Test Connectivity Successful: OK (200)** appears.




For more information about Google SecOps feeds, see [Google SecOps feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

## Supported Zscaler CASB log formats

The Zscaler CASB parser supports logs in JSON format.

## Supported Zscaler CASB Sample Logs

  * JSON
        
        {
            "sourcetype": "zscalernss-casb",
            "event": {
                "recordid": "7124548470481682433",
                "company": "Dummy Company",
                "tenant": "dummy-tenant",
                "login": "sample@example.com",
                "dept": "Technology Services",
                "applicationname": "ONEDRIVE",
                "filename": "RB nexxus scan.csv",
                "filesource": "/Calvin Projects/PR20081910 AMS DB2 v11 Upgrade in WDM Solution",
                "filemd5": "None",
                "threatname": "None",
                "policy": "None",
                "dlpdictnames": "None",
                "dlpdictcount": "None",
                "dlpenginenames": "None",
                "fullurl": "Unknown URL",
                "lastmodtime": "Wed Mar 23 10:52:11 2022",
                "filescantimems": "217",
                "filedownloadtimems": "175",
                "download_time": "1469",
                "runid": "27",
                "scan_time": "2128",
                "scanid": "2",
                "file_doctype": "Legal",
                "filesha": "ceeedc88dc02cd599865e89696f2bc33a049dc823a698183d429b9bc65735a3a",
                "sender_type": "Bot",
                "last_edit_user": "test-user@cc.com",
                "last_share_user": "last-dummy-user@cc.com",
                "last_shared_on": "Mon Oct 29 071801 2025",
                "botname": "PREDEFINED_GPT",
                "dlpengnames": "HIPAA|PCI|Social SecurityNumbers",
                "departmentname": "Sales",
                "extusername": "ext-dummy-user@cc.com",
                "filetype": "pop",
                "extcollab_groups": "2386907809368318240|2386907809989075232",
                "intcollab_groups": "23869078093683182409|23869078099890752329",
                "oextcollab_groups": "23869078093683182409|23869078099890752328",
                "ointcollab_groups": "2386907809385095456|2386907809401872672",
                "dlpdictcnts": "4|5|1|2",
                "filetypename": "txt"
            }
          }
        
        




## Field mapping reference

### Field mapping reference: ZSCALER_CASB 

The following table lists the log fields of the `ZSCALER_CASB` log type and their corresponding UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`sourcetype` | `additional.fields[sourcetype]` |   
`objnames2` | `about.resource.name` |   
`object_name_2` | `about.resource.name` |   
`objtypename2` | `about.resource.resource_subtype` |   
`externalownername` | `additional.fields[externalownername]` |   
`act_cnt` | `additional.fields[act_cnt]` |   
`attchcomponentfiletypes` | `additional.fields[attchcomponentfiletypes]` |   
`channel_name` | `additional.fields[channel_name]` |   
`collabscope` | `additional.fields[collabscope]` |   
`day` | `additional.fields[day]` |   
`dd` | `additional.fields[dd]` |   
`dlpdictcount` | `security_result.detection_fields[dlpdictcount]` | If the `dlpdictcount` log field value is _not_ empty and the `dlpdictcount` log field value is not equal to `None`, then the `dlpdictcount` log field is mapped to the `security_result.detection_fields.dlpdictcount` UDM field.  
`dlpenginenames` | `security_result.detection_fields[dlpenginenames]` | If the `dlpenginenames` log field value is _not_ empty and the `dlpenginenames` log field value is not equal to `None`, then the `dlpenginenames` log field is mapped to the `security_result.detection_fields.dlpenginenames` UDM field.  
`epochlastmodtime` | `additional.fields[epochlastmodtime]` |   
`extcollabnames` | `additional.fields[extcollabnames]` |   
`extownername` | `additional.fields[extownername]` |   
`file_msg_id` | `additional.fields[file_msg_id]` |   
`fileid` | `additional.fields[fileid]` |   
`filescantimems` | `additional.fields[filescantimems]` |   
`filetypecategory` | `additional.fields[filetypecategory]` |   
`hh` | `additional.fields[hh]` |   
`messageid` | `additional.fields[messageid]` |   
`mm` | `additional.fields[mm]` |   
`mon` | `additional.fields[mon]` |   
`msgsize` | `additional.fields[msgsize]` |   
`mth` | `additional.fields[mth]` |   
`num_ext_recpts` | `additional.fields[num_ext_recpts]` |   
`num_int_recpts` | `additional.fields[num_int_recpts]` |   
`numcollab` | `additional.fields[numcollab]` |   
`rtime` | `additional.fields[rtime]` |   
`ss` | `additional.fields[ss]` |   
`suburl` | `additional.fields[suburl]` |   
`tenant` | `additional.fields[tenant]` |   
`tz` | `additional.fields[tz]` |   
`upload_doctypename` | `additional.fields[upload_doctypename]` |   
`yyyy` | `additional.fields[yyyy]` |   
`collabnames` | `additional.fields[collabnames]` |   
`companyid` | `additional.fields[companyid]` |   
`component` | `additional.fields[component]` |   
`intcollabnames` | `additional.fields[intcollabnames]` | If `intcollabnames` log field value does not match the regular expression pattern `None` then, for `index` in `intcollabnames`, the `index` is mapped to the `additional.fields.value.list_value` UDM field.  
`internal_collabnames` | `additional.fields[internal_collabnames]` |   
`external_collabnames` | `additional.fields[external_collabnames]` |   
`num_external_collab` | `additional.fields[num_external_collab]` |   
`num_internal_collab` | `additional.fields[num_internal_collab]` |   
`repochtime` | `additional.fields[repochtime]` |   
`eventtime` | `metadata.event_timestamp` | If the `eventtime` log field value is _not_ empty, then the `eventtime` log field is mapped to the `metadata.event_timestamp` UDM field.  
`epochtime` | `metadata.event_timestamp` | If the `epochtime` log field value is _not_ empty, then the `epochtime` log field is mapped to the `metadata.event_timestamp` UDM field.  
`time` | `metadata.event_timestamp` | If the `time` log field value is _not_ empty, then the `time` log field is mapped to the `metadata.event_timestamp` UDM field.  
`datetime` | `metadata.event_timestamp` | If the `datetime` log field value is _not_ empty, then the `datetime` log field is mapped to the `metadata.event_timestamp` UDM field.  
`` | `metadata.event_type` | If `principal.ip` is not empty or `principal.hostname` is not empty, and `target.ip` is not empty, then `metadata.event_type` is set to `NETWORK_CONNECTION`.  
  
Else if any of the following UDM fields are empty: `principal.user.userid`, `principal.user.email_addresses`, `principal.hostname`, `principal.asset_id`, `principal.ip`, `principal.mac`, `target.hostname`, `target.asset_id`, `target.ip`, `target.mac`, `target.user.email_addresses`, `target.user.userid`, then `metadata.event_type` is set to `USER_UNCATEGORIZED`.  
  
Else if any of the following UDM fields are empty: `principal.hostname`, `principal.asset_id`, `principal.ip`, `principal.mac`, then `metadata.event_type` is set to `STATUS_UPDATE`.  
`act_type_name` | `metadata.product_event_type` |   
`recordid` | `metadata.product_log_id` |   
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `CASB`.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `Zscaler`.  
`sender` | `network.email.from` | If the `sender` log field value matches the regular expression pattern `(^.*@.*$)`, then the `sender` log field is mapped to the `network.email.from` UDM field.  
`extrecptnames` | `network.email.to` | For `index` in `extrecptnames`, the `index` is mapped to the `network.email.to` UDM field.  
`internal_recptnames` | `network.email.to` | For `index` in `internal_recptnames`, the `index` is mapped to the `network.email.to` UDM field.  
`external_recptnames` | `network.email.to` | For `index` in `external_recptnames`, the `index` is mapped to the `network.email.to` UDM field.  
`intrecptnames` | `network.email.to` | For `index` in `intrecptnames`, the `index` is mapped to the `network.email.to` UDM field.  
`applicationname` | `target.application` | If the `applicationname` log field value is _not_ empty, then the `applicationname` log field is mapped to the `target.application` UDM field.  
  
Else, the `appname` log field is mapped to the `target.application` UDM field.  
`appname` | `target.application` | If the `applicationname` log field value is _not_ empty, then the `applicationname` log field is mapped to the `target.application` UDM field.  
  
Else, the `appname` log field is mapped to the `target.application` UDM field.  
`src_ip` | `principal.ip` |   
`fullurl` | `principal.url` | If the `fullurl` log field is _not_ empty and the `fullurl` log field value is not equal to `Unknown URL`, then the `fullurl` log field is mapped to the `principal.url` UDM field.  
`is_admin_act` | `principal.user.attribute.labels[is_admin_act]` |   
`` | `principal.user.attribute.roles.type` | If the `is_admin_act` log field value is equal to `1`, then the `principal.user.attribute.roles.type` UDM field is set to `ADMINISTRATOR`.  
`company` | `principal.user.company_name` |   
`department` | `principal.user.department` | If the `dept` log field value is _not_ empty, then the `dept` log field is mapped to the `principal.user.department` UDM field. Else, the `department` log field is mapped to the `principal.user.department` UDM field.  
`dept` | `principal.user.department` | If the `dept` log field value is _not_ empty, then the `dept` log field is mapped to the `principal.user.department` UDM field. Else, the `department` log field is mapped to the `principal.user.department` UDM field.  
`user` | `principal.user.email_addresses` | If the `user` log field value matches the regular expression pattern `(^.*@.*$)`, then the `user` log field is mapped to the `principal.user.email_addresses` UDM field.  
`username` | `principal.user.email_addresses` | If the `username` log field value matches the regular expression pattern `(^.*@.*$)`, then the `username` log field is mapped to the `principal.user.email_addresses` UDM field.  
`owner` | `principal.user.email_addresses` | If the `owner` log field value matches the regular expression pattern `(^.*@.*$)`, then the `owner` log field is mapped to the `principal.user.email_addresses` UDM field.  
`login` | `principal.user.email_addresses` | If the `login` log field value matches the regular expression pattern `(^.*@.*$)`, then the `login` log field is mapped to the `principal.user.email_addresses` UDM field.  
`login` | `principal.user.userid` | If the `login` log field value does not match the regular expression pattern `^.+@.+$`, then the `login` log field is mapped to the `principal.user.userid` UDM field.  
`malware` | `security_result.associations.name` |   
`` | `security_result.associations.type` | If the `malware` log field value is _not_ empty, then the `security_result.associations.type` UDM field is set to `MALWARE`.  
`dlpdictnames` | `security_result.detection_fields[dlpdictnames]` |   
`dlpidentifier` | `security_result.detection_fields[dlpidentifier]` |   
`filedownloadtimems` | `additional.fields[filedownloadtimems]` |   
`malwareclass` | `security_result.threat_name` |   
`msgid` | `additional.fields[msgid]` |   
`oattchcomponentfilenames` | `target.file.names` |   
`obucketname` | `target.resource.name` |   
`obucketowner` | `target.resource.attribute.labels[obucketowner]` |   
`ochannel_name` | `additional.fields[ochannel_name]` |   
`ocollabnames` | `additional.fields[ocollabnames]` |   
`odlpdictnames` | `security_result.detection_fields[odlpdictnames]` |   
`odlpenginenames` | `security_result.detection_fields[odlpenginenames]` |   
`oextcollabnames` | `additional.fields[oextcollabnames]` |   
`oexternal_collabnames` | `additional.fields[oexternal_collabnames]` |   
`oexternal_recptnames` | `network.email.to` |   
`oexternalownername` | `additional.fields[oexternalownername]` |   
`oextownername` | `additional.fields[oextownername]` |   
`oextrecptnames` | `network.email.to` |   
`ofile_msg_id` | `additional.fields[ofile_msg_id]` |   
`ofileid` | `additional.fields[ofileid]` |   
`ofullurl` | `principal.url` | If the `ofullurl` log field is _not_ empty and the `ofullurl` log field value is not equal to `Unknown URL`, then the `ofullurl` log field is mapped to the `principal.url` UDM field.  
`ohostname` | `target.hostname` |   
`ointcollabnames` | `additional.fields[ointcollabnames]` |   
`ointernal_collabnames` | `additional.fields[ointernal_collabnames]` |   
`ointernal_recptnames` | `network.email.to` |   
`ointrecptnames` | `network.email.to` |   
`omessageid` | `additional.fields[omessageid]` |   
`omsgid` | `additional.fields[omsgid]` |   
`oowner` | `principal.user.email_addresses` | If the `oowner` log field value matches the regular expression pattern `(^.*@.*$)`, then the `oowner` log field is mapped to the `principal.user.email_addresses` UDM field.  
`orulelabel` | `security_result.rule_name` |   
`osender` | `network.email.from` | If the `osender` log field value matches the regular expression pattern `(^.*@.*$)`, then the `osender` log field is mapped to the `network.email.from` UDM field.  
`osharedchannel_hostname` | `target.hostname` |   
`otenant` | `additional.fields[otenant]` |   
`ouser` | `principal.user.email_addresses` | If the `ouser` log field value matches the regular expression pattern `(^.*@.*$)`, then the `ouser` log field is mapped to the `principal.user.email_addresses` UDM field.  
`any_incident` | `security_result.detection_fields[any_incident]` |   
`is_inbound` | `security_result.detection_fields[is_inbound]` |   
`policy` | `security_result.rule_labels[policy]` |   
`ruletype` | `security_result.rule_labels[ruletype]` |   
`rulelabel` | `security_result.rule_name` |   
`` | `security_result.severity` | If the `severity` log field value is equal to `High`, then the `security_result.severity` UDM field is set to `HIGH`.  
  
Else, if the `severity` log field value is equal to `Medium`, then the `security_result.severity` UDM field is set to `MEDIUM`.  
  
Else, if the `severity` log field value is equal to `Low`, then the `security_result.sevrity` UDM field is set to `LOW`.  
  
Else, if the `severity` log field value is equal to `Information`, then the `security_result.severity` UDM field is set to `INFORMATIONAL`.  
`threatname` | `security_result.threat_name` | If the `threatname` log field value is _not_ empty and the `dlpdictcount` log field value is not equal to `None`, then the `threatname` log field is mapped to the `security_result.threat_name` UDM field.  
`filesource` | `target.file.full_path` | If `filepath` is not empty, then the `filepath` log field is mapped to the `target.file.full_path` UDM field. Else if `filesource` is not empty, then the `filesource` log field is mapped to the `target.file.full_path` UDM field.  
`filepath` | `target.file.full_path` | If `filepath` is not empty, then the `filepath` log field is mapped to the `target.file.full_path` UDM field. Else if `filesource` is not empty, then the `filesource` log field is mapped to the `target.file.full_path` UDM field.  
`lastmodtime` | If the `file_msg_mod_time` log field value is _not_ empty, then the `file_msg_mod_time` log field is mapped to the `target.file.last_modification_time` UDM field.  
  
Else if the `lastmodtime` log field value is _not_ empty, then the `lastmodtime` log field is mapped to the `target.file.last_modification_time` UDM field.  
`file_msg_mod_time` | `target.file.last_modification_time` | If the `file_msg_mod_time` log field value is _not_ empty, then the `file_msg_mod_time` log field is mapped to the `target.file.last_modification_time` UDM field.  
  
Else if the `lastmodtime` log field value is _not_ empty, then the `lastmodtime` log field is mapped to the `target.file.last_modification_time` UDM field.  
`filemd5` | `target.file.md5` | If the `attchcomponentmd5s` log field value is _not_ equal to empty and the `attchcomponentmd5s` log field value matches the regular expression pattern `^[a-fA-F0-9]{32}$`, then the `attchcomponentmd5s` log field is mapped to the `target.file.md5` UDM field.  
  
Else, if the `filemd5` log field value matches the regular expression pattern `^[a-fA-F0-9]{32}$`, then the `filemd5` log field is mapped to the `target.file.md5` UDM field.  
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
`filename` | `target.file.names` |   
`attchcomponentfilenames` | `target.file.names` |   
`attchcomponentfilesizes` | `target.file.size` | If the `filesize` log field value is _not_ empty, then the `filesize` log field is mapped to the `target.file.size` UDM field.  
  
Else if the `attchcomponentfilesizes` log field value is _not_ empty, then the `attchcomponentfilesizes` log field is mapped to the `target.file.size` UDM field.  
`b64attchcomponentfilesizes` | `target.file.size` | If the `filesize` log field value is _not_ empty, then the `filesize` log field is mapped to the `target.file.size` UDM field.  
  
Else if the `b64attchcomponentfilesizes` log field value is _not_ empty, then the `b64attchcomponentfilesizes` log field is mapped to the `target.file.size` UDM field.  
`sha` | `target.file.sha256` | If the `sha` log field value matches the regular expression pattern `^[0-9a-f]+$`, then the `sha` log field is mapped to the `target.file.sha256` UDM field.  
`filesize` | `target.file.size` | If the `filesize` log field value is _not_ empty, then the `filesize` log field is mapped to the `target.file.size` UDM field.  
  
Else if the `attchcomponentfilesizes` log field value is _not_ empty, then the `attchcomponentfilesizes` log field is mapped to the `target.file.size` UDM field.  
`sharedchannel_hostname` | `target.hostname` |   
`hostname` | `target.hostname` | If the `sharedchannel_hostname` log field value is empty and the `osharedchannel_hostname` log field value is empty, then the `hostname` log field is mapped to the `target.hostname` UDM field.  
`datacentercity` | `target.location.city` |   
`datacentercountry` | `target.location.country_or_region` |   
`datacenter` | `target.location.name` |   
`bucketowner` | `target.resource.attribute.labels[bucketowner]` |   
`projectname` | `target.resource.attribute.labels[projectname]` |   
`bucketname` | `target.resource.name` | If the `bucketname` log field value is _not_ empty, then the `bucketname` log field is mapped to the `target.resource.name` UDM field.  
`objnames1` | `target.resource.name` | If the `objnames1` log field value is _not_ empty, then the `objnames1` log field is mapped to the `target.resource.name` UDM field.  
`objectname` | `target.resource.name` | If the `objectname` log field value is _not_ empty, then the `objectname` log field is mapped to the `target.resource.name` UDM field.  
`reponame` | `target.resource.name` | If the `reponame` log field value is _not_ empty, then the `reponame` log field is mapped to the `target.resource.name` UDM field.  
`object_name_1` | `target.resource.name` | If the `object_name_1` log field value is _not_ empty, then the `object_name_1` log field is mapped to the `target.resource.name` UDM field.  
`bucketid` | `target.resource.product_object_id` |   
`objtypename1` | `target.resource.resource_subtype` | If the `objtypename1` log field value is _not_ empty, then the `objtypename1` log field is mapped to the `target.resource.resource_subtype` UDM field.  
`objecttype` | `target.resource.resource_subtype` | If the `objecttype` log field value is _not_ empty, then the `objecttype` log field is mapped to the `target.resource.resource_subtype` UDM field.  
`object_type` | `target.resource.resource_subtype` |   
`` | `target.resource.resource_type` | If the `bucketname` log field value is _not_ empty, then the `target.resource.resource_type` UDM field is set to `STORAGE_BUCKET`.  
  
If the `reponame` log field value is _not_ empty, then the `target.resource.resource_type` UDM field is set to `REPOSITORY`.  
`departmentname` | `principal.user.department` |   
`extusername` | `target.user.userid` |   
`download_time` | `additional.fields[download_time]` |   
`runid` | `additional.fields[runid]` |   
`scan_time` | `additional.fields[scan_time]` |   
`scanid` | `additional.fields[scanid]` |   
`file_doctype` | `additional.fields[file_doctype]` |   
`filesha` | `additional.fields[filesha]` |   
`sender_type` | `additional.fields[sender_type]` |   
`last_edit_user` | `security_result.detection_fields[last_edit_user]` |   
`last_share_user` | `security_result.detection_fields[last_share_user]` |   
`last_shared_on` | `security_result.detection_fields[last_shared_on]` |   
`botname` | `security_result.detection_fields[botname]` |   
`dlpengnames` | `security_result.detection_fields[dlpengnames]` |   
`filetype` | `target.file.file_type` | If the `filetype` log field value matches the regular expression `(?i)(xlsx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XLSX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(xls)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XLS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(cab)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CAB`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pcapng|pcap|cap)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CAP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(tar.gz|egg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYTHON_PKG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(gzip|tgz|gz)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GZIP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(zip)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZIP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(gif)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GIF`.  
Else, if the log message matches the regular expression `(?i)(\\bdos\\b)` AND the `filetype` log field value matches the regular expression `(?i)(exe|com)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOS_EXE`.  
Else, if the log message matches the regular expression `(?i)(\\bne_exe\\b)` AND the `filetype` log field value matches the regular expression `(?i)(exe)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_NE_EXE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(exe)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PE_EXE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(msi)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MSI`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ocx|sys)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PE_DLL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pdf|(portable\\s*document\\s*format))`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PDF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(docx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOCX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(doc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOC`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(html|htm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_HTML`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(jar)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAR`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(jpeg|jpg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JPEG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(mov)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MOV`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(mp3)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MP3`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(mp4)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MP4`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(png)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PNG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pptx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PPTX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ppt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PPT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rar)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RAR`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ace)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ACE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(apk|aar|dex)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ANDROID`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(plist)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLE_PLIST`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(applescript)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLESCRIPT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(app)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(scpt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLESCRIPT_COMPILED`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(arc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ARC`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(arj)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ARJ`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(asd)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ASD`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(asf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ASF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(avi)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_AVI`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(awk)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_AWK`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(bmp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_BMP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dib)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DIB`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(bz2)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_BZIP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(chm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CHM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(cljc|cljs|clj)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CLJ`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(crt|cer)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CRT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(crx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CRX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(csv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CSV`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(deb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DEB`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dmg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DMG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(divx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DIVX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(com)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DOS_COM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dwg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DWG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dxf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DXF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dyalog)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DYALOG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dzip)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_DZIP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(epub|mobi|azw)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EBOOK`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(elf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ELF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(eml)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EMAIL_TYPE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(emf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EMF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(eot)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EOT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(eps)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EPS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(flac)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLAC`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(fla)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLA`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(fli)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLI`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(flc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLC`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(flv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FLV`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(fpx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FPX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(xcf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GIMP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(go)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GOLANG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(gul)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_GUL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(hwp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_HWP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ico)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ICO`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(indd|idml)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_IN_DESIGN`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ipa)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_IPHONE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ips)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_IPS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(iso)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ISOIMAGE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(java)` AND the `filetype` log field value does NOT match the regular expression `(?i)(javascript)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAVA`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(class)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAVA_BYTECODE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(jmod)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JMOD`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(jng)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JNG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(json)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JSON`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(js)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_JAVASCRIPT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(kgb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_KGB`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(tex)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LATEX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(lzfse)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LZFSE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(vmlinuz|ko)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LINUX_KERNEL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(bundle|framework)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`.  
Else, if the log message matches the regular expression `(?i)(\\bmach\\b)` AND the `filetype` log field value matches the regular expression `(?i)(dylib|o)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACH_O`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(so|initrd|vmlinux|pkg.tar.zst|ext4|ext3|ext2|swap)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LINUX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ini)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_INI`.  
Else, if the log message matches the regular expression `(?i)(\\blinux\\b)` AND the `filetype` log field value matches the regular expression `sfs`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LINUX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(lnk)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_LNK`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(m4)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_M4`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(midi|mid)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MIDI`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(mkv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MKV`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(mpg|mpeg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MPEG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(sz_)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MSCOMPRESS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(dll)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_NE_DLL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(odg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(odp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ods)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(odt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ogg|oga|ogv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OGG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(one)` AND the `filetype` log field value does NOT match the regular expression `(?i)(none)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ONE_NOTE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pst|ost)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OUTLOOK`.  
Else, if the log message matches the regular expression `(?i)(\\boutlook\\b)` AND the `filetype` log field value matches the regular expression `(?i)(msg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OUTLOOK`.  
Else, if the log message matches the regular expression `(?i)(\\bemail\\b)` AND the `filetype` log field value matches the regular expression `(?i)(msg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_EMAIL_TYPE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(prc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PALMOS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pdb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PDB`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pem)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PEM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pgp|gpg|asc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PGP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(php)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PHP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pkg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PKG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ps1|psm1)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_POWERSHELL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ppsx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PPSX`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(psd)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PSD`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ps)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pyc)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYC`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(py|pyw)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYTHON`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(whl)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PYTHON_WHL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(qt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_QUICKTIME`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rm|rmvb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rom|bin)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ROM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rpm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RPM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rtf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RTF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RUBY`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(rz)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_RZIP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(7z)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SEVENZIP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(sgml|sgm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SGML`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(bash|csh|zsh)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SHELLSCRIPT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(sql)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SQL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(sqfs|sfs)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SQUASHFS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(svg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SVG`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(swf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SWF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(sis|sisx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SYMBIAN`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(3gp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_T3GP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(tar)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TAR`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(tga)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TARGA`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(3ds|max)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_THREEDS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(tif|tiff)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TIFF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(torrent)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TORRENT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(ttf)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TTF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(vba)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_VBA`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(vhd|vhdx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_VHD`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(wav)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WAV`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(webm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WEBM`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(webp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WEBP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(wer)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WER`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(wma)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WMA`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(wmv)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WMV`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(woff|woff2)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WOFF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(xml)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XML`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(xpi)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XPI`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(xwd)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_XWD`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(zst)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZST`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(Makefile|makefile|mk)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MAKEFILE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(zlib)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ZLIB`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(hqx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(hfs|dsk|toast)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH_HFS`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(bh|log|dat)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_BLACKHOLE`.  
Else, if the log message matches the regular expression `(?i)(\\bcookie\\b)` AND the `filetype` log field value matches the regular expression `(?i)(txt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_COOKIE`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(txt)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_TEXT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(docx|xlsx|pptx)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OOXML`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(odt|ods|odp|odg)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_ODF`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(for|f90|f95)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FORTRAN`.  
Else, if the log message matches the regular expression `(?i)(\\bwince\\b)` AND the `filetype` log field value matches the regular expression `(?i)(exe|cab|dll)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_WINCE`.  
Else, if the log message matches the regular expression `(?i)(\\bscript\\b)` AND the `filetype` log field value matches the regular expression `(?i)(py|js|pl|rb)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SCRIPT`.  
Else, if the log message matches the regular expression `(?i)(\\bapplesingle\\b)` AND the `filetype` log field value matches the regular expression `(?i)(as|bin)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLESINGLE`.  
Else, if the log message matches the regular expression `(?i)(\\bmacintosh\\b)` AND the `filetype` log field value matches the regular expression `(?i)(dylib|a)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_MACINTOSH_LIB`.  
Else, if the log message matches the regular expression `(?i)(\\bappledouble\\b)` AND the `filetype` log field value matches the regular expression `(?i)(ad|._)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_APPLEDOUBLE`.  
Else, if the log message matches the regular expression `(?i)(\\bobjetivec\\b)` AND the `filetype` log field value matches the regular expression `(?i)(m|mm|h)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_OBJETIVEC`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(obj|lib)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_COFF`.  
Else, if the log message matches the regular expression `(?i)(\\bcpp\\b)` AND the `filetype` log field value matches the regular expression `(?i)(hpp|cpp|cc|cxx|h)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_CPP`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pas|pp)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PASCAL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)(pl|pm)`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_PERL`.  
Else, if the `filetype` log field value matches the regular expression `(?i)\\bsh\\b`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_SHELLSCRIPT`.  
Else, if the `filetype` log field value matches the regular expression `(?i)\\bc\\b$`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_C`.  
Else, if the `filetype` log field value matches the regular expression `(?i)\\bn\\b$`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_NEKO`.  
Else, if the `filetype` log field value matches the regular expression `(?i)\\bf\\b`, then the `target.file.file_type` UDM field is set to `FILE_TYPE_FORTRAN`.  
Else, the UDM field `additional.fields.key` is set to `filetype` and the log field value `filetype` is mapped to the `additional.fields.value` UDM field, provided the `filetype` value is not empty.  
`extcollab_groups` | `security_result.detection_fields[extcollab_groups]` |   
`intcollab_groups` | `security_result.detection_fields[intcollab_groups]` |   
`oextcollab_groups` | `security_result.detection_fields[oextcollab_groups]` |   
`ointcollab_groups` | `security_result.detection_fields[ointcollab_groups]` |   
`dlpdictcnts` | `security_result.detection_fields[dlpdictcnts]` |   
`attchcomponentmd5s` | `target.file.md5` | If the `attchcomponentmd5s` log field value is _not_ equal to empty and the `attchcomponentmd5s` log field value matches the regular expression pattern `^[a-fA-F0-9]{32}$`, then the `attchcomponentmd5s` log field is mapped to the `target.file.md5` UDM field.  
  
Else, if the `filemd5` log field value matches the regular expression pattern `^[a-fA-F0-9]{32}$`, then the `filemd5` log field is mapped to the `target.file.md5` UDM field.  
`b64attchcomponentfilenames` | `target.file.names` |   
`b64attchcomponentfiletypes` | `additional.fields[b64attchcomponentfiletypes]` |   
`b64attchcomponentmd5s` | `target.file.md5` | If the `b64attchcomponentmd5s` log field value is _not_ equal to empty and the `b64attchcomponentmd5s` log field value matches the regular expression pattern `^[a-fA-F0-9]{32}$`, then the `b64attchcomponentmd5s` log field is mapped to the `target.file.md5` UDM field.  
  
Else, if the `filemd5` log field value matches the regular expression pattern `^[a-fA-F0-9]{32}$`, then the `filemd5` log field is mapped to the `target.file.md5` UDM field.  
`b64bucketname` | `target.resource.name` |   
`b64collabnames` | `additional.fields[b64collabnames]` |   
`b64department` | `principal.user.department` | If the `dept` log field value is _not_ empty, then the `dept` log field is mapped to the `principal.user.department` UDM field. Else, the `b64department` log field is mapped to the `principal.user.department` UDM field.  
`b64dlpdictnames` | `security_result.detection_fields[b64dlpdictnames]` |   
`b64dlpenginenames` | `security_result.detection_fields[b64dlpenginenames]` |   
`b64external_collabnames` | `additional.fields[b64external_collabnames]` |   
`b64external_recptnames` | `network.email.to` |   
`b64extownername` | `additional.fields[b64extownername]` |   
`b64extrecptnames` | `network.email.to` |   
`b64filename` | `target.file.names` |   
`b64filepath` | `target.file.full_path` | If `b64filepath` is not empty, then the `b64filepath` log field is mapped to the `target.file.full_path` UDM field. Else if `filesource` is not empty, then the `filesource` log field is mapped to the `target.file.full_path` UDM field.  
`b64filesource` | `target.file.full_path` | If `filepath` is not empty, then the `filepath` log field is mapped to the `target.file.full_path` UDM field. Else if `b64filesource` is not empty, then the `b64filesource` log field is mapped to the `target.file.full_path` UDM field.  
`b64fullurl` | `principal.url` | If the `b64fullurl` log field is _not_ empty and the `b64fullurl` log field value is not equal to `Unknown URL`, then the `b64fullurl` log field is mapped to the `principal.url` UDM field.  
`b64hostname` | `target.hostname` | If the `sharedchannel_hostname` log field value is empty and the `osharedchannel_hostname` log field value is empty, then the `b64hostname` log field is mapped to the `target.hostname` UDM field.  
`b64internal_collabnames` | `additional.fields[b64internal_collabnames]` |   
`b64internal_recptnames` | `network.email.to` |   
`b64intrecptnames` | `network.email.to` |   
`b64objectname` | `target.resource.name` |   
`b64owner` | `principal.user.email_addresses` | If the `b64owner` log field value matches the regular expression pattern `(^.*@.*$)`, then the `b64owner` log field is mapped to the `principal.user.email_addresses` UDM field.  
`b64projectname` | `target.resource.attribute.labels[b64projectname]` |   
`b64reponame` | `target.resource.name` |   
`b64rulelabel` | `security_result.rule_name` |   
`b64sender` | `network.email.from` | If the `b64sender` log field value matches the regular expression pattern `(^.*@.*$)`, then the `b64sender` log field is mapped to the `network.email.from` UDM field.  
`b64tenant` | `additional.fields[b64tenant]` |   
`b64threatname` | `security_result.threat_name` |   
`b64intcollab_groups` | `security_result.detection_fields[b64intcollab_groups]` |   
`b64extcollab_groups` | `security_result.detection_fields[b64extcollab_groups]` |   
`eattchcomponentfilenames` | `target.file.names` |   
`eattchcomponentfiletypes` | `additional.fields[eattchcomponentfiletypes]` |   
`ebucketname` | `target.resource.name` |   
`ebucketowner` | `target.resource.attribute.labels[ebucketowner]` |   
`ecollabnames` | `additional.fields[ecollabnames]` |   
`edepartment` | `principal.user.department` | If the `dept` log field value is _not_ empty, then the `dept` log field is mapped to the `principal.user.department` UDM field. Else, the `edepartment` log field is mapped to the `principal.user.department` UDM field.  
`edlpdictnames` | `security_result.detection_fields[edlpdictnames]` |   
`edlpenginenames` | `security_result.detection_fields[edlpenginenames]` |   
`eexternal_collabnames` | `additional.fields[eexternal_collabnames]` |   
`eextownername` | `additional.fields[eextownername]` |   
`eextrecptnames` | `network.email.to` |   
`efilename` | `target.file.names` |   
`efilepath` | `target.file.full_path` | If `efilepath` is not empty, then the `efilepath` log field is mapped to the `target.file.full_path` UDM field. Else if `filesource` is not empty, then the `filesource` log field is mapped to the `target.file.full_path` UDM field.  
`efilesource` | `target.file.full_path` | If `filepath` is not empty, then the `filepath` log field is mapped to the `target.file.full_path` UDM field. Else if `efilesource` is not empty, then the `efilesource` log field is mapped to the `target.file.full_path` UDM field.  
`efullurl` | `principal.url` | If the `efullurl` log field is _not_ empty and the `efullurl` log field value is not equal to `Unknown URL`, then the `efullurl` log field is mapped to the `principal.url` UDM field.  
`ehostname` | `target.hostname` |   
`einternal_collabnames` | `additional.fields[einternal_collabnames]` |   
`eintrecptnames` | `network.email.to` |   
`eobjectname` | `target.resource.name` |   
`eowner` | `principal.user.email_addresses` | If the `eowner` log field value matches the regular expression pattern `(^.*@.*$)`, then the `eowner` log field is mapped to the `principal.user.email_addresses` UDM field.  
`eprojectname` | `target.resource.attribute.labels[eprojectname]` |   
`ereponame` | `target.resource.name` |   
`esender` | `network.email.from` | If the `esender` log field value matches the regular expression pattern `(^.*@.*$)`, then the `esender` log field is mapped to the `network.email.from` UDM field.  
`ethreatname` | `security_result.threat_name` |   
  
## What's next

  * [Data ingestion to Google SecOps](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow)



## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-casb-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
