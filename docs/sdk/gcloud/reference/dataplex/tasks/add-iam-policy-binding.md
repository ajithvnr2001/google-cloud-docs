---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/tasks/add-iam-policy-binding/
title: gcloud dataplex tasks add-iam-policy-binding \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:29.074329+00:00
---

# gcloud dataplex tasks add-iam-policy-binding  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/tasks/add-iam-policy-binding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataplex tasks add-iam-policy-binding Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataplex tasks add-iam-policy-binding - add IAM policy binding to a Dataplex task resource 
SYNOPSIS
    

`gcloud dataplex tasks add-iam-policy-binding` (`TASK` : `--lake`=`LAKE` `--location`=`LOCATION`) `--member`=`PRINCIPAL` `--role`=`ROLE` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Add IAM policy binding to a Dataplex task resource. 
EXAMPLES
     To add an IAM policy binding for the role of `roles/dataplex.viewer` for the user 'testuser@gmail.com' to task `test-task` within lake `test-lake` in location `us-central`, run: 
    
    
    gcloud dataplex tasks add-iam-policy-binding test-task --location=us-central1 --lake=test-lake --role=roles/dataplex.viewer --member=user:testuser@gmail.com

See <https://cloud.google.com/dataplex/docs/iam-roles> for details of policy role and member types. 

POSITIONAL ARGUMENTS
    

Tasks resource - Arguments and flags that define the Dataplex task you want to add IAM policy binding to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `task` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TASK`
     ID of the tasks or fully qualified identifier for the tasks. 

To set the `task` attribute: 

  * provide the argument `task` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--lake`=`LAKE`
     The identifier of the Dataplex lake resource. 

To set the `lake` attribute: 

  * provide the argument `task` on the command line with a fully specified name; 
  * provide the argument `--lake` on the command line. 


`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `task` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--member`=`PRINCIPAL`
     The principal to add the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`. 

Examples: `user:test-user@gmail.com`, `group:admins@example.com`, `serviceAccount:test123@example.domain.com`, or `domain:example.domain.com`. 

Some resources also accept the following special values: 

  * `allUsers` \- Special identifier that represents anyone who is on the internet, with or without a Google account. 
  * `allAuthenticatedUsers` \- Special identifier that represents anyone who is authenticated with a Google account or a service account. 


`--role`=`ROLE`
     Role name to assign to the principal. The role name is the complete path of a predefined role, such as `roles/logging.viewer`, or the role ID for a custom role, such as `organizations/{ORGANIZATION_ID}/roles/logging.viewer`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha dataplex tasks add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/tasks/add-iam-policy-binding)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
