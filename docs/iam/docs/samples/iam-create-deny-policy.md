---
url: https://docs.cloud.google.com/iam/docs/samples/iam-create-deny-policy/
title: Create a deny policy \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:47.715706+00:00
---

# Create a deny policy  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-create-deny-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Create a deny policy Stay organized with collections  Save and categorize content based on your preferences. 

Creates a deny policy based on the configuration provided.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deny access to resources](https://docs.cloud.google.com/iam/docs/deny-access)



## Code sample

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.iam.v2.[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.CreatePolicyRequest.html);
    import com.google.iam.v2.[DenyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.DenyRule.html);
    import com.google.iam.v2.[PoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html);
    import com.google.iam.v2.[Policy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.Policy.html);
    import com.google.iam.v2.[PolicyRule](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PolicyRule.html);
    import com.google.longrunning.[Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html);
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
          [Operation](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html) operation =
              policiesClient
                  .[createPolicyCallable](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v2.PoliciesClient.html#com_google_iam_v2_PoliciesClient_createPolicyCallable__)()
                  .futureCall(createPolicyRequest)
                  .get(3, TimeUnit.MINUTES);
    
          // Wait for the operation to complete.
          if (operation.[hasError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_hasError__)()) {
            System.out.println("Error in creating the policy " + operation.[getError](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.longrunning.Operation.html#com_google_longrunning_Operation_getError__)());
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

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Node.js API reference documentation](https://googleapis.dev/nodejs/googleapis/latest/iam/index.html). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
