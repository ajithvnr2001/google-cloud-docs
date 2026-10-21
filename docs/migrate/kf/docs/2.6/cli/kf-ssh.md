---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/cli/kf-ssh/
title: kf ssh \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:27:25.407451+00:00
---

# kf ssh  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/cli/kf-ssh/

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

#  kf ssh Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf ssh` \- Open a shell on an App instance.

### Synopsis
    
    
    kf ssh APP_NAME [flags]

### Description

Opens a shell on an App instance using the Pod exec endpoint.

This command mimics CF's SSH command by opening a connection to the Kubernetes control plane which spawns a process in a Pod.

The command connects to an arbitrary Pod that matches the App's runtime labels. If you want a specific Pod, use the pod/ notation.

NOTE: Traffic is encrypted between the CLI and the control plane, and between the control plane and Pod. A malicious Kubernetes control plane could observe the traffic.

### Examples
    
    
    # Open a shell to a specific App
    kf ssh myapp
    
    # Open a shell to a specific Pod
    kf ssh pod/myapp-revhex-podhex
    
    # Start a different command with args
    kf ssh myapp -c /my/command -c arg1 -c arg2
    

### Flags

`-c, --command=stringArray`
    

Command to run for the shell. Subsequent definitions will be used as args. (default [/bin/bash])

`--container=string`
    

Container to start the command in. (default "user-container")

`-T, --disable-pseudo-tty`
    

Don't use a TTY when executing.

`-h, --help`
    

help for ssh

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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
