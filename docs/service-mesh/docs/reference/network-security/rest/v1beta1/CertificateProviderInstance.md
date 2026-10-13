---
url: https://docs.cloud.google.com/service-mesh/docs/reference/network-security/rest/v1beta1/CertificateProviderInstance/
title: CertificateProviderInstance \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:03.899566+00:00
---

# CertificateProviderInstance  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/reference/network-security/rest/v1beta1/CertificateProviderInstance/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/docs/apis)



Send feedback 

#  CertificateProviderInstance Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Specification of a TLS certificate provider instance. Workloads may have one or more CertificateProvider instances (plugins) and one of them is enabled and configured by specifying this message. Workloads use the values from this message to locate and load the CertificateProvider instance configuration.

JSON representation  
---  
      
    
    {
      "pluginInstance": string
    }  
  
Fields  
---  
`pluginInstance` |  `string` Required. Plugin instance name, used to locate and load CertificateProvider instance configuration. Set to "google_cloud_private_spiffe" to use Certificate Authority Service certificate provider instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-18 UTC."],[],[]] 
