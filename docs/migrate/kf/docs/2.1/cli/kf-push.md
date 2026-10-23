---
url: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-push/
title: kf push \u00a0|\u00a0 Kf 2.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:05.216401+00:00
---

# kf push  |  Kf 2.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.1/cli/kf-push/

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

#  kf push Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf push` \- Create a new App or apply updates to an existing one

### Synopsis
    
    
    kf push APP_NAME [flags]

### Examples
    
    
      kf push myapp
      kf push myapp --buildpack my.special.buildpack # Discover via kf buildpacks
      kf push myapp --env FOO=bar --env BAZ=foo
      kf push myapp --stack cloudfoundry/cflinuxfs3 # Use a cflinuxfs3 runtime

### Flags

`--app-suffix=string`
    Suffix to append to the end of every pushed App.
`--args=stringArray`
    Override the args for the image. Can't be used with the command flag.
`-b, --buildpack=string`
    Use the specified buildpack rather than the built-in.
`-c, --command=string`
    Startup command for the App, this overrides the default command specified by the web process.
`--container-registry=string`
    Container registry to push images to.
`--cpu-cores=string`
    Number of dedicated CPU cores to give each App instance (e.g, 100m, 0.5, 1, 2). For more information see https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
`-k, --disk-quota=string`
    Size of dedicated ephemeral disk attached to each App instance (e.g. 512M, 2G, 1T)
`--docker-image=string`
    Docker image to deploy rather than building from source.
`--dockerfile=string`
    Path to the Dockerfile to build. Relative to the source root.
`--entrypoint=string`
    Overwrite the default entrypoint of the image. Can't be used with the command flag.
`-e, --env=stringArray`
    Set environment variables. Multiple can be set by using the flag multiple times (e.g., NAME=VALUE).
`-u, --health-check-type=string`
    App health check type (http, port or process, default: port)
`-h, --help`
    help for push
`-i, --instances=int32`
    Number of instances of the App to run (default: 1) (default -1)
`-f, --manifest=string`
    Path to manifest
`-m, --memory-limit=string`
    Amount of dedicated RAM to give each App instance (e.g. 512M, 6G, 1T)
`--no-manifest`
    Do not read the manifest file even if one exists.
`--no-route`
    Prevents the App from being reachable once deployed.
`--no-start`
    Build but do not run the App
`-p, --path=string`
    Path to the source code (default: current directory) (default ".")
`--random-route`
    Create a random Route for this App if it doesn't have one.
`--route=stringArray`
    Use the routes flag to provide multiple HTTP and TCP routes. Each Route for this App is created if it does not already exist.
`-s, --stack=string`
    Base image to use for to use for Apps created with a buildpack.
`-t, --timeout=int`
    Amount of time the App can be unhealthy before declaring it as unhealthy.
`--var=stringToString`
    Manifest variable substitution. Multiple can be set by using the flag multiple times (e.g., NAME=VALUE).
`--vars-file=stringArray`
    JSON or YAML file to read variable substitutions from. Can be supplied multiple times.

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
