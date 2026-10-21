---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/ekm-connections/update/
title: gcloud beta kms ekm-connections update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:33:00.115705+00:00
---

# gcloud beta kms ekm-connections update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/kms/ekm-connections/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta kms ekm-connections update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta kms ekm-connections update - update an ekmconnection 
SYNOPSIS
    

`gcloud beta kms ekm-connections update` (`EKM_CONNECTION` : `--location`=`LOCATION`) [`--endpoint-filter`=`ENDPOINT_FILTER`] [`--hostname`=`HOSTNAME`] [`--server-certificates-files`=[`SERVER_CERTIFICATES`,…]] [`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`] [`--crypto-space-path`=`CRYPTO_SPACE_PATH` `--key-management-mode`=`KEY_MANAGEMENT_MODE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` gcloud beta kms ekm-connections update can be used to update the ekmconnection. Updates can be made to the ekmconnection's service resolver's fields. 
EXAMPLES
     The following command updates an ekm-connection named `laplace` service resolver's hostname within location `us-east1`: 
    
    
    gcloud beta kms ekm-connections update laplace --location=us-east1 --hostname=newhostname.foo

The following command updates an ekm-connection named `laplace` service resolver's service_directory_service, endpoint_filter, hostname, and server_certificates within location `us-east1`: 
    
    
    gcloud beta kms ekm-connections update laplace --location=us-east1 --service-directory-service="foo" --endpoint-filter="foo > bar" --hostname="newhostname.foo" --server-certificates-files=foo.pem,bar.pem

The following command updates an ekm-connection named `laplace` key_management_mode within location `us-east1`: 
    
    
    gcloud beta kms ekm-connections update laplace --location=us-east1 --key-management-mode=manual

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


FLAGS
    

`--endpoint-filter`=`ENDPOINT_FILTER`
     The filter applied to the endpoints of the resolved service. If no filter is specified, all endpoints will be considered. 
`--hostname`=`HOSTNAME`
     The hostname of the EKM replica used at TLS and HTTP layers. 
`--server-certificates-files`=[`SERVER_CERTIFICATES`,…]
     A list of filenames of leaf server certificates used to authenticate HTTPS connections to the EKM replica in PEM format. If files are not in PEM, the assumed format will be DER. 
`--service-directory-service`=`SERVICE_DIRECTORY_SERVICE`
     The resource name of the Service Directory service pointing to an EKM replica. 
Specifies the key management mode for the EkmConnection and associated fields. 
`--crypto-space-path`=`CRYPTO_SPACE_PATH`
     Crypto space path for the EkmConnection. Required during EkmConnection creation if `--key-management-mode=cloud-kms`. 
`--key-management-mode`=`KEY_MANAGEMENT_MODE`
     Key management mode of the ekm connection. An EkmConnection in `cloud-kms` mode means Cloud KMS will attempt to create and manage the key material that resides on the EKM for crypto keys created with this EkmConnection. An EkmConnection in `manual` mode means the external key material will not be managed by Cloud KMS. Omitting the flag defaults to `manual`. `KEY_MANAGEMENT_MODE` must be one of: `manual`, `cloud-kms`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud kms ekm-connections update](https://docs.cloud.google.com/sdk/gcloud/reference/kms/ekm-connections/update)
    
    
    [gcloud alpha kms ekm-connections update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/kms/ekm-connections/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
