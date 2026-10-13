---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-installation/
title: Resolving installation issues \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:20.575544+00:00
---

# Resolving installation issues  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-installation/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving installation issues

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.29/docs/getting-support).

## Failed installation due to missing `meshtelemetry.googleapis.com` API

If your installation fails due to the enablement of `meshtelemetry.googleapis.com`, ensure you have removed the enablement of `meshtelemetry.googleapis.com` from your installation process. This API is no longer required and has been deprecated. For more information, see the full list of [required APIs](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/provision-control-plane#before_you_begin).

## Failed installation because `mdp-controller` is not ready

If your installation fails with error code `REVISION_FAILED_PRECONDITION` or an error message saying the `mdp-controller` is not ready, ensure that your cluster has nodes which can be used to provision MDP controller. MDP controller is required to onboard to Cloud Service Mesh. A common issue that can prevent a node from being used for MDP controller deployment is if you have node taints configured. 

You can run the following command to verify the node taints you have configured:
    
    
    kubectl describe node NODE_NAME
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
