---
url: https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws/
title: Connect to AWS for configuration and resource data collection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:46.826929+00:00
---

# Connect to AWS for configuration and resource data collection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Connect to AWS for configuration and resource data collection Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

You can connect Security Command Center Enterprise tier to your Amazon Web Services (AWS) environment so that you can do the following:

  * Detect and remediate software vulnerabilities and misconfigurations in your AWS environment
  * Create and manage a security posture for AWS
  * Identify potential attack paths from the public internet to your high-value AWS assets
  * Map compliance of AWS resources with various standards and benchmarks



When you connect Security Command Center to AWS, a single place for your security operations team is created to manage and remediate threats and vulnerabilities across Google Cloud and AWS.

To let Security Command Center monitor your AWS organization, you configure a _connector_. The connector uses a [Google Cloud service agent](https://docs.cloud.google.com/iam/docs/service-agents) and an AWS account that has access to the resources that you want to monitor. Security Command Center uses this connector to periodically collect data across all the AWS accounts and regions that you define. This data is handled in the same way as Service Data, according to the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

You can create one AWS connector for each Google Cloud organization. The connector uses API calls to collect AWS asset data. These API calls might incur AWS charges.

This document describes how to set up the connector for AWS. When you set up a connector, you configure the following:

  * A series of accounts in AWS that have direct access to the AWS resources that you want to monitor. In the Google Cloud console, these accounts are called _collector accounts_.
  * An account in AWS that has the appropriate policies and roles to allow authentication to collector accounts. In the Google Cloud console, this account is called the _delegated account_. Both the _delegated account_ and the _collector accounts_ must be in the same AWS organization.
  * A service agent in Google Cloud that connects to the delegated account for authentication.
  * A pipeline to collect asset data from AWS resources.
  * Optional: Permissions for Sensitive Data Protection to profile your AWS content.



## Data collection types

Depending on your security goals, you can connect Security Command Center to AWS to collect different types of data:

  * **Resource and configuration data** : The AWS connector collects configuration metadata and resource data to discover misconfigurations, assess your security posture, and identify attack paths.
  * **Log data** : To power SIEM-curated detection capabilities and analyze AWS event logs (such as CloudTrail), you configure a separate connection for log ingestion. For more information, see [Connect to AWS for log data collection](https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws).



The following diagram shows this configuration. The tenant project is a project that is created automatically and contains your asset data collection pipeline instance.

![AWS and Security Command Center configuration.](https://docs.cloud.google.com/static/security-command-center/images/aws-scc-connection.svg)

## High-level overview of configuration steps

To connect Security Command Center to AWS, you complete the following steps in both AWS and Google Cloud

  1. Complete the steps in Before you begin.

  2. Configure the AWS connector and specify the delegated account ID. This action creates the service agent ID needed for the AWS configuration.

  3. Configure your AWS environment to create the required roles and policies using one of the following methods:

     * Automatically with CloudFormation templates.
     * Manually by entering AWS accounts.
  4. Complete the AWS connector configuration process and test the connection.




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



### Review AWS features

Make sure you are familiar with the following concepts and capabilities in AWS:

  * [AWS IAM roles and trust relationships](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

  * [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)

  * [AWS Organizations management accounts and delegated administrator](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)




### Plan for data collection

When you plan the data collection strategy, do the following. You need this information when performing the steps in this document.

  * Identify your [AWS management account ID](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html#FindAccountId). You must run the CloudFormation stack sets from the management account.
  * Identify the AWS account you'll use as the **delegated account**. This account authenticates the connection to Google Cloud.
  * Decide which AWS regions and accounts you want to collect data from.



## Configure the AWS connector

  1. Open the **Connectors** tab on the **Settings** page.

[Go to Connectors](https://console.cloud.google.com/security/command-center/config/connectors)

  2. Select the organization where you activated Security Command Center Enterprise.

  3. Select **Connectors > Add connector > Amazon Web Services**.

  4. In **Delegated account ID** , enter the AWS account ID for the AWS account that you can use as the delegated account.

  5. To let Sensitive Data Protection profile your AWS data, keep **Grant permissions for Sensitive Data Protection discovery** selected. This option adds AWS Identity and Access Management (IAM) permissions in the CloudFormation template for the collector role.

#### AWS IAM permissions granted by this option

     * `s3:GetBucketLocation`
     * `s3:ListAllMyBuckets`
     * `s3:GetBucketPolicyStatus`
     * `s3:ListBucket`
     * `s3:GetObject`
     * `s3:GetObjectVersion`
     * `s3:GetBucketPublicAccessBlock`
     * `s3:GetBucketOwnershipControls`
     * `s3:GetBucketTagging`
     * `iam:ListAttachedRolePolicies`
     * `iam:GetPolicy`
     * `iam:GetPolicyVersion`
     * `iam:ListRolePolicies`
     * `iam:GetRolePolicy`
     * `ce:GetCostAndUsage`
     * `dynamodb:DescribeTableReplicaAutoScaling`
     * `identitystore:ListGroupMemberships`
     * `identitystore:ListGroups`
     * `identitystore:ListUsers`
     * `lambda:GetFunction`
     * `lambda:GetFunctionConcurrency`
     * `logs:ListTagsForResource`
     * `s3express:CreateSession`
     * `s3express:GetBucketPolicy`
     * `s3express:ListAllMyDirectoryBuckets`
     * `wafv2:GetIPSet`

**Note:** This option only grants the required AWS permissions to the collector role. To profile your AWS data, [enable sensitive data discovery](https://docs.cloud.google.com/security-command-center/docs/aws-sensitive-data-discovery) after creating this AWS connector.
  6. Optionally, review and edit the **Advanced options**. See Customize the AWS connector configuration for information about additional options.

  7. Click **Continue**. The **Connect to AWS** page opens.

  8. Select one of the following:

     * **Use AWS CloudFormation templates** , and then download and review the CloudFormation templates for the delegated role and the collector role.

     * **Configure AWS accounts manually** : Select this if you configured the advanced options or need to change the default AWS role names (**aws-delegated-role** , **aws-collector-role** , and **aws-sensitive-data-protection-role**). Copy the service agent ID, delegated role name, collector role name, and the Sensitive Data Protection collector role name.

You can't change the role names after you create the connection.

  9. To configure the required roles and policies, follow the instructions in Configure your AWS environment.

**Important:** You must complete the steps in Configure your AWS environment before you click **Save** or **Continue** on the **Connect to AWS** page.



## Configure your AWS environment

You can set up your AWS environment using one of the following methods:

  * Use the CloudFormation templates that you downloaded in Configure the AWS connector. For instructions, see Use CloudFormation templates to set up your AWS environment.
  * Configure the AWS accounts manually if you're using customized settings or role names. For instructions, see Configure AWS accounts manually.



### Use CloudFormation templates to set up your AWS environment

If you downloaded CloudFormation templates, use these high-level steps to set up your AWS environment:

  1. Sign in to the [AWS delegate account console](https://console.aws.amazon.com/iam). Make sure that you're signed in to the delegate account that is used to assume other collector AWS accounts (that is, either an AWS management account or any member account that's registered as a delegated administrator).
  2. Create a stack that provisions the delegate role. For more information, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).

Keep the following in mind:

     * If you changed the role name for the delegated role, collector role, or Sensitive Data Protection role, update the parameters accordingly. The parameters that you enter must match the ones that are listed in the **Connect to AWS** page in the Google Cloud console.
     * Wait for the stack to be created. If an error occurs, see Troubleshooting. For more information, see [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the AWS documentation.
  3. Create a stack that provisions the collector roles. For more information about how to do this, see [Create CloudFormation StackSets with service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-associate-stackset-with-org.html).

Keep the following in mind:

     * If you added AWS accounts individually (by selecting **Add accounts individually** when configuring the connector in the Google Cloud console), you can also create separate stacks for each AWS account instead of creating a single stack set.

       * Service-managed permissions is the recommended setting. You can choose to use self-managed permissions, but then you must [grant the permissions manually](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html).
**Note:** If you choose self-managed permissions, you can choose which AWS accounts you want to deploy to. The CloudFormation template doesn't support using a list of AWS accounts to include or exclude, as described in Custom configuration. If you want to create a list of AWS accounts to include or exclude, the stack set might create some stacks that are not required. You can ignore or remove those stacks.
       * If you changed the role name for the delegated role, collector role, or Sensitive Data Protection role, update the parameters accordingly. The parameters that you enter must match the ones that are listed in the **Connect to AWS** page in the Google Cloud console.

       * As required by your organization, configure your stack set options.

       * When specifying the deployment options, choose your deployment targets. You can deploy to the entire AWS organization or deploy to an organization unit (OU) that includes all the AWS accounts that you want to collect data from.

       * Specify the AWS regions to create the roles and policies in. Because roles are global resources, you don't need to specify multiple regions.

       * If you receive an error, see Troubleshooting. For more information, see [Create CloudFormation StackSets with service-managed permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-associate-stackset-with-org.html) in the AWS documentation.

  4. If you need to collect data from the management account, then sign in to the management account and deploy a separate stack to provision the collector roles. When specifying the template, upload the collector role template file.

This step is needed because AWS CloudFormation stack sets don't create stack instances in management accounts. For more information, see [DeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html) in the AWS documentation.




After you finish these steps, complete the AWS connector configuration.

### Configure AWS accounts manually

If you can't use the CloudFormation templates (for example, you're using different role names or are customizing the integration), you can create the required AWS IAM policies and AWS IAM roles manually.

Review and complete these sections in the following order:

  1. Create the AWS IAM policy for the delegated role.
  2. Create an AWS IAM role for the trust relationship between AWS and Google Cloud.
  3. Create the AWS IAM policy for asset configuration data collection.
  4. Create the AWS IAM role for asset configuration data collection in each account.
  5. Create the AWS IAM policy for Sensitive Data Protection.



You must create AWS IAM policies and AWS IAM roles for the delegated account and the collector accounts.

#### Create the AWS IAM policy for the delegated role

To create an AWS IAM policy for the delegated role (a delegated policy), follow the steps in [Create a policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html#step1-create-policy) in the AWS documentation.

When creating the policy, paste one of the following for the JSON step, depending on whether you selected the **Grant permissions for Sensitive Data Protection discovery** checkbox in Configure Security Command Center.

#### **Grant permissions for Sensitive Data Protection discovery** : cleared
    
    
        {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Action": "sts:AssumeRole",
                  "Resource": "arn:aws:iam::_:role/ COLLECTOR_ROLE_NAME",
                  "Effect": "Allow"
              },
              {
                  "Action": [
                      "organizations:List_",
                      "organizations:Describe _"
                  ],
                  "Resource": "_ ",
                  "Effect": "Allow"
              }
          ]
        }
        

Replace `COLLECTOR_ROLE_NAME` with the name of the collector role that you copied when configuring Security Command Center (the default is `aws-collector-role`).

#### **Grant permissions for Sensitive Data Protection discovery** : selected
    
    
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Action": "sts:AssumeRole",
              "Resource": [
                "arn:aws:iam::*:role/COLLECTOR_ROLE_NAME",
                "arn:aws:iam::*:role/SCAN_SENSITIVE_DATA_COLLECTOR_ROLE_NAME"
              ],
              "Effect": "Allow"
            },
            {
              "Action": [
                "organizations:List*",
                "organizations:Describe*"
              ],
              "Resource": "*",
              "Effect": "Allow"
            }
          ]
        }
        

Replace the following:

  * `COLLECTOR_ROLE_NAME`: the name of the configuration data collector role that you copied when configuring Security Command Center (the default is `aws-collector-role`).
  * `SCAN_SENSITIVE_DATA_COLLECTOR_ROLE_NAME`: the name of the Sensitive Data Protection collector role that you copied when configuring Security Command Center (the default is `aws-sensitive-data-protection-role`).



#### Create an AWS IAM role for the trust relationship between AWS and Google Cloud

Create a delegated role that sets up a trusted relationship between AWS and Google Cloud. This role uses the delegated policy that was created in Create the AWS IAM policy for the delegated role.

Follow the instructions in [Creating a role for OIDC](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html#idp_oidc_Create) in the AWS documentation.

When creating the role, specify the following:

  * **Trusted entity type** : Choose **Web Identity**.

  * **Identity Provider** : Choose **Google**.

  * **Audience** : Enter the service agent ID that you copied when you configured Security Command Center.

  * To grant the delegated role access to the collector roles, attach the permission policies to the role. Search for the delegated policy that was created in Create the AWS IAM policy for the delegated role and select it.

  * **Role details** : Enter the **Delegated role name** that you copied when you configured Security Command Center (the default name is `aws-delegated-role`).




#### Create the AWS IAM policy for asset configuration data collection

To create an AWS IAM policy for asset configuration data collection (a collector policy), complete the following:

  * Follow the steps in [Create a policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html#step1-create-policy) in the AWS documentation and repeat these steps, as needed, for each collector account.

When you create the role, specify the following for the JSON step:

**Note:** This custom policy grants additional permissions that are required for Security Command Center that are not included in the standard AWS managed policies. You attach this custom policy and the `ViewOnlyAccess` and `SecurityAudit` managed policies to the collector role in a later step.
        
        {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Effect": "Allow",
                  "Action": [
                      "ce:GetCostAndUsage",
                      "dynamodb:DescribeTableReplicaAutoScaling",
                      "identitystore:ListGroupMemberships",
                      "identitystore:ListGroups",
                      "identitystore:ListUsers",
                      "lambda:GetFunction",
                      "lambda:GetFunctionConcurrency",
                      "logs:ListTagsForResource",
                      "s3express:GetBucketPolicy",
                      "s3express:ListAllMyDirectoryBuckets",
                      "wafv2:GetIPSet"
                  ],
                  "Resource": [
                      "*"
                  ]
              },
              {
                  "Effect": "Allow",
                  "Action": [
                      "apigateway:GET"
                  ],
                  "Resource": [
                      "arn:aws:apigateway:*::/usageplans",
                      "arn:aws:apigateway:*::/usageplans/*/keys",
                      "arn:aws:apigateway:*::/vpclinks/*"
                  ]
              }
          ]
        
        }
        




#### Create the AWS IAM role for asset configuration data collection in each account

Create the collector role that lets Security Command Center get asset configuration data from AWS. This role uses the collector policy that was created in Create the AWS IAM policy for asset configuration data collection.

  * Follow the steps in [Create a custom role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html) in the AWS documentation and repeat these steps, as needed, for each collector account.

For the custom trust policy, add the following:
        
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::DELEGATE_ACCOUNT_ID:role/DELEGATE_ACCOUNT_ROLE"
              },
              "Action": "sts:AssumeRole"
            }
          ]
        }
        

