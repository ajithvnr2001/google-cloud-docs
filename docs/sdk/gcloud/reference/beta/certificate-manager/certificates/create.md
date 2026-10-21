---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/certificates/create/
title: gcloud beta certificate-manager certificates create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:25.758935+00:00
---

# gcloud beta certificate-manager certificates create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/certificate-manager/certificates/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta certificate-manager certificates create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta certificate-manager certificates create - create a certificate 
SYNOPSIS
    

`gcloud beta certificate-manager certificates create` (`CERTIFICATE` : `--location`=`LOCATION`) (`--certificate-file`=`PATH_TO_FILE` `--private-key-file`=`PATH_TO_FILE` | [`--domains`=[`DOMAINS`,…] : `--dns-authorizations`=[`DNS_AUTHORIZATIONS`,…] | `--issuance-config`=`ISSUANCE_CONFIG`]) [`--description`=`DESCRIPTION`] [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`--scope`=`SCOPE`; default="DEFAULT"] [`--tags`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new certificate. 

  * Managed certificates can be created by supplying one or more domain names and an (optional) list of DNS authorizations for those domain names. 
  * Self-managed certificates can be created by uploading a certificate and its corresponding private key (both in PEM format). 


EXAMPLES
     To create (upload) a self-managed certificate called `www-example-com`, run: 
    
    
    gcloud beta certificate-manager certificates create www-example-com --private-key-file=key.pem --certificate-file=cert.pem

To create a certificate managed by Certificate Manager called `api-example-com`, run: 
    
    
    gcloud beta certificate-manager certificates create api-example-com --domains="api.example.com"

To create a certificate managed by Certificate Manager called `api-example-com`, using an existing DNS authorization, run: 
    
    
    gcloud beta certificate-manager certificates create api-example-com --dns-authorizations=api-example-com --domains="api.example.com"

POSITIONAL ARGUMENTS
    

Certificate resource - The certificate to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `certificate` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CERTIFICATE`
     ID of the certificate or fully qualified identifier for the certificate. 

To set the `certificate` attribute: 

  * provide the argument `certificate` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the certificate. 

To set the `location` attribute: 

  * provide the argument `certificate` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * default value of location is [global]. 


REQUIRED FLAGS
    

Configuration for creating and uploading certificates to Cloud Certificate Manager. 

Exactly one of these must be specified: 

Configuration for uploading self-managed certificates and keys. 
`--certificate-file`=`PATH_TO_FILE`
     Certificate data in PEM-encoded form. Use a full or relative path to a local file containing the value of certificate_file. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--private-key-file`=`PATH_TO_FILE`
     Private key data in PEM-encoded form. Use a full or relative path to a local file containing the value of private_key_file. 

This flag argument must be specified if any of the other arguments in this group are specified. 

Configuration for creating new managed certificates. 
`--domains`=[`DOMAINS`,…]
     Public domain name(s) to create a certificate for. 

  * If a DNS authorization is provided for the domain, the certificate will be validated against the DNS record you added as part of the authorization flow. 
  * If no DNS authorization is provided, Certificate Manager will attempt to validate the domain against the serving endpoint directly. 



You may list multiple, comma-separated domain names to include multiple names as Subject Alternative Names on the issued certificate. 

This flag argument must be specified if any of the other arguments in this group are specified. 

At most one of these can be specified: 

`--dns-authorizations`=[`DNS_AUTHORIZATIONS`,…]
     Name(s) of the DNS authorizations for each listed domain. 

Note that each domain requires a matching authorization, and any domain that fails authorization will prevent issuance and/or renewal of the certificate. 

To reference multiple DNS authorizations, provide a list of comma separated DNS authorization resource names or URLs. For example: 
    
    
    gcloud beta certificate-manager certificates create --dns-authorizations=api-example-com,www-example-com

`--issuance-config`=`ISSUANCE_CONFIG`
     Name of the Certificate Issuance Config to use for issuance. 
COMMONLY USED FLAGS
    

`--description`=`DESCRIPTION`
     Text description of a certificate. 
OTHER FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--scope`=`SCOPE`; default="DEFAULT"
     Scope of the managed certificate. This determines which services the certificate can be attached to/associated with. Defaults to `DEFAULT`. `SCOPE` must be one of: 

`all-regions`
     Certificates with scope ALL_REGIONS are currently used for Cross-region Internal Application Load Balancer only. 
`client-auth`
     Certificates with scope CLIENT_AUTH are used for client authentication. 
`default`
     Certificates with DEFAULT scope are used for Load Balancing and Cloud CDN. 

If unsure, choose this option. 

`edge-cache`
     Certificates with scope EDGE_CACHE are special-purposed certificates, scoped for use with Media Edge services only. 
`--tags`=[`KEY`=`VALUE`,…]
     List of tags KEY=VALUE pairs to bind. Each item must be expressed as `<tag-key-namespaced-name>=<tag-value-short-name>`. 

Example: `123/environment=production,123/costCenter=marketing`

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the certificatemanager/v1 API. The full documentation for this API can be found at: <https://docs.cloud.google.com/certificate-manager/docs/overview>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud certificate-manager certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/certificate-manager/certificates/create)
    
    
    [gcloud alpha certificate-manager certificates create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager/certificates/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
