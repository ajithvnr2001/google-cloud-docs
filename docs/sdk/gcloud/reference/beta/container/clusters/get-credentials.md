---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/get-credentials/
title: gcloud beta container clusters get-credentials \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:30.131977+00:00
---

# gcloud beta container clusters get-credentials  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters/get-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container clusters get-credentials Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container clusters get-credentials - fetch credentials for a running cluster 
SYNOPSIS
    

`gcloud beta container clusters get-credentials` `NAME` [`--dns-endpoint`] [`--internal-ip`] [`--location`=`LOCATION` | `--region`=`REGION` | `--zone`=`ZONE`, `-z` `ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta container clusters get-credentials updates a `kubeconfig` file with appropriate credentials and endpoint information to point `kubectl` at a specific cluster in Google Kubernetes Engine. 

It takes a project and a zone as parameters, passed through by set defaults or flags. By default, credentials are written to `HOME/.kube/config`. You can provide an alternate path by setting the `KUBECONFIG` environment variable. If `KUBECONFIG` contains multiple paths, the first one is used. 

This command enables switching to a specific cluster, when working with multiple clusters. It can also be used to access a previously created cluster from a new workstation. 

By default, gcloud beta container clusters get-credentials will configure kubectl to automatically refresh its credentials using the same identity as gcloud. If you are running kubectl as part of an application, it is recommended to use [application default credentials](https://cloud.google.com/docs/authentication/production). To configure a `kubeconfig` file to use application default credentials, set the container/use_application_default_credentials [Cloud SDK property](https://cloud.google.com/sdk/docs/properties) to true before running gcloud beta container clusters get-credentials 

See <https://cloud.google.com/kubernetes-engine/docs/kubectl> for kubectl documentation. 

EXAMPLES
     To switch to working on your cluster 'sample-cluster', run: 
    
    
    gcloud beta container clusters get-credentials sample-cluster --location=us-central1-f

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the cluster to get credentials for. Overrides the default `container/cluster` property value for this command invocation. 
FLAGS
    

`--dns-endpoint`
     Whether to use the DNS-based endpoint for the cluster address. 
`--internal-ip`
     Whether to use the internal IP address of the cluster endpoint. 
At most one of these can be specified: 

`--location`=`LOCATION`
     Compute zone or region (e.g. us-central1-a or us-central1) for the cluster. Overrides the default compute/region or compute/zone value for this command invocation. Prefer using this flag over the --region or --zone flags. 
`--region`=`REGION`
     Compute region (e.g. us-central1) for a regional cluster. Overrides the default compute/region property value for this command invocation. 
`--zone`=`ZONE`, `-z` `ZONE`
     Compute zone (e.g. us-central1-a) for a zonal cluster. Overrides the default compute/zone property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container clusters get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/get-credentials)
    
    
    [gcloud alpha container clusters get-credentials](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters/get-credentials)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
