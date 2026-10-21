---
url: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/set-iam-policy/
title: gcloud data-catalog taxonomies policy-tags set-iam-policy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:08.633622+00:00
---

# gcloud data-catalog taxonomies policy-tags set-iam-policy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/set-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud data-catalog taxonomies policy-tags set-iam-policy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud data-catalog taxonomies policy-tags set-iam-policy - set the IAM policy for a Data Catalog Policy Tag 
SYNOPSIS
    

`gcloud data-catalog taxonomies policy-tags set-iam-policy` (`POLICY_TAG` : `--location`=`LOCATION` `--taxonomy`=`TAXONOMY`) `POLICY_FILE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Set the IAM policy for the given Data Catalog Policy Tag as defined in a JSON or YAML file. 
EXAMPLES
     The following command will read am IAM policy defined in a JSON file 'policy.json' and set it for the Policy Tag 'POLICY_TAG' with location 'LOCATION' in the taxonomy 'TAXONOMY': 
    
    
    gcloud data-catalog taxonomies policy-tags set-iam-policy POLICY_TAG --location=LOCATION --taxonomy=TAXONOMY policy.json

See <https://cloud.google.com/iam/docs/managing-policies> for details of the policy file format and contents. 

POSITIONAL ARGUMENTS
    

Policy tag resource - Policy tag for which to set the IAM policy. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy_tag` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`POLICY_TAG`
     ID of the policy tag or fully qualified identifier for the policy tag. 

To set the `policy_tag` attribute: 

  * provide the argument `policy_tag` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the policy tag. To set the `location` attribute: 

  * provide the argument `policy_tag` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--taxonomy`=`TAXONOMY`
     Taxonomy of the policy tag. To set the `taxonomy` attribute: 

  * provide the argument `policy_tag` on the command line with a fully specified name; 
  * provide the argument `--taxonomy` on the command line. 


`POLICY_FILE`
     Path to a local JSON or YAML formatted file containing a valid policy. 

The output of the `get-iam-policy` command is a valid file, as is any JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha data-catalog taxonomies policy-tags set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/taxonomies/policy-tags/set-iam-policy)
    
    
    [gcloud beta data-catalog taxonomies policy-tags set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/taxonomies/policy-tags/set-iam-policy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
