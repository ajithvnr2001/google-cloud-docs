---
url: https://docs.cloud.google.com/speech-to-text/priv/docs/configurations/
title: On-Prem API configuration parameters \u00a0|\u00a0 Cloud Speech-to-Text private documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:00.104920+00:00
---

# On-Prem API configuration parameters  |  Cloud Speech-to-Text private documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/priv/docs/configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text)
  * [ Cloud Speech-to-Text On-Prem ](https://docs.cloud.google.com/speech-to-text/priv)
  * [ Documentation ](https://docs.cloud.google.com/speech-to-text/priv/docs)



Send feedback 

#  On-Prem API configuration parameters Stay organized with collections  Save and categorize content based on your preferences. 

**Private feature**  
This product is a private feature. The documentation is publicly available but you must [contact Google](https://cloud.google.com/contact) for full access. 

The Speech-to-Text On-Prem solution exposes some configuration parameters. The parameters below are exposed in both CLI and marketplace app launcher installations.

Parameter name | Description  
---|---  
**Name** | The name of the application. The string "speech" is a safe default. This value is referred to as $NAME.  
**Namespace** | The namespace the application is deployed to. The string "speech" is a safe default. This value is referred to as $NAMESPACE.  
**Replicas** | The number of replicas you want the solution to run (default is 3). This allows you to scale your application horizontally. This value is referred to as $REPLICAS.  
**CPUs per pod** | How many CPUs to allocate to each pod that runs the Speech-to-Text binary. The default is 2, and at least 2 are recommended. This value is referred to as $CPU. If you specify more CPUs than are available in your cluster, the app throws errors such as "Does not have minimum availability" or "Pod errors: Unschedulable".  
**Memory per pod** | How much RAM to allocate to each pod running the Speech-to-Text binary. The default is 1Gi, and at least 1Gi is recommended. This value is referred to as $MEMORY. If you specify more Memory than is available in your cluster, the app throws errors such as "Does not have minimum availability" or "Pod errors: Unschedulable".  
**The Google Cloud Platform project ID to export metrics to** | (Optional) You can specify a Google Cloud Platform project ID so the On-Prem server can export metrics to Stackdriver in that Google Cloud Platform project. Use the same Google Cloud Platform project where the On-Prem server will be running. If you provide a different project, make sure that the service account running the On-Prem server has permission to send metrics to that project. If this field is empty, no metrics will be sent. This value is referred to as $METRIC_PROJECT.  
**Install Istio objects for load balancing** | (Optional) You can specify whether or not to install Istio objects for gRPC load balancing. If checked, incoming gRPC requests will be distributed to different pods to serve. You must have Istio already installed in the cluster, otherwise the installation will fail. This value is referred to as $ENABLE_ISTIO. See the [before you begin](https://docs.cloud.google.com/speech-to-text/priv/docs/before-you-begin) quickstart for more information on installing and setting up Istio.  
**Public IP** | (Optional) You can supply a public IP address in this field to make your solution publicly reachable. This only applies if your cluster supports public IPs and you have allocated one to the region your cluster is running in. If you do not supply a public IP, you will need to configure your networking yourself. This value is referred to as $PUBLIC_IP. Be aware that this public IP is accessible on the Internet.  
**Model 1** | You should specify the first language for the onprem server to serve incoming ASR requests. This value is referred to as $MODEL1.  
**Model 2** | You should specify the second language for the onprem server to serve incoming ASR requests. If you don't need a second language, you can choose None. This value is referred to as $MODEL2.  
**Model 3** | You should specify the third language for the onprem server to serve incoming ASR requests. If you don't need a third language, you can choose None. This value is referred to as $MODEL3.  
**Secret Name** | (Optional for GKE, Required for GKE On-Prem and other hybrid clouds) A Google service account from the Google Cloud Platform project allowlist is required for authentication in order for the k8s pods within GKE on-prem clusters to query Google Cloud services. This service account must have at least Project Viewer permission. Download a key for the Google service account and wrap it into a secret in the same namespace as the application. The file must be named as key.json. This value is referred to as $GSA_SECRET. See the [Kubernetes documentation](https://cloud.google.com/kubernetes-engine/docs/tutorials/authenticating-to-cloud-platform) for more details.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
