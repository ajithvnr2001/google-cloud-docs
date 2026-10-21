---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service-controller-enable-and-disable/
title: Enabling and disabling the Canonical Service controller \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:47.126994+00:00
---

# Enabling and disabling the Canonical Service controller  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service-controller-enable-and-disable/

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enabling and disabling the Canonical Service controller

**Note:** Canonical Services are supported automatically in Cloud Service Mesh version 1.6.8 and higher.

The Canonical Service controller groups workloads belonging to the same logical service and is required for the full functionality of the Services dashboard in the Google Cloud console. 

All managed Cloud Service Mesh installations and in-cluster installations with asmcli from version 1.25 provisioned with the managed Canonical Service controller. The in-cluster Canonical Service Controller has been deprecated and will no longer receive updates. While existing deployments of in-cluster controller will continue to operate, we strongly recommend migrating to the managed Canonical Service Controller to ensure compatibility with future releases, access to the latest features, and continued support.

To determine if the in-cluster Canonical Service controller is enabled on your cluster:
    
    
    kubectl get services -n asm-system
    

## Disable the in-cluster Canonical Service controller

For existing in-cluster controller deployments, you should migrate to the managed Canonical Service controller. Follow the [migration guide](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service-migrate-from-in-cluster-controller).

## Enable the Managed Canonical Service Controller

If you installed managed Cloud Service Mesh, then the Managed Canonical Service Controller was installed by default. Also, all the in-cluster Cloud Service Mesh installations with asmcli from version 1.25 will be provisioned with the managed Canonical Service controller. 

Ensure you are running the Managed Canonical Service Controller by running the following command:

Replace FLEET_PROJECT_ID with the ID of your Fleet Host project. Generally, the FLEET_PROJECT_ID has the same name as the project.
    
    
      gcloud beta container hub mesh describe --project FLEET_PROJECT_ID
    

  1. If the description states that the Canonical Services are reconciled successfully, then Manged Canonical Service Controller is operating as expected. No further action is required.
         
         projects/<your project number>/locations/<location>/memberships/<membership-name>:
             code: OK
             description: |-
               Revision(s) ready for use: asm-managed.
               All Canonical Services have been reconciled successfully.
             servicemeshFeatureState: {}
             updateTime: '2021-11-16T21:10:36.289467777Z'
         

  2. If the description states that Managed Canonical Service Controller is yielding to the in-cluster controller, follow the [migration guide](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service-migrate-from-in-cluster-controller).
         
         projects/<your project number>/locations/<location>/memberships/<membership-name>:
             code: OK
             description: |-
               Revision(s) ready for use: istiod-asm-173-6.
               The Managed Canonical Service Controller is yielding to the in-cluster controller.  See https://cloud.google.com/service-mesh/v1.28/docs/canonical-service-controller-enable-and-disable#disable-in-cluster-service-controller for instructions on removing the in-cluster controller.
             servicemeshFeatureState: {}
             updateTime: '2021-11-16T21:05:43.286828851Z'
           lifecycleState: ENABLED
         

  3. For any other issues, refer to [Resolve Managed Canonical Service Controller issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-canonical-service#resolve-managed-canonical-controller-issues) for troubleshooting guidance.




## What's next

Learn about:

  * [Canonical Services](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service)
  * [Best practices in Canonical Services](https://docs.cloud.google.com/service-mesh/v1.28/docs/canonical-service-best-practices)
  * [Define a Canonical Service](https://docs.cloud.google.com/service-mesh/v1.28/docs/define-canonical-service)
  * [Resolving Canonical Service issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-canonical-service)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
