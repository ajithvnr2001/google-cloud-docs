---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/cli/kf-run-task/
title: kf run-task \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:54.825435+00:00
---

# kf run-task  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/cli/kf-run-task/

Version 2.7

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
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.7/reference)



Send feedback 

#  kf run-task Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf run-task` \- Run a short-lived Task on the App.

### Synopsis
    
    
    kf run-task APP_NAME [flags]

### Description

The run-task sub-command lets operators run a short-lived Task on the App.

### Examples
    
    
    kf run-task my-app --command "sleep 100" --name my-task

### Flags

`-c, --command=string`
    

Command to execute on the Task.

`--cpu-cores=string`
    

Amount of dedicated CPU cores to give the Task (for example 256M, 1024M, 1G).

`-k, --disk-quota=string`
    

Amount of dedicated disk space to give the Task (for example 256M, 1024M, 1G).

`-h, --help`
    

help for run-task

`-m, --memory-limit=string`
    

Amount of dedicated memory to give the Task (for example 256M, 1024M, 1G).

`--name=string`
    

Display name to give the Task (auto generated if omitted).

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
