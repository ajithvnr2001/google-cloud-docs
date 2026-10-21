---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/learning-path-cleanup/
title: Clean up the sample cluster and workload \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:42:35.602515+00:00
---

# Clean up the sample cluster and workload  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/learning-path-cleanup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Clean up the sample cluster and workload Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

When you finish learning about GKE, clean up to avoid billing charges.

If you plan to take additional tutorials, wait until you finish those tutorials before you clean up. You can use the sample Kubernetes cluster in most GKE tutorials.

## Clean up to avoid billing charges

If you created a new project to learn about GKE and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).

If you used an existing GKE project, delete the resources you created to avoid incurring charges to your account:

  1. Go to the GKE **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the row containing **hello-world-cluster** , and click **Delete**.

  3. In the **Delete hello-world-cluster** window, do the following:

     1. In the **hello-world-cluster** field, enter `hello-world-cluster`.

     2. Click **Delete**.

If you receive an error message about the cluster being repaired, you can wait for the process to complete, and then delete the cluster. This operation might take some time to complete.

  4. If you created a logs sink and bucket when following instructions in other tutorials:

     1. Go to the Cloud Logging **Logs storage** page.

[Go to Logs storage](https://console.cloud.google.com/logs/storage)

     2. Select **hello-world-cluster-bucket** and click **Delete**.

     3. Go to the Logging **Log router** page.

[Go to Log router](https://console.cloud.google.com/logs/router)

     4. Select **hello-world-cluster-sink** and click **Delete**.




## What's next

  * View [code samples](https://docs.cloud.google.com/docs/samples) demonstrating the usage of Google Cloud products.

  * Discover [best practices and reference architectures](https://docs.cloud.google.com/architecture/application-development) for application development "Architecture guides for application development"

  * [Plan, architect, deploy, and operate](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/scalability) large workloads on GKE clusters while scaling workloads within service-level objectives (SLOs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
