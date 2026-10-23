---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancers/
title: Load balancer overview \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:43.310765+00:00
---

# Load balancer overview  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/load-balancers/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Load balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS supports multiple AWS load balancers and Cloud Service Mesh.

The following table lists the different load balancer options and how to get started with them.

Type | OSI Layer and Connections supported | Instructions | AWS [ Classic Elastic Load Balancers (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html) | Layer 4: (TCP and UDP) | [Network load balancer](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-load-balancing)  
---|---|---  
AWS [ Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) | Layer 4 (TCP and UDP) | [Network load balancer](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/network-load-balancing)  
AWS [ Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) | Layer 7 (HTTP) | [HTTP load balancer](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/http-load-balancing)  
[Cloud Service Mesh gateway](https://docs.cloud.google.com/service-mesh/docs/overview) | Layer 4 (TCP), Layer 5 (TLS), and layer 7 (HTTP) | [Install Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/unified-install/install), [Install and upgrade gateways](https://docs.cloud.google.com/service-mesh/docs/gateways#in-cluster), [ Ingress Gateway](https://istio.io/latest/docs/tasks/traffic-management/ingress/ingress-control/)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
