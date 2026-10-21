---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/managed-zones/update/
title: gcloud beta dns managed-zones update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:30:22.788196+00:00
---

# gcloud beta dns managed-zones update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dns/managed-zones/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dns managed-zones update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dns managed-zones update - update an existing Cloud DNS managed-zone 
SYNOPSIS
    

`gcloud beta dns managed-zones update` `ZONE` [`--async`] [`--denial-of-existence`=`DENIAL_OF_EXISTENCE`] [`--description`=`DESCRIPTION`] [`--dnssec-state`=`DNSSEC_STATE`] [`--forwarding-targets`=[`IP_ADDRESSES`,…]] [`--gkeclusters`=[`GKECLUSTERS`,…]] [`--ksk-algorithm`=`KSK_ALGORITHM`] [`--ksk-key-length`=`KSK_KEY_LENGTH`] [`--location`=`LOCATION`] [`--[no-]log-dns-queries`] [`--managed-reverse-lookup`] [`--networks`=[`NETWORK`,…]] [`--outbound-endpoints`=[`OUTBOUND_ENDPOINTS`,…]] [`--private-forwarding-targets`=[`IP_ADDRESSES`,…]] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--zsk-algorithm`=`ZSK_ALGORITHM`] [`--zsk-key-length`=`ZSK_KEY_LENGTH`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--target-network`=`TARGET_NETWORK` `--target-project`=`TARGET_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update an existing Cloud DNS managed-zone. 
EXAMPLES
     To change the description of a managed-zone, run: 
    
    
    gcloud beta dns managed-zones update my-zone --description="Hello, world!"

To change the description of a zonal managed-zone in us-east1-a, run: 
    
    
    gcloud beta dns managed-zones update my-zone --description="Hello, world!" --location=us-east1-a

POSITIONAL ARGUMENTS
    

Zone resource - The name of the managed-zone to be updated. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `zone` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ZONE`
     ID of the zone or fully qualified identifier for the zone. 

To set the `zone` attribute: 

  * provide the argument `zone` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--denial-of-existence`=`DENIAL_OF_EXISTENCE`
     Requires DNSSEC enabled. `DENIAL_OF_EXISTENCE` must be one of: `nsec`, `nsec3`. 
`--description`=`DESCRIPTION`
     Short description for the managed zone. 
`--dnssec-state`=`DNSSEC_STATE`
     The DNSSEC state for this managed zone. `DNSSEC_STATE` must be one of: 

`off`
     Disable DNSSEC for the managed zone. 
`on`
     Enable DNSSEC for the managed zone. 
`transfer`
     Enable DNSSEC and allow transferring a signed zone in or out. 
`--forwarding-targets`=[`IP_ADDRESSES`,…]
     List of IPv4/IPv6 addresses or one domain name of the target name server that the zone will forward queries to. Ignored for `public` visibility. Non-RFC1918 addresses will forward to the target through the Internet. RFC1918 addresses will forward through the VPC. 
`--gkeclusters`=[`GKECLUSTERS`,…]
     List of GKE clusters that the zone should be visible in if the zone visibility is [private]. 
`--ksk-algorithm`=`KSK_ALGORITHM`
     String mnemonic specifying the DNSSEC algorithm of the key-signing key. Requires DNSSEC enabled. `KSK_ALGORITHM` must be one of: `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, `rsasha512`. 
`--ksk-key-length`=`KSK_KEY_LENGTH`
     Length of the key-signing key in bits. Requires DNSSEC enabled. 
`--location`=`LOCATION`
     Specifies the desired service location the request is sent to. Defaults to Cloud DNS global service. Use --location=global if you want to target the global service. 
`--[no-]log-dns-queries`
     Specifies whether to enable query logging. Defaults to False. Use `--log-dns-queries` to enable and `--no-log-dns-queries` to disable. 
`--managed-reverse-lookup`
     Specifies whether this zone is a managed reverse lookup zone, required for Cloud DNS to correctly resolve Non-RFC1918 PTR records. 
`--networks`=[`NETWORK`,…]
     List of networks that the zone should be visible in if the zone visibility is [private]. 
`--outbound-endpoints`=[`OUTBOUND_ENDPOINTS`,…]
     List of outbound endpoints to use for forwarding queries. Specify either the outbound endpoint name formatted as `locations/LOCATION/outboundEndpoints/NAME` or the full resource path `projects/PROJECT/locations/LOCATION/outboundEndpoints/NAME`. 
`--private-forwarding-targets`=[`IP_ADDRESSES`,…]
     List of IPv4/IPv6 addresses or one domain name of the target name server that the zone will forward queries to. Ignored for `public` visibility. All addresses specified for this parameter will be reached through the VPC. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--zsk-algorithm`=`ZSK_ALGORITHM`
     String mnemonic specifying the DNSSEC algorithm of the key-signing key. Requires DNSSEC enabled. `ZSK_ALGORITHM` must be one of: `ecdsap256sha256`, `ecdsap384sha384`, `rsasha1`, `rsasha256`, `rsasha512`. 
`--zsk-key-length`=`ZSK_KEY_LENGTH`
     Length of the zone-signing key in bits. Requires DNSSEC enabled. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta dns managed-zones update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta dns managed-zones update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
`--target-network`=`TARGET_NETWORK`
     Network ID of the Google Compute Engine private network to forward queries to. 
`--target-project`=`TARGET_PROJECT`
     Project ID of the Google Compute Engine private network to forward queries to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud dns managed-zones update](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/update)
    
    
    [gcloud alpha dns managed-zones update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dns/managed-zones/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
