---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-DnsSettings-DsRecord-Algorithm/
title: Cloud Domains V1 API - Module Google::Cloud::Domains::V1::DnsSettings::DsRecord::Algorithm (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:41.846520+00:00
---

# Cloud Domains V1 API - Module Google::Cloud::Domains::V1::DnsSettings::DsRecord::Algorithm (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-domains-v1/latest/Google-Cloud-Domains-V1-DnsSettings-DsRecord-Algorithm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Domains V1 API - Module Google::Cloud::Domains::V1::DnsSettings::DsRecord::Algorithm (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Domains V1 API module Google::Cloud::Domains::V1::DnsSettings::DsRecord::Algorithm.

List of algorithms used to create a DNSKEY. Certain algorithms are not supported for particular domains.

## Constants 

### ALGORITHM_UNSPECIFIED

**value:** 0  
The algorithm is unspecified.

### RSAMD5

**value:** 1  
RSA/MD5. Cannot be used for new deployments.

### DH

**value:** 2  
Diffie-Hellman. Cannot be used for new deployments.

### DSA

**value:** 3  
DSA/SHA1. Not recommended for new deployments.

### ECC

**value:** 4  
ECC. Not recommended for new deployments.

### RSASHA1

**value:** 5  
RSA/SHA-1. Not recommended for new deployments.

### DSANSEC3SHA1

**value:** 6  
DSA-NSEC3-SHA1. Not recommended for new deployments.

### RSASHA1NSEC3SHA1

**value:** 7  
RSA/SHA1-NSEC3-SHA1. Not recommended for new deployments.

### RSASHA256

**value:** 8  
RSA/SHA-256.

### RSASHA512

**value:** 10  
RSA/SHA-512.

### ECCGOST

**value:** 12  
GOST R 34.10-2001.

### ECDSAP256SHA256

**value:** 13  
ECDSA Curve P-256 with SHA-256.

### ECDSAP384SHA384

**value:** 14  
ECDSA Curve P-384 with SHA-384.

### ED25519

**value:** 15  
Ed25519.

### ED448

**value:** 16  
Ed448.

### INDIRECT

**value:** 252  
Reserved for Indirect Keys. Cannot be used for new deployments.

### PRIVATEDNS

**value:** 253  
Private algorithm. Cannot be used for new deployments.

### PRIVATEOID

**value:** 254  
Private algorithm OID. Cannot be used for new deployments.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
