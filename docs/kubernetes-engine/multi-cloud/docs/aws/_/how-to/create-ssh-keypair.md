---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/create-ssh-keypair/
title: Create an EC2 key pair \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:41:26.897848+00:00
---

# Create an EC2 key pair  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws//how-to/create-ssh-keypair/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Create an EC2 key pair Stay organized with collections  Save and categorize content based on your preferences. 

You can associate a specific SSH key pair with control plane or node pool instances during creation.

To generate an asymmetric private key and import its public key into AWS, run the following commands:
    
    
    ssh-keygen -t rsa -m PEM -b 4096 -C "COMMENT" \
          -f SSH_PRIVATE_KEY -N "" 1>/dev/null
    
    aws ec2 import-key-pair --key-name SSH_KEY_PAIR_NAME \
          --public-key-material fileb://SSH_PRIVATE_KEY.pub
    

Replace the following:

  * `SSH_PRIVATE_KEY`: a file name to save the key in
  * `SSH_KEY_PAIR_NAME`: a name you choose for the key pair
  * `COMMENT`: a text string describing the key



## What's next

  * [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/quickstart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
