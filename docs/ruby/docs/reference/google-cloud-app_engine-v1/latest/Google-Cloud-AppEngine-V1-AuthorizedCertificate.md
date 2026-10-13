---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthorizedCertificate/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::AuthorizedCertificate (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:36:15.689282+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::AuthorizedCertificate (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthorizedCertificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::AuthorizedCertificate (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::AuthorizedCertificate.

An SSL certificate that a user has been authorized to administer. A user is authorized to administer any certificate that applies to one of their authorized domains.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #certificate_raw_data
    
    
    def certificate_raw_data() -> ::Google::Cloud::AppEngine::V1::CertificateRawData

**Returns**

  * ([::Google::Cloud::AppEngine::V1::CertificateRawData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CertificateRawData)) — The SSL certificate serving the `AuthorizedCertificate` resource. This must be obtained independently from a certificate authority. 



### #certificate_raw_data=
    
    
    def certificate_raw_data=(value) -> ::Google::Cloud::AppEngine::V1::CertificateRawData

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::CertificateRawData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CertificateRawData)) — The SSL certificate serving the `AuthorizedCertificate` resource. This must be obtained independently from a certificate authority. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::CertificateRawData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CertificateRawData)) — The SSL certificate serving the `AuthorizedCertificate` resource. This must be obtained independently from a certificate authority. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — The user-specified display name of the certificate. This is not guaranteed to be unique. Example: `My Certificate`. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The user-specified display name of the certificate. This is not guaranteed to be unique. Example: `My Certificate`. 



**Returns**

  * (::String) — The user-specified display name of the certificate. This is not guaranteed to be unique. Example: `My Certificate`. 



### #domain_mappings_count
    
    
    def domain_mappings_count() -> ::Integer

**Returns**

  * (::Integer) — Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have `VIEWER` permissions.

Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option. 




### #domain_mappings_count=
    
    
    def domain_mappings_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have `VIEWER` permissions.

Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option. 




**Returns**

  * (::Integer) — Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have `VIEWER` permissions.

Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option. 




### #domain_names
    
    
    def domain_names() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: `example.com`. 



### #domain_names=
    
    
    def domain_names=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: `example.com`. 



**Returns**

  * (::Array<::String>) — Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: `example.com`. 



### #expire_time
    
    
    def expire_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using [`AuthorizedCertificates.UpdateAuthorizedCertificate`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthorizedCertificate/). 



### #expire_time=
    
    
    def expire_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using [`AuthorizedCertificates.UpdateAuthorizedCertificate`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthorizedCertificate/). 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-Timestamp)) — The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using [`AuthorizedCertificates.UpdateAuthorizedCertificate`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-AuthorizedCertificate/). 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Relative name of the certificate. This is a unique value autogenerated on `AuthorizedCertificate` resource creation. Example: `12345`. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Relative name of the certificate. This is a unique value autogenerated on `AuthorizedCertificate` resource creation. Example: `12345`. 



**Returns**

  * (::String) — Relative name of the certificate. This is a unique value autogenerated on `AuthorizedCertificate` resource creation. Example: `12345`. 



### #managed_certificate
    
    
    def managed_certificate() -> ::Google::Cloud::AppEngine::V1::ManagedCertificate

**Returns**

  * ([::Google::Cloud::AppEngine::V1::ManagedCertificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ManagedCertificate)) — Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a `DomainMapping` and cannot be updated or deleted via the `AuthorizedCertificates` API. If this certificate is manually administered by the user, this field will be empty. 



### #managed_certificate=
    
    
    def managed_certificate=(value) -> ::Google::Cloud::AppEngine::V1::ManagedCertificate

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::ManagedCertificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ManagedCertificate)) — Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a `DomainMapping` and cannot be updated or deleted via the `AuthorizedCertificates` API. If this certificate is manually administered by the user, this field will be empty. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::ManagedCertificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ManagedCertificate)) — Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a `DomainMapping` and cannot be updated or deleted via the `AuthorizedCertificates` API. If this certificate is manually administered by the user, this field will be empty. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Full path to the `AuthorizedCertificate` resource in the API. Example: `apps/myapp/authorizedCertificates/12345`. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Full path to the `AuthorizedCertificate` resource in the API. Example: `apps/myapp/authorizedCertificates/12345`. 



**Returns**

  * (::String) — Full path to the `AuthorizedCertificate` resource in the API. Example: `apps/myapp/authorizedCertificates/12345`. 



### #visible_domain_mappings
    
    
    def visible_domain_mappings() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: `apps/myapp/domainMappings/example.com`.

This may not represent the full list of mapped domain mappings if the user does not have `VIEWER` permissions on all of the applications that have this certificate mapped. See `domain_mappings_count` for a complete count.

Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option. 




### #visible_domain_mappings=
    
    
    def visible_domain_mappings=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: `apps/myapp/domainMappings/example.com`.

This may not represent the full list of mapped domain mappings if the user does not have `VIEWER` permissions on all of the applications that have this certificate mapped. See `domain_mappings_count` for a complete count.

Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option. 




**Returns**

  * (::Array<::String>) — The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: `apps/myapp/domainMappings/example.com`.

This may not represent the full list of mapped domain mappings if the user does not have `VIEWER` permissions on all of the applications that have this certificate mapped. See `domain_mappings_count` for a complete count.

Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
