---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/units/create/
title: gcloud beta app-lifecycle-manager units create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:43.853605+00:00
---

# gcloud beta app-lifecycle-manager units create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/units/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager units create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager units create - create a Unit 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager units create` `UNIT` [`--application`=`APPLICATION`] [`--flag-revisions`=[`FLAG_REVISIONS`,…]] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--maintenance-pinned-until-time`=`MAINTENANCE_PINNED_UNTIL_TIME`] [`--management-mode`=`MANAGEMENT_MODE`] [`--tenant`=`TENANT`] [`--unit-kind`=`UNIT_KIND`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Unit 
EXAMPLES
     To create the Unit, run: 
    
    
    gcloud beta app-lifecycle-manager units create

POSITIONAL ARGUMENTS
    

Unit resource - Identifier. The resource name (full URI of the resource) following the standard naming scheme: 
    
    
    "projects/{project}/locations/{location}/units/{unit}" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `unit` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `unit` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`UNIT`
     ID of the unit or fully qualified identifier for the unit. 

To set the `unit` attribute: 

  * provide the argument `unit` on the command line. 


FLAGS
    

`--application`=`APPLICATION`
     Reference to the AppHub Application this unit belongs to. All resources deployed in this Unit will be associated with the specified Application. 
FlagRevision resource - List of flag revisions used by this unit This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--flag-revisions` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--flag-revisions` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--flag-revisions`=[`FLAG_REVISIONS`,…]
     IDs of the flagRevisions or fully qualified identifiers for the flagRevisions. 

To set the `flag-revision` attribute: 

  * provide the argument `--flag-revisions` on the command line. 


`--labels`=[`LABELS`,…]
     The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels. 

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

`--location`=`LOCATION`
     For resources [unit, flag-revisions, tenant, unit-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Captures requested directives for performing future maintenance on the unit. This includes a request for the unit to skip maintenance for a period of time and remain pinned to its current release as well as controls for postponing maintenance scheduled in future. 
`--maintenance-pinned-until-time`=`MAINTENANCE_PINNED_UNTIL_TIME`
     If present, it fixes the release on the unit until the given time; i.e. changes to the release field will be rejected. Rollouts should and will also respect this by not requesting an upgrade in the first place. 
`--management-mode`=`MANAGEMENT_MODE`
     Indicates whether the Unit life cycle is controlled by the user or by the system. Immutable once created. `MANAGEMENT_MODE` must be one of: 

`system`
     The system will decide when to deprovision and delete the unit. User still can deprovision or delete the unit manually. 
`user`
     Unit's lifecycle is managed by the user. 
Tenant resource - Reference to the Saas Tenant resource this unit belongs to. This for example informs the maintenance policies to use for scheduling future updates on a unit. (optional and immutable once created) This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--tenant` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--tenant` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--tenant`=`TENANT`
     ID of the tenant or fully qualified identifier for the tenant. 

To set the `tenant` attribute: 

  * provide the argument `--tenant` on the command line. 


UnitKind resource - Reference to the UnitKind this Unit belongs to (required and immutable once created). This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--unit-kind`=`UNIT_KIND`
     ID of the unitKind or fully qualified identifier for the unitKind. 

To set the `unit-kind` attribute: 

  * provide the argument `--unit-kind` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `saasservicemgmt/v1beta1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/app-lifecycle-manager>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
