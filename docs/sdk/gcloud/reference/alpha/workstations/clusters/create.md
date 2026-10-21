---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/workstations/clusters/create/
title: gcloud alpha workstations clusters create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:29.936740+00:00
---

# gcloud alpha workstations clusters create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/workstations/clusters/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha workstations clusters create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha workstations clusters create - create a workstation cluster 
SYNOPSIS
    

`gcloud alpha workstations clusters create` (`CLUSTER` : `--region`=`REGION`) [`--async`] [`--console-base-url`=`CONSOLE_BASE_URL`] [`--domain`=`DOMAIN`] [`--enable-http2`] [`--enable-private-endpoint`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--network`=`NETWORK`] [`--subnetwork`=`SUBNETWORK`] [`--tags`=[`KEY`=`VALUE`,…]] [`--workstation-authorization-url`=`WORKSTATION_AUTHORIZATION_URL`] [`--workstation-launch-url`=`WORKSTATION_LAUNCH_URL`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a workstation cluster. 
EXAMPLES
     To create a public cluster `my-cluster` in region `us-central1`, run: 
    
    
    gcloud alpha workstations clusters create my-cluster --region=us-central1

To create a private cluster 'my-private-cluster' associated with network 'my-network' and subnetwork 'my-subnetwork'. run: 
    
    
    gcloud alpha workstations clusters create my-private-cluster --region=us-central1 --enable-private-endpoint --network='my-network' --subnetwork='my-subnetwork'

POSITIONAL ARGUMENTS
    

Cluster resource - Arguments and flags that specify the cluster to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `cluster` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the region of the cluster. To set the `region` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `workstations/region`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--console-base-url`=`CONSOLE_BASE_URL`
     Cloud Console Base URL to be used for workstations in this cluster. 
`--domain`=`DOMAIN`
     Domain used by Workstations for HTTP ingress. 
`--enable-http2`
     Whether HTTP/2 is enabled for the workstation cluster. 
`--enable-private-endpoint`
     Default is false. If specified, the cluster will be assigned an internal IP address to the Cluster Gateway. This isolates the cluster's workstations from public networks, but requires additional configuration. Learn more: <https://cloud.google.com/workstations/docs>. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--labels`=[`KEY`=`VALUE`,…]
     Labels that are applied to the cluster and propagated to the underlying Compute Engine resources. 
`--network`=`NETWORK`
     Fully specified network path for instances created in this cluster. 
`--subnetwork`=`SUBNETWORK`
     Fully specified subnetwork path for instances created in this cluster. 
`--tags`=[`KEY`=`VALUE`,…]
     Resource manager tags to be bound to this cluster. For example: "123/environment=production" "123/costCenter=marketing" 
`--workstation-authorization-url`=`WORKSTATION_AUTHORIZATION_URL`
     The redirect URL for unauthorized requests. Redirects to this endpoint send a base64 encoded 'state' query param with the workstation name and original request hostname. 
`--workstation-launch-url`=`WORKSTATION_LAUNCH_URL`
     The launch URL for workstations. Requests sent to unstarted workstations will be redirected to this URL with 'workstation' and 'project' query params. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `workstations/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/workstations>
REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud workstations clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/workstations/clusters/create)
    
    
    [gcloud beta workstations clusters create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workstations/clusters/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
