---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/cli/kf-migrate-scan-cf-cluster/
title: kf migrate scan-cf-cluster \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:24.276156+00:00
---

# kf migrate scan-cf-cluster  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/cli/kf-migrate-scan-cf-cluster/

Version 2.6

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.6/reference)



Send feedback 

#  kf migrate scan-cf-cluster Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf migrate scan-cf-cluster` \- Reports migration readiness of a CF cluster.

### Synopsis
    
    
    kf migrate scan-cf-cluster REPORT_NAME.(xlsx|txt) [flags]

### Description

This tool is intended to be used by Cloud Foundry operators to provide a picture about the portability of their foundation to other platforms.

It does this by using the local cf CLI to read information about a cluster.

**Requirements**

  * The `cf` CLI to be on your path
  * The `cf` CLI to be authenticated to and targeting the cluster to scan
  * The `cf` CLI to be logged in with administrator permissions



**Reading the report**

The report does not contain all the information retrieved from the API, instead it targets specific pieces of data that can be used to estimate portability to Kubernetes.

While the tool does its best to obfuscate or skip processing any known fields that might contain sensitive data, you should read through the report before sending it off. For example, URIs might contain usernames, passwords, or keys.

### Examples
    
    
    # Validate the cluster to be targeted
    cf curl /v2/info
    
    # Run the command and get XLSX results (recommended)
    kf migrate scan-cf-cluster report.xlsx
    
    # Run the command and get text results
    kf migrate scan-cf-cluster report.txt

### Flags

`-h, --help`
    

help for scan-cf-cluster

### Inherited flags

These flags are inherited from parent commands.

`--as=string`
    

Username to impersonate for the operation.

`--as-group=strings`
    

Group to impersonate for the operation. Include this flag multiple times to specify multiple groups.

`--config=string`
    

Path to the Kf config file to use for CLI requests.

`--kubeconfig=string`
    

Path to the kubeconfig file to use for CLI requests.

`--log-http`
    

Log HTTP requests to standard error.

`--space=string`
    

Space to run the command against. This flag overrides the currently targeted Space.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
