---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudfront-changelog/
title: Change log for AWS_CLOUDFRONT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:18:19.002368+00:00
---

# Change log for AWS_CLOUDFRONT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-cloudfront-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_CLOUDFRONT

Date | Changes  
---|---  
2026-04-27 |  Enhancement:  
\- `event.idm.read_only_udm.network.sent_bytes`: Modified grok patterns to parse `sent_bytes` log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.   
2026-03-13 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs_cookie` , `time-taken`, `time-to-first-byte`, and `cribl_pipe` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.referer`: Newly mapped `cs-referer` raw log field with `event.idm.read_only_udm.network.http.referer` UDM field.  
\- `event.idm.read_only_udm.network.http.url_details.query`: Newly mapped `cs-uri-query` raw log field with `event.idm.read_only_udm.network.http.url_details.query` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `cs-user-agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `cs-uri-stem` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `security_result.detection_fields`: Newly mapped `x-forwarded-for` raw log field with `security_result.detection_fields` UDM field.  
Added a conditional check before the already existing mapping of `c-ip` to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
Added a conditional check before the already existing mapping of `x-forwarded-for` to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.   
2025-09-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `time_taken` raw log field to `event.idm.read_only_udm.additional.fields[`time_taken`]` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cdn_request_id` raw log field to `event.idm.read_only_udm.additional.fields[`cdn_request_id`]` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `request_query` raw log field to `event.idm.read_only_udm.additional.fields[`request_query`]` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `url4` raw log field to `event.idm.read_only_udm.additional.fields[`http_host_header`]` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sc-content-type` raw log field to `event.idm.read_only_udm.additional.fields[`sc-content-type`]` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `cs-bytes` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `sc-bytes` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `edge_location` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- Added Grok patterns and conditional logic to handle field extraction from the CSV columns.   
2025-05-22 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2025-05-19 |  Enhancement:  
\- Added support for the SYSLOG logs having repeated fields.  
\- Added a conditional check for `agent` field as it is mapping wrong values to `event.idm.read_only_udm.network.http.user_agent`.   
2025-04-26 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.  
\- Added Support to handle the new format of logs .  
\- event.idm.read_only_udm.additional.fields : Newly mapped `avgrequestTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `htmlType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `responseTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `securityKey` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM Field.  
\- event.idm.read_only_udm.src.port: Newly mapped `srcport` raw log field with `event.idm.read_only_udm.src.port` UDM Field.  
\- event.idm.read_only_udm.security_result.about.resource.name: Newly mapped `encryptionType` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM Field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM Field.  
\- event.idm.read_only_udm.src.ip: Newly mapped `scrip` raw log field with `event.idm.read_only_udm.src.ip` UDM Field.  
\- event.idm.read_only_udm.target.ip : Newly mapped `targetip` raw log field with `event.idm.read_only_udm.target.ip` UDM Field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `targetip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM Field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `tlsvVersion` raw log field with `event.idm.read_only_udm.network.tls.version` UDM Field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `CloudFront-Is-Desktop-Viewer` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `CloudFront-Is-Mobile-Viewer` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `CloudFront-Is-SmartTV-Viewer` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `CloudFront-Is-Tablet-Viewer` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent : Newly mapped `vDetails` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `x-envoy-expected-rq-timeout-ms` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `x-envoy-external-address` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `x-envoy-original-authority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `x-f5-cdn-tls-ja3` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `x-f5-cdn-tls-ja4` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `x-forwarded-proto` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `xc-trusted-source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `ipType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.http.method : Newly Mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM Field.  
\- event.idm.read_only_udm.metadata.product_log_id : Newly Mapped `x-request-id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM Field.  
\- event.idm.read_only_udm.metadata.product_log_id : Newly Mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM Field.  
\- event.idm.read_only_udm.network.http.response_code : Newly Mapped `requestCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM Field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.   
2025-04-25 |  Enhancement:  
\- event.idm.read_only_udm.metadata.additional.fields: Newly mapped `uri_query` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified the Grok pattern to correctly parse the `referral_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field and `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2025-02-26 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Mapped `Bucket` to `target.resource.name`.  
\- Mapped `accountID` to `principal.user.userid`.  
\- Mapped `file` to `target.file.full_path`.  
\- Mapped `region` to `principal.location.country_or_region` and `principal.cloud.availability_zone`.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `service`, `aggregation`, `func`, `requestID`, `lpcltype`, `lpclagg`, `level` and `LoggingEnabled` to `additional.fields`.   
2024-09-05 |  Enhancement:  
\- Modified a Grok pattern to parse new pattern of logs.   
2024-05-27 |  Enhancement:  
\- Added support for JSON format logs.   
2022-05-27 |  Enhancement - Modified the value stored in metadata.product_name to `AWS CloudFront` and metadata.vendor_name to `AMAZON`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
