---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/remove-iam-policy-binding/
title: gcloud beta ai-platform models remove-iam-policy-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:15.485608+00:00
---

# gcloud beta ai-platform models remove-iam-policy-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/remove-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai-platform models remove-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai-platform models remove-iam-policy-binding - remove IAM policy binding for a model 
SYNOPSIS
    

`gcloud beta ai-platform models remove-iam-policy-binding` `MODEL` `--member`=`PRINCIPAL` `--role`=`ROLE` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Removes a policy binding from an AI Platform Model. One binding consists of a member, a role and an optional condition. See $ [gcloud beta ai-platform models get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/models/get-iam-policy) for examples of how to specify a model resource. 
EXAMPLES
     To remove an IAM policy binding for the role of `roles/ml.admin` for the user `test-user@gmail.com` on model with identifier `my_model`, run: 
    
    
    gcloud beta ai-platform models remove-iam-policy-binding my_model --member='user:test-user@gmail.com' --role='roles/ml.admin'

To remove an IAM policy binding for the role of `roles/ml.admin` from all authenticated users on model `my_model`, run: 
    
    
    gcloud beta ai-platform models remove-iam-policy-binding my_model --member='allAuthenticatedUsers' --role='roles/ml.admin'

See <https://cloud.google.com/iam/docs/managing-policies> for details of policy role and member types. 

POSITIONAL ARGUMENTS
    

Model resource - The AI Platform model for which to remove IAM policy binding from. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `model` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MODEL`
     ID of the model or fully qualified identifier for the model. 

To set the `name` attribute: 

  * provide the argument `model` on the command line. 


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
OPTIONAL FLAGS
    

`--region`=`REGION`
     Google Cloud region of the regional endpoint to use for this command. For the global endpoint, the region needs to be specified as `global`. 

Learn more about regional endpoints and see a list of available regions: <https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints>

`REGION` must be one of: `global`, `asia-east1`, `asia-northeast1`, `asia-southeast1`, `australia-southeast1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `northamerica-northeast1`, `us-central1`, `us-east1`, `us-east4`, `us-west1`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai-platform models remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/models/remove-iam-policy-binding)
    
    
    [gcloud alpha ai-platform models remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/models/remove-iam-policy-binding)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
