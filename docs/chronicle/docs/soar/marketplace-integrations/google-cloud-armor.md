---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-armor/
title: Integrate Cloud Armor with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:13.577038+00:00
---

# Integrate Cloud Armor with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-cloud-armor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Cloud Armor with Google SecOps

This document explains how to integrate Google Cloud Armor with Google Security Operations.

## Use cases

The **Cloud Armor** integration supports the following use cases:

  * **Automated threat blocking** : Instantly block malicious IP addresses or ranges at the Google Cloud edge by updating security policy rules during an incident.

  * **Security policy management** : List, retrieve, and update security policies and rules across your environment to ensure consistent WAF protection.

  * **Dynamic DDoS mitigation** : Respond to volumetric or protocol-based attacks by programmatically adjusting security policy settings.

  * **Forensic auditing** : Retrieve configuration details of existing security policies to correlate edge protections with internal security alerts.




## Before you begin

Before you configure the **Cloud Armor** integration in Google SecOps, complete the following prerequisite steps:

  1. Create and configure a custom Identity and Access Management role.

  2. Create a service account.

  3. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived tokens by using service account impersonation.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file.




### Create and configure the IAM role

To provide the integration with the necessary permissions, create a custom role in your Google Cloud project:

  1. In the Google Cloud console, go to **Roles**.

