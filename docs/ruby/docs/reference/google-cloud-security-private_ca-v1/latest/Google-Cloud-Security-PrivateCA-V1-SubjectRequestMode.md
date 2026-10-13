---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectRequestMode/
title: Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::SubjectRequestMode (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:49.010082+00:00
---

# Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::SubjectRequestMode (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectRequestMode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::SubjectRequestMode (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.1  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.6 

Reference documentation and code samples for the Certificate Authority Service V1 API module Google::Cloud::Security::PrivateCA::V1::SubjectRequestMode.

Describes the way in which a [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)")'s [Subject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Subject "Google::Cloud::Security::PrivateCA::V1::Subject \(class\)") and/or [SubjectAltNames](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectAltNames "Google::Cloud::Security::PrivateCA::V1::SubjectAltNames \(class\)") will be resolved.

## Constants 

### SUBJECT_REQUEST_MODE_UNSPECIFIED

**value:** 0  
Not specified.

### DEFAULT

**value:** 1  
The default mode used in most cases. Indicates that the certificate's [Subject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Subject "Google::Cloud::Security::PrivateCA::V1::Subject \(class\)") and/or [SubjectAltNames](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectAltNames "Google::Cloud::Security::PrivateCA::V1::SubjectAltNames \(class\)") are specified in the certificate request. This mode requires the caller to have the `privateca.certificates.create` permission.

### RDN_SEQUENCE

**value:** 3  
A mode used to get an accurate representation of the Subject field's distinguished name. Indicates that the certificate's [Subject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Subject "Google::Cloud::Security::PrivateCA::V1::Subject \(class\)") and/or [SubjectAltNames](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectAltNames "Google::Cloud::Security::PrivateCA::V1::SubjectAltNames \(class\)") are specified in the certificate request. When parsing a PEM CSR this mode will maintain the sequence of RDNs found in the CSR's subject field in the issued [Certificate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Certificate "Google::Cloud::Security::PrivateCA::V1::Certificate \(class\)"). This mode requires the caller to have the `privateca.certificates.create` permission.

### REFLECTED_SPIFFE

**value:** 2  
A mode reserved for special cases. Indicates that the certificate should have one SPIFFE [SubjectAltNames](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectAltNames "Google::Cloud::Security::PrivateCA::V1::SubjectAltNames \(class\)") set by the service based on the caller's identity. This mode will ignore any explicitly specified [Subject](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-Subject "Google::Cloud::Security::PrivateCA::V1::Subject \(class\)") and/or [SubjectAltNames](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-SubjectAltNames "Google::Cloud::Security::PrivateCA::V1::SubjectAltNames \(class\)") in the certificate request. This mode requires the caller to have the `privateca.certificates.createForSelf` permission.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
