---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.isslcertificate
title: Interface protos.google.backstory.ISSLCertificate (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:11.400041+00:00
---

# Interface protos.google.backstory.ISSLCertificate (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.backstory.isslcertificate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.backstory.ISSLCertificate (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Properties of a SSLCertificate.

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Properties 

### certExtensions
    
    
    certExtensions?: (google.protobuf.IStruct|null);

SSLCertificate certExtensions

### certSignature
    
    
    certSignature?: (google.backstory.SSLCertificate.ICertSignature|null);

SSLCertificate certSignature

### ec
    
    
    ec?: (google.backstory.SSLCertificate.IEC|null);

SSLCertificate ec

### extension
    
    
    extension?: (google.backstory.SSLCertificate.IExtension|null);

SSLCertificate extension

### firstSeenTime
    
    
    firstSeenTime?: (google.protobuf.ITimestamp|null);

SSLCertificate firstSeenTime

### issuer
    
    
    issuer?: (google.backstory.SSLCertificate.ISubject|null);

SSLCertificate issuer

### publicKey
    
    
    publicKey?: (google.backstory.SSLCertificate.IPublicKey|null);

SSLCertificate publicKey

### serialNumber
    
    
    serialNumber?: (string|null);

SSLCertificate serialNumber

### signatureAlgorithm
    
    
    signatureAlgorithm?: (string|null);

SSLCertificate signatureAlgorithm

### size
    
    
    size?: (number|Long|string|null);

SSLCertificate size

### subject
    
    
    subject?: (google.backstory.SSLCertificate.ISubject|null);

SSLCertificate subject

### thumbprint
    
    
    thumbprint?: (string|null);

SSLCertificate thumbprint

### thumbprintSha256
    
    
    thumbprintSha256?: (string|null);

SSLCertificate thumbprintSha256

### validity
    
    
    validity?: (google.backstory.SSLCertificate.IValidity|null);

SSLCertificate validity

### version
    
    
    version?: (string|null);

SSLCertificate version

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
