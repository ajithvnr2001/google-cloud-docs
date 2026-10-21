---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/workload/profiles/manifests/create/
title: gcloud container workload profiles manifests create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:27:52.310689+00:00
---

# gcloud container workload profiles manifests create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/workload/profiles/manifests/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container workload profiles manifests create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container workload profiles manifests create - generate optimized Kubernetes manifests for a given workload profile 
SYNOPSIS
    

`gcloud container workload profiles manifests create` `--cluster-version`=`CLUSTER_VERSION` `--workload`=`WORKLOAD` [`--options`=[`KEY`=`VALUE`,…]] [`--output`=`OUTPUT`; default="all"] [`--output-path`=`OUTPUT_PATH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Generate optimized Kubernetes manifests for a given workload profile. 
REQUIRED FLAGS
    

`--cluster-version`=`CLUSTER_VERSION`
     The GKE version to generate the manifest for. 
`--workload`=`WORKLOAD`
     The name of the optimization set to generate the manifest for. This specifies the workload, workload version, and workload characterization to optimize for (e.g., "redis-7-caching"). 
OPTIONAL FLAGS
    

`--options`=[`KEY`=`VALUE`,…]
     Additional key-value pair options for generating the manifest. For example, to specify allowed machine types: --options=machineType=type1,type2 
`--output`=`OUTPUT`; default="all"
     The output to display. Default is all. `OUTPUT` must be one of: `manifest`, `all`. 
`--output-path`=`OUTPUT_PATH`
     The path to save the output to. If not specified, output to the terminal. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
