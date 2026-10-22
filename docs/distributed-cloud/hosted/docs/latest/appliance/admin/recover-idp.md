---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/recover-idp/
title: Recover device if identity provider is unavailable \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:22.269570+00:00
---

# Recover device if identity provider is unavailable  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/recover-idp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Recover device if identity provider is unavailable Stay organized with collections  Save and categorize content based on your preferences. 

If you cannot log into the appliance because the identity provider (IdP) is unavailable, complete the following steps:

  1. Use the kubeconfig file to edit the config:
         
         kubectl edit clientconfig default -n kube-public
         

  2. In the kubeconfig file, remove the IdP configurations for the IdP that is unavailable.

  3. Configure your identity provider again by doing one of the following:

     * If you use your own IdP, run the following command and follow the steps.
           
           gdcloud appliance configure
           

     * If you use the built-in IdP, run the following command to automatically configure the IdP:
           
           gdcloud appliance install --phase identity-provider
           




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
