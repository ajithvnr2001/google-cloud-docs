---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/configure-console-and-apis-risk-policy/
title: Configure user activity conditions in a Console and APIs Access Policy \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:09.286080+00:00
---

# Configure user activity conditions in a Console and APIs Access Policy  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/configure-console-and-apis-risk-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)



Send feedback 

#  Configure user activity conditions in a Console and APIs Access Policy Stay organized with collections  Save and categorize content based on your preferences. 

**Private Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to configure user activity conditions in a Console and APIs Access Policy. User activity conditions are powered by over 60 security risk indicators from [Security Command Center Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules), many of which can be triggered by specific user actions.

You can strengthen your organization's security posture and achieve dynamic risk-based access control by adding user activity based risk conditions to your Console and APIs Access Policy.

These conditions can help you proactively address identity-based attacks at scale and mitigate risks by triggering reauthentication prompts for users when the defined risk threshold is exceeded. For example, if someone tries to access your systems from a known dangerous IP address, signs in from a place they don't usually sign in from, or exhibits behavior that suggests an attempt to bypass security measures, they'll be asked to reauthenticate.

For more information about how adding user activity conditions to your access policy enhances your security posture, see [Identity Threat Detection and Response (ITDR) with Context-Aware Access](https://docs.cloud.google.com/access-context-manager/docs/identity-threat-detection-response).

## Before you begin

As you set up this feature, keep the following in mind:

  * User activity conditions are a premium feature and requires a [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/service-tiers) Premium or Enterprise license.

  * The user activity conditions feature is only available for Google identity user accounts within a specified group. Single Sign-On (SSO) users and service accounts are not supported for this feature. 

  * You cannot use user activity conditions with Workforce Identity Federation.

  * Throughout this document, an app refers to either the Google Cloud console or a custom app, such as a Tableau app, which you can use to get data from a Cloud Storage bucket, or BigQuery.




## Configure user activity conditions in your access policy

You can configure an access policy in the following ways:

  * Create a new access policy and access level.
  * Create or update an access level, and then add that access level to a policy.

**Important:** You can't add user activity conditions to custom access levels.

### Create a new access policy and access level with user activity conditions

Complete the following steps to create an access level and a Console & APIs Access Policy.

###  Console 

  1. In the Google Cloud console, open the **Console & APIs Access Policy** page.

[Go to **Console & APIs Access Policy**](https://console.cloud.google.com/security/caa/policy)

  2. From the **Select an organization** drop-down list, select your organization, and then click **Select**.

  3. Click **Add access policy**.

  4. In the **Create access policy** dialog, select a group that you want to restrict access for. 

  5. In **Select applications that access Google Cloud** , select the apps that you want to restrict access for. Access conditions will apply to the applications you select. If you don't select any applications, the conditions will restrict access to all applications, except for user activity conditions. User activity conditions apply only to the Google Cloud console.

  6. In **Access level** , you can select an existing dry run access level or active access level or create a new access level.

     1. To create an access level, click **Create new access level**.

     2. In the **Access level title** field, enter a title for the access level. The title must be at most 50 characters, start with a letter, and can contain only numbers, letters, underscores, and spaces.

     3. [Specify the conditions](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#console) under which principals can access the console and APIs.

     4. For **User Activity** , the **Recommended settings** include all of the following risk types. Deselect any of the risk types that you don't want to include when determining access. 

        * **Suspicious actions** : Potentially malicious actions, such as removing or reducing security restrictions.
        * **Identity reputation** : Changes to account settings or state, such as changing group memberships or becoming active (non-dormant).
        * **Malicious source** : Activity from a suspicious source, such as an IP address associated with bad actors.
        * **Repeat actions** : Excessive failed access attempts, such as Identity and Access Management (IAM) denials.
        * **Atypical location** : Access from unusual locations, such as from a new geographic area.

The **Risk response** , **Require reauthentication** setting indicates that when the Google-determined risk threshold is exceeded for the user based on user activity conditions that you set earlier, users are required to reauthenticate.

     5. If you created more than one condition, use **Combine condition with** to specify whether you want the access level to require a request to meet at least one of the conditions (**OR**), or all of the conditions (**AND**).

     6. Click **Save**.

  7. In the **Create access policy** page, select from the following.

     * **Dry run** : To test your changes before enforcing the policy. We recommend that you start with a dry run, use the policy results to make any changes, and then enforce the policy.
     * **Enforce** : To start enforcing the policy.
     * **Cancel** : To cancel the policy.



###  gcloud 

  1. Create the `custom-level-spec.yaml` YAML file.
         
         expression: "noRiskSignals(userRisk, [RiskType.IDENTITY_REPUTATION, RiskType.MALICIOUS_SOURCE])"
         
         

  2. Run the following command.
         
         gcloud access-context-manager levels create risk_based_access_level\
           --title=TITLE \
           --custom-level-spec=YAML_FILE \
           --description="A risk-based access level" \
           --policy=POLICY_NAME
         

Replace the following:

     * `TITLE`: A descriptive title for your access level.
     * `YAML_FILE`: Your custom access level specification YAML file, such as `custom-level-spec.yaml`.
     * `POLICY_NAME`: The name of your Access Context Manager policy.
  3. Bind the access level to a policy.




### Create or update an access level and add it to a policy

To include user activity conditions in your policy, create a new access level or update an existing one, and then add that access level to a policy.

###  Console 

  1. To add user activity conditions when creating or updating an access level, complete the steps in the following documentation and specify **User Activity**:

     * [Create a basic access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level)
     * [Update an existing access level](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels#update_an_access_level)
  2. To add an access level with user activities to an existing policy, [update the access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#update) and add the access level.




###  gcloud 

  1. Create an access level with user activity conditions:
         
         gcloud access-context-manager levels create risk_based_access_level \
           --title=TITLE \
           --custom-level-spec=risk_level.yaml \
           --description="A risk-based access level" \
           --policy=POLICY_NAME
         

Replace the following:

     * `TITLE`: A descriptive title for your access level, such as `NoAtypicalLocationRisk`.
     * `risk_level.yaml`: The path to the YAML file that you created in the previous step.
     * `POLICY_NAME`: The name of your Access Context Manager policy to add the access level to.

Example `risk_level.yaml` YAML file:
    
    expression: "noRiskSignals(userRisk, [RiskType.ATYPICAL_LOCATION, RiskType.BAD_NETWORK_SIGNALS])"
    

This expression specifies that the access level is granted if the user's risk doesn't include atypical location or bad network signals.

  2. Bind the access level to a scope and a group:
         
         gcloud access-context-manager cloud-bindings create \
         --group-key=GROUP_KEY \
         --organization=ORGANIZATION_ID \
         --binding-file=BINDING_YAML
         

Replace the following:

     * GROUP_KEY: The email address or ID of your Google Group.
     * ORGANIZATION_ID: Your organization's ID.
     * BINDING_YAML: Your YAML configuration file.

Example YAML file:
    
    scopedAccessSettings:
     - scope:
         clientScope:
           restrictedClientApplication:
             name: Cloud Console
       activeSettings:
         accessLevels:
         - accessPolicies/123/accessLevels/access_level_1
       dryRunSettings:
         accessLevels:
         - accessPolicies/123/accessLevels/dry_run_access_level_1
    




### Add an access level with user activity conditions to an access policy

To add a risk-based access level to an existing policy, you can [update the access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#update) and add the access level.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
