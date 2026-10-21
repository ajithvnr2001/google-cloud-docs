---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/clusters/import/
title: gcloud alpha container attached clusters import \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:14.337743+00:00
---

# gcloud alpha container attached clusters import  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/clusters/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container attached clusters import Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container attached clusters import - import fleet membership for an Attached cluster 
SYNOPSIS
    

`gcloud alpha container attached clusters import` `--distribution`=`DISTRIBUTION` `--platform-version`=`PLATFORM_VERSION` (`--context`=`CONTEXT` : `--kubeconfig`=`KUBECONFIG`) (`--fleet-membership`=`FLEET_MEMBERSHIP` : `--fleet-membership-location`=`FLEET_MEMBERSHIP_LOCATION`; default="global") [`--async`] [`--location`=`LOCATION`] [`--validate-only`] [`--proxy-secret-name`=`PROXY_SECRET_NAME` `--proxy-secret-namespace`=`PROXY_SECRET_NAMESPACE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Import fleet membership for an Attached cluster. 
EXAMPLES
     To import the fleet membership of an attached cluster in fleet ``FLEET_MEMBERSHIP`` managed in location ``us-west1``, run: 
    
    
    gcloud alpha container attached clusters import --location=us-west1 --platform-version=PLATFORM_VERSION --fleet-membership=FLEET_MEMBERSHIP --distribution=DISTRIBUTION --context=CLUSTER_CONTEXT --kubeconfig=KUBECONFIG_PATH

REQUIRED FLAGS
    

`--distribution`=`DISTRIBUTION`
     Set the base platform type of the cluster to attach. 

Examples: 
    
    
    gcloud alpha container attached clusters import --distribution=aks
    gcloud alpha container attached clusters import --distribution=eks
    gcloud alpha container attached clusters import --distribution=generic

`--platform-version`=`PLATFORM_VERSION`
     Platform version to use for the cluster. 

To retrieve a list of valid versions, run: 
    
    
    [gcloud alpha container attached get-server-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/attached/get-server-config) --location=LOCATION

Replace ``LOCATION`` with the target Google Cloud location for the cluster. 

kubectl config 

This must be specified. 

`--context`=`CONTEXT`
     Context to use in the kubeconfig. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--kubeconfig`=`KUBECONFIG`
     Path to the kubeconfig file. 

If not provided, the default at ~/.kube/config will be used. 

Fleet membership resource - Membership of the registered cluster. Membership can be the membership ID or the full resource name. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--fleet-membership` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--fleet-membership`=`FLEET_MEMBERSHIP`
     ID of the fleet_membership or fully qualified identifier for the fleet_membership. 

To set the `fleet_membership` attribute: 

  * provide the argument `--fleet-membership` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--fleet-membership-location`=`FLEET_MEMBERSHIP_LOCATION`; default="global"
     Google Cloud location for the fleet_membership. 

To set the `location` attribute: 

  * provide the argument `--fleet-membership` on the command line with a fully specified name; 
  * provide the argument `--fleet-membership-location` on the command line; 
  * set the property `container_attached/location`. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Location resource - Google Cloud location to import attached cluster.. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * set the property `container_attached/location` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
  * set the property `container_attached/location`. 


`--validate-only`
     Validate the cluster to import, but don't actually perform it. 
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
    
    
    [gcloud container attached clusters import](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/import)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
