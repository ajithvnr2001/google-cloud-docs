---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/cloudrun/apply/
title: gcloud alpha container hub cloudrun apply \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:16:10.329762+00:00
---

# gcloud alpha container hub cloudrun apply  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/cloudrun/apply/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container hub cloudrun apply Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container hub cloudrun apply - deploy or update the CloudRun feature 
SYNOPSIS
    

`gcloud alpha container hub cloudrun apply` (`--gke-cluster`=`LOCATION`/`CLUSTER_NAME` | `--gke-uri`=`GKE_URI` | [`--context`=`CONTEXT` : `--kubeconfig`=`KUBECONFIG`]) [`--config`=`CONFIG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Deploy or update a user-specified config file of the CloudRun custom resource. The config file should be a YAML file. 
EXAMPLES
     To apply the CloudRun YAML file, run: 
    
    
    gcloud alpha container hub cloudrun apply --kubeconfig=/path/to/kubeconfig --config=/path/to/cloud-run-cr.yaml

REQUIRED FLAGS
    

Cluster identifier. 

Exactly one of these must be specified: 

`--gke-cluster`=`LOCATION`/`CLUSTER_NAME`
     The location/name of the GKE cluster. The location can be a zone or a region for e.g `us-central1-a/my-cluster`. 
`--gke-uri`=`GKE_URI`
     The URI of a GKE cluster that you want to register to Hub; for example, 'https://container.googleapis.com/v1/projects/my-project/locations/us-central1-a/clusters/my-cluster'. To obtain the URI, you can run 'gcloud container clusters list --uri'. Note that this should only be provided if the cluster being registered is a GKE cluster. The service will validate the provided URI to confirm that it maps to a valid GKE cluster." 
Or at least one of these can be specified: 

Non-GKE cluster identifier. 
`--context`=`CONTEXT`
     The cluster context as it appears in the kubeconfig file. You can get this value from the command line by running command: `kubectl config current-context`. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--kubeconfig`=`KUBECONFIG`
     The kubeconfig file containing an entry for the cluster. Defaults to $KUBECONFIG if it is set in the environment, otherwise defaults to $HOME/.kube/config. 
OPTIONAL FLAGS
    

`--config`=`CONFIG`
     The path to CloudRun custom resource config file. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container hub cloudrun apply](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun/apply)
    
    
    [gcloud beta container hub cloudrun apply](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/cloudrun/apply)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
