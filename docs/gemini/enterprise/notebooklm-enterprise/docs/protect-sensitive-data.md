---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/protect-sensitive-data/
title: Protect sensitive data in Gemini Notebook Enterprise sources \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:14.477845+00:00
---

# Protect sensitive data in Gemini Notebook Enterprise sources  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/protect-sensitive-data/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview)



Send feedback 

#  Protect sensitive data in Gemini Notebook Enterprise sources Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to protect sensitive data in Gemini Notebook Enterprise by integrating with [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview).

## About Sensitive Data Protection in Gemini Notebook Enterprise

[Sensitive Data Protection content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/content-policy) inspect data for policy violations or unwanted content. You can configure content policies to block file uploads to Gemini Notebook Enterprise if they violate your policy. This is a responsible AI practice that protects notebooks from sensitive data exposure.

### Sensitive Data Protection and Model Armor work together

Sensitive Data Protection and Model Armor work together in Gemini Notebook Enterprise to provide a layered security defense for your notebooks. They protect different aspects of your notebook interactions.

#### Sensitive Data Protection safeguards uploaded sources

Sensitive Data Protection prevents sensitive data from being uploaded and ingested into your notebooks. Content policies can inspect content in your sources before they are added to the notebook and block sources if the contents violate the content policy.

Not all source types are supported. See Limitations.

#### Model Armor safeguards the interaction path

Model Armor screens the prompts that users submit to the notebook before processing, and screens responses before displaying them to the user. By screening prompts and responses, Model Armor guards against prompt injection, malicious URLs, and other safety risks. If a policy is violated, Gemini Notebook Enterprise blocks the interaction and displays an error message.

For more information about using Model Armor with Gemini Notebook Enterprise, see [Enable Model Armor](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/enable-model-armor).

## Limitations

The following limitations apply to Sensitive Data Protection content policies in Gemini Notebook Enterprise:

  * Sensitive Data Protection content policies don't apply to audio files or to Google Drive documents and slides.

  * Although you can apply a content policy from one project to Gemini Notebook Enterprise in another project, the two projects must be in the same VPC Service Controls perimeter. For general information about VPC Service Controls for Gemini Enterprise, see [Secure your app with VPC Service Controls](https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls).

  * Sensitive Data Protection can't scan very large files. For information about the maximum size of PDFs, Office 365 files, text files, and image files, see [Content policy limits](https://docs.cloud.google.com/sensitive-data-protection/limits#content-policy-limits). By default, content policies allow content in large files. However, you can configure policies to block content in large files.




## Before you begin

