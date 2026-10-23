---
url: https://docs.cloud.google.com/app-hub/docs/grant-access-applications/
title: Grant permissions to applications \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:33.393302+00:00
---

# Grant permissions to applications  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/grant-access-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Grant permissions to applications Stay organized with collections  Save and categorize content based on your preferences. 

Configure who can access your [App Hub applications](https://docs.cloud.google.com/app-hub/docs/key-concepts#application) by assigning [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles to principals, such as users, groups, or service accounts. Applications are contained within an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), which is a project or a folder of projects, and are managed by a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project).

You can grant these permissions on the management project to principals in two ways:

  * Grant access to all applications in the boundary.
  * Grant access to individual applications in the boundary.



For recommended roles, see [Grant application-centric roles to your users](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles).

## Grant access to all applications

To grant access to all applications within your application management boundary, assign an IAM role to a principal on the management project:

###  Console 

  1. In the Google Cloud console, use the project picker to select your management project.

  2. Navigate to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project)

  3. Click person_add **Grant access**.

  4. Enter an identifier for the principal who will get access to all applications within the boundary. For example, `user@example.com`.

  5. From the **Select a role** drop-down menu, search for the role you want to assign and click it.

  6. Click **Save**.

  7. Verify that the principal and the corresponding role are listed in the IAM page.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the management project.

  2. Add a [policy binding](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access):
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
            --member=USER_EMAIL \
            --role=ROLE
         

Replace the following:

     * `PROJECT_ID`: the ID of the management project.
     * `USER_EMAIL`: the email address of the user who will get access to all applications within the boundary, such as `user@example.com`.
     * `ROLE`: the role that you want to provide to the user, such as `roles/apphub.editor`.



## Grant access to individual applications

To grant access to individual applications within your [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), assign an IAM role to a principal on the application:

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the management project.

  2. Set a [IAM policy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy):
         
         gcloud apphub applications set-iam-policy APPLICATION_NAME \
            --project=PROJECT_ID \
            --location=LOCATION \
            POLICY_FILE
         

Replace the following:

     * `APPLICATION_NAME`: the name of your application. The name must include only lowercase alphanumeric characters without spaces, such as `my-application`.
     * `PROJECT_ID`: the ID of the management project.
     * `LOCATION`: the location of the application.
     * `POLICY_FILE`: the name of the policy file that grants the role to the user, such as `my-policy.yaml`.



The following example of a policy file grants the `roles/apphub.editor` role to the user `user@example.com`:
    
    
    # policyfile.yaml
    bindings:
    - role: roles/apphub.editor
      members:
      - user:user@example.com
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
