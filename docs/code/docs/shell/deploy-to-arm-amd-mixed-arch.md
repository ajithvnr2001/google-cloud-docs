---
url: https://docs.cloud.google.com/code/docs/shell/deploy-to-arm-amd-mixed-arch/
title: Deploy your applications to aarch64, AMD64, or mixed-architecture GKE clusters \u00a0|\u00a0 Cloud Code for Cloud Shell \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:47.882893+00:00
---

# Deploy your applications to aarch64, AMD64, or mixed-architecture GKE clusters  |  Cloud Code for Cloud Shell  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/shell/deploy-to-arm-amd-mixed-arch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ Cloud Code for Cloud Shell ](https://docs.cloud.google.com/code/docs/shell)
  * [ Guides ](https://docs.cloud.google.com/code/docs/shell/quickstart)



Send feedback 

#  Deploy your applications to aarch64, AMD64, or mixed-architecture GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Code automatically detects your target cluster's architecture and builds an image that matches your workstation's architecture, even if your target cluster's architecture is mixed (both x86 and Arm).

You also have the option to add a parameter in your `skaffold.yaml` file that specifies what platform to build for, which overrides Cloud Code's automatic detection.

## Specify the platform to build images for

If you want to override Cloud Code's automatic detection when building your image, you can specify the platform that you want to build images for in your `skaffold.yaml` file.

The following list shows the possible values for the `--platform` flag in your CLI, or the `platforms` parameter in your `skaffold.yaml` file:

x86 | Arm  
---|---  
`amd64` | `aarch64`  
`linux/amd64` | `linux/aarch64`  
  
### Add the platforms parameter to your skaffold.yaml file

To specify the platform you want to build your image for, add the `platforms` parameter to your `skaffold.yaml` file:
    
    
    build:
      platforms: ["linux/aarch64"]
      artifacts:
        - image: example
    

To learn more about Cloud Code's support for Arm and mixed-architecture GKE clusters, see [Arm support](https://docs.cloud.google.com/code/docs/shell/arm-support). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
