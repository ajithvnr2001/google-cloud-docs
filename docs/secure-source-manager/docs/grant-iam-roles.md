---
url: https://docs.cloud.google.com/secure-source-manager/docs/grant-iam-roles/
title: Grant and revoke IAM roles \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:35.582836+00:00
---

# Grant and revoke IAM roles  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/grant-iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Grant and revoke IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant Identity and Access Management (IAM) roles to principals on Secure Source Manager resources. For information on granting roles on other Google Cloud resources, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Secure Source Manager instances and repositories have their own roles. The first time you grant instance roles in a project you must use the gcloud CLI tool or the REST API. You can grant repository roles with the gcloud CLI tool, the REST API, or through the Secure Source Manager web interface.

After you have granted a Secure Source Manager role using the gcloud CLI, web interface, or the REST API, the role is visible for your project in the Google Cloud console.

## Required roles

To get the permissions that you need to update the IAM policy on an instance or repository, ask your administrator to grant you the following IAM roles: 

  * Grant instance IAM roles: [Secure Source Manager Instance Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceOwner) (`roles/securesourcemanager.instanceOwner`) on the Secure Source Manager instance 
  * Grant repository IAM roles: [Secure Source Manager Repo Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) on the repository 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Specify principals

A principal represents an identity that can access a resource. Each principal has its own identifier. Principal identifiers have the following form:
    
    
    PRINCIPAL-TYPE:ID
    

