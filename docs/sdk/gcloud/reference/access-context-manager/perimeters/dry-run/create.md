---
url: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/create/
title: gcloud access-context-manager perimeters dry-run create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:13.228071+00:00
---

# gcloud access-context-manager perimeters dry-run create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud access-context-manager perimeters dry-run create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud access-context-manager perimeters dry-run create - create a dry-run mode configuration for a new or existing Service Perimeter 
SYNOPSIS
    

`gcloud access-context-manager perimeters dry-run create` (`PERIMETER` : `--policy`=`POLICY`) (`--access-levels`=[`access_levels`,…] `--egress-policies`=`YAML_FILE` `--ingress-policies`=`YAML_FILE` `--resources`=[`resources`,…] `--restricted-services`=[`restricted_services`,…] `--vpc-accessible-services`=`VPC_ACCESSIBLE_SERVICES_YAML_FILE` | `--enable-vpc-accessible-services` `--vpc-allowed-services`=[`vpc_allowed_services`,…] | [`--perimeter-title`=`PERIMETER_TITLE` `--perimeter-type`=`PERIMETER_TYPE` : `--perimeter-access-levels`=[`access_levels`,…] `--perimeter-description`=`PERIMETER_DESCRIPTION` `--perimeter-egress-policies`=`YAML_FILE` `--perimeter-ingress-policies`=`YAML_FILE` `--perimeter-resources`=[`resources`,…] `--perimeter-restricted-services`=[`restricted_services`,…] `--perimeter-vpc-accessible-services`=`VPC_ACCESSIBLE_SERVICES_YAML_FILE` | `--perimeter-enable-vpc-accessible-services` `--perimeter-vpc-allowed-services`=[`vpc_allowed_services`,…]]) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     When a Service Perimeter with the specified name does not exist, a new Service Perimeter will be created. In this case, the newly created Service Perimeter will not have any enforcement mode configuration, and, therefore, all policy violations will be logged. 

When a perimeter with the specified name does exist, a dry-run mode configuration will be created for it. The behavior of the enforcement mode configuration, if present, will not be impacted in this case. Requests that violate the existing enforcement mode configuration of the Service Perimeter will continue being denied. Requests that only violate the policy in the dry-run mode configuration will be logged but will not be denied. 

EXAMPLES
     To create a dry-run configuration for an existing Service Perimeter: 
    
    
    gcloud access-context-manager perimeters dry-run create my-perimeter --resources="projects/0123456789" --access-levels="accessPolicies/a_policy/accessLevels/a_level" --restricted-services="storage.googleapis.com"

To create a dry-run configuration for a new Service Perimeter: 
    
    
    gcloud access-context-manager perimeters dry-run create my-perimeter --perimeter-title="My New Perimeter" --perimeter-description="Perimeter description" --perimeter-type="regular" --perimeter-resources="projects/0123456789" --perimeter-access-levels="accessPolicies/a_policy/accessLevels/a_level" --perimeter-restricted-services="storage.googleapis.com"

POSITIONAL ARGUMENTS
    

Perimeter resource - The service perimeter to update. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`PERIMETER`
     ID of the perimeter or fully qualified identifier for the perimeter. 

To set the `perimeter` attribute: 

  * provide the argument `perimeter` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     The ID of the access policy. 

To set the `policy` attribute: 

  * provide the argument `perimeter` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line; 
  * set the property `access_context_manager/policy`. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

Arguments for creating dry-run spec for an **existing** Service Perimeter. 
`--access-levels`=[`access_levels`,…]
     Comma-separated list of IDs for access levels (in the same policy) that an intra-perimeter request must satisfy to be allowed. 
`--egress-policies`=`YAML_FILE`
     Path to a file containing a list of Egress Policies. This file contains a list of YAML-compliant objects representing Egress Policies described in the API reference. For more information about the alpha version, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters> For more information about non-alpha versions, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters>
