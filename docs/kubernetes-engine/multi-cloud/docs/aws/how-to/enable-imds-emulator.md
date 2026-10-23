---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/enable-imds-emulator/
title: Enable the IMDS emulator \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:51.635954+00:00
---

# Enable the IMDS emulator  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/enable-imds-emulator/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Enable the IMDS emulator Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can enable the IMDS emulator, which emulates the AWS instance metadata service (IMDS). You can run the emulator as a sidecar to enable legacy workloads to run in GKE on AWS node pools. If you have legacy workloads that don't support Workload Identity Federation for GKE directly, use this emulator to access IMDS data.

## Limitations

  * Your cluster must use a Kubernetes version of 1.24 or later.
  * The emulator is not supported in the [previous generation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/previous-generation) of GKE on AWS.
  * The IMDS emulator server only serves credential requests (`API_VERSION/meta-data/iam/security-credentials/`). All other metadata requests return a 404 error.
  * A sidecar deployment requires the init container to have the `NET_ADMIN` and `NET_RAW` [security context capacities](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/). If you're not sure if the container has these contexts, consult your security team.
  * The AWS STS token can last for one hour. The role token from EC2 metadata can last for 24 hours. This shouldn't affect your usage of the emulator, but you might need to know this information during a security audit.
  * The IMDS emulator only emulates IMDSv1 responses. IMDSv2 is not supported. 



## Enable the emulator

To enable the IMDS emulator, add a label and an annotation to metadata for a Pod. You can also enable the emulator using a Deployment, DaemonSet, or any other resource that creates Pods:

  1. Add the following label and value to your Pod:
         
         gkemulticloud.googleapis.com/aws-imds-emulator-enabled: "True"
         

The only acceptable value for this label is `True`. All other values (including `true` with a lowercase `t`) disable the emulator.

  2. Add the following annotation to your Pod:
         
         gkemulticloud.googleapis.com/aws-imds-emulator-role-arn: ARN_ROLE
         

Replace `ARN_ROLE` with an Amazon Resource Name (ARN) that specifies the role that you want the resource to have.




### Example

The following example is a Pod with the IMDS emulator enabled:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx
      labels:
        **gkemulticloud.googleapis.com/aws-imds-emulator-enabled : "True"**
      annotations:
        **gkemulticloud.googleapis.com/aws-imds-emulator-role-arn : "arn:aws:iam::123456789012:role/my-example-role"**
    spec:
     serviceAccountName: my-sa
     containers:
     - name: nginx
       image: nginx
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
