---
url: https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update-instance-split/
title: gcloud run worker-pools update-instance-split \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:02:01.915502+00:00
---

# gcloud run worker-pools update-instance-split  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update-instance-split/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud run worker-pools update-instance-split Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud run worker-pools update-instance-split - adjust the instance assignments for a Cloud Run worker-pool 
SYNOPSIS
    

`gcloud run worker-pools update-instance-split` [[`WORKER_POOL`] `--region`=`REGION`] [`--async`] [`--breakglass`=`JUSTIFICATION`] [`--to-latest` | `--to-revisions`=[`REVISION-NAME`=`PERCENTAGE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Adjust the instance assignments for a Cloud Run worker-pool. 
EXAMPLES
     To assign 10% of instances to revision my-worker-pool-s5sxn and 90% of instances to revision my-worker-pool-cp9kw run: 
    
    
    gcloud run worker-pools update-instance-split my-worker-pool --to-revisions=my-worker-pool-s5sxn=10,my-worker-pool-cp9kw=90

To increase the instances to revision my-worker-pool-s5sxn to 20% and by reducing the instances to revision my-worker-pool-cp9kw to 80% run: 
    
    
    gcloud run worker-pools update-instance-split my-worker-pool --to-revisions=my-worker-pool-s5sxn=20

To rollback to revision my-worker-pool-cp9kw run: 
    
    
    gcloud run worker-pools update-instance-split my-worker-pool --to-revisions=my-worker-pool-cp9kw=100

To assign 100% of instances to the current or future LATEST revision run: 
    
    
    gcloud run worker-pools update-instance-split my-worker-pool --to-latest

You can also refer to the current or future LATEST revision in --to-revisions by the string "LATEST". For example, to set 10% of instances to always float to the latest revision: 
    
    
    gcloud run worker-pools update-instance-split my-worker-pool --to-revisions=LATEST=10

POSITIONAL ARGUMENTS
    

WorkerPool resource - WorkerPool to update instance split of. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `WORKER_POOL` on the command line with a fully specified name; 
  * specify the workerpool name from an interactive prompt with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


[`WORKER_POOL`]
     ID of the WorkerPool or fully qualified identifier for the WorkerPool. 

To set the `worker-pool` attribute: 

  * provide the argument `WORKER_POOL` on the command line; 
  * specify the workerpool name from an interactive prompt. 


`--region`=`REGION`
     The Cloud region for the WorkerPool. Overrides the default `run/region` property value for this command invocation. 

To set the `region` attribute: 

  * provide the argument `WORKER_POOL` on the command line with a fully specified name; 
  * specify the workerpool name from an interactive prompt with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `run/region`; 
  * specify the region from an interactive prompt. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--breakglass`=`JUSTIFICATION`
     Justification to bypass Binary Authorization policy constraints and allow the operation. See <https://cloud.google.com/binary-authorization/docs/using-breakglass> for more information. Next update or deploy command will automatically clear existing breakglass justification. 
At most one of these can be specified: 

`--to-latest`
     True to assign 100 percent of instances to the 'latest' revision of this service. Note that when a new revision is created, it will become the 'latest' and instances will be fully assigned to it unless configured otherwise using `--[no-]promote` flag. Defaults to False. Synonymous with '--to-revisions=LATEST=100'. 
`--to-revisions`=[`REVISION-NAME`=`PERCENTAGE`,…]
     Comma separated list of instance assignments in the form REVISION-NAME=PERCENTAGE. REVISION-NAME must be the name for a revision for the worker as returned by 'gcloud run workers revisions list --worker=WORKER' . PERCENTAGE must be an integer percentage between 0 and 100 inclusive. Ex worker-nw9hs=10,worker-nw9hs=20 Up to 100 percent of instances may be assigned. If the total of 100 percent of instances is assigned, the Worker instance split is updated as specified. If under 100 percent of instance split is assigned, the Worker instance split is updated as specified for revisions with assignments and instance split is scaled up or down proportionally as needed for revision that are currently serving workload but that do not have new assignments. For example assume revision-1 is serving 40 percent of workload and revision-2 is serving 60 percent. If revision-1 is assigned 45 percent of instances and no assignment is made for revision-2, the worker is updated with revsion-1 assigned 45 percent of instances and revision-2 scaled down to 55 percent. You can use "LATEST" as a special revision name to always put the given percentage of instance split on the latest ready revision. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

REGIONAL ENDPOINTS
     This command supports regional endpoints. To use regional endpoints for this command, use the `--endpoint-mode=regional-preferred` flag. To use regional endpoints by default, run `$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) regional/endpoint_mode regional-preferred`. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha run worker-pools update-instance-split](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/worker-pools/update-instance-split)
    
    
    [gcloud beta run worker-pools update-instance-split](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/worker-pools/update-instance-split)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
