---
url: https://docs.cloud.google.com/architecture/application-development/three-tier-web-app/
title: Delete the Three-tier web app \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:12.274097+00:00
---

# Delete the Three-tier web app  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/application-development/three-tier-web-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Delete the Three-tier web app Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-10-08 UTC

**Caution:** The Jump Start Solution apps are no longer maintained. Three-tier web app has been migrated to an application template in Application Design Center. For details, see [Three-tier web app](https://docs.cloud.google.com/application-design-center/docs/three-tier-web-app).

This guide describes how to delete the Three-tier web app Jump Start Solution. Use this guide to delete an existing deployment of the solution.

## Cost

For an estimate of the cost of the Google Cloud resources that the three-tier web app solution uses, see the precalculated estimate in the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator?dl=CiRhMmQzOGJlMi0wNTE5LTQ3MTMtOTM5NC1jNDRkMzI4ZWY1YTcQHBokOUM3QTgxN0QtRTA5NS00NUQxLTk4QTQtQTg5OTdERDIzNjU1).

Use the estimate as a starting point to calculate the cost of your deployment. You can modify the estimate to reflect any configuration changes that you made to the resources that are used in the solution.

The precalculated estimate is based on assumptions for certain factors, including the following:

  * The Google Cloud locations where the resources are deployed.
  * The amount of time that the resources are used.



You can also review usage costs for resources that you have deployed. For more details, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports).

## Get the required IAM permissions

To delete an existing deployment, you need the Identity and Access Management (IAM) permissions that are listed in the following table. If you have the `roles/owner` [basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) for the project in which solution is deployed, then you already have all the necessary permissions. If you don't have the `roles/owner` role, then ask your administrator to grant these permissions (or the roles that include these permissions) to you.

IAM permission required | Predefined role that includes the required permissions  
---|---  
`serviceusage.services.enable` | [Service Usage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin)  
(`roles/serviceusage.serviceUsageAdmin`)  
`iam.serviceAccounts.create` | [Service Account Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin)  
(`roles/iam.serviceAccountAdmin`)  
`resourcemanager.projects.setIamPolicy` |  [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin)  
(`roles/resourcemanager.projectIamAdmin`)  
`config.deployments.create`  
`config.deployments.list` | [Cloud Infrastructure Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/config#config.admin)  
(`roles/config.admin`)  
  
#### Service account created for the solution

When you initiate the deletion process through the console, a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) is created to deploy the solution on your behalf (and to delete the deployment later if you choose). This service account is assigned certain IAM permissions _temporarily_ ; that is, the permissions are revoked automatically after the solution deployment and deletion operations are completed. Google recommends that after you delete the deployment, you delete the service account, as described later in this guide.

View the roles assigned to the service account

These roles are listed here in case an administrator of your Google Cloud project or organization needs this information.

  * `roles/artifactregistry.admin`
  * `roles/cloudsql.admin`
  * `roles/compute.networkAdmin`
  * `roles/iam.serviceAccountAdmin`
  * `roles/iam.serviceAccountUser`
  * `roles/redis.admin`
  * `roles/resourcemanager.projectIamAdmin`
  * `roles/run.admin`
  * `roles/servicenetworking.serviceAgent`
  * `roles/serviceusage.serviceUsageViewer`
  * `roles/vpcaccess.admin`



## Delete the deployment

When you no longer need the solution deployment, to avoid continued billing for the resources that you created, delete the deployment.

### Delete through the console

Use this procedure if you deployed the solution through the console.

  1. In the Google Cloud console, go to the **Solution deployments** page.

