---
url: https://docs.cloud.google.com/migrate/kf/docs/2.7/cli/kf-wrap-v2-buildpack/
title: kf wrap-v2-buildpack \u00a0|\u00a0 Kf 2.7 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:34.803870+00:00
---

# kf wrap-v2-buildpack  |  Kf 2.7  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.7/cli/kf-wrap-v2-buildpack/

Version 2.7

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
  * [ 2.7 ](https://docs.cloud.google.com/migrate/kf/docs/2.7)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.7/reference)



Send feedback 

#  kf wrap-v2-buildpack Stay organized with collections  Save and categorize content based on your preferences. 

### Name

`kf wrap-v2-buildpack` \- Create a V3 buildpack that wraps a V2 buildpack.

### Synopsis
    
    
    kf wrap-v2-buildpack NAME V2_BUILDPACK_URL|PATH [flags]

### Description

Creates a V3 buildpack that wraps a V2 buildpack.

The resulting buildpack can then be used with other V3 buildpacks by creating a builder. See https://buildpacks.io/docs/operator-guide/create-a-builder/ for more information.

A V3 buildpack is packaged as an OCI container. If the --publish flag is provided, then the container will be published to the corresponding container repository.

This command uses other CLIs under the hood. This means the following CLIs need to be available on the path: * go * git * pack * cp * unzip

We recommend using Cloud Shell to ensure these CLIs are available and the correct version.

### Examples
    
    
    # Download buildpack from the given git URL. Uses the git CLI to
    # download the repository.
    kf wrap-v2-buildpack gcr.io/some-project/some-name https://github.com/some/buildpack
    
    # Creates the buildpack from the given path.
    kf wrap-v2-buildpack gcr.io/some-project/some-name path/to/buildpack
    
    # Creates the buildpack from the given archive file.
    kf wrap-v2-buildpack gcr.io/some-project/some-name path/to/buildpack.zip
    

### Flags

`--builder-repo=string`
    

Builder repo to use. (default "github.com/poy/buildpackapplifecycle/builder")

`--buildpack-stacks=stringArray`
    

Stack(s) this buildpack will be compatible with. (default [google])

`--buildpack-version=string`
    

Version of the resulting buildpack. This will be used as the image tag. (default "0.0.1")

`-h, --help`
    

help for wrap-v2-buildpack

`--launcher-repo=string`
    

Launcher repo to use. (default "github.com/poy/buildpackapplifecycle/launcher")

`--output-dir=string`
    

Output directory for the buildpack data (before it's packed). If left empty, a temp dir will be used.

`--publish`
    

Publish the buildpack image.

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
