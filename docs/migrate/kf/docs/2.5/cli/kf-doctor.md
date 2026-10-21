---
url: https://docs.cloud.google.com/migrate/kf/docs/2.5/cli/kf-doctor/
title: kf doctor \u00a0|\u00a0 Kf 2.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:08:15.859980+00:00
---

# kf doctor  |  Kf 2.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.5/cli/kf-doctor/

Version 2.5

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
  * [ 2.5 ](https://docs.cloud.google.com/migrate/kf/docs/2.5)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.5/reference)



Send feedback 

#  kf doctor Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf doctor` \- Run validation tests against one or more components.

### Synopsis
    
    
    kf doctor [(COMPONENT|TYPE/NAME)...] [flags]

### Description

Doctor runs tests on one or more components or objects to validate their desired status.

If no arguments are supplied, then all component tests are ran. If one or more arguments are suplied then only the test for those components or objects are ran.

Possible components are:

  * cluster
  * istio



Possible object types are:

  * app
  * build
  * clusterservicebroker
  * route
  * servicebroker
  * serviceinstance
  * serviceinstancebinding
  * sourcepackage
  * space
  * task



### Examples
    
    
    # Run doctor against all components.
    kf doctor
    # Run doctor against server-side components.
    kf doctor cluster
    # Run doctor for a Kf App named my-app.
    kf doctor app/my-app
    # Run doctor for a Kf Service named my-service.
    kf doctor serviceinstance/my-service
    # Run doctor for a Kf Binding named my-binding.
    kf doctor serviceinstancebinding/my-binding
    # Run doctor for the Kf Operator.
    kf doctor operator
    

### Flags

`--delay=duration`
    

Set the delay between executions. (default 5s)

`-h, --help`
    

help for doctor

`--retries=int`
    

Number of times to retry doctor if it isn't successful. (default 1)

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
