---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quotas/
title: Quotas \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:50.785285+00:00
---

# Quotas  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quotas/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quotas)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

GKE on AWS imposes several default quotas. To increase them, contact Google Cloud support.

Starting from Kubernetes 1.26, the scalability of GKE on AWS has been enhanced, and allows up to 1000 nodes per cluster.

Quota Name | Default value | Upper limit  
---|---|---  
Number of clusters per Google Cloud project | 20 | NA  
Number of node pools per cluster | 10 | NA  
Number of nodes per cluster | 500 | 1000  
Number of nodes per node pool | 50 | 500  
Number of pods per node | 110 | 110  
  
In addition to these quotas, your GKE on AWS installation is subject to any [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) on your AWS account, including the following:

  * [EC2](https://docs.aws.amazon.com/general/latest/gr/ec2-service.html)
  * [ELB](https://docs.aws.amazon.com/general/latest/gr/elb.html)
  * [VPC](https://docs.aws.amazon.com/general/latest/gr/vpc-service.html)



For more information, see the [AWS Service Quotas](https://console.aws.amazon.com/servicequotas/home) console.

## What's next

  * [Operating system details](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/os-details)
  * [Supported versions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-versions)
  * [Supported regions](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
