---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/api-keys/create/
title: gcloud alpha services api-keys create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:18.959749+00:00
---

# gcloud alpha services api-keys create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/api-keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha services api-keys create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha services api-keys create - create an API key 
SYNOPSIS
    

`gcloud alpha services api-keys create` [`--annotations`=[`KEY`=`VALUE`,…]] [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--key-id`=`KEY_ID`] [`--service-account`=`SERVICE_ACCOUNT`] [`--api-target`=`service`=`SERVICE`[,`methods`=`METHOD`:…],[…] `--allowed-application`=[`sha1_fingerprint`=`SHA1_FINGERPRINT`,`package_name`=`PACKAGE_NAME`,…] | `--allowed-bundle-ids`=[`ALLOWED_BUNDLE_IDS`,…] | `--allowed-ips`=[`ALLOWED_IPS`,…] | `--allowed-referrers`=[`ALLOWED_REFERRERS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an API key. 
EXAMPLES
     To create a key with display name, allowed IPs, and allowed API targets specified: 
    
    
    gcloud alpha services api-keys create --display-name="test name" --allowed-ips=2620:15c:2c4:203:2776:1f90:6b3b:217,104.133.8.78 --api-target=service=bar.googleapis.com

To create a key with annotations and allowed API targets: 
    
    
    gcloud alpha services api-keys create --annotations=foo=bar,abc=def --api-target=service=bar.googleapis.com

To create a key with user-specified key ID and allowed API targets: 
    
    
    gcloud alpha services api-keys create --key-id="my-key-id" --api-target=service=bar.googleapis.com

To create a key with allowed referrers restriction and allowed API targets: 
    
    
    gcloud alpha services api-keys create --allowed-referrers="https://www.example.com/*,<http://sub.exampl\>
    e.com/*" --api-target=service=bar.googleapis.com

To create a key with allowed IOS app bundle IDs and allowed API targets: 
    
    
    gcloud alpha services api-keys create --allowed-bundle-ids=my.app --api-target=service=bar.googleapis.com

To create a key with allowed Android application and allowed API targets: 
    
    
    gcloud alpha services api-keys create --allowed-application=sha1_fingerprint=DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09,package_name=bar.foo --allowed-application=sha1_fingerprint=DA39A3EE5E6B4B0D3255BFEF95601890AFD80709,package_name=foo.bar --api-target=service=bar.googleapis.com

To create a key with allowed API targets (service name only): 
    
    
    gcloud alpha services api-keys create --api-target=service=bar.googleapis.com --api-target=service=foo.googleapis.com

To create a key with service account and allowed API targets: 
    
    
    gcloud alpha services api-keys create --service-account=my-service-account --api-target=service=bar.googleapis.com

To create a key with allowed API targets (service and methods are specified): 
    
    
    gcloud alpha services api-keys create --flags-file=my-flags.yaml

The content of 'my-flags.yaml' is as follows: 
    
    
    - --api-target:
        service: "foo.googleapis.com"
    - --api-target:
        service: "bar.googleapis.com"
        methods:
          - "foomethod"
          - "barmethod"

FLAGS
    

`--annotations`=[`KEY`=`VALUE`,…]
     Annotations are key resource. Specify annotations as a key-value dictionary for small amounts of arbitrary client data. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Display name of the key to create. 
`--key-id`=`KEY_ID`
     User-specified ID of the key to create. 
`--service-account`=`SERVICE_ACCOUNT`
     The email of the service account the key is bound to. If this field is specified, the key is a service account bound key and auth enabled. 
`--api-target`=`service`=`SERVICE`[,`methods`=`METHOD`:…],[…]
     Repeatable. Specify service and optionally one or multiple specific methods. Both fields are case insensitive. Methods can be specified as a colon-separated list (e.g., `--api-target="service=foo.service.com,methods=method1:method2"`), or using `--flags-file` (see $ [gcloud topic flags-file](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) for details). 
At most one of these can be specified: 

`--allowed-application`=[`sha1_fingerprint`=`SHA1_FINGERPRINT`,`package_name`=`PACKAGE_NAME`,…]
     Repeatable. Specify multiple allowed applications. The accepted keys are `sha1_fingerprint` and `package_name`. `sha1_fingerprint` accepts both a 20-byte colon-delimited hex string (e.g. `DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09`) and a 40-character non-delimited hex string (e.g. `DA39A3EE5E6B4B0D3255BFEF95601890AFD80709`). 
`--allowed-bundle-ids`=[`ALLOWED_BUNDLE_IDS`,…]
     iOS app's bundle ids that are allowed to use the key. 
`--allowed-ips`=[`ALLOWED_IPS`,…]
     A list of the caller IP addresses that are allowed to make API calls with this key. 
`--allowed-referrers`=[`ALLOWED_REFERRERS`,…]
     A list of regular expressions for the referrer URLs that are allowed to make API calls with this key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud services api-keys create](https://docs.cloud.google.com/sdk/gcloud/reference/services/api-keys/create)
    
    
    [gcloud beta services api-keys create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/api-keys/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