Replace the following:

    * `DELEGATE_ACCOUNT_ID`: the AWS account ID for the delegate account.
    * `DELEGATE_ACCOUNT_ROLE`: the **Delegated role name** that you copied when you configured Security Command Center.

    * To grant this collector role access to your AWS asset configuration data, attach the permission policies to the role. Search for the custom collector policy that was created in Create the AWS IAM policy for asset configuration data collection, and select it.

    * Search and select the following managed policies:

      * **arn:aws:iam::aws:policy/job-function/ViewOnlyAccess**.
      * **arn:aws:iam::aws:policy/SecurityAudit**.
    * In the **Role details** section, enter the name of the configuration data collector role that you copied when you configured Security Command Center.




If you selected the **Grant permissions for Sensitive Data Protection discovery** checkbox in Configure Security Command Center, then proceed to the next section.

If you didn't enable the **Grant permissions for Sensitive Data Protection discovery** checkbox, then complete the AWS connector configuration.

#### Create the AWS IAM policy for Sensitive Data Protection

Complete these steps if you selected the **Grant permissions for Sensitive Data Protection discovery** checkbox in Configure Security Command Center.

To create an AWS IAM policy for Sensitive Data Protection (a collector policy), complete the following:

  * Follow the steps in [Create a custom role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html) in the AWS documentation and repeat, as needed, for each collector account.

