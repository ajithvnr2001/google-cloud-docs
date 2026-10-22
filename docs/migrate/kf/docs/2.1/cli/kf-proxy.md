---
url: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-proxy/
title: kf proxy \u00a0|\u00a0 Kf 2.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:30:31.742159+00:00
---

# kf proxy  |  Kf 2.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-proxy/

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

#  kf proxy Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf proxy` \- Start a local reverse proxy to an App

### Synopsis
    
    
    kf proxy APP_NAME [flags]

### Description

Proxy creates a reverse HTTP proxy to the cluster's gateway on a local port opened on the operating system's loopback device.

The proxy rewrites all HTTP requests, changing the HTTP Host header and adding an additional header X-Kf-App to ensure traffic reaches the specified app even if multiple are attached to the same route.

Proxy DOES NOT establish a direct connection to the App.

For proxy to work:

  * The cluster's gateway MUST be accessible from your local machine.
  * The app MUST have a public URL

If you need to establish a direct connection to an App, use the port-forward command in kubectl. It establishes a proxied connection directly to a port on a pod via the Kubernetes cluster. port-forward bypasses all routing.




### Examples
    
    
      kf proxy myapp

### Flags

`--gateway=string`
    HTTP gateway to route requests to (default: autodetected from cluster)
`-h, --help`
    help for proxy
`--port=int`
    Local port to listen on (default 8080)

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
