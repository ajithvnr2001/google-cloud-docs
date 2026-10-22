---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/firewalls-vpc-endpoints/
title: Firewall rules and VPC endpoints \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:20.255966+00:00
---

# Firewall rules and VPC endpoints  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/firewalls-vpc-endpoints/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/apis)



Send feedback 

#  Firewall rules and VPC endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page lists firewall requirements and VPC endpoint requirements for GKE on AWS.

## Firewall requirements

To use GKE on AWS, you must allow your cluster access to the following domains.
    
    
    .gcr.io
    cloudresourcemanager.googleapis.com
    container.googleapis.com
    gkeconnect.googleapis.com
    gkehub.googleapis.com
    oauth2.googleapis.com
    securetoken.googleapis.com
    storage.googleapis.com
    sts.googleapis.com
    www.googleapis.com
    servicecontrol.googleapis.com
    logging.googleapis.com
    monitoring.googleapis.com
    opsconfigmonitoring.googleapis.com
    GCP_LOCATION-gkemulticloud.googleapis.com
    

Replace `GCP_LOCATION` with the Google Cloud region in which your GKE on AWS cluster resides. Specify `us-west1` or another [supported region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/supported-regions).

## VPC Endpoints

VPC endpoints let resources in private subnets access AWS services without public internet access.

The following table lists the AWS services that GKE on AWS requires VPC endpoints for, along with the type of endpoint and the [Security Groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/security-groups) that require access to the endpoint.

Service | Endpoint type | Security groups  
---|---|---  
[Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/aws-auto-scaling-vpc-endpoints.html) | Interface | Control plane, node pools  
[EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interface-vpc-endpoints.html) | Interface | Control plane, node pools  
[EFS](https://docs.aws.amazon.com/efs/latest/ug/efs-vpc-endpoints.html) | Interface | Control plane  
[Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/load-balancer-vpc-endpoints.html) | Interface | Control plane, node pools  
[Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html) | Interface | Control plane, node pools  
[S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) | Gateway | Control plane, node pools  
[Secrets Manager](https://docs.aws.amazon.com/secretsmanager/index.html) | Interface | Control plane, node pools  
[Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) | Interface | Control plane, node pools  
**Important:** You must enable [Private DNS](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-private-dns) (also called **Enable DNS name** on the AWS console) on interface endpoints.

You can create endpoints from the AWS [VPC Console](https://console.aws.amazon.com/vpc/home). The options you set when creating VPC endpoints depend on your VPC configuration.

## What's next

  * [Use a proxy](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-a-proxy) for your GKE clusters.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
