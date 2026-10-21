---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/replace-all/
title: gcloud beta access-context-manager levels replace-all \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:35.804873+00:00
---

# gcloud beta access-context-manager levels replace-all  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/replace-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-context-manager levels replace-all Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-context-manager levels replace-all - replace all existing access levels 
SYNOPSIS
    

`gcloud beta access-context-manager levels replace-all` [`POLICY`] `--source-file`=`SOURCE_FILE` [`--etag`=`ETAG`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Replace all existing access level in specified access policy with access levels specified in a file. 
EXAMPLES
     To replace all levels within a policy, using etag: 
    
    
    gcloud beta access-context-manager levels replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-access-levels.yaml --etag=optional-latest-etag-of-policy

To replace all levels within a policy, without using etag: 
    
    
    gcloud beta access-context-manager levels replace-all my-policy-number --source-file=path-to-file-containing-all-replacement-access-levels.yaml

POSITIONAL ARGUMENTS
    

Policy resource - The access policy that contains the levels you want to replace. This represents a Cloud resource. 
[`POLICY`]
     ID of the policy or fully qualified identifier for the policy. 

To set the `policy` attribute: 

  * provide the argument `policy` on the command line; 
  * set the property `access_context_manager/policy`; 
  * automatically, if the current account belongs to an organization with exactly one access policy.. 


REQUIRED FLAGS
    

`--source-file`=`SOURCE_FILE`
     Path to a file containing a list of access levels. 

An access level file is a YAML-formatted list of access levels, which are YAML objects representing a Basic or Custom level as described in the API reference. For example: 
    
    
    - name: accessPolicies/my_policy/accessLevels/my_level
      title: My Basic Level
      description: Basic level for foo.
      basic:
        combiningFunction: AND
        conditions:
        - ipSubnetworks:
          - 192.168.100.14/24
          - 2001:db8::/48
        - members
          - user1:user1@example.com
    - name: accessPolicies/my_policy/accessLevels/my_other_level
      title: My Other Custom Level
      description: Custom level for bar.
      custom:
        expr:
          expression: "origin.region_code in ['US', 'CA']"

For more information about the alpha version, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.accessLevels> For other versions, see: <https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels>

OPTIONAL FLAGS
    

`--etag`=`ETAG`
     An etag which specifies the version of the Access Policy. Only etags that represent the latest version of the Access Policy will be accepted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `accesscontextmanager/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/access-context-manager/docs/reference/rest/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-context-manager levels replace-all](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/levels/replace-all)
    
    
    [gcloud alpha access-context-manager levels replace-all](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/levels/replace-all)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
