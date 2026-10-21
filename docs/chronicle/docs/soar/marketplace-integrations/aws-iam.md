---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-iam/
title: Integrate AWS Identity and Access Management (IAM) with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:05.072630+00:00
---

# Integrate AWS Identity and Access Management (IAM) with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/aws-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate AWS Identity and Access Management (IAM) with Google SecOps

This document describes how to integrate AWS Identity and Access Management with Google Security Operations.

## Use Cases

The **AWS IAM** integration uses Google SecOps capabilities to support the following use cases:

  * **Compromised user containment** : Automatically revoke access for suspected compromised IAM users by applying inline deny policies during incident response workflows.

  * **Access revocation and privilege adjustment** : Remove users from sensitive IAM groups to immediately restrict access to critical AWS resources upon detecting anomalous behavior.

  * **Policy and group management** : Automate the creation and attachment of managed IAM policies and groups to enforce least-privilege access controls.

  * **Identity auditing and posture discovery** : Retrieve lists of users, groups, and managed policies to enrich security alerts and audit IAM configurations across your AWS environment.

  * **Automated identity provisioning** : Create IAM users and assign them to predefined functional groups as part of automated onboarding or containment remediation tasks.




## Before you begin

Before you configure the AWS IAM integration in Google SecOps, verify that your network environment and AWS credentials satisfy all operational prerequisites.

To prepare your environment for integration, make sure you complete the following:

  1. Verify network line-of-sight between Google SecOps and AWS IAM global service endpoint (`iam.amazonaws.com`).

  2. Obtain AWS programmatic API credentials (an Access Key ID and Secret Access Key) with appropriate IAM permissions.

  3. Configure and test the integration instance within Google SecOps.




### Network requirements

Google SecOps communicates directly with the AWS IAM service endpoint using HTTPS REST APIs and the AWS Python SDK (`boto3`).

Make sure your network environment meets the following connectivity rules:

  * **Outbound HTTPS access** : Enable outbound HTTPS communication from your Google SecOps instance or Remote Agent to the AWS IAM global endpoint (`iam.amazonaws.com`) over port `443/TCP`.

