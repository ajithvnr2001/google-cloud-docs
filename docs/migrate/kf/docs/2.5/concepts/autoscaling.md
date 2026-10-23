---
url: https://docs.cloud.google.com/migrate/kf/docs/2.5/concepts/autoscaling/
title: Autoscaling \u00a0|\u00a0 Kf 2.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:38.271883+00:00
---

# Autoscaling  |  Kf 2.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.5/concepts/autoscaling/

Version 2.5

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.5 ](https://docs.cloud.google.com/migrate/kf/docs/2.5)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.5/documentation)



Send feedback 

#  Autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

Kf leverages the Kubernetes Horizontal Pod Autoscaler (HPA) to automatically scale the number of Pods in a App. When autoscaling is enabled for an App, an HPA object is created and bound to the App object. It then dynamically calculates the target scale and sets it for the App.

## How Kf scaling works

The number of Pods that are deployed for a Kf App is controlled by its underlying Deployment object's `replica` field. The target number of Deployment replicas is set through the App's `replicas` field.

Scaling can be done manually with the [`kf scale`](https://docs.cloud.google.com/migrate/kf/docs/2.5/cli/kf-scale) command. This command is disabled when autoscaling is enabled to avoid conflicting targets.

## How the Kubernetes Horizontal Pod Autoscaler works

The Horizontal Pod Autoscaler (HPA) is implemented as a Kubernetes API resource (the HPA object) and a control loop (the HPA controller) which periodically calculates the number of desired replicas based on current resource utilization. The HPA controller then passes the number to the target object that implements the Scale subresource. The actual scaling is delegated to the underlying object and its controller. You can find more information in the [Kubernetes documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).

### How the Autoscaler determines when to scale

Periodically, the HPA controller queries the resource utilization against the metrics specified in each HorizontalPodAutoscaler definition. The controller obtains the metrics from the resource metrics API for each Pod. Then the controller calculates the utilization value as a percentage of the equivalent resource request. The desired number of replicas is then calculated based on the ratio of current percentage and desired percentage. You can read more about the [autoscaling algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details) in the Kubernetes documentation.

### Metrics

Kf uses HPA v1 which only supports CPU as the target metric.

## How the Kubernetes Horizontal Autoscaler works with Kf

When autoscaling is enabled for a Kf App, the Kf controller will create an HPA object based on the scaling limits and rules specified on the App. Then the HPA controller fetches the specs from the HPA object and scales the App accordingly.

The HPA object will be deleted if Autoscaling is disabled or if the corresponding App is deleted.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
