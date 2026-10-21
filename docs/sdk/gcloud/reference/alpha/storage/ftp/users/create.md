---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/users/create/
title: gcloud alpha storage ftp users create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:54:41.269547+00:00
---

# gcloud alpha storage ftp users create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/storage/ftp/users/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha storage ftp users create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha storage ftp users create - create a new Cloud FTP user 
SYNOPSIS
    

`gcloud alpha storage ftp users create` `USER_ID` `--customer-service-account`=`CUSTOMER_SERVICE_ACCOUNT` `--location`=`LOCATION` `--server`=`SERVER` `--storage-directory-mapping`=[`PROPERTY`=`VALUE`,…] [`--user-credentials-from-file`=`PATH_TO_FILE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Cloud FTP user for a specific server. 
EXAMPLES
     To create a user `my-user` for server `my-server` in `us-west1`, run: 
    
    
    gcloud alpha storage ftp users create my-user --server=my-server --location=us-west1 --customer-service-account=my-sa@my-project.iam.gserviceaccount.com --user-credentials-from-file=keys.json --storage-directory-mapping=bucket=my-bucket,directory=/home/user,permission=READ_WRITE

POSITIONAL ARGUMENTS
    

`USER_ID`
     The ID of the user to create. 
REQUIRED FLAGS
    

`--customer-service-account`=`CUSTOMER_SERVICE_ACCOUNT`
     The service account email associated with this user. 
`--location`=`LOCATION`
     The region of the server. 
`--server`=`SERVER`
     The ID of the server. 
`--storage-directory-mapping`=[`PROPERTY`=`VALUE`,…]
     Mapping of Google Cloud Storage bucket to virtual directory. 
OPTIONAL FLAGS
    

`--user-credentials-from-file`=`PATH_TO_FILE`
     Path to a JSON file containing user credentials. For example: [{"credentialType": "PUBLIC_KEY", "credentialName": "key1", "sshPublicKeyBody": "ssh-rsa…"}]. Use a full or relative path to a local file containing the value of user_credentials. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
