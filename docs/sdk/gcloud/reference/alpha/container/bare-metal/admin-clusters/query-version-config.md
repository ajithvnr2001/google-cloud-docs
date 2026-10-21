---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/admin-clusters/query-version-config/
title: gcloud alpha container bare-metal admin-clusters query-version-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:35.568709+00:00
---

# gcloud alpha container bare-metal admin-clusters query-version-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/admin-clusters/query-version-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container bare-metal admin-clusters query-version-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container bare-metal admin-clusters query-version-config - query versions for creating or upgrading an Anthos on bare metal admin cluster 
SYNOPSIS
    

`gcloud alpha container bare-metal admin-clusters query-version-config` [`--admin-cluster`=`ADMIN_CLUSTER`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Query versions for creating or upgrading an Anthos on bare metal admin cluster. 
EXAMPLES
     To query versions for creating an admin cluster in location `us-west1`, run: 
    
    
    [gcloud alpha container bare-metal admin-clusters](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/admin-clusters) query-version-config --location=us-west1

To query versions for upgrading an admin cluster named `my-admin-cluster` in location `us-west1`, run: 
    
    
    [gcloud alpha container bare-metal admin-clusters](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/admin-clusters) query-version-config --location=us-west1 --admin-cluster=my-admin-cluster

FLAGS
    

Use cases for querying versions. 
Upgrade an Anthos on bare metal admin cluster use case. 
Admin cluster resource - Admin cluster to query versions for upgrade. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--admin-cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--admin-cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_bare_metal/location`. 


`--admin-cluster`=`ADMIN_CLUSTER`
     ID of the admin_cluster or fully qualified identifier for the admin_cluster. 

To set the `admin_cluster` attribute: 

  * provide the argument `--admin-cluster` on the command line. 


Location resource - Google Cloud location to query versions. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * set the property `container_bare_metal/location` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
  * set the property `container_bare_metal/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container bare-metal admin-clusters query-version-config](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/admin-clusters/query-version-config)
    
    
    [gcloud beta container bare-metal admin-clusters](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/admin-clusters) query-version-config

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
