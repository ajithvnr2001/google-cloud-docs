---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memcache/instances/update/
title: gcloud alpha memcache instances update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:48.063295+00:00
---

# gcloud alpha memcache instances update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memcache/instances/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha memcache instances update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha memcache instances update - update a Memorystore Memcached instance 
SYNOPSIS
    

`gcloud alpha memcache instances update` (`INSTANCE` : `--region`=`REGION`) (`--parameters`=`KEY`=`VALUE` | `--display-name`=`DISPLAY_NAME` `--labels`=[`KEY`=`VALUE`,…] `--maintenance-version`=`MAINTENANCE_VERSION` `--node-count`=`NODE_COUNT` `--maintenance-window-any` | `--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY` `--maintenance-window-duration`=`MAINTENANCE_WINDOW_DURATION` `--maintenance-window-start-time`=`MAINTENANCE_WINDOW_START_TIME`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update a Memcached instance with one or more of the following actions: 

  * Scale up or down the number of nodes in the instance. 
  * Stage an update to instance configuration parameters. 
  * Update the instance metadata (display name, labels). 



Updating parameters cannot be combined with any other update actions in the same call. All other update actions can be combined in the same call. 

EXAMPLES
     To scale a Memcached instance named 'my-memcache-instance' in region 'us-central1' to have 3 nodes, run: 
    
    
    gcloud alpha memcache instances update my-memcache-instance --node-count=3 --region=us-central1

To stage an update to the parameters 'protocol' and 'track-sizes' for a Memcached instance named 'my-memcache-instance' in region 'us-central1', run: 
    
    
    gcloud alpha memcache instances update my-memcache-instance --parameters="protocol=ascii,track-sizes=true" --region=us-central1

To update a Memcached instance named 'my-memcache-instance' in region 'us-central1' to have the display name "Foo Cache Service" and the labels 'env' and 'service', run: 
    
    
    gcloud alpha memcache instances update my-memcache-instance --display-name="Foo Cache Service" --labels="env=test,service=foo"

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Memcached instance to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The name of the Memcached region of the instance. Overrides the default memcache/region property value for this command invocation. To set the `region` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `memcache/region`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--parameters`=`KEY`=`VALUE`
     User defined parameters to apply to the memcached process on each node. Possible attributes include: 

`listen-backlog`
     The backlog queue limit for the instance. 
`disable-flush-all`
     If enabled, flush_all command will be disabled. Applicable to 1.4.24 and higher. 
`max-item-size`
     Max bytes of the instance. Must at least be equal to slab_chunk_max (which defaults to 524288 bytes) and less than 134217728 bytes. Additionally it must be a multiple of slab_chunk_max. 
`slab-min-size`
     This is an integer in the range [1, 1024]. 
`slab-growth-factor`
     This is a float in the range [1.01, 100]. 
`protocol`
     This is an enum with acceptable values of ["ascii", "auto"]. 
`disable-cas`
     This is a boolean value. 
`disable-evictions`
     This is a boolean value. 
`max-reqs-per-event`
     This is an integer in the range [1, 1000]. 
`track-sizes`
     This is a boolean value. 
`worker-logbuf-size`
     This is an integer in the range [48, 524288]. 
`watcher-logbuf-size`
     This is an integer in the range [0, 2097151]. 
`lru-crawler`
     This is a boolean value. 
`idle-timeout`
     This is an integer in the range [1,86400]. 
`lru-maintainer`
     This is a boolean value. 
`maxconns-fast`
     This is a boolean value. 
`hash-algorithm`
     This is an enum with accepted values of ["jenkins", "murmur3"]. 
Or at least one of these can be specified: 

`--display-name`=`DISPLAY_NAME`
     An arbitrary and optional user provided name for the instance. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--maintenance-version`=`MAINTENANCE_VERSION`
     The maintenance version to update to. 
`--node-count`=`NODE_COUNT`
     Number of memcache nodes in this instance. Valid values range from 1 to 20. 
At most one of these can be specified: 

`--maintenance-window-any`
     Removes the user-specified maintenance window. 
Or at least one of these can be specified: 

`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY`
     The day of week when the window starts, e.g. 'sunday'. `MAINTENANCE_WINDOW_DAY` must be one of: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. 
`--maintenance-window-duration`=`MAINTENANCE_WINDOW_DURATION`
     Duration in integer hours (`3` to `8`) of the maintenance window. 
`--maintenance-window-start-time`=`MAINTENANCE_WINDOW_START_TIME`
     Hour of day (0 to 23) for the start of maintenance window, in UTC time zone. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memcache/v1beta2` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud memcache instances update](https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/update)
    
    
    [gcloud beta memcache instances update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memcache/instances/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
