---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-KeyUsage-KeyUsageOptions/
title: Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::KeyUsage::KeyUsageOptions (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:34.260528+00:00
---

# Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::KeyUsage::KeyUsageOptions (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-KeyUsage-KeyUsageOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1 API - Class Google::Cloud::Security::PrivateCA::V1::KeyUsage::KeyUsageOptions (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.1  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.6 

Reference documentation and code samples for the Certificate Authority Service V1 API class Google::Cloud::Security::PrivateCA::V1::KeyUsage::KeyUsageOptions.

[KeyUsage.KeyUsageOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-KeyUsage-KeyUsageOptions "Google::Cloud::Security::PrivateCA::V1::KeyUsage::KeyUsageOptions \(class\)") corresponds to the key usage values described in <https://tools.ietf.org/html/rfc5280#section-4.2.1.3>.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cert_sign
    
    
    def cert_sign() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used to sign certificates. 



### #cert_sign=
    
    
    def cert_sign=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used to sign certificates. 



**Returns**

  * (::Boolean) — The key may be used to sign certificates. 



### #content_commitment
    
    
    def content_commitment() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". 



### #content_commitment=
    
    
    def content_commitment=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". 



**Returns**

  * (::Boolean) — The key may be used for cryptographic commitments. Note that this may also be referred to as "non-repudiation". 



### #crl_sign
    
    
    def crl_sign() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used sign certificate revocation lists. 



### #crl_sign=
    
    
    def crl_sign=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used sign certificate revocation lists. 



**Returns**

  * (::Boolean) — The key may be used sign certificate revocation lists. 



### #data_encipherment
    
    
    def data_encipherment() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used to encipher data. 



### #data_encipherment=
    
    
    def data_encipherment=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used to encipher data. 



**Returns**

  * (::Boolean) — The key may be used to encipher data. 



### #decipher_only
    
    
    def decipher_only() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used to decipher only. 



### #decipher_only=
    
    
    def decipher_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used to decipher only. 



**Returns**

  * (::Boolean) — The key may be used to decipher only. 



### #digital_signature
    
    
    def digital_signature() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used for digital signatures. 



### #digital_signature=
    
    
    def digital_signature=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used for digital signatures. 



**Returns**

  * (::Boolean) — The key may be used for digital signatures. 



### #encipher_only
    
    
    def encipher_only() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used to encipher only. 



### #encipher_only=
    
    
    def encipher_only=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used to encipher only. 



**Returns**

  * (::Boolean) — The key may be used to encipher only. 



### #key_agreement
    
    
    def key_agreement() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used in a key agreement protocol. 



### #key_agreement=
    
    
    def key_agreement=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used in a key agreement protocol. 



**Returns**

  * (::Boolean) — The key may be used in a key agreement protocol. 



### #key_encipherment
    
    
    def key_encipherment() -> ::Boolean

**Returns**

  * (::Boolean) — The key may be used to encipher other keys. 



### #key_encipherment=
    
    
    def key_encipherment=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — The key may be used to encipher other keys. 



**Returns**

  * (::Boolean) — The key may be used to encipher other keys. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
