---
url: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-create-user-provided-service/
title: kf create-user-provided-service \u00a0|\u00a0 Kf 2.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:23.831459+00:00
---

# kf create-user-provided-service  |  Kf 2.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-create-user-provided-service/

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

#  kf create-user-provided-service Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf create-user-provided-service` \- Create a standalone service instance from existing credentials

### Synopsis
    
    
    kf create-user-provided-service SERVICE_INSTANCE [-p CREDENTIALS] [-t TAGS] [flags]

### Description

Creates a standalone service instance from existing credentials. User-provided services can be used to inject credentials for services managed outside of Kf into Apps.

Credentials are stored in a Kubernetes Secret in the Space the service is created in. On GKE these Secrets are encrypted at rest and can optionally be encrypted using KMS.

### Examples
    
    
      # Bring an existing database service
      kf create-user-provided-service db-service -p '{"url":"mysql://..."}'
      
      # Create a service with tags for autowiring
      kf create-user-provided-service db-service -t "mysql,database,sql"

### Flags

`--async`
    Don't wait for the action to complete on the server before returning
`-h, --help`
    help for create-user-provided-service
`--mock-class=string`
    Mock class name to use in VCAP_SERVICES rather than 'user-provided'.
`--mock-plan=string`
    Mock plan name to use in VCAP_SERVICES rather than blank.
`-p, --params=string`
    JSON object or path to a JSON file containing configuration parameters. (default "{}")
`-r, --route=string`
    URL to which requests for bound routes will be forwarded. Scheme must be https.
`-t, --tags=string`
    User-defined tags to differentiate services during injection.

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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
