---
url: https://docs.cloud.google.com/cloud-assist/turn-off/
title: Remove Gemini Cloud Assist access \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:34.372769+00:00
---

# Remove Gemini Cloud Assist access  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/turn-off/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Remove Gemini Cloud Assist access Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).

This document shows you how to remove Gemini Cloud Assist access across your Google Cloud projects or organization.

For information about changing the settings that control sharing Gemini Cloud Assist prompts and responses with Google, see [Configure prompt and response sharing for Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/configure-prompt-response-sharing).

## Before you begin

In order to get the required permissions for turning off Gemini Cloud Assist, ask your administrator to grant you the [Owner or Admin basic role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner` or `roles/admin`) on the project.

Both of these roles contain the permissions required to remove access for users and to disable services.

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`
  * `serviceusage.services.disable`
  * If you intend to use the Google Cloud console to turn off Gemini Cloud Assist, you should also have the following permissions: 
    * `serviceusage.services.get`
    * `serviceusage.services.list`



You might be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Remove Gemini Cloud Assist access

To turn off Gemini Cloud Assist, do the following:

###  Console 

  1. To limit access for specific users in your organization, remove Identity and Access Management permissions for Gemini Cloud Assist:

     1. Go to the **IAM & Admin** page.

[Go to IAM & Admin](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=)

     2. In the **Principal** column, find a principal for which you want to remove access to Gemini Cloud Assist, and then click edit **Edit principal** in that row.

     3. In the **Edit access** pane, do the following:

        1. Locate any Gemini Cloud Assist IAM roles, and then click delete **Delete role**. The most common role for a user is the **Gemini Cloud Assist User** role.

**Note:** Depending on when you granted the principal access to Gemini Cloud Assist, they might have the **Gemini for Google Cloud User** role instead of, or in addition to, Gemini Cloud Assist roles. To fully remove a user's access to Gemini Cloud Assist, you must also remove the **Gemini for Google Cloud User** role, but be aware that this role might also grant the user access to other Gemini products in Google Cloud.
        2. Optional: Locate any IAM roles that you granted [specifically for use with Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements), and then click delete **Delete role**.

     4. Click **Save**.

  2. Turn off the Gemini Cloud Assist API (`geminicloudassist.googleapis.com`):

     1. Go to the **Enabled APIs & services** page.

[Go to Enabled APIs & services](https://console.cloud.google.com/project/_/apis/dashboard)

     2. To select the Google Cloud project where you want to disable the Gemini Cloud Assist API, do one of the following:

        * In the **Select a recent project** section, click a Google Cloud project.

        * Use the **Select a resource** dialog:

          1. Click **Select project**.
          2. In the **Select a project** dialog, click the name of the Google Cloud project for which you want to disable the API.
     3. Click the **Gemini Cloud Assist API** entry. If you need help finding the API, use the **Search** field in the Google Cloud console toolbar.

     4. Click _stop_ **Disable API**.

  3. Optional: To disable all Gemini for Google Cloud products, repeat the previous step for the Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. To limit access for specific users in your organization, remove Identity and Access Management permissions for Gemini Cloud Assist:

     1. Remove any Gemini Cloud Assist IAM roles for the user, using the command [`gcloud projects remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/remove-iam-policy-binding). Gemini Cloud Assist roles are prefixed with `roles/geminicloudassist`. For example, the following command removes `roles/geminicloudassist.user`, a typical Gemini Cloud Assist role:
            
            gcloud projects remove-iam-policy-binding PROJECT_ID \
              --member=PRINCIPAL --role=roles/geminicloudassist.user
            

Replace the following:

        * `PROJECT_ID`: the ID of your Google Cloud project. For example,`1234567890`.
        * `PRINCIPAL`: the [identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers) for the principal. For example, `user:cloudysanfrancisco@gmail.com`.

The output is a list of policy bindings.

**Note:** Depending on when you granted the principal access to Gemini Cloud Assist, they might have the `roles/cloudaicompanion.user` role instead of, or in addition to, Gemini Cloud Assist roles. To fully remove a user's access to Gemini Cloud Assist, you must also remove the `roles/cloudaicompanion.user` role, but be aware that this role might also grant the user access to other Gemini products in Google Cloud.
     2. Optional: Repeat the previous step to remove any IAM roles that you granted [specifically for use with Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements).

  3. Turn off the Gemini Cloud Assist API (`geminicloudassist.googleapis.com`) using the command [`gcloud services disable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/disable):
         
         gcloud services disable geminicloudassist.googleapis.com
         

If successful, the command produces output similar to the following:
         
         Waiting for async operation operations/acf.e9d0943b-55d9-4ac0-8af4-745e1b8983f8 to complete...
           Operation finished successfully.
         

  4. Optional: To disable all Gemini for Google Cloud products, repeat the previous step for the Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`).




###  API 

These instructions use [`cURL`](http://curl.haxx.se/) to call API methods.

  1. To limit access for specific users in your organization, remove Identity and Access Management permissions for Gemini Cloud Assist:

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

     3. Copy the project's IAM policy to an empty JSON file, and remove the user from the `members` field of any `role` that begins with `roles/geminicloudassist`, such as `roles/geminicloudassist.user`.

**Note:** Depending on when you granted the principal access to Gemini Cloud Assist, they might appear in the `members` field of the `roles/cloudaicompanion.user` role instead of, or in addition to, Gemini Cloud Assist roles. To fully remove a user's access to Gemini Cloud Assist, you must also remove the user from the `roles/cloudaicompanion.user` role, but be aware that this role might also grant the user access to other Gemini products in Google Cloud.
     4. Optional: Repeat the previous step to remove any IAM roles that you granted [specifically for use with Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/iam-requirements).

     5. Apply the updated IAM policy to the project using the [`projects.setIamPolicy` method](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy):
            
            curl -X POST --data-binary @JSON_FILE_NAME \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                -H "Content-Type: application/json" \
                "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy"
            

Replace the following:

        * `JSON_FILE_NAME`: the path for the JSON file that you created in the previous step.

        * `PROJECT_ID`: the ID for the project.

If successful, the response returns the project's updated IAM policy.

  2. Turn off the Gemini Cloud Assist API (`geminicloudassist.googleapis.com`) using the [`services.disable` method](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/disable):
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://serviceusage.googleapis.com/v1/projects/PROJECT_ID/services/geminicloudassist.googleapis.com:disable"
         

Replace `PROJECT_ID` with the ID of the project for which you are disabling Gemini Cloud Assist.

If the command succeeds, it returns a [`long-running operation`](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations), which includes a `name` field. You can use the value in the `name` field to [check the status of the operation](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations/get).

  3. Optional: To disable all Gemini for Google Cloud products, repeat the previous step for the Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
