---
url: https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications/
title: Set up programmatic notifications \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:21.969998+00:00
---

# Set up programmatic notifications  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Set up programmatic notifications Stay organized with collections  Save and categorize content based on your preferences. 

#### Interactive tutorials: Set up automated responses to Cloud Billing budget notifications (30 minutes)

In this interactive tutorial, you'll learn how to do the following:

  * Set up a Pub/Sub topic
  * Create a budget on a billing account that's connected to the Pub/Sub topic
  * Create a Cloud Run function that listens for updates from the Pub/Sub topic
  * Test your Cloud Run function



[ **Launch the tutorial**](https://console.cloud.google.com/home/dashboard?walkthrough_tutorial_id=billing--budget--cost_enforcement)

This document explains how to set up programmatic budget and cost anomaly ([Preview](https://cloud.google.com/products/#product-launch-stages)) notifications using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

[Budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#manage-notifications) and [cost anomalies](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies#set-notifications) are typically configured to send email notifications. If you use budgets or cost anomaly detection as a cost control tool, email notifications might not be the best method to use to ensure timely action to control your costs. You can set up and use programmatic notifications to automate cost control responses. Examples of automated cost control responses include the following:

  * [Integrate with Slack for faster response](https://docs.cloud.google.com/billing/docs/how-to/send-notifications-to-slack)
  * [Manage resource consumption to reduce costs](https://docs.cloud.google.com/billing/docs/how-to/control-usage)
  * [Limit spending by disabling billing when you reach your budget](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications)



## Limitations

  * Budgets use estimated Cloud Billing data which is subject to change until your invoice is finalized.

  * If you set [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) to [limit resource sharing by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) (specifically, the `iam.allowedPolicyMemberDomains` constraint), then you might encounter an error when you try to set up or connect Pub/Sub topics. In this situation, you must exempt the project containing your Pub/Sub topic from the organization policy. To exempt the project, complete the following steps:

    1. [Override the organization policy for the project](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#override_the_organization_policy_for_a_project) that contains the Pub/Sub topic.
    2. Follow the steps to connect your Pub/Sub topic.



## Permissions required for this task

### Budget notifications

To set up programmatic budget notifications, you need permissions to create or modify budgets and Pub/Sub topics. You need a different set of permissions depending on your level of access.

Users with Cloud Billing account permissions | Users with project-level permissions only ([Preview](https://cloud.google.com/products/#product-launch-stages))  
---|---  
If your organization uses [custom roles](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) for authentication, you need the following permissions in the custom roles: 

  * [`billing.budgets.create`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`billing.budgets.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`billing.budgets.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`billing.budgets.update`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`pubsub.topics.setIamPolicy`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.
  * [`pubsub.topics.list`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.

For custom roles to modify an _existing_ Cloud Billing budget to connect it to an _existing_ Pub/Sub topic, you need the following permissions: 

  * [`billing.budgets.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`billing.budgets.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`billing.budgets.update`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on the Cloud Billing account.
  * [`pubsub.topics.list`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.

To gain the necessary permissions using predefined roles, ask your administrator to grant you one of the following predefined [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) roles on your Cloud Billing account: 

  * [Billing Account Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)

And ask your administrator to grant you the following role on the _target project_ that contains the Pub/Sub topics: 

  * [Pub/Sub Admin](https://docs.cloud.google.com/pubsub/docs/access-control)

|  If your organization uses [custom roles](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) for authentication, you need the following permissions in the custom roles: 

  * [`resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on your project.
  * [`billing.resourceCosts.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on your project (optional).
  * [`billing.resourcebudgets.read`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on your project.
  * [`billing.resourcebudgets.write`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budgets_and_spending_alerts) on your project.
  * [`pubsub.topics.setIamPolicy`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.
  * [`pubsub.topics.list`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.

To gain the necessary permissions using predefined roles, ask your administrator to grant you one of the following predefined [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) roles on the project: 

  * [Project Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic)
  * [Project Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

And ask your administrator to grant you the following role on the _target project_ that contains the Pub/Sub topics: 

  * [Pub/Sub Admin](https://docs.cloud.google.com/pubsub/docs/access-control)

  
  
### Anomaly notifications

To set up programmatic anomaly notifications, you need permissions to create or modify anomalies and Pub/Sub topics. You must have Cloud Billing account permissions.

Users with Cloud Billing account permissions ([Preview](https://cloud.google.com/products/#product-launch-stages))  
---  
If your organization uses [custom roles](https://docs.cloud.google.com/billing/docs/how-to/custom-roles) for authentication, you need the following permissions in the custom roles: 

  * `billing.accounts.get` on the Cloud Billing account.
  * `billing.accounts.getIamPolicy` on the Cloud Billing account.
  * `billing.anomalies.get` on the Cloud Billing account.
  * `billing.anomalies.list` on the Cloud Billing account.
  * [`pubsub.topics.setIamPolicy`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.
  * [`pubsub.topics.list`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ that contains the Pub/Sub topics that you want to use.
  * [`pubsub.subscriptions.consume`](https://docs.cloud.google.com/pubsub/docs/access-control) on the _target project_ (or the subscription) that contains the Pub/Sub subscriptions that you want to use.

To gain the necessary permissions using predefined roles, ask your administrator to grant you one of the following predefined [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) roles on your Cloud Billing account: 

  * [Billing Account Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)

And ask your administrator to grant you the following role on the _target project_ that contains the Pub/Sub topics: 

  * [Pub/Sub Admin](https://docs.cloud.google.com/pubsub/docs/access-control)

  
  
## Create a Pub/Sub topic

To set up programmatic budget or anomaly notifications, you must first [create a Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic). If you already configured a Pub/Sub topic for budgets or cost anomalies, you can skip this step.

  1. Go to the Google Cloud console **Pub/Sub** page.

[Sign in to Google Cloud console Pub/Sub](https://console.cloud.google.com/cloudpubsub/)

  2. Select a project to contain the Pub/Sub topic.

When configuring Pub/Sub topics for billing notifications, we recommend you use a [FinOps administration project](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account#set-up-billing-project) to contain your billing-related Pub/Sub topics.

  3. Click add_box **Create topic**.

  4. In the **Topic ID** field, provide a topic name.

  5. Retain the default subscription and encryption settings, and click **Create**.


**Note:** You must have permission to grant the Pub/Sub Publisher role on the topic to allow Cloud Billing to publish messages to it.

## Connect your Pub/Sub topic

To enable programmatic notifications to receive Pub/Sub messages with the current status of your budget or anomaly, you must connect your budget or anomaly to your Pub/Sub topic.

### Budget notifications

To connect a Pub/Sub topic to a Cloud Billing budget, complete the following steps:

Users with Cloud Billing account permissions | Users with project-level permissions only ([Preview](https://cloud.google.com/products/#product-launch-stages))  
---|---  
  
  1. Sign in to the **Budgets & alerts** page in the Google Cloud console. [ Open Budgets & alerts](https://console.cloud.google.com/billing/budgets)
  2. At the prompt, choose the Cloud Billing account that you want to manage budgets for. The **Budgets & alerts** page opens for the selected billing account.
  3. Select the budget you want to connect, or [create a new budget](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget).
  4. In the **Actions** section, under **Manage notifications** , select **Connect a Pub/Sub topic to this budget**.
  5. In the **Project** field, click **Select a project** and choose the project that contains the Pub/Sub topics you set up.
  6. Under **Select a Pub/Sub topic** , select an existing topic, or create a new topic by clicking **Create a topic**. 
     * If you create a new topic, in the **Topic ID** field, provide a topic name, and click **Create topic**.
     * After you create the topic, it's automatically selected.
  7. Click **Save**.

| 

  1. Sign in to the Google Cloud console dashboard and select a project. [ Open Google Cloud console](https://console.cloud.google.com/projectselector2/home/dashboard?project=_)
  2. Select the project that you want to manage budgets for.
  3. Navigate to the **Billing** section: Open the Google Cloud console **Navigation menu** menu and select **Billing**. If you're prompted to choose which billing account you want to view and manage, click **Go to linked billing account** to view the billing account that's linked to your selected project.  The Billing **Overview** page opens for the selected billing account.
  4. In the **Cost management** section of the **Billing navigation menu** , select **Budgets & alerts**. 
  5. Select the budget you want to connect, or [create a new budget](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget).
  6. In the **Actions** section, under **Manage notifications** , select **Connect a Pub/Sub topic to this budget**.
  7. In the **Project** field, click **Select a project** and choose the project that contains the Pub/Sub topics you set up.
  8. Under **Select a Pub/Sub topic** , select an existing topic, or create a new topic by clicking **Create a topic**. 
     * If you create a new topic, in the **Topic ID** field, provide a topic name, and click **Create topic**.
     * After it's created, the topic will be selected.
  9. Click **Save**.

  
  
### Anomaly notifications

To connect a Pub/Sub topic to a cost anomaly, complete the following steps:

Users with Cloud Billing account permissions ([Preview](https://cloud.google.com/products/#product-launch-stages))  
---  
  
  1. Sign in to the **Anomalies** page in the Google Cloud console. [ Open Anomalies](https://console.cloud.google.com/billing/anomalies)
  2. At the prompt, choose the Cloud Billing account that you want to manage anomalies for. The **Anomalies** page opens for the selected billing account.
  3. Click settings **Manage anomalies**.
  4. Enter an **Anomaly threshold** value for **Cost impact**. This amount is the threshold value that triggers notifications. If you don't provide a value, the threshold is set to zero, and notifications are sent for all anomalies.
  5. In the **Pub/Sub notifications** section, select **Connect a Pub/Sub topic to receive programmatic updates about anomalies**.
  6. From the drop-down menu that appears, select the Pub/Sub topic that you want to connect to receive notifications. 
     * The topics are listed by project. You might need to switch the project you're viewing to find the topic that you want to select.
     * If you want to create a new topic, switch to your preferred project _before_ you click **Create a topic**.
  7. Click **Save**.

  
  
## Notification format

Notifications sent to the Pub/Sub topic consist of two parts:

  * **Attributes** : A set of key-value pairs describing the event.
  * **Data** : A string containing a JSON object that describes the budget alert details.




### Budget notifications

### Attributes

Attributes are key-value pairs contained in all notifications sent by Cloud Billing to your Pub/Sub topic. Notifications always contain the following set of key-value pairs, regardless of the notification payload.

Attribute name | Example | Description  
---|---|---  
**billingAccountId** | ` 01D4EE-079462-DFD6EC ` | The identifier for the Cloud Billing account owning the budget.   
**budgetId** | ` de72f49d-779b-4945-a127-4d6ce8def0bb ` | The identifier for the budget alert within the Cloud Billing account.  
**schemaVersion** | ` 1.0 ` | The notifications schema version.  
  
### Data

Budget alert details are returned in a base64-encoded UTF-8 string containing a JSON object with the following properties:

Data | Example | Description  
---|---|---  
` budgetDisplayName ` | ` "My Personal Budget" ` | The human-readable name assigned to the budget.  
` costAmount ` | ` 140.321 ` | The amount of costs accrued. The type of costs tracked depends on budget filters & settings.  
` costIntervalStart ` | ` "2021-02-01T08:00:00Z" ` |  The start of the budget alert period. `costAmount` includes costs for usage starting at this time. This is the first day of the budget's time period (month, quarter, year, or a custom date range) during which the budget usage occurred.   
` budgetAmount ` | ` 152.557 ` | The amount allocated in the budget.  
` budgetAmountType ` | ` "SPECIFIED_AMOUNT" ` | The budget amount type. This can be one of the following values: 

  * "`SPECIFIED_AMOUNT`": A fixed amount.
  * "`LAST_MONTH_COST`": Total costs incurred during the last calendar month.
  * "`LAST_PERIODS_COST`": The costs incurred during the last, non-monthly, calendar period, such as a quarter or a year.

  
` alertThresholdExceeded ` | ` 0.9 ` | The highest configured actual cost alert threshold exceeded. Value is a percent in decimal format (for example, 0.9 is 90%). This key isn't present if the actual cost doesn't exceed any threshold.  
` forecastThresholdExceeded ` | ` 0.2 ` | The highest forecasted cost alert threshold exceeded. Value is a percent in decimal format (for example, 0.2 is 20%). This key isn't present if the forecasted cost doesn't exceed any threshold.  
` currencyCode ` | ` "USD" ` | The budget alert currency. All costs and budget alert amounts are in this currency.  
**Note:** To test an example budget notification, follow the steps in [Listen to your notifications](https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications).

### Anomaly notifications

### Attributes

Attributes are key-value pairs contained in all notifications sent by Cloud Billing to your Pub/Sub topic. Notifications always contain the following set of key-value pairs, regardless of the notification payload.

Attribute name | Example | Description  
---|---|---  
**scope** | ` scope_project ` | The scope of the anomaly.   
**billingAccountName** | ` billingAccounts/01D4EE-079462-DFD6EC ` | The identifier of the Cloud Billing account where the anomaly occurred.   
**resourceDisplayName** | ` My project ` | The display name of the resource that the anomaly occurred in.  
**resourceName** | ` projects/123456 ` | The identifier of the resource that the anomaly occurred in.  
**SchemaVersion** | ` 1.0 ` | The Pub/Sub schema version.  
  
### Data

Anomaly alert details are returned in a base64-encoded UTF-8 string containing a JSON object with the following properties:

Data | Example | Description  
---|---|---  
` anomalyName ` | ` billingAccounts/01D4EE-079462-DFD6EC/anomalies/aaa ` | The resource name for the anomaly.  
` billingAccountName ` | ` billingAccounts/01D4EE-079462-DFD6EC ` | The identifier of the billing account.  
` resourceName ` | ` "projects/12345" ` | The identifier of the resource that the anomaly occurred in.  
` resourceDisplayName ` | ` "My project" ` |  The display name of the resource that the anomaly occurred in.   
` detectionDate ` | ` "2024-02-01T08:00:00Z" ` | The date the cost anomaly was detected.  
` Scope ` | ` SCOPE_PROJECT ` | Indicates the scope of the anomaly.  
` expectedSpendAmount ` | ` {  
"currencyCode": "USD",  
"units": "8",  
"nanos": 988106832  
}  
` | The expected spend for the resource.  
` actualSpendAmount ` | ` 196.22 ` | The actual spend for the resource.  
` deviationAmount ` | ` 31.01 ` | The difference between the actual spend and expected spend.  
` deviationPercentage ` | ` 18.77 ` | The percentage of deviation amount from expected spend.  
` Root cause ` | 
    
    
    root_causes {
    resource: "services/XXX-XXXX-XXX"
    display_name: "BigQuery"
    cause_type: CAUSE_TYPE_SERVICE
    deviation {
      expected_spend {
        currency_code: "USD"
        units: "5000"
      }
      actual_spend {
        currency_code: "USD"
        units: "5000"
      }
      deviation_amount {
        currency_code: "USD"
        units: "5000"
      }
      deviation_percentage: "Infinity"
    }
    sub_causes {
      resource: "locations/us-west1",
      display_name: "us-west1",
      cause_type: CAUSE_TYPE_LOCATION,
      deviation {
        expected_spend {
          currency_code: "USD",
        }
        actual_spend {
          currency_code: "USD",
          units:"5000"
        }
        deviation_amount {
          currency_code: "USD",
          units: "5000"
        }
        deviation_percentage: "Infinity"
      }
      sub_causes {
        resource: "services/XXXX-XXXX-XXXX/skus/XXXX-XXXX-XXXX"
        display_name: "Some display name"
        cause_type: CAUSE_TYPE_SKU
        deviation {
          expected_spend {
            currency_code: "USD"
          }
          actual_spend {
            currency_code: "USD"
            units: 5000
          }
          deviation_amount {
            currency_code: "USD"
            units: 5000
          }
          deviation_percentage: "Infinity"
        }
      }
      sub_causes {
        resource: "services/XXXX-XXXX-XXXX/skus/XXXX-XXXX-XXXX"
        display_name: "Some display name"
        cause_type: CAUSE_TYPE_SKU
        deviation {
          expected_spend {
            currency_code: "USD"
            units: "1"
            nanos: 5413077
          }
          actual_spend {
            currency_code: "USD"
            units: "1",
            nanos: 122606000
          }
          deviation_amount {
            currency_code: "USD"
            nanos: 117192923
          }
          deviation_percentage:11.656196419841217
        }
      }
    }
    }
    

| A repeated field that contains information about the root cause of the anomaly.   
  
## Delivery for notifications to Pub/Sub

After you connect your budget or anomaly to a Pub/Sub topic, you can expect to receive programmatic notifications as follows:

### Budget notifications

  * Budget notifications are sent to the Pub/Sub topic multiple times per day with the current status of your budget. This cadence is different than the cadence for budget alert emails, which are only sent when a [budget threshold](https://docs.cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) is met.
  * Pub/Sub notifications are sent even if the Cloud Billing account has no usage.
  * It may take several hours before you receive the first Pub/Sub notification.
  * Pub/Sub only provides at-least-once delivery. You might receive a message multiple times, and messages might arrive out of order.
  * If delivery fails due to Pub/Sub topic misconfiguration, you won't be notified.



Delivery might fail for one of the following reasons:

  * The Pub/Sub topic no longer exists.
  * The Cloud Billing no longer has permission to publish to the Pub/Sub topic.
  * You exceeded your notification quota.
  * You have [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) in place that [limit resource sharing by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) (specifically, the `iam.allowedPolicyMemberDomains` constraint).



### Anomaly notifications

  * Anomaly notifications are sent to the Pub/Sub topic only when the [threshold](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies#set-anomaly-threshold) is reached.
  * Pub/Sub only ensures an at-least-once delivery. You might receive a message multiple times, and messages might arrive out of order.
  * If delivery fails due to Pub/Sub topic misconfiguration, you won't be notified.



Delivery might fail for one of the following reasons:

  * The Pub/Sub topic no longer exists.
  * The Cloud Billing account no longer has permission to publish to the Pub/Sub topic.
  * You exceeded your notification quota.
  * You have [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) in place that [limit resource sharing by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) (specifically, the `iam.allowedPolicyMemberDomains` constraint).



For more information, see [Publish and receive messages in Pub/Sub](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console).

## What's next

To learn more about how you can use programmatic notifications, review the following examples of programmatic cost control responses:

  * [Listen to your notifications](https://docs.cloud.google.com/billing/docs/how-to/listen-to-notifications)
  * [Send notifications to Slack](https://docs.cloud.google.com/billing/docs/how-to/send-notifications-to-slack)
  * [Control resource usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/control-usage)
  * [Disable billing usage with notifications](https://docs.cloud.google.com/billing/docs/how-to/disable-billing-with-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
