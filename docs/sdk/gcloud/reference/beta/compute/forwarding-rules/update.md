---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/forwarding-rules/update/
title: gcloud beta compute forwarding-rules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:02.262721+00:00
---

# gcloud beta compute forwarding-rules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/forwarding-rules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute forwarding-rules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute forwarding-rules update - update a Compute Engine forwarding rule 
SYNOPSIS
    

`gcloud beta compute forwarding-rules update` `NAME` [`--allow-global-access`] [`--allow-psc-global-access`] [`--external-managed-backend-bucket-migration-testing-percentage`=`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_TESTING_PERCENTAGE`] [`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`] [`--metadata-filter`=[`filter-labels`=`FILTER-LABELS`],[`filter-match-criteria`=`FILTER-MATCH-CRITERIA`]] [`--source-ip-ranges`=`SOURCE_IP_RANGE`,[…]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-external-managed-backend-bucket-migration-state` | `--external-managed-backend-bucket-migration-state`=`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_STATE`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute forwarding-rules update` updates labels and global access for a Compute Engine forwarding rule. 
EXAMPLES
     To update the forwarding rule to allow global access, run: 
    
    
    gcloud beta compute forwarding-rules update example-fr --allow-global-access --region=us-central1

To add/update labels ``k0`` and ``k1`` and remove labels with key ``k3``, run: 
    
    
    gcloud beta compute forwarding-rules update example-fr --region=us-central1 --update-labels=k0=value1,k1=value2 --remove-labels=k3

Labels can be used to identify the forwarding rule and to filter them as in 
    
    
    [gcloud beta compute forwarding-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/forwarding-rules/list) --filter='labels.k1:value2'

To list existing labels, run: 
    
    
    [gcloud beta compute forwarding-rules describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/forwarding-rules/describe) example-fr --format="default(labels)"

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the forwarding rule to operate on. 
FLAGS
    

`--allow-global-access`
     If True, then clients from all regions can access this internal forwarding rule. This can only be specified for forwarding rules with the LOAD_BALANCING_SCHEME set to INTERNAL or INTERNAL_MANAGED. For forwarding rules of type INTERNAL, the target must be either a backend service or a target instance. 
`--allow-psc-global-access`
     If specified, clients from all regions can access this Private Service Connect forwarding rule. This can only be specified if the forwarding rule's target is a service attachment (--target-service-attachment). 
`--external-managed-backend-bucket-migration-testing-percentage`=`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_TESTING_PERCENTAGE`
     Determines the fraction of requests that should be processed by the Global external Application Load Balancer. 

The value of this field must be in the range [0, 100]. 

`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`
     Only for the Global external Application Load Balancer migration. 

The value of this field must be EXTERNAL or EXTERNAL_MANAGED. 

`LOAD_BALANCING_SCHEME` must be one of: `EXTERNAL`, `EXTERNAL_MANAGED`. 

`--metadata-filter`=[`filter-labels`=`FILTER-LABELS`],[`filter-match-criteria`=`FILTER-MATCH-CRITERIA`]
     Opaque filter criteria used by load balancer to restrict routing configuration to a limited set of xDS compliant clients. 

`filter-match-criteria`
     Specifies how individual filter label matches contribute toward the overall metadata filter match. Supported values are `MATCH_ANY` and `MATCH_ALL`. 
`filter-labels`
     A list of label/value pairs that must match labels in the provided metadata based on filter-match-criteria, e.g., `{'key1':'val1','key2':'val2'}`. 

Can be specified multiple times for multiple metadata filters. 

`--source-ip-ranges`=`SOURCE_IP_RANGE`,[…]
     List of comma-separated IP addresses or IP ranges. If set, this forwarding rule only forwards traffic when the packet's source IP address matches one of the IP ranges set here. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-external-managed-backend-bucket-migration-state`
     Clears current state of external managed migration. 
`--external-managed-backend-bucket-migration-state`=`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_STATE`
     Specifies the migration state. Possible values are PREPARE, TEST_BY_PERCENTAGE, and TEST_ALL_TRAFFIC. 

To begin the migration from EXTERNAL to EXTERNAL_MANAGED, the state must be changed to PREPARE. The state must be changed to TEST_ALL_TRAFFIC before the loadBalancingScheme can be changed to EXTERNAL_MANAGED. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate traffic to backend buckets attached to this forwarding rule by percentage using the \--external-managed-backend-bucket-migration-testing-percentage flag. 

`EXTERNAL_MANAGED_BACKEND_BUCKET_MIGRATION_STATE` must be one of: `PREPARE`, `TEST_BY_PERCENTAGE`, `TEST_ALL_TRAFFIC`. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta compute forwarding-rules update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta compute forwarding-rules update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--global`
     If set, the forwarding rule is global. 
`--region`=`REGION`
     Region of the forwarding rule to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute forwarding-rules update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update)
    
    
    [gcloud alpha compute forwarding-rules update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/update)
    
    
    [gcloud preview compute forwarding-rules update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/forwarding-rules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-28 UTC."],[],[]] 
