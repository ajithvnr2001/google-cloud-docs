---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-ssh-keypair/
title: Create an SSH key pair \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:29.043185+00:00
---

# Create an SSH key pair  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-ssh-keypair/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an SSH key pair

To enable encrypted communications with your cluster, you must create an asymmetric key pair (a public and a private key) and associate it with your control plane or node pool virtual machines.

To generate an asymmetric key pair, run the following command:
    
    
    ssh-keygen -t rsa -m PEM -b 4096 -C "COMMENT" \
        -f SSH_PRIVATE_KEY -N "" 1>/dev/null
    

Replace the following:

  * `SSH_PRIVATE_KEY`: a file name to save the key in
  * `COMMENT`: a text string describing the key



This creates two files: `SSH_PRIVATE_KEY` containing your SSH private key, and `SSH_PRIVATE_KEY.pub` containing the corresponding public key.

To save your SSH public key into an environment variable, run the following command:
    
    
    SSH_PUBLIC_KEY=$(cat SSH_PRIVATE_KEY.pub)
    

## What's next

  * [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/quickstart)
  * [Create a cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
