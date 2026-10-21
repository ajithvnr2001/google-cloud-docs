---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke/
title: gcloud privateca certificates revoke \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:15.313759+00:00
---

# gcloud privateca certificates revoke  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/certificates/revoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca certificates revoke Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca certificates revoke - revoke a certificate 
SYNOPSIS
    

`gcloud privateca certificates revoke` (`--certificate`=`CERTIFICATE` | `--serial-number`=`SERIAL_NUMBER`) [`--reason`=`REASON`; default="unspecified"] [`--issuer-pool`=`ISSUER_POOL` : `--issuer-location`=`ISSUER_LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Revokes the given certificate for the given reason. 
EXAMPLES
     To revoke the 'frontend-server-tls' certificate due to key compromise: 
    
    
    gcloud privateca certificates revoke --certificate=frontend-server-tls --issuer-pool=my-pool --issuer-location=us-west1 --reason=key_compromise

To revoke the a certificate with the serial number '7dc1d9186372de2e1f4824abb1c4c9e5e43cbb40' due to a newer one being issued: 
    
    
    gcloud privateca certificates revoke --serial-number=7dc1d9186372de2e1f4824abb1c4c9e5e43cbb40 --issuer-pool=my-pool --issuer-location=us-west1 --reason=superseded

REQUIRED FLAGS
    

The certificate identifier. 

Exactly one of these must be specified: 

Certificate resource - The certificate to revoke. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--certificate` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `issuer-location` attribute: 

  * provide the argument `--certificate` on the command line with a fully specified name; 
  * set the property `privateca/location`. 



To set the `issuer-pool` attribute: 

  * provide the argument `--certificate` on the command line with a fully specified name. 



`--certificate`=`CERTIFICATE`
     ID of the certificate or fully qualified identifier for the certificate. 

To set the `certificate` attribute: 

* provide the argument `--certificate` on the command line. 
`--serial-number`=`SERIAL_NUMBER`
     The serial number of the certificate. 
OPTIONAL FLAGS
    

`--reason`=`REASON`; default="unspecified"
     Revocation reason to include in the CRL. `REASON` must be one of: `affiliation-changed`, `attribute-authority-compromise`, `certificate-authority-compromise`, `certificate-hold`, `cessation-of-operation`, `key-compromise`, `privilege-withdrawn`, `unspecified`, `superseded`. 
Issuing CA pool resource - The issuing CA pool of the certificate to revoke. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--issuer-pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--issuer-pool`=`ISSUER_POOL`
     ID of the Issuing CA pool or fully qualified identifier for the Issuing CA pool. 

To set the `pool` attribute: 

  * provide the argument `--issuer-pool` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--issuer-location`=`ISSUER_LOCATION`
     The location of the Issuing CA pool. 

To set the `issuer-location` attribute: 

  * provide the argument `--issuer-pool` on the command line with a fully specified name; 
  * provide the argument `--issuer-location` on the command line; 
  * set the property `privateca/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
