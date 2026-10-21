---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/server-tls-policies/update/
title: gcloud beta network-security server-tls-policies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:19:01.243780+00:00
---

# gcloud beta network-security server-tls-policies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/server-tls-policies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security server-tls-policies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security server-tls-policies update - update a ServerTlsPolicy 
SYNOPSIS
    

`gcloud beta network-security server-tls-policies update` (`SERVER_TLS_POLICY` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--client-validation-mode`=`CLIENT_VALIDATION_MODE` `--clear-client-validation-relaxations` | `--client-validation-relaxations`=[`CLIENT_VALIDATION_RELAXATIONS`,…] | `--[no-]allow-open` `--client-validation-ca-grpc-endpoint`=[`TARGET_URI`,…] | `--client-validation-ca-plugin-instance`=[`PLUGIN_INSTANCE`,…] `--server-certificate-grpc-endpoint`=`SERVER_CERTIFICATE_GRPC_ENDPOINT` | `--server-certificate-plugin-instance`=`SERVER_CERTIFICATE_PLUGIN_INSTANCE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the details of a ServerTlsPolicy. 
EXAMPLES
     To update the client validation mode of a ServerTlsPolicy named `my-tls-policy` to `reject-invalid`, run: 
    
    
    gcloud beta network-security server-tls-policies update my-tls-policy --location=global --client-validation-mode=reject-invalid

To update the client validation mode and relaxations of a ServerTlsPolicy named `my-tls-policy`, run: 
    
    
    gcloud beta network-security server-tls-policies update my-tls-policy --location=global --client-validation-mode=allow-validation-relaxations --client-validation-relaxations=allow-missing-eku,allow-expired-leaf-certificate

To clear all client validation relaxations on a ServerTlsPolicy named `my-tls-policy`, run: 
    
    
    gcloud beta network-security server-tls-policies update my-tls-policy --location=global --clear-client-validation-relaxations

POSITIONAL ARGUMENTS
    

Server TLS policy resource - Name of the ServerTlsPolicy to be updated. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Free-text description of the resource. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta network-security server-tls-policies update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta network-security server-tls-policies update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
Configuration for a ServerTlsPolicy configured for frontend mTLS on Application Load Balancers or a ServerTlsPolicy configured for Traffic Director. At most one of these can be specified: 

Options for a ServerTlsPolicy configured for frontend mTLS on Application Load Balancers. 
`--client-validation-mode`=`CLIENT_VALIDATION_MODE`
     Determines how the server handles connections when the client presents an invalid certificate or no certificate at all. `CLIENT_VALIDATION_MODE` must be one of: 

`allow-invalid-or-missing-client-cert`
     Allow connection to the backend even if client certificate is missing or failed validation. 
`allow-validation-relaxations`
     Require a client certificate that chains to the TrustConfig, while allowing configured validation relaxations. 
`reject-invalid`
     Require a valid client certificate that chains to the TrustConfig and passes all validation checks. 
Modify or clear X.509 client certificate validation relaxations. At most one of these can be specified: 

`--clear-client-validation-relaxations`
     Clear all configured client validation relaxations. 
`--client-validation-relaxations`=[`CLIENT_VALIDATION_RELAXATIONS`,…]
     List of X.509 certificate validation relaxations to apply when `--client-validation-mode=allow-validation-relaxations`. 
Options for a ServerTlsPolicy configured for Traffic Director. 
`--[no-]allow-open`
     Determines if server allows plaintext connections. If set to true, server allows plain text connections. Default is false. Use `--allow-open` to enable and `--no-allow-open` to disable. 
Client validation CA configuration for a ServerTlsPolicy configured for Traffic Director. At most one of these can be specified: 

`--client-validation-ca-grpc-endpoint`=[`TARGET_URI`,…]
     List of gRPC endpoint target URIs used to obtain the Certificate Authority certificates to validate peer certificates for a ServerTlsPolicy configured for Traffic Director. 
`--client-validation-ca-plugin-instance`=[`PLUGIN_INSTANCE`,…]
     List of certificate provider plugin instance names used to obtain the Certificate Authority certificates to validate peer certificates for a ServerTlsPolicy configured for Traffic Director. 
Server certificate configuration for a ServerTlsPolicy configured for Traffic Director. At most one of these can be specified: 

`--server-certificate-grpc-endpoint`=`SERVER_CERTIFICATE_GRPC_ENDPOINT`
     Target URI of the gRPC endpoint that provides the server certificate and private key (must start with `unix:`). 
`--server-certificate-plugin-instance`=`SERVER_CERTIFICATE_PLUGIN_INSTANCE`
     Plugin instance name, used to locate and load CertificateProvider instance configuration to obtain the server certificate and private key. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha network-security server-tls-policies update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/server-tls-policies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