For example, `user:my-user@example.com`. For more information on principals, read [How IAM works](https://docs.cloud.google.com/iam/docs/overview#how_cloud_iam_works).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain unless you are using Workforce Identity Federation. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

### Workforce Identity Federation principals

If you use Workforce Identity Federation to access Secure Source Manager, then principals are represented differently. To learn more about granting access to principals that represent groups of identities, see [Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users).

For example, the following command grants the user `user@example.com` the Instance Accessor role (`roles/securesourcemanager.instanceAccessor`) in the workforce pool `my-pool` on the instance `my-instance` in the project `my-project` in the `us-central1` region:
    
    
      gcloud source-manager instances add-iam-policy-binding my-instance \
          --project=my-project \
          --region=us-central1 \
          --member=principal://iam.googleapis.com/locations/global/workforcePools/my-pool/subject/user@example.com \
          --role=roles/securesourcemanager.instanceAccessor
    

You can grant users or groups within your workforce identity pool based on your Identity provider (IdP) attributes, or use [Common Expression Language (CEL)](https://github.com/google/cel-spec) to map your OIDC attributes to custom attributes to define an authorization strategy in your IAM policy. For more information about attribute mappings, read [Attribute mappings](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings).

## Grant or revoke instance roles

To grant or revoke instance roles for principals, use the gcloud CLI tool or the Secure Source Manager API.

### `gcloud`

  1. To grant a role to a principal on an instance, run the following command:
         
         gcloud source-manager instances add-iam-policy-binding INSTANCE_ID \
             --project=PROJECT_ID \
             --region=REGION \
             --member=PRINCIPAL \
             --role=ROLE_NAME
         

Replace the following:

     * `INSTANCE_ID` with the instance ID.
     * `PROJECT_ID` with the project ID or project number of the instance.
     * `REGION` with the region the instance is located in. See the [locations documentation](https://docs.cloud.google.com/secure-source-manager/docs/locations) for available Secure Source Manager regions.
     * `PRINCIPAL` with the principal to grant the role to. For example, `user:my-user@example.com`.
     * `ROLE_NAME` with the name of the role to grant. For example, `roles/securesourcemanager.instanceOwner`.
  2. To revoke a role from a principal on an instance, run the following command:
         
         gcloud source-manager instances remove-iam-policy-binding INSTANCE_ID \
             --project=PROJECT_ID \
             --region=REGION \
             --member=PRINCIPAL \
             --role=ROLE_NAME
         

Replace the following:

     * `INSTANCE_ID` with the instance ID.
     * `PROJECT_ID` with the project ID or project number of the instance.
     * `REGION` with the region the instance is located in.
     * `PRINCIPAL` with the principal to revoke the role from. For example, `user:my-user@example.com`.
     * `ROLE_NAME` with the name of the role to revoke. For example, `roles/securesourcemanager.instanceOwner`.



### API

  1. Run the following [`instances.getIamPolicy`](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.instances/getIamPolicy) command to read the current policy:
         
         curl \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/instances/INSTANCE_ID:getIamPolicy > /tmp/instance.json
         

Replace the following:

     * `PROJECT_ID` the project ID or project number of the instance.
     * `REGION` the region the instance is located in. See the [locations documentation](https://docs.cloud.google.com/secure-source-manager/docs/locations) for available Secure Source Manager regions.
     * `INSTANCE_ID` the instance ID.

The output will include any existing bindings, or, if none exist, the `etag` value similar to the following:
    
    {
        "etag": "BwUjHYKJUiQ="
    }
    

  2. Programmatically or using a text editor, modify the local copy of your instance's allow policy to reflect the roles that you want to grant or revoke.

To ensure that you don't overwrite other changes, don't edit or remove the allow policy's `etag` field. The `etag` field identifies the current state of the allow policy. When you set the updated allow policy, IAM compares the `etag` value in the request with the existing `etag`, and only writes the allow policy if the values match.

**Important:** None of your changes will take effect until you set the updated allow policy.

To edit the roles that an allow policy grants, you need to edit the role bindings in the allow policy. Role bindings have the following format:
         
         {
           "role": "ROLE_NAME",
           "members": [
             "PRINCIPAL_1",
             "PRINCIPAL_2",
             ...
             "PRINCIPAL_N"
           ]
         }
         

The placeholders have the following values:

     * `ROLE_NAME`: The name of the role that you want to grant. Use the following format: `roles/securesourcemanager.IDENTIFIER`

     * `PRINCIPAL_1`, `PRINCIPAL_2`, `...PRINCIPAL_N`: Identifiers for the principals that you want to grant the role to.

For example, the following policy grants the `instanceOwner` role to `user1@gmail.com`, and the `instanceManager` role to users `user2@gmail.com`,`user3@gmail.com`, and service account `my-other-app@appspot.gserviceaccount.com`.
    
    {
    "policy": {
        "etag": "BwUjHYKJUiQ=",
        "bindings": [
        {
            "role": "roles/securesourcemanager.instanceOwner",
            "members": [
                "user:user1@gmail.com"
            ]
        },
        {
            "role": "roles/resourcemanager.instanceManager",
            "members": [
                "user:user2@gmail.com",
                "user:user3@gmail.com",
                "serviceAccount:my-other-app@appspot.gserviceaccount.com"
            ]
        }
        ]
    }
    }
    

  3. After you modify the allow policy to grant and revoke the chosen roles, call `instances.setIamPolicy()` to make the updates.

**Warning:** Setting a new allow policy permanently overwrites the existing allow policy on the resource. To avoid removing role bindings unintentionally, always follow the _read-modify-write_ pattern when updating an allow policy: read the existing allow policy, modify it as needed, and then write the updated version of the allow policy.

Use the following `instances.setIamPolicy` command to set the new policy on the instance.
         
         curl \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/instances/INSTANCE_ID:setIamPolicy \
             -d @/tmp/instance.json
         

Replace the following:

     * `PROJECT_ID` the project ID or project number of the instance.
     * `REGION` the region the instance is located in. See the [locations documentation](https://docs.cloud.google.com/secure-source-manager/docs/locations) for available Secure Source Manager regions.
     * `INSTANCE_ID` the instance ID.



## Grant or revoke repository roles

To grant or revoke repository roles to users and service accounts, you can assign them from the Secure Source Manager web interface, or use the Secure Source Manager API to update the repository allow policy. To grant groups repository roles, you must use the Secure Source Manager API.

Users must be granted an instance role before they can be granted repository roles. For information on granting instance roles, see [Grant or revoke instance roles](https://docs.cloud.google.com/secure-source-manager/docs/grant-iam-roles#grant-revoke-instance-roles).

### Web interface

To grant users or service accounts repository-level roles using the web interface:

  1. Navigate to the instance URL provided by your Google contact.
  2. From the **My repositories** page, Select your repository.
  3. Click the **Permissions** tab.
  4. In the **People and permissions** section, click **Add users**.
  5. In the **Add principal** field, enter the email of the user or service account you want to grant the role to.
  6. In the **Assign a role** menu, select the role to assign.
  7. Click **Save**.



To add additional roles click the edit **Edit** icon and add the roles using the **Assign a role** menu.

### API

The Secure Source Manager API [`repositories.getIamPolicy`](https://docs.cloud.google.com/secure-source-manager/docs/reference/rest/v1/projects.locations.repositories/getIamPolicy) method gets a repository's allow policy.

  1. Run the following `repositories.getIamPolicy` command to read the current policy and save it to `/tmp/repository.json`:


    
    
    curl \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        https://securesourcemanager.googleapis.com/v1/projects/REPOSITORY_PROJECT/locations/REGION/repositories/REPOSITORY_ID:getIamPolicy > /tmp/repository.json
    

Replace the following:

  * `REPOSITORY_PROJECT` the project ID or project number of the repository.
  * `REGION` the region the repository is located in.
  * `REPOSITORY_ID` the repository ID.



The output will include any existing bindings, or, if none exist, the `etag` value similar to the following:
    
    
    {
        "etag": "BwUjHYKJUiQ="
    }
    

  1. Programmatically or using a text editor, modify the local copy of your repository's allow policy saved in `/tmp/repository.json` to reflect the roles that you want to grant or revoke.

To ensure that you don't overwrite other changes, don't edit or remove the allow policy's `etag` field. The `etag` field identifies the current state of the allow policy. When you set the updated allow policy, IAM compares the `etag` value in the request with the existing `etag`, and only writes the allow policy if the values match.

**Important:** None of your changes will take effect until you set the updated allow policy.

To edit the roles that an allow policy grants, you need to edit the role bindings in the allow policy. Role bindings have the following format:
         
         {
           "role": "ROLE_NAME",
           "members": [
             "PRINCIPAL_1",
             "PRINCIPAL_2",
             ...
             "PRINCIPAL_N"
           ]
         }
         

The placeholders have the following values:

     * `ROLE_NAME`: The name of the role that you want to grant. Use the following format: `roles/securesourcemanager.<var>IDENTIFIER</var>`

     * `PRINCIPAL_1`, `PRINCIPAL_2`, `...PRINCIPAL_N`: Identifiers for the principals that you want to grant the role to.

**Important:** keep the `etag` value from the `getIamPolicy` response to ensure that you don't overwrite someone else's changes. If you want to overwrite all other changes, you can remove the `etag` value.

The following example grants the `repoAdmin` role to the user `email1@gmail.com`, and the `repoWriter` role to users `email2@gmail.com`, `group1@gmail.com`, and service account `my-other-app@appspot.gserviceaccount.com`.
    
    {
    "policy": {
        "etag": "BwUjHYKJUiQ=",
        "bindings": [
        {
            "role": "roles/securesourcemanager.repoAdmin",
            "members": [
                "user:email1@gmail.com"
            ]
        },
        {
            "role": "roles/resourcemanager.repoWriter",
            "members": [
                "user:email2@gmail.com",
                "group:group1@gmail.com",
                "serviceAccount:my-other-app@appspot.gserviceaccount.com"
            ]
        }
        ]
    }
    }
    

  2. Save the edited `/tmp/repository.json` file.

  3. Set the new policy with the `setIamPolicy` command:
         
         curl \
             -H "Content-Type: application/json" \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://securesourcemanager.googleapis.com/v1/projects/REPOSITORY_PROJECT/locations/REGION/repositories/REPOSITORY_ID:setIamPolicy \
             -d @/tmp/repository.json
         

Replace the following:

     * `REPOSITORY_PROJECT` the project ID or project number of the repository.
     * `REGION` the region the repository is located in. See the [locations documentation](https://docs.cloud.google.com/secure-source-manager/docs/locations) for available Secure Source Manager regions.
     * `REPOSITORY_ID` the repository ID.



## What's next

  * Learn more about [access control with IAM in Secure Source Manager](https://docs.cloud.google.com/secure-source-manager/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