For more information about AWS endpoints, see [AWS Service Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in AWS documentation.

  * **Proxy configuration** : If your organization routes outbound traffic through an HTTP/HTTPS proxy, configure standard environment proxy variables (`HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY`) on the Google SecOps server or Remote Agent host.




### Authentication and credentials

The AWS IAM integration requires programmatic API credentials to authenticate requests using AWS Signature Version 4.

Make sure your AWS environment satisfies the following authentication requirements:

  * **Programmatic credentials** : Obtain a valid AWS Access Key ID and AWS Secret Key associated with an AWS IAM user or role.

For information on creating IAM identities and generating credentials, see [Managing access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) and [IAM Identities](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) in AWS documentation.

  * **Least privilege** : Restrict permissions to only the actions required for your automated workflows, and rotate credentials periodically.

For details on security recommendations, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in AWS documentation.




### Configure action permissions

Grant the authenticating AWS IAM identity the specific permissions required for the actions your Google SecOps playbooks execute.

**Important:** Most AWS IAM actions in Google SecOps execute an internal connectivity check during action initialization that calls `iam:GetAccountSummary`. Make sure that `iam:GetAccountSummary` is included in your policy to prevent action initialization errors.

Refer to the minimal permissions for **AWS IAM** actions in the following table:

Action Name | Required AWS IAM Permission (`ActionName:Permission`) | Prerequisite Permission | Description / Resource Scope  
---|---|---|---  
**Add a User to a Group** | `iam:AddUserToGroup` | `iam:GetAccountSummary` | Adds an IAM user to an IAM group. Resource: target IAM group ARN.  
**Attach a Policy** | `iam:AttachUserPolicy`  
`iam:AttachGroupPolicy`  
`iam:AttachRolePolicy` | `iam:ListPolicies` | Attaches a managed policy to an IAM user, group, or role. Requires `iam:ListPolicies` to look up policy ARNs by name.  
**Create a Group** | `iam:CreateGroup` | `iam:GetAccountSummary` | Creates a new IAM group. Resource: target IAM group ARN.  
**Create a Policy** | `iam:CreatePolicy` | `iam:GetAccountSummary` | Creates a new customer managed policy. Resource: target IAM policy ARN.  
**Create a User** | `iam:CreateUser` | `iam:GetAccountSummary` | Creates a new IAM user. Resource: target IAM user ARN.  
**Disable User Access** | `iam:PutUserPolicy` | — | Attaches an inline deny policy (`DisableUserAccessPolicy`) to revoke user access. Resource: target IAM user ARN.  
**List Groups** | `iam:ListGroups` | `iam:GetAccountSummary` | Lists IAM groups in the account. Resource: `*`.  
**List Policies** | `iam:ListPolicies` | `iam:GetAccountSummary` | Lists managed policies in the account. Resource: `*`.  
**List Users** | `iam:ListUsers` | `iam:GetAccountSummary` | Lists IAM users in the account. Resource: `*`.  
**Ping** | `iam:GetAccountSummary` | — | Validates integration connectivity. Resource: `*`.  
**Remove a User from a Group** | `iam:RemoveUserFromGroup` | `iam:GetAccountSummary` | Removes an IAM user from an IAM group. Resource: target IAM group ARN.  
  
#### Quick reference (`ActionName:Permission`)

Use the following quick reference to review the required permissions for each action:
    
    
    Ping: iam:GetAccountSummary
    Add a User to a Group: iam:AddUserToGroup, iam:GetAccountSummary
    Attach a Policy: iam:ListPolicies, iam:AttachUserPolicy, iam:AttachGroupPolicy, iam:AttachRolePolicy
    Create a Group: iam:CreateGroup, iam:GetAccountSummary
    Create a Policy: iam:CreatePolicy, iam:GetAccountSummary
    Create a User: iam:CreateUser, iam:GetAccountSummary
    Disable User Access: iam:PutUserPolicy
    List Groups: iam:ListGroups, iam:GetAccountSummary
    List Policies: iam:ListPolicies, iam:GetAccountSummary
    List Users: iam:ListUsers, iam:GetAccountSummary
    Remove a User from a Group: iam:RemoveUserFromGroup, iam:GetAccountSummary
    

### Sample IAM policy (least privilege)

The following example policy demonstrates the permissions required to run all AWS IAM actions in Google SecOps.

For instructions on creating and attaching IAM policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in AWS documentation.
    
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "SecOpsIAMDiscovery",
          "Effect": "Allow",
          "Action": [
            "iam:GetAccountSummary",
            "iam:ListUsers",
            "iam:ListGroups",
            "iam:ListPolicies"
          ],
          "Resource": "*"
        },
        {
          "Sid": "SecOpsIAMManagement",
          "Effect": "Allow",
          "Action": [
            "iam:CreateUser",
            "iam:CreateGroup",
            "iam:CreatePolicy",
            "iam:AddUserToGroup",
            "iam:RemoveUserFromGroup",
            "iam:PutUserPolicy",
            "iam:AttachUserPolicy",
            "iam:AttachGroupPolicy",
            "iam:AttachRolePolicy"
          ],
          "Resource": [
            "arn:aws:iam::*:user/*",
            "arn:aws:iam::*:group/*",
            "arn:aws:iam::*:role/*",
            "arn:aws:iam::*:policy/*"
          ]
        }
      ]
    }
    

## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AWS Access Key ID | String | N/A | Yes | AWS Access Key ID to use in integration.  
AWS Secret Key | Password | N/A | Yes | AWS Secret Key to use in integration.  
Verify SSL | Boolean | True | No | If selected, the integration validates the SSL certificate when connecting to the AWS IAM server.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add a User to a Group

Adds the specified user to the specified IAM group. Use groups to apply the same permissions policies across multiple users at once.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Group Name | String | N/A | Yes | The name of the group to update. Note: Group names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-.  
User Name | String | N/A | Yes | The name of the user to add. Note: User names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Comma separated values.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** print "Successfully added the user <User name> to the IAM group: <Group name>"
  * **If error - Group not exist or/and User not exist:**  
**_group not exist:_** Print "Could not add <UserName> to <Group name>. The Group <group name> cannot be found.  
**user not exist/both:** Print "Could not add <UserName> to <Group name>. The user <user name> cannot be found. 
  * **If error**  
