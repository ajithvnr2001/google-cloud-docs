---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/ekm-connections/create/
title: gcloud alpha kms ekm-connections create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:37:38.791674+00:00
---

# gcloud alpha kms ekm-connections create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/ekm-connections/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha kms ekm-connections create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha kms ekm-connections create - create a new ekm connection 
SYNOPSIS
    

`gcloud alpha kms ekm-connections create` (`EKM_CONNECTION` : `--location`=`LOCATION`) `--hostname`=`HOSTNAME` `--server-certificates-files`=[`SERVER_CERTIFICATES`,…] `--service-directory-service`=`SERVICE_DIRECTORY_SERVICE` [`--endpoint-filter`=`ENDPOINT_FILTER`] [`--crypto-space-path`=`CRYPTO_SPACE_PATH` `--key-management-mode`=`KEY_MANAGEMENT_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a new connection within the given location. 
EXAMPLES
     The following command creates an ekm connection named `laplace` within the location `us-central1`: 
    
    
    gcloud alpha kms ekm-connections create laplace --location=us-central1 --service-directory-service="foo" --endpoint-filter="foo > bar" --hostname="hostname.foo" --server-certificates-files=foo.pem,bar.pem

The following command creates an ekm connection named `laplace` within the location `us-central1` in `cloud-kms` key management mode with the required crypto-space-path : 
    
    
    gcloud alpha kms ekm-connections create laplace --location=us-central1 --service-directory-service="foo" --endpoint-filter="foo > bar" --hostname="hostname.foo" --key-management-mode=cloud-kms --crypto-space-path="foo" --server-certificates-files=foo.pem,bar.pem

POSITIONAL ARGUMENTS
    

Ekmconnection resource - The KMS ekm connection resource. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `ekm_connection` on the command line with a fully specified name; 
  * set the property `core/project`. 



This must be specified. 

`EKM_CONNECTION`
     ID of the ekmconnection or fully qualified identifier for the ekmconnection. 

To set the `ekmconnection` attribute: 

  * provide the argument `ekm_connection` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Google Cloud location for the ekmconnection. 

To set the `location` attribute: 

  * provide the argument `ekm_connection` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--hostname`=`HOSTNAME`
     The hostname of the EKM replica used at TLS and HTTP layers. 
`--server-certificates-files`=[`SERVER_CERTIFICATES`,…]
     A list of filenames of leaf server certificates used to authenticate HTTPS connections to the EKM replica in PEM format. If files are not in PEM, the assumed format will be DER. 
`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`
     The resource name of the Service Directory service pointing to an EKM replica. 
OPTIONAL FLAGS
    

`--endpoint-filter`=`ENDPOINT_FILTER`
     The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. 
Specifies the key management mode for the EkmConnection and associated fields. 
`--crypto-space-path`=`CRYPTO_SPACE_PATH`
     Crypto space path for the EkmConnection. Required during EkmConnection creation if `--key-management-mode=cloud-kms`. 
`--key-management-mode`=`KEY_MANAGEMENT_MODE`
     Key management mode of the ekm connection. An EkmConnection in `cloud-kms` mode means Cloud KMS will attempt to create and manage the key material that resides on the EKM for crypto keys created with this EkmConnection. An EkmConnection in `manual` mode means the external key material will not be managed by Cloud KMS. Omitting the flag defaults to `manual`. `KEY_MANAGEMENT_MODE` must be one of: `manual`, `cloud-kms`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud kms ekm-connections create](https://docs.cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/create)
    
    
    [gcloud beta kms ekm-connections create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/ekm-connections/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
