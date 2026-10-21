---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/dns-threat-detectors/create/
title: gcloud network-security dns-threat-detectors create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:19.856559+00:00
---

# gcloud network-security dns-threat-detectors create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/dns-threat-detectors/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security dns-threat-detectors create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security dns-threat-detectors create - create a DnsThreatDetector resource 
SYNOPSIS
    

`gcloud network-security dns-threat-detectors create` (`DNS_THREAT_DETECTOR` : `--location`=`LOCATION`) `--provider`=`PROVIDER` [`--excluded-networks`=[`EXCLUDED_NETWORKS`,…]] [`--labels`=[`LABELS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a DnsThreatDetector resource. 
EXAMPLES
     To create `DnsThreatDetector` resource `my-dns-threat-detector`, and using the Infoblox threat detection engine, run: 
    
    
    gcloud network-security dns-threat-detectors create --location=global --provider=infoblox my-dns-threat-detector

POSITIONAL ARGUMENTS
    

DnsThreatDetector resource - Identifier. Name of the DnsThreatDetector resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `dns_threat_detector` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DNS_THREAT_DETECTOR`
     ID of the dnsThreatDetector or fully qualified identifier for the dnsThreatDetector. 

To set the `dns_threat_detector` attribute: 

  * provide the argument `dns_threat_detector` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the dnsThreatDetector resource. 

To set the `location` attribute: 

  * provide the argument `dns_threat_detector` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--provider`=`PROVIDER`
     The provider used for DNS threat analysis. `PROVIDER` must be (only one value is supported): 

`infoblox`
     The Infoblox DNS threat detector provider. 
OPTIONAL FLAGS
    

Network resource - A list of network resource names which aren't monitored by this DnsThreatDetector. 

Example: `projects/PROJECT_ID/global/networks/NETWORK_NAME`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--excluded-networks` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--excluded-networks`=[`EXCLUDED_NETWORKS`,…]
     IDs of the networks or fully qualified identifiers for the networks. 

To set the `network` attribute: 

  * provide the argument `--excluded-networks` on the command line. 


`--labels`=[`LABELS`,…]
     Any labels associated with the DnsThreatDetector, listed as key value pairs. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security dns-threat-detectors create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/dns-threat-detectors/create)
    
    
    [gcloud beta network-security dns-threat-detectors create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/dns-threat-detectors/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
