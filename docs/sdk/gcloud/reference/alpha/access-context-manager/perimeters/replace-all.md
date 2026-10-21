---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/replace-all/
title: gcloud alpha access-context-manager perimeters replace-all \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:25.914698+00:00
---

# gcloud alpha access-context-manager perimeters replace-all  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/replace-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha access-context-manager perimeters replace-all Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha access-context-manager perimeters replace-all - replace all existing service perimeters 
SYNOPSIS
    

`gcloud alpha access-context-manager perimeters replace-all` [`POLICY`] `--source-file`=`SOURCE_FILE` [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Replace all existing service perimeter in specified access policy with service perimeters specified in a file. 
EXAMPLES
     To replace all perimeters within a policy, using etag: 
    
    
    gcloud alpha access-context-manager perimeters replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-service-perimeters.yaml --etag=optional-latest-etag-of-policy

To replace all perimeters within a policy, without using etag: 
    
    
    gcloud alpha access-context-manager perimeters replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-service-perimeters.yaml

POSITIONAL ARGUMENTS
    

Policy resource - The access policy that contains the perimeters you want to replace. This represents a Cloud resource. 
[`POLICY`]
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy` on the command line; 
  * set the property `access_context_manager/policy`; 
  * automatically, if the current account belongs to an organization with exactly one access policy.. 


REQUIRED FLAGS
    

`--source-file`=`SOURCE_FILE`
     Path to a file containing a list of service perimeters. 

An service perimeter file is a YAML-formatted list of service perimeters, which are YAML objects representing a Condition as described in the API reference. For example: 
    
    
    - name: my_perimeter
      title: My Perimeter
      description: Perimeter for foo.
      perimeterType: PERIMETER_TYPE_REGULAR
      status:
        resources:
        - projects/0123456789
        accessLevels:
        - accessPolicies/my_policy/accessLevels/my_level
        restrictedServices:
        - storage.googleapis.com

For more information about the alpha version, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters> For other versions, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters>

OPTIONAL FLAGS
    

`--etag`=`ETAG`
     An etag which specifies the version of the Access Policy. Only etags that represent the latest version of the Access Policy will be accepted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud access-context-manager perimeters replace-all](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/replace-all)
    
    
    [gcloud beta access-context-manager perimeters replace-all](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/replace-all)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
