---
url: https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/deploying-an-app/
title: Deploy an application \u00a0|\u00a0 Kf 2.11 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:21.960482+00:00
---

# Deploy an application  |  Kf 2.11  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/deploying-an-app/

Version 2.11 - Latest version

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
  * [ 2.11 ](https://docs.cloud.google.com/migrate/kf/docs/2.11)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.11/getting-started)



Send feedback 

#  Deploy an application Stay organized with collections  Save and categorize content based on your preferences. 

When pushing an app (via `kf push`) to Kf, there are three lifecycles that Kf uses to take your source code and allow it to handle traffic:

  1. Source code upload
  2. Build
  3. Run



## Source code upload

The first thing that happens when you `kf push` is the Kf CLI (`kf`) packages up your directory (either current or `--path/-p`) into a container and publishes it to the container registry configured for the Space. This is called the source container. The Kf CLI then creates an `App` type in Kubernetes that contains both the source image and configuration from the App manifest and push flags.

### Ignore files during push

In many cases, you will not want to upload certain files during `kf push` (i.e., "ignore" them). This is where a `.kfignore` (or `.cfignore`) file can be used. Similar to a `.gitignore` file, this file instructs the Kf CLI which files to not include in the source code container.

To create a `.kfignore` file, create a text file named `.kfignore` in the base directory of your app (similar to where you would store the manifest file). Then populate it with a newline delimited list of files and directories you don't want published. For example:
    
    
    bin
    .idea
    

This will tell the Kf CLI to not include anything in the `bin` or `.idea` directories.

Kf supports [gitignore](https://git-scm.com/docs/gitignore) style syntax.

## Build

The Build lifecycle is handled by a Tekton [TaskRun](https://github.com/tektoncd/pipeline/blob/master/docs/taskruns.md). Depending on the flags that you provide while pushing, it will choose a specific Tekton [Task](https://github.com/tektoncd/pipeline/blob/master/docs/tasks.md). Kf currently has the following Tekton Tasks:

  * buildpackv2
  * buildpackv3
  * kaniko



Kf tracks each TaskRun as a Build. If a Build succeeds, the resulting container image is then deployed via the Run lifecycle (described below).

More information can be found at [Build runtime](https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/build-runtime).

## Run

The Run lifecycle is responsible for taking a container image and creating a [Kubernetes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

It also creates:

  * [Istio Virtual Services](https://istio.io/docs/reference/config/networking/virtual-service/)
  * [Kubernetes Secrets](https://kubernetes.io/docs/concepts/configuration/secret/)



More information can be found at [Build runtime](https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/build-runtime).

## Push timeouts

Kf supports setting an environment variable to instruct the CLI to time out while pushing apps. If set, the variables `KF_STARTUP_TIMEOUT` or `CF_STARTUP_TIMEOUT` are parsed as a golang style duration (for example `15m`, `1h`). If a value is not set, the push timeout defaults to 15 minutes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
