---
url: https://docs.cloud.google.com/migrate/kf/docs/2.2/cli/kf-env/
title: kf env \u00a0|\u00a0 Kf 2.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:29:43.137591+00:00
---

# kf env  |  Kf 2.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.2/cli/kf-env/

Version 2.2

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
  * [ 2.2 ](https://docs.cloud.google.com/migrate/kf/docs/2.2)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.2/reference)



Send feedback 

#  kf env Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf env` \- Print information about an App's environment variables.

### Synopsis
    
    
    kf env APP_NAME [flags]

### Description

The env command gets the names and values of developer managed environment variables for an App.

Environment variables are evaluated in the following order with later values overriding earlier ones with the same name:

  1. Space (set by administrators)
  2. App (set by developers)
  3. System (set by Kf) Environment variables containing variable substitution "$(...)" are replaced at runtime by Kubernetes. Kf provides the following runtime environment variables:


  * CF_INSTANCE_ADDR: The cluster-visible IP:PORT of the App instance.
  * CF_INSTANCE_GUID: The UUID of the App instance.
  * INSTANCE_GUID: Alias of CF_INSTANCE_GUID
  * CF_INSTANCE_INDEX: The index number of the App instance, this will ALWAYS be 0.
  * INSTANCE_INDEX: Alias of CF_INSTANCE_INDEX
  * CF_INSTANCE_IP: The cluster-visible IP of the App instance.
  * CF_INSTANCE_INTERNAL_IP: Alias of CF_INSTANCE_IP
  * VCAP_APP_HOST: Alias of CF_INSTANCE_IP
  * CF_INSTANCE_PORT: The cluster-visible port of the App instance. In Kf this is the same as PORT.
  * DATABASE_URL: The first URI found in a VCAP_SERVICES credential.
  * DISK_LIMIT: The maximum amount of disk storage in MB the App can use.
  * LANG: Required by buildpacks to ensure consistent script load order.
  * MEMORY_LIMIT: The maximum amount of memory in MB the App can consume.
  * PORT: The port the App should listen on for requests.
  * VCAP_APP_PORT: Alias of PORT
  * VCAP_APPLICATION: A JSON structure containing app metadata.
  * VCAP_SERVICES: A JSON structure specifying bound services.



### Examples
    
    
      kf env myapp

### Flags

`-h, --help`
    help for env

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
