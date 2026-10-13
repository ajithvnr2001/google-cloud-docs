---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig/
title: Connectors V1 API - Class Google::Cloud::Connectors::V1::SslConfig (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:14.426914+00:00
---

# Connectors V1 API - Class Google::Cloud::Connectors::V1::SslConfig (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Cloud::Connectors::V1::SslConfig (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Cloud::Connectors::V1::SslConfig.

SSL Configuration of a connection

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_variables
    
    
    def additional_variables() -> ::Array<::Google::Cloud::Connectors::V1::ConfigVariable>

**Returns**

  * (::Array<[::Google::Cloud::Connectors::V1::ConfigVariable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConfigVariable)>) — Additional SSL related field values 



### #additional_variables=
    
    
    def additional_variables=(value) -> ::Array<::Google::Cloud::Connectors::V1::ConfigVariable>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Connectors::V1::ConfigVariable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConfigVariable)>) — Additional SSL related field values 



**Returns**

  * (::Array<[::Google::Cloud::Connectors::V1::ConfigVariable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-ConfigVariable)>) — Additional SSL related field values 



### #client_cert_type
    
    
    def client_cert_type() -> ::Google::Cloud::Connectors::V1::CertType

**Returns**

  * ([::Google::Cloud::Connectors::V1::CertType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CertType)) — Type of Client Cert (PEM/JKS/.. etc.) 



### #client_cert_type=
    
    
    def client_cert_type=(value) -> ::Google::Cloud::Connectors::V1::CertType

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::CertType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CertType)) — Type of Client Cert (PEM/JKS/.. etc.) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::CertType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CertType)) — Type of Client Cert (PEM/JKS/.. etc.) 



### #client_certificate
    
    
    def client_certificate() -> ::Google::Cloud::Connectors::V1::Secret

**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Client Certificate 



### #client_certificate=
    
    
    def client_certificate=(value) -> ::Google::Cloud::Connectors::V1::Secret

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Client Certificate 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Client Certificate 



### #client_private_key
    
    
    def client_private_key() -> ::Google::Cloud::Connectors::V1::Secret

**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Client Private Key 



### #client_private_key=
    
    
    def client_private_key=(value) -> ::Google::Cloud::Connectors::V1::Secret

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Client Private Key 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Client Private Key 



### #client_private_key_pass
    
    
    def client_private_key_pass() -> ::Google::Cloud::Connectors::V1::Secret

**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Secret containing the passphrase protecting the Client Private Key 



### #client_private_key_pass=
    
    
    def client_private_key_pass=(value) -> ::Google::Cloud::Connectors::V1::Secret

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Secret containing the passphrase protecting the Client Private Key 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Secret containing the passphrase protecting the Client Private Key 



### #private_server_certificate
    
    
    def private_server_certificate() -> ::Google::Cloud::Connectors::V1::Secret

**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Private Server Certificate. Needs to be specified if trust model is `PRIVATE`. 



### #private_server_certificate=
    
    
    def private_server_certificate=(value) -> ::Google::Cloud::Connectors::V1::Secret

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Private Server Certificate. Needs to be specified if trust model is `PRIVATE`. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Private Server Certificate. Needs to be specified if trust model is `PRIVATE`. 



### #server_cert_type
    
    
    def server_cert_type() -> ::Google::Cloud::Connectors::V1::CertType

**Returns**

  * ([::Google::Cloud::Connectors::V1::CertType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CertType)) — Type of Server Cert (PEM/JKS/.. etc.) 



### #server_cert_type=
    
    
    def server_cert_type=(value) -> ::Google::Cloud::Connectors::V1::CertType

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::CertType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CertType)) — Type of Server Cert (PEM/JKS/.. etc.) 



**Returns**

  * ([::Google::Cloud::Connectors::V1::CertType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-CertType)) — Type of Server Cert (PEM/JKS/.. etc.) 



### #trust_model
    
    
    def trust_model() -> ::Google::Cloud::Connectors::V1::SslConfig::TrustModel

**Returns**

  * ([::Google::Cloud::Connectors::V1::SslConfig::TrustModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig-TrustModel)) — Trust Model of the SSL connection 



### #trust_model=
    
    
    def trust_model=(value) -> ::Google::Cloud::Connectors::V1::SslConfig::TrustModel

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::SslConfig::TrustModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig-TrustModel)) — Trust Model of the SSL connection 



**Returns**

  * ([::Google::Cloud::Connectors::V1::SslConfig::TrustModel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslConfig-TrustModel)) — Trust Model of the SSL connection 



### #type
    
    
    def type() -> ::Google::Cloud::Connectors::V1::SslType

**Returns**

  * ([::Google::Cloud::Connectors::V1::SslType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslType)) — Controls the ssl type for the given connector version. 



### #type=
    
    
    def type=(value) -> ::Google::Cloud::Connectors::V1::SslType

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::SslType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslType)) — Controls the ssl type for the given connector version. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::SslType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-SslType)) — Controls the ssl type for the given connector version. 



### #use_ssl
    
    
    def use_ssl() -> ::Boolean

**Returns**

  * (::Boolean) — Bool for enabling SSL 



### #use_ssl=
    
    
    def use_ssl=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Bool for enabling SSL 



**Returns**

  * (::Boolean) — Bool for enabling SSL 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
