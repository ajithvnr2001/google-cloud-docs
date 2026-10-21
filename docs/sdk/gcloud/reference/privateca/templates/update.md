---
url: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/update/
title: gcloud privateca templates update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:42:27.213093+00:00
---

# gcloud privateca templates update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/privateca/templates/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud privateca templates update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud privateca templates update - update a certificate template 
SYNOPSIS
    

`gcloud privateca templates update` (`CERTIFICATE_TEMPLATE` : `--location`=`LOCATION`) [`--copy-sans`] [`--copy-subject`] [`--description`=`DESCRIPTION`] [`--identity-cel-expression`=`IDENTITY_CEL_EXPRESSION`] [`--predefined-values-file`=`PREDEFINED_VALUES_FILE`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--copy-all-requested-extensions` | `--copy-extensions-by-oid`=[`OBJECT_ID`,…] | `--drop-oid-extensions` `--copy-known-extensions`=[`KNOWN_EXTENSIONS`,…] | `--drop-known-extensions`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a certificate template. 
EXAMPLES
     To update a template named "dns-restricted" with new default x509 extensions: 
    
    
    gcloud privateca templates update dns-restricted --location=us-west1 --predefined-values-file=x509_parameters.yaml

To update a template named "dns-restricted" to allow requestors to specify subject: 
    
    
    gcloud privateca templates update dns-restricted --location=us-west1 --copy-subject

To update a template named "dns-restricted" with allowed extension 'base-key-usage' to allow requestors to specify additional x509 extension 'extended-key-usage': 
    
    
    gcloud privateca templates update dns-restricted --location=us-west1 --copy-known-extensions=base-key-usage,extended-key-usage

To update a template named "mtls-restricted" with allowed OID '1.1' to allow requestors to specify alternative OIDS '2.2,3.3': 
    
    
    gcloud privateca templates update mtls-restricted --location=us-west1 --copy-extensions-by-oid=2.2,3.3

POSITIONAL ARGUMENTS
    

CERTIFICATE TEMPLATE resource - The template to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `CERTIFICATE_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE_TEMPLATE`
     ID of the CERTIFICATE_TEMPLATE or fully qualified identifier for the CERTIFICATE_TEMPLATE. 

To set the `certificate template` attribute: 

  * provide the argument `CERTIFICATE_TEMPLATE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the CERTIFICATE_TEMPLATE. 

To set the `location` attribute: 

  * provide the argument `CERTIFICATE_TEMPLATE` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `privateca/location`. 


FLAGS
    

`--copy-sans`
     If this is specified, the Subject Alternative Name extension from the certificate request will be copied into the signed certificate. Specify \--no-copy-sans to drop any caller-specified SANs in the certificate request. 
`--copy-subject`
     If this is specified, the Subject from the certificate request will be copied into the signed certificate. Specify --no-copy-subject to drop any caller-specified subjects from the certificate request. 
`--description`=`DESCRIPTION`
     A text description for the Certificate Template. 
`--identity-cel-expression`=`IDENTITY_CEL_EXPRESSION`
     A CEL expression that will be evaluated against the identity in the certificate before it is issued, and returns a boolean signifying whether the request should be allowed. 
`--predefined-values-file`=`PREDEFINED_VALUES_FILE`
     A YAML file describing any predefined X.509 values set by this template. The provided extensions will be copied over to any certificate requests that use this template, taking precedent over any allowed extensions in the certificate request. The format of this file should be a YAML representation of the X509Parameters message, which is defined here: <https://cloud.google.com/certificate-authority-service/docs/reference/rest/v1/X509Parameters>. Some examples can be found here: <https://cloud.google.com/certificate-authority-service/docs/creating-certificate-template>
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud privateca templates update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud privateca templates update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
Constraints on requested X.509 extensions. 

At most one of these can be specified: 

`--copy-all-requested-extensions`
     If this is set, all extensions, whether known or specified by OID, that are specified in the certificate request will be copied into the signed certificate. 
Or at least one of these can be specified: 

Specify exact x509 extensions to copy by OID or known extension. 
Constraints on unknown extensions by their OIDs. 

At most one of these can be specified: 

`--copy-extensions-by-oid`=[`OBJECT_ID`,…]
     If this is set, then extensions with the given OIDs will be copied from the certificate request into the signed certificate. 
`--drop-oid-extensions`
     If this is set, then all existing OID extensions will be removed from the template, prohibiting any extensions specified by OIDs to be specified by the requester. 
Constraints on known extensions. 

At most one of these can be specified: 

`--copy-known-extensions`=[`KNOWN_EXTENSIONS`,…]
     If this is set, then the given extensions will be copied from the certificate request into the signed certificate. `KNOWN_EXTENSIONS` must be one of: `base-key-usage`, `extended-key-usage`, `ca-options`, `policy-ids`, `aia-ocsp-servers`. 
`--drop-known-extensions`
     If this is set, then all known extensions will be removed from the template, prohibiting any known x509 extensions to be specified by the requester. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