When you create the custom role, specify the following for the JSON step:
        
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "s3:GetBucketLocation",
                "s3:ListAllMyBuckets",
                "s3:GetBucketPolicyStatus",
                "s3:ListBucket",
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketOwnershipControls",
                "s3:GetBucketTagging"
              ],
              "Resource": ["arn:aws:s3:::*"]
            },
            {
              "Effect": "Allow",
              "Action": [
                "iam:ListAttachedRolePolicies",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:ListRolePolicies",
                "iam:GetRolePolicy",
                "ce:GetCostAndUsage",
                "dynamodb:DescribeTableReplicaAutoScaling",
                "identitystore:ListGroupMemberships",
                "identitystore:ListGroups",
                "identitystore:ListUsers",
                "lambda:GetFunction",
                "lambda:GetFunctionConcurrency",
                "logs:ListTagsForResource",
                "s3express:GetBucketPolicy",
                "s3express:ListAllMyDirectoryBuckets",
                "wafv2:GetIPSet"
              ],
              "Resource": ["*"]
            },
            {
              "Effect": "Allow",
              "Action": [
                  "s3express:CreateSession"
              ],
              "Resource": ["arn:aws:s3express:*:*:bucket/*"]
            }
          ]
        }
        




#### Create the AWS IAM role for Sensitive Data Protection in each account

