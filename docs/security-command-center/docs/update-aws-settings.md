---
url: https://docs.cloud.google.com/security-command-center/docs/update-aws-settings/
title: Modify the AWS connection settings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:16.255338+00:00
---

# Modify the AWS connection settings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/update-aws-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)



Send feedback 

#  Modify the AWS connection settings Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

After you connect [Security Command Center to Amazon Web Services (AWS)](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws) for configuration and resource data collection, you can modify the connection settings.

## Before you begin

Complete these tasks before you complete the remaining tasks on this page.

### Set up permissions in Google Cloud

To get the permissions that you need to use the AWS connector, ask your administrator to grant you the [Cloud Asset Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.owner) (`roles/cloudasset.owner`) IAM role. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create AWS accounts

Ensure that you have the following AWS resources:

  * An [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) with [AWS IAM access](https://aws.amazon.com/iam/getting-started/?nc=sn&loc=3) for the delegated and collector AWS account consoles.

  * The [AWS account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId) for an AWS account that you can use as the delegated account. The delegated account must meet the following requirements:

    * The delegated account must be attached to an [AWS organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#orgs_getting-started_concepts-orgs). To attach an account to an AWS organization, do the following:

      1. [Create](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html) or identify an organization where you will attach the delegated account.
      2. Invite the delegated account to [join the organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html).
    * The delegated account must be one of the following:

      * An [AWS management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html).
      * An [AWS delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html).
      * An AWS account with a [resource-based delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html#orgs-policy-delegate) that provides the `organizations:ListAccounts` permission. For an example policy, see [Create a resource-based delegation policy with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-policy-delegate.html) in the AWS documentation.



## Modify the AWS connection

Modify an existing AWS connection when your AWS environment configuration changes. For example, you want to monitor different AWS regions, or change the list of AWS accounts that Security Command Center uses. You can't modify the names of the delegated role and the collector role. If you need to change these role names, you must delete your AWS connector and set up a new connection.

  1. In the Google Cloud console, go to the Security Command Center page.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/config/services)

  2. Select the organization that you activated Security Command Center Enterprise on.

  3. Click **settings Settings**.

  4. Click the **Connectors** tab.

  5. Click **Edit** beside the connection that you want to update.

  6. In the **Edit Amazon Web Services connector** page, make your changes. The following table describes the options.

Option | Description  
---|---  
**Add AWS connector accounts** | Select an option, depending on your preference:
     * **Add accounts automatically (recommended)** : Select this option to let Security Command Center discover the AWS accounts automatically.
     * **Add accounts individually** : Select this option to manually add AWS accounts yourself.  
**Exclude AWS connector accounts** | If you selected **Add accounts automatically** under the **Add AWS connector accounts** section, provide a list of AWS accounts that Security Command Center should not use to find resources.  
**Enter AWS connector accounts******|  If you selected **Add accounts individually** under the **Add AWS connector accounts** section, provide a list of AWS accounts that Security Command Center can use to find resources.  
**Select regions to collect data******|  Select one or more AWS regions for Security Command Center to collect data from. Leave the **AWS regions** field empty to collect data from all regions.  
**Maximum queries per second (QPS)** for AWS services | You can change the QPS to control the quota limit for Security Command Center. Set the override to a value that is less than the default value for that service, and greater than or equal to `1`. The default value is the maximum value. If you do change the QPS, Security Command Center might encounter issues fetching data. Therefore, we don't recommend changing this value.  
**Endpoint for AWS Security Token Service** | You can specify a specific endpoint for the AWS Security Token Service (for example, `https://sts.us-east-2.amazonaws.com`). Leave the **AWS Security Token Service** field empty to use the default global endpoint (`https://sts.amazonaws.com`).  
  7. If you changed the delegated account ID or the list of AWS accounts to include or exclude, you must update your AWS environment. A change to the delegated account ID requires that you set up your AWS configuration again. A change to the list of AWS accounts requires that you add or remove collector roles. Removing AWS accounts from the exclude list, because you want to include them, requires you to add the collector roles to those accounts. Complete the following:

     1. Click **Continue**.
     2. In the **Create connection with AWS** page, complete one of the following:

        * Download the CloudFormation templates for the delegated role and the collector role. For instructions on using the templates, see [Use CloudFormation templates to set up your AWS environment](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#cloudformation).

        * If you want to change the AWS configuration manually, select **Use the AWS console**. Copy the service agent ID, delegated role name, and the collector role name. For instructions on updating AWS manually, see [Configure AWS accounts manually](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#configure-aws-manually).

  8. If you added an AWS account to the list of AWS accounts to exclude, we recommend that you remove the collector role from the account.

  9. Click **Test connector** to verify that Security Command Center can connect to your AWS environment. If the connection is successful, the Google Cloud service agent can assume the delegated role and the delegated role has all the required permissions to assume the collector role. If the connection isn't successful, see [Troubleshooting errors when testing the connection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws#troubleshooting-connection).

  10. Click **Save**.




## What's next

  * For troubleshooting information, see [Connect Security Command Center to AWS](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