`--ingress-policies`=`YAML_FILE`
     Path to a file containing a list of Ingress Policies. This file contains a list of YAML-compliant objects representing Ingress Policies described in the API reference. For more information about the alpha version, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters> For more information about non-alpha versions, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters>
`--resources`=[`resources`,…]
     Comma-separated list of resources (currently only projects, in the form `projects/<projectnumber>`) in this perimeter. 
`--restricted-services`=[`restricted_services`,…]
     Comma-separated list of services to which the perimeter boundary `does` apply (for example, `storage.googleapis.com`). 
At most one of these can be specified: 

`--vpc-accessible-services`=`VPC_ACCESSIBLE_SERVICES_YAML_FILE`
     Path to a YAML file containing a VpcAccessibleServices object. 
Or at least one of these can be specified: 

`--enable-vpc-accessible-services`
     Whether to restrict API calls within the perimeter to those in the `vpc-allowed-services` list. 
`--vpc-allowed-services`=[`vpc_allowed_services`,…]
     Comma-separated list of APIs accessible from within the Service Perimeter. In order to include all restricted services, use reference "RESTRICTED-SERVICES". Requires vpc-accessible-services be enabled. 
Arguments for creating a dry-run spec for a new Service Perimeter. 
`--perimeter-title`=`PERIMETER_TITLE`
     Short human-readable title for the Service Perimeter. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--perimeter-type`=`PERIMETER_TYPE`
     Type of the perimeter. 
    
    
    A *regular* perimeter allows resources within this service perimeter
    to import and export data amongst themselves. A project may belong
    to at most one regular service perimeter.
    
    
    A *bridge* perimeter allows resources in different regular service
    perimeters to import and export data between each other. A project
    may belong to multiple bridge service perimeters (only if it also
    belongs to a regular service perimeter). Both restricted and
    unrestricted service lists, as well as access level lists, must be
    empty.

This flag argument must be specified if any of the other arguments in this group are specified. 

`--perimeter-access-levels`=[`access_levels`,…]
     Comma-separated list of IDs for access levels (in the same policy) that an intra-perimeter request must satisfy to be allowed. 
`--perimeter-description`=`PERIMETER_DESCRIPTION`
     Long-form description of Service Perimeter. 
`--perimeter-egress-policies`=`YAML_FILE`
     Path to a file containing a list of Egress Policies. This file contains a list of YAML-compliant objects representing Egress Policies described in the API reference. For more information about the alpha version, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters> For more information about non-alpha versions, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters>
`--perimeter-ingress-policies`=`YAML_FILE`
     Path to a file containing a list of Ingress Policies. This file contains a list of YAML-compliant objects representing Ingress Policies described in the API reference. For more information about the alpha version, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters> For more information about non-alpha versions, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters>
`--perimeter-resources`=[`resources`,…]
     Comma-separated list of resources (currently only projects, in the form `projects/<projectnumber>`) in this perimeter. 
`--perimeter-restricted-services`=[`restricted_services`,…]
     Comma-separated list of services to which the perimeter boundary `does` apply (for example, `storage.googleapis.com`). 
At most one of these can be specified: 

`--perimeter-vpc-accessible-services`=`VPC_ACCESSIBLE_SERVICES_YAML_FILE`
     Path to a YAML file containing a VpcAccessibleServices object. 
Or at least one of these can be specified: 

`--perimeter-enable-vpc-accessible-services`
     Whether to restrict API calls within the perimeter to those in the `vpc-allowed-services` list. 
`--perimeter-vpc-allowed-services`=[`vpc_allowed_services`,…]
     Comma-separated list of APIs accessible from within the Service Perimeter. In order to include all restricted services, use reference "RESTRICTED-SERVICES". Requires vpc-accessible-services be enabled. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha access-context-manager perimeters dry-run create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/create)
    
    
    [gcloud beta access-context-manager perimeters dry-run create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
