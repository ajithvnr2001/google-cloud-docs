---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/server-tls-policies/create/
title: gcloud beta network-security server-tls-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:16:37.922226+00:00
---

# gcloud beta network-security server-tls-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/server-tls-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security server-tls-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security server-tls-policies create - create a ServerTlsPolicy 
SYNOPSIS
    

`gcloud beta network-security server-tls-policies create` (`SERVER_TLS_POLICY` : `--location`=`LOCATION`) ([`--client-validation-mode`=`CLIENT_VALIDATION_MODE` : `--client-validation-relaxations`=[`CLIENT_VALIDATION_RELAXATIONS`,…] `--client-validation-trust-config`=`CLIENT_VALIDATION_TRUST_CONFIG`] | `--allow-open` `--client-validation-ca-grpc-endpoint`=[`TARGET_URI`,…] | `--client-validation-ca-plugin-instance`=[`PLUGIN_INSTANCE`,…] `--server-certificate-grpc-endpoint`=`SERVER_CERTIFICATE_GRPC_ENDPOINT` | `--server-certificate-plugin-instance`=`SERVER_CERTIFICATE_PLUGIN_INSTANCE`) [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new ServerTlsPolicy. 
EXAMPLES
     To create a ServerTlsPolicy configured for frontend mTLS on Application Load Balancers, run: 
    
    
    gcloud beta network-security server-tls-policies create my-server-tls-policy --location=global --client-validation-mode=reject-invalid --client-validation-trust-config=projects/my-project/locations/global/trustConfigs/my-trust-config

To create a ServerTlsPolicy configured for frontend mTLS on Application Load Balancers with validation relaxations, run: 
    
    
    gcloud beta network-security server-tls-policies create my-server-tls-policy --location=global --client-validation-mode=allow-validation-relaxations --client-validation-trust-config=projects/my-project/locations/global/trustConfigs/my-trust-config --client-validation-relaxations=allow-missing-eku,allow-expired-leaf-certificate

To create a ServerTlsPolicy configured for Traffic Director, run: 
    
    
    gcloud beta network-security server-tls-policies create my-td-policy --location=global --allow-open --client-validation-ca-plugin-instance=google_cloud_private_spiffe

POSITIONAL ARGUMENTS
    

Server TLS policy resource - Name of the ServerTlsPolicy to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `server_tls_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SERVER_TLS_POLICY`
     ID of the server TLS policy or fully qualified identifier for the server TLS policy. 

To set the `server_tls_policy` attribute: 

  * provide the argument `server_tls_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `server_tls_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Configuration for a ServerTlsPolicy configured for frontend mTLS on Application Load Balancers or for Traffic Director. Exactly one of these must be specified: 

ServerTlsPolicy configured for frontend mTLS on Application Load Balancers. 
`--client-validation-mode`=`CLIENT_VALIDATION_MODE`
     Specifies how the client connection is handled when the client presents an invalid certificate or no certificate to the load balancer. `CLIENT_VALIDATION_MODE` must be one of: 

`allow-invalid-or-missing-client-cert`
     Allow connection even if certificate chain validation of the client certificate failed or no client certificate was presented. 
`allow-validation-relaxations`
     Require a client certificate, but apply the specific validation relaxations requested in `--client-validation-relaxations`. 
`reject-invalid`
     Require a client certificate and allow connection to the backend only if validation of the client certificate passed. 
This flag argument must be specified if any of the other arguments in this group are specified. 
`--client-validation-relaxations`=[`CLIENT_VALIDATION_RELAXATIONS`,…]
     List of validation relaxations to apply when `--client-validation-mode` is set to `allow-validation-relaxations`. `CLIENT_VALIDATION_RELAXATIONS` must be one of: 

`allow-expired-leaf-certificate`
     Allows validation of an expired client leaf certificate. The certificate will be validated as if the current time was one second before the end of its validity period (the `notAfter` timestamp). 
`allow-missing-eku`
     Allows the client certificate to completely omit the Extended Key Usage (EKU) extension. If the EKU extension is present, it must permit the `clientAuth` key purpose (OID 1.3.6.1.5.5.7.3.2). 
`allow-sha1-hashing`
     Allows validation of client certificate chains signed using legacy SHA-1 message digests. 
`--client-validation-trust-config`=`CLIENT_VALIDATION_TRUST_CONFIG`
     Reference to the Certificate Manager TrustConfig resource (`projects/*/locations/*/trustConfigs/*` or TrustConfig ID in the same project and location) used to validate client certificates. 
ServerTlsPolicy configured for Traffic Director. 
`--allow-open`
     Determines if the server allows plaintext connections when configured for Traffic Director. 
Client validation CA configuration for Traffic Director. At most one of these can be specified: 

`--client-validation-ca-grpc-endpoint`=[`TARGET_URI`,…]
     List of gRPC endpoint target URIs used to obtain the Certificate Authority certificates to validate peer certificates for Traffic Director. 
`--client-validation-ca-plugin-instance`=[`PLUGIN_INSTANCE`,…]
     List of certificate provider plugin instance names used to obtain the Certificate Authority certificates to validate peer certificates for Traffic Director. 
Server certificate configuration for Traffic Director. At most one of these can be specified: 

`--server-certificate-grpc-endpoint`=`SERVER_CERTIFICATE_GRPC_ENDPOINT`
     Target URI of the gRPC endpoint that provides the server certificate and private key (must start with `unix:`). 
`--server-certificate-plugin-instance`=`SERVER_CERTIFICATE_PLUGIN_INSTANCE`
     Plugin instance name that will be passed to the data plane to load server identity credentials. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Free-text description of the resource. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha network-security server-tls-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/server-tls-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
