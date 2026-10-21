---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships/unregister/
title: gcloud beta container hub memberships unregister \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:08:01.388824+00:00
---

# gcloud beta container hub memberships unregister  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships/unregister/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub memberships unregister Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub memberships unregister - unregister a cluster from a fleet 
SYNOPSIS
    

`gcloud beta container hub memberships unregister` (`MEMBERSHIP_NAME` : `--location`=`LOCATION`) (`--gke-cluster`=`LOCATION`/`CLUSTER_NAME` | `--gke-uri`=`GKE_URI` | [`--context`=`CONTEXT` : `--kubeconfig`=`KUBECONFIG`]) [`--uninstall-connect-agent`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command unregisters a cluster with the fleet by: 
    
    
    1. Deleting the Fleet Membership resource for this cluster (a.k.a
       `[gcloud beta container hub memberships delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships/delete)`).
    2. Removing the corresponding in-cluster Kubernetes Resources that make the
       cluster exclusive to one fleet (a.k.a `kubectl delete memberships
       membership`).
    3. [Optional for GKE cluster] Uninstalling the Connect agent from this
       cluster (a.k.a `kubectl delete on the gke-connect namespace`).

The unregister command makes additional internal checks to ensure that all three steps can be safely done to properly clean-up in-Fleet and in-cluster resources. 

To unregister a GKE cluster use `--gke-cluster` or `--gke-uri` flag (no `--kubeconfig` flag is required). 

To unregister a third-party cluster use `--context` flag (with an optional -`-kubeconfig`s flag). 

To only delete the Fleet Membership resource, consider using the command: 

`[gcloud beta container hub memberships delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships/delete)`. This command is intended to delete stale Fleet Membership resources as doing so on a fully registered cluster will skip some of the steps above and orphan in-cluster resources and agent connections to Google. `

EXAMPLES
     Unregister a third-party cluster referenced from a specific kubeconfig file: 
    
    
    gcloud beta container hub memberships unregister my-membership --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig

Unregister a third-party cluster referenced from the default kubeconfig file: 
    
    
    gcloud beta container hub memberships unregister my-membership --context=my-cluster-context

Unregister a GKE cluster referenced from a GKE URI: 
    
    
    gcloud beta container hub memberships unregister my-membership --gke-uri=my-cluster-gke-uri

Unregister a GKE cluster referenced from a GKE Cluster location and name: 
    
    
    gcloud beta container hub memberships unregister my-membership --gke-cluster=my-cluster-region-or-zone/my-cluster

Unregister a GKE cluster and uninstall Connect agent: 
    
    
    gcloud beta container hub memberships unregister my-membership --gke-cluster=my-cluster-region-or-zone/my-cluster --uninstall-connect-agent

POSITIONAL ARGUMENTS
    

Membership resource - The group of arguments defining a membership. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MEMBERSHIP_NAME`
     ID of the membership or fully qualified identifier for the membership. 

To set the `membership` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the membership resource, e.g. `us-central1`. If not specified, defaults to `global`. To set the `location` attribute: 

  * provide the argument `MEMBERSHIP_NAME` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkehub/location`. 


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
    

`--uninstall-connect-agent`
     If set to True for a GKE cluster, Connect agent will be uninstalled from the cluster. No-op for third-party clusters, where Connect agent will always be uninstalled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub memberships unregister](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/memberships/unregister)
    
    
    [gcloud alpha container hub memberships unregister](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub/memberships/unregister)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