[Go to Solution deployments](https://console.cloud.google.com/products/solutions/deployments)

  2. Select the project that contains the deployment that you want to delete.

  3. Locate the deployment that you want to delete.

  4. In the row for the deployment, click more_vert **Actions** and then select **Delete**.

You might need to scroll to see **Actions** in the row.

  5. Enter the name of the deployment and then click **Confirm**.

The **Status** field shows **Deleting**.

If the deletion fails, see the troubleshooting guidance in Error when deleting a deployment.




When you no longer need the Google Cloud project that you used for the solution, you can delete the project. For more information, see Optional: Delete the project.

### Delete using the Terraform CLI

Use this procedure if you deployed the solution by using the Terraform CLI.

  1. In Cloud Shell, make sure that the current working directory is `$HOME/cloudshell_open/terraform-google-three-tier-web-app/`. If it isn't, go to that directory.

  2. Remove the resources that were provisioned by Terraform:
         
         terraform destroy
         

Terraform displays a list of the resources that will be destroyed.

  3. When you're prompted to perform the actions, enter `yes`.

Terraform displays messages showing the progress. After all the resources are deleted, Terraform displays the following message:
         
         Destroy complete!
         

If the deletion fails, see the troubleshooting guidance in Error when deleting a deployment.




When you no longer need the Google Cloud project that you used for the solution, you can delete the project. For more information, see Optional: Delete the project.

### Optional: Delete the project

If you deployed the solution in a new Google Cloud project, and if you no longer need the project, then delete it by completing the following steps:

**Caution:** If you delete a project, all the resources in the project are permanently deleted.

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. At the prompt, type the project ID, and then click **Shut down**. 



If you decide to retain the project, then delete the service account that was created for this solution, as described in the next section.

### Optional: Delete the service account

If you deleted the project that you used for the solution, then skip this section.

As mentioned earlier in this guide, when you deployed the solution, a service account was created on your behalf. The service account was assigned certain IAM permissions _temporarily_ ; that is, the permissions were revoked automatically after the solution deployment and deletion operations were completed, but the service account isn't deleted. Google recommends that you delete this service account.

  * If you deployed the solution through the Google Cloud console, go to the [**Solution deployments**](https://console.cloud.google.com/products/solutions/deployments) page. (If you're already on that page, refresh the browser.) A process is triggered in the background to delete the service account. No further action is necessary.

  * If you deployed the solution by using the Terraform CLI, complete the following steps:

    1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

    2. Select the project that you used for the solution.

    3. Select the service account that you want to delete.

The email ID of the service account that was created for the solution is in the following format:
           
           goog-sc-DEPLOYMENT_NAME-NNN@PROJECT_ID.iam.gserviceaccount.com
           

The email ID contains the following values:

       * DEPLOYMENT_NAME: the name of the deployment.
       * NNN: a random 3-digit number.
       * PROJECT_ID: the ID of the project in which you deployed the solution.
    4. Click **Delete**.




## Troubleshoot errors

The actions that you can take to diagnose and resolve errors depend on the deployment method and the complexity of the error.

### Error when deleting a deployment

In certain cases, attempts to delete a deployment might fail:

  * After deploying a solution through the console, if you change any resource that was provisioned by the solution, and if you then try to delete the deployment, the deletion might fail. The **Status** field on the **Solution deployments** page shows **Failed** , and the Cloud Build log shows the cause of the error.
  * After deploying a solution by using the Terraform CLI, if you change any resource by using a non-Terraform interface (for example, the console), and if you then try to delete the deployment, the deletion might fail. The messages in the output of the `terraform destroy` command show the cause of the error.



Review the error logs and messages, identify and delete the resources that caused the error, and then try deleting the deployment again.

If a console-based deployment doesn't get deleted and if you can't diagnose the error by using the Cloud Build log, then you can delete the deployment by using the Terraform CLI, as described in the next section.

### Delete a console-based deployment by using the Terraform CLI

This section describes how to delete a console-based deployment if errors occur when you try to delete it through the console. In this approach, you download the Terraform configuration for the deployment that you want to delete and then use the Terraform CLI to delete the deployment.

  1. Identify the region where the deployment's Terraform code, logs, and other data are stored. This region might be different from the region that you selected while deploying the solution.

     1. In the Google Cloud console, go to the **Solution deployments** page.

[Go to Solution deployments](https://console.cloud.google.com/products/solutions/deployments)

     2. Select the project that contains the deployment that you want to delete.

     3. In the list of deployments, identify the row for the deployment that you want to delete.

     4. Click expand_more **View all row content**.

     5. In the **Location** column, note the _second_ location, as highlighted in the following example:

![Location of the deployment code, logs and other artifacts.](https://docs.cloud.google.com/static/architecture/images/solution-deployment-location.png)

  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. Create environment variables for the project ID, region, and name of the deployment that you want to delete:
         
         export REGION="REGION"
         export PROJECT_ID="PROJECT_ID"
         export DEPLOYMENT_NAME="DEPLOYMENT_NAME"
         

In these commands, replace the following:

     * REGION: the location that you noted earlier in this procedure.
     * PROJECT_ID: the ID of the project where you deployed the solution.
     * DEPLOYMENT_NAME: the name of the deployment that you want to delete.
  4. Get the ID of the latest revision of the deployment that you want to delete:
         
         export REVISION_ID=$(curl \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1alpha2/projects/${PROJECT_ID}/locations/${REGION}/deployments/${DEPLOYMENT_NAME}" \
             | jq .latestRevision -r)
             echo $REVISION_ID
         

The output is similar to the following:
         
         projects/PROJECT_ID/locations/REGION/deployments/DEPLOYMENT_NAME/revisions/r-0
         

  5. Get the Cloud Storage location of the Terraform configuration for the deployment:
         
         export CONTENT_PATH=$(curl \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1alpha2/${REVISION_ID}" \
             | jq .applyResults.content -r)
             echo $CONTENT_PATH
         

The following is an example of the output of this command:
         
         gs://PROJECT_ID-REGION-blueprint-config/DEPLOYMENT_NAME/r-0/apply_results/content
         

  6. Download the Terraform configuration from Cloud Storage to Cloud Shell:
         
         gcloud storage cp $CONTENT_PATH $HOME --recursive
         cd $HOME/content/
         

Wait until the `Operation completed` message is displayed, as shown in the following example:
         
         Operation completed over 45 objects/268.5 KiB
         

  7. Initialize Terraform:
         
         terraform init
         

Wait until you see the following message:
         
         Terraform has been successfully initialized!
         

  8. Remove the deployed resources:
         
         terraform destroy
         

Terraform displays a list of the resources that will be destroyed.

If any warnings about undeclared variables are displayed, ignore the warnings.

  9. When you're prompted to perform the actions, enter `yes`.

Terraform displays messages showing the progress. After all the resources are deleted, Terraform displays the following message:
         
         Destroy complete!
         

  10. Delete the deployment artifact:
         
         curl -X DELETE \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1alpha2/projects/${PROJECT_ID}/locations/${REGION}/deployments/${DEPLOYMENT_NAME}?force=true&delete_policy=abandon"
         

  11. Wait a few seconds and then verify that the deployment artifact was deleted:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://config.googleapis.com/v1alpha2/projects/${PROJECT_ID}/locations/${REGION}/deployments/${DEPLOYMENT_NAME}" \
             | jq .error.message
         

If the output shows `null`, wait a few seconds and then run the command again.

After the deployment artifact is deleted, a message as shown in the following example is displayed:
         
         Resource 'projects/PROJECT_ID/locations/REGION/deployments/DEPLOYMENT_NAME' was not found
         




## What's next

  * [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview)
  * [Cloud Run: General development tips](https://docs.cloud.google.com/run/docs/tips/general)
  * [Memorystore for Redis: Memory management best practices](https://docs.cloud.google.com/memorystore/docs/redis/memory-management-best-practices)
  * [Memorystore for Redis: General best practices](https://docs.cloud.google.com/memorystore/docs/redis/general-best-practices)
  * [Cloud SQL: General best practices](https://docs.cloud.google.com/sql/docs/best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-10-08 UTC."],[],[]] 
