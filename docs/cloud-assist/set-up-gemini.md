---
url: https://docs.cloud.google.com/cloud-assist/set-up-gemini/
title: Set up Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:32.635178+00:00
---

# Set up Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/set-up-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Set up Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).

[Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) helps you design, operate, and optimize your cloud applications and infrastructure with contextual AI guidance. Before team members can use these features, an administrator must complete initial setup for a project or a folder.

## Set up Gemini Cloud Assist for a project

**Caution:** Gemini Cloud Assist can store data in any Google Cloud data center globally. You shouldn't enable the Gemini Cloud Assist API for projects that have data residency or [customer-managed encryption key](https://docs.cloud.google.com/kms/docs/cmek) requirements.

The following steps detail how to set up Gemini Cloud Assist for a project.

###  Console 

**Important:** If your project is contained within a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters), you can't use the Google Cloud console instructions to set up Gemini Cloud Assist. Attempting to do so results in an error, because the Google Cloud console requires the App Optimize API to also be enabled, but the App Optimize API is not supported by VPC Service Controls. Use the gcloud CLI instructions instead to set up Gemini Cloud Assist.

  1. Go to the **Admin for Gemini** page.

[Go to Gemini for Google Cloud](https://console.cloud.google.com/gemini-admin/products)

  2. From the project picker at the top of the page, select your project resource.

  3. Select **Get Gemini Cloud Assist**.

  4. In the **Get Gemini Cloud Assist** dialog, do the following:

     1. Select the expand_more expander arrow found in the **Required & recommended APIs** section.

     2. In the **Recommended APIs** list, select any additional APIs you want to enable to improve the performance of Gemini Cloud Assist.

     3. Optional: Select **Help Google improve Cloud Assist by sharing your prompts and answers**.

     4. Select **Enable Gemini Cloud Assist at no cost**.

  5. Click **Save**.

  6. Grant the IAM roles that are required to use Gemini Cloud Assist.

     1. Go to the **IAM & Admin** page.

[Go to IAM & Admin](https://console.cloud.google.com/projectselector/iam-admin/iam)

     2. In the **Principal** column, find a [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) for which you want to give access to Gemini Cloud Assist, and then click edit **Edit principal** in that row.

     3. In the **Edit access** pane, click add **Add another role**.

     4. In **Select a role** , select **Gemini Cloud Assist User**.

     5. Click **Add another role** and select **Cloud Asset Viewer**.

     6. If the principal wants to get assistance with products they don't already have access to, you might need to grant them additional IAM roles by clicking **Add another role** and selecting additional roles. See [IAM requirements for using Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements) for a table of IAM roles that enable an optimal Gemini Cloud Assist experience for different products.

     7. If your project is part of an organization that uses [custom constraints](https://docs.cloud.google.com/organization-policy/overview#custom-constraints), review [permissions required for chat](https://docs.cloud.google.com/cloud-assist/iam-requirements#chat) to ensure that Gemini Cloud Assist chat isn't blocked.

  7. (Optional) [Configure settings for the project](https://docs.cloud.google.com/gemini/docs/admin-settings).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Enable the Gemini Cloud Assist API using the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
         
         gcloud services enable geminicloudassist.googleapis.com
         

This step also enables the Gemini for Google Cloud API, which is also required to use Gemini Cloud Assist.

If you want to enable the Gemini Cloud Assist API in a different Google Cloud project, add the `--project` parameter:
         
         gcloud services enable geminicloudassist.googleapis.com --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project for which you are enabling Gemini Cloud Assist.

The output is similar to the following:
         
         Waiting for async operation operations/acf.2e2fcfce-8327-4984-9040-a67777082687 to complete...
         Operation finished successfully.
         

  3. Enable [other required APIs](https://docs.cloud.google.com/cloud-assist/api-recommendations#required-apis) using the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) as you did to enable the Gemini Cloud Assist API:
         
         gcloud services enable cloudasset.googleapis.com designcenter.googleapis.com appoptimize.googleapis.com apphub.googleapis.com --project PROJECT_ID
         

**Important:** If your project is contained within a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters), exclude `appoptimize.googleapis.com` from the command, because the App Optimize API is not supported by VPC Service Controls.
  4. (Optional) Enable [recommended APIs](https://docs.cloud.google.com/cloud-assist/api-recommendations#recommended-apis) using the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) as you did to enable the Gemini Cloud Assist API.

  5. Grant IAM roles in a Google Cloud project. For more information, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) and [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).

     1. Grant the `roles/geminicloudassist.user` role:
            
            gcloud projects add-iam-policy-binding PROJECT_ID \
              --member=PRINCIPAL --role=roles/geminicloudassist.user
            

Replace the following:

        * `PROJECT_ID`: the ID of your Google Cloud project—for example,`1234567890`.
        * `PRINCIPAL`: the [identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers) for the principal—for example, `user:cloudysanfrancisco@gmail.com`.

The output is a list of policy bindings that includes the following:
    
    - members:
      - user:PRINCIPAL
      role: roles/geminicloudassist.user
    

     2. Repeat the previous step for the role `roles/cloudasset.viewer`.

     3. If the principal wants to get assistance with products they don't already have access to, you might need to grant them additional IAM roles. See [IAM requirements for using Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements) for a table of IAM roles that enable an optimal Gemini Cloud Assist experience for different products.

     4. If your project is part of an organization that uses [custom constraints](https://docs.cloud.google.com/organization-policy/overview#custom-constraints), review [permissions required for chat](https://docs.cloud.google.com/cloud-assist/iam-requirements#chat) to ensure that Gemini Cloud Assist chat isn't blocked.

  6. (Optional) [Configure settings for the project](https://docs.cloud.google.com/gemini/docs/admin-settings).




###  API 

These instructions use [`cURL`](http://curl.haxx.se/) to call API methods.

  1. Enable the Gemini Cloud Assist API using the [`services.enable` method](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable):
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services/geminicloudassist.googleapis.com:enable"
         

Replace `PROJECT_ID` with the ID of the project for which you are enabling Gemini Cloud Assist.

If the command succeeds, it returns a [`long-running operation`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations), which includes a `name` field. You can use the value in the `name` field to [check the status of the operation](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations/get).

**Note:** Enabling the service `geminicloudassist.googleapis.com` also enables the service `cloudaicompanion.googleapis.com`, which is required to use Gemini Cloud Assist.
  2. Enable the following [additional required APIs](https://docs.cloud.google.com/cloud-assist/api-recommendations#required-apis) using the [`services.enable` method](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) as you did to enable the Gemini Cloud Assist API:

     * `cloudasset.googleapis.com`
     * `designcenter.googleapis.com`
     * `appoptimize.googleapis.com`
     * `apphub.googleapis.com`
**Important:** If your project is contained within a [VPC Service Controls service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters), exclude `appoptimize.googleapis.com` from the group of enabled APIs, because the App Optimize API is not supported by VPC Service Controls.
  3. (Optional) Enable [recommended APIs](https://docs.cloud.google.com/cloud-assist/api-recommendations#recommended-apis) using the [`services.enable` method](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable) as you did to enable the Gemini Cloud Assist API.

  4. Grant IAM roles for the associated Google Cloud project.

     1. Create a JSON file that contains the following information:
            
            {
                "options": {
                  "requestedPolicyVersion": 3
                }
              }
            

     2. Retrieve the existing IAM policy for the project using the [`projects.getIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy):
            
            curl -X POST --data-binary @JSON_FILE_NAME \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                -H "Content-Type: application/json" \
                "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy"
            

Replace the following:

        * `JSON_FILE_NAME`: the path for the JSON file that you created in the previous step.

        * `PROJECT_ID`: the ID for the project.

If successful, the response returns the project's IAM policy.

     3. Copy the project's IAM policy to an empty JSON file, and add the following information to the existing content:
            
            {
                "role": "roles/geminicloudassist.user",
                "members": [
                  "PRINCIPAL"
                ]
              },
              {
                "role": "roles/cloudasset.viewer",
                "members": [
                  "PRINCIPAL"
                ]
              }
            

Replace `PRINCIPAL` with the identifier for the principal to which you are granting Gemini Cloud Assist access.

     4. Apply the updated IAM policy to the project using the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy):
            
            curl -X POST --data-binary @JSON_FILE_NAME \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                -H "Content-Type: application/json" \
                "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy"
            

Replace the following:

        * `JSON_FILE_NAME`: the path for the JSON file that you created in the previous step.

        * `PROJECT_ID`: the ID for the project.

If successful, the response returns the project's updated IAM policy.

     5. If the principal wants to get assistance with products they don't already have access to, you might need to grant them additional IAM roles. See [IAM requirements for using Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements) for a table of IAM roles that enable an optimal Gemini Cloud Assist experience for different products.

     6. If your project is part of an organization that uses [custom constraints](https://docs.cloud.google.com/organization-policy/overview#custom-constraints), review [permissions required for chat](https://docs.cloud.google.com/cloud-assist/iam-requirements#chat) to ensure that Gemini Cloud Assist chat isn't blocked.

  5. (Optional) [Configure settings for the project](https://docs.cloud.google.com/gemini/docs/admin-settings).




## Set up Gemini Cloud Assist for a folder

The following steps detail how to set up Gemini Cloud Assist for a folder using the Google Cloud console. You can't use the Google Cloud CLI or the API to set up Gemini Cloud Assist for folders.

  1. Enable required and recommended APIs.

     1. Go to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin/products)

     2. From the project picker at the top of the page, select your folder resource.

     3. Select **Enable Cloud Assist APIs**.

The **Enable API for existing projects within folder** dialog appears.

     4. In the **Enable API for existing projects within a folder** dialog, select the expand_more expander arrow found in the **Required & recommended APIs** section.

     5. In the **Recommended APIs** list, select any optional APIs you want to enable.

     6. Optional: Select **Help Google improve Cloud Assist by sharing your prompts and answers**.

     7. Select **Enable Gemini Cloud Assist at no cost**.

This step enables the required and selected recommended APIs for all projects in the folder. If you want exceptions for some projects in the folder, then you can block API enablement by setting a **Restrict Resource Service Usage** [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#constraints) on those projects. For more information, see [Restricting resource usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-resources).

  2. [Grant the following IAM roles](https://docs.cloud.google.com/iam/docs/grant-role-console) or [create custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles#console) with equivalent permissions on the _folder_ :

     * **Gemini Cloud Assist User**
     * **Cloud Asset Viewer**

If the principal wants to get assistance with products they don't already have access to, you might need to grant them additional IAM roles. See [IAM requirements for using Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements) for a table of IAM roles that enable an optimal Gemini Cloud Assist experience for different products.

  3. If your folder is part of an organization that uses [custom constraints](https://docs.cloud.google.com/organization-policy/overview#custom-constraints), review [permissions required for chat](https://docs.cloud.google.com/cloud-assist/iam-requirements#chat) to ensure that Gemini Cloud Assist chat isn't blocked.

  4. If you are using Gemini Cloud Assist with applications, then you must also enable [application management at the folder level](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder). This step creates a management project to which you must link a billing account.

     1. Return to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin/products)

     2. Select **Enable App Management**.

The **IAM & Admin** settings page appears.

     3. Select **Enable** in the **App-enablement** section of the page.

The **Enable application APIs on this folder** dialog appears.

     4. Select **Enable**.

A status bar displays the progress of the API enablement. The **IAM & Admin** settings page refreshes when API enablement completes.

     5. Select **Manage billing**.

The **Linked account** page appears.

     6. Select a billing account from the list, and then select **Set account**.

  5. [Grant the IAM roles](https://docs.cloud.google.com/iam/docs/grant-role-console) that you granted to the _folder_ in step 2, or [create custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles#console) with equivalent permissions to the _management project_ created in the previous step.

Find the management project for the folder:

     1. Return to the **Admin for Gemini** page.

[Go to Admin for Gemini](https://console.cloud.google.com/gemini-admin/products)

     2. From the project picker at the top of the page, select your folder resource.

     3. Select **Manage Gemini Cloud Assist Settings**.

The **Manage Gemini Cloud Assist** dialog appears.

     4. Note the **Management project**.

  6. (Optional) [Configure settings for projects in the folder](https://docs.cloud.google.com/gemini/docs/admin-settings).


**Important:** Projects added to this folder in the future won't automatically have Gemini Cloud Assist enabled. For such projects, you must enable Gemini Cloud Assist for the project after creating the project.

## What's next

  * Learn about [Gemini Cloud Assist pricing](https://cloud.google.com/products/gemini/pricing).
  * Learn how to [use the **Cloud Assist** panel in the Google Cloud console](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Learn how to [configure additional settings for Gemini Cloud Assist](https://docs.cloud.google.com/gemini/docs/admin-settings). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