**** _User limitation - IAM user can be a member of 10 groups  
_ Group limitation - 5000 users can be in a group  
****Print "Could not add <UserName> to <Group name> because it attempted to create resources beyond the current AWS account limits."

**The action should fail and stop a playbook execution:**

  * **If not successful (wrong creds, no connection, other sdk error):** print "Error executing action 'Add a User to a Group. Reason: {exception.stacktrace}

| General  
  
### Attach a Policy

Attach the specified managed policy to an identity (user, group, role).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Identity Type | DDL  
(User, Group, Role) | Group | Yes | IAM Identity type.  
Identity Name | String | N/A | Yes | The name (friendly name, not ARN) of the identity to attach the policy to. Identity names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-.  
Policy Name | String | N/A | Yes | The name (friendly name, not ARN) of the policy to attach the policy to. Policy names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** print "Policy was attached to <Identity Type>: <Identity Name>"

******The action should fail and stop a playbook execution:**

  * **If error -:** Print "Could not create <policy name> policy. Policy names must be unique within an account.
  * **If error - identity name was invalid:** Print "Could not attach <policy name> to <Identity Type>: <Identity Name>. Names must contain only alphanumeric characters and/or the following: +=,.@_-. 
  * **if not successful (wrong credentials, no connection to server, other server error):** print "Error executing action 'Attach a Policy'. Reason: {exception.stacktrace}

| General  
  
### Create a Group

Create a new IAM group for your AWS account. To set up a group, you need to create the group. Then give the group permissions based on the type of work that you expect the users in the group to do. Finally, add users to the group.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Group Name | String | N/A | Yes | Name of the group to create. Comma separated values. Note: Group names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Names must be unique within an account.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [{
       "Arn":"arn:aws:iam::582302349248:group/ZivGroup",
       "CreateDate":"2020-12-05 16:18:36+00:00",
       "Path":"/",
       "GroupId":"'AGPAYPE7MW7AMKCWMJPMX",
       "GroupName":"ZivGroup"
    }]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful (few/all group names were valid):** print "Successfully added the following groups to IAM: <Group names>"
  * **If error - group already exists:** Print "Could not add the following groups to IAM: <Group names>. Names must be unique within an account.
  * **If error (few group names were invalid):** Print "Could not add the following groups to IAM: <Group names>. Group names must contain only alphanumeric characters and/or the following: +=,.@_-. 
  * **If error (raise limitation. Max 500 groups per account):** Print "Could not add the following groups to IAM: <Group names>. Reach to Groups limitation in your aws account. 

****  
**The action should fail and stop a playbook execution:**

  * **if not successful (all names were invalid, wrong creds, no connection, other error):** print "Error executing action 'Create a Group. Reason: {exception.stacktrace}

| General  
  
### Create a Policy

Create an IAM customer managed policy for your AWS account. This action creates a policy version with a version identifier of v1and sets v1 as the policy's default version.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Policy Name | String | N/A | Yes | Name of the policy to create. Policy name can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Policy names must be unique within an account.  
Policy Document | String | N/A | Yes | The JSON policy document that you want to use as the content for the new policy.  
Description | String | N/A | No | Description of the policy.Typically used to store information about the permissions defined in the policy. For example, "Grants access to production DynamoDB tables." The policy description is immutable. After a value is assigned, it cannot be changed.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "PolicyName": "S3-read-only-bucket",
        "PolicyId": "ANPAYPE7MW7AFKUDK3HD7",
        "Arn": "arn:aws:iam::582302349248:policy/S3-read-only-bucket",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2020-12-6T17:16:45",
        "UpdateDate": "2020-12-6T17:16:45"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** print "<Policy name> policy was successfully created"

The action should fail and stop a playbook execution:

  * **If error - Policy already exists:** Print "Could not create <policy name> policy. Policy names must be unique within an account.
  * **If error - policy name was invalid:** Print "Could not create <policy name> policy. Policy names must contain only alphanumeric characters and/or the following: +=,.@_-. 
  * **If error - Policy doc was malformed :** Print "Could not create <policy name> policy. The policy document was malformed.Reason: {exception.stacktrace}

**if not successful (LimitExceededException, wrong creds, no connection, other error):** print "Error executing action 'Create a Policy'. Reason: {exception.stacktrace} | General  
  
### Create a User

