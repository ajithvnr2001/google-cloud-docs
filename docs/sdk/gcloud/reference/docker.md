---
url: https://docs.cloud.google.com/sdk/gcloud/reference/docker/
title: gcloud docker \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:37.492248+00:00
---

# gcloud docker  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/docker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud docker Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud docker - enable Docker CLI access to Google Container Registry 
SYNOPSIS
    

`gcloud docker` [`--authorize-only`, `-a`] [`--docker-host`=`DOCKER_HOST`] [`--server`=`SERVER`,[`SERVER`,…], `-s` `SERVER`,[`SERVER`,…]; default="gcr.io,us.gcr.io,eu.gcr.io,asia.gcr.io,staging-k8s.gcr.io,marketplace.gcr.io"] [`GCLOUD_WIDE_FLAG …`] [-- `DOCKER_ARGS` …]
DESCRIPTION
     `(DEPRECATED)` Enable Docker CLI access to Google Container Registry. 

`gcloud docker` will not be supported for Docker client versions above 18.03. 

As an alternative, use `[gcloud auth configure-docker](https://docs.cloud.google.com/sdk/gcloud/reference/auth/configure-docker)` to configure `docker` to use `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` as a credential helper, then use `docker` as you would for non-GCR registries, e.g. `docker pull gcr.io/project-id/my-image`. Add `--verbosity=error` to silence this warning: `gcloud docker --verbosity=error -- pull gcr.io/project-id/my-image`. 

See: <https://cloud.google.com/container-registry/docs/support/deprecation-notices#gcloud-docker> gcloud docker wraps Docker commands so that `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` can inject the appropriate fresh authentication token into requests that interact with the Docker registry. 

All Docker-specific flags are passed through to the underlying `docker` command. A full reference of Docker's command line options available after `--` can be found here: <https://docs.docker.com/engine/reference/commandline/cli/>. You may also run `gcloud docker -- --help` to view the Docker CLI's help directly. 

Detailed documentation on Container Registry can be found here: <https://cloud.google.com/container-registry/docs/>

EXAMPLES
     To pull the image 'gcr.io/google-containers/pause:1.0' from the docker registry, run: 
    
    
    gcloud docker -- pull gcr.io/google-containers/pause:1.0

Push the image 'gcr.io/example-org/example-image:latest' to our private docker registry. 
    
    
    gcloud docker -- push gcr.io/example-org/example-image:latest

Configure authentication, then simply use docker: 
    
    
    gcloud docker --authorize-only
    docker push gcr.io/example-org/example-image:latest

POSITIONAL ARGUMENTS
    

[-- `DOCKER_ARGS` …]
     Arguments to pass to Docker. 

The '--' argument must be specified between gcloud specific args on the left and DOCKER_ARGS on the right. 

FLAGS
    

`--authorize-only`, `-a`
     Configure Docker authorization only; do not launch the Docker command-line. 
`--docker-host`=`DOCKER_HOST`
     URL to connect to Docker Daemon. Format: tcp://host:port or unix:///path/to/socket. 
`--server`=`SERVER`,[`SERVER`,…], `-s` `SERVER`,[`SERVER`,…]; default="gcr.io,us.gcr.io,eu.gcr.io,asia.gcr.io,staging-k8s.gcr.io,marketplace.gcr.io"
     Address of the Google Cloud Registry. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
