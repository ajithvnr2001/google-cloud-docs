---
url: https://docs.cloud.google.com/sdk/gcloud/reference/services/api-keys/update/
title: gcloud services api-keys update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:44.750635+00:00
---

# gcloud services api-keys update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/services/api-keys/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud services api-keys update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud services api-keys update - update an API key's metadata 
SYNOPSIS
    

`gcloud services api-keys update` (`KEY` : `--location`=`LOCATION`) [`--append`] [`--async`] [`--[no-]check-existing-usage`] [`--display-name`=`DISPLAY_NAME`] [`--annotations`=[`KEY`=`VALUE`,…] | `--clear-annotations`] [`--api-target`=`service`=`SERVICE`[,`methods`=`METHOD`:…],[…] `--allowed-application`=[`sha1_fingerprint`=`SHA1_FINGERPRINT`,`package_name`=`PACKAGE_NAME`,…] | `--allowed-bundle-ids`=[`ALLOWED_BUNDLE_IDS`,…] | `--allowed-ips`=[`ALLOWED_IPS`,…] | `--allowed-referrers`=[`ALLOWED_REFERRERS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an API key's metadata. 
EXAMPLES
     To update display name and set allowed ips as server key restrictions: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --display-name="test name" --allowed-ips=2620:15c:2c4:203:2776:1f90:6b3b:217,104.133.8.78

To update annotations: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --annotations=foo=bar,abc=def

To update key's allowed referrers restriction: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --allowed-referrers="https://www.example.com/*,<http://sub.exampl\>
    e.com/*"

To update key's allowed ios app bundle ids: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --allowed-bundle-ids=my.app

To update key's allowed android application: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --allowed-application=sha1_fingerprint=DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09,package_name=bar1 --allowed-application=sha1_fingerprint=DA39A3EE5E6B4B0D3255BFEF95601890AFD80709,package_name=bar2

To update keys' allowed api target with multiple services: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --api-target=service=bar.googleapis.com --api-target=service=foo.googleapis.com

To update keys' allowed api target with service and method: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --flags-file=my-flags.yaml
    
    
    The content of 'my-flags.yaml' is as follows:
    
    
      - --api-target:
          service: "foo.googleapis.com"
      - --api-target:
          service: "bar.googleapis.com"
          methods:
          - "foomethod"
          - "barmethod"

To append allowed referrers and api targets to an existing key: 
    
    
    gcloud services api-keys update projects/myproject/locations/global/keys/my-key-id --append --allowed-referrers="https://www.example.com/*" --api-target=service=foo.googleapis.com

POSITIONAL ARGUMENTS
    

Key resource - The name of the key to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `key` attribute: 

  * provide the argument `key` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the key. 

To set the `location` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * location will default to global. 


FLAGS
    

`--append`
     If specified, merge the new restrictions with the current restrictions of the key instead of replacing them. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--[no-]check-existing-usage`
     If true, existing usage will be checked before the key is updated. If the key has traffic in the last 7 days that is incompatible with the requested change, the request fails with an error. Defaults to true. Set to false (--no-check-existing-usage) to skip the check. Use `--check-existing-usage` to enable and `--no-check-existing-usage` to disable. 
`--display-name`=`DISPLAY_NAME`
     Display name of the key to update. 
At most one of these can be specified: 

`--annotations`=[`KEY`=`VALUE`,…]
     Annotations are key resource. Specify annotations as a key-value dictionary for small amounts of arbitrary client data. 
`--clear-annotations`
     If set, clear all annotations on the key. 
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
     These variants are also available: 
    
    
    [gcloud alpha services api-keys update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/api-keys/update)
    
    
    [gcloud beta services api-keys update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/api-keys/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
