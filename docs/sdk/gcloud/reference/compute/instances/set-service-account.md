---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account/
title: gcloud compute instances set-service-account \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:01:49.759046+00:00
---

# gcloud compute instances set-service-account  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instances set-service-account Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instances set-service-account - set a service account and access scopes for a Compute Engine VM instance 
SYNOPSIS
    

`gcloud compute instances set-service-account` `INSTANCE_NAME` [`--zone`=`ZONE`] [`--scopes`=[`SCOPE`,…] | `--no-scopes`] [`--service-account`=`SERVICE_ACCOUNT` | `--no-service-account`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instances set-service-account` lets you configure a service account and access scopes for a Compute Engine VM instance. 

As a best practice, grant the ``cloud-platform`` access scope on your VM instance. Then, to restrict resource access, grant only the required IAM roles to the VM instance's service account. For more information, see <https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes#best_practices>. 

EXAMPLES
     To set a service account with the ``cloud-platform`` scope, run: 
    
    
    gcloud compute instances set-service-account example-instance --scopes=cloud-platform --zone=us-central1-b --service-account=example-account

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--scopes`=[`SCOPE`,…]
     If not provided, the instance will keep the scopes it currently has. 

SCOPE can be either the full URI of the scope or an alias. `Default` scopes are assigned to all instances. Available aliases are: 

> Alias | URI  
> ---|---  
> bigquery | https://www.googleapis.com/auth/bigquery  
> cloud-platform | https://www.googleapis.com/auth/cloud-platform  
> cloud-source-repos | https://www.googleapis.com/auth/source.full_control  
> cloud-source-repos-ro | https://www.googleapis.com/auth/source.read_only  
> compute-ro | https://www.googleapis.com/auth/compute.readonly  
> compute-rw | https://www.googleapis.com/auth/compute  
> datastore | https://www.googleapis.com/auth/datastore  
> default | https://www.googleapis.com/auth/devstorage.read_only  
> | https://www.googleapis.com/auth/logging.write  
> | https://www.googleapis.com/auth/monitoring.write  
> | https://www.googleapis.com/auth/pubsub  
> | https://www.googleapis.com/auth/service.management.readonly  
> | https://www.googleapis.com/auth/servicecontrol  
> | https://www.googleapis.com/auth/trace.append  
> gke-default | https://www.googleapis.com/auth/devstorage.read_only  
> | https://www.googleapis.com/auth/logging.write  
> | https://www.googleapis.com/auth/monitoring  
> | https://www.googleapis.com/auth/service.management.readonly  
> | https://www.googleapis.com/auth/servicecontrol  
> | https://www.googleapis.com/auth/trace.append  
> logging-write | https://www.googleapis.com/auth/logging.write  
> monitoring | https://www.googleapis.com/auth/monitoring  
> monitoring-read | https://www.googleapis.com/auth/monitoring.read  
> monitoring-write | https://www.googleapis.com/auth/monitoring.write  
> pubsub | https://www.googleapis.com/auth/pubsub  
> service-control | https://www.googleapis.com/auth/servicecontrol  
> service-management | https://www.googleapis.com/auth/service.management.readonly  
> sql (deprecated) | https://www.googleapis.com/auth/sqlservice  
> sql-admin | https://www.googleapis.com/auth/sqlservice.admin  
> storage-full | https://www.googleapis.com/auth/devstorage.full_control  
> storage-ro | https://www.googleapis.com/auth/devstorage.read_only  
> storage-rw | https://www.googleapis.com/auth/devstorage.read_write  
> taskqueue | https://www.googleapis.com/auth/taskqueue  
> trace | https://www.googleapis.com/auth/trace.append  
> userinfo-email | https://www.googleapis.com/auth/userinfo.email  
  
DEPRECATION WARNING: <https://www.googleapis.com/auth/sqlservice> account scope and `sql` alias do not provide SQL instance management capabilities and have been deprecated. Please, use <https://www.googleapis.com/auth/sqlservice.admin> or `sql-admin` to manage your Google SQL Service instances. 
`--no-scopes`
     Remove all scopes from the instance 
At most one of these can be specified: 

`--service-account`=`SERVICE_ACCOUNT`
     A service account is an identity attached to the instance. Its access tokens can be accessed through the instance metadata server and are used to authenticate applications on the instance. The account can be set using an email address corresponding to the required service account. You can explicitly specify the Compute Engine default service account using the 'default' alias. 

If not provided, the instance will use the service account it currently has. 

`--no-service-account`
     Remove service account from the instance 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud preview compute instances set-service-account](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/set-service-account)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
