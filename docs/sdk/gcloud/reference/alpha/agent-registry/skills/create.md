---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/create/
title: gcloud alpha agent-registry skills create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:08.168790+00:00
---

# gcloud alpha agent-registry skills create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/agent-registry/skills/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha agent-registry skills create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha agent-registry skills create - create skills 
SYNOPSIS
    

`gcloud alpha agent-registry skills create` `SKILL` [`--async`] [`--default-revision`=`DEFAULT_REVISION`] [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--location`=`LOCATION`] [`--publisher`=`PUBLISHER`] [`--request-id`=`REQUEST_ID`] [`--target-state`=`TARGET_STATE`] [`--type`=`TYPE`] [`--initial-revision-name`=`INITIAL_REVISION_NAME` `--payload`=`PAYLOAD` | [`--gcs-source-uri`=`GCS_SOURCE_URI` : `--gcs-source-generation`=`GCS_SOURCE_GENERATION`]] [`--scanning-policy`=`SCANNING_POLICY` | `--scanning-state`=`SCANNING_STATE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a skill 
EXAMPLES
     To create the skill, run: 
    
    
    gcloud alpha agent-registry skills create

POSITIONAL ARGUMENTS
    

Skill resource - Identifier. Resource name of the Skill. Format: `projects/{project}/locations/{location}/skills/{skill}` The `{skill}` segment acts as the resource ID. If the skill is associated with a Publisher, this segment typically uses a hyphenated namespace prefix corresponding to the publisher (e.g., `google-workspace-create-docs`). This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `skill` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `skill` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`SKILL`
     ID of the skill or fully qualified identifier for the skill. 

To set the `skill` attribute: 

  * provide the argument `skill` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
Revision resource - The full resource name of the revision currently served by default (floating track). Format: `projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}` This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--default-revision` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--default-revision` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



To set the `skill` attribute: 

  * provide the argument `--default-revision` on the command line with a fully specified name. 


`--default-revision`=`DEFAULT_REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `--default-revision` on the command line. 


`--description`=`DESCRIPTION`
     Brief summary describing the capabilities of the skill. Maximum length is 2048 characters. 
`--display-name`=`DISPLAY_NAME`
     Human-readable display name of the skill. Maximum length is 128 characters. 
`--location`=`LOCATION`
     For resources [skill, default-revision, publisher], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Publisher resource - The publisher resource associated with this skill. Format: `projects/{project}/locations/{location}/publishers/{publisher}` The publisher dictates the allowed namespace prefixes for the skill's name and logical `skill_id` (e.g., Publisher `google` authorizes the `google-*` prefix). This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--publisher` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--publisher` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--publisher`=`PUBLISHER`
     ID of the publisher or fully qualified identifier for the publisher. 

To set the `publisher` attribute: 

  * provide the argument `--publisher` on the command line. 


`--request-id`=`REQUEST_ID`
     Signed UUID request idempotency token. 
`--target-state`=`TARGET_STATE`
     User-managed target state of the skill. `TARGET_STATE` must be one of: 

`active`
     The skill is active. 
`decommissioned`
     The skill is decommissioned. 
`deprecated`
     The skill is deprecated. 
`disabled`
     The skill is disabled. 
`draft`
     The skill is in draft. 
`target-state-active`
     The skill is active and can be served. 
`target-state-decommissioned`
     The skill is decommissioned and cannot be served. 
`target-state-deprecated`
     The skill is deprecated. It can still be served, but emits warnings. 
`target-state-disabled`
     The skill is disabled and cannot be served. 
`target-state-draft`
     The skill is in draft and cannot be served. 
`--type`=`TYPE`
     Structural deployment type (SIMPLE leaf vs COMPOSITE bundle). `TYPE` must be (only one value is supported): 

`simple`
     A standard, leaf executable skill containing natural language and code. 
Represents an immutable, versioned snapshot of a Skill package. 
`--initial-revision-name`=`INITIAL_REVISION_NAME`
     Identifier. Resource name of the SkillRevision. Format: `projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}`
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
Scanning configuration for the skill. 

At most one of these can be specified: 

`--scanning-policy`=`SCANNING_POLICY`
     Scanning policy for security analysis. `SCANNING_POLICY` must be one of: 

`disabled`
     Bypasses security scanning entirely. 
`enabled-blocking`
     Scans skills and blocks revision download/promotion if findings are detected. 
`enabled-nonblocking`
     Scans skills and reports findings without blocking download/promotion. 
`--scanning-state`=`SCANNING_STATE`
     Scanning policy for security analysis (alias for --scanning-policy). `SCANNING_STATE` must be one of: 

`disabled`
     Bypasses security scanning entirely. 
`enabled-blocking`
     Scans skills and blocks revision download/promotion if findings are detected. 
`enabled-nonblocking`
     Scans skills and reports findings without blocking download/promotion. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `agentregistry/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/agent-registry/overview>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
