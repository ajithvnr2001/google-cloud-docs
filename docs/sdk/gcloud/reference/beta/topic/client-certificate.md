---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/client-certificate/
title: gcloud beta topic client-certificate \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:30:03.776440+00:00
---

# gcloud beta topic client-certificate  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/client-certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta topic client-certificate Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta topic client-certificate - client certificate authorization supplementary help 
DESCRIPTION
     `(BETA)` Client certificate authorization supplementary help. 

Device Certificate Authorization (DCA) enables Context-aware access to identify devices by their X.509 certificates. DCA for Google Cloud APIs is the second in a series of releases that provides administrators the capability to protect access to their Google Cloud resources with device certificates. This feature builds on top of the existing Context-aware access suite (Endpoint Verification, Access Context Manager, and VPC Service Controls) and ensures that only users on trusted devices with a Google-generated certificate are able to access Google Cloud APIs. This provides a stronger signal of device identity (device certificate verification), and protects users from credential theft to accidental loss by only granting access when credentials and the original device certificate are presented. 

To use this feature, organizations can follow the instructions below to install an endpoint verification agent to devices: 

  * Automatically deploy endpoint verification (https://support.google.com/a/answer/9007320#) 
    * Via Chrome Policy for the extension 
    * 3rd party image/software distribution tools for the Native Helper on macOS and Windows 
  * Let users install endpoint verification themselves from the Chrome Webstore (https://support.google.com/a/users/answer/9018161#install) 
    * Users would also be prompted to install the Native Helper as well 

For a greater level of security, operating system key stores can be used to store client certificate objects. This feature is enabled by using [enterprise-certificate-proxy](https://github.com/googleapis/enterprise-certificate-proxy). 

enterprise-certificate-proxy can be installed by running `$ [gcloud components install](https://docs.cloud.google.com/sdk/gcloud/reference/components/install) enterprise-certificate-proxy`. 

In order to use enterprise-certificate-proxy it must first be configured. By default the configuration should be written to `~/.config/gcloud/certificate_config.json`. 

The enterprise-certificate-proxy schema is documented on the [GitHub project page](https://github.com/googleapis/enterprise-certificate-proxy#certificate-configuration). Each operating system that gcloud supports uses a different key store. The certificate_config may contain multiple OS configurations. 

Provisioning the key stores is not in scope for this document. 

Run ``$ [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) context_aware/use_client_certificate True`` so that the gcloud CLI will load the certificate and send it to services. 

See <https://cloud.google.com/sdk/gcloud/reference/topic/client-certificate> for the support list for the latest version of the gcloud CLI. Please upgrade the gcloud command-line tool if necessary. 

Note: iap_tunnel is a special service gcloud CLI uses to create the IAP tunnel. For example, ``gcloud compute start-iap-tunnel`` can start a tunnel to Cloud Identity-Aware Proxy through which another process can create a connection (e.g. SSH, RDP) to a Google Compute Engine instance. Client certificate authorization is supported in tunnel creation. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud topic client-certificate](https://docs.cloud.google.com/sdk/gcloud/reference/topic/client-certificate)
    
    
    [gcloud alpha topic client-certificate](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/client-certificate)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
