---
url: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/post-deployment/
title: Post-deployment tasks for SQL Server workloads \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:49.963485+00:00
---

# Post-deployment tasks for SQL Server workloads  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/deploy/sql-server/post-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Post-deployment tasks for SQL Server workloads Stay organized with collections  Save and categorize content based on your preferences. 

Before using your deployed SQL Server system, we recommend that you perform the post-deployment tasks described in this document.

## Review the deployment

After successfully deploying a SQL Server workload, you can review the deployment output and configuration on the dashboard.

### Review the deployment resources

To review the resources created during the deployment:

  1. Go to the Workload Manager page in the Google Cloud console.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page.

  4. Click **Deployment Output** tab to view a list of all resources that were created during the deployment, the resource type, and a link to the resource (if applicable).




### Review the deployment configuration

To review the deployment configuration:

  1. Go to the Workload Manager page in the Google Cloud console.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page.

  4. Click the **Details** tab to view the information that you've entered for the initial configuration of the deployment.




## Modify the system post deployment

In [Preview](https://cloud.google.com/products#product-launch-stages), Workload Manager does not support the ability to modify a deployment that was deployed within the console.

One option is to deploy a new system with the required settings and configurations, and then transfer any configuration or data from the original deployment. Later you can delete the original deployment once the transfer is complete and the new system is validated.

Alternatively, you can manually modify a resource that was deployed using normal modification methods outside of Workload Manager. However, this causes the deployment object within Workload Manager and the underlying Terraform state file to become out of sync with the actual state of the resources.

## Delete a deployment

When deleting a deployment, the tool attempts to only delete the resources that were created as part of the deployment. Shared resources or resources that existed before the deployment, such as secrets and VPCs are not deleted.

Deleting a resource is a permanent action and the resource or data residing on it is not recoverable. If you have not done so already, consider taking a backup of the system.

To delete a deployment, do the following:

  1. Go to the Workload Manager page in the Google Cloud console.

[Go to Workload Manager](https://console.cloud.google.com/workloads)

  2. In the left navigation pane, click **Deployments** to open the deployment dashboard.

  3. Select the name of the deployment to open the **Deployment information** page. In the **Deployment Output** tab, review all the resources that were deployed as part of the deployment.

  4. Click **Delete** at the top of the deployment information page and then confirm the deletion.




Additional items that were used to deploy the system might remain after the system is deleted. You can delete these items manually if you want to.

  * Within a Cloud Storage bucket: 
    * The Cloud Build history and logs
    * The Terraform and state file used by the original deployment
    * The SQL Server Installation media used in the deployment
  * Service accounts 
    * The Google-managed service account used by Workload Manager
    * The service account used by Cloud Build



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
