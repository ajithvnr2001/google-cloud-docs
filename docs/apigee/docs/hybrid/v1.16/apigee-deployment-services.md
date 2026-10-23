---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-deployment-services/
title: Apigee deployment services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:19.636471+00:00
---

# Apigee deployment services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-deployment-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee deployment services Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/apigee-deployment-services.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/apigee-deployment-services.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/apigee-deployment-services.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/apigee-deployment-services.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/apigee-deployment-services.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/apigee-deployment-services.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/apigee-deployment-services.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/apigee-deployment-services.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/apigee-deployment-services.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/apigee-deployment-services.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/apigee-deployment-services.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/apigee-deployment-services.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/apigee-deployment-services.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/apigee-deployment-services.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/apigee-deployment-services.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/apigee-deployment-services.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/apigee-deployment-services.html)



_ApigeeDeployment_ (AD) is a [ CustomResourceDefinition](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions) (CRD) used to define, update, and release stateless Apigee hybrid components in a Kubernetes cluster. For example, AD is used to deploy message processors to the cluster, and the release of these components are triggered by updating the version in the AD. 

Before AD, certain hybrid resources were maintained manually and individually. However, with AD all these resources are maintained as an atomic deployment unit. 

When you list the Apigee hybrid pods in your Kubernetes cluster, you will see these pods listed. These pods do the work to deploy and maintain the AD and validate deployment configurations. 

Pod name | Description  
---|---  
`apigee-operators` | Creates and updates low level Kubernetes and Istio resources that are required to deploy and maintain the AD. For example, the controller carries out the release of message processors. Also validates the ApigeeDeployment configuration before persisting it in Kubernetes cluster.   
  
To get a list of the ApigeeDeployments in your cluster, execute this command: 
    
    
    kubectl get ad -n APIGEE_NAMESPACE

The output should be similar to the following: 
    
    
    NAME                                              AGE
    apigee-mart-my_org                                4h
    apigee-runtime-my_org-my_env                      4h
    apigee-synchronizer-my_org-my_env                 4h
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
