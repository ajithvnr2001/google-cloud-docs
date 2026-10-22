---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/cli/kf-restage/
title: kf restage \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:30:38.440255+00:00
---

# kf restage  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/cli/kf-restage/

Version 2.3

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
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.3/reference)



Send feedback 

#  kf restage Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf restage` \- Rebuild and redeploy an App without downtime.

### Synopsis
    
    
    kf restage APP_NAME [flags]

### Description

Restaging an App will re-run the latest Build to produce a new container image, and if successful will replace each running instance with the new image.

Instances are replaced one at a time, always ensuring that the desired number of instances are healthy. This property is upheld by running one additional instance of the App and swapping it out for an old instance.

The operation completes once all instances have been replaced.

### Examples
    
    
      kf restage myapp

### Flags

`--async`
    Do not wait for the action to complete on the server before returning.
`-h, --help`
    help for restage

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
