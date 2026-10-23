---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/prerequisites/
title: AWS prerequisites overview \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:44.669761+00:00
---

# AWS prerequisites overview  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/prerequisites/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  AWS prerequisites overview Stay organized with collections  Save and categorize content based on your preferences. 

Before creating clusters or node pools in AWS, you need to prepare your AWS VPC.

## Prepare your VPC directly

You can prepare your VPC yourself by following the steps below. 

  1. [Configure the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cloud-sdk)

  2. [Configure the AWS CLI](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-aws-cli)

  3. [Create an AWS VPC](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-vpc)

  4. [Create an AWS KMS key](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-kms-key)

  5. [Create AWS IAM roles](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-aws-iam-roles)

  6. [Create an SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-ssh-keypair)




## Prepare your VPC with Terraform

If you're familiar with Terraform, you can [use Terraform to prepare your VPC](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster-with-terraform). The Terraform scripts also create a cluster and node pool.

## What's next

  * [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
