---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SslCert/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SslCert (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:25.099291+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SslCert (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SslCert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SslCert (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::SslCert.

SslCerts Resource

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #cert
    
    
    def cert() -> ::String

**Returns**

  * (::String) — PEM representation. 



### #cert=
    
    
    def cert=(value) -> ::String

**Parameter**

  * **value** (::String) — PEM representation. 



**Returns**

  * (::String) — PEM representation. 



### #cert_serial_number
    
    
    def cert_serial_number() -> ::String

**Returns**

  * (::String) — Serial number, as extracted from the certificate. 



### #cert_serial_number=
    
    
    def cert_serial_number=(value) -> ::String

**Parameter**

  * **value** (::String) — Serial number, as extracted from the certificate. 



**Returns**

  * (::String) — Serial number, as extracted from the certificate. 



### #common_name
    
    
    def common_name() -> ::String

**Returns**

  * (::String) — User supplied name. Constrained to [a-zA-Z.-_ ]+. 



### #common_name=
    
    
    def common_name=(value) -> ::String

**Parameter**

  * **value** (::String) — User supplied name. Constrained to [a-zA-Z.-_ ]+. 



**Returns**

  * (::String) — User supplied name. Constrained to [a-zA-Z.-_ ]+. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`



### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`



### #expiration_time
    
    
    def expiration_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. 



### #expiration_time=
    
    
    def expiration_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Timestamp)) — The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. 



### #instance
    
    
    def instance() -> ::String

**Returns**

  * (::String) — Name of the database instance. 



### #instance=
    
    
    def instance=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the database instance. 



**Returns**

  * (::String) — Name of the database instance. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — This is always `sql#sslCert`. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — This is always `sql#sslCert`. 



**Returns**

  * (::String) — This is always `sql#sslCert`. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — The URI of this resource. 



### #self_link=
    
    
    def self_link=(value) -> ::String

**Parameter**

  * **value** (::String) — The URI of this resource. 



**Returns**

  * (::String) — The URI of this resource. 



### #sha1_fingerprint
    
    
    def sha1_fingerprint() -> ::String

**Returns**

  * (::String) — Sha1 Fingerprint. 



### #sha1_fingerprint=
    
    
    def sha1_fingerprint=(value) -> ::String

**Parameter**

  * **value** (::String) — Sha1 Fingerprint. 



**Returns**

  * (::String) — Sha1 Fingerprint. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
