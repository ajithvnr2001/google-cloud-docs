---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/code/dev/
title: gcloud beta code dev \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:11.809393+00:00
---

# gcloud beta code dev  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/code/dev/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta code dev Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta code dev - run a Cloud Run service in a local development environment 
SYNOPSIS
    

`gcloud beta code dev` [`SERVICE_CONFIG`] [`--[no-]allow-secret-manager`] [`--local-port`=`LOCAL_PORT`] [`--secrets`=[`KEY`=`VALUE`,…]] [`--source`=`SOURCE`] [`--no-stop-cluster`] [`--application-default-credential` | `--service-account`=`SERVICE_ACCOUNT`] [`--builder`=`BUILDER` | `--dockerfile`=`DOCKERFILE`; default="Dockerfile"] [`--kube-context`=`KUBE_CONTEXT` | `--minikube-profile`=`MINIKUBE_PROFILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Run a Cloud Run service in a local development environment. 

This command takes Cloud Run source, builds it, and runs it on the local machine. This command also watches the relevant source files and updates the container when they change. 

EXAMPLES
     If building images using a Dockerfile: 
    
    
    gcloud beta code dev --dockerfile=<path_to_dockerfile>

If the Dockerfile is named `Dockerfile` and is located in the current directory, the `--dockerfile` flag may be omitted: 
    
    
    gcloud beta code dev

To access Google Cloud Platform services with the current user's credentials, login to obtain the application default credentials and invoke this command with the `--application-default-credential` flag. 
    
    
    [gcloud auth application-default login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login)
    gcloud beta code dev --dockerfile=<path_to_dockerfile> --application-default-credential

POSITIONAL ARGUMENTS
    

[`SERVICE_CONFIG`]
     service.yaml filename override. Defaults to the first file matching `*service.dev.yaml` then `*service.yaml`, if any exist. This path is relative to the --source dir. 
FLAGS
    

`--[no-]allow-secret-manager`
     Suppress warnings if secrets need to be pulled from secret manager. Use `--allow-secret-manager` to enable and `--no-allow-secret-manager` to disable. 
`--local-port`=`LOCAL_PORT`
     Local port to which the service connection is forwarded. If this flag is not set, then a random port is chosen. 
`--secrets`=[`KEY`=`VALUE`,…]
     List of key-value pairs to set as secrets. 
`--source`=`SOURCE`
     The directory containing the source to build. If not specified, the current directory is used. 
`--stop-cluster`
     If running on minikube, stop the minkube profile at the end of the session. Enabled by default, use `--no-stop-cluster` to disable. 
At most one of these can be specified: 

`--application-default-credential`
     When connecting to Google Cloud Platform services, use the application default credential. 
`--service-account`=`SERVICE_ACCOUNT`
     When connecting to Google Cloud Platform services, use a service account key. 
At most one of these can be specified: 

`--builder`=`BUILDER`
     Build with a given Cloud Native Computing Foundation Buildpack builder. 
`--dockerfile`=`DOCKERFILE`; default="Dockerfile"
     Dockerfile for the service image. 
At most one of these can be specified: 

`--kube-context`=`KUBE_CONTEXT`
     Kubernetes context. 
`--minikube-profile`=`MINIKUBE_PROFILE`
     Minikube profile. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha code dev](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/code/dev)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
