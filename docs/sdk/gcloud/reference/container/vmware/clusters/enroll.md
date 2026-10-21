---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/enroll/
title: gcloud container vmware clusters enroll \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:34:46.782159+00:00
---

# gcloud container vmware clusters enroll  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/vmware/clusters/enroll/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container vmware clusters enroll Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container vmware clusters enroll - enroll an Anthos cluster on VMware 
SYNOPSIS
    

`gcloud container vmware clusters enroll` (`CLUSTER` : `--location`=`LOCATION`) (`--admin-cluster-membership`=`ADMIN_CLUSTER_MEMBERSHIP` : `--admin-cluster-membership-location`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION` `--admin-cluster-membership-project`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`) [`--async`] [`--local-name`=`LOCAL_NAME`] [`--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Enroll an Anthos cluster on VMware. 
EXAMPLES
     To enroll a cluster named ``my-cluster`` managed in location ``us-west1`` with admin cluster membership of ``projects/my-project/locations/us-west1/memberships/my-admin-cluster-membership``, run: 
    
    
    gcloud container vmware clusters enroll my-cluster --location=us-west1 --admin-cluster-membership=projects/my-project/locations/us-west1/memberships/my-admin-cluster-membership

POSITIONAL ARGUMENTS
    

Cluster resource - cluster to enroll The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--location`=`LOCATION`
     Google Cloud location for the cluster. 

To set the `location` attribute: 

  * provide the argument `cluster` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `container_vmware/location`. 


REQUIRED FLAGS
    

Admin cluster membership resource - membership of the admin cluster. Membership name is the same as the admin cluster name. 

Examples: 
    
    
    gcloud container vmware clusters enroll
          --admin-cluster-membership=projects/example-project-12345/locations/us-west1/memberships/example-admin-cluster-name

or 
    
    
    gcloud container vmware clusters enroll
          --admin-cluster-membership-project=example-project-12345
          --admin-cluster-membership-location=us-west1
          --admin-cluster-membership=example-admin-cluster-name
    
    
    The arguments in this group can be used to specify the attributes of this resource.

This must be specified. 

`--admin-cluster-membership`=`ADMIN_CLUSTER_MEMBERSHIP`
     ID of the admin_cluster_membership or fully qualified identifier for the admin_cluster_membership. 

To set the `admin_cluster_membership` attribute: 

  * provide the argument `--admin-cluster-membership` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--admin-cluster-membership-location`=`ADMIN_CLUSTER_MEMBERSHIP_LOCATION`
     Google Cloud location for the admin_cluster_membership. 

To set the `location` attribute: 

  * provide the argument `--admin-cluster-membership` on the command line with a fully specified name; 
  * provide the argument `--admin-cluster-membership-location` on the command line. 


`--admin-cluster-membership-project`=`ADMIN_CLUSTER_MEMBERSHIP_PROJECT`
     Google Cloud project for the admin_cluster_membership. 

To set the `project` attribute: 

  * provide the argument `--admin-cluster-membership` on the command line with a fully specified name; 
  * provide the argument `--admin-cluster-membership-project` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--local-name`=`LOCAL_NAME`
     The object name of the VMware OnPremUserCluster custom resource on the associated admin cluster. This field is used to support conflicting resource names when enrolling existing clusters to the API. When not provided, this field will resolve to the vmware_cluster_id. Otherwise, it must match the object name of the VMware OnPremUserCluster custom resource. It is not modifiable outside / beyond the enrollment operation. 
`--validate-only`
     If set, only validate the request, but do not actually perform the operation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha container vmware clusters enroll](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/vmware/clusters/enroll)
    
    
    [gcloud beta container vmware clusters enroll](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/vmware/clusters/enroll)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