Make sure you have the required roles assigned to you and the Gemini Enterprise service account:

  * You need the [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role.

  * The Gemini Enterprise service account needs the DLP User (`roles/dlp.user`) role.




For more information, see [Required roles](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies#required-roles) in _Create and manage content policies_ in the Sensitive Data Protection documentation set.

**Note:** To grant multiple IAM roles to a service account, see [Grant or revoke multiple IAM roles using the Google Cloud console](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#multiple-roles-console).

## Create a content policy

To prepare a Sensitive Data Protection content policy to apply to Gemini Notebook Enterprise, do the following:

  1. Create a content policy following the instructions in [Create and manage content policies](https://docs.cloud.google.com/sensitive-data-protection/docs/manage-content-policies) in the Sensitive Data Protection documentation.

Make sure to create the policy in the same region as the notebooks that you want to protect.

  2. Make a note of the policy name. To add a policy to a connector, you need the full path, in the form `projects/PROJECT_ID/locations/LOCATION/contentPolicies/POLICY_ID`.




## Configure Gemini Notebook Enterprise with the data protection policy

To configure Gemini Notebook Enterprise with the data protection policy, do the following:

  1. Call the [`projects.patch`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects/patch) method to associate the content policy with a region in your project.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER?update_mask=customer_provided_config" \
         -d '{
           "customer_provided_config": {
             "notebooklm_config": {
               "data_protection_policy": {
                 "sensitive_data_protection_policy": {
                   "policy": "POLICY_ID"
                 }
               }
             }
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `LOCATION`: the location of your project: `global`, `us`, or `eu`.

     * `PROJECT_NUMBER`: the project number of your project.

     * `POLICY_ID`: the resource name of the Sensitive Data Protection content policy that you want to apply.

#### Example command and result
    
    $ curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "x-goog-user-project: my-project-123" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/123456?update_mask=customer_provided_config" \
    -d '{
      "customer_provided_config": {
        "notebooklm_config": {
          "data_protection_policy": {
            "sensitive_data_protection_policy": {
              "policy": "projects/my-project-123/locations/global/contentPolicies/12345678-abcd-1234-abcd-1234567890ab"
            }
          }
        }
      }
    }'
    {
      "name": "projects/123456",
      "createTime": "2023-08-15T21:57:03.738773660Z",
      "provisionCompletionTime": "2023-08-15T21:57:03.738773660Z",
      "serviceTermsMap": {
        "GA_DATA_USE_TERMS": {
          "id": "GA_DATA_USE_TERMS",
          "version": "2022-11-23",
          "state": "TERMS_ACCEPTED",
          "acceptTime": "2023-08-15T21:57:03.738773660Z"
        }
      },
      "customerProvidedConfig": {
        "notebooklmConfig": {
          "dataProtectionPolicy": {
            "sensitiveDataProtectionPolicy": {
              "policy": "projects/my-project-123/locations/global/contentPolicies/12345678-abcd-1234-abcd-1234567890ab"
            }
          }
        }
      }
    }
    

  2. Wait for the configuration to propagate. It typically takes about 10 minutes for the policy to take effect.

  3. Optional: Test the content policy:

     1. Create a source document that contains a harmless violation of the policy. For example, if the content policy blocks US social security numbers, create a source file that says "Mickey Mouse's social security number is 999-00-0000".

     2. Upload the source document to a notebook. If the policy is in effect, the document appears as blocked in the source list.

![Unable to import this source. It violates policies](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/blocked-notebook-source.png)




## Remove the data protection policy

To remove the data protection policy from Gemini Notebook Enterprise, do the following:

  1. Call the `projects.patch` method with an empty `data_protection_policy` object.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER?update_mask=customer_provided_config" \
         -d '{
           "customer_provided_config": {
             "notebooklm_config": {
               "data_protection_policy": {}
             }
           }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.

     * `LOCATION`: the location of your project: `global`, `us`, or `eu`.

     * `PROJECT_NUMBER`: the project number of your project.

#### Example command and result
    
    $ curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "x-goog-user-project: my-project-123" \
    "https://global-discoveryengine.googleapis.com/v1alpha/projects/123456?update_mask=customer_provided_config" \
    -d '{
      "customer_provided_config": {
        "notebooklm_config": {
          "data_protection_policy": {}
        }
      }
    }'
    {
      "name": "projects/123456",
      "createTime": "2023-08-15T21:57:03.738773660Z",
      "provisionCompletionTime": "2023-08-15T21:57:03.738773660Z",
      "serviceTermsMap": {
        "GA_DATA_USE_TERMS": {
          "id": "GA_DATA_USE_TERMS",
          "version": "2022-11-23",
          "state": "TERMS_ACCEPTED",
          "acceptTime": "2023-08-15T21:57:03.738773660Z"
        }
      },
      "customerProvidedConfig": {
        "notebooklmConfig": {
          "dataProtectionPolicy": {}
        }
      }
    }
    

  2. Wait for the configuration to propagate. It typically takes about 10 minutes for the policy to be removed.

  3. Optional: Test to see if the content policy has been removed:

     1. Create a source document that contains a harmless violation of the policy.

     2. Upload the source document to a notebook. If the document is added to the source list and not blocked, then the policy has been removed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
