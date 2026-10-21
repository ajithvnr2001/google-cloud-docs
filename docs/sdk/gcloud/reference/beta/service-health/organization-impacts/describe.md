---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-health/organization-impacts/describe/
title: gcloud beta service-health organization-impacts describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:02.635822+00:00
---

# gcloud beta service-health organization-impacts describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-health/organization-impacts/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta service-health organization-impacts describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta service-health organization-impacts describe - get details of an asset impact by an event under an organization 
SYNOPSIS
    

`gcloud beta service-health organization-impacts describe` (`ORGANIZATION_IMPACT` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Retrieves a resource containing information about impact to an asset under an organization affected by a service health event. 

To retrieve impact for service health incident events, use location `global`. 

EXAMPLES
     To get the details of organization impact `my-impact` in location `global` for organization `123456789`, run: 
    
    
    gcloud beta service-health organization-impacts describe my-impact --organization=123456789 --location=global

POSITIONAL ARGUMENTS
    

OrganizationImpact resource - Name of the resource using the form `organizations/{organization_id}/locations/global/organizationImpacts/{organization_impact_id}`. 

`organization_id` \- ID (number) of the organization that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 

`organization_impact_id` \- ID of the [OrganizationImpact resource](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact). The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`ORGANIZATION_IMPACT`
     ID of the organizationImpact or fully qualified identifier for the organizationImpact. 

To set the `organization_impact` attribute: 

  * provide the argument `organization_impact` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location to use when working with Service Health resources. 

If not specified, will use `default` servicehealth/location. To set the `location` attribute: 

  * provide the argument `organization_impact` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `servicehealth/location`. 


`--organization`=`ORGANIZATION`
     The organization id of the organizationImpact resource. 

To set the `organization` attribute: 

  * provide the argument `organization_impact` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `servicehealth/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/service-health/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud service-health organization-impacts describe](https://docs.cloud.google.com/sdk/gcloud/reference/service-health/organization-impacts/describe)
    
    
    [gcloud alpha service-health organization-impacts describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-health/organization-impacts/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
