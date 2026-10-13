---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-RevocationReason/
title: Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::RevocationReason (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:55.623666+00:00
---

# Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::RevocationReason (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-RevocationReason/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::RevocationReason (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.1  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.6 

Reference documentation and code samples for the Certificate Authority Service V1 API module Google::Cloud::Security::PrivateCA::V1::RevocationReason.

A [RevocationReason](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-RevocationReason "Google::Cloud::Security::PrivateCA::V1::RevocationReason \(module\)") indicates whether a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") has been revoked, and the reason for revocation. These correspond to standard revocation reasons from RFC 5280. Note that the enum labels and values in this definition are not the same ASN.1 values defined in RFC 5280. These values will be translated to the correct ASN.1 values when a CRL is created.

## Constants 

### REVOCATION_REASON_UNSPECIFIED

**value:** 0  
Default unspecified value. This value does indicate that a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") has been revoked, but that a reason has not been recorded.

### KEY_COMPROMISE

**value:** 1  
Key material for this [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") may have leaked.

### CERTIFICATE_AUTHORITY_COMPROMISE

**value:** 2  
The key material for a certificate authority in the issuing path may have leaked.

### AFFILIATION_CHANGED

**value:** 3  
The subject or other attributes in this [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") have changed.

### SUPERSEDED

**value:** 4  
This [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") has been superseded.

### CESSATION_OF_OPERATION

**value:** 5  
This [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") or entities in the issuing path have ceased to operate.

### CERTIFICATE_HOLD

**value:** 6  
This [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") should not be considered valid, it is expected that it may become valid in the future.

### PRIVILEGE_WITHDRAWN

**value:** 7  
This [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") no longer has permission to assert the listed attributes.

### ATTRIBUTE_AUTHORITY_COMPROMISE

**value:** 8  
The authority which determines appropriate attributes for a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)") may have been compromised.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
