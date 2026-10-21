---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update/
title: gcloud compute target-ssl-proxies update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:37:07.868168+00:00
---

# gcloud compute target-ssl-proxies update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-ssl-proxies/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute target-ssl-proxies update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute target-ssl-proxies update - update a target SSL proxy 
SYNOPSIS
    

`gcloud compute target-ssl-proxies update` `NAME` [`--backend-service`=`BACKEND_SERVICE`] [`--proxy-header`=`PROXY_HEADER`] [`--clear-ssl-policy` | `--ssl-policy`=`SSL_POLICY` `--global-ssl-policy` | `--ssl-policy-region`=`SSL_POLICY_REGION`] [`--ssl-certificates`=`SSL_CERTIFICATE`,[…] | `--clear-ssl-certificates` | `--certificate-map`=`CERTIFICATE_MAP` | `--clear-certificate-map`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute target-ssl-proxies update` is used to replace the SSL certificate, backend service, proxy header or SSL policy of existing target SSL proxies. A target SSL proxy is referenced by one or more forwarding rules which define which packets the proxy is responsible for routing. The target SSL proxy in turn points to a backend service which will handle the requests. The target SSL proxy also points to at most 15 SSL certificates used for server-side authentication or one certificate map. The target SSL proxy can be associated with at most one SSL policy. 
POSITIONAL ARGUMENTS
    

`NAME`
     Name of the target SSL proxy to update. 
FLAGS
    

`--backend-service`=`BACKEND_SERVICE`
     A backend service that will be used for connections to the target SSL proxy. 
`--proxy-header`=`PROXY_HEADER`
     The type of proxy protocol header to be sent to the backend. `PROXY_HEADER` must be one of: 

`NONE`
     No proxy header is added. 
`PROXY_V1`
     Enables PROXY protocol (version 1) for passing client connection information. 
At most one of these can be specified: 

`--clear-ssl-policy`
     Removes any attached SSL policy from the SSL proxy. 
Or at least one of these can be specified: 

`--ssl-policy`=`SSL_POLICY`
     A reference to an SSL policy resource that defines the server-side support for SSL features and affects the connections between clients and load balancers that are using the SSL proxy. The SSL policy must exist and cannot be deleted while referenced by a target SSL proxy. 
At most one of these can be specified: 

`--global-ssl-policy`
     If set, the SSL policy is global. 
`--ssl-policy-region`=`SSL_POLICY_REGION`
     Region of the SSL policy to operate on. Overrides the default `compute/region` property value for this command invocation. 
At most one of these can be specified: 

`--ssl-certificates`=`SSL_CERTIFICATE`,[…]
     References to at most 15 SSL certificate resources that are used for server-side authentication. The first SSL certificate in this list is considered the primary SSL certificate associated with the load balancer. The SSL certificates must exist and cannot be deleted while referenced by a target SSL proxy. 
`--clear-ssl-certificates`
     Remove any attached SSL certificates from the SSL proxy. 
Or at least one of these can be specified: 

Certificate map resource - The certificate map to attach. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--certificate-map` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--certificate-map` on the command line with a fully specified name; 
  * default value of location is [global]. 


`--certificate-map`=`CERTIFICATE_MAP`
     ID of the certificate map or fully qualified identifier for the certificate map. 

To set the `map` attribute: 

  * provide the argument `--certificate-map` on the command line. 


`--clear-certificate-map`
     Removes any attached certificate map from the SSL proxy. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute target-ssl-proxies update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/target-ssl-proxies/update)
    
    
    [gcloud beta compute target-ssl-proxies update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/target-ssl-proxies/update)
    
    
    [gcloud preview compute target-ssl-proxies update](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/target-ssl-proxies/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
