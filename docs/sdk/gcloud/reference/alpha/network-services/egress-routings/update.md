---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/egress-routings/update/
title: gcloud alpha network-services egress-routings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:24.667821+00:00
---

# gcloud alpha network-services egress-routings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/egress-routings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha network-services egress-routings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha network-services egress-routings update - update an Egress Routing 
SYNOPSIS
    

`gcloud alpha network-services egress-routings update` (`EGRESS_ROUTING` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--gateway`=`GATEWAY`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--sources`=[`workloadUri`=`WORKLOADURI`] | `--add-sources`=[`workloadUri`=`WORKLOADURI`] `--clear-sources` | `--remove-sources`=[`workloadUri`=`WORKLOADURI`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Updates the parameters of a single EgressRouting. 
EXAMPLES
     To update the description of the egress routing `my-egress-routing` in location `us-central1`, run: 
    
    
    gcloud alpha network-services egress-routings update my-egress-routing --location=us-central1 --description="Updated description"

POSITIONAL ARGUMENTS
    

EgressRouting resource - Identifier. Name of the EgressRouting resource. It matches pattern `projects/*/locations/*/egressRoutings/<egress_routing>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `egress_routing` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`EGRESS_ROUTING`
     ID of the egressRouting or fully qualified identifier for the egressRouting. 

To set the `egress_routing` attribute: 

  * provide the argument `egress_routing` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the egressRouting resource. 

To set the `location` attribute: 

  * provide the argument `egress_routing` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A free-text description of the resource. Max length 1024 characters. 
`--etag`=`ETAG`
     Etag of the resource. If this is provided, it must match the server's etag. If the provided etag does not match the server's etag, the request will fail with a 409 ABORTED error. 
`--gateway`=`GATEWAY`
     The resource URI of the Policy Enforcement Point (PEP) where matched egress traffic must be redirected. 

Supported PEPs: Secure Web Proxy (SWP), managed Agent Gateway, and SWP behind Service Attachment (PSC-SA). 

Examples: "//networkservices.googleapis.com/projects/{project_id}/locations/{location}/gateways/{gateway_id}" "//networkservices.googleapis.com/projects/{project_id}/locations/{location}/agentGateways/{agent_gateway_id}" "//compute.googleapis.com/projects/{project_id}/regions/{region}/serviceAttachments/{service_attachment_id}" 

Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Set of label tags associated with the EgressRouting resource. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Set of label tags associated with the EgressRouting resource. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

Update sources. 

At most one of these can be specified: 

`--sources`=[`workloadUri`=`WORKLOADURI`]
     Set sources to new value. Specifies the source workloads to which this EgressRouting rule applies. 

`workloadUri`
     The resource URI representing the workload, project, or location. Examples: "//cloudresourcemanager.googleapis.com/projects/{project_id}" "//run.googleapis.com/projects/{project_id}/locations/{location}/services/`" "//container.googleapis.com/projects/{project_id}/locations/{location}/clusters/{cluster_name}" "//container.googleapis.com/projects/{project_id}/locations/{location}/clusters/{cluster_name}/k8s/namespaces/{namespace}". `
Shorthand Example:`
    
    
    --sources=workloadUri=string --sources=workloadUri=string

`JSON Example:`
    
    
    --sources='[{"workloadUri": "string"}]'

`File Example:`
    
    
    --sources=path_to_file.(yaml|json)

`
Or at least one of these can be specified: 

\--add-sources`=[`workloadUri`=`WORKLOADURI`]`
     Add new value to sources list. Specifies the source workloads to which this EgressRouting rule applies. 

workloadUri``
     The resource URI representing the workload, project, or location. Examples: "//cloudresourcemanager.googleapis.com/projects/{project_id}" "//run.googleapis.com/projects/{project_id}/locations/{location}/services/" "//container.googleapis.com/projects/{project_id}/locations/{location}/clusters/{cluster_name}" "//container.googleapis.com/projects/{project_id}/locations/{location}/clusters/{cluster_name}/k8s/namespaces/{namespace}". 
`Shorthand Example:`
    
    
    --add-sources=workloadUri=string --add-sources=workloadUri=string

`JSON Example:`
    
    
    --add-sources='[{"workloadUri": "string"}]'

`File Example:`
    
    
    --add-sources=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-sources`
     Clear sources value and set to empty list. 
`--remove-sources`=[`workloadUri`=`WORKLOADURI`]
     Remove existing value from sources list. Specifies the source workloads to which this EgressRouting rule applies. 

`workloadUri`
     The resource URI representing the workload, project, or location. Examples: "//cloudresourcemanager.googleapis.com/projects/{project_id}" "//run.googleapis.com/projects/{project_id}/locations/{location}/services/`" "//container.googleapis.com/projects/{project_id}/locations/{location}/clusters/{cluster_name}" "//container.googleapis.com/projects/{project_id}/locations/{location}/clusters/{cluster_name}/k8s/namespaces/{namespace}". `
Shorthand Example:`
    
    
    --remove-sources=workloadUri=string --remove-sources=workloadUri=string

`JSON Example:`
    
    
    --remove-sources='[{"workloadUri": "string"}]'

`File Example:`
    
    
    --remove-sources=path_to_file.(yaml|json)

`
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
