---
url: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/set-default-policy/
title: Set default Key Access Justifications policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:57.626211+00:00
---

# Set default Key Access Justifications policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/set-default-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management)
  * [ Key Access Justifications ](https://docs.cloud.google.com/assured-workloads/key-access-justifications)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set default Key Access Justifications policy

This page shows you how to configure default Key Access Justifications policies for Assured Workloads. You can set a default Key Access Justifications policy for an organization, folder, or project. The default Key Access Justifications policy is automatically applied to new keys created within that resource, unless a Key Access Justifications policy is set on the key when it is created. Default Key Access Justifications policies are not applied to existing keys.

## Before you begin

  * You can only set default Key Access Justifications policies for Cloud KMS keys in folders enrolled in the Japan Regions control package in Assured Workloads.



### Required IAM permissions

To get the permissions that you need to create and manage default Key Access Justifications policies, ask your administrator to grant you the [Key Access Justifications Policy Config Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.keyAccessJustificationsPolicyConfigAdmin) (`roles/cloudkms.keyAccessJustificationsPolicyConfigAdmin`) IAM role on the organization, folder, or project that contains the key. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage default Key Access Justifications policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage default Key Access Justifications policies:

  * `cloudkms.keyAccessJustificationsConfig.getKeyAccessJustificationsPolicyConfig`
  * `cloudkms.keyAccessJustificationsConfig.updateKeyAccessJustificationsPolicyConfig`
  * `cloudkms.keyAccessJustificationsConfig.showEffectiveKeyAccessJustificationsPolicyConfig`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set or change a default Key Access Justifications policy

###  Console 

  1. In the Google Cloud console, go to the **Key management** page.

[ Go to Key management](https://console.cloud.google.com/security/kms)

  2. Click **KMS Controls** and then click **Key Access Justifications (KAJ)**.

  3. Click **Edit**.

  4. Select **Set Key Access Justifications policy** , and then select **Allow specific reason codes**.

**Warning:** If you select **Deny all reason codes** , the key will be unusable.
  5. For **Justification reasons** , select **Customer-initiated access** , **Google-initiated system operation** , and any other reason codes that you want to allow. Both **Customer-initiated access** and **Google-initiated system operation** are essential for normal functioning.

  6. Click **Create**.




###  gcloud 

#### Set default policy on an organization

Create or update a default Key Access Justifications policy on a folder using the `kms kaj-config update` command with the `--organization` flag:
    
    
    gcloud beta kms kaj-config update
        --organization=ORGANIZATION_NUMBER
        --allowed-access-reasons="ALLOWED_ACCESS_REASONS"
    

Replace the following:

  * `ORGANIZATION_NUMBER`: the number of the organization for which you want to set the default Key Access Justifications policy.
  * `ALLOWED_ACCESS_REASONS`: the Key Access Justifications policy listing allowed access reasons, formatted as a comma-separated list—for example, `CUSTOMER_INITIATED_ACCESS,GOOGLE_INITIATED_SYSTEM_OPERATION`. For a list of possible justification reasons, see [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).



#### Set default policy on a folder

Create or update a default Key Access Justifications policy on a folder using the `kms kaj-config update` command with the `--folder` flag:
    
    
    gcloud beta kms kaj-config update
        --folder=FOLDER_ID
        --allowed-access-reasons="ALLOWED_ACCESS_REASONS"
    

Replace the following:

  * `FOLDER_ID`: the ID of the folder that you want to set the default Key Access Justifications policy for.
  * `ALLOWED_ACCESS_REASONS`: the Key Access Justifications policy listing allowed access reasons, formatted as a comma-separated list—for example, `CUSTOMER_INITIATED_ACCESS,GOOGLE_INITIATED_SYSTEM_OPERATION`. For a list of possible justification reasons, see [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).



#### Set default policy on a project

Create or update a default Key Access Justifications policy on a project using the `kms kaj-config update` command with the `--project` flag:
    
    
    gcloud beta kms kaj-config update
        --project=PROJECT_ID
        --allowed-access-reasons="ALLOWED_ACCESS_REASONS"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to set the default Key Access Justifications policy.
  * `ALLOWED_ACCESS_REASONS`: the Key Access Justifications policy listing allowed access reasons, formatted as a comma-separated list—for example, `CUSTOMER_INITIATED_ACCESS,GOOGLE_INITIATED_SYSTEM_OPERATION`. For a list of possible justification reasons, see [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).



###  REST 

#### Set default policy on an organization

Create or update a default Key Access Justifications policy on an organization using the [`organizations.updateKeyAccessJustificationsPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/organizations/updateKajPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/organizations/ORGANIZATION_ID/kajPolicyConfig?updateMask=defaultKeyAccessJustificationPolicy" \
      --request "PATCH" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data '{"name": "organizations/ORGANIZATION_ID/kajPolicyConfig", "defaultKeyAccessJustificationPolicy": POLICY}'
    

Replace the following:

  * `ORGANIZATION_ID`: the ID of the organization for which you want to set the default Key Access Justifications policy.
  * `POLICY`: the Key Access Justifications policy listing allowed `allowedAccessReasons`, formatted as a JSON object—for example, `{"allowedAccessReasons": ["CUSTOMER_INITIATED_ACCESS", "GOOGLE_INITIATED_SYSTEM_OPERATION"]}`. For a list of possible justification reasons, see [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).



#### Set default policy on a folder

Create or update a default Key Access Justifications policy on a folder using the [`folders.updateKeyAccessJustificationsPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/folders/updateKajPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/folders/FOLDER_ID/kajPolicyConfig?updateMask=defaultKeyAccessJustificationPolicy" \
      --request "PATCH" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data '{"name": "folders/FOLDER_ID/kajPolicyConfig", "defaultKeyAccessJustificationPolicy": POLICY}'
    

Replace the following:

  * `FOLDER_ID`: the ID of the folder for which you want to set the default Key Access Justifications policy.
  * `POLICY`: the Key Access Justifications policy listing allowed `allowedAccessReasons`, formatted as a JSON object—for example, `{"allowedAccessReasons": ["CUSTOMER_INITIATED_ACCESS", "GOOGLE_INITIATED_SYSTEM_OPERATION"]}`. For a list of possible justification reasons, see [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).



#### Set default policy on a project

Create or update a default Key Access Justifications policy on a project using the [`projects.updateKeyAccessJustificationsPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects/updateKajPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/kajPolicyConfig?updateMask=defaultKeyAccessJustificationPolicy" \
      --request "PATCH" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data '{"name": "projects/PROJECT_ID/kajPolicyConfig", "defaultKeyAccessJustificationPolicy": POLICY}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project for which you want to set the default Key Access Justifications policy.
  * `POLICY`: the Key Access Justifications policy listing allowed `allowedAccessReasons`, formatted as a JSON object—for example, `{"allowedAccessReasons": ["CUSTOMER_INITIATED_ACCESS", "GOOGLE_INITIATED_SYSTEM_OPERATION"]}`. For a list of possible justification reasons, see [justification codes](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes).



## View a default Key Access Justifications policy

###  Console 

  1. In the Google Cloud console, go to the **Key management** page.

[ Go to Key management](https://console.cloud.google.com/security/kms)

  2. Click **KMS Controls** and then click **Key Access Justifications (KAJ)**. The default policy for the selected organization, folder, or project is displayed.




###  gcloud 

#### View the default policy on an organization

To view the default policy set on an organization, run the `kms kaj-config describe` command with the `--organization` flag:
    
    
    gcloud beta kms kaj-config describe --organization=ORGANIZATION_NUMBER
    

Replace `ORGANIZATION_NUMBER` with the number of the organization.

The response is similar to the following:
    
    
    defaultKeyAccessJustificationPolicy:
      defaultPolicyAvailable: true
      allowedAccessReasons:
      - CUSTOMER_INITIATED_ACCESS
      - GOOGLE_INITIATED_SYSTEM_OPERATION
    name: organizations/ORGANIZATION_NUMBER/kajPolicyConfig
    

#### View the default policy on a folder

To view the default policy set on a folder, run the `kms kaj-config describe` command with the `--folder` flag:
    
    
    gcloud beta kms kaj-config describe --folder=FOLDER_ID
    

Replace `FOLDER_ID` with the ID of the folder.

The response is similar to the following:
    
    
    defaultKeyAccessJustificationPolicy:
      defaultPolicyAvailable: true
      allowedAccessReasons:
      - CUSTOMER_INITIATED_ACCESS
      - GOOGLE_INITIATED_SYSTEM_OPERATION
    name: folders/FOLDER_ID/kajPolicyConfig
    

#### View the default policy on a project

To view the default policy set on a project, run the `kms kaj-config describe` command with the `--project` flag:
    
    
    gcloud beta kms kaj-config describe --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project.

The response is similar to the following:
    
    
    defaultKeyAccessJustificationPolicy:
      defaultPolicyAvailable: true
      allowedAccessReasons:
      - CUSTOMER_INITIATED_ACCESS
      - GOOGLE_INITIATED_SYSTEM_OPERATION
    name: projects/PROJECT_ID/kajPolicyConfig
    

This command returns the default policy set on the project if one exists. If no default policy is set on the project, this command returns no policy, even if the project inherits a default policy from a parent folder or organization. To view the effective default policy on a project, see View the effective default Key Access Justifications policy on a project on this page.

###  REST 

Get metadata about the existing default Key Access Justifications policy on an organization using the [`organizations.getKajPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/organizations/getKajPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/organizations/ORGANIZATION_ID/kajPolicyConfig"
    

Replace `ORGANIZATION_ID` with the ID of the organization for which you want to get the default Key Access Justifications policy.

The response is similar to the following:
    
    
    {
      "name" : "organizations/ORGANIZATION_ID/kajPolicyConfig"
      "defaultKeyAccessJustificationPolicy": {
        "defaultPolicyAvailable": true,
        "allowedAccessReasons": [
          "CUSTOMER_INITIATED_ACCESS",
          "GOOGLE_INITIATED_SYSTEM_OPERATION"
        ]
      }
    }
    

Get metadata about the existing default Key Access Justifications policy on a folder using the [`folders.getKajPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/folders/getKajPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/folders/FOLDER_ID/kajPolicyConfig"
    

Replace `FOLDER_ID` with the ID of the folder for which you want to get the default Key Access Justifications policy.

The response is similar to the following:
    
    
    {
      "name" : "folders/FOLDER_ID/kajPolicyConfig"
      "defaultKeyAccessJustificationPolicy": {
        "defaultPolicyAvailable": true,
        "allowedAccessReasons": [
          "CUSTOMER_INITIATED_ACCESS",
          "GOOGLE_INITIATED_SYSTEM_OPERATION"
        ]
      }
    }
    

Get metadata about the existing default Key Access Justifications policy on a project using the [`projects.getKajPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects/getKajPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/kajPolicyConfig"
    

Replace `PROJECT_ID` with the ID of the project for which you want to get the default Key Access Justifications policy.

The response is similar to the following:
    
    
    {
      "name" : "project/PROJECT_ID/kajPolicyConfig"
      "defaultKeyAccessJustificationPolicy": {
        "defaultPolicyAvailable": true,
        "allowedAccessReasons": [
          "CUSTOMER_INITIATED_ACCESS",
          "GOOGLE_INITIATED_SYSTEM_OPERATION"
        ]
      }
    }
    

## View the effective default Key Access Justifications policy on a project

Projects inherit the default policy from their nearest parent folder or organization. If there are multiple default policies set on ancestors of a single project, you can get the effective policy for the project to see the policy that is applied to new Cloud KMS keys created in that project.

In the Google Cloud console, the effective default Key Access Justifications policy on a project is displayed while you are creating a key in the project. During key creation, you choose whether to inherit the effective default policy or to [create a new key and policy](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-kaj#create).

###  gcloud 

To view metadata about the effective default Key Access Justifications policy on a project, call the [`projects.showEffectiveKeyAccessJustificationsPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects/showEffectiveKeyAccessJustificationsPolicyConfig) method:
    
    
    gcloud beta kms kaj-config show-effective-config --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project for which you want to get the effective default Key Access Justifications policy.

The response is similar to the following:
    
    
    effectiveKajPolicy:
      defaultKeyAccessJustificationPolicy:
        defaultPolicyAvailable: true
        allowedAccessReasons:
        - CUSTOMER_INITIATED_ACCESS
        - GOOGLE_INITIATED_SYSTEM_OPERATION
      name: folders/FOLDER_ID/kajPolicyConfig
    

###  REST 

To view metadata about the effective default Key Access Justifications policy on a project, call the [`projects.showEffectiveKeyAccessJustificationsPolicyConfig`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects/showEffectiveKeyAccessJustificationsPolicyConfig) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID:showEffectiveKeyAccessJustificationsPolicyConfig"
    

Replace `PROJECT_ID` with the ID of the project for which you want to get the effective default Key Access Justifications policy.

The response is similar to the following:
    
    
    {
      "effectiveKajPolicy" : {
        "name" : "folders/FOLDER_ID/kajPolicyConfig"
        "defaultKeyAccessJustificationPolicy": {
          "defaultPolicyAvailable": true,
          "allowedAccessReasons": [
            "CUSTOMER_INITIATED_ACCESS",
            "GOOGLE_INITIATED_SYSTEM_OPERATION"
          ]
        }
      }
    }
    

## What's next

  * You can also [set Key Access Justifications policy on individual keys](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/configure-kaj). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
