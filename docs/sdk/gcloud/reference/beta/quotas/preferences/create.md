---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/preferences/create/
title: gcloud beta quotas preferences create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:22:17.951470+00:00
---

# gcloud beta quotas preferences create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/preferences/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta quotas preferences create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta quotas preferences create - create a new QuotaPreference that declares the desired value for a quota 
SYNOPSIS
    

`gcloud beta quotas preferences create` `--preferred-value`=`PREFERRED_VALUE` `--quota-id`=`QUOTA_ID` `--service`=`SERVICE` (`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID_OR_NUMBER`) [`--allow-high-percentage-quota-decrease`] [`--allow-quota-decrease-below-usage`] [`--dimensions`=[`KEY`=`VALUE`,…]] [`--email`=`EMAIL`] [`--justification`=`JUSTIFICATION`] [`--preference-id`=`PREFERENCE_ID`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a quota preference in region `us-central1` that applies to the `default_limit` quota under service `example.googleapis.com` for `projects/12321`, run: 
    
    
    gcloud beta quotas preferences create --service=example.googleapis.com --project=12321 --quota-id=default_limit --preferred-value=100 --dimensions=region=us-central1 --preference-id=example_default-limit_us-central1

To create a quota preference under service `example.googleapis.com` for `organizations/789` with random preference ID, run: 
    
    
    gcloud beta quotas preferences create --service=example.googleapis.com --organization=789 --quota-id=default_limit --preferred-value=200

REQUIRED FLAGS
    

`--preferred-value`=`PREFERRED_VALUE`
     Preferred value. Must be greater than or equal to -1. If set to -1, it means the value is "unlimited". 
`--quota-id`=`QUOTA_ID`
     ID of the quota, which is unique within the service. 
`--service`=`SERVICE`
     Name of the service in which the quota is defined. 
Exactly one of these must be specified: 

`--folder`=`FOLDER_ID`
     Folder of the quota preference to create. 
`--organization`=`ORGANIZATION_ID`
     Organization of the quota preference to create. 
`--project`=`PROJECT_ID_OR_NUMBER`
     Project of the quota preference to create. 
OPTIONAL FLAGS
    

`--allow-high-percentage-quota-decrease`
     If specified, allows you to reduce your effective limit by more than 10 percent. Default is false. 
`--allow-quota-decrease-below-usage`
     If specified, allows you to reduce your effective limit below your quota usage. Default is false. 
`--dimensions`=[`KEY`=`VALUE`,…]
     Dimensions of the quota. 
`--email`=`EMAIL`
     An optional email address that can be used for quota related communication between the Google Cloud and the user in case the Google Cloud needs further information to make a decision on whether the user preferred quota can be granted. The Google account for the email address must have quota update permission for the project, folder or organization this quota preference is for. If no contact email address is provided, or the provided email address does not have the required quota update permission, the quota preference request will be denied in case further information is required to make a decision. 
`--justification`=`JUSTIFICATION`
     A short statement to justify quota increase requests. 
`--preference-id`=`PREFERENCE_ID`
     ID of the Quota Preference object, must be unique under its parent. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud quotas preferences create](https://docs.cloud.google.com/sdk/gcloud/reference/quotas/preferences/create)
    
    
    [gcloud alpha quotas preferences create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/quotas/preferences/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
