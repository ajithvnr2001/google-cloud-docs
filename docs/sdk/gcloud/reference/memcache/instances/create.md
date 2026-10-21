---
url: https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/create/
title: gcloud memcache instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:31.547290+00:00
---

# gcloud memcache instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/memcache/instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud memcache instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud memcache instances create - create a Memorystore Memcached instance 
SYNOPSIS
    

`gcloud memcache instances create` (`INSTANCE` : `--region`=`REGION`) `--node-count`=`NODE_COUNT` `--node-cpu`=`NODE_CPU` `--node-memory`=`NODE_MEMORY` [`--async`] [`--authorized-network`=`AUTHORIZED_NETWORK`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY`] [`--maintenance-window-duration`=`MAINTENANCE_WINDOW_DURATION`] [`--maintenance-window-start-time`=`MAINTENANCE_WINDOW_START_TIME`] [`--memcached-version`=`MEMCACHED_VERSION`] [`--parameters`=`KEY`=`VALUE`] [`--reserved-ip-range-id`=[`RESERVED_IP_RANGE_ID`,…]] [`--tags`=[`KEY`=`VALUE`,…]] [`--zones`=[`ZONES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Memorystore Memcached instance. 

This command can fail for the following reasons: 

  * An instance with the same name already exists. 
  * The active account does not have the necessary permissions to create instances. 


EXAMPLES
     To create a Memcached instance named 'my-memcache-instance' in region 'us-central1' with 3 nodes, each with 2 CPUs and 2GB of memory, run: 
    
    
    gcloud memcache instances create my-memcache-instance --region=us-central1 --node-count=3 --node-cpu=2 --node-memory=2GB

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Memcached instance to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--node-count`=`NODE_COUNT`
     Number of memcache nodes in this instance. Valid values range from 1 to 20. 
`--node-cpu`=`NODE_CPU`
     Number of cpus per node in this instance. Valid values are 1 or even number between 2-32. Value of 1 is not supported in all regions. 
`--node-memory`=`NODE_MEMORY`
     Amount of memory allocated per node in this instance. The value must be a whole number followed by a size unit of 'MB' for megabyte, or 'GB' for gigabyte, ie '3072MB' or '9GB'. The value must be between 1024MB and 307200MB. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--authorized-network`=`AUTHORIZED_NETWORK`
     Full name of the Google Compute Engine network to which the instance is connected. If unspecified, the default network will be used. 
`--display-name`=`DISPLAY_NAME`
     An arbitrary and optional user provided name for the instance. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--maintenance-window-day`=`MAINTENANCE_WINDOW_DAY`
     The day of week when the window starts, e.g. `sunday`. `MAINTENANCE_WINDOW_DAY` must be one of: `friday`, `monday`, `saturday`, `sunday`, `thursday`, `tuesday`, `wednesday`. 
`--maintenance-window-duration`=`MAINTENANCE_WINDOW_DURATION`
     Duration in integer hours (`3` to `8`) of the maintenance window. 
`--maintenance-window-start-time`=`MAINTENANCE_WINDOW_START_TIME`
     Hour of day (`0` to `23`) for the start of maintenance window, in UTC time zone. 
`--memcached-version`=`MEMCACHED_VERSION`
     Optional major version of Memcached software to use with the instance. If not provided, default of "1.5" will be used. `MEMCACHED_VERSION` must be one of: 

`1.5`
     Memcached major version 1.5 
`1.6.15`
     Memcached version 1.6.15 
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
`--reserved-ip-range-id`=[`RESERVED_IP_RANGE_ID`,…]
     Contains the name of allocated IP address ranges associated with the private service access connection for example, "test-default" associated with IP range 10.0.0.0/29. 
`--tags`=[`KEY`=`VALUE`,…]
     List of tag KEY=VALUE pairs to add. 
`--zones`=[`ZONES`,…]
     List of zones for the memcache nodes. The nodes will be divided equally across the given zones up to --node-count value. If not provided, the service will by default create nodes in all zones in the region specified by --region flag. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memcache/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha memcache instances create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memcache/instances/create)
    
    
    [gcloud beta memcache instances create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memcache/instances/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
