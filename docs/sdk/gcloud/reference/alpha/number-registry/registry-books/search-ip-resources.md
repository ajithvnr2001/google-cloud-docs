---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/search-ip-resources/
title: gcloud alpha number-registry registry-books search-ip-resources \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:50.820947+00:00
---

# gcloud alpha number-registry registry-books search-ip-resources  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/search-ip-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha number-registry registry-books search-ip-resources Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha number-registry registry-books search-ip-resources - search IP resources in a registry book 
SYNOPSIS
    

`gcloud alpha number-registry registry-books search-ip-resources` (`REGISTRY_BOOK` : `--location`=`LOCATION`) [`--query`=`QUERY`] [`--search-resource-types`=[`SEARCH_RESOURCE_TYPES`,…]] [`--show-utilization`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Search IP resources in a registry book using IP address, IP version, attributes, etc. 
EXAMPLES
     To search for an ip address across ranges in a registry book run: 
    
    
    gcloud alpha number-registry registry-books search-ip-resources my-registry-book --location=global --query="ip_address=10.0.0.1 AND ip_version=IPV4"

To search for a range in a registry book with text in its attributes run: 
    
    
    gcloud alpha number-registry registry-books search-ip-resources my-registry-book --location=global --query="attribute_text=foo"

To search for a range in a registry book with exact text in its attributes run: 
    
    
    gcloud alpha number-registry registry-books search-ip-resources my-registry-book --location=global --query="attribute:(foo=bar)"

To additionally show the utilization of a range in a registry book run: 
    
    
    gcloud alpha number-registry registry-books search-ip-resources my-registry-book --location=global --query="ip_address=10.0.0.1 AND ip_version=IPV4" --show-utilization

POSITIONAL ARGUMENTS
    

RegistryBook resource - The resource name of the RegistryBook to search in. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `registry_book` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REGISTRY_BOOK`
     ID of the registryBook or fully qualified identifier for the registryBook. 

To set the `registry_book` attribute: 

  * provide the argument `registry_book` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the registryBook resource. 

To set the `location` attribute: 

  * provide the argument `registry_book` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--query`=`QUERY`
     Search query. This string filters resources in an AIP-160-like format. It has some limitations. You can only specify top level conjunctions or attribute level negations. Each restriction can only be used once except the attribute restriction. 

The available restrictions for Ranges are: 

  * `resource_id`: The resource ID to search for within Ranges (only substring matching using the format `resource_id="*value*"` is supported). 
  * `realm`: The Realm name to search in. 
  * `ip_address`: The IP address to search for within Ranges. 
  * `ip_version`: The IP version to filter by (e.g., "IPV4", "IPV6"). 
  * `parent_range`: The parent Range of the Range to search for. 
  * `attribute_text`: The attribute text to search for within Ranges. 
  * `attribute`: The attribute key and value to filter by. 



The available restrictions for Realms are: 

  * `ip_version`: The IP version to search for. 
  * `management_type`: The management type of the Realm (e.g., "CNR", "USER"). 



Only one of attribute_text or multiple attribute filters can be specified. Examples: 

  * `realm=test-realm`
  * `realm=test-realm AND ip_address=10.0.0.0`
  * `realm=test-realm AND ip_version=IPV6`
  * `realm=test-realm AND resource_id="*my-range*"`
  * `realm=test-realm AND attribute_text=test`
  * `ip_address=10.0.0.0 AND attribute:(key1=value1) AND attribute:(key2=value2)`
  * `attribute_text=test AND parent_range=projects/123/locations/global/discoveredRanges/test-parent-range`
  * `management_type=CNR`


`--search-resource-types`=[`SEARCH_RESOURCE_TYPES`,…]
     The type of resources to search for. If not specified, the server will return Ranges. `SEARCH_RESOURCE_TYPES` must be one of: 

`ranges`
     Search for Ranges. 
`realms`
     Search for Realms. 
`--show-utilization`
     Whether to show the utilization of the Ranges in the response. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudnumberregistry/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/number-registry/reference/rest>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
