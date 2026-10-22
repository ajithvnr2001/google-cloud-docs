---
url: https://docs.cloud.google.com/migrate/kf/docs/2.4/cli/kf-unmap-route/
title: kf unmap-route \u00a0|\u00a0 Kf 2.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:30:22.570087+00:00
---

# kf unmap-route  |  Kf 2.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.4/cli/kf-unmap-route/

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

#  kf unmap-route Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf unmap-route` \- Revoke an App's access to receive traffic from the Route.

### Synopsis
    
    
    kf unmap-route APP_NAME DOMAIN [--hostname HOSTNAME] [--path PATH] [flags]

### Description

Unmapping an App from a Route will cause traffic matching the Route to no longer be forwarded to the App.

The App may still receive traffic from an unmapped Route for a small period of time while the traffic rules on the gateways are propagated.

The Route will re-balance its routing weights so other Apps mapped to it will receive the traffic. If no other Apps are bound the Route will return a 404 HTTP status code.

### Examples
    
    
    # Unmap myapp.example.com from myapp in the targeted Space
    kf unmap-route myapp example.com --hostname myapp
    
    # Unmap the Route in a specific Space
    kf unmap-route --space myspace myapp example.com --hostname myapp
    
    # Unmap a Route with a path
    kf unmap-route myapp example.com --hostname myapp --path /mypath
    

### Flags

`--async`
    

Do not wait for the action to complete on the server before returning.

`--destination-port=int32`
    

Port on the App the Route will connect to.

`-h, --help`
    

help for unmap-route

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
