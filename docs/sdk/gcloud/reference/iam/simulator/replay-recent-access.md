---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access/
title: gcloud iam simulator replay-recent-access \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:00:30.935138+00:00
---

# gcloud iam simulator replay-recent-access  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/simulator/replay-recent-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam simulator replay-recent-access Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam simulator replay-recent-access - determine affected recent access attempts before IAM policy change deployment 
SYNOPSIS
    

`gcloud iam simulator replay-recent-access` `RESOURCE` `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Replay the most recent 1,000 access logs from the past 90 days using the simulated policy. For each log entry, the replay determines if setting the provided policy on the given resource would result in a change in the access state, e.g. a previously granted access becoming denied. Any differences found are returned. 
EXAMPLES
     To simulate a permission change of a member on a resource, run: 
    
    
    gcloud iam simulator replay-recent-access projects/project-id path/to/policy_file.json

See <https://cloud.google.com/iam/docs/managing-policies> for details of policy role and member types. 

POSITIONAL ARGUMENTS
    

`RESOURCE`
     Full resource name to simulate the IAM policy for. 

See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>. 

`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a Policy. See [the Policy reference](https://cloud.google.com/iam/reference/rest/v1/Policy) for details. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
