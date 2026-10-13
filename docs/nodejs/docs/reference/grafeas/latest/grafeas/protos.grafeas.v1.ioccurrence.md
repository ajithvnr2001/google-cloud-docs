---
url: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.ioccurrence
title: Interface protos.grafeas.v1.IOccurrence (7.0.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:47.173800+00:00
---

# Interface protos.grafeas.v1.IOccurrence (7.0.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/grafeas/protos.grafeas.v1.ioccurrence

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.grafeas.v1.IOccurrence (7.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.0.1 (latest)  6.0.1  5.5.0  4.5.0  4.2.2  4.1.2  3.6.1  3.5.0  3.4.6 

Properties of an Occurrence.

## Package

[@google-cloud/grafeas](https://docs.cloud.google.com/nodejs/docs/reference/grafeas/latest/overview.html)

## Properties 

### attestation
    
    
    attestation?: (grafeas.v1.IAttestationOccurrence|null);

Occurrence attestation

### build
    
    
    build?: (grafeas.v1.IBuildOccurrence|null);

Occurrence build

### compliance
    
    
    compliance?: (grafeas.v1.IComplianceOccurrence|null);

Occurrence compliance

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Occurrence createTime

### deployment
    
    
    deployment?: (grafeas.v1.IDeploymentOccurrence|null);

Occurrence deployment

### discovery
    
    
    discovery?: (grafeas.v1.IDiscoveryOccurrence|null);

Occurrence discovery

### dsseAttestation
    
    
    dsseAttestation?: (grafeas.v1.IDSSEAttestationOccurrence|null);

Occurrence dsseAttestation

### envelope
    
    
    envelope?: (grafeas.v1.IEnvelope|null);

Occurrence envelope

### image
    
    
    image?: (grafeas.v1.IImageOccurrence|null);

Occurrence image

### kind
    
    
    kind?: (grafeas.v1.NoteKind|keyof typeof grafeas.v1.NoteKind|null);

Occurrence kind

### name
    
    
    name?: (string|null);

Occurrence name

### noteName
    
    
    noteName?: (string|null);

Occurrence noteName

### package
    
    
    "package"?: (grafeas.v1.IPackageOccurrence|null);

Occurrence package

### remediation
    
    
    remediation?: (string|null);

Occurrence remediation

### resourceUri
    
    
    resourceUri?: (string|null);

Occurrence resourceUri

### sbomReference
    
    
    sbomReference?: (grafeas.v1.ISBOMReferenceOccurrence|null);

Occurrence sbomReference

### secret
    
    
    secret?: (grafeas.v1.ISecretOccurrence|null);

Occurrence secret

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Occurrence updateTime

### upgrade
    
    
    upgrade?: (grafeas.v1.IUpgradeOccurrence|null);

Occurrence upgrade

### vulnerability
    
    
    vulnerability?: (grafeas.v1.IVulnerabilityOccurrence|null);

Occurrence vulnerability

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
