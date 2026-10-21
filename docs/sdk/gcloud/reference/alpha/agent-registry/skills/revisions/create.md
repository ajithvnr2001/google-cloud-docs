---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/revisions/create/
title: gcloud alpha agent-registry skills revisions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:42:05.110116+00:00
---

# gcloud alpha agent-registry skills revisions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/revisions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha agent-registry skills revisions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha agent-registry skills revisions create - create skillRevisions 
SYNOPSIS
    

`gcloud alpha agent-registry skills revisions create` (`REVISION` : `--location`=`LOCATION` `--skill`=`SKILL`) [`--async`] [`--request-id`=`REQUEST_ID`] [`--payload`=`PAYLOAD` | [`--gcs-source-uri`=`GCS_SOURCE_URI` : `--gcs-source-generation`=`GCS_SOURCE_GENERATION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a skillRevision 
EXAMPLES
     To create the skillRevision, run: 
    
    
    gcloud alpha agent-registry skills revisions create

POSITIONAL ARGUMENTS
    

Revision resource - Identifier. Resource name of the SkillRevision. Format: `projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `revision` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the revision resource. 

To set the `location` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--skill`=`SKILL`
     The skill id of the revision resource. 

To set the `skill` attribute: 

  * provide the argument `revision` on the command line with a fully specified name; 
  * provide the argument `--skill` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--request-id`=`REQUEST_ID`
     Signed UUID request idempotency token. 
Arguments for the source. 

At most one of these can be specified: 

Direct write-only raw archive payload upload. 
`--payload`=`PAYLOAD`
     Local path to the ZIP archive payload containing the skill. 
Specifications for Cloud Storage objects. 
`--gcs-source-uri`=`GCS_SOURCE_URI`
     Cloud Storage object URI. Format: `gs://{bucket_name}/{object_name}`

This flag argument must be specified if any of the other arguments in this group are specified. 

`--gcs-source-generation`=`GCS_SOURCE_GENERATION`
     Cloud Storage object generation ID. If not specified, the latest generation is used. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentregistry/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/agent-registry/overview>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
