---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies/
title: Create and manage content policies \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:03.974680+00:00
---

# Create and manage content policies  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Create and manage content policies Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create, get, list, update, and delete content policies. For more information about content policies, see [Overview of content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy).

## Required roles

To get the permissions that you need to create and manage content policies, ask your administrator to grant you the [DLP Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.admin) (`roles/dlp.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage content policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage content policies:

  * `dlp.contentPolicies.create`
  * `dlp.contentPolicies.update`
  * `dlp.contentPolicies.list`
  * `dlp.contentPolicies.get`
  * `dlp.contentPolicies.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you plan to apply content policies to your Gemini Enterprise connectors and apps or Gemini Notebook Enterprise notebooks, then you must also grant the DLP User (`roles/dlp.user`) role to your Gemini Enterprise service account. For more information, see [Protect sensitive data in sources](https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud Data Loss Prevention API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud Data Loss Prevention API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dlp.googleapis.com)

  10. Optional: To log the content policy actions to a BigQuery table, [create the table](https://docs.cloud.google.com/bigquery/docs/tables). For information about the schema of the exported logs, see `[ContentPolicyActionLog](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog)`. 



## Create a content policy

### Console

  1. In the Google Cloud console, go to the Sensitive Data Protection **Content Policies** page.

[Go to Content Policies](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/content-policies;source=7)

  2. Select your project.

  3. Click **Create**.

  4. In **Basic Information** , do the following:

     1. Enter a name for the content policy.
     2. Optional. Enter a unique content policy ID. If you don't enter a content policy ID, Sensitive Data Protection sets one automatically.
     3. Select the region or multi-region where you want to store the content policy.
     4. Click **Continue**.
  5. In **Inspection Configuration** , do the following:

     1. Select the [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) or [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) infoTypes to detect. For more information, see [Manage infoTypes through the Google Cloud console](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-infotypes-console).

To configure detection using an existing [inspection template](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect), click **Import from a template** , and enter the template's full resource name.

     2. Optional. Add an inspection ruleset. 

#### Click to show instructions

Inspection rulesets let you customize both built-in and custom infoType detectors using context rules. The types of inspection rules are: 

        * _[Exclusion rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#exclusion-rules)_ , which help exclude false or unwanted findings.
        * _[Hotword rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#hotword_rules)_ , which help detect additional findings.
        * _[Adjustment rules](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#adjustment-rules)_ , which adjust the likelihood of findings based on the context in which they appear.

To add a new ruleset, first specify one or more built-in or custom infoType detectors in the **InfoTypes** section. Select all infoType detectors that your rulesets modify (the _target_ infoTypes) or use for assessment (the _context_ infoTypes). Then, do the following: 

        1. Click **Add a ruleset**.
        2. In the **Choose target infoTypes** field, select the infoTypes that the ruleset modifies if the rules are met.
        3. Click **Add a rule** to open a menu with options, including **Hotword rule** , **Exclusion rule** , and **Adjustment rule**.

To create a hotword rule, select **Hotword rule**. Then, do the following: 

        1. In the **Hotword** field, enter a regular expression that Sensitive Data Protection looks for.
        2. From the **Hotword proximity** menu, select whether the hotword you entered is found before or after the chosen infoType.
        3. In **Hotword distance from infoType** , enter the approximate number of characters between the hotword and the chosen infoType.
        4. In **Confidence level adjustment** , select whether to assign matches a fixed [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) level, or to increase or decrease the default likelihood level by a certain amount.

To create an exclusion rule, select **Exclusion rule** and the type of exclusion rule to create, for example, **Regular expression**. Then, do the following: 

        1. Depending on the exclusion rule type that you selected, enter the regular expression, phrase, hotword, or context infoType that must be found for the rule to apply.
        2. Depending on the exclusion rule type that you selected, set the matching type or image containment type:
           * If you selected a text-based exclusion rule, select one of the following matching types:
             * **Full match** : The finding must completely match the text or context infoType that you provided.
             * **Partial match** : A substring of the finding must match the text or context infoType that you provided.
             * **Inverse match** : The finding must not match the text or context infoType that you provided.
           * If you selected an image-based exclusion rule, select the required spatial relationship between the target and context infoTypes. For example, if you select **Encloses** , the context finding must enclose the target finding for the rule to apply.

To create an adjustment rule, select **Adjustment rule** and the type of adjustment rule, for example, **Adjust by image findings**. Then, do the following: 

        1. In the **Context infoTypes** field, select the infoType detectors that provide context for the target finding. Sensitive Data Protection uses context infoTypes to assess whether it must adjust the target infoType.
        2. In the **Minimum likelihood** field, select the lowest likelihood level that the context infoTypes can have and still trigger the adjustment rule. If the likelihood value of any detected context finding is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the target finding.
        3. For image findings, in the **Image containment type** field, select the required spatial relationship between the target and context infoTypes. For example, if you select **Encloses** , the context finding must enclose the target finding for the rule to apply.
        4. In the **Likelihood** field, select the new likelihood level to assign to the target finding.

You can add more rulesets to further refine your scan results. 

     3. Optional. Set the confidence threshold for findings to detect. For more information, see [Match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood).

     4. Click **Continue**.

  6. In **Policy Rules** , add policy rules to specify the verdict (**Allow** or **Block**) that Sensitive Data Protection returns when it detects an infoType that you specified in your inspection configuration. You can add a single policy rule to return the same verdict for any infoType, or add multiple policy rules to return different verdicts for different infoTypes. You must set a condition for each policy rule that you add.

To add a policy rule, do the following:

     1. Click **Add policy rule**.
     2. Select a verdict to assign to an infoType finding: **Allow** or **Block**.
     3. Click **Add condition**. Depending on whether you want to set different verdicts for different infoTypes, set **Condition type** to **Any infoType** or **Specific infoTypes**.
     4. If you selected **Specific infoTypes** , enter the infoTypes that must be detected for Sensitive Data Protection to return the verdict that you selected.
     5. If needed, add more policy rules and their corresponding conditions.
     6. Click **Continue**.
  7. Optional. In **Default Actions** , specify the verdicts to apply in the following conditions:

     * A verdict to assign to unsupported files. For more information, see [Supported file types and scanning modes](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).
     * A verdict to assign to supported files that are [too large to scan](https://docs.cloud.google.com/sensitive-data-protection/limits#content-policy-limits).
     * A verdict to assign to files that can't be scanned, for example, corrupted or encrypted files.
     * A verdict to assign if none of the rules match the scanned content.

For each of these conditions, the default verdict is `ALLOW`.

Click **Continue**.

  8. Optional. In **Logging Configuration** , enable logging to record verdicts issued by the content policy for the data that you scan. Do the following:

     1. Select **Log policy execution to BigQuery**.
     2. Enter the details of an existing BigQuery table where Sensitive Data Protection must log the results.
  9. Click **Create**. 




### REST

To create a content policy, send a `POST` request to the [`projects.locations.contentPolicies.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/create) method. The request body defines a `content_policy` object that contains the inspection configuration and rules that determine the verdict based on findings. 

The `content_policy` object has the following properties:
    
    
    {
      "contentPolicy": {
        "displayName": "DISPLAY_NAME",
        "inspectConfig": {
          "infoTypes": [
            {
              "name": "INFOTYPE_DETECTOR"
            }
          ],
          "ruleSet": "LIST_OF_RULES"
        },
        "rules": [
          {
            "conditions": [
              {
                "infoTypeCondition": {
                  "anyInfoType": {}
                }
              }
            ],
            "action": {
              "returnVerdict": "INFOTYPE_CONDITION_VERDICT"
            }
          }
        ],
        "unsupportedFileType": {
          "returnVerdict": "UNSUPPORTED_FILE_TYPE_VERDICT"
        },
        "inputTooLarge": {
          "returnVerdict": "INPUT_TOO_LARGE_VERDICT"
        },
        "failedToScanSupportedFileType": {
          "returnVerdict": "FAILED_TO_SCAN_VERDICT"
        },
        "defaultAction": {
          "returnVerdict": "DEFAULT_ACTION_VERDICT"
        },
        "loggingConfigs": [
          {
            "logToBigQuery": {
              "projectId": "LOG_PROJECT_ID",
              "datasetId": "LOG_DATASET_ID",
              "tableId": "LOG_TABLE_ID"
            }
          }
        ]
      },
      "contentPolicyId": "CONTENT_POLICY_ID"
    }
    

Replace the following:

  * `DISPLAY_NAME`: Optional. A human-readable name for the content policy.
  * `INFOTYPE_DETECTOR`: A [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) or [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) infoType.
  * `LIST_OF_RULES`: Optional. A list of inspection rules as defined in [Modifying infoType detectors to refine scan results](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules). This code is truncated for brevity. For an example of a ruleset definition within a content policy, see Expanded example.
  * `INFOTYPE_CONDITION_VERDICT`: A verdict to assign to a finding of an infoType: `ALLOW` or `BLOCK`.
  * `UNSUPPORTED_FILE_TYPE_VERDICT`: Optional. A verdict to assign to unsupported files: `ALLOW` or `BLOCK`. For more information, see [Supported file types and scanning modes](https://docs.cloud.google.com/sensitive-data-protection/docs/supported-file-types).
  * `INPUT_TOO_LARGE_VERDICT`: Optional. A verdict to assign to supported files that are [too large to scan](https://docs.cloud.google.com/sensitive-data-protection/limits#content-policy-limits): `ALLOW` or `BLOCK`.
  * `FAILED_TO_SCAN_VERDICT`: Optional. A verdict to assign to files that can't be scanned, for example, corrupted or encrypted files: `ALLOW` or `BLOCK`.
  * `DEFAULT_ACTION_VERDICT`: Optional. A verdict to assign if none of the rules match the scanned content: `ALLOW` or `BLOCK`.
  * `LOG_PROJECT_ID`: The ID of the project that contains the BigQuery table to write to.
  * `LOG_DATASET_ID`: The ID of the dataset that contains the BigQuery table to write to.
  * `LOG_TABLE_ID`: The ID of the BigQuery table to write to.
  * `CONTENT_POLICY_ID`: A unique ID for the content policy.



For an example response, see Expanded example. 

## Get the details of a content policy

### Console

  1. In the Google Cloud console, go to the Sensitive Data Protection **Content Policies** page.

[Go to Content Policies](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/content-policies;source=7)

  2. Select your project.

  3. Click the resource name of a content policy to view.

  4. On the **Details** tab, view details about the content policy. 




### REST

To get a content policy, send a `GET` request to the [`projects.locations.contentPolicies.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/get) method. 

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where the content policy is stored—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: the ID of the project that contains the content policy. 
  * `CONTENT_POLICY_ID`: the ID of the content policy to get details for. 



HTTP method and URL: 
    
    
    GET https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-west1/contentPolicies/block-credit-cards-policy",
      "rules": [
        {
          "conditions": [
            {
              "infoTypeCondition": {
                "anyInfoType": {}
              }
            }
          ],
          "action": {
            "returnVerdict": "BLOCK"
          }
        }
      ],
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ],
        "minLikelihood": "LIKELY",
        "limits": {}
      }
    }
    

## List all content policies in a project

### Console

  1. In the Google Cloud console, go to the Sensitive Data Protection **Content Policies** page.

[Go to Content Policies](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/content-policies;source=7)

  2. Select your project. The list of content policies in the project appears. 




### REST

To list the content policies in a project, send a `LIST` request to the [`projects.locations.contentPolicies.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/list) method.

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where the content policies that you want to list are stored—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: the ID of the project that contains the content policies to list. 



HTTP method and URL: 
    
    
    GET https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "contentPolicies": [
          {
      "name": "projects/example-project/locations/us-west1/contentPolicies/block-credit-cards-policy",
      "rules": [
        {
          "conditions": [
            {
              "infoTypeCondition": {
                "anyInfoType": {}
              }
            }
          ],
          "action": {
            "returnVerdict": "BLOCK"
          }
        }
      ],
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ],
        "minLikelihood": "LIKELY",
        "limits": {}
      }
    },
        {
          "name": "projects/example-project/locations/us-west1/contentPolicies/block-pii",
          ...
        }
      ]
    }

## Update a content policy

### Console

  1. In the Google Cloud console, go to the Sensitive Data Protection **Content Policies** page.

[Go to Content Policies](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/content-policies;source=7)

  2. Select your project.

  3. Click the resource name of a content policy to edit.

  4. Click **Edit**.

  5. Edit the details of the content policy.




### REST

To update a content policy, send a `PATCH` request to the [`projects.locations.contentPolicies.patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/patch) method. The request body defines the updated `content_policy` object. 

Before using any of the request data, make the following replacements: 

  * `REGION`: a region where a regional endpoint for Sensitive Data Protection is available—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: your Google Cloud project ID. Project IDs are alphanumeric strings, like `example-project`. 
  * `CONTENT_POLICY_ID`: the ID of the content policy to update. 



HTTP method and URL: 
    
    
    PATCH https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID

Request JSON body: 
    
    
    {
      "contentPolicy": {
        "displayName": "displayName",
        "inspectConfig": {
          "infoTypes": [
            {
              "name": "CREDIT_CARD_NUMBER"
            }
          ],
          "minLikelihood": "LIKELY"
        },
        "rules": [
          {
            "conditions": [
              {
                "infoTypeCondition": {
                  "anyInfoType": {}
                }
              }
            ],
            "action": {
              "returnVerdict": "BLOCK"
            }
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `content-policy-update-request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @content-policy-update-request.json \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `content-policy-update-request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile content-policy-update-request.json `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-west1/contentPolicies/block-credit-cards-policy",
      "rules": [
        {
          "conditions": [
            {
              "infoTypeCondition": {
                "anyInfoType": {}
              }
            }
          ],
          "action": {
            "returnVerdict": "BLOCK"
          }
        }
      ],
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ],
        "minLikelihood": "LIKELY",
        "limits": {}
      }
    }
    

## Delete a content policy

### Console

  1. In the Google Cloud console, go to the Sensitive Data Protection **Content Policies** page.

[Go to Content Policies](https://console.cloud.google.com/security/sensitive-data-protection/landing/configuration/content-policies;source=7)

  2. Select your project.

  3. Select the content policy to delete.

  4. Click **Delete**. 




### REST

To delete a content policy, send a `DELETE` request to the [`projects.locations.contentPolicies.delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/delete) method.

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where the content policy is stored—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: the ID of the project that contains the content policy. 
  * `CONTENT_POLICY_ID`: the ID of the content policy to delete. 



HTTP method and URL: 
    
    
    DELETE https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies/CONTENT_POLICY_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## REST examples

The following REST examples show how to create a content policy using the REST API.

### Simple example

The following example creates a policy that identifies `CREDIT_CARD_NUMBER` findings with a likelihood of `POSSIBLE` or higher. If a credit card number is found, Sensitive Data Protection returns a `BLOCK` verdict.

Before using any of the request data, make the following replacements: 

  * `REGION`: a region where a regional endpoint for Sensitive Data Protection is available—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: your Google Cloud project ID. Project IDs are alphanumeric strings, like `example-project`. 



HTTP method and URL: 
    
    
    POST https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies

Request JSON body: 
    
    
    {
      "contentPolicy": {
        "displayName": "displayName",
        "inspectConfig": {
          "infoTypes": [
            {
              "name": "CREDIT_CARD_NUMBER"
            }
          ],
          "minLikelihood": "POSSIBLE"
        },
        "rules": [
          {
            "conditions": [
              {
                "infoTypeCondition": {
                  "anyInfoType": {}
                }
              }
            ],
            "action": {
              "returnVerdict": "BLOCK"
            }
          }
        ]
      },
      "contentPolicyId": "block-credit-cards-policy"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `content-policy-create-request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @content-policy-create-request.json \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `content-policy-create-request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile content-policy-create-request.json `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-west1/contentPolicies/block-credit-cards-policy",
      "rules": [
        {
          "conditions": [
            {
              "infoTypeCondition": {
                "anyInfoType": {}
              }
            }
          ],
          "action": {
            "returnVerdict": "BLOCK"
          }
        }
      ],
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ],
        "minLikelihood": "POSSIBLE",
        "limits": {}
      }
    }

### Expanded example

The following example creates a policy that identifies `CREDIT_CARD_NUMBER` findings with a likelihood of `POSSIBLE` or higher. It includes a hotword rule that boosts the likelihood value of the finding to `VERY_LIKELY` if the word `credit card` is detected near the finding.

  * If Sensitive Data Protection detects a possible credit card number, it returns a `BLOCK` verdict.
  * If the file to scan is unsupported, too large, corrupted, encrypted, or otherwise unscannable, Sensitive Data Protection returns a `BLOCK` verdict.
  * If none of the rules match the scanned content, Sensitive Data Protection returns an `ALLOW` verdict.



Before using any of the request data, make the following replacements: 

  * `REGION`: a region where a regional endpoint for Sensitive Data Protection is available—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: your Google Cloud project ID. Project IDs are alphanumeric strings, like `example-project`. 



HTTP method and URL: 
    
    
    POST https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies

Request JSON body: 
    
    
    {
      "contentPolicy": {
        "displayName": "displayName",
        "inspectConfig": {
          "infoTypes": [
            {
              "name": "CREDIT_CARD_NUMBER"
            }
          ],
          "ruleSet": [
            {
              "infoTypes": [
                {
                  "name": "CREDIT_CARD_NUMBER"
                }
              ],
              "rules": [
                {
                  "hotwordRule": {
                    "hotwordRegex": {
                      "pattern": "credit\\scard"
                    },
                    "proximity": {
                      "windowBefore": 10,
                      "windowAfter": 10
                    },
                    "likelihoodAdjustment": {
                      "fixedLikelihood": "VERY_LIKELY"
                    }
                  }
                }
              ]
            }
          ]
        },
        "rules": [
          {
            "conditions": [
              {
                "infoTypeCondition": {
                  "anyInfoType": {}
                }
              }
            ],
            "action": {
              "returnVerdict": "BLOCK"
            }
          }
        ],
        "unsupportedFileType": {
          "returnVerdict": "BLOCK"
        },
        "inputTooLarge": {
          "returnVerdict": "BLOCK"
        },
        "failedToScanSupportedFileType": {
          "returnVerdict": "BLOCK"
        },
        "defaultAction": {
          "returnVerdict": "ALLOW"
        }
      },
      "contentPolicyId": "block-credit-cards-policy"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `content-policy-create-request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @content-policy-create-request.json \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `content-policy-create-request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile content-policy-create-request.json `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-west2/contentPolicies/block-credit-cards-policy",
      "rules": [
        {
          "conditions": [
            {
              "infoTypeCondition": {
                "anyInfoType": {}
              }
            }
          ],
          "action": {
            "returnVerdict": "BLOCK"
          }
        }
      ],
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ],
        "limits": {},
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "CREDIT_CARD_NUMBER"
              }
            ],
            "rules": [
              {
                "hotwordRule": {
                  "hotwordRegex": {
                    "pattern": "credit\\scard"
                  },
                  "proximity": {
                    "windowBefore": 10,
                    "windowAfter": 10
                  },
                  "likelihoodAdjustment": {
                    "fixedLikelihood": "VERY_LIKELY"
                  }
                }
              }
            ]
          }
        ]
      },
      "unsupportedFileType": {
        "returnVerdict": "BLOCK"
      },
      "inputTooLarge": {
        "returnVerdict": "BLOCK"
      },
      "failedToScanSupportedFileType": {
        "returnVerdict": "BLOCK"
      },
      "defaultAction": {
        "returnVerdict": "ALLOW"
      }
    }

