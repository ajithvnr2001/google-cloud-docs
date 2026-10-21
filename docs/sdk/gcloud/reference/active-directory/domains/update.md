---
url: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/update/
title: gcloud active-directory domains update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:34.342969+00:00
---

# gcloud active-directory domains update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud active-directory domains update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud active-directory domains update - update a Managed Microsoft AD domain 
SYNOPSIS
    

`gcloud active-directory domains update` `DOMAIN` [`--async`] [`--enable-audit-logs`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--add-authorized-networks`=[`AUTH_NET1`, `AUTH_NET2`, …,…] | `--remove-authorized-networks`=[`AUTH_NET1`, `AUTH_NET2`, …,…]] [`--add-region`=`ADD_REGION` | `--remove-region`=`REMOVE_REGION`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the metadata and/or configuration parameters of a managed Microsoft AD domain. 

This command can fail for the following reasons: 

  * The AD domain specified does not exist. 
  * The active account does not have permission to update the given AD domain. 


EXAMPLES
     The following command updates an AD domain with the name `my-domain.com` to add the two labels, `env` and `service` and to add a provisioned region `us-west1`: 
    
    
    gcloud active-directory domains update my-domain.com --update-labels=env=test,service=foo --add-region=us-west1

This peers the domain `my-domain.com` to the network `my-network`. 
    
    
    gcloud active-directory domains update my-domain.com --add-authorized-networks=projects/my-project/global/networks/my-network

POSITIONAL ARGUMENTS
    

Domain resource - Name of the Managed Microsoft AD domain you want to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `domain` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DOMAIN`
     ID of the domain or fully qualified identifier for the domain. 

To set the `domain` attribute: 

  * provide the argument `domain` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--enable-audit-logs`
     If specified, Active Directory data audit logs are enabled for the domain. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--add-authorized-networks`=[`AUTH_NET1`, `AUTH_NET2`, …,…]
     A list of URLs of additional networks to peer this domain to in the form projects/{project}/global/networks/{network}. Networks must belong to the project. 
`--remove-authorized-networks`=[`AUTH_NET1`, `AUTH_NET2`, …,…]
     A list of URLs of additional networks to unpeer this domain from in the form projects/{project}/global/networks/{network}. Networks must belong to the project. 
At most one of these can be specified: 

`--add-region`=`ADD_REGION`
     An additional region to provision this domain in. If domain is already provisioned in region, nothing will be done in that region. Supported regions are: asia-east1, asia-northeast1, asia-south1, asia-southeast1, australia-southeast1, europe-north1, europe-west1, europe-west2, europe-west3, europe-west4, northamerica-northeast1, southamerica-east1, us-central1, us-east1, us-east4, us-west1, us-west2. 
`--remove-region`=`REMOVE_REGION`
     A region to de-provision this domain from. If domain is already not provisioned in a region, nothing will be done in that region. Domains must be left provisioned in at least one region. Supported regions are: asia-east1, asia-northeast1, asia-south1, asia-southeast1, australia-southeast1, europe-north1, europe-west1, europe-west2, europe-west3, europe-west4, northamerica-northeast1, southamerica-east1, us-central1, us-east1, us-east4, us-west1, us-west2. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud active-directory domains update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud active-directory domains update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha active-directory domains update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/update)
    
    
    [gcloud beta active-directory domains update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
