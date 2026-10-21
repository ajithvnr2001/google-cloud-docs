---
url: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update/
title: gcloud edge-cache keysets update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:15.808292+00:00
---

# gcloud edge-cache keysets update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/keysets/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud edge-cache keysets update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud edge-cache keysets update - update an EdgeCacheKeyset resource 
SYNOPSIS
    

`gcloud edge-cache keysets update` (`KEYSET` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--public-key`=[`id`=`ID`],[`managed`=`MANAGED`],[`value`=`VALUE`]] [`--validation-shared-key`=[`secret_version`=`SECRET_VERSION`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an existing EdgeCacheKeyset resource. 
EXAMPLES
     To update an EdgeCacheKeyset resource called 'my-keyset', run: 
    
    
    gcloud edge-cache keysets update my-keyset --public-key='id=KEYID,value=BASE64PUBLICKEY'

The `update` command appends keys to an existing EdgeCacheKeyset resource. To add more than one key to an EdgeCacheKeyset resource, provide multiple `--public-key` values: 
    
    
    gcloud edge-cache keysets update my-keyset --public-key='id=KEYID,value=BASE64PUBLICKEY' --public-key='id=EXISTING,value=EXISTINGPUBLICKEY'

You can specify, and an EdgeCacheKeyset resource can contain, up to three (3) public keys. To delete unused public keys within an existing Keyset, use the `import` command to specify the EdgeCacheKeyset resource in full, omitting any unused publicKey items. 

POSITIONAL ARGUMENTS
    

Keyset resource - The name of the EdgeCacheKeyset resource to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `keyset` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`KEYSET`
     ID of the keyset or fully qualified identifier for the keyset. 

To set the `keyset` attribute: 

  * provide the argument `keyset` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `keyset` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * use global location. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Human-readable description of the resource. 
`--labels`=[`KEY`=`VALUE`,…]
     List of KEY=VALUE labels to attach to this resource. 
`--public-key`=[`id`=`ID`],[`managed`=`MANAGED`],[`value`=`VALUE`]
     Set of public keys to use for validating signed requests, when associated with a route. This flag can be repeated to create a Keyset with multiple public keys. 

If you are providing your own public keys, specify the key in the form `id=ID,value=BASE64ENCODEDPUBLICKEY`. 

If you are using Google-managed public keys as part of a dual-token setup, specify the key in the form `id=ID,managed=true`. 

`id`
     id (name) name of the key within the keyset. 
`value`
     URL-safe base64 encoded public key. Cannot be specified if `managed=true`. 
`managed`
     Boolean indicating this is a Google-managed key. Cannot be specified if `value=true`. 
To create a public key with `id` 'foo', pass `--public-key='id=foo,value=VALUE'` to gcloud edge-cache keysets update. 

To create a Google-managed public key with `id` 'bar', pass `--public-key='id=foo,managed=true'` to gcloud edge-cache keysets update. 

At least one of public-key or validation-shared-key must be specified. 

`--validation-shared-key`=[`secret_version`=`SECRET_VERSION`]
     An ordered list of shared keys to use for validating signed requests. 

To create a validation shared key pointing to a Secret Manager secret version with name `projects/PROJECT/secrets/SECRET/versions/VERSION`, pass `--validation-shared-key='secret_version=projects/PROJECT/secrets/SECRET/versions/VERSION'` to gcloud edge-cache keysets update. 

`secret_version`
     The name of the secret in Secret Manager. Must be in the format `projects/PROJECT/secrets/SECRET/versions/VERSION`. 
At least one of public-key or validation-shared-key must be specified. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha edge-cache keysets update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cache/keysets/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
