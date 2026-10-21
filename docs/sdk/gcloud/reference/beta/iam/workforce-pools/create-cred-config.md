---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/create-cred-config/
title: gcloud beta iam workforce-pools create-cred-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:50.053974+00:00
---

# gcloud beta iam workforce-pools create-cred-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/create-cred-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam workforce-pools create-cred-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam workforce-pools create-cred-config - create a configuration file for generated credentials 
SYNOPSIS
    

`gcloud beta iam workforce-pools create-cred-config` `AUDIENCE` `--output-file`=`OUTPUT_FILE` `--workforce-pool-user-project`=`WORKFORCE_POOL_USER_PROJECT` (`--credential-source-file`=`CREDENTIAL_SOURCE_FILE` | `--credential-source-url`=`CREDENTIAL_SOURCE_URL` | `--executable-command`=`EXECUTABLE_COMMAND`) [`--credential-source-field-name`=`CREDENTIAL_SOURCE_FIELD_NAME`] [`--credential-source-headers`=[`key`=`value`,…]] [`--credential-source-type`=`CREDENTIAL_SOURCE_TYPE`] [`--subject-token-type`=`SUBJECT_TOKEN_TYPE`] [`--executable-interactive-timeout-millis`=`EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS` `--executable-output-file`=`EXECUTABLE_OUTPUT_FILE` `--executable-timeout-millis`=`EXECUTABLE_TIMEOUT_MILLIS`] [`--service-account`=`SERVICE_ACCOUNT` : `--service-account-token-lifetime-seconds`=`SERVICE_ACCOUNT_TOKEN_LIFETIME_SECONDS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command creates a configuration file to allow access to authenticated Google Cloud actions from a variety of external user accounts. 
EXAMPLES
     To create a file-sourced credential configuration by using the short-format audience, run: 
    
    
    gcloud beta iam workforce-pools create-cred-config $WORKFORCE_POOL_ID/$PROVIDER_ID --credential-source-file=$PATH_TO_OIDC_ID_TOKEN --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json

To create a file-sourced credential configuration by using the full resource name audience, run: 
    
    
    gcloud beta iam workforce-pools create-cred-config locations/$REGION/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID --credential-source-file=$PATH_TO_OIDC_ID_TOKEN --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json

To create a URL-sourced credential configuration for your project, run: 
    
    
    gcloud beta iam workforce-pools create-cred-config $WORKFORCE_POOL_ID/$PROVIDER_ID --credential-source-url=$URL_FOR_OIDC_TOKEN --credential-source-headers=Key=Value --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json

To create an executable-source credential configuration for your project, run the following command: 
    
    
    gcloud beta iam workforce-pools create-cred-config $WORKFORCE_POOL_ID/$PROVIDER_ID --executable-command=$EXECUTABLE_COMMAND --executable-timeout-millis=30000 --executable-output-file=$CACHE_FILE --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json

To use the resulting file for any of these commands, set the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the generated file. 

POSITIONAL ARGUMENTS
    

`AUDIENCE`
     The workforce pool provider resource name in the format "<pool>/<provider>" or "locations/<location>/workforcePools/<pool>/providers/<provider>". 
REQUIRED FLAGS
    

`--output-file`=`OUTPUT_FILE`
     Location to store the generated credential configuration file. 
`--workforce-pool-user-project`=`WORKFORCE_POOL_USER_PROJECT`
     The client project number used to identify the application (client project) to the server when calling Google APIs. The user principal must have serviceusage.services.use IAM permission to use the specified project. 
Credential types. 

Exactly one of these must be specified: 

`--credential-source-file`=`CREDENTIAL_SOURCE_FILE`
     The location of the file which stores the credential. 
`--credential-source-url`=`CREDENTIAL_SOURCE_URL`
     The URL to obtain the credential from. 
`--executable-command`=`EXECUTABLE_COMMAND`
     The full command to run to retrieve the credential. Must be an absolute path for the program including arguments. 
OPTIONAL FLAGS
    

`--credential-source-field-name`=`CREDENTIAL_SOURCE_FIELD_NAME`
     Subject token field name (key) in a JSON credential source. 
`--credential-source-headers`=[`key`=`value`,…]
     Headers to use when querying the credential-source-url. 
`--credential-source-type`=`CREDENTIAL_SOURCE_TYPE`
     Format of the credential source (JSON or text). 
`--subject-token-type`=`SUBJECT_TOKEN_TYPE`
     The type of token being used for authorization. This defaults to urn:ietf:params:oauth:token-type:id_token. 
Arguments for an executable type credential source. 
`--executable-interactive-timeout-millis`=`EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS`
     Timeout duration, in milliseconds, to wait for the executable to finish when the command is running in interactive mode. 
`--executable-output-file`=`EXECUTABLE_OUTPUT_FILE`
     Absolute path to the file storing the executable response. 
`--executable-timeout-millis`=`EXECUTABLE_TIMEOUT_MILLIS`
     Timeout duration, in milliseconds, to wait for the executable to finish. 
Service account impersonation options. 
`--service-account`=`SERVICE_ACCOUNT`
     Email of the service account to impersonate. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--service-account-token-lifetime-seconds`=`SERVICE_ACCOUNT_TOKEN_LIFETIME_SECONDS`
     Lifetime duration of the service account access token in seconds. Defaults to one hour if not specified. If a lifetime greater than one hour is required, the service account must be added as an allowed value in an Organization Policy that enforces the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` constraint. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iam workforce-pools create-cred-config](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config)
    
    
    [gcloud alpha iam workforce-pools create-cred-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/create-cred-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
