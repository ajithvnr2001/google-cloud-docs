---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/cli/kf-unbind-route-service/
title: kf unbind-route-service \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:30:36.114368+00:00
---

# kf unbind-route-service  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/cli/kf-unbind-route-service/

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

#  kf unbind-route-service Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf unbind-route-service` \- Unbind a route service instance from an HTTP route.

### Synopsis
    
    
    kf unbind-route-service DOMAIN [--hostname HOSTNAME] [--path PATH] SERVICE_INSTANCE [flags]

### Description

Unbinding a route service from an HTTP route causes requests to go straight to the HTTP route, rather than being processed by the route service first.

### Examples
    
    
      kf unbind-route-service company.com --hostname myapp --path mypath myauthservice

### Flags

`--async`
    Do not wait for the action to complete on the server before returning.
`-h, --help`
    help for unbind-route-service
`--hostname=string`
    Hostname for the Route.
`--path=string`
    URL path for the Route.

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
