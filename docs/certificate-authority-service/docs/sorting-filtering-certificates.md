---
url: https://docs.cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates/
title: Sort and filter certificates \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:29:44.402459+00:00
---

# Sort and filter certificates  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/sorting-filtering-certificates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sort and filter certificates

This page describes how you can sort and filter the certificates that are returned by the [`ListCertificates`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/list) API call in Certificate Authority Service.

For information about listing and viewing issued certificates, see [View issued certificates](https://docs.cloud.google.com/certificate-authority-service/docs/view-issued-certificates).

## Sorting support

By default, the [`ListCertificates`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/list) API call returns the certificates ordered by the [`create_time`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates#Certificate.FIELDS.create_time) field, with the newest certificates being listed first. No other sort order can be specified.

## Filtering support

The following fields can be used for filtering the certificates returned by the [`ListCertificates`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates/list) API call:

Field Name | Field Type | Supported Operators  
---|---|---  
[create_time](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates#Certificate.FIELDS.create_time) | [timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) | `<, >, <=, >=, =, !=`  
[update_time](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates#Certificate.FIELDS.update_time) | [timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) | `<, >, <=, >=, =, !=`  
[certificate_description.subject_description.not_after_time](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#SubjectDescription.FIELDS.not_after_time) | [timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) | `<, >, <=, >=, =, !=`  
[certificate_description.subject_description.not_before_time](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#SubjectDescription.FIELDS.not_before_time) | [timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) | `<, >, <=, >=, =, !=`  
[certificate_description.cert_fingerprint.sha256_hash](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#CertificateFingerprint.FIELDS.sha256_hash) | string | `=, !=`  
[certificate_description.subject_description.hex_serial_number](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/CertificateDescription#SubjectDescription.FIELDS.hex_serial_number) | string | `=, !=`  
[certificate_description.subject_description.subject.common_name](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.common_name) | string | `=, !=`  
[certificate_description.subject_description.subject.country_code](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.country_code) | string | `=, !=`  
[certificate_description.subject_description.subject.organization](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.organization) | string | `=, !=`  
[certificate_description.subject_description.subject.organizational_unit](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.organizational_unit) | string | `=, !=`  
[certificate_description.subject_description.subject.locality](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.locality) | string | `=, !=`  
[certificate_description.subject_description.subject.province](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.province) | string | `=, !=`  
[certificate_description.subject_description.subject.street_address](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.street_address) | string | `=, !=`  
[certificate_description.subject_description.subject.postal_code](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/Subject#FIELDS.postal_code) | string | `=, !=`  
[certificate_description.subject_description.subject_alt_name.dns_names](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/SubjectAltNames#FIELDS.dns_names) | string | [: (HAS operator)](https://google.aip.dev/160#has-operator)  
[certificate_description.x509_description.key_usage.extended_key_usage.client_auth](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#ExtendedKeyUsageOptions.FIELDS.client_auth) | bool | `=, !=`  
[certificate_description.x509_description.key_usage.extended_key_usage.server_auth](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#ExtendedKeyUsageOptions.FIELDS.server_auth) | bool | `=, !=`  
[labels](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates#Certificate.FIELDS.labels) | [map](https://developers.google.com/protocol-buffers/docs/proto3#maps) | [: (HAS operator)](https://google.aip.dev/160#has-operator)  
[certificate_template](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/projects.locations.caPools.certificates#Certificate.FIELDS.certificate_template) | string | `=, !=`, [: (HAS operator)](https://google.aip.dev/160#has-operator)  
  
**Note** : The fields [certificate_description.x509_description.key_usage.extended_key_usage.client_auth](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#ExtendedKeyUsageOptions.FIELDS.client_auth) and [certificate_description.x509_description.key_usage.extended_key_usage.server_auth](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters#ExtendedKeyUsageOptions.FIELDS.server_auth) are booleans that refer to whether the respective Extended Key Usages are present.

### Filtering syntax

The filtering syntax is following the API Filtering guidance set in [AIP 160](https://google.aip.dev/160) with the following limitations:

  * only top level `AND` operators are supported. Everything else is not (for example, `OR`, `NOT`, nested operators, or any combination of these operators).

    * Valid: Filter uses only top level AND operator:
          
          create_time>"2020-08-21T11:30:00.11-05:00" AND certificate_description.x509_description.key_usage.extended_key_usage.server_auth=true
          

    * Invalid: Filter uses OR operator:
          
          create_time>"2020-08-21T11:30:00.11-05:00" OR certificate_description.x509_description.key_usage.extended_key_usage.server_auth=true
          

    * Invalid: Filter uses nested operators:
          
          (create_time>"2020-08-21T11:30:00.11-05:00" AND certificate_description.x509_description.key_usage.extended_key_usage.server_auth=true) AND certificate_description.subject_description.subject.common_name="foo.com"
          

  * wildcard matching (using `*`) is not supported except for the [`certificate_description.subject_description.subject_alt_name.dns_names`](https://docs.cloud.google.com/certificate-authority-service/docs/reference/rest/v1/SubjectAltNames#FIELDS.dns_names) field which supports suffix matching for the DNS labels.

    * Valid: Filter compares a wildcard suffix match:
          
          certificate_description.subject_description.subject_alt_name.dns_names:"*.foo.com"
          

    * Invalid: Filter compares with a wildcard prefix match:
          
          certificate_description.subject_description.subject_alt_name.dns_names:"foo.*"
          

    * Invalid: Filter compares with a wildcard for an unsupported field:
          
          "certificate_description.subject_description.hex_serial_number"="*3d3"
          




## What's next

  * Learn how to [request certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).
  * Learn how to [revoke certificates](https://docs.cloud.google.com/certificate-authority-service/docs/revoking-certificates).
  * See the [REST API reference documentation](https://docs.cloud.google.com/reference/rest).
  * See the [RPC API reference documentation](https://docs.cloud.google.com/reference/rpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