Complete these steps if you selected the **Grant permissions for Sensitive Data Protection discovery** checkbox in Configure the AWS connector.

Create the collector role that lets Sensitive Data Protection profile the contents of your AWS resources. This role uses the collector policy that was created in Create the AWS IAM policy for Sensitive Data Protection.

  * Follow the steps in [Creating an Identity and Access Management role using a custom trust policy (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html#roles-creatingrole-custom-trust-policy-console) in the AWS documentation and repeat the steps, as needed, for each collector account.

When creating the policy, specify the following:

    * **Trusted entity type** : Choose **Custom trust policy**.

    * For the custom trust policy, paste the following:
          
          {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Principal": {
                "AWS": "arn:aws:iam::DELEGATE_ACCOUNT_ID:role/DELEGATE_ACCOUNT_ROLE"
              },
              "Action": "sts:AssumeRole"
            }
          ]
          }
          

Replace the following:

      * `DELEGATE_ACCOUNT_ID`: the AWS account ID for the delegate account.
      * `DELEGATE_ACCOUNT_ROLE`: the **Delegated role name** that you copied when you configured Security Command Center.
    * To grant this collector role access to the contents of your AWS resources, attach the permission policies to the role. Search for the custom collector policy that was created in Create the AWS IAM policy for Sensitive Data Protection, and select it.

    * For role details, enter the name of the role for Sensitive Data Protection that you copied when you configured Security Command Center.




