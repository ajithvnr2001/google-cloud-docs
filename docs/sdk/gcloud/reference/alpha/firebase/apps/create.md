---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/apps/create/
title: gcloud alpha firebase apps create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:12.871848+00:00
---

# gcloud alpha firebase apps create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/apps/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha firebase apps create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha firebase apps create - create a new Firebase application 
SYNOPSIS
    

`gcloud alpha firebase apps create` `--platform`=`PLATFORM` [`--app-store-id`=`APP_STORE_ID`] [`--bundle-id`=`BUNDLE_ID`] [`--display-name`=`DISPLAY_NAME`] [`--package-name`=`PACKAGE_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new Firebase application. 
EXAMPLES
     To create an Android app with package name `com.example.app`: 
    
    
    gcloud alpha firebase apps create --platform=android --package-name=com.example.app --display-name="My Android App"

To create an iOS app with bundle ID `com.example.app`: 
    
    
    gcloud alpha firebase apps create --platform=ios --bundle-id=com.example.app --display-name="My iOS App"

To create a Web app: 
    
    
    gcloud alpha firebase apps create --platform=web --display-name="My Web App"

REQUIRED FLAGS
    

`--platform`=`PLATFORM`
     The platform of the app to create (android, ios, web). `PLATFORM` must be one of: `android`, `ios`, `web`. 
OPTIONAL FLAGS
    

`--app-store-id`=`APP_STORE_ID`
     The App Store ID for the iOS app. 
`--bundle-id`=`BUNDLE_ID`
     The canonical bundle ID of the iOS app as it would appear in the iOS App Store. 
`--display-name`=`DISPLAY_NAME`
     The user-assigned display name of the App. 
`--package-name`=`PACKAGE_NAME`
     The package name for the Android app (e.g. com.example.my_app). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
