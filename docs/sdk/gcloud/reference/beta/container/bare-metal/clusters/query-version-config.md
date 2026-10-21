---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/clusters/query-version-config/
title: gcloud beta container bare-metal clusters query-version-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:21.710282+00:00
---

# gcloud beta container bare-metal clusters query-version-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/bare-metal/clusters/query-version-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container bare-metal clusters query-version-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container bare-metal clusters query-version-config - query versions for creating or upgrading an Anthos on bare metal user cluster 
SYNOPSIS
    

`gcloud beta container bare-metal clusters query-version-config` [`--location`=`LOCATION`] [`--cluster`=`CLUSTER` | [`--admin-cluster-membership`=`ADMIN_CLUSTER_MEMBERSHIP` : `--admin-cluster-membership-location`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION`; default="global" `--admin-cluster-membership-project`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Query versions for creating or upgrading an Anthos on bare metal user cluster. 
EXAMPLES
     To query all available versions in location `us-west1`, run: 
    
    
    gcloud beta container bare-metal clusters query-version-config --location=us-west1

To query versions for creating a cluster with an admin cluster membership named `my-admin-cluster-membership` managed in project `my-admin-cluster-project` and location `us-west`, run: 
    
    
    gcloud beta container bare-metal clusters query-version-config --location=us-west1 --admin-cluster-membership=my-admin-cluster-membership --admin-cluster-membership-project=my-admin-cluster-project

To query versions for upgrading a user cluster named `my-user-cluster` in location `us-west1`, run: 
    
    
    gcloud beta container bare-metal clusters query-version-config --location=us-west1 --cluster=my-user-cluster

FLAGS
    

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


Use cases for querying versions. 

At most one of these can be specified: 

Upgrade an Anthos on bare metal user cluster use case. 
Cluster resource - Cluster to query versions for upgrade. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--cluster` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_bare_metal/location`. 


`--cluster`=`CLUSTER`
     ID of the cluster or fully qualified identifier for the cluster. 

To set the `cluster` attribute: 

  * provide the argument `--cluster` on the command line. 


Create an Anthos on bare metal user cluster use case. 
Admin cluster membership resource - membership of the admin cluster to query versions for create. Membership name is the same as the admin cluster name. 

Examples: 
    
    
    gcloud beta container bare-metal clusters query-version-config
          --admin-cluster-membership=projects/example-project-12345/locations/us-west1/memberships/example-admin-cluster-name

or 
    
    
    gcloud beta container bare-metal clusters query-version-config
          --admin-cluster-membership-project=example-project-12345
          --admin-cluster-membership-location=us-west1
          --admin-cluster-membership=example-admin-cluster-name
    
    
    The arguments in this group can be used to specify the attributes of this resource.

`--admin-cluster-membership`=`ADMIN_CLUSTER_MEMBERSHIP`
     ID of the admin_cluster_membership or fully qualified identifier for the admin_cluster_membership. 

To set the `admin_cluster_membership` attribute: 

  * provide the argument `--admin-cluster-membership` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--admin-cluster-membership-location`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION`; default="global"
     Google Cloud location for the admin_cluster_membership. 

To set the `location` attribute: 

  * provide the argument `--admin-cluster-membership` on the command line with a fully specified name; 
  * provide the argument `--admin-cluster-membership-location` on the command line. 


`--admin-cluster-membership-project`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`
     Project ID of the Google Cloud project for the admin_cluster_membership. 

To set the `project` attribute: 

  * provide the argument `--admin-cluster-membership` on the command line with a fully specified name; 
  * provide the argument `--admin-cluster-membership-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container bare-metal clusters query-version-config](https://docs.cloud.google.com/sdk/gcloud/reference/container/bare-metal/clusters/query-version-config)
    
    
    [gcloud alpha container bare-metal clusters query-version-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/bare-metal/clusters/query-version-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