After you finish these steps, complete the AWS connector configuration.

## Complete the AWS connector configuration

  1. Return to the **Connect to AWS** page, and then click **Continue**.
  2. In the Google Cloud console, on the **Test connector** page, click **Test connector** to verify that Security Command Center can connect to your AWS environment. If the connection is successful, the test determined that the delegated role has all the required permissions to assume the collector roles. If the connection isn't successful, see Troubleshooting errors when testing the connection.

  3. Click **Save**.




## Customize the AWS connector configuration

This section describes some of the ways that you can customize the connection between Security Command Center and AWS. These options are available in the **Advanced options (optional)** section of the [**Add Amazon Web Services connector**](https://console.cloud.google.com/projectselector2/security/command-center/config/connectors/create?supportedpurview=organizationId) page in the Google Cloud console.

By default, Security Command Center automatically discovers your AWS accounts across all AWS regions. The connection uses the [default global endpoint for the AWS Security Token Service](https://docs.aws.amazon.com/general/latest/gr/sts.html) and the default queries per second (QPS) for the AWS service that you're monitoring. These advanced options let you customize the defaults.

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
  
## Modify an existing AWS connector

You can modify an existing AWS connector to update permissions, such as granting sensitive data discovery permissions to profile your AWS content.

The steps that you need to take depend on whether you configured your AWS environment using CloudFormation templates or manually.

### Update an existing connector using CloudFormation templates

If you set up your AWS environment using CloudFormation templates, then follow these steps to grant sensitive data discovery permissions for your existing AWS connector.

  1. In the Google Cloud console, go to **Settings**.

[Go to Settings](https://console.cloud.google.com/security/command-center/config/services)

  2. Select the organization where you activated Security Command Center Enterprise.

  3. Select **Connectors**. The **Configure connector** page opens.

  4. For the **AWS** connector, click more_vert **More options > Edit**.

  5. In the **Review data types** section, select ****Grant permissions for Sensitive Data Protection discovery****.

  6. Click **Continue**. The **Connect to AWS** page opens.

  7. Click **Download delegated role template**. The template is downloaded to your computer.

  8. Click **Download collector role template**. The template is downloaded to your computer.

  9. Click **Continue**. The **Test connector** page opens. Before you test the connector, update the stack templates in your AWS environment.




#### Update AWS stacks and stack sets

  1. In the CloudFormation console, update the stack template for the delegated role:

     1. Sign in to the [AWS delegate account console](https://console.aws.amazon.com/iam). Make sure that you're signed in to the delegate account that is used to assume other collector AWS accounts.
     2. Go to the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation) console.
     3. Replace the stack template for the delegated role with the updated delegated role template that you downloaded.

For more information, see [Update a stack's template (console)](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-get-template.html#using-cfn-updating-stacks-get-stack.CON) in the AWS documentation.

  2. Update the stack set for the collector role:

     1. Using an AWS management account or any member account that's registered as a delegated administrator, go to the [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/) console.
     2. Replace the stack set template for the collector role with the updated collector role template that you downloaded.

For more information, see [Update your stack set using the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-update.html#stacksets-update-console) in the AWS documentation.

  3. If you need to collect data from the management account, then sign in to the management account and replace the template in the collector stack with the updated collector role template that you downloaded.

This step is needed because AWS CloudFormation stack sets don't create stack instances in management accounts. For more information, see [DeploymentTargets](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentTargets.html) in the AWS documentation.




#### Verify the updated connection

  1. In the Google Cloud console, on the **Test connector** page, click **Test connector**. If the connection is successful, the test determined that the delegated role has all the required permissions to assume the collector roles. If the connection isn't successful, see Troubleshooting errors when testing the connection.
  2. Click **Save**.



### Update an existing connector manually

If you configured your AWS accounts manually when you created the AWS connector, then follow these steps to grant sensitive data discovery permissions for your existing AWS connector.

#### Update connector settings

  1. Open the **Connectors** tab on the **Settings** page.

[Go to Connectors](https://console.cloud.google.com/security/command-center/config/connectors)

  2. Select the organization where you activated Security Command Center Enterprise.

  3. For the **AWS** connector, click more_vert **More options > Edit**.

  4. In the **Review data types** section, select ****Grant permissions for Sensitive Data Protection discovery****.

  5. Click **Continue**. The **Connect to AWS** page opens.

  6. Click **Configure AWS accounts manually (recommended if you use advanced settings or customized role names)**.

  7. Copy the values of the following fields:

     * **Delegated role name**
     * **Collector role name**
     * **Sensitive Data Protection collector role name**
  8. Click **Continue**. The **Test connector** page opens. Before you test the connector, update the IAM policies in your AWS environment.




#### Update AWS IAM roles and policies

  1. In the [AWS delegate account console](https://console.aws.amazon.com/iam), update the AWS IAM policy for the delegated role to use the following JSON:
         
         {
               "Version": "2012-10-17",
               "Statement": [
                 {
                   "Action": "sts:AssumeRole",
                   "Resource": [
                     "arn:aws:iam::*:role/COLLECTOR_ROLE_NAME",
                     "arn:aws:iam::*:role/SCAN_SENSITIVE_DATA_COLLECTOR_ROLE_NAME"
                   ],
                   "Effect": "Allow"
                 },
                 {
                   "Action": [
                     "organizations:List*",
                     "organizations:Describe*"
                   ],
                   "Resource": "*",
                   "Effect": "Allow"
                 }
               ]
             }
             

Replace the following:

     * `COLLECTOR_ROLE_NAME`: the name of the configuration data collector role that you copied (the default is `aws-collector-role`)
     * `SCAN_SENSITIVE_DATA_COLLECTOR_ROLE_NAME`: the name of the Sensitive Data Protection collector role that you copied (the default is `aws-sensitive-data-protection-role`)

For more information, see [Editing customer managed policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) in the AWS documentation.

  2. For each collector account, perform these procedures:

     1. Create the AWS IAM policy for Sensitive Data Protection.

     2. Create the AWS IAM role for Sensitive Data Protection in each account.




#### Verify the updated connection

  1. In the Google Cloud console, on the **Test connector** page, click **Test connector**. If the connection is successful, the test determined that the delegated role has all the required permissions to assume the collector roles. If the connection isn't successful, see Troubleshooting errors when testing the connection.

  2. Click **Save**.




## Troubleshooting

This section describes some common problems that you might encounter when you integrate Security Command Center with AWS.

### Resources already exist

This error occurs in the AWS environment when you try to create the AWS IAM policies and AWS IAM roles, and the role already exists in your AWS account.

To resolve this issue, do the following:

  * Check whether the role or policy that you're creating already exists and satisfies the requirements listed in this guide.
  * If necessary, change the role name to avoid conflicts.



### Invalid principal in policy

This error can occur in the AWS environment when you're creating the collector roles, but the delegate role doesn't exist yet.

To resolve this issue, do the following: Create the AWS IAM policy for the delegated role and wait until the delegate role is created before continuing.

### Throttling limitations in AWS

AWS throttles API requests for each AWS account on a per-account or per-region basis. To ensure that these limits are not exceeded when Security Command Center collects asset configuration data from AWS, Security Command Center collects the data at a fixed maximum QPS for each AWS service, as described in the API documentation for the AWS service.

To resolve this issue, do the following:

  * In the [AWS connector settings page](https://console.cloud.google.com/security/command-center/config/connectors), set a custom QPS for the AWS service that is experiencing request throttling.

  * Restrict the permissions of the AWS collector role so that the data from that specific service isn't collected anymore. This mitigation technique prevents attack path simulations from working correctly for AWS.




Revoking all permissions in AWS stops the data collector process immediately. Deleting the AWS connector doesn't immediately stop the data collector process but it won't start again after it finishes.

### Finding is returned for a deleted AWS resource

After an AWS resource is deleted, it can take up to 40 hours for it to be removed from the Security Command Center asset inventory system. If you choose to resolve a finding by deleting the resource, you may see the finding reported within this time period because the asset has not yet been removed from the Security Command Center asset inventory system.

## Troubleshooting errors when testing the connection

These errors can occur when you test the connection between Security Command Center and AWS.

### AWS_FAILED_TO_ASSUME_DELEGATED_ROLE

The connection is invalid because the Google Cloud service agent can't assume the delegated role.

To resolve this issue, do the following:

  * Verify that the delegated role exists. To create it, see Create an AWS IAM role for the trust relationship between AWS and Google Cloud.

  * The inline policy of the delegated role is missing. Without it, the service agent can't assume the role. To verify that the inline policy exists, see Create an AWS IAM role for the trust relationship between AWS and Google Cloud.

  * If the error detail contains the message `InvalidIdentityToken: Incorrect token audience`, this may be caused by a separate OIDC identity provider for `accounts.google.com` in the AWS environment. To resolve this error, remove the OIDC identity provider for `accounts.google.com` in the AWS environment by following the instructions in [Creating and managing an OIDC provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html#manage-oidc-provider-console).




### AWS_FAILED_TO_CONNECT_TO_ORGNIZATIONS_SERVICE

The connection is invalid because the connection cannot connect to the AWS Organizations Service. This status is only applicable to connections with auto-discovery disabled.

To resolve this issue, do the following:

  * Verify the configuration by checking that you followed the steps in Configure your AWS environment. Confirm that the AWS IAM permissions for the delegated role are correctly configured.
  * Review the AWS Organization Setup by referring to [Troubleshooting AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_troubleshoot.html).
  * Check the AWS CloudTrail logs for specific access denied errors that are related to AWS Organizations services. This step can help you pinpoint the exact permission gap.



### AWS_FAILED_TO_LIST_ACCOUNTS

The connection is invalid because auto-discovery is enabled and the delegated role can't get all AWS accounts in the organizations.

This error indicates that the policy to allow the `organizations:ListAccounts` action on the delegated role is missing on certain resources.

To resolve this issue, do the following:

  * Verify which resources are missing. To verify the settings for the delegated policy, see Create the AWS IAM policy for the delegated role.
  * Check that you created and configured the AWS accounts as described in the Configure AWS accounts manually section.



### AWS_ACTIVE_COLLECTOR_ACCOUNTS_NOT_FOUND

The connection is invalid because no AWS collector accounts were found with the [`ACTIVE`](https://docs.aws.amazon.com/organizations/latest/APIReference/API_Account.html#organizations-Type-Account-Status) status.

If you selected **Add accounts automatically** in the **Add AWS connector accounts** field, then no AWS accounts were found with the `ACTIVE` status, excluding those specified in the **Exclude AWS connector accounts** field.

If you selected **Add accounts individually** , in the **Add AWS connector accounts** field, check that the accounts you provided have the `ACTIVE` status.

### AWS_INVALID_COLLECTOR_ACCOUNTS

The connection is invalid because there are invalid collector accounts. The error message includes more information about the possible causes, which include the following:

  * AWS_FAILED_TO_ASSUME_COLLECTOR_ROLE
  * AWS_COLLECTOR_ROLE_POLICY_MISSING_REQUIRED_PERMISSION



### AWS_FAILED_TO_ASSUME_COLLECTOR_ROLE

The collector account is invalid because the delegated role cannot assume the collector role in the collector account.

To resolve this error, consider the following:

  * Verify that the collector role exists.

    * To create the collector role for asset configuration data, see Create the AWS IAM role for asset configuration data collection in each account.
    * To create the collector role for Sensitive Data Protection, see Create the AWS IAM role for Sensitive Data Protection in each account.
  * The policy to allow the delegated role to assume the collector role is missing. To verify that the policy exists, see Create the AWS IAM policy for the delegated role.




### AWS_COLLECTOR_ROLE_POLICY_MISSING_REQUIRED_PERMISSION

The connection is invalid because the collector policy is missing some of the required permission settings.

To resolve this error, consider the following causes:

  * Some of the required AWS managed policies might not be attached to the collector role for asset configuration data. To verify that all policies are attached, see step 6 in Create the AWS IAM role for asset configuration data collection in each account.

  * One of the following issues with a collector policy might be present:

    * The collector policy might not exist.
    * The collector policy isn't attached to the collector role.
    * The collector policy doesn't include all the required permissions.

To resolve issues with a collector policy, see the following:

    * Create the AWS IAM policy for asset configuration data collection
    * Create the AWS IAM policy for Sensitive Data Protection



## What's next

  * If you're setting up Security Command Center Enterprise for the first time, [configure additional features using the setup guide](https://docs.cloud.google.com/security-command-center/docs/activate-enterprise-tier#monitor-configure-enterprise-tab).
  * You can also do the following: 
    * [Review and remediate findings](https://docs.cloud.google.com/security-command-center/docs/review-manage-findings) from AWS data.
    * [View resources](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console) related to findings in the Security Operations console.
    * View [attack path simulations for AWS resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn).
    * Map [compliance of AWS resources](https://docs.cloud.google.com/security-command-center/docs/compliance-management) with various standards and benchmarks.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
