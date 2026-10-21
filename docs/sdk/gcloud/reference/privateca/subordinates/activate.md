---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/subordinates/activate/
title: gcloud privateca subordinates activate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:40:18.492088+00:00
---

# gcloud privateca subordinates activate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/subordinates/activate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca subordinates activate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca subordinates activate - activate a subordinate certificate authority awaiting user activation 
SYNOPSIS
    

`gcloud privateca subordinates activate` (`CERTIFICATE_AUTHORITY` : `--location`=`LOCATION` `--pool`=`POOL`) (`--pem-chain`=`PEM_CHAIN` | `--issuer-ca`=`ISSUER_CA` [`--issuer-pool`=`ISSUER_POOL` : `--issuer-location`=`ISSUER_LOCATION`]) [`--auto-enable`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command activates a subordinate Certificate Authority (CA) that has been created but is awaiting activation. To activate a CA either provide the path to an already-created PEM CA certificate and issuer chain, or specify the issuer's CA Pool to create the CA certificate now. 
EXAMPLES
     To activate a subordinate CA named 'server-tls-1' in the location 'us-west1' and CA Pool 'server-tls-pool' using a PEM certificate chain in 'chain.crt': 
    
    
    gcloud privateca subordinates activate server-tls-1 --location=us-west1 --pool=server-tls-pool --pem-chain=./chain.crt

To activate a subordinate CA named 'server-tls-1' in the location 'us-west1' and CA Pool 'server-tls-pool' using an issuer CA Pool 'issuer-pool' in the same location: 
    
    
    gcloud privateca subordinates activate server-tls-1 --location=us-west1 --pool=server-tls-pool --issuer-pool=issuer-pool

To activate a subordinate CA named 'server-tls-1' in the location 'us-west1' and CA Pool 'server-tls-pool' using a specific issuer CA 'issuer-ca-1' in the issuer CA Pool 'issuer-pool' in location 'us-east1': 
    
    
    gcloud privateca subordinates activate server-tls-1 --location=us-west1 --pool=server-tls-pool --issuer-pool=issuer-pool --issuer-location=us-east1 --issuer-ca=issuer-ca-1

POSITIONAL ARGUMENTS
    

CERTIFICATE AUTHORITY resource - The certificate authority to activate. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE_AUTHORITY`
     ID of the CERTIFICATE_AUTHORITY or fully qualified identifier for the CERTIFICATE_AUTHORITY. 

To set the `certificate_authority` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the CERTIFICATE_AUTHORITY. 

To set the `location` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `privateca/location`. 


`--pool`=`POOL`
     The parent CA Pool of the CERTIFICATE_AUTHORITY. 

To set the `pool` attribute: 

  * provide the argument `CERTIFICATE_AUTHORITY` on the command line with a fully specified name; 
  * provide the argument `--pool` on the command line. 


REQUIRED FLAGS
    

The activation method for the subordinate CA. 

Exactly one of these must be specified: 

`--pem-chain`=`PEM_CHAIN`
     A file containing a list of PEM-encoded certificates, starting with the current CA certificate and ending with the root CA certificate. 
Or at least one of these can be specified: 

The issuing resource used for this CA certificate. 
`--issuer-ca`=`ISSUER_CA`
     The Certificate Authority ID of the CA to issue the subordinate CA certificate from. This ID is optional. If omitted, any available ENABLED CA in the issuing CA pool will be chosen. 
Issuer resource - The issuing CA Pool to use, if it is on Certificate Authority Service. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--issuer-pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--issuer-pool`=`ISSUER_POOL`
     ID of the Issuer or fully qualified identifier for the Issuer. 

To set the `pool` attribute: 

  * provide the argument `--issuer-pool` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--issuer-location`=`ISSUER_LOCATION`
     The location of the Issuer. 

To set the `location` attribute: 

  * provide the argument `--issuer-pool` on the command line with a fully specified name; 
  * provide the argument `--issuer-location` on the command line; 
  * set the property `privateca/location`. 


OPTIONAL FLAGS
    

`--auto-enable`
     If this flag is set, the Certificate Authority will be automatically enabled upon creation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
