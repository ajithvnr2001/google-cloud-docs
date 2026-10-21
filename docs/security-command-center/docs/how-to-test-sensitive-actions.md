---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-test-sensitive-actions/
title: Test Sensitive Actions Service \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:02.275163+00:00
---

# Test Sensitive Actions Service  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-test-sensitive-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Test Sensitive Actions Service Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Verify that Sensitive Actions Service is working by intentionally triggering the `Persistence: project SSH key added` detector and checking for findings.

To learn more about the Sensitive Actions Service service, see [Sensitive Actions Service overview](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).

## Before you begin

To complete this guide, you must have an Identity and Access Management (IAM) role with the `compute.projects.setCommonInstanceMetadata` and `iam.serviceAccounts.actAs` permissions in the project where you will perform the test, such as the Compute Admin role (`roles/compute.admin`).

## Testing Sensitive Actions Service

To test Sensitive Actions Service, you add a project-level SSH key, which may grant SSH key access to all instances in the project.

This detector doesn't generate a finding if there is already a project-level SSH key set on the project. Choose a project that doesn't already have any project-level SSH keys.

### Step 1: Triggering a Sensitive Actions Service detector

To trigger the detector, you need a test user account. You can create a test user account with a gmail.com email address or use an existing user account in your organization. You add the test user account to your organization and grant it excessive permissions.

For more instructions on how to add the project-level SSH key, see [Add SSH keys to project metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#add_ssh_keys_to_project_metadata). For instructions on how to generate an SSH key, see [Create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).

  1. Go to the [Compute Engine Metadata](https://console.cloud.google.com/compute/metadata) page in the Google Cloud console.

[Go to Metadata](https://console.cloud.google.com/compute/metadata)

  2. Click the **SSH Keys** tab.

  3. Verify that there aren't currently any SSH keys set on the project. If SSH keys are set, you will see the existing keys in a table, and the test won't work. Choose a project that doesn't have any existing project-level SSH keys for the test.

  4. Click **Add SSH Key**.

  5. Add a public key into the text box. For more details on how to generate an SSH key, see [Create SSH keys](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys).

  6. Click **Save**.




Next, verify that the `Persistence: project SSH key added` detector has written findings.

### Step 2: Viewing the finding in Security Command Center

To review Sensitive Actions Service findings in the console, follow these steps:

  1. In the Google Cloud console, go to the **Findings** page of Security Command Center.

[Go to Findings](https://console.cloud.google.com/security/command-center/findingsv2)

  2. Select your Google Cloud project or organization.
  3. In the **Quick filters** section, in the **Source display name** subsection, select **Sensitive Actions Service**. The findings query results are updated to show only the findings from this source. 
  4. To view the details of a specific finding, click the finding name in the **Category** column. The details panel for the finding opens and displays the **Summary** tab. 
  5. On the **Summary** tab, review the details of the finding, including information about what was detected, the affected resource, and—if available—steps that you can take to remediate the finding. 
  6. Optional: To view the full JSON definition of the finding, click the **JSON** tab.



### Step 3: Viewing the finding in Cloud Logging

You can view sensitive action log entries by using Cloud Logging.

  1. Go to **Logs Explorer** in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. If required, change to the organization view by using the **Organization selector** at the top of the page.

  3. Use the **Query** pane to build your query:

     1. In the **All resources** list, select **sensitiveaction.googleapis.com/Location**.
     2. Click **Apply**. The **Query results** table is updated with the logs you selected.
  4. To view a log, click a table row, and then click **Expand nested fields**.




## Clean up

When you're finished testing, remove the project-level SSH key.

  1. Go to the **Compute Engine Metadata** page in the Google Cloud console.

[Go to Metadata](https://console.cloud.google.com/compute/metadata)

  2. Click **Edit**.

  3. Click delete**Delete item** next to the SSH key.

  4. Click **Save**.




## What's next

  * Learn more about [using Sensitive Actions Service](https://docs.cloud.google.com/security-command-center/docs/how-to-use-sensitive-actions).
  * Read a high-level overview of [Sensitive Actions Service concepts](https://docs.cloud.google.com/security-command-center/docs/concepts-sensitive-actions-overview).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
