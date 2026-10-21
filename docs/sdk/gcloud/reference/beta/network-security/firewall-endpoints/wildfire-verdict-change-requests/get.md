---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/wildfire-verdict-change-requests/get/
title: gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:55:52.383518+00:00
---

# gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/wildfire-verdict-change-requests/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get - get a WildFire Verdict Change Request 
SYNOPSIS
    

`gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get` `NAME` (`--endpoint`=`ENDPOINT` : `--organization`=`ORGANIZATION` `--zone`=`ZONE`) [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get a WildFire Verdict Change Request. 
EXAMPLES
     To get a WildFire Verdict Change Request with name `req-123` and endpoint `organizations/1234/locations/us-central1-a/firewallEndpoints/my-endpoint`: 
    
    
    [gcloud beta network-security firewall-endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints) wildfire-verdict-change-requests get req-123 --endpoint=organizations/1234/locations/us-central1-a/firewallEndpoints/my-endpoint

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the verdict change request to get. 
REQUIRED FLAGS
    

Endpoint resource - The endpoint to which the verdict change request belongs. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--endpoint` on the command line with a fully specified name; 
  * set the property `core/project`. This resource can be one of the following types: [networksecurity.organizations.locations.firewallEndpoints, networksecurity.projects.locations.firewallEndpoints]. 



This must be specified. 

`--endpoint`=`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `endpoint-name` attribute: 

  * provide the argument `--endpoint` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     Organization ID of the endpoint. 

To set the `organization` attribute: 

  * provide the argument `--endpoint` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [networksecurity.organizations.locations.firewallEndpoints]. 


`--zone`=`ZONE`
     Zone of the endpoint. 

To set the `zone` attribute: 

  * provide the argument `--endpoint` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * provide the argument `--location` on the command line. 


OPTIONAL FLAGS
    

`--location`=`LOCATION`
     Location of the endpoint 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha network-security firewall-endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/firewall-endpoints) wildfire-verdict-change-requests get

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
