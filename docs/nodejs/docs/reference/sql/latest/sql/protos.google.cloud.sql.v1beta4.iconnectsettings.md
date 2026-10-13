---
url: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.iconnectsettings
title: Interface protos.google.cloud.sql.v1beta4.IConnectSettings (0.29.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:49.584538+00:00
---

# Interface protos.google.cloud.sql.v1beta4.IConnectSettings (0.29.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/sql/protos.google.cloud.sql.v1beta4.iconnectsettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.sql.v1beta4.IConnectSettings (0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.25.0  0.23.0  0.19.1  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.4.0 

Properties of a ConnectSettings.

## Package

[@google-cloud/sql](https://docs.cloud.google.com/nodejs/docs/reference/sql/latest/overview.html)

## Properties 

### backendType
    
    
    backendType?: (google.cloud.sql.v1beta4.SqlBackendType|keyof typeof google.cloud.sql.v1beta4.SqlBackendType|null);

ConnectSettings backendType

### connectionName
    
    
    connectionName?: (string|null);

ConnectSettings connectionName

### customSubjectAlternativeNames
    
    
    customSubjectAlternativeNames?: (string[]|null);

ConnectSettings customSubjectAlternativeNames

### databaseVersion
    
    
    databaseVersion?: (google.cloud.sql.v1beta4.SqlDatabaseVersion|keyof typeof google.cloud.sql.v1beta4.SqlDatabaseVersion|null);

ConnectSettings databaseVersion

### dnsName
    
    
    dnsName?: (string|null);

ConnectSettings dnsName

### dnsNames
    
    
    dnsNames?: (google.cloud.sql.v1beta4.IDnsNameMapping[]|null);

ConnectSettings dnsNames

### ipAddresses
    
    
    ipAddresses?: (google.cloud.sql.v1beta4.IIpMapping[]|null);

ConnectSettings ipAddresses

### kind
    
    
    kind?: (string|null);

ConnectSettings kind

### mdxProtocolSupport
    
    
    mdxProtocolSupport?: (google.cloud.sql.v1beta4.ConnectSettings.MdxProtocolSupport[]|null);

ConnectSettings mdxProtocolSupport

### nodeCount
    
    
    nodeCount?: (number|null);

ConnectSettings nodeCount

### nodes
    
    
    nodes?: (google.cloud.sql.v1beta4.ConnectSettings.IConnectPoolNodeConfig[]|null);

ConnectSettings nodes

### pscEnabled
    
    
    pscEnabled?: (boolean|null);

ConnectSettings pscEnabled

### region
    
    
    region?: (string|null);

ConnectSettings region

### serverCaCert
    
    
    serverCaCert?: (google.cloud.sql.v1beta4.ISslCert|null);

ConnectSettings serverCaCert

### serverCaMode
    
    
    serverCaMode?: (google.cloud.sql.v1beta4.ConnectSettings.CaMode|keyof typeof google.cloud.sql.v1beta4.ConnectSettings.CaMode|null);

ConnectSettings serverCaMode

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
