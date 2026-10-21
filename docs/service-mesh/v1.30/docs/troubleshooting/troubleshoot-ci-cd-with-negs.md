---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-ci-cd-with-negs/
title: Troubleshooting NEGs with CI/CD Tools \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:28:01.902780+00:00
---

# Troubleshooting NEGs with CI/CD Tools  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-ci-cd-with-negs/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting NEGs with CI/CD Tools

If your cluster is using the Traffic Director control plane (see [Check control plane implementation](https://cloud.google.com/service-mesh/v1.30/docs/check-control-plane-implementation) to check which control plane your cluster is using) and you are using CI/CD tools for managing your Kubernetes resources, then you need to be aware of possible incompatibilities and workarounds.

## Traffic Director and NEG annotations

When using the Traffic Director control plane your services are annotated with 'cloud.google.com/neg' and 'cloud.google.com/neg-status' annotations. This could cause contention between the CI/CD tool and Cloud Service Mesh. In case your CI/CD tool finds this annotation unexpected and tries to remove it, you must configure your CI/CD tool to ignore the NEG annotations.

The configuration to ignore the NEG annotation will differ for every tool. For example, if you are using ArgoCD you can configure it to ignore NEG annotation.

### ArgoCD

Utilize ArgoCD's Diffing Customization to instruct ArgoCD to ignore the NEG annotation. The configuration should look like the following:
    
    
    spec:
      ignoreDifferences:
        - group: 'v1'
          kind: 'Service'
          jsonPointers:
            - /metadata/annotations/cloud.google.com~1neg-status
            - /metadata/annotations/cloud.google.com~1neg
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
