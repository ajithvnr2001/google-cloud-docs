---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ts-buildinfo/
title: Print build info \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:47.551486+00:00
---

# Print build info  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/ts-buildinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Print build info Stay organized with collections  Save and categorize content based on your preferences. 

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This document is applicable for Apigee hybrid users only. 

The `buildinfo` API returns information about the current build for a runtime component. This information may be useful if you need to contact support:  


  1. Execute the following command to forward to port 8843. This allows you to call the API in the pod: 
         
         kubectl port-forward -n namespace apigee-runtime-pod-name 8843:8843

  2. Call the buildinfo API: 
         
         curl -v https://0:8843/v1/buildinfo -k
         
             SCM_BRANCH=origin/Hybrid_190912
             RELEASE_ID=190912_01
             SCM_REVISION=aea312cc3026e13fe4b27424a276b1a83c38a8aa
             RPM_NAME=apigee-rpm-1.0.0.20272.aea312cc3.1909130337-190912_01
             BUILD_NUMBER=20272
             BUILD_TIMESTAMP=1568346068541




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
