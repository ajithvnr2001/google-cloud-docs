---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-UpdateScanConfigRequest/
title: Web Security Scanner V1beta API - Class Google::Cloud::WebSecurityScanner::V1beta::UpdateScanConfigRequest (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:14.266785+00:00
---

# Web Security Scanner V1beta API - Class Google::Cloud::WebSecurityScanner::V1beta::UpdateScanConfigRequest (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-UpdateScanConfigRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Web Security Scanner V1beta API - Class Google::Cloud::WebSecurityScanner::V1beta::UpdateScanConfigRequest (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.1  0.13.1  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the Web Security Scanner V1beta API class Google::Cloud::WebSecurityScanner::V1beta::UpdateScanConfigRequest.

Request for the `UpdateScanConfigRequest` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #scan_config
    
    
    def scan_config() -> ::Google::Cloud::WebSecurityScanner::V1beta::ScanConfig

**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::ScanConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ScanConfig)) — Required. The ScanConfig to be updated. The name field must be set to identify the resource to be updated. The values of fields not covered by the mask will be ignored. 



### #scan_config=
    
    
    def scan_config=(value) -> ::Google::Cloud::WebSecurityScanner::V1beta::ScanConfig

**Parameter**

  * **value** ([::Google::Cloud::WebSecurityScanner::V1beta::ScanConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ScanConfig)) — Required. The ScanConfig to be updated. The name field must be set to identify the resource to be updated. The values of fields not covered by the mask will be ignored. 



**Returns**

  * ([::Google::Cloud::WebSecurityScanner::V1beta::ScanConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Cloud-WebSecurityScanner-V1beta-ScanConfig)) — Required. The ScanConfig to be updated. The name field must be set to identify the resource to be updated. The values of fields not covered by the mask will be ignored. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Protobuf-FieldMask)) — Required. The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Protobuf-FieldMask)) — Required. The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-web_security_scanner-v1beta/latest/Google-Protobuf-FieldMask)) — Required. The update mask applies to the resource. For the `FieldMask` definition, see https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
