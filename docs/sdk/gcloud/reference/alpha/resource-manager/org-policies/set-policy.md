---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/org-policies/set-policy/
title: gcloud alpha resource-manager org-policies set-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:59.664666+00:00
---

# gcloud alpha resource-manager org-policies set-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/org-policies/set-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha resource-manager org-policies set-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha resource-manager org-policies set-policy - set Organization Policy 
SYNOPSIS
    

`gcloud alpha resource-manager org-policies set-policy` `POLICY_FILE` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Sets an Organization Policy associated with the specified resource from a file that contains the JSON or YAML encoded Organization Policy. 
EXAMPLES
     Organization policy list constraint YAML file example: 
    
    
    constraint: constraints/CONSTRAINT_NAME
    listPolicy:
      deniedValues:
      - VALUE_A

Organization policy list constraint JSON file example: 
    
    
    {
      "constraint": "constraints/CONSTRAINT_NAME",
      "listPolicy": {
        "deniedValues": ["VALUE_A"]
      }
    }

The following command sets an Organization Policy for a constraint on project `foo-project` from file `/tmp/policy.yaml`: 
    
    
    gcloud alpha resource-manager org-policies set-policy --project=foo-project /tmp/policy.yaml

POSITIONAL ARGUMENTS
    

`POLICY_FILE`
     JSON or YAML file with the Organization Policy. 
REQUIRED FLAGS
    

Resource that is associated with the organization policy. 

Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder ID. 
`--organization`=`ORGANIZATION_ID`
     Organization ID. 
`--project`=`PROJECT_ID`
     Project ID. Overrides the default `core/project` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud resource-manager org-policies set-policy](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy)
    
    
    [gcloud beta resource-manager org-policies set-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/org-policies/set-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
