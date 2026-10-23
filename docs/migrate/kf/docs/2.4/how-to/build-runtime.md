---
url: https://docs.cloud.google.com/migrate/kf/docs/2.4/how-to/build-runtime/
title: Build Runtime \u00a0|\u00a0 Kf 2.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:47:18.000537+00:00
---

# Build Runtime  |  Kf 2.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.4/how-to/build-runtime/

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

#  Build Runtime Stay organized with collections  Save and categorize content based on your preferences. 

The Build runtime is the environment Apps are built in.

| Buildpack Builds | Docker Builds  
---|---|---  
System libraries | Provided by the Stack | User supplied  
Network access | Full access through Envoy sidecar | Full access through Envoy sidecar  
File system | No storage | No storage  
Language runtime | Provided by the Stack | User supplied  
User | Specified by the Stack | User supplied  
Isolation mechanism | Kubernetes Pod | Kubernetes Pod  
DNS | Provided by Kubernetes | Provided by Kubernetes  
  
## Environment variables

Environment variables are injected into the Build at runtime. Variables are added based on the following order, where later values override earlier ones with the same name:

  1. Space (set by administrators)
  2. App (set by developers)
  3. System (set by Kf)



Kf provides the following system environment variables to Builds:

Variable | Purpose  
---|---  
`CF_INSTANCE_ADDR` | The cluster-visible IP:PORT of the Build.  
`INSTANCE_GUID` | Alias of `CF_INSTANCE_GUID`.  
`CF_INSTANCE_IP` | The cluster-visible IP of the Build.  
`CF_INSTANCE_INTERNAL_IP` | Alias of `CF_INSTANCE_IP`  
`VCAP_APP_HOST` | Alias of `CF_INSTANCE_IP`  
`CF_INSTANCE_PORT` | The cluster-visible port of the Build.  
`LANG` | Required by Buildpacks to ensure consistent script load order.  
`MEMORY_LIMIT` | The maximum amount of memory in MB the Build can consume.  
`VCAP_APPLICATION` | A JSON structure containing App metadata.  
`VCAP_SERVICES` | A JSON structure specifying bound services.  
**Note:** The environment variables Kf provides to Builds are a subset of those provided to [App Runtime](https://docs.cloud.google.com/migrate/kf/docs/2.4/how-to/app-runtime).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
