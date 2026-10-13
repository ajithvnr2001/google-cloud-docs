---
url: https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.iconnectionprofile
title: Interface protos.google.cloud.clouddms.v1.IConnectionProfile (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:27.382387+00:00
---

# Interface protos.google.cloud.clouddms.v1.IConnectionProfile (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/dms/protos.google.cloud.clouddms.v1.iconnectionprofile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.clouddms.v1.IConnectionProfile (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  2.2.2  2.1.2  1.1.0  1.0.5 

Properties of a ConnectionProfile.

## Package

[@google-cloud/dms](https://docs.cloud.google.com/nodejs/docs/reference/dms/latest/overview.html)

## Properties 

### alloydb
    
    
    alloydb?: (google.cloud.clouddms.v1.IAlloyDbConnectionProfile|null);

ConnectionProfile alloydb

### cloudsql
    
    
    cloudsql?: (google.cloud.clouddms.v1.ICloudSqlConnectionProfile|null);

ConnectionProfile cloudsql

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

ConnectionProfile createTime

### displayName
    
    
    displayName?: (string|null);

ConnectionProfile displayName

### error
    
    
    error?: (google.rpc.IStatus|null);

ConnectionProfile error

### labels
    
    
    labels?: ({ [k: string]: string }|null);

ConnectionProfile labels

### mysql
    
    
    mysql?: (google.cloud.clouddms.v1.IMySqlConnectionProfile|null);

ConnectionProfile mysql

### name
    
    
    name?: (string|null);

ConnectionProfile name

### oracle
    
    
    oracle?: (google.cloud.clouddms.v1.IOracleConnectionProfile|null);

ConnectionProfile oracle

### postgresql
    
    
    postgresql?: (google.cloud.clouddms.v1.IPostgreSqlConnectionProfile|null);

ConnectionProfile postgresql

### provider
    
    
    provider?: (google.cloud.clouddms.v1.DatabaseProvider|keyof typeof google.cloud.clouddms.v1.DatabaseProvider|null);

ConnectionProfile provider

### state
    
    
    state?: (google.cloud.clouddms.v1.ConnectionProfile.State|keyof typeof google.cloud.clouddms.v1.ConnectionProfile.State|null);

ConnectionProfile state

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

ConnectionProfile updateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
