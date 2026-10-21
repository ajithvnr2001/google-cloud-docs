---
url: https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update/
title: gcloud iam workload-identity-pools update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:07:09.068115+00:00
---

# gcloud iam workload-identity-pools update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud iam workload-identity-pools update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud iam workload-identity-pools update - update a workload identity pool 
SYNOPSIS
    

`gcloud iam workload-identity-pools update` (`WORKLOAD_IDENTITY_POOL` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--disabled`] [`--display-name`=`DISPLAY_NAME`] [`--inline-trust-config-file`=`INLINE_TRUST_CONFIG_FILE`] [`--inline-certificate-issuance-config-file`=`INLINE_CERTIFICATE_ISSUANCE_CONFIG_FILE` | `--certificate-lifetime`=`CERTIFICATE_LIFETIME` `--key-algorithm`=`KEY_ALGORITHM` `--rotation-window-percentage`=`ROTATION_WINDOW_PERCENTAGE` `--[no-]use-default-shared-ca`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a workload identity pool. 
EXAMPLES
     The following command updates the workload identity pool with the ID ``my-workload-identity-pool``: 
    
    
    gcloud iam workload-identity-pools update my-workload-identity-pool --location="global" --display-name="My workload pool" --description="My workload pool description" --disabled

POSITIONAL ARGUMENTS
    

Workload identity pool resource - The workload identity pool to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `workload_identity_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`WORKLOAD_IDENTITY_POOL`
     ID of the workload identity pool or fully qualified identifier for the workload identity pool. 

To set the `workload_identity_pool` attribute: 

  * provide the argument `workload_identity_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `workload_identity_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--description`=`DESCRIPTION`
     A description of the pool. Cannot exceed 256 characters. 
`--disabled`
     Whether the pool is disabled. You cannot use a disabled pool to exchange tokens, or use existing tokens to access resources. If the pool is re-enabled, existing tokens grant access again. 
`--display-name`=`DISPLAY_NAME`
     A display name for the pool. Cannot exceed 32 characters. 
`--inline-trust-config-file`=`INLINE_TRUST_CONFIG_FILE`
     YAML file with configuration for providing additional trust bundles. Example file format:
    
    
    inlineTrustConfig:
      additionalTrustBundles:
        example.com:
          trustAnchors:
          - pemCertificate: "-----BEGIN CERTIFICATE-----
            <certificate>
            -----END CERTIFICATE-----"
          - pemCertificate: "-----BEGIN CERTIFICATE-----
            <certificate>
            -----END CERTIFICATE-----"
        myorg.com:
          trustAnchors:
          - pemCertificate: "-----BEGIN CERTIFICATE-----
            <certificate>
            -----END CERTIFICATE-----"
          - pemCertificate: "-----BEGIN CERTIFICATE-----
            <certificate>
            -----END CERTIFICATE-----"

At most one of these can be specified: 

`--inline-certificate-issuance-config-file`=`INLINE_CERTIFICATE_ISSUANCE_CONFIG_FILE`
     YAML file with configuration for certificate issuance. Example file format:
    
    
    inlineCertificateIssuanceConfig:
      caPools:
        us-east1: projects/1234/locations/us-east1/caPools/capoolname
        us-west1: projects/1234/locations/us-west1/caPools/capoolname
      keyAlgorithm: ECDSA_P256
      lifetime: 86400s
      rotationWindowPercentage: 50

Or at least one of these can be specified: 

`--certificate-lifetime`=`CERTIFICATE_LIFETIME`
     Lifetime of the workload certificates issued by the CA pool. 
`--key-algorithm`=`KEY_ALGORITHM`
     Key algorithm to use when generating the key pair. This key pair will be used to create the certificate. `KEY_ALGORITHM` must be one of: `ecdsa-p256`, `ecdsa-p384`, `key-algorithm-unspecified`, `rsa-2048`, `rsa-3072`, `rsa-4096`. 
`--rotation-window-percentage`=`ROTATION_WINDOW_PERCENTAGE`
     Rotation window percentage indicating when certificate rotation should be initiated based on remaining lifetime. 
`--[no-]use-default-shared-ca`
     Use the default shared certificate authorities (CAs) to issue certificates. If enabled, Google Cloud automatically provisions certificates from a default shared CA in the same region as the workload. Enabling this flag clears any existing CA pools configuration. Use `--use-default-shared-ca` to enable and `--no-use-default-shared-ca` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha iam workload-identity-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workload-identity-pools/update)
    
    
    [gcloud beta iam workload-identity-pools update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workload-identity-pools/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
