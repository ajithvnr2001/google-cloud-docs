---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/tcp/dest-groups/update/
title: gcloud alpha iap tcp dest-groups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:19.524389+00:00
---

# gcloud alpha iap tcp dest-groups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/tcp/dest-groups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iap tcp dest-groups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iap tcp dest-groups update - update the IAP TCP Destination Group resource 
SYNOPSIS
    

`gcloud alpha iap tcp dest-groups update` `GROUP_NAME` `--region`=`REGION` (`--fqdn-list`=`FQDN_LIST` `--ip-range-list`=`IP_RANGE_LIST`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update the IAP TCP Destination Group resource. 
EXAMPLES
     To update a DestGroup with name ``GROUP_NAME``, in region ``REGION`` with ip ranges ``CIDR1``, ``CIDR2`` in the current project run: 
    
    
    gcloud alpha iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --ip-range-list=CIDR1,CIDR2

To update a DestGroup with name ``GROUP_NAME``, in region ``REGION`` with fqdns ``FQDN1``, ``FQDN2`` in the current project run: 
    
    
    gcloud alpha iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --fqdn-list=FQDN1,FQDN2

To update a DestGroup with name ``GROUP_NAME``, in region ``REGION`` with fqdns ``FQDN1``, ``FQDN2`` and ip ranges ``CIDR1``, ``CIDR2`` in the project ``PROJECT_ID`` run: 
    
    
    gcloud alpha iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --fqdn-list=FQDN1,FQDN2 --ip-range-list=CIDR1,CIDR2 --project=PROJECT_ID

To clear the fqdn list in a DestGroup with name ``GROUP_NAME``, in region ``REGION`` in the current project run: 
    
    
    gcloud alpha iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --fqdn-list=""

To clear the ip range list in a DestGroup with name ``GROUP_NAME``, in region ``REGION`` in the current project run: 
    
    
    gcloud alpha iap tcp dest-groups update DEST_GROUP_NAME --region=REGION --ip-range-list=""

POSITIONAL ARGUMENTS
    

`GROUP_NAME`
     Name of the Destination Group. 
REQUIRED FLAGS
    

`--region`=`REGION`
     Region of the Destination Group. 
At least one of these must be specified: 

`--fqdn-list`=`FQDN_LIST`
     List of FQDNs in the Destination Group. 
`--ip-range-list`=`IP_RANGE_LIST`
     List of ip-ranges in the Destination Group. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iap tcp dest-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/update)
    
    
    [gcloud beta iap tcp dest-groups update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/tcp/dest-groups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
