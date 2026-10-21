---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/artifact-guard/policies/update/
title: gcloud alpha scc artifact-guard policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:10.885162+00:00
---

# gcloud alpha scc artifact-guard policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/artifact-guard/policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha scc artifact-guard policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha scc artifact-guard policies update - update an existing artifact guard policy 
SYNOPSIS
    

`gcloud alpha scc artifact-guard policies update` (`POLICY` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--policy-file-path`=`PATH_TO_FILE` [`--allow-missing`] [`--update-mask`=`UPDATE_MASK`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Updates an existing artifact guard policy. Update Mask: It updates the policy with the fields specified in the update mask. If the update mask is not specified or is set to "`", all the fields are updated. Partial field updates are not supported. The following fields are supported: 

  * "display_name" 
  * "description" 
  * "scope" 
  * "enablement_state" 
  * "vulnerability_policy" 
  * "annotations" 

`
EXAMPLES
     To update a policy named "organizations/123/locations/global/policies/myPolicy",
    
    
    gcloud alpha scc artifact-guard policies update organizations/123/locations/global/policies/myPolicy --policy-file-path=policy.yaml OR
    gcloud alpha scc artifact-guard policies update myPolicy --location=global --organization=123 --policy-file-path=policy.yaml

POSITIONAL ARGUMENTS
    

Policy resource - The full name of the policy to update. The parent of the policy can be either an organization or a project. For example: `organizations/123/locations/global/policies/myPolicy` or `projects/123/locations/global/policies/myPolicy`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [artifactscanguard.organizations.locations.policies, artifactscanguard.projects.locations.policies]. 



This must be specified. 

`POLICY`
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     ID of the location where the resource exists (for example, global). To set the `location` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     Organization ID. To set the `organization` attribute: 

  * provide the argument `policy` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [artifactscanguard.organizations.locations.policies]. 


REQUIRED FLAGS
    

`--policy-file-path`=`PATH_TO_FILE`
     YAML file containing the body of the policy to be created. Use a full or relative path to a local file containing the value of policy_file_path. 
OPTIONAL FLAGS
    

`--allow-missing`
     If set, the policy will be created if it does not exist. 
`--update-mask`=`UPDATE_MASK`
     The list of fields to update. Eg: "description,display_name" 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `artifactscanguard/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/security-command-center>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
