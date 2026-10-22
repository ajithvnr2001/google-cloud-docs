---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-tunnel/
title: Collect Zscaler Tunnel logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:55.761799+00:00
---

# Collect Zscaler Tunnel logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-tunnel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect Zscaler Tunnel logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how to export Zscaler Tunnel logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.

For more information, see [Data ingestion to Google SecOps overview](https://docs.cloud.google.com/chronicle/docs/data-ingestion-flow).

A typical deployment consists of Zscaler Tunnel and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.

The deployment contains the following components:

  * **Zscaler Tunnel** : The platform from which you collect logs.

  * **Google SecOps feed** : The Google SecOps feed that fetches logs from Zscaler Tunnel and writes logs to Google SecOps.

  * **Google SecOps** : Retains and analyzes the logs.




An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the `ZSCALER_TUNNEL` label.

## Before you begin

Ensure you have the following prerequisites:

  * Access to Zscaler Internet Access console. For more information, see [Secure Internet and SaaS Access ZIA Help](https://help.zscaler.com/zia/getting-started).
  * Zscaler Tunnel version 1.0 or version 2.0
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

## Set up Zscaler Tunnel

  1. In Zscaler Internet Access console, go to **Administration > Nanolog Streaming Service > Cloud NSS Feeds**.
  2. Click **Add Cloud NSS Feed**.
  3. Enter a name for the feed in the **Feed Name** field.
  4. Select **NSS for Tunnel** in **NSS Type**.
  5. Select the status from the **Status** list to activate or deactivate the NSS feed.
  6. Keep the value in the **SIEM Rate** drop-down as **Unlimited**. To suppress the output stream due to licensing or other constraints, change the value.
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
  12. Select **Tunnel** in the **Log Types** list.

  13. Select **JSON** in the **Feed Output Type** list.

  14. Disable **JSON Array Notation**.

  15. Set **Feed Escape Character** to `, \ "`.

  16. To add a new field to the **Feed Output Format,** select **Custom** in the **Feed Output Type** list.

  17. Copy-paste the **Feed Output Format** and add new fields. Ensure the key names match the actual field names.

The following are the default **Feed Output Formats** :

     * For IKE Phase 1:
           
           \{ "sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"IPSEC IKEV %d{ikeversion}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","destinationport":"%d{dstport}","lifetime":"%d{lifetime}","ikeversion":"%d{ikeversion}","spi_in":"%lu{spi_in}","spi_out":"%lu{spi_out}","algo":"%s{algo}","authentication":"%s{authentication}","authtype":"%s{authtype}","recordid":"%d{recordid}"\}\}
           

     * For IKE Phase 2:
           
           \{ "sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"IPSEC IKEV %d{ikeversion}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","sourceportstart":"%d{srcportstart}","destinationportstart":"%d{destportstart}","srcipstart":"%s{srcipstart}","srcipend":"%s{srcipend}","destinationipstart":"%s{destipstart}","destinationipend":"%s{destipend}","lifetime":"%d{lifetime}","ikeversion":"%d{ikeversion}","lifebytes":"%d{lifebytes}","spi":"%d{spi}","algo":"%s{algo}","authentication":"%s{authentication}","authtype":"%s{authtype}","protocol":"%s{protocol}","tunnelprotocol":"%s{tunnelprotocol}","policydirection":"%s{policydirection}","recordid":"%d{recordid}"\}\}
           

     * For Tunnel Event:
           
           \{ "sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"%s{tunneltype}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","event":"%s{event}","eventreason":"%s{eventreason}","recordid":"%d{recordid}"\}\}
           

     * For Sample:
           
           \{ "sourcetype" : "zscalernss-tunnel", "event" : \{"datetime":"%s{datetime}","Recordtype":"%s{tunnelactionname}","tunneltype":"%s{tunneltype}","user":"%s{vpncredentialname}","location":"%s{elocationname}","sourceip":"%s{sourceip}","destinationip":"%s{destvip}","sourceport":"%d{srcport}","txbytes":"%lu{txbytes}","rxbytes":"%lu{rxbytes}","dpdrec":"%d{dpdrec}","recordid":"%d{recordid}"\}\}
           

  18. Select the time zone for the **Time** field in the output file in the **Timezone** list. By default, the time zone is set to your organization's time zone.

  19. Review the configured settings.

  20. Click **Save** to test connectivity. If the connection is successful, a green tick accompanied by the message **Test Connectivity Successful: OK (200)** appears.




For more information about Google SecOps feeds, see [Google SecOps feeds documentation](https://docs.cloud.google.com/chronicle/docs/administration/feed-management). For information about requirements for each feed type, see [Feed configuration by type](https://docs.cloud.google.com/chronicle/docs/reference/feed-management-api#feed_configuration_by_type).

If you encounter issues when you create feeds, contact [Google SecOps support](https://docs.cloud.google.com/chronicle/docs/support).

## Supported Zscaler Tunnel log formats

The Zscaler Tunnel parser supports logs in JSON format.

## Supported Zscaler Tunnel sample logs

  * JSON
        
        {
          "sourcetype": "zscalernss-tunnel",
          "event": {
            "datetime": "Sun Jan 21 06:17:00 2024",
            "Recordtype": "Tunnel Samples",
            "tunneltype": "IPSec IKEv2",
            "user": "dummy-user@dummydomain.net",
            "location": "PLWSE06",
            "sourceip": "198.51.100.0",
            "destinationip": "198.51.100.1",
            "sourceport": "0",
            "txbytes": "12560",
            "rxbytes": "0",
            "dpdrec": "0",
            "recordid": "7326416289073594372"
          }
        }
        




## UDM Mapping Table

### Field mapping reference: ZSCALER_TUNNEL 

The following table lists the log fields of the `ZSCALER_TUNNEL` log type and their corresponding UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`algo` | `additional.fields[algo]` |   
`authtype` | `additional.fields[authtype]` |   
`authentication` | `additional.fields[authentication]` |   
`dd` | `additional.fields[dd]` |   
`day` | `additional.fields[day]` |   
`destinationportstart` | `additional.fields[destinationportstart]` |   
`dpdrec` | `additional.fields[dpdrec]` |   
`eventreason` | `additional.fields[eventreason]` |   
`hh` | `additional.fields[hh]` |   
`ikeversion` | `additional.fields[ikeversion]` |   
`lifebytes` | `additional.fields[lifebytes]` |   
`mm` | `additional.fields[mm]` |   
`mon` | `additional.fields[mon]` |   
`mth` | `additional.fields[mth]` |   
`olocationname` | `principal.location.name` |   
`ovpncredentialname` | `principal.user.userid` and `principal.user.email_addresses` if regular expression match `^.+@.+$` |   
`ss` | `additional.fields[ss]` |   
`sourcetype` | `additional.fields[sourcetype]` |   
`spi_in` | `additional.fields[spi_in]` |   
`spi_out` | `additional.fields[spi_out]` |   
`sourceportstart` | `additional.fields[sourceportstart]` |   
`tz` | `additional.fields[tz]` |   
`tunnelprotocol` | `additional.fields[tunnelprotocol]` |   
`tunneltype` | `additional.fields[tunneltype]` |   
`vendorname` | `additional.fields[vendorname]` |   
`yyyy` | `additional.fields[yyyy]` |   
`spi` | `additional.fields[spi]` |   
`event` | `metadata.description` |   
`datetime` | `metadata.event_timestamp` |   
`` | `metadata.event_type` | If (the `srcipstart` log field value is _not_ empty or the `srcipend` log field value is _not_ empty or the `sourceip` log field value is _not_ empty) and (the `destinationipstart` log field value is _not_ empty or the `destinationip` log field value is _not_ empty or the `destinationipend` log field value is _not_ empty), then the `metadata.event_type` UDM field is set to `NETWORK_CONNECTION`.  
  
Else, if the `srcipstart` log field value is _not_ empty or the `srcipend` log field value is _not_ empty or the `sourceip` log field value is _not_ empty, then the `metadata.event_type` UDM field is set to `STATUS_UPDATE`.  
  
Else, the `metadata.event_type` UDM field is set to `GENERIC_EVENT`.  
`Recordtype` | `metadata.product_event_type` |   
`recordid` | `metadata.product_log_id` |   
`` | `metadata.product_name` | The `metadata.product_name` UDM field is set to `ZSCALER_TUNNEL`.  
`` | `metadata.vendor_name` | The `metadata.vendor_name` UDM field is set to `ZSCALER`.  
`` | `network.direction` | If the `policydirection` log field value matches the regular expression pattern `(?i)Inbound`, then the `network.direction` UDM field is set to `INBOUND`.  
  
Else, if the `policydirection` log field value matches the regular expression pattern `(?i)Outbound`, then the `network.direction` UDM field is set to `OUTBOUND`.  
`protocol` | `network.ip_protocol` | If the `protocol` log field value contain one of the following values, then the `protocol` log field is mapped to the `network.ip_protocol` UDM field. 

  * `TCP`
  * `EIGRP`
  * `ESP`
  * `ETHERIP`
  * `GRE`
  * `ICMP`
  * `IGMP`
  * `IP6IN4`
  * `PIM`
  * `UDP`
  * `VRRP`

  
`rxbytes` | `network.received_bytes` |   
`rxpackets` | `network.received_packets` |   
`txbytes` | `network.sent_bytes` |   
`txpackets` | `network.sent_packets` |   
`lifetime` | `network.session_duration.seconds` |   
`srcipstart` | `principal.ip` |   
`sourceip` | `principal.ip` |   
`srcipend` | `principal.ip` |   
`location` | `principal.location.name` |   
`sourceport` | `principal.port` |   
`user` | `principal.user.userid` and `principal.user.email_addresses` if regular expression match `^.+@.+$` |   
`destinationipstart` | `target.ip` |   
`destinationip` | `target.ip` |   
`destinationipend'` | `target.ip` |   
`destinationport` | `target.port` |   
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zscaler-tunnel-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
