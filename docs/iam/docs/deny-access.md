---
url: https://docs.cloud.google.com/iam/docs/deny-access/
title: Deny access to resources \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:48.205385+00:00
---

# Deny access to resources  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/deny-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Deny access to resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to deny principals access by preventing them from using specific Identity and Access Management (IAM) permissions.

In IAM, you deny access with _deny policies_. Each deny policy is attached to a Google Cloud organization, folder, or project. A deny policy contains _deny rules_ , which identify principals and list the permissions that the principals cannot use.

Deny policies are separate from _allow policies_ , also known as _IAM policies_. An allow policy provides access to resources by granting IAM roles to principals.

You can manage deny policies with the Google Cloud console, Google Cloud CLI, or the IAM `v2` REST API.

## Before you begin

  * Enable the IAM API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Node.js

To use the Node.js samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  * Read the [overview of deny policies](https://docs.cloud.google.com/iam/docs/deny-overview).




### Required roles

To get the permissions that you need to manage deny policies, ask your administrator to grant you the following IAM roles on the organization: 

  * To view deny policies: [Deny Reviewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyReviewer) (`roles/iam.denyReviewer`) 
  * To view, create, update, and delete deny policies: [Deny Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.denyAdmin) (`roles/iam.denyAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage deny policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage deny policies:

  * To view deny policies: 
    * `iam.denypolicies.get`
    * `iam.denypolicies.list`
  * To create, update, and delete deny policies: 
    * `iam.denypolicies.create`
    * `iam.denypolicies.delete`
    * `iam.denypolicies.get`
    * `iam.denypolicies.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Identify permissions to deny

Before you create a deny policy, you must decide which permissions you want to deny, and which principals should be denied these permissions.

Only some permissions can be denied. For a list of permissions that you can deny, see [Permissions supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).

In some cases, you can also use permission groups to deny sets of permissions. For more information, see [Permission groups](https://docs.cloud.google.com/iam/docs/deny-overview#permission-groups).

You manage deny policies with the `v2` REST API, which requires a special format for permission names. For example, the permission to create an IAM custom role is named as follows:

  * `v1` API: `iam.roles.create`
  * `v2` API: `iam.googleapis.com/roles.create`



## Create a deny policy

You can add deny policies to organizations, folders, and projects. Each resource can have up to 500 deny policies.

Deny policies contain deny rules, which specify the following:

  * The permissions to deny.
  * The principals that are denied those permissions.
  * Optional: Principals that are exempt from the denial of permissions.

For example, you can deny a permission to a group, but exempt specific users who belong to that group.

  * Optional: A [condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview) that specifies when the principals cannot use the permissions. In deny policies, condition expressions can only use functions for [resource tags](https://docs.cloud.google.com/iam/docs/tags-access-control)—other functions and operators are not supported.




Each resource can have up to 500 deny rules across all of its attached deny policies.

Deny policies are inherited through the [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#resource-hierarchy). For example, if you deny a permission at the organization level, that permission will also be denied on the folders and projects within that organization, and on the service-specific resources within each project.

Deny policies override allow policies. If a principal is granted a role that contains a specific permission, but a deny policy says that the principal cannot use that permission, then the principal cannot use the permission.

**Note:** In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

### Console

  1. In the Google Cloud console, go to the **Deny** tab on the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam/deny?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Click add_box **Create deny policy**.

  4. In the **Policy name** section, define the policy ID by doing one of the following:

     * In the **Display name** field, enter a display name for the policy. Filling out this field automatically fills out the **ID** field. If you want to change the ID of the policy, update the text in the **ID** field.
     * In the **ID** field, enter an ID for the policy.
  5. In the **Deny rules** section, define the policy's deny rules. Each deny policy must have at least one deny rule. To add additional deny rules, click **Add deny rule**.

For each deny rule, do the following:

     1. In the **Denied principals** field, add one or more principals that you want to prevent from using the specified permissions. The principal can be any of the principal types in the [principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny), except the principals whose IDs begin with `deleted:`.
     2. Optional: In the **Exception principals** field, add the principals that you want to be able to use the specified permissions, even if those principals are included in **Denied principals** section. For example, you can use this field to make an exception for specific users who belong to a denied group.

**Note** : If a principal set in the list of denied principals includes [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)—for example, the principal set `principalSet://goog/public:all`—then we recommend adding your service agents as exceptions in the deny rule. This helps ensure that your services continue to function properly. When adding service agents as exceptions, use the project, folder, or organization's [service agent principal set](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny-service-agent-principal-sets). 

     3. In the **Denied permissions** sections, add the permissions that you want to deny. The permissions must be [supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).

In some cases, you can also use permission groups to deny sets of permissions. For more information, see [Permission groups](https://docs.cloud.google.com/iam/docs/deny-overview#permission-groups).

     4. Optional: Add exception permissions. Exception permissions are permissions that you don't want this deny rule to deny, even if they're included in the list of denied permissions. For example, you can use this field to make exceptions for specific permissions in a permission group.

To add exception permissions, click **Exception permissions** , click add **Add another permission** , and then enter the permission in the **Permission 1** field. Continue adding permissions until you've added all permissions that you want to exempt from the deny policy.

     5. Optional: Add a denial condition to specify when the principals can't use the permission. To add a denial condition, click add **Add denial condition** , and then define the following fields:

        * **Title** : Optional. A brief summary of the purpose of the condition.
        * **Description** : Optional. A longer description of the condition.
        * Condition expression: You can add a condition expression using the **Condition builder** or **Condition editor**. The condition builder provides an interactive interface to select your desired condition type, operator, and other applicable details about the expression. The condition editor provides a text-based interface to manually enter an expression using [Common Expression Language (CEL) syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel).

Denial conditions must be based on [resource tags](https://docs.cloud.google.com/iam/docs/tags-access-control). Other functions and operators aren't supported.

  6. Click **Create**.




### gcloud

To create a deny policy for a resource, start by creating a JSON file that contains the policy. A deny policy uses the following format:
    
    
    {
      "displayName": "POLICY_NAME",
      "rules": [
        {
          "denyRule": DENY_RULE_1
        },
        {
          "denyRule": DENY_RULE_2
        },
        {
          "denyRule": DENY_RULE_N
        }
      ]
    }

Provide the following values:

  * `POLICY_NAME`: The display name for the deny policy.
  * `DENY_RULE_1`, `DENY_RULE_2`, `...DENY_RULE_N`: The deny rules in the policy. Each deny rule can contain these fields: 

    * `deniedPermissions`: A list of permissions that the specified principals cannot use. The permissions must be [supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support). 

In some cases, you can also use permission groups to deny sets of permissions. For more information, see [Permission groups](https://docs.cloud.google.com/iam/docs/deny-overview#permission-groups). 

    * `exceptionPermissions`: A list of permissions that the specified principals can use, even if those permissions are included in `deniedPermissions`. For example, you can use this field to make exceptions for specific permissions in a group of permissions. 
    * `deniedPrincipals`: A list of principals that cannot use the specified permissions. To learn how to format the principal identifiers, see [Principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny). 
    * `exceptionPrincipals`: Optional. A list of principals that can use the specified permissions, even if those principals are included in `deniedPrincipals`. For example, you can use this field to make an exception for specific users who belong to a denied group. To learn how to format the principal identifiers, see [Principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny).

**Note** : If a principal set in the list of denied principals includes [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)—for example, the principal set `principalSet://goog/public:all`—then we recommend adding your service agents as exceptions in the deny rule. This helps ensure that your services continue to function properly. When adding service agents as exceptions, use the project, folder, or organization's [service agent principal set](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny-service-agent-principal-sets). 
    * `denialCondition`: Optional. A [condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview) that specifies when the principals cannot use the permissions. Contains the following fields: 

      * `expression`: A condition expression that uses [Common Expression Language (CEL) syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel). The expression must use the [CEL functions for evaluating resource tags](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags). Other functions and operators are not supported. 
      * `title`: Optional. A brief summary of the purpose of the condition. 
      * `description`: Optional. A longer description of the condition. 

For examples of deny rules, see [Common use cases](https://docs.cloud.google.com/iam/docs/deny-overview#use-cases). 




For example, the following deny policy contains one deny rule, which denies one permission to Lucian:
    
    
    {
      "displayName": "My deny policy.",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principal://goog/subject/lucian@example.com"
            ],
            "deniedPermissions": [
              "iam.googleapis.com/roles.create"
            ]
          }
        }
      ]
    }
    

Next, run the [`gcloud iam policies create`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/create) command:
    
    
    gcloud iam policies create POLICY_ID \
        --attachment-point=ATTACHMENT_POINT \
        --kind=denypolicies \
        --policy-file=POLICY_FILE

Provide the following values:

  * `POLICY_ID`: The identifier for the deny policy.

  * `ATTACHMENT_POINT`: An identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).

  * `POLICY_FILE`: The filepath for the JSON file that contains the deny policy.




By default, if this command succeeds, it does not print any output. To print a detailed response, add the flag `--format=json` to the command.

For example, the following command creates a deny policy named `my-deny-policy` for the project `my-project`, using a file named `policy.json`:
    
    
    gcloud iam policies create my-deny-policy \
        --attachment-point=cloudresourcemanager.googleapis.com/projects/my-project \
        --kind=denypolicies \
        --policy-file=policy.json
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 
    
    
    data "google_project" "default" {
    }
    
    # Create a service account
    resource "google_service_account" "default" {
      display_name = "IAM Deny Example - Service Account"
      account_id   = "example-sa"
      project      = data.google_project.default.project_id
    }
    
    # Create an IAM deny policy that denies a permission for the service account
    resource "google_iam_deny_policy" "default" {
      provider     = google-beta
      parent       = urlencode("cloudresourcemanager.googleapis.com/projects/${data.google_project.default.project_id}")
      name         = "my-deny-policy"
      display_name = "My deny policy."
      rules {
        deny_rule {
          denied_principals  = ["principal://iam.googleapis.com/projects/-/serviceAccounts/${google_service_account.default.email}"]
          denied_permissions = ["iam.googleapis.com/roles.create"]
        }
      }
    }

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    	"cloud.google.com/go/iam/apiv2/iampb"
    
    	"google.golang.org/genproto/googleapis/type/expr"
    )
    
    // createDenyPolicy creates a deny policy.
    func createDenyPolicy(w io.Writer, projectID, policyID string) error {
    	// You can add deny policies to organizations, folders, and projects.
    	// Each of these resources can have up to 5 deny policies.
    	// Deny policies contain deny rules, which specify the following:
    	// 1. The permissions to deny and/or exempt.
    	// 2. The principals that are denied, or exempted from denial.
    	// 3. An optional condition on when to enforce the deny rules.
    
    	// projectID := "your_project_id"
    	// policyID := "your_policy_id"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	denyRule := &iampb.DenyRule{
    		// Add one or more principals who should be denied the permissions specified in this rule.
    		// For more information on allowed values,
    		// see: https://cloud.google.com/iam/help/deny/principal-identifiers
    		DeniedPrincipals: []string{"principalSet://goog/public:all"},
    		// Optionally, set the principals who should be exempted from the
    		// list of denied principals. For example, if you want to deny certain permissions
    		// to a group but exempt a few principals, then add those here.
    		// ExceptionPrincipals: []string{"principalSet://goog/group/project-admins@example.com"},
    		//
    		// Set the permissions to deny.
    		// The permission value is of the format: service_fqdn/resource.action
    		// For the list of supported permissions,
    		// see: https://cloud.google.com/iam/help/deny/supported-permissions
    		DeniedPermissions: []string{"cloudresourcemanager.googleapis.com/projects.delete"},
    		// Optionally, add the permissions to be exempted from this rule.
    		// Meaning, the deny rule will not be applicable to these permissions.
    		// ExceptionPermissions: []string{"cloudresourcemanager.googleapis.com/projects.create"},
    		//
    		// Set the condition which will enforce the deny rule.
    		// If this condition is true, the deny rule will be applicable.
    		// Else, the rule will not be enforced.
    		// The expression uses Common Expression Language syntax (CEL).
    		// Here we block access based on tags.
    		//
    		// Here, we create a deny rule that denies the
    		// cloudresourcemanager.googleapis.com/projects.delete permission
    		// to everyone except project-admins@example.com for resources that are tagged test.
    		// A tag is a key-value pair that can be attached to an organization, folder, or project.
    		// For more info, see: https://cloud.google.com/iam/docs/deny-access#create-deny-policy
    		DenialCondition: &expr.Expr{
    			Expression: "!resource.matchTag('12345678/env', 'test')",
    		},
    	}
    
    	// Add the deny rule and a description for it.
    	policyRule := &iampb.PolicyRule{
    		Description: "block all principals from deleting projects, unless the principal is a member of project-admins@example.com and the project being deleted has a tag with the value test",
    		Kind: &iampb.PolicyRule_DenyRule{
    			DenyRule: denyRule,
    		},
    	}
    
    	policy := &iampb.Policy{
    		DisplayName: "Restrict project deletion access",
    		Rules:       [](*iampb.PolicyRule){policyRule},
    	}
    
    	req := &iampb.CreatePolicyRequest{
    		// Construct the full path of the resource's deny policies.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies"
    		Parent:   fmt.Sprintf("policies/%s/denypolicies", attachmentPoint),
    		Policy:   policy,
    		PolicyId: policyID,
    	}
    	op, err := policiesClient.CreatePolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to create policy: %w", err)
    	}
    
    	policy, err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Policy %s created\n", policy.GetName())
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.iam.v2.[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.CreatePolicyRequest.html);
    import com.google.iam.v2.[DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html);
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import com.google.iam.v2.[PolicyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import com.google.type.[Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateDenyPolicy {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // Specify the id of the Deny policy you want to create.
        String policyId = "deny-policy-id";
    
        createDenyPolicy(projectId, policyId);
      }
    
      // Create a deny policy.
      // You can add deny policies to organizations, folders, and projects.
      // Each of these resources can have up to 5 deny policies.
      //
      // Deny policies contain deny rules, which specify the following:
      // 1. The permissions to deny and/or exempt.
      // 2. The principals that are denied, or exempted from denial.
      // 3. An optional condition on when to enforce the deny rules.
      public static void createDenyPolicy(String projectId, String policyId)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached.
          // Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
          String policyParent = String.format("policies/%s/denypolicies", attachmentPoint);
    
          [DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html) denyRule =
              [DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html).newBuilder()
                  // Add one or more principals who should be denied the permissions specified in this
                  // rule.
                  // For more information on allowed values, see:
                  // https://cloud.google.com/iam/docs/principal-identifiers
                  .[addDeniedPrincipals](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.Builder.html#com_google_iam_v2_DenyRule_Builder_addDeniedPrincipals_java_lang_String_)("principalSet://goog/public:all")
    
                  // Optionally, set the principals who should be exempted from the
                  // list of denied principals. For example, if you want to deny certain permissions
                  // to a group but exempt a few principals, then add those here.
                  // .addExceptionPrincipals(
                  //     "principalSet://goog/group/project-admins@example.com")
    
                  // Set the permissions to deny.
                  // The permission value is of the format: service_fqdn/resource.action
                  // For the list of supported permissions, see:
                  // https://cloud.google.com/iam/help/deny/supported-permissions
                  .[addDeniedPermissions](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.Builder.html#com_google_iam_v2_DenyRule_Builder_addDeniedPermissions_java_lang_String_)("cloudresourcemanager.googleapis.com/projects.delete")
    
                  // Optionally, add the permissions to be exempted from this rule.
                  // Meaning, the deny rule will not be applicable to these permissions.
                  // .addExceptionPermissions("cloudresourcemanager.googleapis.com/projects.create")
    
                  // Set the condition which will enforce the deny rule. If this condition is true,
                  // the deny rule will be applicable. Else, the rule will not be enforced.
                  .[setDenialCondition](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.Builder.html#com_google_iam_v2_DenyRule_Builder_setDenialCondition_com_google_type_Expr_)(
                      [Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html).newBuilder()
                          // The expression uses Common Expression Language syntax (CEL).
                          // Here we block access based on tags.
                          //
                          // A tag is a key-value pair that can be attached to an organization, folder,
                          // or project. You can use deny policies to deny permissions based on tags
                          // without adding an IAM Condition to every role grant.
                          // For example, imagine that you tag all of your projects as dev, test, or
                          // prod. You want only members of project-admins@example.com to be able to
                          // perform operations on projects that are tagged prod.
                          // To solve this problem, you create a deny rule that denies the
                          // cloudresourcemanager.googleapis.com/projects.delete permission to everyone
                          // except project-admins@example.com for resources that are tagged test.
                          .[setExpression](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setExpression_java_lang_String_)("!resource.matchTag('12345678/env', 'test')")
                          .[setTitle](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setTitle_java_lang_String_)("Only for test projects")
                          .build())
                  .build();
    
          // Add the deny rule and a description for it.
          [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) policy =
              [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html).newBuilder()
                  // Set the deny rule.
                  .[addRules](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.Builder.html#com_google_iam_v2_Policy_Builder_addRules_com_google_iam_v2_PolicyRule_)(
                      [PolicyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.html).newBuilder()
                          // Set a description for the rule.
                          .setDescription(
                              "block all principals from deleting projects, unless the principal"
                                  + " is a member of project-admins@example.com and the project"
                                  + " being deleted has a tag with the value test")
                          .[setDenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.Builder.html#com_google_iam_v2_PolicyRule_Builder_setDenyRule_com_google_iam_v2_DenyRule_)(denyRule)
                          .build())
                  .build();
    
          // Set the policy resource path, policy rules and a unique ID for the policy.
          [CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.CreatePolicyRequest.html) createPolicyRequest =
              [CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.CreatePolicyRequest.html).newBuilder()
                  .setParent(policyParent)
                  .setPolicy(policy)
                  .[setPolicyId](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.CreatePolicyRequest.Builder.html#com_google_iam_v2_CreatePolicyRequest_Builder_setPolicyId_java_lang_String_)(policyId)
                  .build();
    
          // Build the create policy request.
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) operation =
              policiesClient
                  .[createPolicyCallable](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html#com_google_iam_v2_PoliciesClient_createPolicyCallable__)()
                  .futureCall(createPolicyRequest)
                  .get(3, TimeUnit.MINUTES);
    
          // Wait for the operation to complete.
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in creating the policy " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          // Retrieve the policy name.
          [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) response = policiesClient.getPolicy(String.format("%s/%s", policyParent, policyId));
          String policyName = response.[getName](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html#com_google_iam_v2_Policy_getName__)();
          System.out.println(
              "Created the deny policy: " + policyName.substring(policyName.lastIndexOf("/") + 1));
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const policyID = 'YOUR_POLICY_ID';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    const denyRule = {
      // Add one or more principals who should be denied the permissions specified in this rule.
      // For more information on allowed values, see: https://cloud.google.com/iam/help/deny/principal-identifiers
      deniedPrincipals: ['principalSet://goog/public:all'],
      // Optionally, set the principals who should be exempted from the
      // list of denied principals. For example, if you want to deny certain permissions
      // to a group but exempt a few principals, then add those here.
      // exceptionPrincipals: ['principalSet://goog/group/project-admins@example.com'],
      // Set the permissions to deny.
      // The permission value is of the format: service_fqdn/resource.action
      // For the list of supported permissions, see: https://cloud.google.com/iam/help/deny/supported-permissions
      deniedPermissions: ['cloudresourcemanager.googleapis.com/projects.delete'],
      // Optionally, add the permissions to be exempted from this rule.
      // Meaning, the deny rule will not be applicable to these permissions.
      // exceptionPermissions: ['cloudresourcemanager.googleapis.com/projects.create']
      //
      // Set the condition which will enforce the deny rule.
      // If this condition is true, the deny rule will be applicable. Else, the rule will not be enforced.
      // The expression uses Common Expression Language syntax (CEL).
      // Here we block access based on tags.
      //
      // Here, we create a deny rule that denies the cloudresourcemanager.googleapis.com/projects.delete permission to everyone except project-admins@example.com for resources that are tagged test.
      // A tag is a key-value pair that can be attached to an organization, folder, or project.
      // For more info, see: https://cloud.google.com/iam/docs/deny-access#create-deny-policy
      denialCondition: {
        expression: '!resource.matchTag("12345678/env", "test")',
      },
    };
    
    async function createDenyPolicy() {
      const request = {
        parent: `policies/${attachmentPoint}/denypolicies`,
        policy: {
          displayName: 'Restrict project deletion access',
          rules: [
            {
              description:
                'block all principals from deleting projects, unless the principal is a member of project-admins@example.com and the project being deleted has a tag with the value test',
              denyRule,
            },
          ],
        },
        policyId,
      };
    
      const [operation] = await iamClient.createPolicy(request);
      const [policy] = await operation.promise();
    
      console.log(`Created the deny policy: ${policy.name}`);
    }
    
    createDenyPolicy();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    def create_deny_policy(project_id: str, policy_id: str) -> None:
        """Create a deny policy.
    
        You can add deny policies to organizations, folders, and projects.
        Each of these resources can have up to 5 deny policies.
    
        Deny policies contain deny rules, which specify the following:
        1. The permissions to deny and/or exempt.
        2. The principals that are denied, or exempted from denial.
        3. An optional condition on when to enforce the deny rules.
    
        Params:
        project_id: ID or number of the Google Cloud project you want to use.
        policy_id: Specify the ID of the deny policy you want to create.
        """
    
        from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
        from google.cloud.iam_v2 import types
    
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name. Hence, replace
        # the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        deny_rule = types.[DenyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.DenyRule.html)()
        # Add one or more principals who should be denied the permissions specified in this rule.
        # For more information on allowed values, see: https://cloud.google.com/iam/help/deny/principal-identifiers
        deny_rule.denied_principals = ["principalSet://goog/public:all"]
    
        # Optionally, set the principals who should be exempted from the
        # list of denied principals. For example, if you want to deny certain permissions
        # to a group but exempt a few principals, then add those here.
        # deny_rule.exception_principals = ["principalSet://goog/group/project-admins@example.com"]
    
        # Set the permissions to deny.
        # The permission value is of the format: service_fqdn/resource.action
        # For the list of supported permissions, see: https://cloud.google.com/iam/help/deny/supported-permissions
        deny_rule.denied_permissions = [
            "cloudresourcemanager.googleapis.com/projects.delete"
        ]
    
        # Optionally, add the permissions to be exempted from this rule.
        # Meaning, the deny rule will not be applicable to these permissions.
        # deny_rule.exception_permissions = ["cloudresourcemanager.googleapis.com/projects.create"]
    
        # Set the condition which will enforce the deny rule.
        # If this condition is true, the deny rule will be applicable. Else, the rule will not be enforced.
        # The expression uses Common Expression Language syntax (CEL).
        # Here we block access based on tags.
        #
        # Here, we create a deny rule that denies the cloudresourcemanager.googleapis.com/projects.delete permission to everyone except project-admins@example.com for resources that are tagged test.
        # A tag is a key-value pair that can be attached to an organization, folder, or project.
        # For more info, see: https://cloud.google.com/iam/docs/deny-access#create-deny-policy
        deny_rule.denial_condition = {
            "expression": "!resource.matchTag('12345678/env', 'test')"
        }
    
        # Add the deny rule and a description for it.
        policy_rule = types.[PolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.PolicyRule.html)()
        policy_rule.description = "block all principals from deleting projects, unless the principal is a member of project-admins@example.com and the project being deleted has a tag with the value test"
        policy_rule.deny_rule = deny_rule
    
        policy = types.[Policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy.html)()
        policy.display_name = "Restrict project deletion access"
        policy.rules = [policy_rule]
    
        # Set the policy resource path, policy rules and a unique ID for the policy.
        request = types.[CreatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.CreatePolicyRequest.html)()
        # Construct the full path of the resource's deny policies.
        # Its format is: "policies/{attachmentPoint}/denypolicies"
        request.parent = f"policies/{attachment_point}/denypolicies"
        request.policy = policy
        request.policy_id = policy_id
    
        # Build the create policy request and wait for the operation to complete.
        result = policies_client.[create_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_create_policy)(request=request).result()
        print(f"Created the deny policy: {result.name.rsplit('/')[-1]}")
    
    
    if __name__ == "__main__":
        import uuid
    
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
    
        # Test the policy lifecycle.
        create_deny_policy(PROJECT_ID, policy_id)

### REST

The `[policies.createPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/createPolicy)` method creates a deny policy for a resource. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 

  * `POLICY_ID`: An identifier for the deny policy. 
  * `POLICY_NAME`: The display name for the deny policy. 
  * `DENY_RULE_1`, `DENY_RULE_2`, `...DENY_RULE_N`: The deny rules in the policy. Each deny rule can contain these fields: 

    * `deniedPermissions`: A list of permissions that the specified principals cannot use. The permissions must be [supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support). 

In some cases, you can also use permission groups to deny sets of permissions. For more information, see [Permission groups](https://docs.cloud.google.com/iam/docs/deny-overview#permission-groups). 

    * `exceptionPermissions`: A list of permissions that the specified principals can use, even if those permissions are included in `deniedPermissions`. For example, you can use this field to make exceptions for specific permissions in a group of permissions. 
    * `deniedPrincipals`: A list of principals that cannot use the specified permissions. To learn how to format the principal identifiers, see [Principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny). 
    * `exceptionPrincipals`: Optional. A list of principals that can use the specified permissions, even if those principals are included in `deniedPrincipals`. For example, you can use this field to make an exception for specific users who belong to a denied group. To learn how to format the principal identifiers, see [Principal identifiers for deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny).

**Note** : If a principal set in the list of denied principals includes [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents)—for example, the principal set `principalSet://goog/public:all`—then we recommend adding your service agents as exceptions in the deny rule. This helps ensure that your services continue to function properly. When adding service agents as exceptions, use the project, folder, or organization's [service agent principal set](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny-service-agent-principal-sets). 
    * `denialCondition`: Optional. A [condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview) that specifies when the principals cannot use the permissions. Contains the following fields: 

      * `expression`: A condition expression that uses [Common Expression Language (CEL) syntax](https://docs.cloud.google.com/iam/docs/conditions-overview#cel). The expression must use the [CEL functions for evaluating resource tags](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags). Other functions and operators are not supported. 
      * `title`: Optional. A brief summary of the purpose of the condition. 
      * `description`: Optional. A longer description of the condition. 

For examples of deny rules, see [Common use cases](https://docs.cloud.google.com/iam/docs/deny-overview#use-cases). 




HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies?policyId=POLICY_ID

Request JSON body: 
    
    
    {
      "displayName": "POLICY_NAME",
      "rules": [
        {
          "denyRule": DENY_RULE_1
        },
        {
          "denyRule": DENY_RULE_2
        },
    
        {
          "denyRule": DENY_RULE_N
        }
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies?policyId=POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies?policyId=POLICY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/createPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy/operations/89cb3e508bf1ff01",
      "metadata": {
        "@type": "type.googleapis.com/google.iam.v2.PolicyOperationMetadata",
        "createTime": "2022-06-28T19:06:12.455151Z"
      },
      "response": {
        "@type": "type.googleapis.com/google.iam.v2.Policy",
        "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
        "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
        "kind": "DenyPolicy",
        "displayName": "My deny policy.",
        "etag": "MTc3NDU4MjM4OTY0MzU5MjQ5OTI=",
        "createTime": "2022-06-28T19:06:12.455151Z",
        "updateTime": "2022-06-28T22:26:21.968687Z"
        "rules": [
          {
            "denyRule": {
              "deniedPrincipals": [
                "principal://goog/subject/lucian@example.com"
              ],
              "deniedPermissions": [
                "iam.googleapis.com/roles.create"
              ]
            }
          }
        ]
      }
    }
    

The response identifies a long-running operation. You can monitor the status of the long-running operation to find out when it's complete. For details, see Check the status of a long-running operation on this page. 

**Note:** When you use an email alias in a deny policy, IAM automatically replaces the alias with the user's primary email address. 

## List deny policies

A resource can have multiple deny policies. You can list all of the deny policies that are attached to a resource, and then view each deny policy to see the deny rules in each policy.

### Console

  1. In the Google Cloud console, go to the **Deny** tab on the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam/deny?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

The Google Cloud console lists all deny policies that apply to that project, folder, or organization. This includes deny policies that have been inherited from other resources. For more information about deny policy inheritance, see [Deny policy inheritance](https://docs.cloud.google.com/iam/docs/deny-overview#inheritance).




### gcloud

To list the deny policies for a resource, run the [`gcloud iam policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/list) command:
    
    
    gcloud iam policies list \
        --attachment-point=ATTACHMENT_POINT \
        --kind=denypolicies \
        --format=json

Provide the following value:

  * `ATTACHMENT_POINT`: An identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).




For example, the following command lists deny policies attached to an organization whose numeric ID is `123456789012`:
    
    
    gcloud iam policies list \
        --attachment-point=cloudresourcemanager.googleapis.com/organizations/123456789012 \
        --kind=denypolicies \
        --format=json
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    	"cloud.google.com/go/iam/apiv2/iampb"
    	"google.golang.org/api/iterator"
    )
    
    // listDenyPolicies lists all the deny policies that are attached to a resource.
    // A resource can have up to 5 deny policies.
    func listDenyPolicies(w io.Writer, projectID string) error {
    	// projectID := "your_project_id"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	req := &iampb.ListPoliciesRequest{
    		// Construct the full path of the resource's deny policies.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies"
    		Parent: fmt.Sprintf("policies/%s/denypolicies", attachmentPoint),
    	}
    	it := policiesClient.ListPolicies(ctx, req)
    	fmt.Fprintf(w, "Policies found in project %s:\n", projectID)
    
    	for {
    		policy, err := it.[Next](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PolicyIterator_Next)()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return err
    		}
    		fmt.Fprintf(w, "- %s\n", policy.GetName())
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    
    public class ListDenyPolicies {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        listDenyPolicies(projectId);
      }
    
      // List all the deny policies that are attached to a resource.
      // A resource can have up to 5 deny policies.
      public static void listDenyPolicies(String projectId) throws IOException {
        // Initialize the Policies client.
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
    
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached.
          // Its format is: "policies/{attachmentPoint}/denypolicies"
          String policyParent = String.format("policies/%s/denypolicies", attachmentPoint);
    
          // Create a list request and iterate over the returned policies.
          for ([Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) policy : policiesClient.listPolicies(policyParent).iterateAll()) {
            System.out.println(policy.getName());
          }
          System.out.println("Listed all deny policies");
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    async function listDenyPolicies() {
      const request = {
        parent: `policies/${attachmentPoint}/denypolicies`,
      };
    
      const policies = await iamClient.listPoliciesAsync(request);
      for await (const policy of policies) {
        console.log(`- ${policy.name}`);
      }
    }
    
    listDenyPolicies();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    def list_deny_policy(project_id: str) -> None:
        """List all the deny policies that are attached to a resource.
    
        A resource can have up to 5 deny policies.
    
        project_id: ID or number of the Google Cloud project you want to use.
        """
    
        from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
        from google.cloud.iam_v2 import types
    
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name. Hence, replace
        # the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        request = types.[ListPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesRequest.html)()
        # Construct the full path of the resource's deny policies.
        # Its format is: "policies/{attachmentPoint}/denypolicies"
        request.parent = f"policies/{attachment_point}/denypolicies"
    
        # Create a list request and iterate over the returned policies.
        policies = policies_client.[list_policies](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_list_policies)(request=request)
    
        for policy in policies:
            print(policy.name)
        print("Listed all deny policies")
    
    
    if __name__ == "__main__":
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
    
        list_deny_policy(PROJECT_ID)

### REST

The `[policies.listPolicies](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies)` method lists the deny policies for a resource. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 




HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/listPolicies). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "policies": [
        {
          "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1067607927478/denypolicies/test-policy",
          "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
          "kind": "DenyPolicy",
          "displayName": "My deny policy.",
          "createTime": "2022-06-28T19:06:12.455151Z",
          "updateTime": "2022-06-28T22:26:21.968687Z"
        },
        {
          "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1067607927478/denypolicies/test-policy-2",
          "uid": "8465d710-ea20-0a08-d92c-b2a3ebf766ab",
          "kind": "DenyPolicy",
          "displayName": "My second deny policy.",
          "createTime": "2022-06-05T19:21:53.595455Z",
          "updateTime": "2022-06-05T19:21:53.595455Z"
        },
        {
          "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1067607927478/denypolicies/test-policy-3",
          "uid": "ee9f7c2f-7e8c-b05c-d4e5-e03bfb2954e0",
          "kind": "DenyPolicy",
          "displayName": "My third deny policy.",
          "createTime": "2022-06-05T19:22:26.770543Z",
          "updateTime": "2022-06-05T19:22:26.770543Z"
        }
      ]
    }
    
    

## View a deny policy

You can view a deny policy to see the deny rules that it contains, including the permissions that are denied and the principals who cannot use those permissions.

### Console

  1. In the Google Cloud console, go to the **Deny** tab on the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam/deny?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. In the **Policy ID** column, click the ID of the policy that you want to view.

The Google Cloud console shows the details of the deny policy, including the policy ID, when the policy was created, and the deny rules in the deny policy.




### gcloud

To get the deny policy for a resource, run the [`gcloud iam policies get`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/get) command:
    
    
    gcloud iam policies get POLICY_ID \
        --attachment-point=ATTACHMENT_POINT \
        --kind=denypolicies \
        --format=json

Provide the following values:

  * `POLICY_ID`: The identifier for the deny policy.

  * `ATTACHMENT_POINT`: An identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).




For example, the following command gets the deny policy named `my-deny-policy` for the project `my-project` and saves it in a file named `policy.json`:
    
    
    gcloud iam policies get my-deny-policy \
        --attachment-point=cloudresourcemanager.googleapis.com/projects/my-project \
        --kind=denypolicies \
        --format=json \
        > ./policy.json
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    	"cloud.google.com/go/iam/apiv2/iampb"
    )
    
    // getDenyPolicy retrieves the deny policy given the project ID and policy ID.
    func getDenyPolicy(w io.Writer, projectID, policyID string) error {
    	// projectID := "your_project_id"
    	// policyID := "your_policy_id"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	req := &iampb.GetPolicyRequest{
    		// Construct the full path of the policy.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies/POLICY_ID"
    		Name: fmt.Sprintf("policies/%s/denypolicies/%s", attachmentPoint, policyID),
    	}
    	policy, err := policiesClient.GetPolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get policy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Policy %s retrieved\n", policy.GetName())
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.iam.v2.[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.GetPolicyRequest.html);
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    
    public class GetDenyPolicy {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // Specify the ID of the deny policy you want to retrieve.
        String policyId = "deny-policy-id";
    
        getDenyPolicy(projectId, policyId);
      }
    
      // Retrieve the deny policy given the project ID and policy ID.
      public static void getDenyPolicy(String projectId, String policyId) throws IOException {
        // Create the IAM Policies client.
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
    
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached.
          // Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
          String policyParent = String.format("policies/%s/denypolicies/%s", attachmentPoint, policyId);
    
          // Specify the policyParent and execute the GetPolicy request.
          [GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.GetPolicyRequest.html) getPolicyRequest =
              [GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.GetPolicyRequest.html).newBuilder().setName(policyParent).build();
    
          [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) policy = policiesClient.getPolicy(getPolicyRequest);
          System.out.printf("Retrieved the deny policy: %s : %s%n", policyId, policy);
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const policyID = 'YOUR_POLICY_ID';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    async function getDenyPolicy() {
      const request = {
        name: `policies/${attachmentPoint}/denypolicies/${policyId}`,
      };
    
      const [policy] = await iamClient.getPolicy(request);
    
      console.log(`Retrieved the deny policy: ${policy.name}`);
    }
    
    getDenyPolicy();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
    from google.cloud.iam_v2 import [Policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy.html), types
    
    
    def get_deny_policy(project_id: str, policy_id: str) -> Policy:
        """Retrieve the deny policy given the project ID and policy ID.
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy_id: The ID of the deny policy you want to retrieve.
        """
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name. Hence, replace
        # the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        request = types.[GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.GetPolicyRequest.html)()
        # Construct the full path of the policy.
        # Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
        request.name = f"policies/{attachment_point}/denypolicies/{policy_id}"
    
        # Execute the GetPolicy request.
        policy = policies_client.[get_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_get_policy)(request=request)
        print(f"Retrieved the deny policy: {policy_id} : {policy}")
        return policy
    
    
    if __name__ == "__main__":
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
    
        policy = get_deny_policy(PROJECT_ID, policy_id)

### REST

The `[policies.get](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/get)` method gets a deny policy for a resource. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 

  * `POLICY_ID`: An identifier for the deny policy. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
      "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
      "kind": "DenyPolicy",
      "displayName": "My deny policy.",
      "etag": "MTc3NDU4MjM4OTY0MzU5MjQ5OTI=",
      "createTime": "2022-06-05T19:22:26.770543Z",
      "updateTime": "2022-06-05T19:22:26.770543Z",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principal://goog/subject/lucian@example.com"
            ],
            "deniedPermissions": [
              "iam.googleapis.com/roles.create"
            ]
          }
        }
      ]
    }
    

**Note:** When you use an email alias in a deny policy, IAM automatically replaces the alias with the user's primary email address. 

## Update a deny policy

After you create a deny policy, you can update the deny rules that it contains, as well as its display name.

You can update a deny policy using the Google Cloud console, or using one of the following programmatic methods:

  * The gcloud CLI
  * The REST API
  * The IAM client libraries



### Update a deny policy using the Google Cloud console

  1. In the Google Cloud console, go to the **Deny** tab on the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam/deny?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. In the **Policy ID** column, click the ID of the policy that you want to edit.

  4. Click edit **Edit**.

  5. Update the deny policy:

     * To change the policy display name, edit the **Display name** field.
     * To edit an existing deny rule, click the deny rule, and then modify the rule's principals, exception principals, denied permissions, exception permissions, or denial condition.
     * To remove a deny rule, find the deny rule that you want to delete, and then click delete **Delete** in that row.
     * To add a deny rule, click **Add deny rule** , and then create a deny rule like you do when you create a deny policy.
  6. When you're done updating the deny policy, click **Save**.




### Update a deny policy programmatically

To update a deny policy using the gcloud CLI, the REST API, or the IAM client libraries, use the _read-modify-write_ pattern:

  1. Read the current version of the policy.
  2. Modify the information in the policy as needed.
  3. Write the updated policy.



#### Read the deny policy

### gcloud

To get the deny policy for a resource, run the [`gcloud iam policies get`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/get) command:
    
    
    gcloud iam policies get POLICY_ID \
        --attachment-point=ATTACHMENT_POINT \
        --kind=denypolicies \
        --format=json

Provide the following values:

  * `POLICY_ID`: The identifier for the deny policy.

  * `ATTACHMENT_POINT`: An identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).




For example, the following command gets the deny policy named `my-deny-policy` for the project `my-project` and saves it in a file named `policy.json`:
    
    
    gcloud iam policies get my-deny-policy \
        --attachment-point=cloudresourcemanager.googleapis.com/projects/my-project \
        --kind=denypolicies \
        --format=json \
        > ./policy.json
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    	"cloud.google.com/go/iam/apiv2/iampb"
    )
    
    // getDenyPolicy retrieves the deny policy given the project ID and policy ID.
    func getDenyPolicy(w io.Writer, projectID, policyID string) error {
    	// projectID := "your_project_id"
    	// policyID := "your_policy_id"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	req := &iampb.GetPolicyRequest{
    		// Construct the full path of the policy.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies/POLICY_ID"
    		Name: fmt.Sprintf("policies/%s/denypolicies/%s", attachmentPoint, policyID),
    	}
    	policy, err := policiesClient.GetPolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to get policy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Policy %s retrieved\n", policy.GetName())
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.iam.v2.[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.GetPolicyRequest.html);
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    
    public class GetDenyPolicy {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // Specify the ID of the deny policy you want to retrieve.
        String policyId = "deny-policy-id";
    
        getDenyPolicy(projectId, policyId);
      }
    
      // Retrieve the deny policy given the project ID and policy ID.
      public static void getDenyPolicy(String projectId, String policyId) throws IOException {
        // Create the IAM Policies client.
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
    
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached.
          // Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
          String policyParent = String.format("policies/%s/denypolicies/%s", attachmentPoint, policyId);
    
          // Specify the policyParent and execute the GetPolicy request.
          [GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.GetPolicyRequest.html) getPolicyRequest =
              [GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.GetPolicyRequest.html).newBuilder().setName(policyParent).build();
    
          [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) policy = policiesClient.getPolicy(getPolicyRequest);
          System.out.printf("Retrieved the deny policy: %s : %s%n", policyId, policy);
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const policyID = 'YOUR_POLICY_ID';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    async function getDenyPolicy() {
      const request = {
        name: `policies/${attachmentPoint}/denypolicies/${policyId}`,
      };
    
      const [policy] = await iamClient.getPolicy(request);
    
      console.log(`Retrieved the deny policy: ${policy.name}`);
    }
    
    getDenyPolicy();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
    from google.cloud.iam_v2 import [Policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy.html), types
    
    
    def get_deny_policy(project_id: str, policy_id: str) -> Policy:
        """Retrieve the deny policy given the project ID and policy ID.
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy_id: The ID of the deny policy you want to retrieve.
        """
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name. Hence, replace
        # the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        request = types.[GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.GetPolicyRequest.html)()
        # Construct the full path of the policy.
        # Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
        request.name = f"policies/{attachment_point}/denypolicies/{policy_id}"
    
        # Execute the GetPolicy request.
        policy = policies_client.[get_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_get_policy)(request=request)
        print(f"Retrieved the deny policy: {policy_id} : {policy}")
        return policy
    
    
    if __name__ == "__main__":
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
    
        policy = get_deny_policy(PROJECT_ID, policy_id)

### REST

The `[policies.get](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/get)` method gets a deny policy for a resource. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 

  * `POLICY_ID`: An identifier for the deny policy. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
      "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
      "kind": "DenyPolicy",
      "displayName": "My deny policy.",
      "etag": "MTc3NDU4MjM4OTY0MzU5MjQ5OTI=",
      "createTime": "2022-06-05T19:22:26.770543Z",
      "updateTime": "2022-06-05T19:22:26.770543Z",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principal://goog/subject/lucian@example.com"
            ],
            "deniedPermissions": [
              "iam.googleapis.com/roles.create"
            ]
          }
        }
      ]
    }
    

#### Modify the deny policy

To modify the deny policy, you make changes to the copy of the policy that you previously read from IAM. You can update the display name, or you can add, change, or remove deny rules. The changes don't take effect until you write the updated policy.

**Note:** In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

For example, you could add a permission to an existing deny rule:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
      "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
      "kind": "DenyPolicy",
      "displayName": "My deny policy.",
      "etag": "MTc3NDU4MjM4OTY0MzU5MjQ5OTI=",
      "createTime": "2021-10-05T19:22:26.770543Z",
      "updateTime": "2021-10-05T19:22:26.770543Z",
      "rules": [
        {
          "denyRule": {
            "deniedPrincipals": [
              "principal://goog/subject/lucian@example.com"
            ],
            "deniedPermissions": [
              "iam.googleapis.com/roles.create",
              **"iam.googleapis.com/roles.delete"**
            ]
          }
        }
      ]
    }

#### Write the updated deny policy

After you modify the deny policy locally, you must write the updated deny policy to IAM.

Each deny policy contains an `etag` field that identifies the policy version. The `etag` changes each time you update the policy. When you write the updated policy, the `etag` in your request must match the current `etag` stored in IAM; if the values do not match, the request fails. This feature helps prevent concurrent changes from overwriting each other.

### gcloud

To update the deny policy for a resource, run the [`gcloud iam policies update`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/update) command:
    
    
    gcloud iam policies update POLICY_ID \
        --attachment-point=ATTACHMENT_POINT \
        --kind=denypolicies \
        --policy-file=POLICY_FILE

Provide the following values:

  * `POLICY_ID`: The identifier for the deny policy.

  * `ATTACHMENT_POINT`: An identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).

  * `POLICY_FILE`: The filepath for the JSON file that contains the deny policy.




By default, if this command succeeds, it does not print any output. To print a detailed response, add the flag `--format=json` to the command.

For example, the following command updates a deny policy named `my-deny-policy` for the project `my-project`, using a file named `policy.json`:
    
    
    gcloud iam policies update my-deny-policy \
        --attachment-point=cloudresourcemanager.googleapis.com/projects/my-project \
        --kind=denypolicies \
        --policy-file=policy.json
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    
    	"cloud.google.com/go/iam/apiv2/iampb"
    	"google.golang.org/genproto/googleapis/type/expr"
    )
    
    // updateDenyPolicy updates the deny rules and/ or its display name after policy creation.
    func updateDenyPolicy(w io.Writer, projectID, policyID, etag string) error {
    	// projectID := "your_project_id"
    	// policyID := "your_policy_id"
    	// etag := "your_etag"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	denyRule := &iampb.DenyRule{
    		// Add one or more principals who should be denied the permissions specified in this rule.
    		// For more information on allowed values,
    		// see: https://cloud.google.com/iam/help/deny/principal-identifiers
    		DeniedPrincipals: []string{"principalSet://goog/public:all"},
    		// Optionally, set the principals who should be exempted from the
    		// list of denied principals. For example, if you want to deny certain permissions
    		// to a group but exempt a few principals, then add those here.
    		// ExceptionPrincipals: []string{"principalSet://goog/group/project-admins@example.com"},
    		//
    		// Set the permissions to deny.
    		// The permission value is of the format: service_fqdn/resource.action
    		// For the list of supported permissions,
    		// see: https://cloud.google.com/iam/help/deny/supported-permissions
    		DeniedPermissions: []string{"cloudresourcemanager.googleapis.com/projects.delete"},
    		// Optionally, add the permissions to be exempted from this rule.
    		// Meaning, the deny rule will not be applicable to these permissions.
    		// ExceptionPermissions: []string{"cloudresourcemanager.googleapis.com/projects.create"},
    		//
    		// Set the condition which will enforce the deny rule.
    		// If this condition is true, the deny rule will be applicable.
    		// Else, the rule will not be enforced.
    		// The expression uses Common Expression Language syntax (CEL).
    		// Here we block access based on tags.
    		//
    		// Here, we create a deny rule that denies the
    		// cloudresourcemanager.googleapis.com/projects.delete permission
    		// to everyone except project-admins@example.com for resources that are tagged prod.
    		// A tag is a key-value pair that can be attached to an organization, folder, or project.
    		// For more info, see: https://cloud.google.com/iam/docs/deny-access#create-deny-policy
    		DenialCondition: &expr.Expr{
    			Expression: "!resource.matchTag('12345678/env', 'prod')",
    		},
    	}
    
    	// Set the rule description and deny rule to update.
    	policyRule := &iampb.PolicyRule{
    		Description: "block all principals from deleting projects, unless the principal is a member of project-admins@example.com and the project being deleted has a tag with the value prod",
    		Kind: &iampb.PolicyRule_DenyRule{
    			DenyRule: denyRule,
    		},
    	}
    
    	// Set the policy resource path, version (etag) and the updated deny rules.
    	policy := &iampb.Policy{
    		// Construct the full path of the policy.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies/POLICY_ID"
    		Name:  fmt.Sprintf("policies/%s/denypolicies/%s", attachmentPoint, policyID),
    		Etag:  etag,
    		Rules: [](*iampb.PolicyRule){policyRule},
    	}
    
    	// Create the update policy request.
    	req := &iampb.UpdatePolicyRequest{
    		Policy: policy,
    	}
    	op, err := policiesClient.UpdatePolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to update policy: %w", err)
    	}
    
    	policy, err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Policy %s updated\n", policy.GetName())
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.iam.v2.[DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html);
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import com.google.iam.v2.[PolicyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.html);
    import com.google.iam.v2.[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.UpdatePolicyRequest.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import com.google.type.[Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdateDenyPolicy {
    
      public static void main(String[] args)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // Specify the ID of the Deny policy you want to retrieve.
        String policyId = "deny-policy-id";
    
        // Etag field that identifies the policy version. The etag changes each time
        // you update the policy. Get the etag of an existing policy by performing a GetPolicy request.
        String etag = "policy_etag";
    
        updateDenyPolicy(projectId, policyId, etag);
      }
    
      // Update the deny rules and/ or its display name after policy creation.
      public static void updateDenyPolicy(String projectId, String policyId, String etag)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
    
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
    
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached to.
          // Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
          String policyParent = String.format("policies/%s/denypolicies/%s", attachmentPoint, policyId);
    
          [DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html) denyRule =
              [DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html).newBuilder()
                  // Add one or more principals who should be denied the permissions specified in this
                  // rule.
                  // For more information on allowed values, see:
                  // https://cloud.google.com/iam/docs/principal-identifiers
                  .[addDeniedPrincipals](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.Builder.html#com_google_iam_v2_DenyRule_Builder_addDeniedPrincipals_java_lang_String_)("principalSet://goog/public:all")
    
                  // Optionally, set the principals who should be exempted from the list of principals
                  // added in "DeniedPrincipals".
                  // Example, if you want to deny certain permissions to a group but exempt a few
                  // principals, then add those here.
                  // .addExceptionPrincipals(
                  //     "principalSet://goog/group/project-admins@example.com")
    
                  // Set the permissions to deny.
                  // The permission value is of the format: service_fqdn/resource.action
                  // For the list of supported permissions, see:
                  // https://cloud.google.com/iam/help/deny/supported-permissions
                  .[addDeniedPermissions](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.Builder.html#com_google_iam_v2_DenyRule_Builder_addDeniedPermissions_java_lang_String_)("cloudresourcemanager.googleapis.com/projects.delete")
    
                  // Add the permissions to be exempted from this rule.
                  // Meaning, the deny rule will not be applicable to these permissions.
                  // .addExceptionPermissions("cloudresourcemanager.googleapis.com/projects.get")
    
                  // Set the condition which will enforce the deny rule.
                  // If this condition is true, the deny rule will be applicable. Else, the rule will
                  // not be enforced.
                  .[setDenialCondition](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.Builder.html#com_google_iam_v2_DenyRule_Builder_setDenialCondition_com_google_type_Expr_)(
                      [Expr](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.html).newBuilder()
                          // The expression uses Common Expression Language syntax (CEL). Here we block
                          // access based on tags.
                          //
                          // A tag is a key-value pair that can be attached to an organization, folder,
                          // or project. You can use deny policies to deny permissions based on tags
                          // without adding an IAM Condition to every role grant.
                          // For example, imagine that you tag all of your projects as dev, test, or
                          // prod. You want only members of project-admins@example.com to be able to
                          // perform operations on projects that are tagged prod.
                          // To solve this problem, you create a deny rule that denies the
                          // cloudresourcemanager.googleapis.com/projects.delete permission to everyone
                          // except project-admins@example.com for resources that are tagged prod.
                          .[setExpression](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setExpression_java_lang_String_)("!resource.matchTag('12345678/env', 'prod')")
                          .[setTitle](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Expr.Builder.html#com_google_type_Expr_Builder_setTitle_java_lang_String_)("Only for prod projects")
                          .build())
                  .build();
    
          // Set the policy resource path, version (etag) and the updated deny rules.
          [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html) policy =
              [Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html).newBuilder()
                  .setName(policyParent)
                  .setEtag(etag)
                  .[addRules](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.Builder.html#com_google_iam_v2_Policy_Builder_addRules_com_google_iam_v2_PolicyRule_)(
                      [PolicyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.html).newBuilder()
                          // Set the rule description to update.
                          .setDescription(
                              "Block all principals from deleting projects, unless the principal"
                                  + " is a member of project-admins@example.com and the project"
                                  + "being deleted has a tag with the value prod")
                          // Set the deny rule to update.
                          .[setDenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.Builder.html#com_google_iam_v2_PolicyRule_Builder_setDenyRule_com_google_iam_v2_DenyRule_)(denyRule)
                          .build())
                  .build();
    
          // Create the update policy request.
          [UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.UpdatePolicyRequest.html) updatePolicyRequest =
              [UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.UpdatePolicyRequest.html).newBuilder().setPolicy(policy).build();
    
          // Wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) operation =
              policiesClient
                  .[updatePolicyCallable](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html#com_google_iam_v2_PoliciesClient_updatePolicyCallable__)()
                  .futureCall(updatePolicyRequest)
                  .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in updating the policy " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println("Updated the deny policy: " + policyId);
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const policyID = 'YOUR_POLICY_ID';
    // const etag = 'YOUR_ETAG';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    const denyRule = {
      // Add one or more principals who should be denied the permissions specified in this rule.
      // For more information on allowed values, see: https://cloud.google.com/iam/help/deny/principal-identifiers
      deniedPrincipals: ['principalSet://goog/public:all'],
      // Optionally, set the principals who should be exempted from the
      // list of denied principals. For example, if you want to deny certain permissions
      // to a group but exempt a few principals, then add those here.
      // exceptionPrincipals: ['principalSet://goog/group/project-admins@example.com'],
      // Set the permissions to deny.
      // The permission value is of the format: service_fqdn/resource.action
      // For the list of supported permissions, see: https://cloud.google.com/iam/help/deny/supported-permissions
      deniedPermissions: ['cloudresourcemanager.googleapis.com/projects.delete'],
      // Optionally, add the permissions to be exempted from this rule.
      // Meaning, the deny rule will not be applicable to these permissions.
      // exceptionPermissions: ['cloudresourcemanager.googleapis.com/projects.create']
      //
      // Set the condition which will enforce the deny rule.
      // If this condition is true, the deny rule will be applicable. Else, the rule will not be enforced.
      // The expression uses Common Expression Language syntax (CEL).
      // Here we block access based on tags.
      //
      // Here, we create a deny rule that denies the cloudresourcemanager.googleapis.com/projects.delete permission to everyone except project-admins@example.com for resources that are tagged test.
      // A tag is a key-value pair that can be attached to an organization, folder, or project.
      // For more info, see: https://cloud.google.com/iam/docs/deny-access#create-deny-policy
      denialCondition: {
        expression: '!resource.matchTag("12345678/env", "prod")',
      },
    };
    
    async function updateDenyPolicy() {
      const request = {
        policy: {
          name: `policies/${attachmentPoint}/denypolicies/${policyId}`,
          etag,
          rules: [
            {
              description:
                'block all principals from deleting projects, unless the principal is a member of project-admins@example.com and the project being deleted has a tag with the value prod',
              denyRule,
            },
          ],
        },
        policyId,
      };
    
      const [operation] = await iamClient.updatePolicy(request);
      const [policy] = await operation.promise();
    
      console.log(`Updated the deny policy: ${policy.name}`);
    }
    
    updateDenyPolicy();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    def update_deny_policy(project_id: str, policy_id: str, etag: str) -> None:
        """Update the deny rules and/ or its display name after policy creation.
    
        project_id: ID or number of the Google Cloud project you want to use.
    
        policy_id: The ID of the deny policy you want to retrieve.
    
        etag: Etag field that identifies the policy version. The etag changes each time
        you update the policy. Get the etag of an existing policy by performing a GetPolicy request.
        """
    
        from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
        from google.cloud.iam_v2 import types
    
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name.
        # Hence, replace the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        deny_rule = types.[DenyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.DenyRule.html)()
    
        # Add one or more principals who should be denied the permissions
        # specified in this rule.
        # For more information on allowed values, see:
        # https://cloud.google.com/iam/help/deny/principal-identifiers
        deny_rule.denied_principals = ["principalSet://goog/public:all"]
    
        # Optionally, set the principals who should be exempted
        # from the list of principals added in "DeniedPrincipals".
        # Example, if you want to deny certain permissions to a group
        # but exempt a few principals, then add those here.
        # deny_rule.exception_principals = ["principalSet://goog/group/project-admins@example.com"]
    
        # Set the permissions to deny.
        # The permission value is of the format: service_fqdn/resource.action
        # For the list of supported permissions, see:
        # https://cloud.google.com/iam/help/deny/supported-permissions
        deny_rule.denied_permissions = [
            "cloudresourcemanager.googleapis.com/projects.delete"
        ]
    
        # Add the permissions to be exempted from this rule.
        # Meaning, the deny rule will not be applicable to these permissions.
        # deny_rule.exception_permissions = ["cloudresourcemanager.googleapis.com/projects.get"]
    
        # Set the condition which will enforce the deny rule.
        # If this condition is true, the deny rule will be applicable.
        # Else, the rule will not be enforced.
        #
        # The expression uses Common Expression Language syntax (CEL).
        # Here we block access based on tags.
        #
        # Here, we create a deny rule that denies the
        # cloudresourcemanager.googleapis.com/projects.delete permission to everyone
        # except project-admins@example.com for resources that are tagged prod.
        # A tag is a key-value pair that can be attached
        # to an organization, folder, or project.
        # For more info, see:
        # https://cloud.google.com/iam/docs/deny-access#create-deny-policy
        deny_rule.denial_condition = {
            "expression": "!resource.matchTag('12345678/env', 'prod')"
        }
    
        # Set the rule description and deny rule to update.
        policy_rule = types.[PolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.PolicyRule.html)()
        policy_rule.description = "block all principals from deleting projects, unless the principal is a member of project-admins@example.com and the project being deleted has a tag with the value prod"
        policy_rule.deny_rule = deny_rule
    
        # Set the policy resource path, version (etag) and the updated deny rules.
        policy = types.[Policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy.html)()
        # Construct the full path of the policy.
        # Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
        policy.name = f"policies/{attachment_point}/denypolicies/{policy_id}"
        policy.etag = etag
        policy.rules = [policy_rule]
    
        # Create the update policy request.
        request = types.[UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.UpdatePolicyRequest.html)()
        request.policy = policy
    
        result = policies_client.[update_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_update_policy)(request=request).result()
        print(f"Updated the deny policy: {result.name.rsplit('/')[-1]}")
    
    
    if __name__ == "__main__":
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
        # Get the etag by performing a Get policy request.
        etag = "etag"
    
        update_deny_policy(PROJECT_ID, policy_id, etag)

### REST

The `[policies.update](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/update)` method updates a deny policy. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 

  * `POLICY_ID`: An identifier for the deny policy. 
  * `POLICY`: The updated deny policy. 

For example, to add a permission to the policy shown in the previous step, replace `POLICY` with the following: 
        
        {
          "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
          "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
          "kind": "DenyPolicy",
          "displayName": "My deny policy.",
          "etag": "MTc3NDU4MjM4OTY0MzU5MjQ5OTI=",
          "createTime": "2022-06-05T19:22:26.770543Z",
          "updateTime": "2022-06-05T19:22:26.770543Z",
          "rules": [
            {
              "denyRule": {
                "deniedPrincipals": [
                  "principal://goog/subject/lucian@example.com"
                ],
                "deniedPermissions": [
                  "iam.googleapis.com/roles.create",
                  **"iam.googleapis.com/roles.delete"**
                ]
              }
            }
          ]
        }




HTTP method and URL: 
    
    
    PUT https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID

Request JSON body: 
    
    
    POLICY
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/update). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy/operations/8b2d0ab2daf1ff01",
      "metadata": {
        "@type": "type.googleapis.com/google.iam.v2.PolicyOperationMetadata",
        "createTime": "2021-10-05T22:26:21.968687Z"
      },
      "response": {
        "@type": "type.googleapis.com/google.iam.v2.Policy",
        "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
        "uid": "6665c437-a3b2-a018-6934-54dd16d3426e",
        "kind": "DenyPolicy",
        "displayName": "My deny policy.",
        "etag": "MTgxNTIxNDE3NTYxNjQxODYxMTI=",
        "createTime": "2022-06-05T19:22:26.770543Z",
        "updateTime": "2022-06-05T22:26:21.968687Z",
        "rules": [
          {
            "denyRule": {
              "deniedPrincipals": [
                "principal://goog/subject/lucian@example.com"
              ],
              "deniedPermissions": [
                "iam.googleapis.com/roles.create",
                "iam.googleapis.com/roles.delete"
              ]
            }
          }
        ]
      }
    }
    

The response identifies a long-running operation. You can monitor the status of the long-running operation to find out when it's complete. For details, see Check the status of a long-running operation on this page. 

## Delete a deny policy

If you no longer want to enforce the rules in a deny policy, you can delete the deny policy.

**Caution:** Deleting a deny policy is permanent. You cannot undelete deny policies.

Optionally, you can specify the `etag` for the policy version that you are deleting. If you specify the `etag`, it must match the current `etag` stored by IAM; if the values do not match, the request fails. You can use this feature to ensure that you are deleting the intended policy, rather than an updated version of that policy.

If you omit the `etag` from the request, IAM deletes the policy unconditionally.

**Note:** In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

### Console

  1. In the Google Cloud console, go to the **Deny** tab on the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam/deny?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. In the **Policy ID** column, click the ID of the policy that you want to delete.

  4. Click delete **Delete**. In the confirmation dialog, click **Confirm**.




### gcloud

To delete a deny policy from a resource, run the [`gcloud iam policies delete`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/delete) command:
    
    
    gcloud iam policies delete POLICY_ID \
        --attachment-point=ATTACHMENT_POINT \
        --kind=denypolicies

Provide the following values:

  * `POLICY_ID`: The identifier for the deny policy.

  * `ATTACHMENT_POINT`: An identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point).




Optionally, you can add the flag `--etag=ETAG`. Replace `ETAG` with the current `etag` value for the deny policy.

By default, if this command succeeds, it does not print any output. To print a detailed response, add the flag `--format=json` to the command.

For example, the following command deletes a deny policy named `my-deny-policy` from the project `my-project`:
    
    
    gcloud iam policies delete my-deny-policy \
        --attachment-point=cloudresourcemanager.googleapis.com/projects/my-project \
        --kind=denypolicies
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "cloud.google.com/go/iam/apiv2"
    
    	"cloud.google.com/go/iam/apiv2/iampb"
    )
    
    // deleteDenyPolicy deletes the policy if you no longer want to enforce the rules in a deny policy.
    func deleteDenyPolicy(w io.Writer, projectID, policyID string) error {
    	// projectID := "your_project_id"
    	// policyID := "your_policy_id"
    
    	ctx := context.Background()
    	policiesClient, err := iam.NewPoliciesClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewPoliciesClient: %w", err)
    	}
    	defer policiesClient.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/apiv2.html#cloud_google_com_go_iam_apiv2_PoliciesClient_Close)()
    
    	// Each deny policy is attached to an organization, folder, or project.
    	// To work with deny policies, specify the attachment point.
    	//
    	// Its format can be one of the following:
    	// 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    	// 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    	// 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    	//
    	// The attachment point is identified by its URL-encoded resource name. Hence, replace
    	// the "/" with "%%2F".
    	attachmentPoint := fmt.Sprintf(
    		"cloudresourcemanager.googleapis.com%%2Fprojects%%2F%s",
    		projectID,
    	)
    
    	req := &iampb.DeletePolicyRequest{
    		// Construct the full path of the policy.
    		// Its format is: "policies/ATTACHMENT_POINT/denypolicies/POLICY_ID"
    		Name: fmt.Sprintf("policies/%s/denypolicies/%s", attachmentPoint, policyID),
    	}
    	op, err := policiesClient.DeletePolicy(ctx, req)
    	if err != nil {
    		return fmt.Errorf("unable to delete policy: %w", err)
    	}
    
    	policy, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("unable to wait for the operation: %w", err)
    	}
    
    	fmt.Fprintf(w, "Policy %s deleted\n", policy.GetName())
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v2). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.iam.v2.[DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DeletePolicyRequest.html);
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html);
    import java.io.IOException;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteDenyPolicy {
    
      public static void main(String[] args)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        // TODO(developer): Replace these variables before running the sample.
    
        // ID or number of the Google Cloud project you want to use.
        String projectId = "your-google-cloud-project-id";
    
        // Specify the ID of the deny policy you want to retrieve.
        String policyId = "deny-policy-id";
    
        deleteDenyPolicy(projectId, policyId);
      }
    
      // Delete the policy if you no longer want to enforce the rules in a deny policy.
      public static void deleteDenyPolicy(String projectId, String policyId)
          throws IOException, InterruptedException, ExecutionException, TimeoutException {
        try ([PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html) policiesClient = [PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html).create()) {
    
          // Each deny policy is attached to an organization, folder, or project.
          // To work with deny policies, specify the attachment point.
          //
          // Its format can be one of the following:
          // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
          // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
          // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
          //
          // The attachment point is identified by its URL-encoded resource name.
          String urlEncodedResource =
              URLEncoder.encode(
                  "cloudresourcemanager.googleapis.com/projects/", StandardCharsets.UTF_8);
          String attachmentPoint = String.format("%s%s", urlEncodedResource, projectId);
    
          // Construct the full path of the resource to which the policy is attached.
          // Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
          String policyParent = String.format("policies/%s/denypolicies/%s", attachmentPoint, policyId);
    
          // Create the DeletePolicy request.
          [DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DeletePolicyRequest.html) deletePolicyRequest =
              [DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DeletePolicyRequest.html).newBuilder().setName(policyParent).build();
    
          // Delete the policy and wait for the operation to complete.
          [Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html) operation =
              policiesClient
                  .[deletePolicyCallable](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html#com_google_iam_v2_PoliciesClient_deletePolicyCallable__)()
                  .futureCall(deletePolicyRequest)
                  .get(3, TimeUnit.MINUTES);
    
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in deleting the policy " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
            return;
          }
    
          System.out.println("Deleted the deny policy: " + policyId);
        }
      }
    }

### Node.js

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    /**
     * TODO(developer): Uncomment and replace these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const policyID = 'YOUR_POLICY_ID';
    
    const {PoliciesClient} = require('[@google-cloud/iam](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)').v2;
    
    const iamClient = new [PoliciesClient](https://docs.cloud.google.com/nodejs/docs/reference/iam/latest/overview.html)();
    
    // Each deny policy is attached to an organization, folder, or project.
    // To work with deny policies, specify the attachment point.
    //
    // Its format can be one of the following:
    // 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
    // 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
    // 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
    //
    // The attachment point is identified by its URL-encoded resource name. Hence, replace
    // the "/" with "%2F".
    const attachmentPoint = `cloudresourcemanager.googleapis.com%2Fprojects%2F${projectId}`;
    
    async function deleteDenyPolicy() {
      const request = {
        name: `policies/${attachmentPoint}/denypolicies/${policyId}`,
      };
    
      const [operation] = await iamClient.deletePolicy(request);
      const [policy] = await operation.promise();
    
      console.log(`Deleted the deny policy: ${policy.name}`);
    }
    
    deleteDenyPolicy();

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    def delete_deny_policy(project_id: str, policy_id: str) -> None:
        """Delete the policy if you no longer want to enforce the rules in a deny policy.
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy_id: The ID of the deny policy you want to retrieve.
        """
    
        from google.cloud import [iam](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.html)_v2
        from google.cloud.iam_v2 import types
    
        policies_client = iam_v2.[PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html)()
    
        # Each deny policy is attached to an organization, folder, or project.
        # To work with deny policies, specify the attachment point.
        #
        # Its format can be one of the following:
        # 1. cloudresourcemanager.googleapis.com/organizations/ORG_ID
        # 2. cloudresourcemanager.googleapis.com/folders/FOLDER_ID
        # 3. cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        #
        # The attachment point is identified by its URL-encoded resource name. Hence, replace
        # the "/" with "%2F".
        attachment_point = f"cloudresourcemanager.googleapis.com%2Fprojects%2F{project_id}"
    
        request = types.[DeletePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.DeletePolicyRequest.html)()
        # Construct the full path of the policy.
        # Its format is: "policies/{attachmentPoint}/denypolicies/{policyId}"
        request.name = f"policies/{attachment_point}/denypolicies/{policy_id}"
    
        # Create the DeletePolicy request.
        result = policies_client.[delete_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient.html#google_cloud_iam_v2_services_policies_PoliciesClient_delete_policy)(request=request).result()
        print(f"Deleted the deny policy: {result.name.rsplit('/')[-1]}")
    
    
    if __name__ == "__main__":
        import uuid
    
        # Your Google Cloud project ID.
        PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-google-cloud-project-id")
    
        # Any unique ID (0 to 63 chars) starting with a lowercase letter.
        policy_id = f"deny-{uuid.uuid4()}"
    
        delete_deny_policy(PROJECT_ID, policy_id)

### REST

The `[policies.delete](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/delete)` method deletes a deny policy from a resource. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 

  * `POLICY_ID`: An identifier for the deny policy. 
  * `ETAG`: Optional. An identifier for the version of the policy. If present, this value must match the current `etag` value for the policy. 



HTTP method and URL: 
    
    
    DELETE https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID?etag=ETAG

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID?etag=ETAG"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/denypolicies/POLICY_ID?etag=ETAG" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy/operations/8223fe308bf1ff01",
      "metadata": {
        "@type": "type.googleapis.com/google.iam.v2.PolicyOperationMetadata",
        "createTime": "2021-10-05T19:45:00.133311Z"
      },
      "response": {
        "@type": "type.googleapis.com/google.iam.v2.Policy",
        "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy",
        "kind": "DenyPolicy",
        "displayName": "My deny policy.",
        "etag": "MTc3NDU4MjM4OTY0MzU5MjQ5OTI=",
        "createTime": "2022-06-28T19:06:12.455151Z",
        "updateTime": "2022-07-05T19:45:00.133311Z",
        "deleteTime": "2022-07-05T19:45:00.133311Z",
        "rules": [
          {
            "denyRule": {
              "deniedPrincipals": [
                "principal://goog/subject/lucian@example.com"
              ],
              "deniedPermissions": [
                "iam.googleapis.com/roles.create"
              ]
            }
          }
        ]
      }
    }
    

The response identifies a long-running operation. You can monitor the status of the long-running operation to find out when it's complete. For details, see Check the status of a long-running operation on this page. 

## Check the status of a long-running operation

When you use the REST API or the client libraries, any method that changes a deny policy returns a long-running operation, or LRO. The long-running operation tracks the status of the request and indicates whether the change to the policy is complete.

**Note:** If you use the gcloud CLI, you can see the long-running operation by running a command with the `--format=json` flag. However, you must use the REST API or the client libraries to get the operation's status.

### Go

The code samples on this page show how to wait for a long-running operation to finish, and then access its result.

### Java

The code samples on this page show how to wait for a long-running operation to finish, and then access its result.

### Node.js

The code samples on this page show how to wait for a long-running operation to finish, and then access its result.

### Python

The code samples on this page show how to wait for a long-running operation to finish, and then access its result.

### REST

The `[policies.operations.get](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies.operations/get)` method returns the status of a long-running operation. 

Before using any of the request data, make the following replacements: 

  * `ENCODED_ATTACHMENT_POINT`: A URL-encoded identifier for the resource that the deny policy is attached to. To learn how to format this value, see [Attachment point](https://docs.cloud.google.com/iam/docs/deny-overview#attachment-point). 

  * `OPERATION_ID`: The identifier for the operation. You receive this identifier in the response to your original request, as part of the operation name. Use the hexadecimal value at the end of the operation name. For example, `89cb3e508bf1ff01`. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/operations/OPERATION_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/operations/OPERATION_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v2/policies/ENCODED_ATTACHMENT_POINT/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v2/policies.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "policies/cloudresourcemanager.googleapis.com%2Fprojects%2F1234567890123/denypolicies/my-policy/operations/89cb3e508bf1ff01",
      "done": true
    }
    

If the operation's `done` field is not present, continue to monitor its status by getting the operation repeatedly. Use [truncated exponential backoff](https://docs.cloud.google.com/iam/docs/retry-strategy#algorithm) to introduce a delay between each request. When the `done` field is set to `true`, the operation is complete, and you can stop getting the operation.

## What's next

  * Identify the [permissions that are supported in deny policies](https://docs.cloud.google.com/iam/docs/deny-permissions-support).
  * Get the format of [principal identifiers in deny policies](https://docs.cloud.google.com/iam/docs/principal-identifiers#deny).
  * Find out how to [troubleshoot access issues with deny policies](https://docs.cloud.google.com/iam/docs/troubleshoot-policies).
  * Learn more about [denying access to principals](https://docs.cloud.google.com/iam/docs/deny-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
