---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/clusters/update/
title: gcloud alpha container attached clusters update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:15.006479+00:00
---

# gcloud alpha container attached clusters update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/clusters/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container attached clusters update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container attached clusters update - update an Attached cluster 
SYNOPSIS
    

`gcloud alpha container attached clusters update` (`CLUSTER` : `--location`=`LOCATION`) [`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]] [`--async`] [`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`] [`--clear-description`] [`--description`=`DESCRIPTION`] [`--logging`=`COMPONENT`,[`COMPONENT`,…]] [`--platform-version`=`PLATFORM_VERSION`] [`--validate-only`] [`--admin-groups`=[`GROUP`,…] | `--clear-admin-groups`] [`--admin-users`=[`USER`,…] | `--clear-admin-users`] [`--disable-cloud-monitoring` | `--enable-cloud-monitoring`] [`--disable-managed-prometheus` | `--enable-managed-prometheus`] [`--proxy-secret-name`=`PROXY_SECRET_NAME` `--proxy-secret-namespace`=`PROXY_SECRET_NAMESPACE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update an Attached cluster. 
EXAMPLES
     To update a cluster named ``my-cluster`` managed in location ``us-west1``, run: 
    
    
    gcloud alpha container attached clusters update my-cluster --location=us-west1 --description=testcluster

POSITIONAL ARGUMENTS
    

Cluster resource - cluster to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
  * set the property `container_attached/location`. 


FLAGS
    

`--annotations`=`ANNOTATION`,[`ANNOTATION`,…]
     Annotations for the cluster. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`
     Set Binary Authorization evaluation mode for this cluster. `BINAUTHZ_EVALUATION_MODE` must be one of: `DISABLED`, `PROJECT_SINGLETON_POLICY_ENFORCE`. 
`--clear-description`
     Clear the description for the cluster. 
`--description`=`DESCRIPTION`
     Description for the cluster. 
`--logging`=`COMPONENT`,[`COMPONENT`,…]
     Set the components that have logging enabled. 

Examples: 
    
    
    gcloud alpha container attached clusters update --logging=SYSTEM
    gcloud alpha container attached clusters update --logging=SYSTEM,WORKLOAD
    gcloud alpha container attached clusters update --logging=NONE

`COMPONENT` must be one of: `NONE`, `SYSTEM`, `WORKLOAD`. 

`--platform-version`=`PLATFORM_VERSION`
     Platform version to use for the cluster. 

To retrieve a list of valid versions, run: 
    
    
    [gcloud alpha container attached get-server-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/get-server-config) --location=LOCATION

Replace ``LOCATION`` with the target Google Cloud location for the cluster. 

`--validate-only`
     Validate the update of the cluster, but don't actually perform it. 
Admin groups 

At most one of these can be specified: 

`--admin-groups`=[`GROUP`,…]
     Groups of users that can perform operations as a cluster administrator. 
`--clear-admin-groups`
     Clear the admin groups associated with the cluster 
Admin users 

At most one of these can be specified: 

`--admin-users`=[`USER`,…]
     Users that can perform operations as a cluster administrator. 
`--clear-admin-users`
     Clear the admin users associated with the cluster 
Cloud Monitoring Config 

At most one of these can be specified: 

`--disable-cloud-monitoring`
     Disable managed collection for Cloud Monitoring. 
`--enable-cloud-monitoring`
     Enable managed collection for Cloud Monitoring. 
Monitoring Config 

At most one of these can be specified: 

`--disable-managed-prometheus`
     Disable managed collection for Managed Service for Prometheus. 
`--enable-managed-prometheus`
     Enable managed collection for Managed Service for Prometheus. 
Proxy config 
`--proxy-secret-name`=`PROXY_SECRET_NAME`
     Name of the Kubernetes secret that contains the HTTP/HTTPS proxy configuration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--proxy-secret-namespace`=`PROXY_SECRET_NAMESPACE`
     Namespace of the Kubernetes secret that contains the HTTP/HTTPS proxy configuration. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud container attached clusters update](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