[Go to Roles](https://console.cloud.google.com/iam-admin/roles)

  2. Click **add Create custom role**.

  3. Provide a **Title** , **Description** , and a unique **ID**.

  4. Set the **Role Launch Stage** to **General Availability**.

  5. Add the following permissions to the role:

     * `compute.backendBuckets.setSecurityPolicy`
     * `compute.backendServices.setSecurityPolicy`
     * `compute.regionBackendServices.setSecurityPolicy`
     * `compute.regionSecurityPolicies.create`
     * `compute.regionSecurityPolicies.get`
     * `compute.regionSecurityPolicies.list`
     * `compute.regionSecurityPolicies.update`
     * `compute.securityPolicies.create`
     * `compute.securityPolicies.get`
     * `compute.securityPolicies.list`
     * `compute.securityPolicies.update`
  6. Click **Create**.




### Create a service account

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name and description and click **Create and continue**.

  4. In the **Grant this service account access to project** step, assign the custom IAM role you created.

  5. Click **Done**. Note the service account's **Email address**.




### Configure Workload Identity credentials

Workload Identity is the recommended approach because it uses short-lived tokens by using service account impersonation.

#### Identify the unique instance identity

Establishing a connection requires granting your Google SecOps instance permission to impersonate your service account.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Cloud Armor** integration and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test fails.

  4. Click the close_small button next to **Test** and locate the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




### Configure a JSON key

Static, long-lived secret key files require manual rotation. Use this method only if Workload Identity authentication isn't available.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select your service account.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab and click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The key file downloads to your computer.




## Integration parameters

The **Cloud Armor** integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API root of the Cloud Armor service. The default value is `https://compute.googleapis.com/compute/v1/`.  
`Project ID` | Optional. The project ID to target for Cloud Armor. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Workload Identity Email` | Optional. The client email address of your service account. Configure this parameter for Workload Identity authentication. If configured, `User Service Account` is ignored.  
`User Service Account` | Optional. The full content of the service account key JSON file. Configure this parameter for service account key authentication. If configured, the integration ignores `Workload Identity Email`.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Google Cloud server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add a Rule to a Security Policy

Add a new rule to the security policy in the Cloud Armor service. 

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters  
---  
`Policy Name` | _Required_ Security policy name to add a new rule to.  
`Region` | _Optional_ Region for the policy to add the rule in.If no value is provided, the rule is added to the global-level security policy.   
`Rule JSON` | _Required_ JSON definition of the rule to add.For more information about adding a rule to a policy, see [Method: securityPolicies.addRule](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/addRule).  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | Available  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result
    
    
    {
       "kind": "compute#securityPolicy",
       "id": "ID",
       "creationTimestamp": "2024-04-14T05:39:05.798-07:00",
       "name": "example",
       "description": "Test for integration",
       "rules": [
           {
               "kind": "compute#securityPolicyRule",
               "description": "test",
               "priority": 100,
               "match": {
                   "versionedExpr": "SRC_IPS_V1",
                   "config": {
                       "srcIpRanges": [
                           "*"
                       ]
                   }
               },
               "action": "allow",
               "preview": false
           },
           {
               "kind": "compute#securityPolicyRule",
               "description": "Default rule, higher priority overrides it",
               "priority": 2147483647,
               "match": {
                   "versionedExpr": "SRC_IPS_V1",
                   "config": {
                       "srcIpRanges": [
                           "*"
                       ]
                   }
               },
               "action": "allow",
               "preview": false
           }
       ],
       "fingerprint": "A3hq2ZQYxj8=",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/northamerica-northeast1/securityPolicies/example",
       "type": "CLOUD_ARMOR",
       "labelFingerprint": "42WmSpB8rSM=",
       "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/northamerica-northeast1"
    }
    

##### Case wall

This action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added a new rule to the security policy!` | Action succeeded.  
`Error executing action "Add a Rule to a Security Policy". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, credentials, region name, the content of the JSON file, or a policy name.  
  
### Create a Security Policy

Create a security policy in the Cloud Armor service.

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters  
---  
`Region` | _Optional_ The region to create a policy in.If no value is provided, the global-level security policy is created.  
`Policy JSON` | _Required_ The JSON definition of the policy to create. For more information about policies, see [REST Resource: securityPolicies](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies).  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | Available  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result
    
    
    {
       "kind": "compute#securityPolicy",
       "id": "ID",
       "creationTimestamp": "2024-04-14T05:39:05.798-07:00",
       "name": "example",
       "description": "Test for integration",
       "rules": [
           {
               "kind": "compute#securityPolicyRule",
               "description": "test",
               "priority": 100,
               "match": {
                   "versionedExpr": "SRC_IPS_V1",
                   "config": {
                       "srcIpRanges": [
                           "*"
                       ]
                   }
               },
               "action": "allow",
               "preview": false
           },
           {
               "kind": "compute#securityPolicyRule",
               "description": "Default rule, higher priority overrides it",
               "priority": 2147483647,
               "match": {
                   "versionedExpr": "SRC_IPS_V1",
                   "config": {
                       "srcIpRanges": [
                           "*"
                       ]
                   }
               },
               "action": "allow",
               "preview": false
           }
       ],
       "fingerprint": "A3hq2ZQYxj8=",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/northamerica-northeast1/securityPolicies/example",
       "type": "CLOUD_ARMOR",
       "labelFingerprint": "42WmSpB8rSM=",
       "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/northamerica-northeast1"
    }
    

##### Case wall

This action provides the following output messages:

Output message | Message description  
---|---  
`Successfully created a new security policy!` | Action succeeded.  
`Error executing action "Create a Security Policy". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, credentials, region name, or the content of a JSON file.   
  
### Ping

Test connectivity to the Cloud Armor service with parameters provided at the integration configuration page.

#### Entities

This action doesn't run on entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True or False  
  
##### Case wall

This action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Cloud Armor service with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the Google Cloud Armor service! Error is ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
### Update a Security Policy

Update the existing security policy in the Cloud Armor service.

This action cannot update rules in a policy. To add a rule to the related policy, use the Add a Rule to a Security Policy action.

#### Entities

This action doesn't run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters  
---  
`Policy Name` | _Required_ Security policy name to add a new rule to.  
`Region` | _Optional_ Region for the updated policy.If no value is provided, the global-level security policy is created.  
`Rule JSON` | _Required_ JSON definition of the policy to update.For more information about the policy updates, see [Method: securityPolicies.patch ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/securityPolicies/patch).You cannot update rules with this action. To add a rule to a policy, use the Add a Rule to a Security Policy action.  
  
#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | Available  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True or False  
  
##### JSON result
    
    
    {
       "kind": "compute#securityPolicy",
       "id": "ID",
       "creationTimestamp": "2024-04-14T05:39:05.798-07:00",
       "name": "example",
       "description": "Test for integration",
       "rules": [
           {
               "kind": "compute#securityPolicyRule",
               "description": "test",
               "priority": 100,
               "match": {
                   "versionedExpr": "SRC_IPS_V1",
                   "config": {
                       "srcIpRanges": [
                           "*"
                       ]
                   }
               },
               "action": "allow",
               "preview": false
           },
           {
               "kind": "compute#securityPolicyRule",
               "description": "Default rule, higher priority overrides it",
               "priority": 2147483647,
               "match": {
                   "versionedExpr": "SRC_IPS_V1",
                   "config": {
                       "srcIpRanges": [
                           "*"
                       ]
                   }
               },
               "action": "allow",
               "preview": false
           }
       ],
       "fingerprint": "A3hq2ZQYxj8=",
       "selfLink": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/northamerica-northeast1/securityPolicies/example",
       "type": "CLOUD_ARMOR",
       "labelFingerprint": "42WmSpB8rSM=",
       "region": "https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/regions/northamerica-northeast1"
    }
    

##### Case wall

This action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to the identity protection detection with ID  DETECTION_ID in CrowdStrike` | Action succeeded.  
`Error executing action "Update a Security Policy". Reason: ERROR_REASON` | Action failed.Check the connection to the server, input parameters, or credentials.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
