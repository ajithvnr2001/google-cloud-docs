---
url: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/remove-iam-policy-binding/
title: gcloud data-catalog taxonomies policy-tags remove-iam-policy-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:08.889604+00:00
---

# gcloud data-catalog taxonomies policy-tags remove-iam-policy-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags/remove-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud data-catalog taxonomies policy-tags remove-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud data-catalog taxonomies policy-tags remove-iam-policy-binding - remove an IAM policy binding from a Data Catalog policy tag 
SYNOPSIS
    

`gcloud data-catalog taxonomies policy-tags remove-iam-policy-binding` (`POLICY_TAG` : `--location`=`LOCATION` `--taxonomy`=`TAXONOMY`) `--member`=`PRINCIPAL` `--role`=`ROLE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Remove an IAM policy binding from a Data Catalog policy tag. 
EXAMPLES
     To remove an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on policy tag 'POLICY_TAG' in location 'LOCATION' and taxonomy 'TAXONOMY', run: 
    
    
    [gcloud data-catalog taxonomies policy-tags](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags) remove-iam-policy-binding POLICY_TAG --location='LOCATION' --taxonomy='TAXONOMY' --member='user:test-user@gmail.com' --role='roles/editor'

To remove an IAM policy binding for the role of 'roles/editor' from all authenticated users on policy tag 'POLICY_TAG' in location 'LOCATION' and taxonomy 'TAXONOMY', run: 
    
    
    [gcloud data-catalog taxonomies policy-tags](https://docs.cloud.google.com/sdk/gcloud/reference/data-catalog/taxonomies/policy-tags) remove-iam-policy-binding POLICY_TAG --location='LOCATION' --taxonomy='TAXONOMY' --member='allAuthenticatedUsers' --role='roles/editor'

See <https://cloud.google.com/iam/docs/managing-policies> for details of policy role and member types. 

POSITIONAL ARGUMENTS
    

Policy tag resource - Policy tag from which to remove the IAM policy binding. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

`--member`=`PRINCIPAL`
     The principal to remove the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`. 

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`. 

Deleted principals have an additional `deleted:` prefix and a `?uid=UID` suffix, where ``UID`` is a unique identifier for the principal. Example: `deleted:user:test-user@gmail.com?uid=123456789012345678901`. 

Some resources also accept the following special values: 

  * `allUsers` \- Special identifier that represents anyone who is on the internet, with or without a Google account. 
  * `allAuthenticatedUsers` \- Special identifier that represents anyone who is authenticated with a Google account or a service account. 


`--role`=`ROLE`
     The role to remove the principal from. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `datacatalog/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/data-catalog/docs/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha data-catalog taxonomies policy-tags](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/data-catalog/taxonomies/policy-tags) remove-iam-policy-binding
    
    
    [gcloud beta data-catalog taxonomies policy-tags](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-catalog/taxonomies/policy-tags) remove-iam-policy-binding

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
