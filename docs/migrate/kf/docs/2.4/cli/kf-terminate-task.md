---
url: https://docs.cloud.google.com/migrate/kf/docs/2.4/cli/kf-terminate-task/
title: kf terminate-task \u00a0|\u00a0 Kf 2.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:30:23.143430+00:00
---

# kf terminate-task  |  Kf 2.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.4/cli/kf-terminate-task/

Version 2.4

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
  * [ 2.4 ](https://docs.cloud.google.com/migrate/kf/docs/2.4)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.4/reference)



Send feedback 

#  kf terminate-task Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf terminate-task` \- Terminate a running Task.

### Synopsis
    
    
    kf terminate-task {TASK_NAME | APP_NAME TASK_ID} [flags]

### Description

Allows operators to terminate a running Task on an App.

### Examples
    
    
    # Terminate Task by Task name
    kf terminate-task my-task-name
    
    # Terminate Task by App name and Task ID
    kf terminate-task my-app 1
    

### Flags

`--async`
    

Do not wait for the action to complete on the server before returning.

`-h, --help`
    

help for terminate-task

`--retries=int`
    

Number of times to retry execution if the command isn't successful. (default 5)

`--retry-delay=duration`
    

Set the delay between retries. (default 1s)

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
