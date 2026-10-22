---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/web-risk/
title: Integrate Web Risk with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:38:55.093132+00:00
---

# Integrate Web Risk with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/web-risk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Web Risk with Google SecOps

This document explains how to integrate Web Risk with Google Security Operations.

## Use cases

The **Web Risk** integration uses Google SecOps capabilities to support the following use cases:

  * **URL reputation lookups** : Check URLs against Google's lists of known malicious resources to identify phishing, malware, and unwanted software.

  * **Incident enrichment** : Automatically enrich security alerts with threat intelligence from Web Risk to help analysts prioritize and respond to threats.

  * **Malicious URL mitigation** : Incorporate Web Risk checks into playbooks to automatically block or flag high-risk domains identified during investigations.

  * **Automate phishing response** : Verify suspicious links extracted from user-reported emails to confirm phishing attempts and trigger automated containment actions like user notification or credential resets.

  * **Validate external intelligence** : Cross-reference URLs from third-party threat feeds with Google's high-fidelity lists to reduce false positives and confirm malicious intent before taking destructive actions.




## Before you begin

Before you configure the **Web Risk** integration in Google SecOps, complete the following prerequisites:

  1. Create a service account.

  2. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens through service account impersonation, so you don't need to store secrets.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity authentication isn't available in your environment.




### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account** and provide a name and description.

  3. Click **Done** to finish creating the account. The email address of this service account is used during the authentication configuration process.




### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Workload Identity is the recommended and more secure approach because it uses short-lived, temporary access tokens using service account impersonation, eliminating the need to store or rotate long-lived secrets.

#### Identify the unique instance identity

To authenticate using a Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This lets the instance securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Web Risk** integration, and enter your service account email in **Workload Identity Email**.

  3. Enter a valid project ID in **Quota Project ID**.

  4. Click **Save > Test**. The test is expected to fail. 

  5. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  6. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

After you retrieve the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step enables service account impersonation, which lets the platform generate short-lived tokens and act on your behalf without the need for static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




#### Grant quota project access

When authenticating using a Workload Identity, you must specify a `Quota Project ID` in the integration settings to track API usage and billing. 

To authorize this, you must grant your service account the following role on the designated quota project:

  1. In the Google Cloud console, go to **IAM & Admin > IAM** and select your project.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Locate your service account in the list of principals and click **edit(Edit principal)** for that account.

  3. Click **Add another role** and select the **Service Usage Consumer** role (`roles/serviceusage.serviceUsageConsumer`).

  4. Click **Save**.




### Configure a JSON key

Choose this method or the Workload Identity method to authenticate the integration. Use the JSON key method only if Workload Identity isn't available in your environment. Workload Identity is the recommended and more secure approach. This method relies on a static, long-lived secret key file that requires manual management and rotation.

Use the following procedure to generate the JSON key file required to authenticate the integration:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key > Create new key**.

  4. Select **JSON** as the key type and click **Create**. The browser downloads the JSON file to your computer.

  5. Copy the entire content of this file and paste it into `Service Account JSON File Content` during integration configuration.




## Integration parameters

The **Web Risk** integration requires the following parameters:

Parameter | Description  
---|---  
`Workload Identity Email` | Optional. The client email address of your service account. Only configure this parameter if you're authenticating using a Workload Identity. If you configure this parameter, you must also configure `Quota Project ID`.  
`Service Account JSON File Content` | Optional. The full content of the service account JSON key file. Only configure this parameter if you're authenticating using a JSON key.  
`Quota Project ID` | Optional. The Google Cloud project ID used for API usage and billing purposes. This parameter is mandatory if you're authenticating using a Workload Identity.  
`Project ID` | Optional. The Google Cloud project ID to use in the integration. If no value is provided, the integration retrieves the ID from the service account credentials.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Web Risk server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enrich Entities

Use the **Enrich Entities** action to return information about Google SecOps entities from Web Risk.

This action runs on the Google SecOps `URL` entity.

#### Action inputs

None.

#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The **Enrich Entities** action can enrich the `URL` entity and provide the following enrichment results:

Enrichment field name | Source (JSON key) | Applicability  
---|---|---  
`threatTypes` | The CSV file of threat types. | When available in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Entities** action:
    
    
    {
       "Entity": "Entity",
       "EntityResult": [
           {
               "expireTime": "2024-12-20T13:47:20.786242980Z",
               "threatTypes": [
                   "SOCIAL_ENGINEERING_EXTENDED_COVERAGE"
               ]
           }
       ]
    }
    

##### Output messages

The **Enrich Entities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully enriched the following entities in Web Risk: ENTITY_ID.` `The action wasn't able to enrich the following entities in Web Risk: ENTITY_ID.` `No information was found for the provided entities.` | The action succeeded.  
`Error executing action "Enrich Entities". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Web Risk.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Web Risk server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Web Risk server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Submit Entities

Use the **Submit Entities** action to submit entities to Web Risk for analysis.

This action is asynchronous. Adjust the script timeout value in the Google SecOps integrated development environment (IDE) for the action, as needed.

This action runs on the Google SecOps `URL` entity.

#### Action inputs

The **Submit Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Abuse Type` | Optional.The abuse type that associates with a submission. For more information about abuse types, see [AbuseType](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#abusetype).The possible values are as follows:

  * `Select One`
  * `Malware`
  * `Social Engineering`
  * `Unwanted Software`

The default value is `Select One`.  
`Confidence Level` | Optional.The confidence level for a submission.For more information about confidence levels, see [Confidence](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#confidence) and [ConfidenceLevel](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#confidencelevel).The possible values are as follows:

  * `Select One`
  * `Low`
  * `Medium`
  * `High`

The default value is `Select One`.  
`Justification` | Optional.The justification for a submission.For more information about justification options, see [JustificationLabel](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#justificationlabel).The possible values are as follows:

  * `Manual Verification`
  * `User Report`
  * `Automated Report`

The default value is `User Report`.  
`Comment` | Optional.A comment to justify the submission.  
`Region Code` | Optional.A comma-separated list of the Common Locale Data Repository (CLDR) codes for countries or regions that associate with the submission. For more information about submissions, see [Submission](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#submission).  
`Platform` | Optional.A platform type where the submission was detected. The possible values are as follows:

  * `Select One`
  * `Android`
  * `iOS`
  * `MacOS`
  * `Windows`

The default value is `Select One`.  
`Skip Waiting` | Optional.If selected, action initializes the submission and does not wait for it to finish.The default value is `True`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