Create a new IAM user for your AWS account. You can add multiple users at once with comma separated values. Please note that no policies will be applied at this stage.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
User Name | String | N/A | Yes | Name of the user to create. Comma separated values. Note: Username can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Names must be unique within an account.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [{
       "Arn":"arn:aws:iam::582302349248:user/ziv",
       "CreateDate":"2020-12-03T12:12:20",
       "Path":"/",
       "UserId":"AIDAYPE7MW7AFMHK4WCHS",
       "UserName":"ziv"
    }]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful (few usernames were valid):** print "Successfully added the following users to IAM: <User names>"
  * **If error - users already exists:** Print "Could not add the following users to IAM: <Usernames>. Names must be unique within an account.
  * **If error (few usernames were invalid):** Print "Could not add the following users to IAM: <Usernames>. Usernames must contain only **alphanumeric characters and/or the following: +=,.@_-._**
  * **If error (raise limitation. Max 5000 users per account):** Print "Could not add the following users to IAM: <Usernames>. Reach to Users limitation in your aws account. 

**Note:** If nothing happened: all users are invalid/exists/limit → action should failed**The action should fail and stop a playbook execution:**

  * **If not successful (all usernames were invalid, wrong creds, no connection, other error):** print "Error executing action 'Create a User'. Reason: {exception.stacktrace}

**Note:** In case of all usernames were invalid, print " "Error executing action 'Create a User'. Reason: {invalid usernames}: Usernames must contain only alphanumeric characters and/or the following: +=,.@-. {existing usernames}: Names must be unique within an account. | General  
  
### Disable User Access

Disable user access in AWS by adding an explicit inline deny policy. 

This action only supports regular AWS users, not federated users or IAM roles.

#### Entities

This action runs on the User entity.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | Available  
Script result | Available  
  
##### JSON result
    
    
    [
      {
        "Entity": "//iam.googleapis.com/projects/example/serviceAccounts/service-account@example.iam.gserviceaccount.com",
        "EntityResult": [
          {
            "fullResourceName": "//iam.googleapis.com/projects/example/serviceAccounts/service-account@example.iam.gserviceaccount.com",
            "activityType": "serviceAccountLastAuthentication",
            "observationPeriod": {
              "startTime": "2023-05-23T07:00:00Z",
              "endTime": "2023-08-20T07:00:00Z"
            },
            "activity": {
              "lastAuthenticatedTime": "2023-08-20T07:00:00Z",
              "serviceAccount": {
                "serviceAccountId": "example-account-id",
                "projectNumber": "example-project-id",
                "fullResourceName": "//iam.googleapis.com/projects/example/serviceAccounts/service-account@example.iam.gserviceaccount.com"
              }
            }
          }
        ]
      }
    ]
    

##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### Case wall

The action provides the following output messages:

Output message | Message description  
---|---  
`Successfully added deny policy to the following users in AWS IAM: USERNAME_LIST` `Action wasn't able to find the following users in AWS IAM: USERNAME_LIST` `Action wasn't able to add deny policy to the following users in AWS IAM: USERNAME_LIST` | Action succeeded.  
`Successfully added deny policy to the following users in AWS IAM: USERNAME_LIST` | Action failed.Error prevented applying the deny policy to at least one provided user.  
`Error executing action "Disable User Access". Reason: ERROR_REASON` | Action failed.Check connection to the server, input parameters, or credentials.  
  
### List Groups

Get a list of all groups in the IAM.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Max Groups to Return | Integer | 50 | No | Specify how many groups to return. Maximum is 1000 groups. Default is 50.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [{
       "Arn":"arn:aws:iam::582302349248:group/ZivGroup",
       "CreateDate":"2020-12-05 16:18:36+00:00",
       "Path":"/",
       "GroupId":"AGPAYPE7MW7AMKCWMJPMX",
       "GroupName":"ZivGroup"
    }]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **The action should not fail nor stop a playbook execution:****if successful:** print "Successfully listed available groups in AWS IAM"**If no data available:** Print "No Groups found in AWS IAM"****  
**The action should fail and stop a playbook execution:****if not successful (wrong credentials, no connection to server, other server error, If 'Max Groups' > 1000):** print "Error executing action 'List Groups'. Reason: {exception.stacktrace} | General  
CSV Table | **Title:** IAM Groups**Columns:** Group nameGroup IDARNCreation Date | General  
  
