---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/delete/
title: Delete a deployment \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:31.951117+00:00
---

# Delete a deployment  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Delete a deployment Stay organized with collections  Save and categorize content based on your preferences. 

When you no longer need a deployment that you created by using Workload Manager, you can delete it to free up resources, stop incurring costs, or remove a test environment. When you delete a deployment, Workload Manager: Guided Deployment Automation deletes only the resources that were created as part of that deployment. It doesn't delete shared resources or resources that existed before the deployment, such as Secrets and Virtual Private Cloud (VPC) networks.

To delete a deployment, do the following.

**Caution:** Deleting a resource is a permanent action, and the resource or data residing on it might not be recoverable. If you haven't done so already, consider backing up the system.

  1. In the Google Cloud console, go to the Workload Manager **Deployments** page.

[Go to Deployments](https://console.cloud.google.com/workload-manager/deployments)

  2. Select the deployment that you want to delete. You see the deployment details page.

  3. In the **Deployment Output** tab, review all the resources that were deployed as part of the deployment.

  4. If you want to continue with deletion, click **Delete** at the top of the deployment details page and then confirm the deletion.




After you delete the deployment, you can manually delete the following remaining resources from the Cloud Storage bucket:

  * The Cloud Build history and logs
  * The Terraform and state file used by the original deployment
  * The [SAP installation media](https://docs.cloud.google.com/workload-manager/docs/deploy/sap/sap-install-files#upload-install-files) used in the deployment



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
