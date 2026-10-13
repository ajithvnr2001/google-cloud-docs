---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/set-iam-policy/
title: gcloud alpha compute snapshots set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:50.357034+00:00
---

# gcloud alpha compute snapshots set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/snapshots/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute snapshots set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute snapshots set-iam-policy - set the IAM policy for a Compute Engine snapshot 
SYNOPSIS
    

`gcloud alpha compute snapshots set-iam-policy` `SNAPSHOT_NAME` `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Sets the IAM policy for the given snapshot as defined in a JSON or YAML file. 
EXAMPLES
     The following command will read am IAM policy defined in a JSON file 'policy.json' and set it for the snapshot `my-snapshot`: 
    
    
    gcloud alpha compute snapshots set-iam-policy my-snapshot policy.json

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 

POSITIONAL ARGUMENTS
    

Snapshot resource - The snapshot to set the IAM policy for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `snapshot_name` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SNAPSHOT_NAME`
     ID of the snapshot or fully qualified identifier for the snapshot. 

To set the `snapshot_name` attribute: 

  * provide the argument `snapshot_name` on the command line. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `compute/alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/compute/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute snapshots set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/set-iam-policy)
    
    
    [gcloud beta compute snapshots set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/snapshots/set-iam-policy)
    
    
    [gcloud preview compute snapshots set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/snapshots/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