### List Policies

List all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies. You can filter the list of policies that are returned using the optional Only Attached, Scope, and Policy Usage parameters. For example, to list only the customer managed policies in your AWS account, set Scope to Local. To list only AWS managed policies, set Scope to AWS.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Only Attached | Boolean | No | No | When checked, filtering the results to only the policies that are attached to an IAM user, group or role. When unchecked, all policies will be returned.  
Scope | DDL  
(All, AWS, Local) | All | No | The scope to use for filtering the results. To list only AWS managed policies, set Scope to AWS. To list only the customer managed policies in your AWS account, set Scope to Local. As default, all policies will be returned.  
Max Policies to Return | Integer | 100 | No | Specify how many policies to return. Default is 100. Maximum is 1000.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [{
    'PolicyName': 'string',
    'PolicyId': 'string',
    'Arn': 'string',
    'Path': 'string',
    'DefaultVersionId': 'string',
    'AttachmentCount': 123,
    'PermissionsBoundaryUsageCount': 123,
    'IsAttachable': True|False,
    'Description': 'string',
    'CreateDate': "2020-12-6T17:16:45",
    'UpdateDate':"2020-12-6T17:16:45"
    }]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** print "Successfully listed available policies in AWS IAM"
  * **If 'Max Policies' value < matched policies based on the filter:** Print "Successfully listed available policies in AWS IAM. Please note, there are additional policies that match the provided filter."
  * **If no data:** Print "No Policies were found in AWS IAM"

****  
**The action should fail and stop a playbook execution:**

  * **if not successful (wrong credentials, no connection to server, other server error, max >1000):** print "Error executing action 'List Policies. Reason: {exception.stacktrace}

| General  
CSV Table | **Title:** IAM Policies**Columns:** Policy NamePolicy IDCreate DateUpdate Date | General  
  
### List Users

Get a list of all users in the IAM.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Max Users to Return | Integer | 50 | No | Specify how many users to return. Maximum is 1000 users. Default is 50.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [{
       "Arn":"arn:aws:iam::582302349248:user/ziv",
       "CreateDate":"2020-12-03T12:12:20",
       "Path":"/",
       "UserId":"AIDAYPE7MW7AFMHK4WCHS",
       "UserName":"ziv"
    }]
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful:** print "Successfully listed available users in AWS IAM"**If no data available:** Print "No users found in AWS IAM"****  
**The action should fail and stop a playbook execution:****if not successful (wrong credentials, no connection to server, other server error, if max >10000):** print "Error executing action 'List Users'. Reason: {exception.stacktrace} | General  
CSV Table | **Title:** IAM Users**Columns:** UsernameUser IDARNCreation Date | General  
  
### Ping

Test connectivity to AWS IAM with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful:** print "Successfully connected to the AWS IAM server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:****if not successful:** print "Failed to connect to the AWS IAM server! Error is {0}".format(exception.stacktrace) | General  
  
### Remove a User from a Group

Adds the specified user to the specified IAM group. Use groups to apply the same permissions policies across multiple users at once.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Group Name | String | N/A | Yes | The name of the group to update. Note: Group names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-.  
User Name | String | N/A | Yes | The name of the user to remove. Note: User names can not include spaces and must contain only alphanumeric characters and/or the following: +=.@_-. Comma separated values.  
  
This action doesn't run on Google SecOps entities. 

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** print "<User name> has been removed from group: <Group name>"
  * **If error - Group not exist or/and User not exist:**  
**_group not exist:_** Print "Could not remove <UserName> from <Group name>. The Group <group name> cannot be found.  
**user not exist/both:** Print "Could not remove <UserName> from <Group name>. The user <user name> cannot be found. 
  * **If error**  
**** _User limitation - IAM user can be a member of 10 groups  
_ Group limitation - 5000 users can be in a group  
****Print "Could not remove <UserName> from <Group name> because it attempted to create resources beyond the current AWS account limits."

**The action should fail and stop a playbook execution:**

  * **If not successful (wrong creds, no connection, other sdk error):** print "Error executing action 'Remove a User from a Group. Reason: {exception.stacktrace}

| General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
