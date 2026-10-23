---
url: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-logs/
title: kf logs \u00a0|\u00a0 Kf 2.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:06.235587+00:00
---

# kf logs  |  Kf 2.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-logs/

Version 2.1

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
  * [ 2.1 ](https://docs.cloud.google.com/migrate/kf/docs/2.1)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.1/reference)



Send feedback 

#  kf logs Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf logs` \- Show logs for an App

### Synopsis
    
    
    kf logs APP_NAME [flags]

### Description

Logs are streamed from the Kubernetes log endpoint for each running App instance.

If App instances change or the connection to Kubernetes times out the log stream may show duplicate logs.

Logs are retained for App instances as space permits on the cluster, but will be deleted if space is low or past their retention date. Cloud Logging is a more reliable mechanism to access historical logs.

If you need logs for a particular instance use the` kubectl` CLI.

### Examples
    
    
      # Follow/tail the log stream
      kf logs myapp
      
      # Follow/tail the log stream with 20 lines of context
      kf logs myapp -n 20
      
      # Get recent logs from the App
      kf logs myapp --recent
      
      # Get the most recent 200 lines of logs from the App
      kf logs myapp --recent -n 200

### Flags

`-h, --help`
    help for logs
`-n, --number=int`
    Show the last N lines of logs. (default 10)
`--recent`
    Dump recent logs instead of tailing.

### Inherited flags

These flags are inherited from parent commands.

`--config=string`
    Config file (default is $HOME/.kf)
`--kubeconfig=string`
    Kubectl config file (default is $HOME/.kube/config)
`--log-http`
    Log HTTP requests to stderr
`--space=string`
    Space to run the command against. This overrides the currently targeted space

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