### Example with metadata label scanning

The following example instructs Sensitive Data Protection to scan for credit card numbers and metadata labels that have the key `MSIP_Label_12345-12345-1234-12345_Enabled`. Sensitive Data Protection returns a `BLOCK` verdict if any is found.

For more information about metadata label scanning, see [Create a custom metadata label detector](https://docs.cloud.google.com/sensitive-data-protection/docs/create-custom-infotypes-metadata-labels).

Before using any of the request data, make the following replacements: 

  * `REGION`: a region where a regional endpoint for Sensitive Data Protection is available—for example, `us-west2`. For a full list of regions, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `PROJECT_ID`: your Google Cloud project ID. Project IDs are alphanumeric strings, like `example-project`. 



HTTP method and URL: 
    
    
    POST https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies

Request JSON body: 
    
    
    {
      "contentPolicy": {
        "displayName": "displayName",
        "inspectConfig": {
          "infoTypes": [
            {
              "name": "CREDIT_CARD_NUMBER"
            }
          ],
          "customInfoTypes": [
            {
              "infoType": {
                "name": "CUSTOM_MSIP1"
              },
              "likelihood": "VERY_LIKELY",
              "fileLabelInfoType": {
                "sensitivityLabel": {
                  "guid": "12345678-1234-1234-1234-123456789012"
                }
              }
            }
          ],
          "minLikelihood": "POSSIBLE"
        },
        "rules": [
          {
            "conditions": [
              {
                "infoTypeCondition": {
                  "anyInfoType": {}
                }
              }
            ],
            "action": {
              "returnVerdict": "BLOCK"
            }
          }
        ]
      },
      "contentPolicyId": "block-credit-cards-policy-metadata-scanning"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dlp.REGION.rep.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/contentPolicies" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-west1/contentPolicies/block-credit-cards-policy-metadata-scanning",
      "rules": [
        {
          "conditions": [
            {
              "infoTypeCondition": {
                "anyInfoType": {}
              }
            }
          ],
          "action": {
            "returnVerdict": "BLOCK"
          }
        }
      ],
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "CREDIT_CARD_NUMBER"
          }
        ],
        "minLikelihood": "POSSIBLE",
        "limits": {},
        "customInfoTypes": [
          {
            "infoType": {
              "name": "CUSTOM_MSIP1"
            },
            "likelihood": "VERY_LIKELY",
            "fileLabelInfoType": {
              "sensitivityLabel": {
                "guid": "12345678-1234-1234-1234-123456789012"
              }
            }
          }
        ]
      }
    }

## What's next

  * Learn about [content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
